---
layout: page
title: Programme & framework
kicker: How the work is organised
lede: Three service pillars, six deliverables, one five-stage operational framework. This page is the map — every tool, method, API, tutorial and case study on this site attaches to a stage of the framework and to one or more deliverables.
trail:
  - label: Programme
permalink: /programme/
---

{%- assign p = site.data.programme -%}

<section id="pillars">
  <div class="section-head">
    <h2>{{ p.pillars_heading }}</h2>
    <p>{{ p.pillars_lede }}</p>
  </div>
  <div class="grid grid--3">
    {%- for pillar in p.pillars %}
    <div class="card card--flat">
      <p class="eyebrow" style="margin:0">Pillar {{ pillar.number }}{% if pillar.when %} · {{ pillar.when }}{% endif %}</p>
      <h3>{{ pillar.title }}</h3>
      <p>{{ pillar.body }}</p>
    </div>
    {%- endfor %}
  </div>
  <p style="margin-top:1.5rem;font-size:var(--t-sm);color:var(--c-ink-2);max-width:68ch">{{ p.pillars_note }}</p>
</section>

<section id="framework" style="margin-top:4rem">
  <div class="section-head">
    <h2>{{ p.framework_heading }}</h2>
    <p>{{ p.framework_lede }}</p>
  </div>

  <ol class="pipeline" style="list-style:none;padding:0;margin:0 0 1.5rem">
    {%- for s in p.stages %}
    <li class="pipeline__stage" style="--stage-color:{{ s.colour }};--stage-bg:{{ s.tint }}">
      <h3><span class="pipeline__num">Stage {{ forloop.index }}</span> <span>{{ s.name }}</span></h3>
      <p style="margin:0 0 .5rem;font-size:var(--t-sm);color:var(--c-ink-2)">{{ s.detail }}</p>
      <span class="pipeline__link">{{ s.maps }}</span>
    </li>
    {%- unless forloop.last %}
    <li class="pipeline__arrow" aria-hidden="true">
      <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true" focusable="false"><path d="M7 1v12M3 9l4 4 4-4"/></svg>
    </li>
    {%- endunless %}
    {%- endfor %}
  </ol>

  <div class="callout callout--note">
    <strong class="callout__title">{{ p.framework_note_title }}</strong>
    <p style="margin:0">{{ p.framework_note }}</p>
  </div>
</section>

<section id="six-layer-model" style="margin-top:4rem">
  <div class="section-head">
    <h2>{{ p.six_layer_heading }}</h2>
    <p>{{ p.six_layer_lede }}</p>
  </div>
  {% include six-layer-model.html %}
</section>

<section id="deliverables" style="margin-top:4rem">
  <div class="section-head">
    <h2>{{ p.deliverables_heading }}</h2>
    <p>{{ p.deliverables_lede }}</p>
  </div>
  {%- for d in p.deliverables %}
  <details class="disclosure">
    <summary>
      <span class="badge badge--blue">{{ d.id }}</span>
      <span>{{ d.title }}</span>
      {%- if d.when %}<span class="badge badge--neutral" style="margin-left:auto">{{ d.when }}</span>{% endif %}
    </summary>
    <div class="disclosure__body">
      <p>{{ d.summary }}</p>
      <p class="eyebrow">Activities</p>
      <ol>{% for a in d.activities %}<li>{{ a }}</li>{% endfor %}</ol>
      <p class="eyebrow">Team</p>
      <p style="margin-bottom:1rem">{{ d.team | join: ' · ' }}</p>
      {%- if d.links.size > 0 %}
      <p class="eyebrow">Documented on this site</p>
      <ul class="link-list">
        {%- for l in d.links %}<li><a href="{{ l.url | relative_url }}">{{ l.label }}<span>→</span></a></li>{% endfor %}
      </ul>
      {%- endif %}
    </div>
  </details>
  {%- endfor %}
</section>

<section id="partners" style="margin-top:4rem">
  <div class="section-head">
    <h2>{{ p.partners_heading }}</h2>
    <p>{{ p.partners_lede }}</p>
  </div>
  <div class="grid grid--3">
    {%- for group in p.partners %}
    <div class="card card--flat">
      <h3>{{ group.group }}</h3>
      <ul style="font-size:var(--t-sm);margin:0">
        {%- for i in group.items %}<li>{{ i }}</li>{% endfor %}
      </ul>
    </div>
    {%- endfor %}
  </div>
  <p style="margin-top:1rem;font-size:var(--t-xs);color:var(--c-muted)">{{ p.partners_note }}</p>
</section>
