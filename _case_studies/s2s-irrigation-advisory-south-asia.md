---
title: S2S irrigation advisory — South Asia
summary: Sub-seasonal forecasts downscaled to irrigation command scale to inform canal release timing and district drought triggers, delivered through three platforms serving three different user tiers.
status: Pilot
weight: 100
deliverables:
- D2
- D3
- D5
- D6
team:
- Suman
- Dhyey
- Niranga
- Surya Kiran
tags:
- Irrigation
- Water
- Drought
- S2S
- Downscaling
- Hydrology
- Early warning
regions:
- India
- Sri Lanka
- South Asia
location: Upper Krishna and Indira Gandhi Canal commands, India; validation in the Cauvery, Narmada and eastern India basins, Odisha and Sri Lanka
context: Irrigation engineers decide when to release canal water on a fixed decision calendar. Short-range weather forecasts arrive too late to change that decision and seasonal forecasts lack the timing precision it requires. The 2–6 week window is where the decision actually sits.
decision: Canal release timing at 2–6 week lead, and drought prediction at 2–3 week lead for the AWARE and SADMS platforms.
workflow:
- stage: Needs
  detail: 'End users are irrigation engineers and farmers in the Upper Krishna and Indira Gandhi Canal commands. Decision: when to release canal water, at 2–6 week lead. Priority variables: rainfall, evapotranspiration, soil moisture.'
- stage: Datasets
  detail: IITM S2S forecasts bias-corrected to command level; Earth observation inputs from SMAP, GPM IMERG and Google Earth Engine; AgERA5, ISRIC and CMIP6 for context.
- stage: Downscale, model and generate indicators
  detail: 'QBR downscaling to irrigation command resolution, driving the PARAM agro-hydrological model (Cauvery), SAC-SMA / GR4J (Narmada) and APSIM crop-water modelling. Indicators: ET/AET deficit, SPEI, VCI, canal inflow forecast, crop water stress. Packaged from NetCDF to GeoTIFF and Zarr via the D3 APIs.'
- stage: Pilots and capacity
  detail: 'CI-IDSS Digital Twin v1 (Upper Krishna) extended to v2 with S2S irrigation advisories; AWARE dashboard integration providing 1–7 day alerts and 7–30 day outlooks; SADMS / SukhaRakshak AI issuing district-level drought triggers over SMS and WhatsApp. Capacity outputs: QBR methodology guide and CMIP6 downscaling notebooks on GitHub.'
- stage: Benchmarking
  detail: 'Cauvery basin skill assessment plus Narmada and eastern India basins. Metrics: RMSE, KGE and NSE for streamflow; BSS and RPSS for tercile forecasts. Bayesian hierarchical multi-model ensemble feeding the D6 India performance report.'
climate_information:
- IITM S2S forecasts — 2–6 week precipitation and temperature, bias-corrected via QBR to command level
- NASA SMAP soil moisture
- GPM IMERG rainfall
- NDVI and ET from Google Earth Engine
- AgERA5 reanalysis
- ISRIC soil grids
- CMIP6 for long-range context
end_users:
- Irrigation engineers
- Farmers in the Upper Krishna and Indira Gandhi Canal commands
- District drought management officers
lessons:
- The three delivery platforms each serve a different user tier — a technical digital twin, an operational dashboard, and a last-mile SMS/WhatsApp channel. One interface would not have reached all three audiences.
- 'Hindcast validation is treated as a feedback loop: skill results in the Cauvery, Odisha and Sri Lanka domains are used to refine QBR parameters and model calibration rather than simply reported.'
related_tools:
- ci-idss-digital-twin
- aware
- sadms-sukharakshak
- interoperability-toolkit
related_methods:
- quantile-bin-resampling
- impact-modelling
- indicator-generation
- forecast-verification
---

## Why this case matters

This is the reference implementation of the [five-stage operational
framework]({{ site.baseurl }}/about/#framework). Every stage in the generic framework has a
concrete counterpart here, which makes it the clearest worked example of how a
forecast becomes a decision.

The entry point is deliberately not the forecast — it is the irrigation
engineer's decision calendar. The forecast system, the downscaling method and
the delivery platform are all selected to fit a decision that already exists.

## Results

Results and adoption evidence are being generated through the
Deliverable&nbsp;5 monitoring and learning activity, which assesses adoption,
behavioural response, forecast use and links to early-warning protocols and
safety-net financing. Findings have not been published yet.
