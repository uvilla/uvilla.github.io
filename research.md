---
title: Research
layout: default
container: full
eyebrow: Research
heading: Computing that makes medical images answer clinical questions
subtitle: >-
  My group develops computational, statistical, and AI methods for biomedical
  imaging — and the tools needed to judge, rigorously, whether those methods
  actually help with the task at hand.
---

<div class="prose">

<p>My research interests and expertise are in computational engineering and biomedical
imaging, informed by transdisciplinary training that combines engineering, mathematical
modeling, artificial intelligence, and scientific computing. The goal is to use the power
of computing to accelerate biomedical innovation and help resolve major challenges in
medicine and public health, including early detection of cancer and improved treatment
outcomes.</p>

<p>Three questions organize the work: how do we <strong>advance emerging imaging
modalities</strong> so they meet real needs in clinical medicine and basic science; how do
we <strong>optimize the design of imaging instruments</strong> and the algorithms that turn
their measurements into images; and how do we <strong>support clinical decision-making</strong>
for patient-specific treatment. Running through all three is a conviction that system designs
and reconstruction methods must be evaluated by how well they support the clinical task, not
by how good the images look.</p>

</div>

<ul class="cards" style="margin-top:2.25rem">
  <li class="card">
    <span class="card__num">1</span>
    <h3>Task-based image quality</h3>
    <p>Numerical observers and performance bounds that measure what a system lets a clinician actually do.</p>
    <a class="card__link" href="#task-based-assessment">Read more</a>
  </li>
  <li class="card">
    <span class="card__num">2</span>
    <h3>Trustworthy deep learning</h3>
    <p>Exposing the failure modes of learned reconstruction, and designing methods that can be analyzed.</p>
    <a class="card__link" href="#deep-learning-reconstruction">Read more</a>
  </li>
  <li class="card">
    <span class="card__num">3</span>
    <h3>Virtual imaging trials</h3>
    <p>Stochastic numerical phantoms and end-to-end simulation, with ground truth you control.</p>
    <a class="card__link" href="#virtual-imaging-trials">Read more</a>
  </li>
  <li class="card">
    <span class="card__num">4</span>
    <h3>Physics-based reconstruction</h3>
    <p>Accurate imaging operators and novel object representations for PACT and USCT.</p>
    <a class="card__link" href="#physics-based-reconstruction">Read more</a>
  </li>
  <li class="card">
    <span class="card__num">5</span>
    <h3>Inverse problems &amp; UQ</h3>
    <p>Scalable Bayesian inversion at scale, delivered as open-source software people can use.</p>
    <a class="card__link" href="#inverse-problems-uq">Read more</a>
  </li>
</ul>

<section class="theme" id="task-based-assessment">
  <div class="theme__head">
    <span class="theme__num">01</span>
    <h2>Objective, task-based assessment of image quality</h2>
  </div>
  <div class="theme__body">
    <p>The performance of a medical imaging system should be measured by how well it enables
    the clinical task it was built for — detecting a lesion, or quantifying a physiological
    parameter. Physical fidelity measures such as mean square error, signal-to-noise ratio,
    or structural similarity do not reliably correlate with diagnostic performance. My work
    develops the computational tools that make objective assessment tractable for modern,
    high-dimensional, nonlinear imaging systems.</p>

    <p>With collaborators, I have established how the <em>Bayesian ideal observer</em> — the
    optimal task-based performance bound — can be approximated by Markov-chain Monte Carlo
    methods that use deep generative models to represent realistic object statistics; shown
    how learned ideal and Hotelling observers can be trained directly from simulated ensembles
    to estimate upper bounds on system performance, including for multimodal data; developed
    methods to compute and characterize the <em>null space</em> of an imaging operator, which
    determines precisely what object information a system can and cannot recover, and
    therefore what no reconstruction method can recover; and derived Bayesian Cramér–Rao
    bounds for quantitative estimation tasks, giving a principled objective for imaging
    system design.</p>

    <p>Although developed in the context of photoacoustic and ultrasound imaging, these tools
    are modality-agnostic and apply to the assessment of any computed imaging system.</p>

{% include pub_refs.html keys="LiVillaLiEtAl24, ZhouVillaAnastasio23, KuoGranstedtVillaEtAl22, CraftScopeAnastasioVilla24" %}
  </div>
</section>

<section class="theme" id="deep-learning-reconstruction">
  <div class="theme__head">
    <span class="theme__num">02</span>
    <h2>Rigorous evaluation and trustworthy design of learned reconstruction</h2>
  </div>
  <div class="theme__body">
    <p>Deep learning methods routinely report large gains over classical and model-based
    reconstruction, but those gains are typically demonstrated with physical fidelity measures
    on limited test sets. My work addresses the resulting credibility gap from both directions:
    by exposing the specific failure modes of learned reconstruction, and by designing learned
    methods whose behavior can be interpreted rather than merely benchmarked.</p>

    <p>We have shown that ill-posed tomographic problems admit <em>multiple</em> data-consistent
    solutions within the manifold of a deep generative model — a concrete mechanism for
    hallucination, and a tool for exploring it. We have critically assessed whether
    diffusion-model posterior samplers actually deliver calibrated uncertainty quantification
    for Bayesian inverse problems; they frequently do not, despite being widely presented as
    if they do. On the design side, we develop <em>task-informed</em> learned full-waveform
    inversion, in which the downstream task enters training so that reconstruction optimizes
    clinically relevant rather than pixel-wise performance; learned filtered-backprojection
    operators with analyzable structure, for which stability and consistency properties can
    be established; and learned forward-model and aberration corrections that remain anchored
    to the underlying physics.</p>

{% include pub_refs.html keys="LozenskiWangLiEtAl24, CamVillaAnastasio24, CraftsVilla25, LinFengTheilerEtal26" %}
  </div>
</section>

<section class="theme" id="virtual-imaging-trials">
  <div class="theme__head">
    <span class="theme__num">03</span>
    <h2>Virtual imaging trials: object ensembles and end-to-end simulation</h2>
  </div>
  <div class="theme__body">
    <p>Task-based assessment requires an <em>ensemble</em> of statistically realistic objects
    with known ground truth — something no clinical dataset can supply, because ground truth
    is unavailable and anatomical variability is not controllable. Virtual imaging trials
    close that gap, and are the practical enabler of everything above.</p>

    <p>My long-term goal is to establish end-to-end virtual imaging frameworks as the first
    step in developing and validating new imaging technologies. That means constructing virtual
    patient populations via stochastic numerical phantoms that capture realistic variability in
    anatomy, tissue composition, and acoustic and optical properties; simulating the data
    acquisition process at high fidelity, including instrument-specific physics; applying both
    model-based and learned reconstruction within a common, controlled pipeline; and reading out
    image quality with clinically relevant, task-based measures. I have led or co-led the
    development of 3-D stochastic numerical breast, head, and mouse phantoms for ultrasound and
    photoacoustic computed tomography, and released these resources to the community. The
    framework is what allows learned and classical methods to be compared on identical object
    ensembles, at sample sizes sufficient for statistically meaningful conclusions.</p>

{% include pub_refs.html keys="LiVillaParkEtAl21, ParkVillaLiEtAl23, ParkJeongVillaEtal26, HuangKuoParkEtAl26" %}
  </div>
</section>

<section class="theme" id="physics-based-reconstruction">
  <div class="theme__head">
    <span class="theme__num">04</span>
    <h2>Physics-based reconstruction for emerging imaging modalities</h2>
  </div>
  <div class="theme__body">
    <p>Credible assessment of learned reconstruction requires a defensible reference: a
    model-based method that exploits the measurement physics as fully as computation allows.
    My work establishes such reference methods for emerging acoustic and optical modalities,
    and in doing so advances the quantitative accuracy achievable without learning.</p>

    <p>This includes accurate imaging operators — a 3-D full-waveform-inversion forward model
    incorporating elevation-focused transducer properties for ultrasound computed tomography,
    and a multiphysics finite-element full-wave model for transcranial photoacoustic imaging
    that accounts for skull-induced aberration; novel object representations for dynamic
    imaging, including tensor decompositions and neural fields as a memory-efficient,
    self-supervised representation for spatiotemporal reconstruction; spatiotemporal methods
    that enable high-frame-rate dynamic photoacoustic imaging from sparse rotating-gantry
    measurements; and rigorous analysis of the identifiability limits of joint estimation
    problems. <!--That last line matters for everything above: identifiability analysis tells us
    when an apparent deep learning success is recovering real information, and when it is
    supplying a prior.--></p>

{% include pub_refs.html keys="LozenskiAnastasioVilla22, LozenskiCamPagelEtAl24, LiVillaDuricEtAl23, GangwonVillaAnastasio25" %}
  </div>
</section>

<section class="theme" id="inverse-problems-uq">
  <div class="theme__head">
    <span class="theme__num">05</span>
    <h2>Large-scale inverse problems, uncertainty quantification, and open-source software</h2>
  </div>
  <div class="theme__body">
    <p>Image reconstruction is an inverse problem, and Bayesian inverse theory provides a
    rigorous framework for quantifying posterior uncertainty, measuring information content,
    and assessing experimental-design objectives. My work develops scalable algorithms for
    infinite-dimensional Bayesian inverse problems and — equally important — delivers them as
    software the community can actually use.</p>

    <p>I am the lead developer of <a href="https://hippylib.github.io">hIPPYlib</a>, an
    extensible framework for large-scale PDE-constrained inverse problems that has become a
    widely adopted reference implementation for scalable deterministic and Bayesian inversion,
    and a co-developer of hIPPYlib-MUQ (coupling scalable inversion with advanced MCMC) and
    SOUPy (PDE-constrained optimization under high-dimensional uncertainty). Methodologically,
    I have contributed derivative-informed reduced neural operators and projected neural
    networks that give fast, accurate surrogates for high-dimensional parameter-to-observable
    maps — an enabling technology for the many forward solves that ensemble-based assessment
    requires — along with Hessian-based adaptive quadrature, scalable samplers for spatially
    correlated random fields, and preconditioners for large-scale inversion.</p>

    <p>These methods have been applied across imaging, computational oncology (predictive
    digital twins with quantified uncertainty for patient-specific decision making),
    geophysics, and glaciology, which has repeatedly sharpened the algorithms.</p>

{% include pub_refs.html keys="VillaPetraGhattas21, KimVillaParnoEtAl23, OLearyVillaChenEtAl21, PashVillaHormuthEtAl26" %}
  </div>
</section>

<section class="theme" id="earlier-work">
  <div class="theme__head">
    <span class="theme__num">06</span>
    <h2>Earlier work</h2>
  </div>
  <div class="theme__body">
    <p>During my doctoral program and postdoctoral training I worked on large-scale numerical
    simulation as a tool to inform decision-making under uncertainty: patient-specific
    computational hemodynamics to quantify wall shear stress and predict aneurysm rupture risk;
    optimal control of the inlet condition of a turbulent jet to ensure proper mixing;
    information-theoretic approaches to optimally designing sensing systems; and algebraic
    multigrid and numerical upscaling for flow in porous media.</p>

    <ul class="figure-grid">
      <li><figure>
        <img src="{{ '/images/optimized/research/inverseproblems.png' | relative_url }}" alt="Diagram of the Bayesian inverse problem workflow" loading="lazy">
        <figcaption>Extracting knowledge from data by solving inverse problems</figcaption>
      </figure></li>
      <li><figure>
        <img src="{{ '/images/optimized/research/random_field.png' | relative_url }}" alt="Realization of a Gaussian random field" loading="lazy">
        <figcaption>Scalable sampling algorithms for Gaussian random fields</figcaption>
      </figure></li>
      <li><figure>
        <img src="{{ '/images/optimized/research/hemodynamics.png' | relative_url }}" alt="Patient-specific blood flow simulation" loading="lazy">
        <figcaption>Computational hemodynamics</figcaption>
      </figure></li>
      <li><figure>
        <img src="{{ '/images/optimized/research/two_phases.png' | relative_url }}" alt="Two-phase porous media flow simulation" loading="lazy">
        <figcaption>Two-phase porous media flow</figcaption>
      </figure></li>
      <li><figure>
        <img src="{{ '/images/optimized/research/amge.png' | relative_url }}" alt="Hierarchy of agglomerated meshes" loading="lazy">
        <figcaption>Hierarchy of agglomerated meshes for element-based AMG</figcaption>
      </figure></li>
    </ul>
  </div>
</section>

<div class="callout callout--note" style="margin-top:3rem">
  <span class="callout__title">Full record</span>
  <p style="margin-bottom:0">Browse the complete <a href="{{ '/publications.html' | relative_url }}">list of publications</a>,
  or find me on <a href="https://scholar.google.com/citations?user=lELCubQAAAAJ&amp;hl=en" target="_blank" rel="noopener">Google&nbsp;Scholar</a>.</p>
</div>
