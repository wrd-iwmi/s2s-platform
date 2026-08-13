# Copy-paste templates

These files are not published. They exist so you can start a new page without
staring at a blank screen.

**To use one:** open the file, copy everything, then create a new file in the
matching folder and paste it in. See `../EDITING-GUIDE.md` for the full walkthrough.

| Template | Copy it into | Becomes |
| --- | --- | --- |
| `tool.md` | `_tools/` | `/tools/your-file-name/` |
| `method.md` | `_methods/` | `/methods/your-file-name/` |
| `api.md` | `_apis/` | `/apis/your-file-name/` |
| `tutorial.md` | `_tutorials/` | `/tutorials/your-file-name/` |
| `case-study.md` | `_case_studies/` | `/case-studies/your-file-name/` |
| `dataset.md` | `_datasets/` | `/datasets/your-file-name/` |

Name the file in lowercase with hyphens: `soil-moisture-monitor.md`.

**Delete any line you cannot fill in honestly.** The page will show a clear
"information to be added" block in its place, which is what we want.

## Lines that are commented out

Every template has some settings behind a `#`. They are off by default because
most pages do not need them. Delete the `#` to switch one on.

| Setting | What it does |
| --- | --- |
| `updated` | Shows "Last updated ..." under the page title. Use `YYYY-MM-DD`. |
| `published: false` | Keeps the file, but the page is not built. Nothing is lost. |
| `coming_soon: true` | Replaces the page body with a "Coming soon" panel. Your text stays in the file. |

## A tutorial that is a notebook

Do not start from `tutorial.md`. Put the `.ipynb` in `../notebooks/` and run the
converter — the page then shows every cell and output, with download and Colab
buttons. See `../notebooks/README.md`.
