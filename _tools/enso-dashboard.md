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
ENSO is a major driver of climate variability, but the information needed to understand its
implications is fragmented across climate forecasts, Earth observation products, hydrological datasets,
agricultural indicators and food-market information. Decision-makers are often left to interpret these
signals separately, making it difficult to move from a global climate signal to an understanding of
where risks may emerge and which sectors could be affected.
The ENSO Dashboard brings these disparate sources together in a single, interactive platform, combining
ENSO monitoring and forecasts with seasonal and sub-seasonal outlooks, water stress, hydrological and
Earth observation indicators, and food-price signals. It provides a common evidence base for exploring
how an evolving ENSO state may translate into risks for water, agriculture and food systems, supporting
earlier interpretation and more informed anticipatory action.
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
