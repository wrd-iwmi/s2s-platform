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

A full-resolution basin or admin boundary is often tens of megabytes and looks
identical on screen once simplified. To fix that:

- **[mapshaper.org](https://mapshaper.org)** — drag your file in, move the
  simplify slider to around 5–10%, export as GeoJSON. Runs entirely in the
  browser, nothing to install, and it will tell you the new file size.
- Delete attribute columns you are not going to show in a popup. They are often
  most of the file size.
- Round coordinates to 4 or 5 decimal places (about 1–10 m precision) — plenty
  for a locator map.

The layers are fetched only when the map scrolls into view, so a visitor who
never reaches that section pays nothing for them. But once they do scroll, they
pay the full size.

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
| Nothing loads when opening the offline preview folder | Expected. Browsers block `fetch` from `file://` URLs. Run `python3 -m http.server` in the built folder and open `http://localhost:8000` instead, or just check on the live site |
| Popup shows raw field names | Set `label_field` and `popup_fields` to the properties you want |
