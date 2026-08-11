# How to edit this website

**You do not need to install anything, and you do not need to know how to code.**
Everything on this site is a text file you edit in your web browser on GitHub.
When you save, the site rebuilds itself in about a minute.

This guide is for researchers. If you are a developer setting the site up for the
first time, read `README.md` instead.

---

## Contents

1. [The 60-second version](#the-60-second-version)
2. [Editing a page that already exists](#editing-a-page-that-already-exists)
3. [Adding a brand new page](#adding-a-brand-new-page)
4. [Understanding the top part of a page](#understanding-the-top-part-of-a-page)
5. [Writing the main text](#writing-the-main-text)
6. [The one rule that matters most](#the-one-rule-that-matters-most)
7. [Adding a Jupyter notebook as a tutorial](#adding-a-jupyter-notebook-as-a-tutorial)
8. [Adding a country to the map](#adding-a-country-to-the-map)
9. [If you would rather use Word](#if-you-would-rather-use-word)
10. [Changing the homepage, the menu and the programme page](#changing-the-homepage-the-menu-and-the-programme-page)
11. [Field reference](#field-reference)
12. [If something breaks](#if-something-breaks)

---

## The 60-second version

- Every page on the site is one file ending in `.md`.
- Files live in folders named after what they hold: `_tools`, `_methods`, `_apis`,
  `_tutorials`, `_case_studies`, `_datasets`.
- Each file has two parts: a **settings block** at the top between two `---` lines,
  and **your writing** underneath it.
- To change a page, edit the file. To add a page, copy a file from `_templates`
  into the right folder and fill it in.
- Save (GitHub calls this "Commit changes"). Wait a minute. Refresh the site.

---

## Editing a page that already exists

1. Open the site and find the page you want to change.
2. Look at the address bar. A page at `…/methods/quantile-bin-resampling/` lives
   in the file `_methods/quantile-bin-resampling.md`.
3. In GitHub, open that folder, click the file, then click the **pencil icon**
   (top right) to edit it.
4. Make your change.
5. Scroll to the bottom, write a short note about what you changed
   (for example *"Added validation results for Cauvery"*), and click
   **Commit changes**.
6. Wait about a minute, then refresh the page on the site.

> **Tip:** GitHub has a **Preview** tab next to **Edit**. It shows roughly how
> your text will look. It will not show the settings block correctly — that is
> normal.

---

## Adding a brand new page

1. Open the `_templates` folder. Pick the template that matches what you are
   adding — for example `tool.md` for a new tool.
2. Click the file, then click the **copy raw contents** button, or select all
   the text and copy it.
3. Go to the folder where the page belongs (`_tools` for a tool).
4. Click **Add file → Create new file**.
5. Type the file name. **This becomes the web address**, so use lowercase
   letters and hyphens, no spaces:

   | You type | Page appears at |
   | --- | --- |
   | `drought-monitor.md` | `…/tools/drought-monitor/` |
   | `Drought Monitor.md` | ✗ don't — spaces and capitals break the address |

6. Paste the template in, fill it out, and click **Commit changes**.

That is it. The page appears automatically in the tools list, in the site search,
in the filters and in the sitemap. Nobody has to add it anywhere else.

### Which folder?

| I am documenting… | Folder | Template |
| --- | --- | --- |
| A dashboard, platform, digital twin or toolkit | `_tools` | `_templates/tool.md` |
| A scientific or statistical method | `_methods` | `_templates/method.md` |
| An API or data-access service | `_apis` | `_templates/api.md` |
| A training module or how-to | `_tutorials` | `_templates/tutorial.md` |
| A real-world application of the work | `_case_studies` | `_templates/case-study.md` |
| A dataset the programme uses | `_datasets` | `_templates/dataset.md` |

---

## Understanding the top part of a page

The block between the two `---` lines is the **settings block**. It tells the site
what to put in the sidebar, the badges, the filters and the search index.

```yaml
---
title: My New Tool
summary: One sentence explaining what this is and who it is for.
status: In development
tags:
  - Drought
  - Early warning
regions:
  - Ghana
---
```

Five rules, and you will never have a broken page:

1. **Keep the two `---` lines.** They mark where the settings end and your
   writing begins.
2. **A setting is `name: value`.** One space after the colon.
3. **A list is one item per line, each starting with `- `**, indented two spaces.
4. **If your text contains a colon followed by a space, wrap it in quotes.**
   `summary: "Rainfall: a new approach"` — without the quotes this breaks.
5. **Don't rename the settings.** `summary` works; `Summary` and `sumary` do not.

Every field is optional except `title` and `summary`. Leave out anything you do
not have — the page will show a clear placeholder instead, which is exactly what
we want (see the next section but one).

---

## Writing the main text

Below the second `---`, write normally. This is Markdown:

```md
## A heading

A normal paragraph. Put a blank line between paragraphs.

**Bold text** and *italic text*.

- A bullet
- Another bullet

1. A numbered item
2. Another

| Column | Column |
| --- | --- |
| Cell | Cell |

> A quoted note.
```

### Links

**To another website:**

```md
[CHIRPS documentation](https://www.chc.ucsb.edu/data/chirps)
```

**To another page on this site** — copy this pattern exactly, including the
curly brackets:

```md
[Quantile Bin Resampling]({{ site.baseurl }}/methods/quantile-bin-resampling/)
```

The `{{ site.baseurl }}` part is what makes the link keep working no matter where
the site is published. Leave it in.

### Images

Put the image file in `assets/img/`, then:

```md
![A short description of what the image shows]({{ site.baseurl }}/assets/img/my-figure.png)
```

Always write the description — a screen reader reads it aloud, and it shows if
the image fails to load on a slow connection. Keep image files under about
300&nbsp;KB so the page still loads on a modest mobile network.

---

## The one rule that matters most

**Never invent a fact to fill a gap.**

If you do not know the resolution of a dataset, the endpoint of an API, the
validation result of a method or the licence of a product — **leave the field
out entirely**. The site will show a clearly marked amber block saying the
information has not been documented yet.

That is the correct outcome. A visible gap is honest and tells the next person
exactly what to supply. A plausible-sounding guess on a scientific platform is a
real reputational risk, and it is very hard to detect later.

You can also put a placeholder in the middle of your writing:

```md
{% raw %}{% include placeholder.html what="Validation results to be added" %}{% endraw %}
```

or with an explanation:

```md
{% raw %}{% include placeholder.html
   what="Endpoint not published"
   note="Waiting on the data team to confirm the public URL." %}{% endraw %}
```

### Other useful blocks

A coloured note box:

```md
{% raw %}{% include callout.html variant="caution" title="Before you start"
   body="This product has not been validated outside the Cauvery basin." %}{% endraw %}
```

`variant` can be `note`, `caution`, `limitation` or `method`.

---

## Adding a Jupyter notebook as a tutorial

You do not need to rewrite a notebook as a web page. Send the `.ipynb` file and
it becomes a tutorial with everything intact — code, printed output, tables,
plots, even error messages.

**Three things to do first:**

1. **Add the page settings.** Make the very first cell a **raw cell**
   (*Cell → Cell Type → Raw*) containing:

   ```
   ---
   title: Reading a downscaled S2S forecast in Python
   summary: Open a forecast file, check its metadata, and plot the ensemble spread.
   difficulty: Beginner
   status: Operational
   objective: >-
     What the reader will be able to do by the end.
   ---
   ```

2. **Restart and run all.** The page shows the outputs stored in the file. If
   the cells were run out of order, the page will show that.

3. **Keep figures small.** `dpi=110` and a figure about 7×3.5 inches gives a
   sharp plot at roughly 100 KB. Many readers are on modest mobile connections.

Then send the file to the maintainer, or drop it in the `notebooks/` folder if
you have repository access. Full detail in `notebooks/README.md`.

The published page gets **Download .ipynb**, **Run in Colab** and **View on
nbviewer** buttons automatically, so readers can run your work themselves.

---

## Adding a country to the map

Open `_data/geography.yml` and copy an existing block:

```yaml
  - name: Kenya
    lat: -0.02
    lon: 37.91
    note: "What the programme does there"
    url: /case-studies/some-case-study/     # optional
```

To find the numbers: go to <https://www.openstreetmap.org>, search for the
place, and read the latitude and longitude from the address bar — or right-click
the spot and choose *Show address*.

Latitude is positive north of the equator, longitude positive east of Greenwich.
Nothing else needs changing; the marker, its tooltip and the list beside the map
all update.

### Changing the map size

Also in `_data/geography.yml`, under `settings`:

```yaml
  height: 340          # pixels on a laptop
  height_mobile: 260   # pixels on a phone
```

### Drawing basins, districts or station networks

Put a GeoJSON file in `assets/geo/`, then add a block under `layers:` in the
same file:

```yaml
layers:
  - name: "Cauvery basin"
    file: assets/geo/cauvery-basin.geojson
    colour: "#0f6f7d"
    fill_opacity: 0.15
    label_field: name
```

Points, lines and polygons all work, and a layer switcher appears on the map
automatically. `assets/geo/README.md` covers the options, how to convert from a
shapefile, and how to shrink a large boundary file.

---

## If you would rather use Word

There are Word forms in the `intake-forms/` folder — one for each kind of page.
Fill one in, send it to the site maintainer, and it becomes a page.

The rules are the same as everywhere else on this site:

- Type your answer in the blank line under each blue heading.
- **If you cannot answer something truthfully, delete the line and leave it
  empty.** The site shows a clear "information to be added" note. Do not guess.
- Do not rename or reorder the blue headings — they are how the converter finds
  your answers.
- The grey italic text is guidance. Leave it; it is ignored.

Bold, italics, bullet lists, numbered lists and tables all carry across.
`intake-forms/EXAMPLE-filled-tool-form.docx` shows a completed one.

Worth knowing: this route needs a person to run the conversion, so it is slower
than editing the page yourself. If you try the GitHub route once
([above](#editing-a-page-that-already-exists)) you will probably not go back —
you can see your change on the site a minute after saving it.

---

## Changing the homepage, the menu and the programme page

These live in the `_data` folder. They are plain settings files — no HTML.

| To change… | Edit |
| --- | --- |
| The menu at the top, and the footer links | `_data/navigation.yml` |
| Every word on the homepage | `_data/homepage.yml` |
| The value-chain diagram boxes | `_data/ecosystem.yml` |
| The countries on the homepage map | `_data/geography.yml` |
| Whether the map is interactive or a simple drawing | `_data/geography.yml`, `settings.interactive` |
| The programme page — pillars, stages, deliverables, partners | `_data/programme.yml` |
| The six-layer model | `_data/six_layer_model.yml` |
| Site name, contact email, web address | `_config.yml` |

For example, to remove "Applications" from the menu, open
`_data/navigation.yml` and delete these two lines:

```yaml
  - title: Applications
    url: /case-studies/
```

To reorder the menu, move the blocks up or down. That is the whole operation.

> **One catch:** changes to `_config.yml` need a full rebuild. On GitHub that
> happens automatically. If you are previewing on your own computer, stop the
> server and start it again.

---

## Field reference

### Every page can use these

| Field | What it does |
| --- | --- |
| `title` | **Required.** The page heading. |
| `summary` | **Required.** One sentence. Appears on cards, in search results and in Google. |
| `status` | `Operational`, `In development`, `Pilot`, `Planned`, `Documentation pending` |
| `tags` | Topics. These become the filter buttons — reuse existing ones where you can. |
| `regions` | Countries or regions. Also filterable. |
| `deliverables` | e.g. `D2`, `D3` |
| `team` | Names shown in the sidebar. |
| `weight` | Sort order on list pages. Higher appears first. Default `0`. |
| `updated` | `2026-08-11`. Shows a "last updated" date. |
| `links` | Access links — see below. |

### Links block

```yaml
links:
  - label: Toolkit repository
    url: https://github.com/example/repo
    kind: Repository
  - label: API documentation
    url: /apis/
    kind: Documentation
  - label: Web application
    url: "#"
    kind: Web application
    available: false          # shows a "Not yet public" tag instead of a link
    note: URL to be confirmed.
```

`kind` must be one of: `Web application`, `API`, `Dataset`, `Repository`,
`Documentation`, `Download`, `Demonstration`, `Publication`.

### Tool pages

| Field | What it does |
| --- | --- |
| `problem` | The problem the tool addresses. Shown at the top. |
| `flagship` | `true` puts it on the homepage. |
| `capabilities` | List of `title` + `description`. Becomes the capability cards. |
| `workflow` | List of `stage` + `detail`. Becomes the "How it works" diagram. |
| `outputs` | List of what a user gets. |
| `citation` | How to cite the tool. |
| `related_methods`, `related_apis`, `related_tutorials`, `related_case_studies` | Lists of file names (without `.md`) to cross-link. |

### Method pages

| Field | What it does |
| --- | --- |
| `executive_summary` | **Required.** Level 1 — the plain-language explanation. |
| `objective` | What the method is for. |
| `inputs`, `outputs` | Lists shown in the technical tab. |
| `spatial_scale`, `temporal_scale` | Sidebar metadata. |
| `validation`, `uncertainty`, `compute_notes`, `reproducibility` | Level 3 — implementation detail. Omit any you do not have. |
| `strengths`, `limitations` | Lists. Please fill in `limitations` — it is the most valuable part of a method page. |
| `references` | List of `citation` + optional `url`. |
| `related_tools` | File names of tools that use the method. |

### API pages

| Field | What it does |
| --- | --- |
| `purpose` | **Required.** One or two sentences. |
| `version`, `base_url`, `authentication`, `response_formats`, `update_frequency`, `coverage`, `rate_limits` | Reference table. Omit anything unpublished. |
| `endpoints` | List of `path`, `method`, `description`, `parameters`, `example_request`, `example_response`. |
| `related_tool` | File name of the tool this API belongs to. |

### Tutorial pages

| Field | What it does |
| --- | --- |
| `difficulty` | **Required.** `Beginner`, `Intermediate` or `Advanced`. |
| `objective` | **Required.** What the reader will be able to do afterwards. |
| `prerequisites`, `requirements` | Lists. |
| `estimated_time` | e.g. `45 minutes`. |
| `related_tool`, `related_method` | File names. |

### Case study pages

| Field | What it does |
| --- | --- |
| `location` | **Required.** Country, basin or district. |
| `context` | **Required.** The problem that existed. |
| `climate_information` | List of datasets and products used. |
| `workflow` | List of `stage` + `detail`. |
| `decision`, `results` | Prose. |
| `end_users`, `partners`, `lessons` | Lists. |
| `related_tools`, `related_methods` | File names. |

### Dataset pages

| Field | What it does |
| --- | --- |
| `source` | **Required.** Who produces it. |
| `role` | **Required.** `Forecast`, `Observation`, `Reanalysis`, `Projection`, `Ancillary` or `Product`. |
| `variables` | List. |
| `spatial_resolution`, `temporal_resolution`, `temporal_coverage`, `update_frequency`, `licence` | Only fill these in if you are confident. Otherwise leave them out. |

---

## If something breaks

**The site did not update.**
Give it two minutes. Then in the GitHub repository click the **Actions** tab —
a green tick means it published, a red cross means the build failed. Click the
red cross to see the error.

**The build failed.**
Almost always the settings block. Check:

- Are both `---` lines still there?
- Is there a space after every colon?
- Does any value contain a colon-and-space without quotes around it?
- Are list items indented by exactly two spaces and starting with `- `?

**My page is not showing in the list.**
Check the file is in the right folder, ends in `.md`, and does not have
`draft: true` in its settings.

**A link goes to a "page not found".**
For links inside this site, check you used the `{{ site.baseurl }}` pattern and
that the address ends with a slash.

**Something looks wrong and you cannot see why.**
Every change is recorded, and any change can be undone. Nothing you do here can
permanently break the site. Open an issue in the repository, or contact the
platform maintainer — describe what you were editing and paste the error.
