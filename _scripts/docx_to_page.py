#!/usr/bin/env python3
"""
Convert a filled-in Word intake form into a page for this site.

    python3 _scripts/docx_to_page.py submissions/aware-update.docx

That reads the Word document, works out what kind of page it is, converts it to
markdown with the right front matter, and writes it into the matching folder.

    python3 _scripts/docx_to_page.py submissions/*.docx          # a whole batch
    python3 _scripts/docx_to_page.py form.docx --dry-run         # print, don't write
    python3 _scripts/docx_to_page.py form.docx --slug my-name    # set the file name

--------------------------------------------------------------------------------
HOW THE FORM WORKS
--------------------------------------------------------------------------------
The Word templates in `intake-forms/` are ordinary documents with **Heading 2**
lines naming each field, and normal paragraphs underneath holding the answer.

    Title                     ← Heading 2
    AWARE                     ← the answer

    Tags                      ← Heading 2
    Drought                   ← one per line, or comma-separated
    Early warning

The script matches heading text to field names, so a researcher only has to type
into a Word document. Headings they leave blank are skipped, which produces the
site's "information to be added" placeholder — exactly the right outcome.

Bold, italic, bullet lists, numbered lists and tables all carry across.

--------------------------------------------------------------------------------
REQUIREMENTS
--------------------------------------------------------------------------------
Nothing to install. A .docx file is a zip archive of XML, and this script reads
it with the Python standard library.
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


# ==========================================================================
# 1. FIELD DEFINITIONS
#    Each collection lists the headings the form may contain and how the
#    answer should be stored. Add a row here to add a field to the form.
#
#    kind:  text   one line, becomes  field: value
#           block  several paragraphs, becomes the page body or a folded scalar
#           list   one item per line, becomes a YAML list
#           pairs  "Label — description" lines, becomes a list of objects
# ==========================================================================

COMMON = {
    'title':        ('title', 'text'),
    'summary':      ('summary', 'text'),
    'status':       ('status', 'text'),
    'tags':         ('tags', 'list'),
    'regions':      ('regions', 'list'),
    'deliverables': ('deliverables', 'list'),
    'team':         ('team', 'list'),
    'weight':       ('weight', 'text'),
    'last updated': ('updated', 'text'),
    'updated':      ('updated', 'text'),
    'links':        ('links', 'links'),
    'main text':    ('__body__', 'block'),
    'body':         ('__body__', 'block'),
    'description':  ('__body__', 'block'),
}

SCHEMAS = {
    'tools': {
        **COMMON,
        'problem addressed':   ('problem', 'text'),
        'organisation':        ('organisation', 'text'),
        'key capabilities':    ('capabilities', 'pairs:title,description'),
        'how it works':        ('workflow', 'pairs:stage,detail'),
        'outputs':             ('outputs', 'list'),
        'related tools':       ('related_tools', 'list'),
        'related methods':     ('related_methods', 'list'),
        'related case studies':('related_case_studies', 'list'),
        'related tutorials':   ('related_tutorials', 'list'),
        'related apis':        ('related_apis', 'list'),
        'citation':            ('citation', 'text'),
    },
    'methods': {
        **COMMON,
        'plain language summary': ('executive_summary', 'text'),
        'executive summary':      ('executive_summary', 'text'),
        'objective':              ('objective', 'text'),
        'input datasets':         ('inputs', 'list'),
        'outputs':                ('outputs', 'list'),
        'spatial scale':          ('spatial_scale', 'text'),
        'temporal scale':         ('temporal_scale', 'text'),
        'validation':             ('validation', 'text'),
        'uncertainty':            ('uncertainty', 'text'),
        'computational requirements': ('compute_notes', 'text'),
        'reproducibility':        ('reproducibility', 'text'),
        'strengths':              ('strengths', 'list'),
        'limitations':            ('limitations', 'list'),
        'references':             ('references', 'pairs:citation,url'),
        'related tools':          ('related_tools', 'list'),
    },
    'apis': {
        **COMMON,
        'purpose':          ('purpose', 'text'),
        'version':          ('version', 'text'),
        'base url':         ('base_url', 'text'),
        'authentication':   ('authentication', 'text'),
        'response formats': ('response_formats', 'list'),
        'update frequency': ('update_frequency', 'text'),
        'coverage':         ('coverage', 'text'),
        'rate limits':      ('rate_limits', 'text'),
        'interactive docs url': ('console_url', 'text'),
        'console url':      ('console_url', 'text'),
        'service url':      ('service_url', 'text'),
        'related tool':     ('related_tool', 'text'),
    },
    'tutorials': {
        **COMMON,
        'difficulty':     ('difficulty', 'text'),
        'objective':      ('objective', 'text'),
        'prerequisites':  ('prerequisites', 'list'),
        'required data and tools': ('requirements', 'list'),
        'estimated time': ('estimated_time', 'text'),
        'related tool':   ('related_tool', 'text'),
        'related method': ('related_method', 'text'),
        'steps':          ('__body__', 'block'),
    },
    'case_studies': {
        **COMMON,
        'location':           ('location', 'text'),
        'context':            ('context', 'text'),
        'climate information':('climate_information', 'list'),
        'workflow':           ('workflow', 'pairs:stage,detail'),
        'decision':           ('decision', 'text'),
        'results':            ('results', 'text'),
        'lessons':            ('lessons', 'list'),
        'end users':          ('end_users', 'list'),
        'partners':           ('partners', 'list'),
        'related tools':      ('related_tools', 'list'),
        'related methods':    ('related_methods', 'list'),
    },
    'datasets': {
        **COMMON,
        'source':              ('source', 'text'),
        'role':                ('role', 'text'),
        'variables':           ('variables', 'list'),
        'spatial resolution':  ('spatial_resolution', 'text'),
        'temporal resolution': ('temporal_resolution', 'text'),
        'temporal coverage':   ('temporal_coverage', 'text'),
        'update frequency':    ('update_frequency', 'text'),
        'licence':             ('licence', 'text'),
        'license':             ('licence', 'text'),
    },
}

# Words that mean "I have not filled this in" — treated as blank, so the page
# shows a proper placeholder instead of the instruction text.
IGNORE_VALUES = {
    '', '-', '--', 'n/a', 'na', 'none', 'tbc', 'tbd', 'to be added',
    'to be confirmed', 'unknown', 'delete this line if you cannot answer it',
    'type your answer here', 'your answer here', '[your answer here]',
}

# Required fields per collection. Missing ones are reported, not invented.
REQUIRED = {
    'tools': ['title', 'summary'],
    'methods': ['title', 'summary', 'executive_summary'],
    'apis': ['title', 'summary', 'purpose'],
    'tutorials': ['title', 'summary', 'objective', 'difficulty'],
    'case_studies': ['title', 'summary', 'location', 'context'],
    'datasets': ['title', 'summary', 'source', 'role'],
}

VALID_STATUS = {'Operational', 'In development', 'Pilot', 'Planned', 'Documentation pending'}
VALID_DIFFICULTY = {'Beginner', 'Intermediate', 'Advanced'}
VALID_ROLE = {'Forecast', 'Observation', 'Reanalysis', 'Projection', 'Ancillary', 'Product'}
VALID_KIND = {'Web application', 'API', 'Dataset', 'Repository', 'Documentation',
              'Download', 'Demonstration', 'Publication'}


# ==========================================================================
# 2. READING THE .DOCX
# ==========================================================================

def run_text(run) -> str:
    """Text of one run, carrying bold and italic through as markdown."""
    text = ''.join(node.text or '' for node in run.iter(f'{W}t'))
    if not text:
        if run.find(f'{W}br') is not None:
            return '\n'
        if run.find(f'{W}tab') is not None:
            return ' '
        return ''
    props = run.find(f'{W}rPr')
    if props is not None:
        stripped = text.strip()
        if stripped:
            lead = text[:len(text) - len(text.lstrip())]
            trail = text[len(text.rstrip()):]
            if props.find(f'{W}b') is not None:
                stripped = f'**{stripped}**'
            if props.find(f'{W}i') is not None:
                stripped = f'*{stripped}*'
            text = lead + stripped + trail
    return text


R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'


def paragraph_text(par, rels=None) -> str:
    """
    Text of one paragraph.

    Word wraps a clicked-in link in a <w:hyperlink> element, so its runs are
    *not* direct children of the paragraph. Walking only direct children — which
    an earlier version of this script did — silently dropped every URL a
    researcher pasted in. We walk the whole paragraph instead, and where the
    visible text differs from the link target we emit markdown `[text](url)` so
    neither the wording nor the address is lost.
    """
    parts = []
    for node in par:
        if node.tag == f'{W}r':
            parts.append(run_text(node))
        elif node.tag == f'{W}hyperlink':
            inner = ''.join(run_text(r) for r in node.iter(f'{W}r'))
            target = (rels or {}).get(node.get(f'{R}id'), '')
            anchor = node.get(f'{W}anchor')
            if not target and anchor:
                target = '#' + anchor
            visible = inner.strip()
            if target and visible and visible.rstrip('/') != target.rstrip('/'):
                parts.append(f'[{visible}]({target})')
            else:
                parts.append(inner or target)
        else:
            # Tracked insertions, smart tags, bookmarks and content controls all
            # nest runs one level deeper. Take any text they carry.
            runs = list(node.iter(f'{W}r'))
            if runs:
                parts.append(''.join(run_text(r) for r in runs))
    return ''.join(parts).strip()


def read_rels(path: Path):
    """Map a hyperlink relationship id to the URL it points at."""
    rels = {}
    try:
        with zipfile.ZipFile(path) as zf:
            if 'word/_rels/document.xml.rels' not in zf.namelist():
                return rels
            root = ET.fromstring(zf.read('word/_rels/document.xml.rels'))
        for rel in root:
            if rel.get('Type', '').endswith('/hyperlink'):
                rels[rel.get('Id')] = rel.get('Target', '')
    except Exception:
        pass
    return rels


def paragraph_style(par) -> str:
    props = par.find(f'{W}pPr')
    if props is None:
        return ''
    style = props.find(f'{W}pStyle')
    return (style.get(f'{W}val') or '') if style is not None else ''


def list_level(par):
    """Return the list indent level, or None if the paragraph is not a list."""
    props = par.find(f'{W}pPr')
    if props is None:
        return None
    num = props.find(f'{W}numPr')
    if num is None:
        return None
    ilvl = num.find(f'{W}ilvl')
    return int(ilvl.get(f'{W}val')) if ilvl is not None else 0


def table_to_markdown(tbl, rels=None) -> str:
    rows = []
    for tr in tbl.findall(f'{W}tr'):
        cells = []
        for tc in tr.findall(f'{W}tc'):
            text = ' '.join(paragraph_text(p, rels) for p in tc.findall(f'{W}p')).strip()
            cells.append(text.replace('|', '\\|'))
        if any(cells):
            rows.append(cells)
    if not rows:
        return ''
    width = max(len(r) for r in rows)
    rows = [r + [''] * (width - len(r)) for r in rows]
    out = ['| ' + ' | '.join(rows[0]) + ' |',
           '| ' + ' | '.join(['---'] * width) + ' |']
    for r in rows[1:]:
        out.append('| ' + ' | '.join(r) + ' |')
    return '\n'.join(out)


def read_blocks(path: Path):
    """Walk the document, yielding ('heading'|'para'|'bullet'|'number'|'table', text)."""
    with zipfile.ZipFile(path) as zf:
        xml = zf.read('word/document.xml')
    body = ET.fromstring(xml).find(f'{W}body')
    if body is None:
        return

    numbering_kinds = read_numbering(path)
    rels = read_rels(path)

    for child in body:
        tag = child.tag
        if tag == f'{W}p':
            style = paragraph_style(child)
            text = paragraph_text(child, rels)
            if not text:
                continue
            # Instruction text in the Word template carries the 'Guidance'
            # style. It is never part of the researcher's answer.
            if style == 'Guidance':
                continue
            if style.lower().startswith('heading') or style in ('Title', 'Subtitle'):
                level = re.sub(r'\D', '', style) or '1'
                yield ('heading', text, int(level))
            elif list_level(child) is not None:
                props = child.find(f'{W}pPr')
                num = props.find(f'{W}numPr')
                num_id_el = num.find(f'{W}numId')
                num_id = num_id_el.get(f'{W}val') if num_id_el is not None else None
                kind = numbering_kinds.get(num_id, 'bullet')
                yield (kind, text, list_level(child) or 0)
            else:
                yield ('para', text, 0)
        elif tag == f'{W}tbl':
            md = table_to_markdown(child, rels)
            if md:
                yield ('table', md, 0)


def read_numbering(path: Path):
    """Map numId to 'bullet' or 'number' so ordered lists survive."""
    kinds = {}
    try:
        with zipfile.ZipFile(path) as zf:
            if 'word/numbering.xml' not in zf.namelist():
                return kinds
            root = ET.fromstring(zf.read('word/numbering.xml'))
        abstract = {}
        for a in root.findall(f'{W}abstractNum'):
            aid = a.get(f'{W}abstractNumId')
            lvl = a.find(f'{W}lvl')
            fmt = 'bullet'
            if lvl is not None:
                nf = lvl.find(f'{W}numFmt')
                if nf is not None and nf.get(f'{W}val') != 'bullet':
                    fmt = 'number'
            abstract[aid] = fmt
        for n in root.findall(f'{W}num'):
            nid = n.get(f'{W}numId')
            ref = n.find(f'{W}abstractNumId')
            if ref is not None:
                kinds[nid] = abstract.get(ref.get(f'{W}val'), 'bullet')
    except Exception:
        pass
    return kinds


# ==========================================================================
# 3. TURNING BLOCKS INTO FIELDS
# ==========================================================================

def is_blank(value: str) -> bool:
    return value.strip().lower().strip('.') in IGNORE_VALUES


def clean_heading(text: str) -> str:
    """Normalise a field heading: drop the [required] marker and any emphasis."""
    text = re.sub(r'\[\s*required\s*\]', '', text, flags=re.I)
    text = re.sub(r'\(\s*required\s*\)', '', text, flags=re.I)
    text = text.replace('**', '').replace('*', '')
    return text.strip().rstrip(':').strip()


def collect_sections(blocks):
    """Group the document into {heading: [blocks]} plus anything before the first heading."""
    sections = {}
    current = None
    preamble = []
    for kind, text, level in blocks:
        if kind == 'heading' and level == 1:
            # Document title — not a field.
            current = None
            continue
        if kind == 'heading' and level == 2:
            current = clean_heading(text)
            sections.setdefault(current, [])
        elif current is None:
            preamble.append((kind, text, level))
        else:
            sections[current].append((kind, text, level))
    return sections, preamble


def blocks_to_markdown(blocks) -> str:
    out = []
    for kind, text, level in blocks:
        indent = '  ' * level
        if kind == 'bullet':
            out.append(f'{indent}- {text}')
        elif kind == 'number':
            out.append(f'{indent}1. {text}')
        elif kind == 'table':
            out.append('\n' + text + '\n')
        elif kind == 'heading':
            out.append(f'\n{"#" * max(level, 3)} {text}\n')
        else:
            out.append('\n' + text + '\n')
    md = '\n'.join(out)
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()


# A bullet glyph or dash typed at the *start* of a line. Anchored, so a value
# ending in a hyphen or containing one keeps it.
BULLET_PREFIX = re.compile(r'^[\s ]*(?:[-–—•·*●▪‣⁃]\s+)?')


def blocks_to_lines(blocks):
    """
    Every non-empty line, with any leading bullet glyph removed.

    This is the literal reading of what the researcher typed. It does NOT split
    on commas — an earlier version did, which quietly deleted every comma from
    one-line prose answers such as a summary. Splitting is the caller's choice;
    see `lines_to_list`.
    """
    lines = []
    for kind, text, _ in blocks:
        if kind == 'table':
            continue
        for piece in text.split('\n'):
            piece = BULLET_PREFIX.sub('', piece).strip()
            if piece and not is_blank(piece):
                lines.append(piece)
    return lines


LABEL_MAX = 40


def lines_to_list(lines):
    """
    List fields only. A researcher may write one item per line, or put them all
    on one line separated by commas or semicolons — both are accepted.

    The split only happens when every piece looks like a short label: at most
    LABEL_MAX characters and no full stop. A sentence such as "a GeoTIFF clipped
    to the area, together with the range used for the colour scale" is one
    output, not two, and must not be chopped at its comma. Semicolons are tried
    first so "Rainfall, mm; Temperature, °C" survives intact.
    """
    if len(lines) != 1:
        return lines
    only = lines[0]
    for sep in (';', ','):
        if sep not in only:
            continue
        parts = [p.strip() for p in only.split(sep) if p.strip()]
        if len(parts) >= 2 and all(len(p) <= LABEL_MAX and '.' not in p for p in parts):
            return parts
    return lines


SPLITTERS = [' — ', ' – ', ' -- ', ' | ', ': ', ' - ']


def split_pair(line):
    for sep in SPLITTERS:
        if sep in line:
            left, right = line.split(sep, 1)
            return left.strip(), right.strip()
    return line.strip(), ''


# ==========================================================================
# 4. YAML OUTPUT
# ==========================================================================

def yaml_scalar(value, indent: int = 0) -> str:
    """
    Render one value as YAML.

    `indent` is the column the *key* sits at. A folded block scalar's
    continuation lines must be indented further than that, so the caller has to
    say where it is. Getting this wrong produces YAML that looks fine and does
    not parse — a long list item or a long capability description used to emit
    its continuation at the same depth as its own `- `, which broke the page's
    front matter outright.
    """
    if isinstance(value, bool):
        return 'true' if value else 'false'
    value = str(value).strip()
    if value == '':
        return '""'
    if '\n' in value or len(value) > 110:
        pad = ' ' * (indent + 2)
        body = '\n'.join(pad + l.strip() for l in value.split('\n') if l.strip())
        return '>-\n' + body
    if re.search(r'^[\[\]{}#&*!|>%@`\'"]|: |:$|^\s|\s$| #', value) \
            or value.lower() in ('yes', 'no', 'true', 'false', 'on', 'off', 'null', '~'):
        return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return value


def render_front_matter(fields, order):
    lines = []
    for key in order:
        if key not in fields:
            continue
        value = fields[key]
        if isinstance(value, list):
            if not value:
                continue
            if isinstance(value[0], dict):
                lines.append(f'{key}:')
                for item in value:
                    first = True
                    for k, v in item.items():
                        prefix = '  - ' if first else '    '
                        # Both forms put the key at column 4.
                        lines.append(f'{prefix}{k}: {yaml_scalar(v, 4)}')
                        first = False
            else:
                lines.append(f'{key}:')
                for item in value:
                    lines.append(f'  - {yaml_scalar(item, 4)}')
        else:
            lines.append(f'{key}: {yaml_scalar(value, 0)}')
    return '\n'.join(lines)


FIELD_ORDER = [
    'title', 'summary', 'status', 'weight', 'difficulty', 'role', 'source',
    'location', 'version', 'purpose', 'objective', 'executive_summary',
    'problem', 'context', 'organisation', 'decision', 'results',
    'spatial_scale', 'temporal_scale', 'spatial_resolution',
    'temporal_resolution', 'temporal_coverage', 'update_frequency', 'licence',
    'variables', 'estimated_time', 'authentication', 'response_formats',
    'coverage', 'rate_limits', 'base_url', 'console_url', 'service_url',
    'updated', 'tags', 'regions', 'deliverables',
    'team', 'capabilities', 'workflow', 'inputs', 'outputs', 'prerequisites',
    'requirements', 'climate_information', 'end_users', 'partners',
    'strengths', 'limitations', 'lessons', 'validation', 'uncertainty',
    'compute_notes', 'reproducibility', 'references', 'related_tool',
    'related_method', 'related_tools', 'related_methods', 'related_apis',
    'related_case_studies', 'related_tutorials', 'links', 'citation',
]


# ==========================================================================
# 5. CONVERSION
# ==========================================================================

def detect_collection(sections, preamble, override=None):
    if override:
        return override
    # The template writes "Page type: Tool" near the top.
    haystack = ' '.join(t for _, t, _ in preamble).lower()
    for heading in sections:
        haystack += ' ' + heading.lower()
    for label, coll in (('case study', 'case_studies'), ('dataset', 'datasets'),
                        ('tutorial', 'tutorials'), ('method', 'methods'),
                        ('api', 'apis'), ('tool', 'tools')):
        if re.search(rf'page type\s*[:\-]?\s*{label}', haystack):
            return coll
    # Fall back to the distinguishing headings.
    keys = {h.lower().rstrip(':') for h in sections}
    if 'plain language summary' in keys or 'executive summary' in keys:
        return 'methods'
    if 'difficulty' in keys:
        return 'tutorials'
    if 'purpose' in keys and 'base url' in keys:
        return 'apis'
    if 'location' in keys and 'context' in keys:
        return 'case_studies'
    if 'source' in keys and 'role' in keys:
        return 'datasets'
    return 'tools'


MD_LINK = re.compile(r'\[([^\]]*)\]\(([^)\s]+)\)')
KIND_BY_LOWER = {k.lower(): k for k in VALID_KIND}


def parse_links(blocks):
    """
    Each line: Label — https://url — Kind

    A Word hyperlink arrives as markdown `[text](url)`, so that form is accepted
    too. `Kind` is matched case-insensitively — Word capitalises the first word
    of a line, and a mis-cased kind used to fall back to Documentation silently.
    """
    links = []
    for line in blocks_to_lines(blocks):
        # Pull the address out of any markdown link, keeping its visible text.
        found = MD_LINK.search(line)
        md_url = found.group(2) if found else ''
        line = MD_LINK.sub(lambda m: m.group(1) or m.group(2), line)

        parts = [p.strip() for p in re.split(r'\s+[—–|]\s+|\s+--\s+', line) if p.strip()]
        if not parts:
            continue
        url = md_url or next((p for p in parts if p.startswith(('http', 'www.', '/', '#'))), '')
        if url.startswith('www.'):
            url = 'https://' + url
        kind = next((KIND_BY_LOWER[p.lower()] for p in parts if p.lower() in KIND_BY_LOWER),
                    'Documentation')
        label = next((p for p in parts if p != url and p.lower() not in KIND_BY_LOWER), '') \
            or parts[0]
        entry = {'label': label, 'url': url or '#', 'kind': kind}
        if not url or url == '#':
            entry['available'] = False
        links.append(entry)
    return links


def convert(path: Path, site_root: Path, collection_override=None, slug_override=None):
    blocks = list(read_blocks(path))
    sections, preamble = collect_sections(blocks)
    collection = detect_collection(sections, preamble, collection_override)
    schema = SCHEMAS[collection]

    fields = {}
    body_parts = []
    unknown_headings = []

    for heading, content in sections.items():
        key = heading.lower().rstrip(':').strip()
        # Ignore the instruction sections in the template.
        if key.startswith(('how to use', 'instructions', 'page type', 'before you')):
            continue
        if key not in schema:
            unknown_headings.append(heading)
            md = blocks_to_markdown(content)
            if md and not is_blank(md):
                body_parts.append(f'## {heading}\n\n{md}')
            continue

        target, kind = schema[key]
        if target == '__body__':
            md = blocks_to_markdown(content)
            if md and not is_blank(md):
                body_parts.append(md)
            continue

        if kind == 'text':
            value = ' '.join(blocks_to_lines(content)).strip()
            if value and not is_blank(value):
                fields[target] = value
        elif kind == 'list':
            values = [v for v in lines_to_list(blocks_to_lines(content)) if not is_blank(v)]
            if values:
                fields[target] = values
        elif kind == 'links':
            links = parse_links(content)
            if links:
                fields[target] = links
        elif kind.startswith('pairs:'):
            a, b = kind.split(':', 1)[1].split(',')
            items = []
            for line in blocks_to_lines(content):
                left, right = split_pair(line)
                if not left or is_blank(left):
                    continue
                items.append({a: left, b: right} if right else {a: left, b: ''})
            if items:
                fields[target] = items

    # ---- validation ------------------------------------------------------
    problems = []
    for key in REQUIRED[collection]:
        if key not in fields:
            problems.append(f"missing required field '{key}'")

    if 'status' in fields and fields['status'] not in VALID_STATUS:
        problems.append(f"status '{fields['status']}' is not one of: {', '.join(sorted(VALID_STATUS))}")
        fields.pop('status')
    if 'difficulty' in fields and fields['difficulty'] not in VALID_DIFFICULTY:
        problems.append(f"difficulty '{fields['difficulty']}' is not one of: {', '.join(sorted(VALID_DIFFICULTY))}")
        fields.pop('difficulty')
    if 'role' in fields and fields['role'] not in VALID_ROLE:
        problems.append(f"role '{fields['role']}' is not one of: {', '.join(sorted(VALID_ROLE))}")
        fields.pop('role')
    if 'weight' in fields and not str(fields['weight']).strip().isdigit():
        problems.append(f"weight '{fields['weight']}' is not a whole number — ignoring it")
        fields.pop('weight')
    if 'updated' in fields and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(fields['updated']).strip()):
        problems.append(f"updated '{fields['updated']}' is not a YYYY-MM-DD date — ignoring it")
        fields.pop('updated')

    # Every schema target must appear in FIELD_ORDER or render_front_matter drops
    # it without a word. Cheap to check, and it catches a mistyped key when a
    # field is added.
    for key in fields:
        if key not in FIELD_ORDER:
            problems.append(f"field '{key}' is missing from FIELD_ORDER in this script — not written")

    slug = slug_override or slugify(fields.get('title', path.stem))
    body = '\n\n'.join(body_parts).strip()
    if not body:
        body = ('*No main text was provided in the form. Add it by editing this '
                'file, or by filling in the "Main text" section of the Word form '
                'and converting again.*')

    page = f"---\n{render_front_matter(fields, FIELD_ORDER)}\n---\n\n{body}\n"
    return collection, slug, page, problems, unknown_headings


def slugify(value: str) -> str:
    value = re.sub(r'[^a-zA-Z0-9]+', '-', value).strip('-').lower()
    return re.sub(r'-{2,}', '-', value)[:70]


# ==========================================================================
# 6. COMMAND LINE
# ==========================================================================

def main() -> int:
    parser = argparse.ArgumentParser(
        description='Convert a filled-in Word intake form into a page for this site.')
    parser.add_argument('files', nargs='+', help='one or more .docx files')
    parser.add_argument('--collection', default=None,
                        choices=sorted(SCHEMAS), help='override the detected page type')
    parser.add_argument('--slug', default=None, help='output file name without .md')
    parser.add_argument('--site-root', default=None, help='repository root')
    parser.add_argument('--dry-run', action='store_true', help='print instead of writing')
    parser.add_argument('--force', action='store_true', help='overwrite an existing page')
    args = parser.parse_args()

    site_root = Path(args.site_root).resolve() if args.site_root \
        else Path(__file__).resolve().parent.parent
    if not (site_root / '_config.yml').exists():
        print(f"{site_root} does not look like the site root. Pass --site-root.", file=sys.stderr)
        return 1

    paths = []
    for pattern in args.files:
        paths.extend(sorted(Path(p) for p in glob.glob(pattern)))
    if not paths:
        print("No .docx files matched.", file=sys.stderr)
        return 1

    failures = 0
    for path in paths:
        if path.name.startswith('~$'):
            continue  # Word lock file
        print(f"\n{path.name}")
        try:
            collection, slug, page, problems, unknown = convert(
                path, site_root, args.collection, args.slug if len(paths) == 1 else None)
        except zipfile.BadZipFile:
            print("  ERROR: not a .docx file. Save as .docx, not .doc or .pdf.")
            failures += 1
            continue
        except Exception as exc:
            print(f"  ERROR: could not read the document — {exc}")
            failures += 1
            continue

        print(f"  page type: {collection}")
        for p in problems:
            print(f"  ! {p}")
        for h in unknown:
            print(f"  note: heading '{h}' is not a known field — kept as a section in the page text")

        if any(p.startswith('missing required') for p in problems):
            print("  NOT WRITTEN — fill in the required fields and convert again.")
            failures += 1
            continue

        out_path = site_root / f'_{collection}' / f'{slug}.md'
        if args.dry_run:
            print('  ---- would write ' + str(out_path.relative_to(site_root)) + ' ----')
            print('\n'.join('  ' + l for l in page.split('\n')[:40]))
            continue
        if out_path.exists() and not args.force:
            print(f"  {out_path.relative_to(site_root)} already exists. "
                  f"Use --force to overwrite it.")
            failures += 1
            continue

        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(page, encoding='utf-8')
        print(f"  wrote {out_path.relative_to(site_root)}")

    if not args.dry_run:
        print("\nReview the generated file, then commit it. "
              "The page appears after GitHub rebuilds the site.")
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
