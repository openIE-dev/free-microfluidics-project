#!/usr/bin/env python3
"""cross_cuts.py — regenerate per-tag prior art cross-cut files.

Usage:
    python3 tools/cross_cuts.py

Reads `corpus.jsonl` and groups entries by each tag in their
`disclosed_subsystems`. For each tag, writes a markdown file at
`cross_cuts/<tag>.md` listing every disclosing entry in chronological
order with the fields that matter for prior art citation.

Also writes `cross_cuts/INDEX.md` summarizing all tags.

These files are the working prior art search tool. Each is a
defensive publication artifact in its own right — examiners and
invalidity-contention attorneys can search by subsystem and find
chronologically-ordered disclosures.
"""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
OUT_DIR = ROOT / "cross_cuts"


def load_corpus():
    return [json.loads(l) for l in CORPUS.read_text().splitlines() if l.strip()]


def date_key(e):
    return e.get("first_disclosure_date") or ""


def write_tag_file(tag, entries):
    entries_sorted = sorted(entries, key=date_key)
    earliest = entries_sorted[0].get("first_disclosure_date", "")
    lines = [
        "---",
        f"title: {tag}",
        "parent: Cross-cuts",
        "layout: default",
        "---",
        "",
        f"# Cross-cut: `{tag}`",
        "",
        f"**{len(entries_sorted)} corpus entries disclose this subsystem.**",
        "",
        f"Earliest disclosure: {earliest}",
        "",
        "Listed in chronological order. Each entry's `prior_art_notes` and",
        "`disclosure_citation` constitute the citeable prior art material.",
        "",
        "---",
        "",
    ]
    for e in entries_sorted:
        date = e.get("first_disclosure_date", "?")
        lines.append(f"## {e.get('canonical_name', '')} ({date})")
        lines.append("")
        lines.append(f"- **id**: `{e.get('id', '')}`")
        lines.append(f"- **corpus**: {e.get('corpus', '')}")
        if e.get("device_class"):
            lines.append(f"- **device class**: {e['device_class']}")
        if e.get("creator"):
            lines.append(f"- **creator**: {e['creator']}")
        if e.get("disclosure_citation"):
            lines.append(f"- **disclosure**: {e['disclosure_citation']}")
        if e.get("ip_status"):
            lines.append(f"- **ip status**: {e['ip_status']}")
        if e.get("prior_art_notes"):
            lines.append(f"- **prior art notes**: {e['prior_art_notes']}")
        lines.append("")
    (OUT_DIR / f"{tag}.md").write_text("\n".join(lines))


def write_index(by_tag):
    rows = []
    for tag in sorted(by_tag.keys()):
        entries = sorted(by_tag[tag], key=date_key)
        earliest = entries[0].get("first_disclosure_date", "?")
        rows.append((tag, len(entries), earliest))

    lines = [
        "---",
        "title: Cross-cuts",
        "has_children: true",
        "nav_order: 3",
        "permalink: /cross_cuts/",
        "---",
        "",
        "# Subsystem cross-cut index",
        "",
        "Each cross-cut file lists every corpus entry disclosing the tagged subsystem,",
        "in chronological order by first verified public disclosure date. Use these as",
        "the working prior art search tool when assessing patent claims in the area.",
        "",
        "| Tag | Entries | Earliest |",
        "|---|---|---|",
    ]
    for tag, count, earliest in rows:
        lines.append(f"| `{tag}` | {count} | {earliest} |")
    (OUT_DIR / "INDEX.md").write_text("\n".join(lines) + "\n")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for f in OUT_DIR.glob("*.md"):
        f.unlink()

    entries = load_corpus()
    by_tag = defaultdict(list)
    for e in entries:
        for tag in e.get("disclosed_subsystems") or []:
            by_tag[tag].append(e)

    for tag, group in by_tag.items():
        write_tag_file(tag, group)

    write_index(by_tag)
    print(f"  cross_cuts: {len(by_tag)} tags written")


if __name__ == "__main__":
    main()
