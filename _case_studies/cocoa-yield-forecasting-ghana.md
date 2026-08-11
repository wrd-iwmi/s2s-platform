---
title: S2S cocoa yield forecasting — Ghana
summary: Seasonal forecasts and machine-learning yield models producing district-level cocoa yield probabilities for COCOBOD, delivered through a dashboard and co-designed policy briefs.
status: Pilot
weight: 90
deliverables:
- D2
- D3
- D5
- D6
team:
- Salomon
tags:
- Agriculture
- Seasonal
- Machine learning
- Climate services
- Forecasting
regions:
- Ghana
- Africa
location: Ghana — district scale
context: Cocoa planting and harvest timing and input allocation are decided ahead of the season. The decision needs a district-scale view of likely yield, at seasonal lead time — a different problem from the sub-seasonal water-release question in South Asia, using the same five-stage pipeline.
decision: Planting and harvest timing and input allocation at seasonal lead time.
workflow:
- stage: Needs
  detail: 'End users are COCOBOD, GMet, extension officers and cocoa farmers. Decision: planting and harvest timing, input allocation. Lead time: seasonal. Variable: yield probability.'
- stage: Datasets
  detail: SEAS5 and NMME seasonal forecasts plus GMet national outlooks; CHIRPS rainfall, ERA5-Land temperature and humidity and district cocoa yield records as observations. Bias correction applied to forecast variables against CHIRPS and ERA5-Land baselines.
- stage: Feature engineering, ML models and indicators
  detail: 'Predictors are cocoa-relevant climate indices — rainfall onset, dry spell duration, humidity. Models: random forest, XGBoost and Ridge/Lasso regression trained on historical yield and climate. Indicators: district-level yield probability and tercile risk categories for main and light crop. Outputs packaged to analysis-ready formats via the D3 APIs for dashboard ingestion.'
- stage: Pilots and dissemination
  detail: Co-design with GMet, COCOBOD and extension services covering the dashboard interface and policy briefs. District-level seasonal yield outlooks published before the planting window. Stakeholder workshops provide forecast interpretation training for extension officers, with integration into CGIAR extension networks for last-mile delivery.
- stage: Benchmarking
  detail: 'Hindcast comparison of ML model skill against a climatology baseline and a persistence benchmark. Metrics: RMSE and MAE for yield, BSS for tercile categories, with cross-validation. The Ghana hindcast validation dataset is contributed to the D6 Africa section.'
climate_information:
- SEAS5 and NMME seasonal forecasts
- GMet national outlooks
- CHIRPS rainfall
- ERA5-Land temperature and humidity
- District cocoa yield records
end_users:
- COCOBOD
- Ghana Meteorological Agency (GMet)
- Extension officers
- Cocoa farmers
partners:
- COCOBOD
- GMet
- CGIAR extension networks
lessons:
- 'The same five-stage pipeline holds even when almost every component differs: a different end user, a different forecast source, a learned model instead of a process-based one, and a dashboard plus policy briefs instead of a digital twin.'
- The output remains a probabilistic impact indicator at district scale — the pipeline standardises the shape of the answer, not the machinery that produces it.
related_tools:
- cocoa-outlook-dashboard
- interoperability-toolkit
related_methods:
- ml-yield-forecasting
- bias-correction
- forecast-verification
---

## Contrast with the South Asia pilot

Read alongside the [South Asia irrigation advisory]({{ site.baseurl }}/case-studies/s2s-irrigation-advisory-south-asia/),
this case is the programme's argument for a shared framework. The two pilots
differ in end user, forecast source, model family and delivery mechanism, yet
they occupy the same five stages and exchange data through the same
interoperability toolkit.

## Results

Adoption and behavioural evidence is being generated through the
Deliverable&nbsp;5 monitoring and learning activity. Findings have not been
published yet.
