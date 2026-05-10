#!/usr/bin/env python3
"""index.py — regenerate CORPUS_INDEX.md, lineage.json, and per-corpus mirrors.

Usage:
    python3 tools/index.py .

Reads `corpus.jsonl` from the given root directory and writes:
    - CORPUS_INDEX.md           (sorted markdown table of every entry)
    - lineage.json       (DAG with nodes, warnings, cycles)
    - private.jsonl
    - open.jsonl
    - fictional.jsonl
    - academic.jsonl

These are derived artifacts. Re-run after every edit to corpus.jsonl.
"""
import json
import sys
from pathlib import Path


def load_corpus(path):
    return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]


def write_per_corpus_mirrors(root, entries):
    by_corpus = {"private": [], "open": [], "fictional": [], "academic": []}
    for e in entries:
        c = e.get("corpus")
        if c in by_corpus:
            by_corpus[c].append(e)
    for c, es in by_corpus.items():
        es_sorted = sorted(es, key=lambda e: e.get("first_disclosure_date", ""))
        with (root / f"{c}.jsonl").open("w") as f:
            for e in es_sorted:
                f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
    return {c: len(es) for c, es in by_corpus.items()}


def write_index_md(root, entries):
    sorted_entries = sorted(entries, key=lambda e: e.get("canonical_name", "").lower())
    lines = [
        "# Corpus Index",
        "",
        f"{len(entries)} entries total. Generated from corpus.jsonl.",
        "",
        "| Name | id | Year | Corpus | IP | Draft |",
        "|---|---|---|---|---|---|",
    ]
    for e in sorted_entries:
        year = (e.get("first_disclosure_date") or "")[:4]
        draft = "✓" if e.get("draft") else ""
        lines.append(
            f"| {e.get('canonical_name', '')} "
            f"| `{e.get('id', '')}` "
            f"| {year} "
            f"| {e.get('corpus', '')} "
            f"| {e.get('ip_status', '')} "
            f"| {draft} |"
        )
    (root / "CORPUS_INDEX.md").write_text("\n".join(lines) + "\n")


def build_lineage(entries):
    by_id = {e["id"]: e for e in entries}
    nodes = []
    warnings = []

    # Collect declared edges (ancestors + descendants), unify, drop dangling refs.
    descendants_of = {eid: set() for eid in by_id}
    ancestors_of = {eid: set() for eid in by_id}

    for e in entries:
        eid = e["id"]
        for anc in e.get("lineage_ancestors") or []:
            if anc in by_id:
                ancestors_of[eid].add(anc)
                descendants_of[anc].add(eid)
            else:
                warnings.append(f"{eid}.lineage_ancestors references unknown id `{anc}`")
        for des in e.get("lineage_descendants") or []:
            if des in by_id:
                descendants_of[eid].add(des)
                ancestors_of[des].add(eid)
            else:
                warnings.append(f"{eid}.lineage_descendants references unknown id `{des}`")

    sorted_ids = sorted(by_id.keys(), key=lambda i: (by_id[i].get("first_disclosure_date", ""), i))
    for eid in sorted_ids:
        e = by_id[eid]
        nodes.append({
            "id": eid,
            "name": e.get("canonical_name", ""),
            "year": (e.get("first_disclosure_date") or "")[:4],
            "corpus": e.get("corpus", ""),
            "ancestors": sorted(ancestors_of[eid]),
            "descendants": sorted(descendants_of[eid]),
        })

    # DFS cycle detection.
    cycles = []
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {eid: WHITE for eid in by_id}
    parent = {}

    def dfs(start):
        stack = [(start, iter(sorted(descendants_of[start])))]
        path = [start]
        color[start] = GRAY
        while stack:
            node, it = stack[-1]
            try:
                nxt = next(it)
            except StopIteration:
                color[node] = BLACK
                stack.pop()
                path.pop()
                continue
            if color[nxt] == GRAY:
                # Cycle: from nxt to current via path.
                if nxt in path:
                    cycles.append(path[path.index(nxt):] + [nxt])
            elif color[nxt] == WHITE:
                color[nxt] = GRAY
                stack.append((nxt, iter(sorted(descendants_of[nxt]))))
                path.append(nxt)

    for eid in sorted_ids:
        if color[eid] == WHITE:
            dfs(eid)

    return {"nodes": nodes, "warnings": warnings, "cycles": cycles}


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: index.py <root>")
    root = Path(sys.argv[1])
    corpus_path = root / "corpus.jsonl"
    entries = load_corpus(corpus_path)
    n = len(entries)

    counts = write_per_corpus_mirrors(root, entries)
    write_index_md(root, entries)
    lineage = build_lineage(entries)
    (root / "lineage.json").write_text(
        json.dumps(lineage, indent=2, ensure_ascii=False) + "\n"
    )

    print(f"  CORPUS_INDEX.md:     {n} entries")
    print(f"  per-corpus:   private={counts['private']} open={counts['open']} "
          f"fictional={counts['fictional']} academic={counts['academic']}")
    print(f"  lineage:      {len(lineage['nodes'])} nodes, "
          f"{len(lineage['warnings'])} warnings, {len(lineage['cycles'])} cycles")
    for w in lineage["warnings"]:
        print(f"  WARN: {w}")
    for c in lineage["cycles"]:
        print(f"  CYCLE: {' -> '.join(c)}")


if __name__ == "__main__":
    main()
