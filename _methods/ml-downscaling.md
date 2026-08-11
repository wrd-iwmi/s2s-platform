---
title: Machine-learning and cGAN downscaling
summary: Learned downscaling approaches used alongside QBR in Stage 3 of the framework.
status: Planned
weight: 70
deliverables:
- D2
tags:
- Downscaling
- Machine learning
- S2S
- Forecasting
regions:
- Global
objective: Generate high-resolution forecast fields using learned mappings between coarse forecast input and high-resolution observed or reanalysis targets.
executive_summary: In addition to the statistical QBR route, the programme's Stage 3 workflow lists conditional generative adversarial networks and other machine-learning approaches as downscaling options for producing decision-scale fields.
inputs:
- Coarse-resolution S2S and seasonal forecast fields
- High-resolution observational and reanalysis targets
outputs:
- Downscaled forecast fields at decision scale
limitations:
- Learned downscaling requires substantial training data and careful validation against physical plausibility
- Skill assessment must distinguish realistic-looking output from genuinely skilful output
related_tools:
- interoperability-toolkit
---

## Status

The programme's Stage&nbsp;3 description lists "QBR / cGAN / ML downscaling" as
the downscaling options feeding the hydrological models. Of these, QBR is the
method described in detail in the programme material. The cGAN and broader
machine-learning routes are recorded as part of the approach but are not yet
specified.
