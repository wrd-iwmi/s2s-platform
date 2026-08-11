# Putting this site on GitHub Pages

Written for this specific deployment:

| | |
| --- | --- |
| **Organisation** | `wrd-iwmi` |
| **Repository** | `s2s-platform` |
| **Site address** | `https://wrd-iwmi.github.io/s2s-platform/` |
| **`baseurl`** | `"/s2s-platform"` |
| **`url`** | `"https://wrd-iwmi.github.io"` |

Those last two are already set in `_config.yml`. If the repository ends up with
a different name, [section 6](#6-if-the-repository-name-changes) tells you the
one line to change.

About fifteen minutes, no command line needed.

---

## Contents

1. [Create the repository](#1-create-the-repository)
2. [Upload the site](#2-upload-the-site)
3. [Switch Pages on](#3-switch-pages-on)
4. [Check it worked](#4-check-it-worked)
5. [Give colleagues access](#5-give-colleagues-access)
6. [If the repository name changes](#6-if-the-repository-name-changes)
7. [Using your own domain name](#7-using-your-own-domain-name)
8. [Protecting the site from accidents](#8-protecting-the-site-from-accidents)
9. [Troubleshooting](#9-troubleshooting)

---

## 1. Create the repository

1. Go to <https://github.com/new>.
2. Set **Owner** to **`wrd-iwmi`**.
3. **Repository name:** `s2s-platform`
4. **Public.** (Pages on a private repository needs a paid plan.)
5. Leave "Add a README" unticked — this folder already has one.
6. **Create repository**.

> **A note on the naming, because it trips everyone up.**
> A repository called `s2s_iwmi.github.io` does *not* produce a site at
> `https://s2s_iwmi.github.io/`. GitHub only treats a repository as an
> organisation site when it is named after the organisation exactly — here that
> would be `wrd-iwmi.github.io`. Any other name is a *project site*, and the
> repository name simply becomes part of the path. So
> `s2s_iwmi.github.io` would have published at
> `https://wrd-iwmi.github.io/s2s_iwmi.github.io/`, with `.github.io` in it
> twice. `s2s-platform` avoids that.

---

## 2. Upload the site

On the empty repository page, click **uploading an existing file**.

Drag in **the contents of the `version-2` folder** — not the folder itself. You
should be dragging `_config.yml`, `index.html`, `about.md`, the `_tools` folder,
and so on. When you are done, `_config.yml` must be visible at the top level of
the repository.

> **Watch out for two things:**
>
> - Folders beginning with an underscore (`_tools`, `_layouts`, `_data`,
>   `_includes`, `_scripts`, `_templates`) are essential. If your file manager
>   hides them, switch on "show hidden files" first.
> - `HANDOVER.md` lives *outside* `version-2/` and should not be uploaded. It is
>   internal notes.

Scroll down, type a message such as *"Initial site"*, and click **Commit
changes**.

If dragging that many files is awkward, use **GitHub Desktop**
(<https://desktop.github.com>): clone the empty repository, copy the contents of
`version-2` into the folder it creates, then **Commit** and **Push**.

---

## 3. Switch Pages on

1. In the repository, click **Settings** (top right).
2. In the left sidebar, click **Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. **Branch:** `main`. **Folder:** `/ (root)`. Click **Save**.

Wait a minute or two, then refresh that screen. It will say:

> Your site is live at `https://wrd-iwmi.github.io/s2s-platform/`

That is the whole deployment. Every push to `main` republishes, in about a
minute. There is no Action to configure and no build step to maintain.

**Do not add a `.nojekyll` file** — it switches off the build that turns the
markdown into web pages.

---

## 4. Check it worked

Open <https://wrd-iwmi.github.io/s2s-platform/> and confirm:

- [ ] The homepage has the dark blue banner and styled cards — **not** a wall of
      plain text. Plain text means `baseurl` is wrong; see
      [section 9](#9-troubleshooting).
- [ ] The menu works and the Tools page lists six tools.
- [ ] A tool page opens with its sidebar and diagrams.
- [ ] Scroll the homepage to "Where the work is happening" — the map loads with
      six markers.
- [ ] Open a notebook tutorial (Learn → *Reading a downscaled S2S forecast in
      Python*) and check the plot appears and the **Run in Colab** button works.
- [ ] Open the site on your phone. The menu should collapse to a **Menu** button.
- [ ] Visit `https://wrd-iwmi.github.io/s2s-platform/sitemap.xml` — it should
      list every page.

Then make a test edit: open any file in `_tools`, change a word, commit, wait a
minute, refresh. If that works, the researchers' workflow works.

---

## 5. Give colleagues access

Settings → **Collaborators and teams** → **Add people**.

| Role | Can do |
| --- | --- |
| **Write** | Edit and add pages directly. Right for the researchers maintaining content. |
| **Triage** | Comment and manage issues, but not change files. |
| **Admin** | Everything, including deleting the repository. Keep to one or two people. |

Everyone with Write access can edit content in the browser exactly as described
in `EDITING-GUIDE.md`. Send them that file, not this one.

---

## 6. If the repository name changes

Renaming on GitHub is instant, keeps all history, and redirects the old URL.
Settings → **General** → **Repository name** → Rename.

Afterwards, change **two lines** in `_config.yml` (and `colab_repo`, if you use
the notebook buttons):

| New address | `baseurl` | `url` |
| --- | --- | --- |
| `https://wrd-iwmi.github.io/s2s-platform/` | `"/s2s-platform"` | `"https://wrd-iwmi.github.io"` |
| `https://wrd-iwmi.github.io/anything-else/` | `"/anything-else"` | `"https://wrd-iwmi.github.io"` |
| `https://wrd-iwmi.github.io/` (repo named `wrd-iwmi.github.io`) | `""` | `"https://wrd-iwmi.github.io"` |
| `https://s2s.iwmi.org/` (custom domain) | `""` | `"https://s2s.iwmi.org"` |

**Leading slash, no trailing slash.** `"/s2s-platform"` is right;
`"s2s-platform"` and `"/s2s-platform/"` are not.

```yaml
colab_repo: "wrd-iwmi/s2s-platform"    # OWNER/REPO — powers the Colab buttons
colab_branch: "main"
```

---

## 7. Using your own domain name

Optional, and it can be done later.

1. In your DNS provider, add a `CNAME` record pointing your subdomain — for
   example `s2s` — at `wrd-iwmi.github.io`.
2. Repository → Settings → Pages → **Custom domain**, type the full domain
   (`s2s.iwmi.org`), click **Save**.
3. Wait for the DNS check to go green, then tick **Enforce HTTPS**.
4. Update `_config.yml`:

   ```yaml
   baseurl: ""
   url: "https://s2s.iwmi.org"
   ```

   A custom domain always serves from the root, so `baseurl` becomes empty even
   though you started as a project site.

GitHub adds a file named `CNAME` to the repository when you do this. Leave it
alone.

---

## 8. Protecting the site from accidents

Optional, but worth ten minutes once several people are editing.

**Require review before publishing.** Settings → **Branches** → *Add branch
protection rule* → Branch name pattern `main` → tick **Require a pull request
before merging**.

Contributors then get a *Propose changes* button instead of a direct commit, and
somebody reviews before it goes live. It adds a step, so decide whether the team
would rather move quickly and fix mistakes afterwards — every change is
reversible either way.

**Undoing a mistake.** Open the repository's **Commits** list, find the change,
click it, and use **Revert**. Nothing is ever permanently lost.

---

## 9. Troubleshooting

**"Your site is live" but I get a 404.**
Give it five minutes on the very first publish. If it persists, check Settings →
Pages shows branch `main` and folder `/ (root)`, and that `index.html` sits at
the top level of the repository — not inside a `version-2` folder. If it is, you
uploaded the folder instead of its contents: move the files up one level.

**The page loads but has no styling, and links 404.**
`baseurl` does not match the address. It should be `"/s2s-platform"` for
`https://wrd-iwmi.github.io/s2s-platform/`. See
[section 6](#6-if-the-repository-name-changes).

**My change has not appeared.**
Wait two minutes. Then open the **Actions** tab — a green tick means published, a
red cross means the build failed. Click the red cross to read the error; it is
almost always a formatting slip in a page's settings block. See the
troubleshooting section of `EDITING-GUIDE.md`.

**The build fails with "could not find a theme".**
Something added a `theme:` or `remote_theme:` line to `_config.yml`. This site
has its own layouts and needs no theme. Remove the line.

**Everything broke after someone added a `.nojekyll` file.**
Delete it. It switches off the Jekyll build entirely.

**The map does not appear.**
It loads only when scrolled into view, and needs access to `unpkg.com` and
`tile.openstreetmap.org`. On a network that blocks those, the country list beside
the map still shows everything — that is by design. To drop the interactive map
altogether, set `interactive: false` in `_data/geography.yml` and the lightweight
schematic drawing comes back.

**The Colab button 404s.**
`colab_repo` must be `OWNER/REPO` (`wrd-iwmi/s2s-platform`) and the branch in
`colab_branch` must exist. The notebook also has to be committed — Colab reads it
from GitHub, not from the site.

**I need to move the site somewhere else.**
Change `baseurl` and `url`. That is the whole migration — this is plain HTML with
no server behind it, so it runs from any static host, or from a folder on a
laptop.
