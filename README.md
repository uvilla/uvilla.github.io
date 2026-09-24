# uvilla.github.io

Personal academic site for Umberto Villa. Jekyll, hosted on GitHub Pages.

## Updating the publication list

The single source of truth is `files/uvilla.bib` (maintained in JabRef).
Everything on the Publications page is generated from it:

```
files/uvilla.bib  ──scripts/bib2yaml.py──►  _data/publications.yml  ──Liquid──►  publications.html
```

`files/` is published, so the bib is also downloadable at
<https://uvilla.github.io/files/uvilla.bib>.

After editing the `.bib`:

```sh
make pubs          # or: python3 scripts/bib2yaml.py
```

Then commit both the `.bib` and the regenerated `_data/publications.yml`.

`make check` parses the bib and reports problems (missing years, missing
journal names, articles with no `classification`, unrecognised topic slugs,
entries where "Umberto Villa" is not among the authors) without writing
anything.

The script needs only Python 3.8+ — no third-party packages.

### What the script does

- de-duplicates entries that share a DOI, an arXiv id, or a title
- normalizes LaTeX accents to Unicode (`Cram\'er` → Cramér)
- collapses co-author name variants to their most complete spelling
  (`M. A. Anastasio`, `Mark Anastasio` → `Mark A Anastasio`)
- moves generational suffixes after the family name (`Hormuth, David A. II`
  → `David A Hormuth II`)
- classifies each entry as article / preprint / conference / dataset /
  software / thesis, and reads its research topics from `classification`

### Topics

Topics come from the non-standard `classification` field in the `.bib` — one
or more comma-separated slugs:

```bibtex
@article{MyCiteKey2026,
  ...
  classification = {pact, dlirm}
}
```

| Slug | Topic |
| --- | --- |
| `pact` | Photoacoustic Computed Tomography |
| `usct` | Ultrasound Computed Tomography |
| `iqa` | Image quality assessment |
| `dlirm` | Deep learning-based image reconstruction |
| `ipuq` | Inverse problems, Uncertainty Quantification, Digital Twins |
| `amg` | Preconditioners, Multigrid and numerical upscaling |
| `cfd` | Computational Fluid Dynamics |
| `health` | Data Science for Public Health |

The order of `TOPICS` in `scripts/bib2yaml.py` sets both the order of the
filter chips and the order of tags on each entry; edit it there to add or
rename a topic.

An article with no `classification` still appears in the list, but only under
the "All" filter — `make check` reports those, along with any slug that isn't
in the table above.

### Showing more than journal articles

`publications.html` currently renders only `kind: "article"`. All other kinds
are already in `_data/publications.yml`; to show conference papers too, change
the filter near the top of the file:

```liquid
{% assign articles = site.data.publications.entries | where: "kind", "article" %}
```

## Citing papers elsewhere on the site

Reference lists on the Research page come from the same data, by cite key:

```liquid
{% include pub_refs.html keys="LiVillaLiEtAl24, ZhouVillaAnastasio23" %}
```

An unknown key renders an HTML comment rather than a broken citation, so a
renamed key shows up as a gap.

## Local development

```sh
bundle exec jekyll serve      # or: make serve
```

There is no `Gemfile`; GitHub Pages builds with its own gem set. To build
locally, `gem install jekyll` (or add a `Gemfile` with `github-pages`).

## Structure

| Path | What it is |
| --- | --- |
| `files/uvilla.bib` | the publication source of truth (also served as a download) |
| `_config.yml` | site metadata, affiliations, profile links |
| `_data/navigation.yml` | top navigation |
| `_data/publications.yml` | **generated** — do not edit by hand |
| `_layouts/` | `base`, `default` (page + header band), `home` (hero), `wide` |
| `_includes/` | `head`, `header`, `footer`, `pub_refs` |
| `assets/css/style.scss` | the whole design system (plain CSS, no theme gem) |
| `scripts/bib2yaml.py` | bib → YAML generator |
| `material/` | drafts and working notes, excluded from the build |
| `images/optimized/` | web-sized images; originals kept alongside |

## Design notes

- No theme gem. `assets/css/style.scss` is self-contained plain CSS built on
  custom properties.
- **Careful with `clamp()`.** GitHub Pages compiles this file with Ruby Sass
  3.7 (`jekyll-sass-converter` 1.5.2), which predates `clamp()`/`min()`/`max()`
  and tries to *evaluate* arithmetic in function arguments. Writing
  `font-size: clamp(2rem, 1.35rem + 2.6vw, 3rem)` fails the build with
  `Incompatible units: 'vw' and 'rem'`. Sass leaves **custom property** values
  alone, so every fluid value lives in a `--token` in `:root` and is used via
  `var()`. Keep new fluid values in tokens too.
  (Switching Pages to a custom Actions workflow with your own `Gemfile` would
  let you use modern Dart Sass and drop this constraint.)
- The site keeps the filename `assets/css/style.scss` on purpose: with no
  `theme:` in `_config.yml`, GitHub Pages falls back to `jekyll-theme-primer`,
  and a file at that exact path shadows the theme's stylesheet.
- Light and dark themes, following the OS by default with a manual toggle in
  the header (stored in `localStorage`).
- Navigation collapses to a CSS-only hamburger below 900px.
- Page container defaults to a reading measure (`.prose`); pages that lay out
  grids set `container: full` in their front matter.
