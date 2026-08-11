---
title: Accessing forecast data via the API
summary: How to request downscaled S2S and seasonal forecast products through the interoperability toolkit and load them into an analysis environment.
status: Planned
weight: 100
deliverables:
- D4
tags:
- API
- Interoperability
- Capacity building
- S2S
regions:
- Global
difficulty: Beginner
objective: Request a downscaled forecast variable for a chosen area and lead time, and load the result into Python or R.
estimated_time: Information to be added
prerequisites:
- Basic familiarity with Python or R
- Ability to run a notebook locally or in a hosted environment
requirements:
- Access credentials for the forecast API (to be confirmed)
- Python 3 with xarray, or R
related_tool: interoperability-toolkit
links:
- label: API catalogue
  url: /apis/
  kind: Documentation
---

## Status

This tutorial is part of the Deliverable&nbsp;4 training programme, which covers
S2S forecasting, heat stress analysis, hydrological modelling, API use and
advisory co-design. It cannot be written until the
[Forecast Data Access API]({{ site.baseurl }}/apis/forecast-data-access-api/) is released, because
the steps depend on its endpoints and authentication model.

## What it will cover

1. Discovering available products through the STAC catalogue
2. Authenticating against the API
3. Requesting a variable for an area of interest and lead time
4. Loading GeoTIFF or Zarr output into xarray or R
5. Checking the metadata that accompanies the product
