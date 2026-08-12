---
title: ENSO Dashboard API
summary: Live REST API behind the ENSO Dashboard — ENSO indices and probabilities, food prices, Earth observation indicators, seasonal and sub-seasonal forecast layers, hydrology and water stress.
purpose: >-
  Give analysts and developers direct access to the data behind the ENSO
  Dashboard, so an indicator can be pulled into a notebook, a national bulletin
  or another platform without re-implementing the processing behind it.
status: Operational
version: "1.0.0"
weight: 200
tags:
  - API
  - Seasonal
  - Forecasting
  - Drought
  - Earth observation
  - Climate services
  - Agriculture
  - Water
regions:
  - Global
base_url: https://enso.iwmi.org/ENSO_api
authentication: None required. The endpoints listed here are open and need no key or token.
response_formats:
  - JSON
  - PNG (XYZ map tiles)
  - GeoJSON
coverage: Global, with country and admin-level breakdowns. ONI series run from 1950 to the present.
related_tool: enso-dashboard
swagger_spec: /assets/api/enso-selected.json

endpoints:
  - path: /api/v1/enso/current-phase
    method: GET
    description: >-
      The latest ENSO phase — value, season, phase code and label — with the
      provenance of how it was derived.
    example_request: |
      curl https://enso.iwmi.org/ENSO_api/api/v1/enso/current-phase
    example_response: |
      {
        "value": 0.5,
        "date": "2026-05",
        "season": "AMJ",
        "phase_code": "WE",
        "phase_label": "Weak El Niño",
        "method": {
          "label": "Current ONI value",
          "provenance": "EXT",
          "formula": "Latest non-null monthly row in oni_timeseries.csv",
          "sources": [
            { "name": "NOAA CPC ONI v5", "role": "input" }
          ]
        }
      }

  - path: /api/v1/enso/oni
    method: GET
    description: Oceanic Niño Index series.
    parameters:
      - name: lead_months
        type: integer
        required: false
        description: "Lead time in months. Default 3."
      - name: start_year
        type: integer
        required: false
        description: First year of the returned series.
    example_request: |
      curl "https://enso.iwmi.org/ENSO_api/api/v1/enso/oni?lead_months=3&start_year=2000"

  - path: /api/v1/enso/probabilities
    method: GET
    description: >-
      El Niño, neutral, La Niña and strong-El Niño probabilities for a
      three-month window, returned alongside the climatological baseline and the
      full derivation.
    parameters:
      - name: window
        type: string
        required: true
        description: 'Three-month season label, for example DJF, AMJ, JAS.'
    example_request: |
      curl "https://enso.iwmi.org/ENSO_api/api/v1/enso/probabilities?window=DJF"
    example_response: |
      {
        "window": "DJF",
        "el_nino": 0.354,
        "neutral": 0.311,
        "la_nina": 0.335,
        "strong_plus": 0.101,
        "climatology": {
          "el_nino": 0.377, "neutral": 0.273,
          "la_nina": 0.351, "strong_plus": 0.117
        },
        "n_historical": 77,
        "method": {
          "formula": "P_window(phase) = 0.6 · climatology + 0.4 · persistence (AR(1) projection of recent ONI)",
          "thresholds": {
            "el_nino": "ONI ≥ +0.5", "neutral": "|ONI| < 0.5",
            "la_nina": "ONI ≤ −0.5", "strong_plus": "ONI ≥ +1.5"
          },
          "limits": "Single-source statistical projection; not a multi-model ensemble. Skill drops sharply past lead 6 months."
        }
      }

  - path: /api/v1/enso/soi
    method: GET
    description: Southern Oscillation Index series. No parameters.

  - path: /api/v1/enso/iod
    method: GET
    description: Indian Ocean Dipole series. No parameters.

  - path: /api/v1/enso/events
    method: GET
    description: Catalogue of historical ENSO events. No parameters.

  - path: /api/v1/enso/oni-historical
    method: GET
    description: Full historical ONI record.
    parameters:
      - name: start_year
        type: integer
        required: false
        description: "First year returned. Default 1950."

links:
  - label: Interactive API documentation (Swagger)
    url: https://enso.iwmi.org/ENSO_api/docs
    kind: Documentation
  - label: OpenAPI specification
    url: https://enso.iwmi.org/ENSO_api/openapi.json
    kind: API
  - label: ENSO Dashboard
    url: /tools/enso-dashboard/
    kind: Web application
---

## What is available

The API exposes **146 endpoints across twelve groups**. Everything below is read
from the live OpenAPI specification, which is the authoritative list.

| Group | Endpoints | What it covers |
| --- | ---: | --- |
| `gee` | 28 | Earth observation indicators from Google Earth Engine — SPI, dry spells, accumulated precipitation, NDVI anomaly, ASIS, SMAP soil moisture, GFS and IRI layers. Point queries, time series, statistics and XYZ map tiles. |
| `forecasts` | 25 | Forecast layers and statistics: IRI, CFS, GEFS, SEAS5, **ECMWF S2S**, GloFAS river discharge and GRACE. Tiles, admin-level aggregates, point series and metadata. |
| `hydro` | 18 | Basins, rivers, lakes and reservoirs. Basin detail and geometry, lake anomalies, basin population, ENSO–basin signal and crop–basin risk. |
| `wfp` | 17 | WFP market food prices — series, indices, anomalies, seasonality, spread, and rankings by commodity, market and country. |
| `enso` | 14 | The core indices and diagnostics: ONI, SOI, IOD, phase probabilities, current phase, historical events, analogue-year scenarios and KPIs. |
| `fao` | 12 | FAO Food Price Index — series, anomalies, correlation with ONI, sensitivity and scenario trajectories. |
| `aqueduct` | 10 | WRI Aqueduct water stress by country and admin-1, monthly and seasonal profiles, future projections, alerts and tiles. |
| `dashboard` | 9 | Composed briefing products: outlook, country brief, region brief, basin brief, advisory, forecasts, comparison and bulletin. |
| `crops` | 5 | Crop calendars, ENSO risk by crop, current phase matching and country lists. |
| `catalog` | 4 | Layer catalogue, summary and diagnostics — a machine-readable index of what the API serves. |
| `population` | 2 | Population statistics and exposed population. |
| `basins` | 2 | Major river basin list and detail. |

## Provenance is built into the response

Worth knowing before you use it: most endpoints return a `method` block
alongside the values, carrying the label, the formula, the processing steps, the
upstream sources and — where relevant — an explicit statement of limits.

The probability endpoint, for example, returns its own caveat:

> "Single-source statistical projection; not a multi-model ensemble. Skill drops
> sharply past lead 6 months."

That makes the products self-documenting: an analyst pulling a number into a
national bulletin gets the derivation and the caveat in the same payload. If you
are building on this API, carry that `method` block through to your users rather
than discarding it.

## Two base URLs

Use the public hostname:

```
https://enso.iwmi.org/ENSO_api
```

A direct IP address also serves the same API on the internal network. It is not
documented here because it is not a stable public endpoint — it has no TLS and
no guarantee of continuity. Always integrate against the hostname.

## Getting started

```python
import requests

BASE = "https://enso.iwmi.org/ENSO_api/api/v1"

phase = requests.get(f"{BASE}/enso/current-phase").json()
print(phase["phase_label"], "-", phase["date"])

probs = requests.get(f"{BASE}/enso/probabilities", params={"window": "DJF"}).json()
for k in ("el_nino", "neutral", "la_nina"):
    print(f"{k:>8}: {probs[k]:.0%}  (climatology {probs['climatology'][k]:.0%})")
```

The full interactive documentation, with every parameter and a "try it" button
for each of the 146 endpoints, is in the Swagger UI linked above.

## Rate limits and support

{% include placeholder.html what="Rate limits and support arrangements to be confirmed" note="No rate limit is published. Be considerate with automated polling, and contact the team before building a service that depends on high request volumes." %}
