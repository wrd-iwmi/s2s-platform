---
layout: page
title: About this platform
kicker: Trust and transparency
lede: What this site is, where its content comes from, what it does not yet cover, and how to cite it.
trail:
  - label: About
permalink: /about/

# ---------------------------------------------------------------------------
#  TEAM TABLE — edit these rows to update the team list
# ---------------------------------------------------------------------------
team:
  - { name: "Giriraj Amarnath", role: "Programme lead",                          deliverables: "D1, D2, D3, D5, D6" }
  - { name: "Niranga Alacoon",          role: "Capacity strengthening",                  deliverables: "D4" }
  - { name: "Dhyey Bhatpuria",            role: "Datasets, interoperability, benchmarking", deliverables: "D2, D3, D6" }
  - { name: "Suman Padhee",            role: "Forecast datasets and downscaling",       deliverables: "D1, D2, D4, D6" }
  # - { name: "Naga",             role: "Datasets, pilots, benchmarking",          deliverables: "D2, D5, D6" }
  - { name: "Kalpani Jaymini",          role: "Interoperability toolkit",                deliverables: "D3" }
  - { name: "Yakob Umer",            role: "Capacity strengthening, pilots",          deliverables: "D4, D5" }
  - { name: "Surya Kiran Guniganti",      role: "South Asia irrigation advisory",          deliverables: "D5" }  
  - { name: "Mirriam Makungwe",          role: "Advisory pilots",                         deliverables: "D5" }
  - { name: "Salomon",          role: "Ghana cocoa yield forecasting",           deliverables: "D5" }  


contributors: ["Aniruddha Saha", "Mohamed Yousuf"]

# ---------------------------------------------------------------------------
#  KNOWN GAPS — keep this list current as material arrives
# ---------------------------------------------------------------------------
gaps:
  # Each gap is a sentence. If it starts with a page name followed by " — ",
  # add a "url" and that name becomes a link automatically.
  - text: "ENSO Dashboard — no descriptive material was supplied, so the page is a structured request for content rather than documentation."
    url: /tools/enso-dashboard/
  - text: "Public URLs for AWARE, SADMS / SukhaRakshak AI, CI-IDSS and the Ghana cocoa dashboard."
  - text: "The expansion of the SADMS and CI-IDSS acronyms."
  - text: "The QBR mathematical formulation, parameters and reference implementation."
  - text: "Tutorial step-by-step content, which follows module development under Deliverable 4."
---

<section id="about">
  <h2>What this site is</h2>
  <p class="lede" style="max-width:68ch">
    A technical knowledge and access portal for the {{ site.lead_institute }}-led work on
    seasonal-to-subseasonal forecasting within {{ site.programme }}.
  </p>
  <p style="max-width:68ch">
    It documents the programme's forecast datasets, downscaling and modelling methods,
    interoperability APIs, training resources and advisory pilots, so that a climate scientist,
    a developer and a government technical officer can each find what they need without going
    through an intermediary.
  </p>
  <p style="max-width:68ch">
    It is a documentation platform, not a forecast service. Live forecast products are served
    by the platforms listed under <a href="{{ '/tools/' | relative_url }}">tools</a>.
  </p>
</section>

<section id="data-sources" style="margin-top:4rem">
  <h2>Data sources</h2>
  <p style="max-width:68ch">
    All content on this site is derived from the CGIAR Climate Action S2S programme
    documentation. Nothing has been added from outside that material.
  </p>
  <p style="max-width:68ch">
    The forecast, observational, reanalysis and ancillary datasets used by the programme are
    listed in the <a href="{{ '/datasets/' | relative_url }}">dataset catalogue</a>
    ({{ site.datasets.size }} entries). Dataset specifications should always be verified against
    the provider's documentation for the product version in use.
  </p>
  <ul class="link-list" style="max-width:68ch">
    {%- assign ds = site.datasets | sort: "weight" | reverse -%}
    {%- for d in ds limit: 6 %}
    <li><a href="{{ d.url | relative_url }}">{{ d.title }}<span>{{ d.role }}</span></a></li>
    {%- endfor %}
  </ul>
</section>

<section id="methodology" style="margin-top:4rem">
  <h2>Methodology</h2>
  <p style="max-width:68ch">
    Methods are documented at three levels — executive summary, technical explanation and
    implementation detail — in the <a href="{{ '/methods/' | relative_url }}">methods library</a>.
    Where a formulation or reference implementation has not been published, the page states that
    explicitly instead of paraphrasing a summary into something that reads like a specification.
  </p>
</section>

<section id="limitations" style="margin-top:4rem">
  <h2>Limitations and documentation status</h2>
  <div class="callout callout--limitation">
    <strong class="callout__title">Read this before relying on anything here</strong>
    <ul style="margin:0">
      <li>These are <strong>research and development capabilities</strong>, not operational services with guaranteed availability.</li>
      <li>Forecast skill varies by region, season, variable and lead time. Skill established in one basin does not transfer to another.</li>
      <li>No API endpoints have been published. Where this site shows a placeholder for an endpoint, credential or schema, that information does not yet exist publicly — it has not been withheld and it should not be assumed.</li>
      <li>Results and adoption evidence from the advisory pilots are still being generated through the Deliverable&nbsp;5 monitoring and learning activity.</li>
      <li>Publications and references have deliberately been left empty rather than populated with plausible-looking citations.</li>
    </ul>
  </div>

  <h3 style="margin-top:2rem">Known gaps in this site</h3>
  <p style="max-width:68ch">The following were requested for the site but no descriptive material was available:</p>
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
</section>

<section id="responsible-use" style="margin-top:4rem">
  <h2>Responsible use</h2>
  <p style="max-width:68ch">
    Forecast information carries uncertainty. Advisories built on these products should
    communicate that uncertainty to end users rather than presenting a probabilistic outlook as
    a deterministic prediction — particularly where an advisory influences planting, input
    purchase, water allocation or anticipatory finance decisions that affect livelihoods.
  </p>
  <p style="max-width:68ch">
    Before building an operational service on any product documented here, consult the
    <a href="{{ '/methods/forecast-verification/' | relative_url }}">skill benchmarking work</a>
    for the relevant region and variable, and contact the team.
  </p>
</section>

<section id="team" style="margin-top:4rem">
  <h2>Team</h2>
  <p style="max-width:68ch">
    Team members named across the programme's six deliverables and two documented pilots.
    Several roles are recorded in the workplan as open positions (Climate Services Specialist,
    Climate Services and Climate-Resilient Agriculture hires).
  </p>
  <div class="table-scroll" style="max-width:68ch">
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

<section id="partners" style="margin-top:4rem">
  <h2>Partners</h2>
  <p style="max-width:68ch">
    The draft partner mapping across innovation, demand and scaling functions is on the
    <a href="{{ '/programme/#partners' | relative_url }}">programme page</a>.
  </p>
</section>

<section id="citation" style="margin-top:4rem">
  <h2>Citation and attribution</h2>
  <p style="max-width:68ch">
    A formal citation for this platform has not been agreed. Until it is, please attribute
    content to the {{ site.lead_institute }} and {{ site.programme }}, and contact the team
    before citing any specific method, dataset or result.
  </p>
  <div class="citation" style="max-width:68ch">
    <code>{{ site.lead_institute }} ({{ site.time | date: '%Y' }}). {{ site.brand_line }}. {{ site.programme }}. Citation format to be confirmed.</code>
  </div>
</section>

<section id="contact" style="margin-top:4rem">
  <h2>Contact</h2>
  <p style="max-width:68ch">
    For questions about a capability, a correction to this site, or a request to collaborate,
    contact the {{ site.lead_institute }}.
  </p>
  <p><a class="btn btn--primary" href="mailto:{{ site.contact_email }}">Email the team</a></p>
  <p style="font-size:var(--t-sm);color:var(--c-muted);max-width:68ch">
    If a page shows a placeholder that you can fill, that is the most useful correction you can
    send — each page is a single markdown file and content changes require no code.
  </p>
</section>
