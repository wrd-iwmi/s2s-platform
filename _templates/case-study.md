---
# ---------------------------------------------------------------------------
#  CASE STUDY PAGE
#  Start from the decision somebody had to make, not from the dataset.
# ---------------------------------------------------------------------------

title: What was done, and where
summary: One sentence covering the decision, the information used and who used it.

location: Country, basin or district
context: >-
  What problem existed before? Whose problem was it, and on what timescale did
  they have to decide? Three or four sentences.

status: Pilot
weight: 50
# updated: 2026-08-13      # date this page was last checked
# published: false         # keeps the file but does not build the page
# coming_soon: true        # replaces the body with a "Coming soon" panel

tags:
  - Irrigation
regions:
  - India
deliverables:
  - D5
team:
  - Researcher name
partners:
  - Partner organisation

end_users:
  - Who actually used the information

climate_information:
  - Forecast or observational product used
  - Another one

# THE PIPELINE — the five stages of the operational framework -------------------
workflow:
  - stage: Needs
    detail: Who the end user is, what they decide, at what lead time.
  - stage: Datasets
    detail: What went in.
  - stage: Downscale, model and generate indicators
    detail: What was done to it.
  - stage: Pilots and capacity
    detail: How it reached people.
  - stage: Benchmarking
    detail: How skill was assessed.

decision: The decision the information fed into, and at what lead time.

# results: What was produced or learned. Leave out until evidence exists.

lessons:
  - What worked, or what did not

related_tools:
  - aware
related_methods:
  - quantile-bin-resampling

# WHERE TO GET IT ------------------------------------------------------------
# kind: Web application | API | Dataset | Repository | Documentation |
#       Download | Demonstration | Publication
links:
  - label: Pilot report
    url: "#"
    kind: Publication
    available: false          # shows "Not yet public" instead of a broken link
---

## Why this case matters

The wider point. What does this example show that a reader should take to their
own context?

## Results

If evidence is not published yet, leave the `results` field out of the settings
above — the page will say so clearly rather than implying an outcome.
