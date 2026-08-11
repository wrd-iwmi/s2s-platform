---
title: STAC Catalogue
summary: SpatioTemporal Asset Catalog interface describing the programme's forecast and derived indicator products.
status: In development
weight: 90
deliverables:
- D3
tags:
- API
- Interoperability
- Earth observation
- S2S
regions:
- Global
version: Unreleased
purpose: Make forecast products discoverable and machine-readable through a standard catalogue specification rather than a bespoke index.
authentication: Information to be added
response_formats:
- JSON (STAC)
related_tool: interoperability-toolkit
links:
- label: STAC specification
  url: https://stacspec.org/
  kind: Documentation
---

## Role in the toolkit

The Deliverable&nbsp;3 interoperability toolkit spans all five stages of the
operational framework and is described as providing "STAC APIs, Python/R
wrappers, GitHub docs, FAIR data framework". The STAC catalogue is the
discovery layer of that toolkit: it describes each product's spatial and
temporal extent, provenance and asset locations in a format that existing
geospatial tooling already understands.

## Catalogue structure

The collection hierarchy, item properties and extensions in use have not been
published yet.
