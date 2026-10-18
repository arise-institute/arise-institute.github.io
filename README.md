# ARISE-Institute Website

Website for **ARISE-Institute: Artificial Intelligence for Resilient, Informed, and Sustainable Agriculture**, a research hub at South Dakota State University led by Dr. Sunish K. Sehgal.

## Where this lives

| Copy | URL | Notes |
|---|---|---|
| **GitHub Pages (live, public)** | https://arise-institute.github.io | Deployed from this repo's `main` branch, root folder. This is the canonical public site. |
| **Claude Artifact** | https://claude.ai/artifact/8kQ3kgr6dMfbGt3TNg5p29 | A separate hosted copy. Private by default; same content, but videos point to Claude's own asset store instead of local files (see "Two video sources" below). |
| **Local dev copy** | `http://localhost:8080` when served from this folder | For previewing changes before pushing. |

## Structure

```
arise-site/
├── index.html              ← the entire site (single file, hash-routed SPA)
├── videos/
│   ├── eot_720p.mp4         Early Observation Trial drone footage (Gallery page)
│   └── tankees_720p.mp4     Trial grounds aerial footage (Gallery page)
└── _source/                 ← NOT part of the live site; raw material for future edits
    ├── photos/               Original team/collaborator headshots, logos, flyers, etc.
    │                         before they were resized/compressed and embedded as
    │                         base64 data URIs into index.html
    ├── videos-original/      (empty placeholder — originals were 100MB–715MB local
    │                         files and an X/Twitter-hosted video; not stored here,
    │                         see "Rebuilding video assets" below)
    ├── arise-institute-artifact.html   The Claude-Artifact-specific variant of
    │                         index.html (video <source> tags point to Claude's
    │                         asset-store URLs: /_blob/<id>, instead of videos/*.mp4)
    └── scripts/
```

## How the site is built

`index.html` is a **single self-contained HTML file** — a hash-routed single-page app (`#team`, `#grants`, `#publications`, `#tools`, `#training`, `#outreach`, `#gallery`). Every photo and the two canvas-drawn icons (drone/sensor/camera/scope) are embedded as base64 `data:` URIs directly in the HTML, except the two Gallery videos, which are real files in `videos/` referenced by relative path.

There is no build step — it's edited directly as HTML/CSS/vanilla JS.

## Two video sources — important when editing

Because the Claude Artifact platform can't reference external file paths or arbitrary external video URLs (its CSP blocks them), **two versions of index.html exist**:

1. **`index.html`** (this repo, what GitHub Pages and local serve) — videos load via `<source src="videos/eot_720p.mp4">` (relative path to the files in `videos/`).
2. **`_source/arise-institute-artifact.html`** — identical except the two video `<source src>` values are swapped to `/_blob/4e90bc26a45fcc1f8e07fbca4125058d` and `/_blob/88bbdfa3f1d5d2c068e865af80f1c1d9` (Claude's own asset-store URLs, uploaded once via the Artifact tool's asset upload).

**Whenever you edit `index.html` and want the Claude Artifact copy to match**, you need to re-apply that same swap before publishing to the Artifact — don't just publish `index.html` directly to the Artifact, its videos will 404 there. The swap is two find-and-replace operations:
```
videos/eot_720p.mp4      →  /_blob/4e90bc26a45fcc1f8e07fbca4125058d
videos/tankees_720p.mp4  →  /_blob/88bbdfa3f1d5d2c068e865af80f1c1d9
```

## Rebuilding video assets (if ever needed)

The two Gallery videos were compressed from:
- **EOT video**: pulled from the live tweet at `x.com/WheatInnovation/status/2073237909713367123` (the account's own already-compressed 1280×720 MP4 variant, ~6MB) — the original local file (`EOTtrim.mp4`, 715MB/4K) was too large for any of these platforms.
- **Tankees aerial footage**: compressed locally from `tankees-2.mov` (100MB/1080p) down to 720p/~18MB via `ffmpeg -vf scale=1280:-2 -c:v libx264 -crf 26`.

## Making future edits

1. Edit `index.html` directly (it's plain HTML/CSS/JS — search for the relevant section's text or `id=`).
2. Preview locally: `cd` into this folder and run `python3 -m http.server 8080`, then open `http://localhost:8080`.
3. Commit and push:
   ```bash
   git add index.html
   git commit -m "describe the change"
   git push
   ```
   GitHub Pages rebuilds automatically within a minute or two.
4. If the change should also appear on the Claude Artifact copy, apply the video-URL swap above, then publish that variant to the Artifact URL.

## Content inventory (as of this snapshot)

- **Home** — mission/vision, 3 research aims, 7-stage "sensor-to-selection" framework with a TPOC/CPOC/Development/Life-Cycle-Management commercialization loop, two-equations section (Breeder's Equation + Liebig's Law of the Minimum), Why-Now, Contact.
- **Team** — 3 core PIs (Sehgal, Maimaitijiang, Sher) with real SDSU directory photos, 6 internal SDSU collaborators (alphabetized), 4 external collaborator network members (alphabetized, linked to their institutional directory pages).
- **Grants** — 6 funded grants ($1,064,551 total) with award numbers where provided, 2 targeted-for-application grants, 12-month roadmap, external partnerships, sustainability plan.
- **Publications** — 4 real 2026 papers with figures pulled from the actual manuscripts, abstracts paraphrased, linked to their DOIs.
- **Tools** — WheatAI (live), 2 live prototype tools (Wheat-TDM, AI-CDM), SD Winter Wheat Dashboard (upcoming), 2 planned tools.
- **Training** — current students (AHPS + Geospatial Science, with photos), Alumni (Hillson Ghimire → Rice University, Swas Kaushal → Syngenta), Summer 2026 interns.
- **Outreach** — X/@wheatinnovation link, Field Days (real photo), Stakeholder Meetings (real flyer), Workshops (upcoming).
- **Gallery** — 2 real drone videos of the trial grounds.

## Attribution

Site built with Claude Code, in conversation with Dr. Sunish Sehgal. All content — photos, videos, grant data, publications, team information — is the real material of the ARISE-Institute team, pulled from official SDSU directory pages, Google Scholar profiles, X/Twitter, and the team's own grant/publication records, each verified before use.
