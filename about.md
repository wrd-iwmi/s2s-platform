---
layout: page
title: About
kicker: The programme, and how this site works
lede: Three service pillars, six deliverables and one five-stage operational framework — plus who is behind the platform, what it does not yet cover, and how to cite it.
trail:
  - label: About
permalink: /about/

# ---------------------------------------------------------------------------
#  TEAM TABLE — edit these rows to update the team list
# ---------------------------------------------------------------------------
team:
  - { name: "Giriraj Amarnath", role: "Programme lead",                             deliverables: "Needs assessment, Forecast datasets, Interoperability toolkit, Advisory pilots, Benchmarking" }
  - { name: "Niranga Alahacoon",  role: "Capacity strengthening",                   deliverables: "Capacity strengthening" }
  - { name: "[Dhyey Bhatpuria](https://www.iwmi.org/people/dhyey-bhatpuria/)",  role: "Datasets, interoperability, benchmarking",   deliverables: "Forecast datasets, Interoperability toolkit, Benchmarking" }
  - { name: "Suman Padhee",     role: "Forecast datasets and downscaling",          deliverables: "Needs assessment, Forecast datasets, Capacity strengthening, Benchmarking" }
  - { name: "Kalpani Jaymini",  role: "Interoperability toolkit",                   deliverables: "Interoperability toolkit" }
  - { name: "Yakob Umer",       role: "Capacity strengthening, pilots",             deliverables: "Capacity strengthening, Advisory pilots" }
  - { name: "Surya Kiran Guniganti", role: "Forecast datasets and downscaling",     deliverables: "Advisory pilots" }
  - { name: "Mirriam Makungwe", role: "Advisory pilots",                            deliverables: "Advisory pilots" }
 # - { name: "Salomon",          role: "Ghana cocoa yield forecasting",              deliverables: "Advisory pilots" }

contributors: ["Aniruddha Saha", "Mohamed Yousuf"]

# ---------------------------------------------------------------------------
#  KNOWN GAPS — keep this list current as material arrives
# ---------------------------------------------------------------------------
gaps:
  # Each gap is a sentence. If it starts with a page name followed by " — ",
  # add a "url" and that name becomes a link automatically.
  - text: "ENSO Dashboard — the tool page still needs a description of the interface itself; its API is documented in full."
    url: /tools/enso-dashboard/
  - text: "Method documentation and both case studies are written but under review, and show as coming soon."
  - text: "Public URLs for CI-IDSS and the Ghana cocoa dashboard."
  - text: "The expansion of the CI-IDSS acronym."
  - text: "The QBR mathematical formulation, parameters and reference implementation."
  - text: "Tutorial step-by-step content for the capacity-strengthening modules."
---

{%- assign p = site.data.programme -%}

<section id="what-this-is">
  <h2>What this platform is</h2>
  <p class="lede" style="max-width:68ch">
    A technical knowledge and access portal for the {{ site.lead_institute }}-led work
    on seasonal-to-subseasonal forecasting within {{ site.programme }}.
  </p>
  <p style="max-width:68ch">
    It documents the programme's forecast datasets, downscaling and modelling methods,
    interoperability APIs, training resources and advisory pilots, so that a climate
    scientist, a developer and a government technical officer can each find what they
    need without going through an intermediary. It is a documentation platform, not a
    forecast service — live products are served by the
    <a href="{{ '/tools/' | relative_url }}">tools</a> it describes.
  </p>
</section>

<section id="pillars" style="margin-top:4rem">
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

<section id="deliverables" style="margin-top:4rem">
  <div class="section-head">
    <h2>Deliverables</h2>
    <p>Expand any deliverable for its activities and the documentation it produces on this site.</p>
  </div>
  {%- for d in p.deliverables %}
  <details class="disclosure">
    <summary>
      <span class="badge badge--blue">{{ d.short_label }}</span>
      <span>{{ d.title }}</span>
      {%- if d.when %}<span class="badge badge--neutral" style="margin-left:auto">{{ d.when }}</span>{% endif %}
    </summary>
    <div class="disclosure__body">
      <p>{{ d.summary }}</p>
      <p class="eyebrow">Activities</p>
      <ol>{% for a in d.activities %}<li>{{ a }}</li>{% endfor %}</ol>
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

<section id="framework" style="margin-top:4rem">
  <div class="section-head">
    <h2>{{ p.framework_heading }}</h2>
    <p>{{ p.framework_lede }}</p>
  </div>

  {% include framework-stages.html %}

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


<section id="limitations" style="margin-top:4rem">
  <h2>Limitations and documentation status</h2>
  <div class="callout callout--limitation">
    <strong class="callout__title">Read this before relying on anything here</strong>
    <ul style="margin:0">
      <li>These are <strong>research and development capabilities</strong>, not operational services with guaranteed availability.</li>
      <li>Forecast skill varies by region, season, variable and lead time. Skill established in one basin does not transfer to another.</li>
      <li>Where this site shows a placeholder for an endpoint, credential, result or schema, that information does not yet exist publicly — it has not been withheld and it should not be assumed.</li>
      <li>Results and adoption evidence from the advisory pilots are still being generated through the monitoring and learning activity.</li>
      <li>Publications and references have deliberately been left empty rather than populated with plausible-looking citations.</li>
    </ul>
  </div>

  <h3 style="margin-top:2rem">Known gaps in this site</h3>
  <p style="max-width:68ch">The following are not yet documented because no descriptive material exists for them:</p>
  <ul style="max-width:68ch">
    {%- for gap in page.gaps -%}
      {%- assign bits = gap.text | split: " — " -%}
      <li>
        {%- if gap.url and bits.size > 1 -%}
          <a href="{{ gap.url | relative_url }}">{{ bits[0] }}</a> — {{ bits[1] }}
        {%- else -%}
          {{ gap.text }}
        {%- endif -%}
      </li>
    {%- endfor -%}
  </ul>

  <p style="max-width:68ch;font-size:var(--t-sm);color:var(--c-ink-2)">
    Provenance for every dataset the programme uses is in the
    <a href="{{ '/datasets/' | relative_url }}">dataset catalogue</a>; method
    assumptions, validation and limitations are on each
    <a href="{{ '/methods/' | relative_url }}">method page</a>.
  </p>
</section>

<section id="responsible-use" style="margin-top:4rem">
  <h2>Responsible use</h2>
  <p style="max-width:68ch">
    Forecast information carries uncertainty. Advisories built on these products should
    communicate that uncertainty to end users rather than presenting a probabilistic
    outlook as a deterministic prediction — particularly where an advisory influences
    planting, input purchase, water allocation or anticipatory finance decisions that
    affect livelihoods.
  </p>
  <p style="max-width:68ch">
    Before building an operational service on any product documented here, consult the
    <a href="{{ '/methods/forecast-verification/' | relative_url }}">skill benchmarking work</a>
    for the relevant region and variable, and contact the team.
  </p>
</section>

<section id="citation" style="margin-top:4rem">
  <h2>Citation and attribution</h2>
  <p style="max-width:68ch">
    A formal citation for this platform has not been agreed. Until it is, please
    attribute content to the {{ site.lead_institute }} and {{ site.programme }}, and
    contact the team before citing any specific method, dataset or result.
  </p>
  <div class="citation" style="max-width:68ch">
    <code>{{ site.lead_institute }} ({{ site.time | date: '%Y' }}). {{ site.brand_line }}. {{ site.programme }}. Citation format to be confirmed.</code>
  </div>
</section>

<section id="team" style="margin-top:4rem">
  <h2>Team</h2>
  <p style="max-width:68ch">
    Team members named across the programme's six deliverables.
  </p>
  <div class="table-scroll" style="max-width:78ch">
    <table>
      <thead><tr><th>Name</th><th>Contribution</th><th>Deliverables</th></tr></thead>
      <tbody>
        {%- for t in page.team %}
        <tr><td>{{ t.name }}</td><td>{{ t.role }}</td><td>{{ t.deliverables }}</td></tr>
        {%- endfor %}
      </tbody>
    </table>
  </div>
  <p style="margin-top:1rem;font-size:var(--t-sm);color:var(--c-ink-2)">
    Interns and contributors: {{ page.contributors | join: ', ' }}.
  </p>
</section>

<section id="contact" style="margin-top:4rem">
  <h2>Contact</h2>
  <p style="max-width:68ch">
    For questions about a capability, a correction to this site, or a request to
    collaborate, contact the {{ site.lead_institute }}.
  </p>
  <p class="btn-row">
    <a class="btn btn--primary" href="mailto:{{ site.contact_email }}">Email the team</a>
    {%- if site.repo_url and site.repo_url != 'https://github.com/' %}
    <a class="btn btn--secondary" href="{{ site.repo_url }}" rel="noopener">Source repository ↗</a>
    {%- endif %}
  </p>
  <p style="font-size:var(--t-sm);color:var(--c-muted);max-width:68ch">
    If a page shows a placeholder that you can fill, that is the most useful correction
    you can send — each page is a single markdown file and content changes require no code.
  </p>
</section>
