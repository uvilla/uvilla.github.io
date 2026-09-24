---
title: Contact
layout: default
container: full
eyebrow: Contact
heading: Get in touch
---

<div class="contact-grid">
  <figure style="margin:0">
    <img src="{{ '/images/optimized/profile.jpg' | relative_url }}" alt="Portrait of {{ site.author }}" width="900" height="900" loading="lazy">
  </figure>

  <div>
    <dl class="contact-dl">
      <dt>Email</dt>
      <dd>uvilla <span style="color:var(--muted)">at</span> austin.utexas.edu</dd>

      <dt>Office</dt>
      <dd>BME 5.202T<br>POB 4.252</dd>

      <dt>Phone</dt>
      <dd><a href="tel:+15122323453">512&nbsp;232-3453</a></dd>

      <dt>Mail</dt>
      <dd>
        Oden Institute for Computational Engineering and Sciences<br>
        The University of Texas at Austin<br>
        201 E. 24th Street, Mail code C0200<br>
        Austin, Texas 78712-1229
      </dd>

      <dt>Online</dt>
      <dd>
        {%- for p in site.profiles -%}
          <a href="{{ p.url }}" target="_blank" rel="noopener">{{ p.name }}</a>{% unless forloop.last %} · {% endunless %}
        {%- endfor -%}
      </dd>
    </dl>

    <div class="callout" style="margin-top:2rem">
      <span class="callout__title">Prospective students</span>
      <p style="margin-bottom:0">If you are writing about joining the group, please read
      <a href="{{ '/available_positions.html' | relative_url }}">Join us</a> first — it explains
      what to include in your email.</p>
    </div>
  </div>
</div>
