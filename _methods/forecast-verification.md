---
title: Forecast verification and skill benchmarking
summary: Region-specific hindcast assessment of forecast skill, using decision-relevant metrics, to establish where S2S products can and cannot be relied upon.
status: In development
weight: 95
deliverables:
- D6
team:
- Giriraj
- Suman
- Ian
- Naga
- Petra
- Angie
- Dhyey
tags:
- Benchmarking
- Forecasting
- S2S
- Seasonal
regions:
- India
- Ghana
- Africa
- South Asia
objective: Evaluate S2S forecast skill for rainfall, soil moisture, heat stress and hydrological outcomes using simple, decision-relevant metrics, and produce scaling guidance from the result.
executive_summary: A forecast product is only useful if somebody has established how well it performs, where, and for which variable. The benchmarking work produces region-specific hindcast datasets and concise performance reports so that CGIAR teams can judge reliability before building a service on top of a product.
inputs:
- Hindcasts from the forecast systems used in the programme
- Observational and reanalysis reference datasets
outputs:
- Region-specific benchmarking datasets
- Performance reports and scaling guidance notes
strengths:
- Metrics chosen for decision-relevance rather than statistical convenience
- Feedback loop — skill results refine QBR parameters and model calibration
limitations:
- Skill established for one region and season does not transfer to another
validation: Hindcast validation against climatology and persistence baselines.
related_tools:
- interoperability-toolkit
coming_soon: true
---

## Metrics

| Metric | Applied to |
| --- | --- |
| RMSE, MAE | Continuous variables including yield |
| KGE, NSE | Streamflow |
| BSS (Brier skill score) | Tercile category forecasts |
| RPSS (ranked probability skill score) | Probabilistic tercile forecasts |

A Bayesian hierarchical multi-model ensemble is used in the South Asia
benchmarking work, feeding the Deliverable&nbsp;6 India performance report. The
Ghana hindcast validation dataset contributes to the Africa section.

## Documented hindcast domains

- Cauvery basin skill assessment
- Narmada and eastern India basins
- Odisha and Sri Lanka (listed as validation domains in the South Asia pilot)
- Ghana, for the cocoa yield application
