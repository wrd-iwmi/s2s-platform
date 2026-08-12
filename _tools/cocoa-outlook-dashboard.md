---
title: Cocoa Seasonal Outlook Dashboard (Ghana)
summary: Dashboard interface delivering district-level seasonal cocoa yield outlooks to COCOBOD, GMet and extension officers, co-designed alongside policy briefs.
status: In development
weight: 76
deliverables:
- D5
team:
- Salomon
tags:
- Agriculture
- Seasonal
- Machine learning
- Climate services
regions:
- Ghana
- Africa
problem: Cocoa planting, harvest timing and input allocation decisions are made ahead of the season with no district-level view of likely yield outcomes.
capabilities:
- title: District-level yield outlooks
  description: Seasonal yield probability and tercile risk categories published before the planting window.
- title: Policy briefs
  description: Dashboard outputs paired with policy briefs co-designed with GMet and extension officers.
workflow:
- stage: Seasonal forecasts
  detail: SEAS5 and NMME seasonal forecasts plus GMet national outlooks.
- stage: Bias correction
  detail: Forecast variables bias-corrected against CHIRPS and ERA5-Land baselines.
- stage: ML yield modelling
  detail: Random forest, XGBoost and Ridge/Lasso regression trained on historical yield and climate.
- stage: Packaging
  detail: Outputs converted to analysis-ready formats via the D3 APIs for dashboard ingestion.
- stage: Dashboard and briefs
  detail: District-level outlooks presented to COCOBOD, GMet and extension networks.
outputs:
- District-level yield probability
- Tercile risk categories for main and light crop
related_methods:
- ml-yield-forecasting
- bias-correction
related_case_studies:
- cocoa-yield-forecasting-ghana
links:
- label: Dashboard
  url: '#'
  kind: Web application
  available: false
  note: In development; delivery mechanism recorded in the programme material as a dashboard plus policy briefs.
---

## About this page

The programme material records the pilot delivery mechanism for the Ghana cocoa
work as dashboards and policy briefs co-designed with GMet and extension
officers, rather than a digital twin platform. Detailed specifications for the
dashboard have not been documented and are marked as outstanding below.
