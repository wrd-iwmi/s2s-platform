---
# ---------------------------------------------------------------------------
#  TOOL PAGE
#  Delete any line you cannot fill in. Do not guess.
#  Keep the --- lines at the top and bottom of this block.
# ---------------------------------------------------------------------------

# REQUIRED -------------------------------------------------------------------
title: Name of the tool
summary: One sentence saying what it does and who it is for. Shown on cards and in search.

# STATUS AND SORTING ---------------------------------------------------------
status: In development     # Operational | In development | Pilot | Planned | Documentation pending
weight: 50                 # higher numbers appear first in the tools list
flagship: false            # true puts this tool on the homepage

# LABELS — these become the filter buttons. Reuse existing ones where you can.
tags:
  - Drought
  - Early warning
regions:
  - India
deliverables:
  - D5
team:
  - Your name

# THE PROBLEM ----------------------------------------------------------------
problem: >-
  What was hard before this tool existed? Two or three sentences. Write it from
  the point of view of the person who has to make a decision.

organisation: IWMI — CGIAR Climate Action

# WHAT IT DOES — becomes a grid of cards --------------------------------------
capabilities:
  - title: First capability
    description: One or two sentences.
  - title: Second capability
    description: One or two sentences.

# HOW IT WORKS — becomes the numbered flow diagram ----------------------------
workflow:
  - stage: Input data
    detail: Which datasets go in.
  - stage: Processing
    detail: What happens to them.
  - stage: Products
    detail: What comes out.
  - stage: Delivery
    detail: How a user gets it.

# WHAT THE USER GETS ---------------------------------------------------------
outputs:
  - A product the user receives
  - Another product

# WHERE TO GET IT ------------------------------------------------------------
# kind: Web application | API | Dataset | Repository | Documentation |
#       Download | Demonstration | Publication
links:
  - label: Web application
    url: https://example.org
    kind: Web application
  - label: Source code
    url: "#"
    kind: Repository
    available: false          # shows "Not yet public" instead of a broken link
    note: Repository not published yet.

# CROSS-LINKS — file names without the .md ------------------------------------
related_methods:
  - quantile-bin-resampling
related_case_studies:
# citation: How to cite this tool. Leave out until it has been agreed.
---

## About this tool

Write the main description here. Use `##` for headings, blank lines between
paragraphs.

Link to another page on this site like this:
[Quantile Bin Resampling]({{ site.baseurl }}/methods/quantile-bin-resampling/)

## Technical basis

What it is built on. Datasets, models, assumptions, resolution.

If something is not documented yet, say so with a placeholder rather than
guessing:

{% include placeholder.html what="Model configuration to be added" %}
