---
title: Reading a downscaled S2S forecast in Python
summary: Open a downscaled forecast file, inspect its metadata, and plot the ensemble spread for one location.
difficulty: Beginner
status: Operational
weight: 98
estimated_time: 25 minutes
objective: >-
  Open a downscaled S2S forecast product in Python, check that its metadata says
  what you expect, and plot the ensemble spread for a single point.
prerequisites:
  - Basic Python
  - Comfortable running a Jupyter notebook
requirements:
  - Python 3.9 or later
  - xarray, matplotlib, numpy
tags:
  - Capacity building
  - S2S
  - Downscaling
regions:
  - Global
deliverables:
  - D4
related_method: quantile-bin-resampling

# Added by _scripts/notebook_to_page.py — do not edit by hand.
notebook: /notebooks/reading-a-downscaled-forecast.ipynb
generated_from_notebook: true
---

## What this notebook does

A downscaled S2S product is an ensemble: many plausible futures rather than one
prediction. Before using one, it is worth looking at how wide that spread is,
because the spread is what tells you how much confidence the forecast supports.

This notebook loads a forecast file, checks its metadata, and plots the ensemble
for a single grid point.

> The example below uses synthetic numbers so the notebook runs anywhere. Replace
> the generated array with a real file once you have access to one.

## Step 1 — Set up

Install what you need, if you do not have it already.

<p class="nb-cell__label">In [1]:</p>

```python
import numpy as np
import matplotlib.pyplot as plt

print("numpy", np.__version__)
```
{: .nb-input}

<div class="nb-cell__output" markdown="0">
<pre class="nb-stream">numpy 2.2.6
</pre>
</div>

## Step 2 — Check the metadata before you trust the numbers

Every product on this platform carries provenance. Read it first: the lead time,
the reference period and the downscaling method all change how the numbers should
be interpreted.

<p class="nb-cell__label">In [2]:</p>

```python
metadata = {
    "variable": "precipitation",
    "units": "mm/week",
    "lead_weeks": "1-8",
    "members": 20,
    "downscaling": "Quantile Bin Resampling (QBR)",
    "bias_correction_baseline": "CHIRPS",
}

for key, value in metadata.items():
    print(f"{key:>26}: {value}")
```
{: .nb-input}

<div class="nb-cell__output" markdown="0">
<pre class="nb-stream">                 variable: precipitation
                    units: mm/week
               lead_weeks: 1-8
                  members: 20
              downscaling: Quantile Bin Resampling (QBR)
 bias_correction_baseline: CHIRPS
</pre>
</div>

## Step 3 — Summarise the ensemble

A table of percentiles is usually more useful to a decision-maker than the raw
members.

<p class="nb-cell__label">In [3]:</p>

```python
rng = np.random.default_rng(7)
weeks = np.arange(1, 9)
members = rng.normal(loc=np.linspace(40, 25, 8), scale=8, size=(20, 8)).clip(0)

summary = {
    "week": weeks,
    "p25": np.percentile(members, 25, axis=0).round(1),
    "median": np.percentile(members, 50, axis=0).round(1),
    "p75": np.percentile(members, 75, axis=0).round(1),
}
summary
```
{: .nb-input}

<div class="nb-cell__output" markdown="0">
<table>
<thead><tr><th>Week</th><th>25th percentile</th><th>Median</th><th>75th percentile</th></tr></thead>
<tbody>
<tr><td>1</td><td>35.4</td><td>40.5</td><td>45.8</td></tr>
<tr><td>2</td><td>33.6</td><td>38.1</td><td>43.9</td></tr>
<tr><td>3</td><td>30.8</td><td>36.0</td><td>41.7</td></tr>
<tr><td>4</td><td>28.9</td><td>34.2</td><td>39.4</td></tr>
<tr><td>5</td><td>26.7</td><td>31.9</td><td>37.6</td></tr>
<tr><td>6</td><td>24.8</td><td>29.7</td><td>35.2</td></tr>
<tr><td>7</td><td>22.6</td><td>27.8</td><td>33.1</td></tr>
<tr><td>8</td><td>20.9</td><td>25.6</td><td>31.0</td></tr>
</tbody></table>
</div>

## Step 4 — Plot the spread

Plot every member faintly, with the ensemble mean and interquartile range on top.
The width of the band is the honest part of the picture.

<p class="nb-cell__label">In [4]:</p>

```python
fig, ax = plt.subplots(figsize=(7, 3.4), dpi=110)

for m in members:
    ax.plot(weeks, m, color="#2a63a8", alpha=0.16, linewidth=1)

ax.plot(weeks, members.mean(axis=0), color="#0a2340", linewidth=2.2, label="Ensemble mean")
ax.fill_between(weeks,
                np.percentile(members, 25, axis=0),
                np.percentile(members, 75, axis=0),
                color="#2a63a8", alpha=0.18, label="Interquartile range")

ax.set_xlabel("Forecast lead (weeks)")
ax.set_ylabel("Weekly rainfall (mm)")
ax.set_title("Downscaled S2S rainfall forecast — 20-member ensemble", fontsize=11)
ax.legend(frameon=False, fontsize=9)
ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
```
{: .nb-input}

<div class="nb-cell__output" markdown="0">
<img src="{{ site.baseurl }}/assets/img/notebooks/reading-a-downscaled-forecast/output-1.png" alt="Figure from the section &#x27;Step 4 — Plot the spread&#x27;" loading="lazy" decoding="async">
</div>

## Step 5 — What to do when it goes wrong

A common mistake is asking for a lead time the product does not cover. The error
looks like this:

<p class="nb-cell__label">In [5]:</p>

```python
members[:, 12]
```
{: .nb-input}

<div class="nb-cell__output" markdown="0">
<pre class="nb-error">---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[5], line 1
----&gt; 1 members[:, 12]
IndexError: index 12 is out of bounds for axis 1 with size 8</pre>
</div>

The product covers leads 1 to 8 weeks, so index 12 does not exist. Always read
`lead_weeks` from the metadata rather than assuming.

## Further reading

- [Quantile Bin Resampling]({{ site.baseurl }}/methods/quantile-bin-resampling/)
- [Forecast verification and skill benchmarking]({{ site.baseurl }}/methods/forecast-verification/)
