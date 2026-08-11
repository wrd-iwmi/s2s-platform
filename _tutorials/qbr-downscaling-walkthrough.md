---
title: QBR downscaling — methodology walkthrough
summary: Step-by-step guide to applying Quantile Bin Resampling to a coarse forecast field, from preparing the observational baseline to validating the downscaled output.
status: Planned
weight: 95
deliverables:
- D4
tags:
- Downscaling
- S2S
- Bias correction
- Capacity building
regions:
- Global
difficulty: Advanced
objective: Apply QBR downscaling to a sub-seasonal forecast field and assess the result against a hindcast baseline.
estimated_time: Information to be added
prerequisites:
- Working knowledge of statistical downscaling and bias correction
- Experience handling gridded climate data in Python
requirements:
- A coarse-resolution forecast dataset
- A high-resolution observational baseline
related_method: quantile-bin-resampling
links:
- label: QBR method page
  url: /methods/quantile-bin-resampling/
  kind: Documentation
- label: QBR methodology guide
  url: '#'
  kind: Documentation
  available: false
---

## Status

The programme workplan lists a **QBR methodology guide** as a capacity-building
output. This tutorial will be built on that guide. It is listed here so that the
learning pathway is visible, not because content exists.

## What it will cover

1. Preparing the observational baseline and defining quantile bins
2. Applying the resampling to a forecast field
3. Propagating the downscaled field into an impact model
4. Validating against a hindcast and interpreting the skill scores
5. Feeding skill results back into parameter refinement
