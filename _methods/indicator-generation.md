---
title: Agro-climate and drought indicator generation
summary: Derivation of standardised drought, hydrological and agro-climate indicators from downscaled forecast and observational fields.
status: In development
weight: 80
deliverables:
- D2
- D3
tags:
- Drought
- Agriculture
- Water
- Earth observation
- S2S
regions:
- South Asia
- Africa
- India
- Ghana
objective: Provide a consistent indicator layer so that every downstream platform interprets the same quantity in the same way.
executive_summary: Raw forecast fields are converted into a small set of standardised indicators — drought indices, vegetation condition, evapotranspiration anomaly, soil moisture and streamflow — that platforms and advisory services consume in place of raw climate variables.
inputs:
- QBR-downscaled forecast fields
- Earth observation inputs — SMAP soil moisture, GPM IMERG rainfall, NDVI and ET from Google Earth Engine
outputs:
- SPI and SPEI
- Vegetation Condition Index (VCI)
- ET anomaly and ET/AET deficit
- Streamflow and soil moisture
- Probabilistic composite indicators
limitations:
- Indicator values inherit the uncertainty of both the forecast and the observational input
- Standardised indices require a stable reference period; results shift if the baseline changes
related_tools:
- interoperability-toolkit
- sadms
coming_soon: true
---

## Position in the six-layer model

Indicator generation is Layer&nbsp;4 of the [six-layer model]({{ site.baseurl }}/about/#six-layer-model):
drought and soil moisture indicators, hydrological indicators, agro-climate
indicators and probabilistic composite indicators sit between the forecast tiers
and the application services that consume them.
