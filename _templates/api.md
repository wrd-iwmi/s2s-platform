---
# ---------------------------------------------------------------------------
#  API PAGE
#  Do not publish an endpoint, credential or example that does not exist yet.
#  Leave the field out and the page will say it is unpublished.
# ---------------------------------------------------------------------------

title: Name of the API
summary: One sentence. What can a developer do with this?
purpose: >-
  Two or three sentences. Who is it for, and what problem does it remove for them?

status: In development
version: Unreleased
weight: 50

tags:
  - API
regions:
  - Global
deliverables:
  - D3
team:
  - Your name

# REFERENCE TABLE — omit any line that is not yet true -------------------------
# base_url: https://api.example.org/v1
authentication: Information to be added
response_formats:
  - GeoTIFF
  - Zarr
# update_frequency: Daily at 06:00 UTC
# coverage: South Asia, 2–8 week lead
# rate_limits: 100 requests per hour

# ENDPOINTS — only add these once they are real --------------------------------
# endpoints:
#   - path: /forecast/{variable}
#     method: GET
#     description: Return a downscaled forecast field.
#     parameters:
#       - name: variable
#         type: string
#         required: true
#         description: rainfall | temperature | soil_moisture
#     example_request: |
#       curl https://api.example.org/v1/forecast/rainfall?lead=14
#     example_response: |
#       { "variable": "rainfall", "lead_days": 14 }

related_tool: interoperability-toolkit

links:
  - label: Related tool
    url: /tools/interoperability-toolkit/
    kind: Documentation
---

## What is defined so far

Describe the design intent, and be explicit about what is intent versus what is
released. If nothing is released, say that plainly — it is more useful than an
invented example.
