---
#  SUPERSEDED, NOT PUBLISHED.
#  This combined page was split into _tools/sadms.md and
#  _tools/sukharakshak-ai.md, which are the live pages. Kept for reference;
#  `published: false` leaves it out of the built site.
published: false
title: SADMS / SukhaRakshak AI
summary: Drought monitoring and advisory platform used to issue district-level drought triggers and to reach users through SMS and WhatsApp channels.
status: Operational
weight: 80
deliverables:
- D5
tags:
- Drought
- Early warning
- Agriculture
- Climate services
regions:
- South Asia
- India
problem: Drought advisories only change behaviour if they reach the people making planting and water-allocation decisions, in a channel they already use.
capabilities:
- title: District-level drought triggers
  description: Drought triggers issued at district scale.
- title: Last-mile dissemination
  description: SMS and WhatsApp channels for reaching farmers and local officials.
- title: Drought prediction at 2–3 week lead
  description: Consumes drought prediction at a 2–3 week lead time from the programme's S2S products.
workflow:
- stage: S2S forecasts
  detail: Sub-seasonal rainfall and temperature forecasts at 2–3 week lead.
- stage: Downscaling and indicators
  detail: QBR downscaling and drought indicator generation.
- stage: Platform ingestion
  detail: Products delivered through the D3 interoperability APIs.
- stage: Triggers and dissemination
  detail: District-level drought triggers pushed to SMS and WhatsApp channels.
outputs:
- District-level drought triggers
- SMS and WhatsApp advisories
related_tools:
- interoperability-toolkit
related_case_studies:
- s2s-irrigation-advisory-south-asia
links:
- label: SADMS platform
  url: '#'
  kind: Web application
  available: false
  note: Public URL to be confirmed by the platform team.
---

## About this page

SADMS / SukhaRakshak AI appears in the programme material as one of three
platforms serving different user tiers in the South Asia irrigation advisory
pilot, alongside CI-IDSS and AWARE. The content below is limited to what the
programme workplan records.

The expansion of the SADMS acronym and the governance arrangement between SADMS
and SukhaRakshak AI are not stated in the source material and are marked as
outstanding on this page.
