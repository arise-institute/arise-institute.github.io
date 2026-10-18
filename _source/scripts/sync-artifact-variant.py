#!/usr/bin/env python3
"""
Regenerates the Claude-Artifact-specific variant of index.html.

The live site (index.html, served by GitHub Pages / local dev server) references
the two Gallery videos by relative path: videos/eot_720p.mp4 and
videos/tankees_720p.mp4. The Claude Artifact platform can't load relative file
paths or arbitrary external URLs (its CSP blocks them), so it needs those two
<source src="..."> values swapped to Claude's own asset-store URLs instead.

Run this after editing index.html, any time you also want to republish the
Claude Artifact copy:

    cd arise-site
    python3 _source/scripts/sync-artifact-variant.py

Then publish the resulting _source/arise-institute-artifact.html to the
Artifact (via the Artifact tool's publish action, passing that file and the
existing artifact's url). The two asset IDs below are permanent — they were
uploaded once and don't change unless the videos themselves are replaced.
"""

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
SRC = ROOT / "index.html"
OUT = ROOT / "_source" / "arise-institute-artifact.html"

REPLACEMENTS = {
    'src="videos/eot_720p.mp4"': 'src="/_blob/4e90bc26a45fcc1f8e07fbca4125058d"',
    'src="videos/tankees_720p.mp4"': 'src="/_blob/88bbdfa3f1d5d2c068e865af80f1c1d9"',
}

def main():
    content = SRC.read_text(encoding="utf-8")
    for old, new in REPLACEMENTS.items():
        if old not in content:
            print(f"WARNING: did not find {old!r} in index.html — video src may have changed")
        content = content.replace(old, new)
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT} ({len(content)} chars)")

if __name__ == "__main__":
    main()
