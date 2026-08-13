---
# ---------------------------------------------------------------------------
#  METHOD PAGE
#  Method pages are read at three levels. The settings below fill levels 1 and 3;
#  your writing underneath fills level 2.
# ---------------------------------------------------------------------------

# REQUIRED -------------------------------------------------------------------
title: Name of the method
summary: One sentence. What problem does this method solve?
executive_summary: >-
  LEVEL 1. Explain the method to someone who is not a specialist, in three or
  four sentences. No equations. Say what it takes in, what it gives back, and
  why that matters for a decision.

status: In development
weight: 50
# updated: 2026-08-13      # date this page was last checked
# published: false         # keeps the file but does not build the page
# coming_soon: true        # replaces the body with a "Coming soon" panel

tags:
  - Downscaling
regions:
  - South Asia
deliverables:
  - D2
team:
  - Your name

objective: What the method is meant to achieve, in one sentence.

# WHAT GOES IN AND WHAT COMES OUT --------------------------------------------
inputs:
  - Dataset or product used as input
outputs:
  - What the method produces

spatial_scale: e.g. district, basin, 0.05 degree grid
temporal_scale: e.g. 2–8 week lead time

# LEVEL 3 — implementation detail. Leave any of these out if not documented.
validation: How the method was tested, against what, in which region.
uncertainty: What the main sources of error are and how they are characterised.
compute_notes: What it takes to run — cores, memory, runtime, storage.
reproducibility: Where the code and configuration live, and what is needed to rerun it.

# HONEST ASSESSMENT ----------------------------------------------------------
strengths:
  - What this method does well
limitations:
  - Where it should not be used, or what it cannot do
  # Please fill this in. It is the most valuable part of a method page.

# PUBLICATIONS ---------------------------------------------------------------
# Leave this out entirely rather than adding a citation you have not checked.
references:
  - citation: "Author, A. (2026). Title. Journal, 1(1), 1–10."
    url: https://doi.org/...

links:
  - label: Methodology note
    url: "#"
    kind: Documentation
    available: false

related_tools:
  - interoperability-toolkit
---

## How it works

LEVEL 2. The technical explanation, for a colleague in a neighbouring field.
Equations, tables and diagrams belong here.

| Parameter | Value |
| --- | --- |
| Example | Example |

## Where it sits in the framework

Which stage of the [operational framework]({{ site.baseurl }}/about/#framework)
this method belongs to, and what runs before and after it.
