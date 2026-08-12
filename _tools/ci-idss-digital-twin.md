---
title: CI-IDSS Digital Twin
summary: Digital twin platform for the Upper Krishna basin, being extended from v1 to a v2 that carries S2S irrigation advisories.
status: In development
weight: 80
deliverables:
- D5
tags:
- Water
- Irrigation
- Hydrology
- S2S
- Climate services
regions:
- India
- South Asia
problem: Canal release decisions are made on a fixed calendar with limited forward information. A basin-scale digital twin lets an irrigation engineer test release timing against a forecast rather than against climatology alone.
capabilities:
- title: Basin digital twin
  description: Version 1 covers the Upper Krishna basin.
- title: S2S irrigation advisories
  description: Version 2 adds S2S irrigation advisories to the twin.
- title: Technical user tier
  description: Serves the most technical of the three user tiers in the South Asia pilot.
workflow:
- stage: Forecast inputs
  detail: IITM S2S precipitation and temperature at 2–6 week lead, bias-corrected to command level via QBR.
- stage: Hydrological modelling
  detail: PARAM agro-hydrological model (Cauvery), SAC-SMA / GR4J (Narmada) and APSIM crop-water modelling.
- stage: Indicator generation
  detail: Canal inflow forecast, crop water stress, ET/AET deficit.
- stage: Digital twin
  detail: Indicators surfaced in the CI-IDSS twin for irrigation planning.
outputs:
- Canal inflow forecasts
- Crop water stress indicators
related_methods:
- quantile-bin-resampling
- impact-modelling
links:
- label: CI-IDSS platform
  url: '#'
  kind: Web application
  available: false
  note: Public URL to be confirmed by the platform team.
---

## About this page

CI-IDSS is recorded in the programme material as a digital twin platform whose
v1 covers the Upper Krishna basin and whose v2 will carry S2S irrigation
advisories. The expansion of the CI-IDSS acronym is not given in the source
material.
