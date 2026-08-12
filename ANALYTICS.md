# Measuring use of the site and the repository

Two separate systems, because they measure different things and neither sees
what the other does.

| | Google Analytics | GitHub |
| --- | --- | --- |
| Covers | The website — pages, downloads, outbound clicks | The repository — clones, forks, source views |
| History | Indefinite | **14 days**, unless you archive it |
| Set-up | Done, see below | Nothing to configure |

---

## 1. Website — Google Analytics

Already wired up. The measurement ID lives in `_config.yml`:

```yaml
google_analytics: "G-NQSWBCK6QN"
```

Empty that field and no script loads and no cookie is set — useful for a staging
copy.

### What is tracked beyond page views

Page views come free. On top of those, `_includes/analytics.html` records the
events that actually matter for a documentation site:

| Event | Fires when | Useful for |
| --- | --- | --- |
| `file_download` | Any link to `.ipynb`, `.geojson`, `.csv`, `.json`, `.pdf`, `.zip`, `.nc`, `.tif`… | Which datasets and notebooks people take away |
| `repo_zip_download` | A GitHub `/archive/` link — the "Download ZIP" path | Repository downloads started from the site |
| `repo_fork_click` | A GitHub `/fork` link | Fork intent |
| `repo_release_click` | A GitHub `/releases` link | Interest in packaged versions |
| `repo_visit` | Any other link to the repository | Traffic you send to GitHub |
| `notebook_open` | Colab or nbviewer buttons, with `service` naming which | Whether tutorials are actually run |
| `outbound_click` | Any other external link, with the domain | Which partners and sources people follow |
| `search` | Someone stops typing in the site search, with the term and the result count | **What people look for — and what they search for and don't find** |
| `map_layer_toggle` | The map layer switcher is used | Whether the GeoJSON layers earn their weight |

That `search` event is the most valuable thing here. A search term returning
zero results is a direct, unambiguous request for a page you have not written.

### Seeing the events

They appear in GA4 within a minute under **Reports → Realtime**, and within
about 24 hours in **Reports → Engagement → Events**.

**Worth doing once:** mark the important ones as conversions so they get their
own reporting. GA4 → **Admin → Events → Mark as key event** for
`file_download`, `repo_zip_download` and `notebook_open`.

**Also worth doing:** GA4 → **Admin → Data streams → your stream → Configure tag
settings → Show all → Define internal traffic**, and add your office IP range so
the team's own visits don't inflate the numbers.

---

## 2. Repository — what GitHub reports

Nothing to install. Go to the repository → **Insights** → **Traffic**.

### What you get

| Metric | Where | Notes |
| --- | --- | --- |
| **Views** and unique visitors | Insights → Traffic | Views of the repository pages on github.com |
| **Clones** and unique cloners | Insights → Traffic | `git clone`, and this is the closest thing to a "download" count |
| **Referring sites** | Insights → Traffic | Where repository visitors came from |
| **Popular content** | Insights → Traffic | Which files people look at |
| **Forks** | Insights → Forks, and the repo header | Full list, with who and when |
| **Stars** | Repo header → Stargazers | Full list |
| **Watchers** | Repo header | People subscribed to notifications |

### The catch, and it matters

**Traffic data is kept for 14 days only.** GitHub does not archive it. If nobody
looks for a fortnight, that period is gone permanently.

You also need **push access** to see the Traffic tab at all — it is not public.

### Archiving traffic data so you keep a history

Two options.

**Manual.** Open Insights → Traffic once a fortnight and screenshot or note the
figures. Free, and adequate if the numbers are for occasional reporting.

**Automated.** A scheduled GitHub Action calls the traffic API every week and
commits the numbers to the repository, building a permanent record. The API
endpoints are:

```
GET /repos/wrd-iwmi/s2s-platform/traffic/views
GET /repos/wrd-iwmi/s2s-platform/traffic/clones
GET /repos/wrd-iwmi/s2s-platform/traffic/popular/paths
GET /repos/wrd-iwmi/s2s-platform/traffic/popular/referrers
GET /repos/wrd-iwmi/s2s-platform/forks
```

All need a token with `repo` scope. Ask and I will write the workflow — it is
about thirty lines, runs weekly, and costs nothing on a public repository.

### What GitHub does *not* tell you

Be clear about these before promising numbers to anyone:

- **"Download ZIP" clicks are not reported separately.** They are counted as
  clones, mixed in with real `git clone` calls. The GA `repo_zip_download` event
  above only catches ZIP downloads that *started from this website* — someone
  who goes straight to github.com is invisible to it.
- **Individual file downloads from the repository are not counted.** Only
  release assets are, and only if you publish formal releases.
- **Nobody is identified.** Clone and view counts are unique-visitor counts, not
  named users. Forks and stars *are* attributed, because those are public acts.
- **Automated traffic inflates clones.** CI systems, mirrors and scrapers all
  clone. Treat clone counts as an upper bound.

### If you publish releases

Release asset downloads *are* counted precisely, per asset, indefinitely:

```
GET /repos/wrd-iwmi/s2s-platform/releases
```

Each asset carries a `download_count`. If download numbers matter for reporting,
publishing a tagged release — say a dated snapshot of the documentation — gives
you a hard figure that the clone count cannot.

---

## 3. Reading the two together

A realistic picture needs both, and they answer different questions:

- **"Is anyone reading this?"** → GA page views and average engagement time.
- **"Is anyone *using* it?"** → GA `file_download` and `notebook_open`, plus
  GitHub clones.
- **"What are we missing?"** → GA `search` events with zero results.
- **"Who is building on it?"** → GitHub forks and stars, which name people.
- **"Where is the audience?"** → GA geography. Worth watching for this
  programme specifically: the site is written for South Asia and Africa, and
  the report will tell you whether it is reaching them.

---

## 4. Privacy

The site sets Google Analytics cookies. It collects no names, no email
addresses, no form data — it is a documentation site with no accounts and no
forms.

Whether that needs a cookie banner depends on where your readers are, and CGIAR
or IWMI may already have an institutional position on this. Worth checking with
whoever handles data protection before the site is promoted widely. If a banner
or an opt-out is required, say so and it can be added — the analytics include is
a single file and is already gated behind one config value.
