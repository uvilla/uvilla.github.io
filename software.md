---
title: Software
layout: default
container: full
eyebrow: Software
heading: Open-source scientific computing
subtitle: >-
  Software development is a core part of my research. Sustainability,
  reproducibility, and a low barrier to entry matter as much as the algorithms.
---

<ul class="cards">
  <li class="card">
    <h3>hIPPYlib</h3>
    <p>An extensible framework implementing state-of-the-art scalable algorithms for PDE-based
    deterministic and Bayesian inverse problems. Built on FEniCS/dolfinx for PDE discretization
    and PETSc for scalable linear algebra.</p>
    <p style="font-size:.85rem;color:var(--muted)">UT Austin · UC Merced — lead developers:
    U. Villa, <a href="http://faculty.ucmerced.edu/npetra/index.html">N. Petra</a></p>
    <p class="btn-row">
      <a class="btn" href="https://hippylib.github.io" target="_blank" rel="noopener">Website</a>
      <a class="btn" href="https://github.com/hippylib/hippylibx" target="_blank" rel="noopener">hIPPYlibx</a>
    </p>
  </li>

  <li class="card">
    <h3>hIPPYlib-MUQ</h3>
    <p>Couples hIPPYlib's scalable inversion machinery with MUQ's advanced MCMC samplers,
    for Bayesian inference with complex predictive models under uncertainty.</p>
    <p class="btn-row">
      <a class="btn" href="https://doi.org/10.1145/3580278" target="_blank" rel="noopener">Paper</a>
    </p>
  </li>

  <li class="card">
    <h3>SOUPy</h3>
    <p>Stochastic PDE-constrained optimization under high-dimensional uncertainty, in Python.
    Built on hIPPYlib and FEniCS.</p>
    <!-- TODO: add the SOUPy repository link (and a DOI for the JOSS paper in the .bib). -->
  </li>

  <li class="card">
    <h3>ParELAG</h3>
    <p>Upscaling and algebraic multigrid techniques for the efficient solution of algebraic
    systems arising from mixed finite element discretizations of saddle point problems.</p>
    <p style="font-size:.85rem;color:var(--muted)">Original author: U. Villa · Developers:
    A. Barker, T. Benson, C. Lee · PI: P. Vassilevski</p>
    <p class="btn-row">
      <a class="btn" href="http://github.com/LLNL/parelag" target="_blank" rel="noopener">GitHub</a>
    </p>
  </li>

  <li class="card">
    <h3>MFEM</h3>
    <p>A lightweight, general, scalable C++ library for finite element methods, relying on
    HYPRE for fast parallel solvers and preconditioners.</p>
    <p style="font-size:.85rem;color:var(--muted)">LLNL — lead developers: T. Kolev, V. Dobrev</p>
    <p class="btn-row">
      <a class="btn" href="http://mfem.org/" target="_blank" rel="noopener">Website</a>
    </p>
  </li>

  <li class="card">
    <h3>LifeV</h3>
    <p>A parallel finite element library with a strong focus on computational fluid dynamics,
    using Trilinos as its linear algebra back end.</p>
    <p style="font-size:.85rem;color:var(--muted)">CMCS–EPFL · E(CM)² – Emory · MOX – Polimi ·
    REO &amp; ESTIME – INRIA</p>
    <p class="btn-row">
      <a class="btn" href="http://lifev.org" target="_blank" rel="noopener">Website</a>
    </p>
  </li>

  <li class="card">
    <h3>tMINRES</h3>
    <p>An efficient, portable C++ implementation of the MINRES algorithm, supporting
    user-defined parallel and serial data structures for vectors, operators, and
    preconditioners. Developed during my Ph.D. at Emory in collaboration with
    <a href="http://web.stanford.edu/group/SOL/software/minres/" target="_blank" rel="noopener">Prof. Saunders</a>.</p>
    <!-- The old Google Code URL is dead; add the current repository link here. -->
  </li>
</ul>
