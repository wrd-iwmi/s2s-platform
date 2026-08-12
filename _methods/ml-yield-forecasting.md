---
title: Machine-learning seasonal yield forecasting
summary: Statistical learning models that convert seasonal climate predictors into district-level crop yield probabilities.
status: In development
weight: 75
deliverables:
- D5
team:
- Salomon
tags:
- Machine learning
- Agriculture
- Seasonal
- Forecasting
regions:
- Ghana
- Africa
objective: Produce district-level probabilistic cocoa yield outlooks ahead of the planting window.
executive_summary: Where a process-based crop model is impractical, a learned model trained on historical yield and climate records can produce probabilistic district-level yield outlooks from seasonal forecast predictors.
spatial_scale: District.
temporal_scale: Seasonal.
inputs:
- Cocoa-relevant climate indices — rainfall onset, dry spell duration, humidity
- SEAS5 and NMME seasonal forecasts, GMet national outlooks
- District cocoa yield records; CHIRPS rainfall; ERA5-Land temperature and humidity
outputs:
- District-level yield probability
- Tercile risk categories for main and light crop
strengths:
- Produces a probabilistic impact indicator directly, without a calibrated process model
- Predictors are climate indices with an agronomic interpretation, not opaque features
limitations:
- Skill is bounded by the length and quality of the district yield record
- A model trained on historical relationships may degrade if those relationships shift
validation: Hindcast comparison of model skill against a climatology baseline and a persistence benchmark, with cross-validation; RMSE and MAE for yield, Brier skill score for tercile categories.
related_tools:
- cocoa-outlook-dashboard
coming_soon: true
---

## Model family

Random forest, XGBoost and Ridge/Lasso regression are the model structures
recorded for this work, trained on historical yield combined with climate
predictors.

## Benchmarking

The Ghana hindcast validation dataset is contributed to the Africa section of
the Deliverable&nbsp;6 benchmarking dataset, so that this pilot's skill is
assessed on the same terms as the rest of the programme.
