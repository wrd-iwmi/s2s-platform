---
title: ENSO Dashboard
summary: Dashboard bringing together ENSO indices, food prices, Earth observation indicators, forecast layers and water stress. Its API is live and fully documented.
status: Operational
flagship: true
weight: 100
tags:
- Seasonal
- Forecasting
- Climate services
regions:
- Global
problem: >-
  Climate information relevant to ENSO impacts is fragmented across forecasts, Earth observation,
  hydrological, agricultural and food-market datasets, making it difficult to translate global
  climate signals into actionable information. The ENSO Dashboard integrates these diverse sources
  in a single platform, enabling users to explore emerging risks across water, agriculture and
  food systems and support informed anticipatory action.
related_apis:
  - enso-dashboard-api
links:
  - label: ENSO Dashboard
    url: https://enso.iwmi.org/
    kind: Web application
  - label: ENSO Dashboard API documentation
    url: /apis/enso-dashboard-api/
    kind: API
  - label: Interactive API documentation (Swagger)
    url: https://enso.iwmi.org/ENSO_api/docs
    kind: Documentation
---

## Status of this page

The dashboard and its API is live — see the
[ENSO Dashboard API]({{ site.baseurl }}/apis/enso-dashboard-api/), which lists
146 endpoints across twelve groups, read from the live OpenAPI specification.

What that API serves tells you a good deal about the dashboard's scope: ENSO
indices and phase probabilities, WFP market food prices, FAO Food Price Index,
Earth observation drought and vegetation indicators, seasonal and sub-seasonal
forecast layers, hydrology and basins, and WRI Aqueduct water stress.

The **descriptive material for the dashboard itself has not been supplied**,
so the sections below remain outstanding. Nothing here has been inferred from
the API.

To complete this page the team needs to supply:

- the public URL of the dashboard interface
- who it is built for, and the decisions it supports
- which visualisations it offers, and how they are intended to be read
- its data architecture and update schedule
- access conditions and licence
- validation, known limitations and a citation
