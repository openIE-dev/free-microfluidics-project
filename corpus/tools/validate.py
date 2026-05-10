#!/usr/bin/env python3
"""validate.py — schema and quality-bar validation for corpus.jsonl.

Usage:
    python3 tools/validate.py corpus.jsonl
    python3 tools/validate.py corpus.jsonl --strict   # gate releases

In default mode, validates structural correctness only:
    - each line is valid JSON
    - required fields present
    - ids unique
    - corpus is one of {private, open, fictional, academic}
    - schema_version is 2
    - lineage references are reported as warnings (not errors)

In --strict mode, additionally enforces the v0.2 quality bar for any
entry with draft != true:
    - prior_art_notes is non-empty
    - disclosure_citation is non-empty
    - first_disclosure_date is non-empty
    - sources is a non-empty list

Exits 0 if everything passes for the requested mode; nonzero otherwise.
"""
import json
import sys
from pathlib import Path

REQUIRED_FIELDS = (
    "id",
    "canonical_name",
    "corpus",
    "first_disclosure_date",
    "schema_version",
    "device_class",
    "creator",
    "ip_status",
    "sources",
)

VALID_CORPUS = {"private", "open", "fictional", "academic"}

VALID_DEVICE_CLASS = {
    "lab-on-chip",
    "point-of-care-cartridge",
    "organ-on-chip",
    "droplet-generator",
    "digital-microfluidics",
    "single-cell-platform",
    "nanofluidic-chip",
    "pump-component",
    "valve-component",
    "mixer-component",
    "separator-component",
    "flow-controller",
    "chip-holder",
    "printer-tooling",
    "consumable-bulk",
    "inkjet-printhead",
    "cooling-substrate",
    "dispenser-pipettor",
    "fictional-laboratory",
    "other",
}

VALID_IP_STATUS = {
    "patented",
    "open-permissive",
    "open-copyleft",
    "public-domain",
    "fictional",
    "trade-secret",
    "unknown",
}

QUALITY_BAR_FIELDS = (
    "prior_art_notes",
    "disclosure_citation",
    "first_disclosure_date",
)


def main():
    args = sys.argv[1:]
    strict = "--strict" in args
    args = [a for a in args if not a.startswith("--")]
    if not args:
        sys.exit("usage: validate.py corpus.jsonl [--strict]")
    path = Path(args[0])
    if not path.exists():
        sys.exit(f"ERROR: {path} not found")

    errors = []
    warnings = []
    entries = []
    seen_ids = set()

    for lineno, line in enumerate(path.read_text().splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError as e:
            errors.append(f"line {lineno}: invalid JSON ({e})")
            continue
        entries.append(entry)

        for f in REQUIRED_FIELDS:
            v = entry.get(f)
            if v in (None, "") or (isinstance(v, list) and not v):
                errors.append(
                    f"line {lineno} ({entry.get('id', '?')}): missing required field `{f}`"
                )

        if entry.get("corpus") not in VALID_CORPUS:
            errors.append(
                f"line {lineno} ({entry.get('id', '?')}): corpus must be one of {sorted(VALID_CORPUS)}"
            )

        dc = entry.get("device_class")
        if dc and dc not in VALID_DEVICE_CLASS:
            errors.append(
                f"line {lineno} ({entry.get('id', '?')}): device_class `{dc}` not in taxonomy"
            )

        ip = entry.get("ip_status")
        if ip and ip not in VALID_IP_STATUS:
            errors.append(
                f"line {lineno} ({entry.get('id', '?')}): ip_status `{ip}` not in taxonomy"
            )

        if entry.get("schema_version") != 2:
            errors.append(
                f"line {lineno} ({entry.get('id', '?')}): schema_version must be 2 (got {entry.get('schema_version')!r})"
            )

        eid = entry.get("id")
        if eid:
            if eid in seen_ids:
                errors.append(f"line {lineno}: duplicate id `{eid}`")
            seen_ids.add(eid)

    # Lineage reference checks (warnings only)
    for entry in entries:
        for field in ("lineage_ancestors", "lineage_descendants"):
            for ref in entry.get(field) or []:
                if ref not in seen_ids:
                    warnings.append(
                        f"{entry['id']}.{field} references unknown id `{ref}`"
                    )

    # Quality bar (strict mode only)
    quality_failures = []
    if strict:
        for entry in entries:
            if entry.get("draft"):
                continue
            for f in QUALITY_BAR_FIELDS:
                v = entry.get(f)
                if v in (None, ""):
                    quality_failures.append(
                        f"{entry['id']}: missing `{f}` (commons-grade entries must have it; flag draft: true if not yet ready)"
                    )
            srcs = entry.get("sources")
            if not isinstance(srcs, list) or not srcs:
                quality_failures.append(
                    f"{entry['id']}: `sources` must be a non-empty list for commons-grade entries"
                )

    n = len(entries)
    drafts = sum(1 for e in entries if e.get("draft"))
    commons = n - drafts

    print(f"  Entries:       {n}")
    print(f"  Commons-grade: {commons}")
    print(f"  Drafts:        {drafts}")
    print(f"  Unique ids:    {len(seen_ids)}")
    print(f"  Errors:        {len(errors)}")
    print(f"  Warnings:      {len(warnings)}")
    if strict:
        print(f"  Quality fails: {len(quality_failures)}")

    for w in warnings:
        print(f"  WARN: {w}")
    for e in errors:
        print(f"  ERROR: {e}")
    if strict:
        for qf in quality_failures:
            print(f"  QUALITY: {qf}")

    if errors:
        sys.exit(1)
    if strict and quality_failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
