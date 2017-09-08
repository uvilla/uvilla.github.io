---
title: Software
layout: default
---

Software development is an important component of my research and I am involved in several open source projects.

- [hIPPYlib](https://hippylib.github.io) implements state-of-the-art scalable algorithms for PDE-based deterministic
and Bayesian inverse problems. It builds on [FEniCS](https://fenicsproject.org) (a parallel finite element element library) 
for the discretization of the PDE and on [PETSc](https://www.mcs.anl.gov/petsc/) for scalable and efficient linear algebra operations
and solvers. (UT Texas, UC Merced - lead developers: U. Villa, [N. Petra](http://faculty.ucmerced.edu/npetra/index.html))

- [ParELAG](http://github.com/LLNL/parelag) implements upscaling and algebraic multigrid techniques for the efficient
solution of the algebraic linear system arising from mixed finite element discretization of saddle point problems (Original author: U. Villa, Developers: A. Barker, T. Benson, C. Lee, Project PI: P. Vassilevski).

- [MFEM](http://mfem.org/) is a lightweight, general, scalable C++ library for finite element methods.
It relies on [HYPRE](http://acts.nersc.gov/hypre/) for fast and scalable parallel linear solvers and preconditioners
(LLNL - lead developers: T. Kolev and V. Dobrev).
    
- [LifeV](http://lifev.org) is a parallel finite element library with a strong focus on computational fluid dynamics.
[Trilinos](https://trilinos.org/) is the linear algebra back-end of LifeV.
(Institutions: [CMCS – EPFL](http://cmcs.epfl.ch/), [E(CM)2 – Emory](http://www.mathcs.emory.edu/Research/Area/ScientificComputing/),
[MOX – Polimi](https://mox.polimi.it/), REO, [ESTIME– INRIA](http://www.rocq.inria.fr/estime)).

- [T-minres](https://code.google.com/p/tminres/) is an efficient and portable C++ implementation of the minres algorithm.
It supports user-defined parallel and serial data structure for the description of vectors, linear operators, and preconditioners
(developed during my Ph.D. at Emory University in collaboration with [Prof. Saunders](http://web.stanford.edu/group/SOL/software/minres/)).
