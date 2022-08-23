---
title: Available Projects 
layout: default
---

## Available projects for undergraduate and master-level CSEM students.

### Can you hear the shape of a tumor
-	In 1966 the Polish American mathematician Mark Kac asked the question: _Can One Hear the Shape of a Drum?_
  Using today medical imaging techniques, we can _hear_ tumors!
  _Photoacoustic tomography_ is an emerging medical imaging modality that uses light and sound to create 3D images 
  of hemoglobin concentration and oxygen saturation within a target tissue.
  Since tumors consume a lot of energy to grow, regions of the image showing high hemoglobin concentration and
  low oxygen saturation may hint to the presence of tumor.
  
-	In this project, we will use _partial differential equations_ to model light and sound propagation,
  _large-scale optimization methods_ to reconstruct images of hemoglobin concentration,
  _machine learning_ to further refine those images.
  
-	Suggested background: **Python**, TensorFlow, numerical analysis, partial differential equations, and finite element methods.

### HPC programming in Python
- `Python` has raised as a first class citizen in high performance computing (HPC). Compared to low level compiled languanges (such as C/C++ or Cuda), python allows for more flexible and readable programming, at the cost of computational performace.  `Pycuda` and `numba` are new python packages that fill this performance gap by performing just-in-time compilation of python code.

- In this project, we will use python and just-in-time compilers to accelerate the implementation of large scale imaging operators including the spherical Radon transform (photoacoustic) and psuedospectral wave solvers.

### Image guided radiation therapy
- Image-guided radiation therapy (IGRT) is the use of imaging during radiation therapy to improve the precision and accuracy of cancer treatment delivery. In particular, magnetic resonance imaging (MRI) allows for tracking the position of the tumor mass and organs-at-risk to maximize treantment delivery to the first, while minimizing radiation to the latter.

- In this project, we will develop new fast MRI reconstruction methods for use in IGRT.

### Make each measurement count: smaller data, richer information
-	Where should I measure? For how long? How often? _Optimal design of experiments_ is an information-theoretic framework
  to guide how data are collected to maximize accuracy and reduce uncertainty
  in parameter estimation and image reconstruction problems.
-	In this project, we will use _numerical simulations_ and _partial differential equations_ to model the measurement process,
  _statistics_ and _information theory_ to quantify the information gain using a particular set of measurements,
   and _large-scale optimization_ to find the best design.
-	Suggested background: Python, numerical optimization, linear algebra, partial differential equations.

### ADLA: Automatic differentiation and local assembly for finite element methods
- [MFEM](https://mfem.org/) is a free, lightweight, scalable C++ library for finite element methods that can solves partial
  differential equations with (bi)millions of parameters on the fastest supercomputer of the world!
  The goal of this project is to develop a general, lightweight and user-friendly framework in MFEM
  to evaluate user-defined finite element functionals and their first/second-order variations using automatic differentiation.
- Suggested background: scientific computing, finite element methods
- Required skill: Fluent in C++ programming

