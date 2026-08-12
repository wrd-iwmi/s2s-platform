# Map layers (GeoJSON)

Put GeoJSON files here to draw points, lines or polygons on the homepage map —
basin boundaries, irrigation command areas, station networks, districts,
anything with coordinates.

---

## Adding a layer

**1. Put the file in this folder.** It must be `.geojson` (or `.json`) in
WGS84 / EPSG:4326 — plain latitude and longitude. That is what every tool
exports by default.

**2. Add a block to `_data/geography.yml`** under `layers:`

```yaml
layers:
  - name: "Cauvery basin"
    file: assets/geo/cauvery-basin.geojson
    colour: "#0f6f7d"
    fill_opacity: 0.15
    weight: 1.5
    label_field: name
    popup_fields: [name, area_km2]
```

**3. Commit.** That is all. A layer switcher appears in the top right of the map
automatically as soon as there is at least one layer.

---

## The options

| Option | What it does | Default |
| --- | --- | --- |
| `name` | Shown in the layer switcher. **Required.** | — |
| `file` | Path from the site root. **Required.** | — |
| `colour` | Line colour, and fill colour for polygons | `#0f6f7d` |
| `fill_opacity` | 0 to 1. Use `0` for outline-only polygons | `0.15` |
| `weight` | Line thickness in pixels | `1.5` |
| `point_radius` | Marker size, if the file contains points | `5` |
| `label_field` | Property to use as the hover tooltip and popup heading | none |
| `popup_fields` | Properties to list in the popup. Omit to show them all | all |
| `show` | `false` = listed in the switcher but off when the page loads | `true` |

`label_field` and `popup_fields` refer to keys inside each feature's
`properties` object. If your file has a feature like this:

```json
{ "type": "Feature",
  "properties": { "basin": "Cauvery", "area_km2": 81155 },
  "geometry": { ... } }
```

then use `label_field: basin` and `popup_fields: [basin, area_km2]`.

---

## Keeping files small

**Aim for under 1 MB.** Much of this site's audience is on modest mobile
connections, and a 20 MB boundary file will stall the page for them.

Layers are fetched only when the map scrolls into view, so a visitor who never
reaches that section pays nothing. But once they do scroll, they pay the full
size.

### The one-command fix

```bash
python3 _scripts/simplify_geojson.py assets/geo/your-file.geojson --keep NAM_0
```

That writes `your-file.min.geojson` beside the original and prints the saving.
No dependencies — plain Python 3.

It does three things: rounds coordinates to 4 decimal places (about 11 m —
exporters typically write 15, which is nanometre precision), removes vertices
that make no visible difference at map zoom, and keeps only the attributes you
name.

Real result on the country boundary file in this folder:

```
  in : countryboundaries.geojson       6.94 MB   168,086 points
  out: countryboundaries.min.geojson     565 KB    31,241 points
  92.1% smaller
```

Useful options:

```bash
--tolerance 0.02                  stronger simplification (default 0.01, ~1 km)
--tolerance 0.005                 gentler, keeps more detail
--keep NAM_0 AREA_KM2             keep only these properties
--drop-props                      drop all properties
--filter NAM_0=India,Ghana        keep only matching features
--no-simplify                     round coordinates only, keep every vertex
```

**Simplify a copy, never your analysis file.** At the default tolerance a
boundary can move by up to about a kilometre. Invisible on a locator map,
unacceptable for anything quantitative.

### Or do it in the browser

[mapshaper.org](https://mapshaper.org) — drag the file in, move the simplify
slider to 5–10%, export as GeoJSON. Nothing to install, and it shows the new
file size as you go.

---

## Converting from other formats

| You have | How to get GeoJSON |
| --- | --- |
| Shapefile (`.shp`) | Drag the whole set (`.shp`, `.shx`, `.dbf`, `.prj`) into mapshaper.org and export as GeoJSON. Or QGIS: right-click layer → Export → Save Features As → GeoJSON |
| KML / KMZ | mapshaper.org, or QGIS as above |
| CSV of lat/lon points | QGIS: Layer → Add Delimited Text Layer, then export as GeoJSON. Or geojson.io |
| Google Earth Engine | `Export.table.toDrive({collection: fc, fileFormat: 'GeoJSON'})` |
| Python | `geopandas`: `gdf.to_crs(4326).to_file('out.geojson', driver='GeoJSON')` |

**Check the projection.** If your layer lands in the Gulf of Guinea (0°N, 0°E)
or does not appear at all, the file is almost certainly in a projected CRS —
UTM, Web Mercator, a national grid — rather than lat/lon. Reproject to EPSG:4326
and re-export.

---

## Trying it out

Two demonstration files ship with the site:

- `EXAMPLE-areas.geojson` — two polygons
- `EXAMPLE-points.geojson` — three points

**They are not programme data.** They are coarse rectangles and invented
locations, there to show how styling and popups behave. To see them, uncomment
the two example blocks at the bottom of `_data/geography.yml`, and comment them
out again afterwards.

---

## If a layer does not appear

The map is built so that a broken layer can never take the whole map down — it
logs a warning and carries on. Open the browser console (F12) to see it.

| Symptom | Cause |
| --- | --- |
| `404` in the console | The `file:` path is wrong. It starts from the site root: `assets/geo/your-file.geojson`, no leading slash |
| `Unexpected token` in the console | The file is not valid JSON. Paste it into [geojson.io](https://geojson.io) to find the problem |
| Layer loads but sits in the wrong place | Wrong projection — reproject to EPSG:4326 |
| Nothing loads when opening the offline preview folder | **Expected.** Browsers block `fetch` from `file://` URLs, so no layer can ever load that way. The map now shows an amber note saying so. Check on the published site, or serve the built folder over HTTP — see below |
| Popup shows raw field names | Set `label_field` and `popup_fields` to the properties you want |
| Layer loads but the page is slow | The file is too big. Run the simplify script above |

A failed layer never takes the map down — the map still draws, and an amber note
appears on it naming the layer and the error.

### Checking layers locally

Because of the `file://` restriction, the offline preview folder cannot show
layers. To check them on your own machine, serve the built site over HTTP:

```bash
cd _site            # or the preview folder
python3 -m http.server 8000
```

Then open `http://localhost:8000`. If the site uses a `baseurl` such as
`/s2s-platform`, put the built files inside a folder of that name first, so the
paths line up:

```bash
mkdir -p /tmp/serve/s2s-platform && cp -r _site/* /tmp/serve/s2s-platform/
cd /tmp/serve && python3 -m http.server 8000
# open http://localhost:8000/s2s-platform/
```
