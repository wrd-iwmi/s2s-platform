---
title: Coupled hydrology–crop impact modelling
summary: Translation of downscaled climate fields into hydrological and agronomic quantities that a water manager or agronomist can act on.
status: In development
weight: 85
deliverables:
- D2
- D5
tags:
- Hydrology
- Crop modelling
- Water
- Irrigation
- S2S
regions:
- India
- South Asia
objective: Link downscaled S2S and seasonal forecasts with hydrological, crop and water-balance models to produce decision-relevant impact indicators.
executive_summary: A rainfall forecast is not a decision. Impact models convert downscaled climate fields into streamflow, soil moisture, crop water stress and water-balance terms, which are the quantities that irrigation and cropping decisions are actually made against.
spatial_scale: Basin and irrigation command scale.
temporal_scale: 2–6 week lead for irrigation scheduling; seasonal for planning.
inputs:
- QBR-downscaled rainfall and temperature at command resolution
- NASA SMAP soil moisture, GPM IMERG rainfall, NDVI and ET from Google Earth Engine
- AgERA5 reanalysis, ISRIC soil grids, CMIP6 for long-range context
outputs:
- Streamflow and canal inflow forecasts
- Soil moisture and ET/AET deficit
- Crop water stress indicators
strengths:
- Produces quantities that map directly onto an irrigation engineer's decision calendar
- Multiple model structures applied across basins rather than one model everywhere
limitations:
- Model calibration is basin-specific and does not transfer without re-calibration
- Compounding uncertainty — forecast error propagates through downscaling and then through the impact model
validation: Hindcast skill assessment in the Cauvery basin and Narmada / eastern India basins, using RMSE, KGE and NSE for streamflow.
related_tools:
- ci-idss-digital-twin
- aware
coming_soon: true
---

## Models used

The programme material names the following model components in the South Asia
application:

| Model | Role | Documented basin |
| --- | --- | --- |
| PARAM | Agro-hydrological modelling | Cauvery |
| SAC-SMA / GR4J | Rainfall–runoff modelling | Narmada |
| HEC | Hydrological modelling | Listed in the Stage 3 framework |
| APSIM | Crop–water modelling | South Asia application |

## Indicator outputs

ET/AET deficit, SPEI, VCI, canal inflow forecast and crop water stress are
listed as the indicators produced from this stage, alongside SPI, streamflow
and soil moisture in the general framework.
