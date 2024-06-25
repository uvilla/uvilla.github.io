---
title: Available Positions 
layout: default
---

## Postdoc position available!

A postdoc position is available to join our dynamic multidisciplinary multi-institutional team working to advance cancer treatment's current state of care.
The successful candidate will work for an NIH project aiming at developing new image reconstruction algorithms that can enable high-resolution accurate estimation of tumor perfusion rates using dynamic contrast-enhanced photoacoustic tomography. 

Applicants should have a strong background in numerical linear algebra, optimization, mathematical modeling, and partial differential equations; excellent written and verbal communication skills; and solid computational and programming skills (in particular, python and GPU accelerated frameworks such as jax, pytorch, cupy). Expertise in inverse problems, imaging science, and optical and acoustic imaging modalities is not required but highly desired.

This position is available immediately and open until filled. For more information on how to apply see [here](files/postdoc_ad.pdf).

## Master and PhD students projects

### Dynamic contrast-enhanced (DCE) imaging -- 4D/5D Image reconstruction methods for DCE photoacoustic tomography (PACT)
- Dynamic contrast-enhanced imaging of tumor perfusion plays a fundamental role in preclinical science to assess response to new treatments, such as anticancer drugs or radiotherapy. DCE PACT presents several advantages compared to other DCE imaging modalities, including fine spatial and temporal resolution, ease of detection of the arterial input function, and the fact of being free from ionizing radiation or potentially toxic contrast agents.
  
- In this project, we will use advanced numerical optimization method, including low-rank (non-negative) matrix factorization, tensor decomposition, etc to derive novel computationally and memory-efficient image reconstruction algorithms for large scale, multi-dimensional (three space dimensions, time, and optical wavelength) image reconstruction.

-	Ideal background: **Python**, **cuda**, pytorch/jax, imaging science, numerical optimization, partial differential equations

-	References: [Lozenski 2022](https://ieeexplore.ieee.org/document/9897089), [Cam 2024](https://doi.org/10.1117/1.JBO.29.S1.S11516), [Lozenski 2024](https://arxiv.org/abs/2403.03860)
  
### Task-based assessment of image quality
- Medical images are taken for a specific clinical task (screening, diagnostics, monitoring). As such, physical measurements of image quality (such as mean square errors or structural similarity) do not always inform the clinical utility of the image. Task-based assessment of image quality, instead, use signal detection and numerical observer theory to measure the performance of a particular imaging system design or image reconstruction algorithm in performing a given clinically relevant task, e.g. detecting and/or segmenting a lesion, discriminating a benign lesion from a tumor.

- In this project, we will combine machine learning and image science to develop and assess conventional (model-based) and learned image reconstruction method in a principled manner by use of statistical signal detection theory and numerical observers.

- References: [Lozenski 2024](https://ieeexplore.ieee.org/document/10384850), [Li 2024](https://doi.org/10.1117/1.JMI.11.2.026002)

### Can you hear the shape of a tumor -- Quantitative Photoacoustic Tomography
-	In 1966 the Polish American mathematician Mark Kac asked the question: _Can One Hear the Shape of a Drum?_
  Using today's medical imaging techniques, we can _hear_ tumors!
  _Photoacoustic tomography_ is an emerging medical imaging modality that uses light and sound to create 3D images 
  of hemoglobin concentration and oxygen saturation within a target tissue.
  Since tumors consume a lot of energy to grow, regions of the image showing high hemoglobin concentration and
  low oxygen saturation may hint at the presence of tumor.
  
-	In this project, we will use _partial differential equations_ to model light and sound propagation,
  _large-scale optimization methods_ to reconstruct images of hemoglobin concentration,
  _machine learning_ to further refine those images.
  
-	Ideal background: **Python**, pytorch/jax, numerical analysis, partial differential equations, and finite element methods.

- References: [Park 2023](https://doi.org/10.1117/1.JBO.28.6.066002), [Scope Crafts 2024](https://doi.org/10.1117/12.3005856)


### Make each measurement count: smaller data, richer information
-	Where should I measure? For how long? How often? _Optimal design of experiments_ is an information-theoretic framework
  to guide how data are collected to maximize accuracy and reduce uncertainty
  in parameter estimation and image reconstruction problems.
 	
-	In this project, we will use _numerical simulations_ and _partial differential equations_ to model the measurement process,
  _statistics_ and _information theory_ to quantify the information gain using a particular set of measurements,
   and _large-scale optimization_ to find the best design.
 	
-	Ideal background: Python, numerical optimization, linear algebra, partial differential equations.

- References: [Scope Crafts 2024](https://doi.org/10.1117/12.3005856)


