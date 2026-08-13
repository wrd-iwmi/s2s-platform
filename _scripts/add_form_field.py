#!/usr/bin/env python3
"""
Add a field to one of the Word intake forms, in place.

    python3 _scripts/add_form_field.py intake-forms/tool-form.docx \
        --heading "Related tools" \
        --guidance "File names of tool pages, without the .md." \
        --example  "aware" \
        --hint     "One per line." \
        --before   "Citation"

Why this exists
---------------
The forms in `intake-forms/` are hand-built Word documents. Adding a field by
hand means opening Word, matching the Heading 2 / Guidance / Answer styles
exactly, and saving without letting Word rewrite anything else. Doing it here
guarantees the new block is byte-identical in structure to the existing ones,
which is what `docx_to_page.py` relies on to find the answer.

After adding a heading here, add the matching row to `SCHEMAS` in
`docx_to_page.py`, or the converter will keep the answer as a body section
instead of a front-matter field. `--check` verifies that link both ways.

Requires nothing but Python 3.8+. A .docx is a zip of XML.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import zipfile
from pathlib import Path

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
DOC = 'word/document.xml'


def esc(text: str) -> str:
    return (text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def guidance_para(text: str, colour: str = '5E6874', size: str = '18') -> str:
    return ('<w:p><w:pPr><w:pStyle w:val="Guidance"/><w:spacing w:after="80"/></w:pPr>'
            f'<w:r><w:rPr><w:i/><w:color w:val="{colour}"/><w:sz w:val="{size}"/></w:rPr>'
            f'<w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:p>')


def build_block(heading: str, guidance: str, example: str = '', hint: str = '') -> str:
    """One field: blue heading, grey guidance, teal example, grey hint, answer line."""
    out = ['<w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr>'
           f'<w:r><w:t xml:space="preserve">{esc(heading)}</w:t></w:r></w:p>']
    if guidance:
        out.append(guidance_para(guidance))
    if example:
        out.append(guidance_para(f'Example: {example}', colour='0F6F7D'))
    if hint:
        out.append(guidance_para(hint, size='16'))
    out.append('<w:p><w:pPr><w:pStyle w:val="Answer"/><w:spacing w:after="280"/></w:pPr>'
               '<w:r><w:rPr><w:color w:val="999999"/></w:rPr>'
               '<w:t>Type your answer here</w:t></w:r></w:p>')
    return ''.join(out)


def heading_offset(xml: str, heading: str) -> int:
    """Character offset of the <w:p> that opens the given Heading 2, or -1."""
    for m in re.finditer(r'<w:p>(?:(?!</w:p>).)*?</w:p>', xml, flags=re.S):
        block = m.group(0)
        if 'w:val="Heading2"' not in block:
            continue
        text = ''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', block, flags=re.S))
        if text.strip().lower().rstrip(':') == heading.strip().lower().rstrip(':'):
            return m.start()
    return -1


def rewrite(path: Path, new_xml: str) -> None:
    """Rewrite document.xml, copying every other part of the zip unchanged."""
    tmp = path.with_suffix('.docx.tmp')
    with zipfile.ZipFile(path) as src, \
            zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as dst:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename == DOC:
                data = new_xml.encode('utf-8')
            dst.writestr(item, data)
    shutil.move(str(tmp), str(path))


def add_field(path: Path, heading: str, guidance: str, example: str, hint: str,
              before: str | None, dry_run: bool) -> int:
    xml = zipfile.ZipFile(path).read(DOC).decode('utf-8')

    if heading_offset(xml, heading) != -1:
        print(f"  '{heading}' is already in {path.name} — nothing to do.")
        return 0

    block = build_block(heading, guidance, example, hint)

    if before:
        at = heading_offset(xml, before)
        if at == -1:
            print(f"  ERROR: {path.name} has no heading '{before}' to insert before.",
                  file=sys.stderr)
            return 1
        new_xml = xml[:at] + block + xml[at:]
    else:
        at = xml.rindex('</w:body>')
        # Keep the final section properties last.
        sect = re.search(r'<w:sectPr\b', xml[:at])
        at = sect.start() if sect else at
        new_xml = xml[:at] + block + xml[at:]

    where = f"before '{before}'" if before else 'at the end'
    if dry_run:
        print(f"  would add '{heading}' to {path.name} {where}")
        return 0
    rewrite(path, new_xml)
    print(f"  added '{heading}' to {path.name} {where}")
    return 0


def check(forms_dir: Path, scripts_dir: Path) -> int:
    """Every Heading 2 in every form should be a key the converter recognises."""
    sys.path.insert(0, str(scripts_dir))
    import docx_to_page as conv

    problems = 0
    for form in sorted(forms_dir.glob('*.docx')):
        # ~$ is a Word lock file. EXAMPLE-* is a filled sample, not a blank form,
        # so it is allowed to have fewer headings than the schema offers.
        if form.name.startswith(('~$', 'EXAMPLE')):
            continue
        blocks = list(conv.read_blocks(form))
        sections, preamble = conv.collect_sections(blocks)
        collection = conv.detect_collection(sections, preamble)
        schema = conv.SCHEMAS[collection]
        print(f"{form.name} -> {collection}")
        for heading in sections:
            key = heading.lower().rstrip(':').strip()
            if key.startswith(('how to use', 'instructions', 'page type', 'before you')):
                continue
            if key not in schema:
                print(f"  ! heading '{heading}' has no row in SCHEMAS['{collection}']")
                problems += 1
        targets = {t for t, _ in schema.values()} - {'__body__'}
        present = {schema[h.lower().rstrip(':')][0] for h in sections
                   if h.lower().rstrip(':') in schema}
        for missing in sorted(targets - present):
            print(f"  ! SCHEMAS['{collection}'] maps to '{missing}', "
                  f"but no heading in the form produces it")
            problems += 1
        for target in sorted(present - {'__body__'}):
            if target not in conv.FIELD_ORDER:
                print(f"  ! '{target}' is missing from FIELD_ORDER — it would be dropped")
                problems += 1
    print(f"\n{problems} problem(s)")
    return 1 if problems else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split('Why this exists')[0].strip(),
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('files', nargs='*', help='one or more form .docx files')
    parser.add_argument('--heading', help='the field name, as a Heading 2 line')
    parser.add_argument('--guidance', default='', help='grey explanatory line')
    parser.add_argument('--example', default='', help='teal "Example: ..." line')
    parser.add_argument('--hint', default='', help='small grey line, e.g. "One per line."')
    parser.add_argument('--before', default=None,
                        help='insert before this existing heading (default: at the end)')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--check', action='store_true',
                        help='verify every form heading maps to a converter field')
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    if args.check:
        return check(here.parent / 'intake-forms', here)

    if not args.files or not args.heading:
        parser.error('give at least one .docx file and --heading (or use --check)')

    failures = 0
    for name in args.files:
        path = Path(name)
        if not path.exists():
            print(f"  ERROR: {path} not found", file=sys.stderr)
            failures += 1
            continue
        failures += add_field(path, args.heading, args.guidance, args.example,
                              args.hint, args.before, args.dry_run)
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
