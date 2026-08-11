---
title: Forecast Data Access API
summary: Planned standardised API for requesting downscaled S2S and seasonal forecast products, developed under the CGIAR Forecast Interoperability & Data Access Toolkit.
status: In development
weight: 100
deliverables:
- D3
team:
- Giriraj
- Angie
- Dhyey
- Kalpani
tags:
- API
- Interoperability
- S2S
- Seasonal
- Climate services
regions:
- Global
version: Unreleased
purpose: Give every CGIAR platform and national partner one consistent way to request a forecast variable, at a given lead time, in an analysis-ready format.
authentication: Information to be added
response_formats:
- GeoTIFF
- Zarr
- NetCDF
related_tool: interoperability-toolkit
links:
- label: Interoperability toolkit
  url: /tools/interoperability-toolkit/
  kind: Documentation
---

## What is defined so far

The programme workplan commits to designing and deploying standardised APIs,
metadata schemas and data pipelines compatible with the AoW1 Data Hub and CGIAR
digital platforms, to ensure consistent forecast access and exchange.

The following are recorded in the programme material and are therefore stated
here as design intent rather than as a released interface:

- **Products served** — downscaled S2S and seasonal forecasts: rainfall,
  temperature, soil moisture, heat-stress indices, evapotranspiration, runoff
  and hydrological variables.
- **Formats** — NetCDF converted to GeoTIFF and Zarr for analysis-ready delivery.
- **Consumers** — AWARE, SADMS / SukhaRakshak AI and CI-IDSS, plus the Ghana
  cocoa outlook dashboard, all ingest products through this route.
- **Compatibility target** — the AoW1 Data Hub and Alliance data infrastructure.

## Endpoints

No public endpoints have been published. Endpoint paths, parameters, response
schemas, rate limits and authentication will be documented on this page as they
are released. They are deliberately left blank rather than illustrated with
plausible-looking examples.
