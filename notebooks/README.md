# Jupyter notebooks

A notebook can become a tutorial page with everything intact — code, printed
output, tables, error messages and plots.

---

## For the researcher

### 1. Add the page settings to your notebook

Make the **very first cell** a **raw cell** (in Jupyter: *Cell → Cell Type →
Raw*; in JupyterLab the cell-type dropdown in the toolbar). Paste this in and
edit it:

```
---
title: Reading a downscaled S2S forecast in Python
summary: Open a forecast file, check its metadata, and plot the ensemble spread.
difficulty: Beginner
status: Operational
estimated_time: 25 minutes
objective: >-
  Open a downscaled S2S forecast product in Python, check its metadata, and plot
  the ensemble spread for a single point.
prerequisites:
  - Basic Python
requirements:
  - Python 3.9 or later
  - xarray, matplotlib
tags:
  - Capacity building
  - S2S
regions:
  - Global
deliverables:
  - D4
---
```

Only `title`, `summary`, `objective` and `difficulty` really matter. Anything
you leave out becomes a clear placeholder on the page rather than a guess.

### 2. Write the notebook normally

- **Markdown cells** become the prose of the page. Use `##` headings to
  structure it.
- **Code cells** appear with syntax highlighting.
- **Outputs** appear underneath: printed text, tables, plots and even error
  tracebacks, exactly as they ran.

### 3. Run it from top to bottom before sending

The page shows the outputs saved in the notebook file. If you send a notebook
whose cells were run out of order, the page will show that. *Kernel → Restart &
Run All* is the safe habit.

### 4. Keep figures small

Plot images are extracted into the site and served to readers, many of whom are
on modest mobile connections. `dpi=110` and a figure around 7×3.5 inches gives a
sharp plot at roughly 100 KB. The converter warns you if an image goes over
400 KB.

### 5. Send the `.ipynb` file to the site maintainer

Or, if you have repository access, drop it in this folder and run the converter
yourself (below).

---

## For the maintainer

```bash
python3 _scripts/notebook_to_page.py notebooks/my-notebook.ipynb
```

That writes `_tutorials/my-notebook.md` and saves any plots into
`assets/img/notebooks/my-notebook/`. No dependencies — a notebook is JSON and
the script reads it with the standard library.

Options:

```bash
--collection methods      write into _methods/ instead of _tutorials/
--slug custom-name        set the output file name
--max-image-kb 250        tighten the image size warning
```

Commit three things: the generated `.md`, the extracted images, and the
`.ipynb` itself. The notebook is published too, so the page can offer it for
download.

### Enabling the Colab and nbviewer buttons

Set your repository in `_config.yml`:

```yaml
colab_repo: "wrd-iwmi/s2s-platform"
colab_branch: "main"
```

The tutorial page then shows **Run in Colab** and **View on nbviewer** buttons
alongside **Download .ipynb**. Leave `colab_repo` empty and only the download
button appears.

### Re-converting after a change

Run the same command again. Images from the previous run are cleared first, so
deleted plots do not linger. The generated `.md` is overwritten — so treat it as
a build product and make edits in the notebook, not in the markdown.

---

## What the reader sees

A short toolbar at the top of the tutorial (download / Colab / nbviewer), a note
explaining that the page is the notebook rendered in full, then the notebook
itself: markdown, code, and outputs in order.

Output longer than about 20 lines collapses behind a **Show all output** button,
so a chatty cell never buries the rest of the page. Images are lazy-loaded.

`reading-a-downscaled-forecast.ipynb` in this folder is a worked example — it
exercises printed output, an HTML table, a matplotlib figure and an error
traceback. It uses synthetic numbers so it runs anywhere; it is a format
demonstration, not a scientific result.
