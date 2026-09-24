#!/usr/bin/env python3
"""
bib2yaml.py -- turn files/uvilla.bib into _data/publications.yml

Zero dependencies (Python 3.8+ standard library only), so it runs anywhere.

Usage:
    python3 scripts/bib2yaml.py                 # bib -> _data/publications.yml
    python3 scripts/bib2yaml.py --check         # report problems, write nothing
    python3 scripts/bib2yaml.py --bib X --out Y

Topic assignment:
    Topics come from the non-standard `classification` field in the .bib --
    one or more comma-separated slugs from TOPICS below:

        @article{MyCiteKey2026,
          ...
          classification = {pact, dlirm}
        }

    An entry with no `classification` gets no topics: it still appears in the
    publication list, but only under the "All" filter. Run with --check to
    list unclassified entries and any unrecognised slugs.
"""

import argparse
import os
import re
import sys
import unicodedata
from collections import OrderedDict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

DEFAULT_BIB = os.path.join(ROOT, "files", "uvilla.bib")
DEFAULT_OUT = os.path.join(ROOT, "_data", "publications.yml")

# The author whose name gets highlighted, and the spellings that mean "me".
ME_DISPLAY = "Umberto Villa"
ME_PATTERNS = [
    ("villa", "u"),  # family startswith, given startswith
]

# ---------------------------------------------------------------------------
# Topics
#
# The slugs here are the vocabulary of the `classification` field in the .bib.
# Order determines the order of the filter chips on the publications page.
# ---------------------------------------------------------------------------

TOPICS = OrderedDict([
    ("pact", "Photoacoustic Computed Tomography"),
    ("usct", "Ultrasound Computed Tomography"),
    ("iqa", "Image quality assessment"),
    ("dlirm", "Deep learning-based image reconstruction"),
    ("ipuq", "Inverse problems, Uncertainty Quantification, Digital Twins"),
    ("amg", "Preconditioners, Multigrid and numerical upscaling"),
    ("cfd", "Computational Fluid Dynamics"),
    ("health", "Data Science for Public Health"),
])

# ---------------------------------------------------------------------------
# LaTeX -> Unicode
# ---------------------------------------------------------------------------

ACCENTS = {
    "'": "\u0301", "`": "\u0300", '"': "\u0308", "^": "\u0302", "~": "\u0303",
    "=": "\u0304", ".": "\u0307", "u": "\u0306", "v": "\u030c", "H": "\u030b",
    "c": "\u0327", "k": "\u0328", "r": "\u030a", "d": "\u0323", "b": "\u0331",
}

SPECIALS = {
    r"\ss": "\u00df", r"\aa": "\u00e5", r"\AA": "\u00c5", r"\ae": "\u00e6",
    r"\AE": "\u00c6", r"\oe": "\u0153", r"\OE": "\u0152", r"\o": "\u00f8",
    r"\O": "\u00d8", r"\l": "\u0142", r"\L": "\u0141", r"\i": "i", r"\j": "j",
    r"\&": "&", r"\%": "%", r"\$": "$", r"\#": "#", r"\_": "_",
    r"\textendash": "\u2013", r"\textemdash": "\u2014",
    r"\ldots": "\u2026", r"\dots": "\u2026",
}


def latex_to_unicode(s):
    if not s:
        return s
    # \'{e}  \'e  \"{o}  \c{c}  {\'e}  {\"{u}}
    def accent_sub(m):
        acc, body = m.group(1), m.group(2)
        body = body.strip("{}")
        if not body:
            return ""
        comb = ACCENTS.get(acc)
        if comb is None:
            return body
        return unicodedata.normalize("NFC", body[0] + comb + body[1:])

    # Dotless i/j only exist to carry an accent -- fold them first so that
    # forms like Mac{\'\i}as are seen by the accent pass below.
    s = re.sub(r"\\i(?![A-Za-z])", "i", s)
    s = re.sub(r"\\j(?![A-Za-z])", "j", s)

    pattern = r"\\([`'\"^~=.uvHckrdb])\s*\{([^{}]*)\}|\\([`'\"^~=.])\s*\{?([A-Za-z])\}?"
    def _sub(m):
        if m.group(1) is not None:
            return accent_sub(m)
        comb = ACCENTS.get(m.group(3))
        ch = m.group(4)
        return unicodedata.normalize("NFC", ch + comb) if comb else ch
    prev = None
    while prev != s:
        prev = s
        s = re.sub(pattern, _sub, s)

    for k, v in SPECIALS.items():
        s = re.sub(re.escape(k) + r"(?![A-Za-z])", v, s)

    s = re.sub(r"\\(?:text(?:it|bf|rm|sf|tt)|emph|mbox|ensuremath)\s*\{([^{}]*)\}", r"\1", s)
    s = s.replace("$", "").replace("\\&", "&")
    s = s.replace("~", " ")
    s = re.sub(r"\\[A-Za-z]+\s*", "", s)
    s = s.replace("{", "").replace("}", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s


# ---------------------------------------------------------------------------
# BibTeX parsing
# ---------------------------------------------------------------------------

MONTHS = {m: i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun",
     "jul", "aug", "sep", "oct", "nov", "dec"])}


def strip_comments(text):
    """Drop % comments that are not inside a brace-delimited value."""
    out = []
    depth = 0
    in_quote = False
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c == "\\" and i + 1 < n:
            out.append(text[i:i + 2])
            i += 2
            continue
        if c == '"' and depth > 0:
            in_quote = not in_quote
        elif c == "{":
            depth += 1
        elif c == "}":
            depth = max(0, depth - 1)
        elif c == "%" and depth == 0 and not in_quote:
            j = text.find("\n", i)
            i = n if j == -1 else j
            continue
        out.append(c)
        i += 1
    return "".join(out)


def parse_bib(text):
    """Return a list of (entrytype, citekey, {field: rawvalue})."""
    text = strip_comments(text)
    entries = []
    for m in re.finditer(r"@(\w+)\s*\{", text):
        etype = m.group(1).lower()
        if etype in ("comment", "preamble", "string"):
            continue
        start = m.end()
        depth = 1
        i = start
        while i < len(text) and depth:
            if text[i] == "\\":
                i += 2
                continue
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
            i += 1
        body = text[start:i - 1]
        key, _, rest = body.partition(",")
        entries.append((etype, key.strip(), parse_fields(rest)))
    return entries


def parse_fields(body):
    fields = {}
    i, n = 0, len(body)
    while i < n:
        m = re.compile(r"\s*([A-Za-z][A-Za-z0-9_\-]*)\s*=\s*").match(body, i)
        if not m:
            j = body.find(",", i)
            if j == -1:
                break
            i = j + 1
            continue
        name = m.group(1).lower()
        i = m.end()
        if i >= n:
            break
        if body[i] == "{":
            depth, j = 1, i + 1
            while j < n and depth:
                if body[j] == "\\":
                    j += 2
                    continue
                if body[j] == "{":
                    depth += 1
                elif body[j] == "}":
                    depth -= 1
                j += 1
            value = body[i + 1:j - 1]
            i = j
        elif body[i] == '"':
            j = i + 1
            while j < n and body[j] != '"':
                if body[j] == "\\":
                    j += 1
                j += 1
            value = body[i + 1:j]
            i = j + 1
        else:
            j = i
            while j < n and body[j] != ",":
                j += 1
            value = body[i:j]
            i = j
        fields[name] = re.sub(r"\s+", " ", value).strip()
        j = body.find(",", i)
        if j == -1:
            break
        i = j + 1
    return fields


# ---------------------------------------------------------------------------
# Normalisation
# ---------------------------------------------------------------------------

def split_authors(raw):
    if not raw:
        return []
    raw = raw.replace("\n", " ")
    parts = re.split(r"\s+and\s+(?![^{]*\})", raw)
    return [p.strip().strip(",") for p in parts if p.strip()]


SUFFIXES = {"jr", "jr.", "sr", "sr.", "ii", "iii", "iv"}


def format_author(raw):
    """Return a 'Given Family [Suffix]' display string."""
    raw = latex_to_unicode(raw)
    raw = re.sub(r"\s+", " ", raw).strip()
    if not raw:
        return ""
    if "," in raw:
        bits = [b.strip() for b in raw.split(",") if b.strip()]
        family = bits[0]
        given = " ".join(bits[1:]).strip()
    else:
        toks = raw.split()
        if len(toks) == 1:
            return toks[0]
        # Treat trailing lowercase particles (van, de, ...) as part of family.
        k = len(toks) - 1
        while k > 1 and toks[k - 1][:1].islower():
            k -= 1
        family = " ".join(toks[k:])
        given = " ".join(toks[:k])

    # Generational suffixes belong after the family name, not inside the
    # given names: "Hormuth, David A. II" -> "David A. Hormuth II".
    suffix = ""
    for bucket in ("given", "family"):
        words = (given if bucket == "given" else family).split()
        while words and words[-1].lower().rstrip(".") in {s.rstrip(".") for s in SUFFIXES}:
            suffix = words.pop() + (" " + suffix if suffix else "")
        if bucket == "given":
            given = " ".join(words)
        else:
            family = " ".join(words)

    name = " ".join(x for x in (given, family, suffix) if x)
    return re.sub(r"\s+", " ", name).strip()


def _given_family(display):
    toks = display.split()
    if len(toks) < 2:
        return "", display
    suffix = ""
    if toks[-1].lower().rstrip(".") in {s.rstrip(".") for s in SUFFIXES}:
        suffix = toks.pop()
    k = len(toks) - 1
    while k > 1 and toks[k - 1][:1].islower():
        k -= 1
    return " ".join(toks[:k]), " ".join(toks[k:]) + ((" " + suffix) if suffix else "")


def canonicalize_authors(records):
    """Collapse spellings of the same co-author to the most complete form.

    "M. A. Anastasio", "Mark Anastasio" and "Mark A. Anastasio" all become the
    longest compatible form. Two spellings are merged only when one's sequence
    of given-name initials is a prefix of the other's and every fully spelled
    given name they share agrees.
    """
    def fold(s):
        """Lowercase and strip accents, so Noemi and Noémi compare equal."""
        d = unicodedata.normalize("NFD", s)
        return "".join(c for c in d if not unicodedata.combining(c)).lower()

    seen = {}
    for r in records:
        for a in r["authors"]:
            given, family = _given_family(a)
            if not given:
                continue
            seen.setdefault(fold(family), {}).setdefault(a, 0)
            seen[fold(family)][a] += 1

    def compatible(short, long_):
        """True if `short` is an abbreviated spelling of `long_`."""
        gs = _given_family(short)[0].split()
        gl = _given_family(long_)[0].split()
        if len(gs) > len(gl):
            return False
        for i, tok in enumerate(gs):
            a, b = fold(tok.rstrip(".")), fold(gl[i].rstrip("."))
            if len(a) == 1 or len(b) == 1:
                if a[:1] != b[:1]:
                    return False
            elif a != b:
                return False
        return True

    def rank(s):
        # Most fully spelled wins; on a tie prefer the accented spelling.
        letters = len(re.sub(r"[^^\w]", "", s, flags=re.UNICODE))
        accents = sum(1 for c in unicodedata.normalize("NFD", s)
                      if unicodedata.combining(c))
        return (-letters, -accents, s)

    canon = {}
    for family, forms in seen.items():
        # Longest (most fully spelled) form first: it becomes the cluster head.
        ordered = sorted(forms, key=rank)
        assigned = {}
        for form in ordered:
            if form in assigned:
                continue
            assigned[form] = form
            for other in ordered:
                if other in assigned:
                    continue
                if compatible(other, form):
                    assigned[other] = form
        for variant, head in assigned.items():
            if variant != head:
                canon[variant] = head

    for r in records:
        r["authors"] = [canon.get(a, a) for a in r["authors"]]
    return canon


def is_me(display):
    low = display.lower()
    for fam, giv in ME_PATTERNS:
        if fam in low and low.split()[0].startswith(giv):
            return True
    return False


def clean_title(raw):
    t = latex_to_unicode(raw)
    t = t.rstrip(" .")
    t = re.sub(r"\s*:\s*", ": ", t)
    return t


def norm_doi(raw):
    if not raw:
        return ""
    d = raw.strip()
    d = re.sub(r"^\s*(https?://(dx\.)?doi\.org/|doi:\s*)", "", d, flags=re.I)
    return d.strip().rstrip(".")


def norm_pages(raw):
    """1--14, 1-14 and 1—14 all become an en-dashed range."""
    p = latex_to_unicode(raw).strip()
    p = p.replace("--", "–").replace("—", "–")
    p = re.sub(r"(?<=[\w])\s*-\s*(?=[\w])", "–", p)
    return p


def norm_title_key(t):
    return re.sub(r"[^a-z0-9]+", "", t.lower())


def get_year(f):
    for v in (f.get("year", ""), f.get("date", "")):
        m = re.search(r"(19|20)\d{2}", v)
        if m:
            return int(m.group(0))
    return 0


def get_month(f):
    v = f.get("month", "").strip().lower().strip("{}")
    if not v:
        return 0
    if v[:3] in MONTHS:
        return MONTHS[v[:3]]
    if v.isdigit():
        return int(v)
    return 0


def kind_of(etype, f):
    if etype in ("mastersthesis", "phdthesis"):
        return "thesis"
    if etype == "data":
        return "dataset"
    if etype in ("inproceedings", "conference", "inbook"):
        return "conference"
    if etype == "misc":
        # Anything posted to a preprint server carries an eprint id; the rest
        # of the @misc entries in this bib are software releases.
        if f.get("eprint") or f.get("archiveprefix"):
            return "preprint"
        return "software"
    if etype == "article":
        if f.get("journal"):
            return "article"
        # An @article with a publisher DOI is published even when the journal
        # field was never filled in; an arXiv-only one is still a preprint.
        doi = norm_doi(f.get("doi", ""))
        if doi and not doi.lower().startswith("10.48550"):
            return "article"
        return "preprint"
    return "other"


def status_of(f, kind):
    if kind == "preprint":
        return "preprint"
    vol = f.get("volume", "").strip()
    if vol.lower().startswith("available on-line") or vol.lower() in ("in press", "to appear"):
        return "in press"
    return "published"


def topics_for(entry):
    """Read the `classification` field, in TOPICS order, dropping unknowns.

    Unknown slugs are collected on the record so that --check can report them
    rather than silently discarding a topic because of a typo.
    """
    raw = entry.get("classification", "")
    slugs = [s.strip().lower() for s in raw.replace(";", ",").split(",")]
    slugs = [s for s in slugs if s]
    entry["unknown_topics"] = [s for s in slugs if s not in TOPICS]
    return [t for t in TOPICS if t in slugs]


# ---------------------------------------------------------------------------
# Build records
# ---------------------------------------------------------------------------

def build(entries):
    records = []
    for etype, key, f in entries:
        kind = kind_of(etype, f)
        title = clean_title(f.get("title", ""))
        if not title:
            continue
        authors = [format_author(a) for a in split_authors(f.get("author", f.get("editor", "")))]
        authors = [ME_DISPLAY if is_me(a) else a for a in authors]
        venue = latex_to_unicode(
            f.get("journal") or f.get("booktitle") or f.get("publisher") or
            f.get("school") or f.get("organization") or "")
        eprint = f.get("eprint", "").strip()
        url = (f.get("url") or f.get("URL") or "").strip()
        doi = norm_doi(f.get("doi", ""))
        rec = {
            "key": key,
            "kind": kind,
            "status": status_of(f, kind),
            "title": title,
            "authors": authors,
            "venue": venue,
            "year": get_year(f),
            "month": get_month(f),
            "volume": latex_to_unicode(f.get("volume", "")),
            "number": latex_to_unicode(f.get("number", "")),
            "pages": norm_pages(f.get("pages", "")),
            "doi": doi,
            "arxiv": eprint if eprint and not eprint.lower().startswith("10.") else "",
            "url": url,
            "keywords": latex_to_unicode(f.get("keywords", "")),
            "classification": f.get("classification", "").strip(),
            "note": latex_to_unicode(f.get("note", "")),
            "role": {"\\fac": "first", "\\lac": "senior",
                     "\\ec": "equal", "\\scon": "significant"}.get(
                         f.get("cc", "").strip(), ""),
        }
        if rec["volume"].lower().startswith("available on-line"):
            rec["volume"] = ""
        records.append(rec)
    return records


def dedupe(records):
    """Collapse duplicate records, preferring the most complete one."""
    def score(r):
        s = 0
        if r["status"] == "published":
            s += 100
        if r["venue"]:
            s += 20
        if r["doi"]:
            s += 10
        if r["pages"]:
            s += 3
        if r["volume"]:
            s += 2
        s += min(len(r["authors"]), 20)
        # Prefer structured "Last, First" keys (CamelCase citekeys) over slugs.
        if re.match(r"^[A-Z][A-Za-z]*[A-Z]", r["key"]):
            s += 1
        return s

    buckets = OrderedDict()
    for r in records:
        ident = None
        if r["doi"]:
            ident = ("doi", r["doi"].lower())
        elif r["arxiv"]:
            ident = ("arxiv", re.sub(r"v\d+$", "", r["arxiv"].lower()))
        else:
            ident = ("title", norm_title_key(r["title"]), r["kind"])
        buckets.setdefault(ident, []).append(r)

    merged, dropped = [], []
    for ident, group in buckets.items():
        if len(group) == 1:
            merged.append(group[0])
            continue
        group.sort(key=score, reverse=True)
        best, rest = group[0], group[1:]
        # Backfill any field the winner is missing.
        for other in rest:
            for fld in ("venue", "doi", "arxiv", "url", "volume", "number",
                        "pages", "keywords", "classification", "note", "role"):
                if not best[fld] and other[fld]:
                    best[fld] = other[fld]
            if len(other["authors"]) > len(best["authors"]):
                best["authors"] = other["authors"]
            if other["status"] == "published" and best["status"] != "published":
                best["status"] = other["status"]
            dropped.append((other["key"], best["key"]))
        merged.append(best)
    return merged, dropped


# ---------------------------------------------------------------------------
# YAML emitter (no dependency on PyYAML)
# ---------------------------------------------------------------------------

def yq(s):
    """Quote a scalar for YAML."""
    if s is None:
        s = ""
    s = str(s)
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def emit_yaml(records, path):
    lines = [
        "# Generated by scripts/bib2yaml.py from files/uvilla.bib",
        "# Do not edit by hand -- edit files/uvilla.bib and re-run:",
        "#     python3 scripts/bib2yaml.py",
        "",
        "topics:",
    ]
    for slug, label in TOPICS.items():
        lines.append("  - slug: %s" % slug)
        lines.append("    label: %s" % yq(label))
    lines.append("")
    lines.append("entries:")
    for r in records:
        lines.append("  - key: %s" % yq(r["key"]))
        lines.append("    kind: %s" % yq(r["kind"]))
        lines.append("    status: %s" % yq(r["status"]))
        lines.append("    title: %s" % yq(r["title"]))
        lines.append("    authors:")
        for a in r["authors"]:
            lines.append("      - %s" % yq(a))
        lines.append("    venue: %s" % yq(r["venue"]))
        lines.append("    year: %d" % r["year"])
        lines.append("    month: %d" % r["month"])
        for fld in ("volume", "number", "pages", "doi", "arxiv", "url", "note", "role"):
            if r[fld]:
                lines.append("    %s: %s" % (fld, yq(r[fld])))
        if r["topics"]:
            lines.append("    topics:")
            for t in r["topics"]:
                lines.append("      - %s" % t)
        else:
            # Always a list, never null, so templates can iterate it safely.
            lines.append("    topics: []")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bib", default=DEFAULT_BIB)
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--check", action="store_true",
                    help="report problems and write nothing")
    ap.add_argument("--min-articles", type=int, default=0, metavar="N",
                    help="exit non-zero if fewer than N journal articles were "
                         "parsed. The parser is deliberately lenient, so a "
                         "truncated or malformed .bib yields a nearly empty "
                         "list rather than an error; this floor turns that "
                         "into a loud failure in CI.")
    args = ap.parse_args()

    with open(args.bib, encoding="utf-8") as fh:
        raw = fh.read()

    entries = parse_bib(raw)
    records = build(entries)
    records, dropped = dedupe(records)
    merged_names = canonicalize_authors(records)

    for r in records:
        r["topics"] = topics_for(r)

    kind_rank = {"article": 0, "preprint": 1, "conference": 2,
                 "dataset": 3, "software": 4, "thesis": 5, "other": 6}
    records.sort(key=lambda r: (-r["year"], -r["month"],
                                kind_rank.get(r["kind"], 9),
                                r["title"].lower()))

    counts = Counter(r["kind"] for r in records)
    print("Parsed %d entries -> %d unique records" % (len(entries), len(records)))
    for k in sorted(counts):
        print("  %-11s %3d" % (k, counts[k]))
    if dropped:
        print("Merged %d duplicate record(s):" % len(dropped))
        for a, b in dropped:
            print("  %s -> %s" % (a, b))
    if merged_names:
        print("Normalised %d author spelling(s), e.g." % len(merged_names))
        for a, b in list(sorted(merged_names.items()))[:6]:
            print("  %-28s -> %s" % (a, b))

    topic_counts = Counter()
    for r in records:
        for t in r["topics"]:
            topic_counts[t] += 1
    print("Topics (from the `classification` field):")
    for slug, label in TOPICS.items():
        print("  %-7s %3d  %s" % (slug, topic_counts[slug], label))

    problems = []
    for r in records:
        if not r["year"]:
            problems.append("%s: missing year" % r["key"])
        if not r["authors"]:
            problems.append("%s: missing authors" % r["key"])
        if r["kind"] == "article" and not r["venue"]:
            problems.append("%s: article with no journal name in the .bib" % r["key"])
        if r["unknown_topics"]:
            problems.append("%s: unrecognised classification %s (known: %s)"
                            % (r["key"], ", ".join(r["unknown_topics"]),
                               ", ".join(TOPICS)))
        # Only the rendered kinds need a classification; conference papers,
        # datasets, software and theses are not shown on the filtered page.
        if r["kind"] == "article" and not r["topics"]:
            problems.append("%s: no `classification` field" % r["key"])
        if r["kind"] in ("software", "dataset", "thesis"):
            continue
        if r["authors"] and ME_DISPLAY not in r["authors"]:
            problems.append("%s: '%s' not among authors (%s)"
                            % (r["key"], ME_DISPLAY, "; ".join(r["authors"][:4])))
    if problems:
        print("\n%d item(s) to check:" % len(problems))
        for p in problems:
            print("  ! " + p)

    # Sanity floor. Nothing is written when it trips, so a bad .bib cannot
    # replace a good publications.yml with an empty one.
    if args.min_articles and counts["article"] < args.min_articles:
        print("\nERROR: parsed only %d journal articles, expected at least %d."
              % (counts["article"], args.min_articles))
        print("       %s is probably truncated or malformed. Nothing written."
              % os.path.relpath(args.bib, ROOT))
        return 2

    if args.check:
        return 0

    emit_yaml(records, args.out)
    print("\nWrote %s" % os.path.relpath(args.out, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
