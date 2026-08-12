#!/usr/bin/env python3
"""
Shrink a GeoJSON file so it is safe to put on the website.

    python3 _scripts/simplify_geojson.py assets/geo/countryboundaries.geojson

That writes `countryboundaries.min.geojson` beside it and prints the saving.

Boundary files exported from GIS tools are routinely 10–100x larger than a web
map needs. Two things cause it:

  * Coordinate precision. Exporters write 15 decimal places — nanometre
    precision on a map where one screen pixel is hundreds of metres.
  * Vertex count. A coastline traced at survey resolution looks identical to a
    simplified one at the zoom levels this map uses.

This script fixes both, plus drops attributes you are not displaying. It uses
only the Python standard library — no geopandas, no GDAL, nothing to install.

--------------------------------------------------------------------------------
OPTIONS
--------------------------------------------------------------------------------
    --precision 4        decimal places to keep (default 4, about 11 m)
    --tolerance 0.01     simplification strength in degrees (default 0.01,
                         about 1 km; use 0.005 for detail, 0.05 for very coarse)
    --keep NAM_0 NAME    only keep these properties (default: keep all)
    --drop-props         drop every property
    --filter NAM_0=India,Ghana
                         keep only features whose property matches
    --out path.geojson   output file
    --no-simplify        round coordinates only, do not remove vertices

--------------------------------------------------------------------------------
A WORD OF CAUTION
--------------------------------------------------------------------------------
Simplification moves boundaries. At the default 0.01° tolerance a national
border can shift by up to about a kilometre. That is invisible on a locator map
and unacceptable for anything analytical. **Never simplify a file you are also
using for analysis** — simplify a copy, for display only, and keep the original.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


# --------------------------------------------------------------------------
# Douglas–Peucker line simplification
# --------------------------------------------------------------------------

def perpendicular_distance(pt, start, end):
    """Distance from pt to the line through start–end, in degrees."""
    x, y = pt[0], pt[1]
    x1, y1 = start[0], start[1]
    x2, y2 = end[0], end[1]
    dx, dy = x2 - x1, y2 - y1
    if dx == 0 and dy == 0:
        return math.hypot(x - x1, y - y1)
    # Area of the parallelogram divided by base length.
    return abs(dy * x - dx * y + x2 * y1 - y2 * x1) / math.hypot(dx, dy)


def simplify(points, tolerance):
    """Iterative Douglas–Peucker. Iterative, not recursive, so a 40,000-vertex
    coastline cannot blow the stack."""
    if len(points) < 3:
        return list(points)

    keep = [False] * len(points)
    keep[0] = keep[-1] = True
    stack = [(0, len(points) - 1)]

    while stack:
        first, last = stack.pop()
        if last <= first + 1:
            continue
        worst_dist, worst_index = -1.0, first
        for i in range(first + 1, last):
            d = perpendicular_distance(points[i], points[first], points[last])
            if d > worst_dist:
                worst_dist, worst_index = d, i
        if worst_dist > tolerance:
            keep[worst_index] = True
            stack.append((first, worst_index))
            stack.append((worst_index, last))

    return [p for p, k in zip(points, keep) if k]


def simplify_ring(ring, tolerance):
    """A polygon ring must stay closed and keep at least four positions."""
    out = simplify(ring, tolerance)
    if len(out) < 4:
        # Too aggressive for this ring — keep the original rather than
        # producing invalid geometry.
        return ring
    if out[0] != out[-1]:
        out.append(out[0])
    return out


# --------------------------------------------------------------------------
# Coordinate walking
# --------------------------------------------------------------------------

def round_pos(pos, precision):
    # Keep any third element (elevation) out of the output — web maps ignore it.
    return [round(pos[0], precision), round(pos[1], precision)]


def process_geometry(geom, precision, tolerance, do_simplify):
    t = geom.get('type')
    c = geom.get('coordinates')

    if t == 'Point':
        return {'type': t, 'coordinates': round_pos(c, precision)}

    if t == 'MultiPoint':
        return {'type': t, 'coordinates': [round_pos(p, precision) for p in c]}

    if t == 'LineString':
        pts = [round_pos(p, precision) for p in c]
        if do_simplify:
            pts = simplify(pts, tolerance)
        return {'type': t, 'coordinates': pts}

    if t == 'MultiLineString':
        lines = []
        for line in c:
            pts = [round_pos(p, precision) for p in line]
            if do_simplify:
                pts = simplify(pts, tolerance)
            if len(pts) >= 2:
                lines.append(pts)
        return {'type': t, 'coordinates': lines}

    if t == 'Polygon':
        rings = []
        for ring in c:
            pts = [round_pos(p, precision) for p in ring]
            if do_simplify:
                pts = simplify_ring(pts, tolerance)
            rings.append(pts)
        return {'type': t, 'coordinates': rings}

    if t == 'MultiPolygon':
        polys = []
        for poly in c:
            rings = []
            for ring in poly:
                pts = [round_pos(p, precision) for p in ring]
                if do_simplify:
                    pts = simplify_ring(pts, tolerance)
                rings.append(pts)
            if rings and len(rings[0]) >= 4:
                polys.append(rings)
        return {'type': t, 'coordinates': polys}

    if t == 'GeometryCollection':
        return {'type': t, 'geometries': [
            process_geometry(g, precision, tolerance, do_simplify)
            for g in geom.get('geometries', [])
        ]}

    return geom


def count_positions(geom):
    t = geom.get('type')
    c = geom.get('coordinates')
    if t == 'Point':
        return 1
    if t in ('MultiPoint', 'LineString'):
        return len(c)
    if t in ('MultiLineString', 'Polygon'):
        return sum(len(r) for r in c)
    if t == 'MultiPolygon':
        return sum(len(r) for poly in c for r in poly)
    if t == 'GeometryCollection':
        return sum(count_positions(g) for g in geom.get('geometries', []))
    return 0


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(
        description='Shrink a GeoJSON file for use on the website.')
    ap.add_argument('input')
    ap.add_argument('--out', default=None)
    ap.add_argument('--precision', type=int, default=4,
                    help='decimal places to keep (default 4, about 11 m)')
    ap.add_argument('--tolerance', type=float, default=0.01,
                    help='simplification strength in degrees (default 0.01, about 1 km)')
    ap.add_argument('--keep', nargs='*', default=None,
                    help='only keep these property names')
    ap.add_argument('--drop-props', action='store_true',
                    help='drop every property')
    ap.add_argument('--filter', default=None,
                    help='keep only matching features, e.g. NAM_0=India,Ghana')
    ap.add_argument('--no-simplify', action='store_true',
                    help='round coordinates only, keep every vertex')
    args = ap.parse_args()

    src = Path(args.input)
    if not src.exists():
        print(f"Cannot find {src}", file=sys.stderr)
        return 1

    before_bytes = src.stat().st_size
    try:
        data = json.loads(src.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        print(f"{src.name} is not valid JSON — {e}", file=sys.stderr)
        print("Paste it into https://geojson.io to find the problem.", file=sys.stderr)
        return 1

    if data.get('type') != 'FeatureCollection':
        print(f"Expected a FeatureCollection, found {data.get('type')!r}.", file=sys.stderr)
        return 1

    features = data.get('features', [])
    before_positions = sum(count_positions(f.get('geometry') or {}) for f in features)

    # Optional feature filter.
    if args.filter:
        if '=' not in args.filter:
            print("--filter must look like NAM_0=India,Ghana", file=sys.stderr)
            return 1
        key, values = args.filter.split('=', 1)
        wanted = {v.strip().lower() for v in values.split(',')}
        kept = [f for f in features
                if str((f.get('properties') or {}).get(key, '')).lower() in wanted]
        print(f"filter {key}: kept {len(kept)} of {len(features)} features")
        missing = wanted - {str((f.get('properties') or {}).get(key, '')).lower() for f in kept}
        if missing:
            print(f"  ! no feature matched: {', '.join(sorted(missing))}")
        features = kept

    out_features = []
    for f in features:
        geom = f.get('geometry')
        if not geom:
            continue
        props = f.get('properties') or {}
        if args.drop_props:
            props = {}
        elif args.keep:
            props = {k: v for k, v in props.items() if k in args.keep}
            for k in args.keep:
                if k not in props:
                    print(f"  ! property {k!r} not present on a feature")
        out_features.append({
            'type': 'Feature',
            'properties': props,
            'geometry': process_geometry(geom, args.precision, args.tolerance,
                                         not args.no_simplify),
        })

    after_positions = sum(count_positions(f['geometry']) for f in out_features)

    # A CRS member is not part of the current GeoJSON spec (RFC 7946); WGS84 is
    # assumed. Dropping it saves bytes and avoids confusing some tools.
    out = {'type': 'FeatureCollection', 'features': out_features}
    if data.get('name'):
        out['name'] = data['name']

    dest = Path(args.out) if args.out else src.with_suffix('').with_suffix('')
    if not args.out:
        dest = src.parent / (src.name.replace('.geojson', '').replace('.json', '') + '.min.geojson')

    dest.write_text(json.dumps(out, separators=(',', ':')), encoding='utf-8')
    after_bytes = dest.stat().st_size

    def mb(n):
        return f"{n/1024/1024:.2f} MB" if n >= 1024 * 1024 else f"{n/1024:.0f} KB"

    print()
    print(f"  in : {src.name:<40} {mb(before_bytes):>10}  {before_positions:>8,} points")
    print(f"  out: {dest.name:<40} {mb(after_bytes):>10}  {after_positions:>8,} points")
    saved = 100 * (1 - after_bytes / before_bytes) if before_bytes else 0
    print(f"  {saved:.1f}% smaller")
    print()
    if after_bytes > 1024 * 1024:
        print("  Still over 1 MB. Try a larger --tolerance (0.02, 0.05), fewer")
        print("  properties with --keep, or --filter to drop features you do not need.")
    else:
        print(f"  Point _data/geography.yml at assets/geo/{dest.name}")
    print()
    print("  Check the result on a map before committing. Simplification moves")
    print("  boundaries — keep the original for anything analytical.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
