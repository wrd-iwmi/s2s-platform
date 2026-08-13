---
# ---------------------------------------------------------------------------
#  TUTORIAL PAGE
# ---------------------------------------------------------------------------

title: Title of the tutorial
summary: One sentence describing what the reader will learn.
objective: >-
  By the end of this tutorial the reader will be able to … Write one concrete,
  checkable outcome.

difficulty: Beginner      # Beginner | Intermediate | Advanced
status: Planned           # change to Operational once the steps are written
weight: 50
estimated_time: 45 minutes
# updated: 2026-08-13     # date this page was last checked
# published: false        # keeps the file but does not build the page
# coming_soon: true       # replaces the body with a "Coming soon" panel

tags:
  - Capacity building
regions:
  - Global
deliverables:
  - D4

prerequisites:
  - What the reader needs to know already
requirements:
  - Software, accounts or data they need to have

related_tool: interoperability-toolkit
related_method: quantile-bin-resampling

# If this tutorial is a Jupyter notebook, do not write it here — put the .ipynb
# in notebooks/ and run _scripts/notebook_to_page.py. That sets `notebook:` and
# `generated_from_notebook:` for you, and the page then carries download, Colab
# and nbviewer buttons. See notebooks/README.md.
# notebook: /notebooks/my-tutorial.ipynb

links:
  - label: Example notebook
    url: "#"
    kind: Repository
    available: false
---

## Step 1 — Set up

What to do first. Keep each step to one action.

```bash
# code goes in a fenced block like this
pip install xarray
```

## Step 2 — Do the thing

Continue. Say what the reader should see after each step, so they can tell
whether it worked.

**Expected output:** describe or show it.

## Troubleshooting

| Problem | Likely cause | Fix |
| --- | --- | --- |
| Error message | Why | What to do |

## Further reading

- [Related method]({{ site.baseurl }}/methods/quantile-bin-resampling/)
