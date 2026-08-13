#!/usr/bin/env python3
"""
Convert a Jupyter notebook into a fully rendered tutorial page for this site.

Everything in the notebook comes across: markdown cells, code cells with syntax
highlighting, printed output, tables, error tracebacks, and plot images.

    python3 _scripts/notebook_to_page.py notebooks/qbr-walkthrough.ipynb

That reads the notebook, writes `_tutorials/qbr-walkthrough.md`, and saves any
plot images into `assets/img/notebooks/qbr-walkthrough/`.

Requires nothing but Python 3.8+ — no nbconvert, no pip install. A notebook is
just a JSON file, and this script reads it directly.

--------------------------------------------------------------------------------
SETTING THE PAGE DETAILS (title, summary, difficulty and so on)
--------------------------------------------------------------------------------
Add a **raw cell** as the very first cell of the notebook, containing the page
settings between two lines of three dashes. In Jupyter: Cell → Cell Type → Raw.

    ---
    title: Accessing forecast data via the API
    summary: Pull a downscaled forecast into a notebook and plot it.
    difficulty: Beginner
    status: Operational
    estimated_time: 30 minutes
    tags:
      - API
      - Capacity building
    ---

If that cell is missing the script builds a minimal page and tells you which
fields to fill in by hand.

--------------------------------------------------------------------------------
OPTIONS
--------------------------------------------------------------------------------
    --collection tutorials     which folder to write into (default: tutorials)
    --slug my-page-name        override the output file name
    --site-root .              repository root, if running from elsewhere
    --max-image-kb 400         warn above this size, so pages stay usable on a
                               modest mobile connection
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import os
import re
import sys
from pathlib import Path

# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------

ANSI = re.compile(r'\x1b\[[0-9;]*[A-Za-z]')

# Output longer than this many lines is collapsed behind a "Show all" button.
COLLAPSE_LINES = 22


def strip_ansi(text: str) -> str:
    """Remove terminal colour codes, which appear in tracebacks."""
    return ANSI.sub('', text)


def join(source) -> str:
    """Notebook fields are either a string or a list of lines."""
    if isinstance(source, list):
        return ''.join(source)
    return source or ''


def slugify(value: str) -> str:
    value = re.sub(r'[^a-zA-Z0-9]+', '-', value).strip('-').lower()
    return re.sub(r'-{2,}', '-', value)


def yaml_quote(value: str) -> str:
    """Quote a scalar if YAML would otherwise misread it."""
    if value == '':
        return '""'
    if re.search(r'[:#]\s|^\s|\s$|^[\[\]{}&*!|>%@`"\']|: ', value) or value.strip() != value:
        return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return value


def warn(message: str) -> None:
    print(f"  ! {message}", file=sys.stderr)


# --------------------------------------------------------------------------
# Front matter
# --------------------------------------------------------------------------

DEFAULT_FRONT_MATTER = {
    'title': 'Untitled notebook',
    'summary': 'TO BE COMPLETED — one sentence describing what the reader will learn.',
    'difficulty': 'Intermediate',
    'status': 'Operational',
}


def extract_front_matter(cells):
    """Read page settings from a leading raw cell, if there is one."""
    for cell in cells:
        if cell.get('cell_type') != 'raw':
            continue
        text = join(cell.get('source')).strip()
        if text.startswith('---'):
            body = text.split('---', 2)
            if len(body) >= 3:
                return body[1].strip(), True
        break
    return None, False


# --------------------------------------------------------------------------
# Output rendering
# --------------------------------------------------------------------------

def render_image(mime, payload, image_dir, image_url_base, index, max_kb, alt):
    """Write an embedded image to disk and return an <img> tag."""
    ext = {'image/png': 'png', 'image/jpeg': 'jpg', 'image/gif': 'gif'}[mime]
    data = base64.b64decode(''.join(payload) if isinstance(payload, list) else payload)
    size_kb = len(data) / 1024
    if size_kb > max_kb:
        warn(f"output image {index} is {size_kb:.0f} KB — consider "
             f"reducing the figure size or dpi so the page stays usable on a slow connection")
    image_dir.mkdir(parents=True, exist_ok=True)
    name = f"output-{index}.{ext}"
    (image_dir / name).write_bytes(data)
    return (f'<img src="{{{{ site.baseurl }}}}{image_url_base}/{name}" '
            f'alt="{html.escape(alt)}" loading="lazy" decoding="async">')


def render_svg(payload):
    svg = join(payload).strip()
    # Strip an XML declaration, which is invalid inside HTML.
    svg = re.sub(r'^<\?xml[^>]*\?>\s*', '', svg)
    return svg


# Placeholder reprs a library leaves in text/plain when the real output is in
# another mime type. On their own they say nothing and must never reach a page.
PLACEHOLDER_REPR = re.compile(
    r'^<(?:IPython\.core\.display\.\w+ object|Figure size [^>]*|'
    r'matplotlib\.[\w.]+ (?:object )?at 0x[0-9a-f]+)>$', re.I)

# Jupyter widgets need a live kernel. A static page cannot run one, so a
# widget output is dropped rather than rendered as its useless text repr.
WIDGET_MIME = 'application/vnd.jupyter.widget-view+json'


def clean_html(fragment: str) -> str:
    """
    Make one HTML output safe to drop into a page.

    Beyond scripts and event handlers this removes `<style>` blocks. Libraries
    ship their own CSS with every cell — geemap emits a theme block on each one —
    and letting that into the page means a notebook can restyle the site.
    """
    fragment = re.sub(r'<script\b.*?</script>', '', fragment, flags=re.S | re.I)
    fragment = re.sub(r'<style\b.*?</style>', '', fragment, flags=re.S | re.I)
    fragment = re.sub(r'\son\w+\s*=\s*"[^"]*"', '', fragment, flags=re.I)
    fragment = re.sub(r"\son\w+\s*=\s*'[^']*'", '', fragment, flags=re.I)

    # Colab wraps a DataFrame in its own container of buttons and generated ids,
    # all of which depend on the scripts just removed — and duplicate ids fail
    # the site's accessibility check. Keep the table, drop the furniture.
    if 'class="dataframe"' in fragment:
        table = re.search(r'<table\b[^>]*class="dataframe".*?</table>', fragment, flags=re.S)
        if table:
            fragment = table.group(0)

    # Every image on this site needs alt text.
    def add_alt(match):
        tag = match.group(0)
        return tag if 'alt=' in tag else tag[:4] + ' alt="Notebook output"' + tag[4:]

    fragment = re.sub(r'<img\b[^>]*>', add_alt, fragment, flags=re.I)
    return fragment.strip()


def render_outputs(cell, ctx):
    """Turn one code cell's outputs into an HTML block."""
    parts = []
    line_count = 0

    for output in cell.get('outputs', []):
        kind = output.get('output_type')

        if kind == 'stream':
            text = strip_ansi(join(output.get('text')))
            line_count += text.count('\n') + 1
            cls = 'nb-stream--stderr' if output.get('name') == 'stderr' else 'nb-stream'
            parts.append(f'<pre class="{cls}">{html.escape(text)}</pre>')

        elif kind == 'error':
            text = strip_ansi('\n'.join(output.get('traceback', [])))
            line_count += text.count('\n') + 1
            parts.append(f'<pre class="nb-error">{html.escape(text)}</pre>')

        elif kind in ('execute_result', 'display_data'):
            data = output.get('data', {})

            # An interactive widget cannot work on a static page. Skip it, and
            # do not fall through to its text repr — "Map(center=[23.5, 90.3],
            # controls=(WidgetControl(..." helps nobody.
            if WIDGET_MIME in data:
                continue

            # Richest representation first.
            if 'image/png' in data or 'image/jpeg' in data or 'image/gif' in data:
                mime = next(m for m in ('image/png', 'image/jpeg', 'image/gif') if m in data)
                ctx['image_index'] += 1
                alt = ctx['alt_hint'] or f"Output of cell {ctx['exec_label']}"
                parts.append(render_image(mime, data[mime], ctx['image_dir'],
                                          ctx['image_url_base'], ctx['image_index'],
                                          ctx['max_kb'], alt))
                line_count += 12  # an image is roughly this tall in the flow
            elif 'image/svg+xml' in data:
                parts.append(render_svg(data['image/svg+xml']))
                line_count += 12
            elif 'text/html' in data:
                fragment = clean_html(join(data['text/html']))
                if not fragment:
                    continue      # was nothing but a <style> block
                line_count += fragment.count('\n') + 1
                parts.append(fragment)
            elif 'text/latex' in data:
                parts.append(f'<pre>{html.escape(join(data["text/latex"]))}</pre>')
            elif 'text/plain' in data:
                text = strip_ansi(join(data['text/plain'])).strip()
                if PLACEHOLDER_REPR.match(text):
                    continue      # the real output was in a mime type we skipped
                line_count += text.count('\n') + 1
                parts.append(f'<pre>{html.escape(text)}</pre>')

    if not parts:
        return ''

    collapse = line_count > COLLAPSE_LINES
    classes = 'nb-cell__output'
    if collapse:
        classes += ' nb-cell__output--long'

    block = (f'<div class="{classes}" markdown="0">\n'
             + '\n'.join(parts)
             + '\n</div>')
    if collapse:
        block += ('\n<button class="nb-cell__expand" type="button" '
                  'data-nb-expand aria-expanded="false">Show all output</button>')
    return block


# --------------------------------------------------------------------------
# Main conversion
# --------------------------------------------------------------------------

def convert(nb_path: Path, site_root: Path, collection: str, slug: str, max_kb: int) -> Path:
    notebook = json.loads(nb_path.read_text(encoding='utf-8'))
    cells = notebook.get('cells', [])

    language = (notebook.get('metadata', {})
                .get('language_info', {})
                .get('name', 'python'))

    front_matter, had_front_matter = extract_front_matter(cells)
    if not had_front_matter:
        warn("no settings cell found — writing a page with placeholder title and summary.")
        warn("Add a raw cell at the top of the notebook (see the top of this script).")

    # The notebook itself is published for download, so its size matters.
    widget_state = notebook.get('metadata', {}).get('widgets')
    if widget_state:
        size_kb = len(json.dumps(widget_state)) / 1024
        warn(f"metadata.widgets is {size_kb:.0f} KB of saved widget state. A static page "
             f"cannot replay a widget, and for geemap this blob holds signed map URLs "
             f"carrying your Cloud project ID. Delete metadata.widgets before committing.")
    nb_kb = nb_path.stat().st_size / 1024
    if nb_kb > 500:
        warn(f"the notebook is {nb_kb:.0f} KB — readers download this file. "
             f"Consider clearing widget state or reducing figure dpi.")

    image_dir = site_root / 'assets' / 'img' / 'notebooks' / slug
    image_url_base = f'/assets/img/notebooks/{slug}'

    # Remove any images from a previous run so deleted plots do not linger.
    if image_dir.exists():
        for old in image_dir.glob('output-*'):
            old.unlink()

    ctx = {
        'image_dir': image_dir,
        'image_url_base': image_url_base,
        'image_index': 0,
        'max_kb': max_kb,
        'alt_hint': '',
        'exec_label': '',
    }

    body = []
    skipped_raw = False

    for cell in cells:
        cell_type = cell.get('cell_type')

        if cell_type == 'raw':
            # The first raw cell is the settings block; later ones pass through.
            if not skipped_raw and had_front_matter:
                skipped_raw = True
                continue
            text = join(cell.get('source')).strip()
            if text:
                body.append(text)
            continue

        if cell_type == 'markdown':
            text = join(cell.get('source')).rstrip()
            if text:
                body.append(text)
                # Use the nearest preceding heading as alt-text context for plots.
                heading = re.findall(r'^#{1,6}\s+(.+)$', text, re.M)
                if heading:
                    ctx['alt_hint'] = f"Figure from the section '{heading[-1].strip()}'"
            continue

        if cell_type == 'code':
            source = join(cell.get('source')).rstrip()
            if cell.get('metadata', {}).get('hide_input'):
                source = ''
            exec_count = cell.get('execution_count')
            ctx['exec_label'] = str(exec_count) if exec_count else ' '

            if source:
                label = f'In [{exec_count}]:' if exec_count else 'In [ ]:'
                body.append(f'<p class="nb-cell__label">{label}</p>')
                body.append(f'```{language}\n{source}\n```\n{{: .nb-input}}')

            rendered = render_outputs(cell, ctx)
            if rendered:
                body.append(rendered)

    # ---- assemble the page -------------------------------------------------
    if had_front_matter:
        fm = front_matter
    else:
        fm = '\n'.join(f'{k}: {yaml_quote(v)}' for k, v in DEFAULT_FRONT_MATTER.items())

    # Record the notebook so the page can offer download / Colab / nbviewer links.
    nb_rel = os.path.relpath(nb_path, site_root).replace(os.sep, '/')
    if 'notebook:' not in fm:
        fm += f'\n\n# Added by _scripts/notebook_to_page.py — do not edit by hand.\nnotebook: /{nb_rel}'
    if 'generated_from_notebook' not in fm:
        fm += '\ngenerated_from_notebook: true'

    page = f"---\n{fm}\n---\n\n" + '\n\n'.join(body) + '\n'

    out_dir = site_root / f'_{collection}'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f'{slug}.md'
    out_path.write_text(page, encoding='utf-8')
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description='Convert a Jupyter notebook into a rendered page for this site.')
    parser.add_argument('notebook', help='path to the .ipynb file')
    parser.add_argument('--collection', default='tutorials',
                        help='tutorials (default), methods, tools, case_studies')
    parser.add_argument('--slug', default=None, help='output file name without .md')
    parser.add_argument('--site-root', default=None, help='repository root')
    parser.add_argument('--max-image-kb', type=int, default=400,
                        help='warn about output images larger than this')
    args = parser.parse_args()

    nb_path = Path(args.notebook).resolve()
    if not nb_path.exists():
        print(f"Cannot find {nb_path}", file=sys.stderr)
        return 1

    site_root = Path(args.site_root).resolve() if args.site_root \
        else Path(__file__).resolve().parent.parent
    if not (site_root / '_config.yml').exists():
        print(f"{site_root} does not look like the site root "
              f"(no _config.yml). Pass --site-root.", file=sys.stderr)
        return 1

    slug = args.slug or slugify(nb_path.stem)

    print(f"Converting {nb_path.name}")
    out = convert(nb_path, site_root, args.collection, slug, args.max_image_kb)
    rel = os.path.relpath(out, site_root)
    print(f"  wrote {rel}")

    images = site_root / 'assets' / 'img' / 'notebooks' / slug
    if images.exists():
        files = sorted(images.glob('output-*'))
        if files:
            total = sum(f.stat().st_size for f in files) / 1024
            print(f"  wrote {len(files)} image(s) to "
                  f"assets/img/notebooks/{slug}/ ({total:.0f} KB total)")

    print(f"\nNow commit {rel}, the images, and the notebook itself.")
    print("The page will appear on the site after GitHub rebuilds it.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
