---
title: Bias correction of forecast fields
summary: Correction of systematic forecast error against an observational baseline, applied before downscaling and impact modelling.
status: In development
weight: 90
deliverables:
- D2
tags:
- Bias correction
- Downscaling
- Seasonal
- S2S
- Forecasting
regions:
- South Asia
- Africa
- Ghana
- India
objective: Remove systematic error from multi-model forecast fields so that downscaled products and impact models are not driven by model drift.
executive_summary: Forecast models carry systematic biases that vary by region, season and variable. Bias correction adjusts forecast fields against a reference observational dataset so that downstream models receive inputs consistent with the local climate.
temporal_scale: Sub-seasonal and seasonal lead times.
inputs:
- Multi-model ensemble forecasts (IITM S2S, ECMWF ERF, SEAS5, NMME)
- Observational baselines — CHIRPS rainfall, ERA5-Land temperature and humidity, AgERA5 reanalysis
outputs:
- Bias-corrected rainfall, temperature and derived forecast fields
strengths:
- Standard, well-understood prerequisite for impact modelling
- Applied consistently across both documented country applications
limitations:
- Correction is only as good as the reference dataset, which carries its own uncertainty
- Cannot correct errors in the timing or spatial structure of a forecast, only its distribution
validation: Assessed as part of the Deliverable 6 benchmarking work, using hindcast skill against climatology and persistence baselines.
related_tools:
- interoperability-toolkit
---

## Documented applications

- **South Asia** — IITM S2S 2–6 week precipitation and temperature forecasts are
  bias-corrected via QBR to command level.
- **Ghana** — SEAS5 and NMME seasonal forecast variables are bias-corrected
  against CHIRPS and ERA5-Land baselines before entering the yield models.

## Implementation details

The specific bias-correction formulation used for each variable and region is
not documented in the material used to build this site.
