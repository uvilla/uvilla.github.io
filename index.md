---
title: Home
layout: home
lede: >-
  I work at the interface of imaging science and predictive scientific computing —
  developing reconstruction algorithms for emerging biomedical imaging modalities,
  and the methods needed to evaluate them rigorously.
---

<div class="prose">

<h2>About</h2>

<p>My research combines engineering, mathematical modeling, artificial intelligence, and
high-performance computing to advance quantitative biomedical imaging. The current focus is
on emerging acoustic and optical modalities — photoacoustic computed tomography (PACT) and
ultrasound computed tomography (USCT) — with the goal of advancing the state of care for
cancer diagnosis and treatment.</p>

<p>I obtained my Ph.D. in Mathematics from <a href="http://emory.edu/">Emory University</a>
in December 2012, specializing in computational mathematics, with
<a href="http://mathcs.emory.edu/~ale">Prof. Alessandro Veneziani</a> as my principal advisor.
I completed my postdoctoral training at the
<a href="http://computation.llnl.gov/casc/">Center for Applied Scientific Computing</a> of
<a href="https://llnl.gov/">Lawrence Livermore National Laboratory</a> (2013–2015), working
with <a href="http://people.llnl.gov/vassilevski1">Dr. Panayot Vassilevski</a> on algebraic
multigrid and numerical upscaling for flow in porous media.</p>

<p>I then joined the <a href="http://oden.utexas.edu/">Oden Institute</a> at
<a href="http://utexas.edu/">UT Austin</a> (2015–2018) as a Research Associate, working with
<a href="http://users.oden.utexas.edu/~omar">Prof. Omar Ghattas</a> on scalable numerical
methods for Bayesian inverse problems, uncertainty quantification, optimal experimental
design, and optimization under uncertainty. After four years as a Research Assistant
Professor of <a href="https://ese.wustl.edu/">Electrical and Systems Engineering</a> at
<a href="https://wustl.edu">Washington University in St. Louis</a> and a member of the
Imaging Science PhD faculty, I rejoined the Oden Institute in August 2022.</p>

</div>

<h2 style="margin-top:3rem">Research areas</h2>

<ul class="cards">
  <li class="card">
    <h3>Task-based image quality</h3>
    <p>Numerical observers and information-theoretic bounds that measure what an imaging system lets a clinician actually do.</p>
    <a class="card__link" href="{{ '/research.html' | relative_url }}#task-based-assessment">Read more</a>
  </li>
  <li class="card">
    <h3>Trustworthy deep learning</h3>
    <p>Exposing the failure modes of learned reconstruction — hallucination, miscalibrated uncertainty — and designing methods that can be analyzed.</p>
    <a class="card__link" href="{{ '/research.html' | relative_url }}#deep-learning-reconstruction">Read more</a>
  </li>
  <li class="card">
    <h3>Virtual imaging trials</h3>
    <p>Stochastic numerical phantoms and end-to-end simulation pipelines, with the ground truth and sample sizes that credible evaluation demands.</p>
    <a class="card__link" href="{{ '/research.html' | relative_url }}#virtual-imaging-trials">Read more</a>
  </li>
  <li class="card">
    <h3>Physics-based reconstruction</h3>
    <p>Accurate imaging operators and novel object representations for photoacoustic and ultrasound computed tomography.</p>
    <a class="card__link" href="{{ '/research.html' | relative_url }}#physics-based-reconstruction">Read more</a>
  </li>
  <li class="card">
    <h3>Inverse problems &amp; UQ</h3>
    <p>Scalable algorithms for infinite-dimensional Bayesian inversion, delivered as sustainable open-source software.</p>
    <a class="card__link" href="{{ '/research.html' | relative_url }}#inverse-problems-uq">Read more</a>
  </li>
  <li class="card">
    <h3>Open-source software</h3>
    <p>hIPPYlib, hIPPYlib-MUQ, SOUPy, ParELAG — tools used by the wider computational science community.</p>
    <a class="card__link" href="{{ '/software.html' | relative_url }}">Read more</a>
  </li>
</ul>

{%- assign recent = site.data.publications.entries | where: "kind", "article" -%}

<h2 style="margin-top:3.5rem">Recent publications</h2>

<ul class="entry-list">
  {%- for a in recent limit: 5 -%}
  <li>
    {%- if a.doi -%}
      <a class="pub__title" href="https://doi.org/{{ a.doi }}" target="_blank" rel="noopener">{{ a.title }}</a>
    {%- else -%}
      <span class="pub__title">{{ a.title }}</span>
    {%- endif -%}
    <p class="pub__meta" style="margin-bottom:0">{% for author in a.authors %}{% if forloop.index > 1 %}, {% endif %}{% if author == site.author %}<span class="me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% endfor %} &middot; <span class="pub__venue">{{ a.venue }}</span> ({{ a.year }})</p>
  </li>
  {%- endfor -%}
</ul>

<p class="btn-row">
  <a class="btn" href="{{ '/publications.html' | relative_url }}">All publications</a>
</p>

<div class="callout" style="margin-top:3rem">
  <span class="callout__title">Join the group</span>
  <p style="margin-bottom:0">We are looking for undergraduate, MS, and PhD students to join the lab.
  See <a href="{{ '/available_positions.html' | relative_url }}">open positions</a> for how to get in touch.</p>
</div>
