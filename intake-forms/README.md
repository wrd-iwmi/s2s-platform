# Word intake forms

For researchers who would rather work in Word than edit the site directly.

Fill in a form, send it to the site maintainer, and it becomes a page.

---

## For the researcher

1. Download the form that matches what you are documenting:

   | You are documenting… | Form |
   | --- | --- |
   | A dashboard, platform, digital twin or toolkit | `tool-form.docx` |
   | A scientific or statistical method | `method-form.docx` |
   | An API or data-access service | `api-form.docx` |
   | A training module or how-to | `tutorial-form.docx` |
   | A real-world application of the work | `case-study-form.docx` |
   | A dataset the programme uses | `dataset-form.docx` |

2. Type your answers in the blank line under each blue heading, replacing the
   grey placeholder text.

3. **If you cannot answer something truthfully, delete the placeholder line and
   leave it empty.** The website will show a clear *"information to be added"*
   note. That is the correct outcome — please do not guess. A visible gap tells
   the next person exactly what to supply; a plausible-sounding invention does
   not, and on a scientific platform it is a real risk.

4. Do not rename, reorder or delete the blue headings. They are how the
   converter finds your answers. The grey italic text is guidance — the
   converter ignores it, so you can leave it in place.

5. Save as **.docx** and send it to the site maintainer.

Bold, italics, bullet lists, numbered lists and tables all carry across.

`EXAMPLE-filled-tool-form.docx` shows a completed form, so you can see what a
good answer looks like. (The tool in it is fictional — it exists only to
demonstrate the format.)

### A note on tutorials

If your tutorial is a **Jupyter notebook**, skip the form. Send the `.ipynb`
file instead — it is converted directly, with every code cell, output, table and
plot intact. See `../notebooks/README.md`.

---

## For the maintainer

```bash
python3 _scripts/docx_to_page.py submissions/aware-update.docx
```

The script works out which kind of page it is, converts it, and writes the
markdown into the matching collection folder. No dependencies — a `.docx` is a
zip of XML and the script reads it with the standard library.

Useful options:

```bash
python3 _scripts/docx_to_page.py forms/*.docx              # convert a batch
python3 _scripts/docx_to_page.py form.docx --dry-run       # print, don't write
python3 _scripts/docx_to_page.py form.docx --force         # overwrite an existing page
python3 _scripts/docx_to_page.py form.docx --slug my-name  # set the file name
python3 _scripts/docx_to_page.py form.docx --collection methods   # override detection
```

### What it checks

- Required fields are present. If any are missing it reports them and **does not
  write the file**, rather than producing a broken page.
- `status`, `difficulty` and `role` are one of the allowed values.
- `weight` is a number.
- Link entries have a recognised `kind`; a link with no URL is marked
  *Not yet public* rather than published as a dead link.
- Headings it does not recognise are kept as sections in the page body and
  reported, so nothing a researcher wrote is silently dropped.

**Always read the generated markdown before committing it.** The converter is
faithful, but it cannot tell whether the content is right.

### Adding a field to a form

1. Add the heading to the Word template (Heading 2 style, with a `Guidance`-styled
   line underneath explaining it).
2. Add a matching row to `SCHEMAS` in `_scripts/docx_to_page.py`, mapping the
   heading text to a front-matter key and a kind (`text`, `list`, `block`,
   `links` or `pairs:a,b`).

---

## Is this the best route?

It is the most familiar one, and it works. But it puts a person in the loop for
every submission, and the round trip is slower than editing the site directly.

If a researcher is willing to try it once, editing the markdown file on GitHub is
genuinely easier — no download, no email, no waiting, and they can see the result
in a minute. `../EDITING-GUIDE.md` walks through it without assuming any
technical background. Consider offering the Word route as the fallback rather
than the default.
