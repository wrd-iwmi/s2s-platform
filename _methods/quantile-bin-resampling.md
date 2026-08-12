---
title: Quantile Bin Resampling (QBR)
summary: Statistical downscaling method used to bring coarse S2S and seasonal forecast fields to the spatial scale at which irrigation and agricultural decisions are actually made.
status: In development
weight: 100
deliverables:
- D2
tags:
- Downscaling
- S2S
- Seasonal
- Bias correction
- Forecasting
regions:
- South Asia
- India
- Africa
objective: Produce decision-scale rainfall, temperature and derived fields from sub-seasonal and seasonal forecast products without discarding the forecast's probabilistic information.
executive_summary: Coarse-resolution forecasts cannot be used directly for a canal command area or a district. QBR resamples forecast values within quantile bins so that the downscaled series preserves the forecast signal while matching the local statistical distribution of the observed record.
spatial_scale: Irrigation command level in the South Asia application; district level in the Ghana application.
temporal_scale: Sub-seasonal (2–8 weeks) and seasonal (1–6 months) lead times.
inputs:
- IITM S2S forecasts (2–6 week precipitation and temperature)
- ECMWF ERF, SEAS5 and NMME forecast products
- AgERA5 reanalysis and CHIRPS/ERA5-Land observational baselines
outputs:
- Downscaled rainfall and temperature at irrigation command resolution
- Bias-corrected fields feeding hydrological, crop and water-balance models
strengths:
- Preserves the distributional characteristics of the local observed record
- Applicable across variables and forecast systems used in the programme
- Feeds directly into the coupled hydrology–crop modelling chain
limitations:
- Depends on the length and quality of the observational record used to define bins
- Statistical downscaling cannot create skill that is absent in the driving forecast
validation: Hindcast validation in the Cauvery basin, Narmada and eastern India basins, with skill feedback used to refine QBR parameters and model calibration.
related_tools:
- interoperability-toolkit
- ci-idss-digital-twin
- sadms
links:
- label: QBR methodology guide
  url: '#'
  kind: Documentation
  available: false
  note: Listed in the programme workplan as a capacity-building output under Deliverable 4.
coming_soon: true
---

## Where it sits in the framework

QBR is the core of Stage&nbsp;3 of the [S2S operational framework]({{ site.baseurl }}/about/#framework):
downscaling, modelling and indicator generation. It is applied after bias
correction and before the impact models that convert climate fields into
decision-relevant indicators.

## Technical explanation

The method is described in the programme material as *Quantile Bin Resampling*,
a novel statistical downscaling approach used to generate downscaled climate
products for CGIAR-wide S2S and seasonal datasets. In both documented
applications it is applied to precipitation and temperature and then propagated
through impact models:

- **South Asia** — QBR downscales IITM S2S forecasts to irrigation command
  resolution, which then drive the PARAM agro-hydrological model (Cauvery),
  SAC-SMA / GR4J (Narmada) and APSIM crop-water modelling.
- **Skill feedback** — hindcast validation in the Cauvery, Narmada and eastern
  India basins feeds back to refine QBR parameters and model calibration. The
  framework treats this as a closed loop rather than a one-off calibration.

## Implementation details

The full mathematical formulation, bin definition strategy, parameter set and
reference implementation have not been published in the material used to build
this site. They are recorded here as outstanding so that no reader mistakes a
summary for a specification.
