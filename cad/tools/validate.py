#!/usr/bin/env python3
"""validate.py — schema and quality-bar validation for designs.jsonl.

Usage:
    python3 tools/validate.py designs.jsonl
    python3 tools/validate.py designs.jsonl --strict   # gate releases

Default mode validates structural correctness; --strict mode additionally
enforces the quality bar for non-draft entries.

Exits 0 if everything passes for the requested mode; nonzero otherwise.
"""
import json
import sys
from pathlib import Path

REQUIRED_FIELDS = (
    "id",
    "canonical_name",
    "designer",
    "license",
    "device_class",
    "fabrication_path",
    "channel_geometry",
    "cad_files",
    "sources",
    "schema_version",
)

VALID_LICENSE = {
    "CC0-1.0",
    "CERN-OHL-P",
    "MIT",
    "BSD-3-Clause",
    "Apache-2.0",
    "other-permissive",
    "encumbered-do-not-use",
}

# Same taxonomy as the corpus, kept independent so each repo can evolve
# its own list without coupling.
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

QUALITY_BAR_FIELDS = (
    "fabrication_path",
    "channel_geometry",
    "cad_files",
)


def main():
    args = sys.argv[1:]
    strict = "--strict" in args
    args = [a for a in args if not a.startswith("--")]
    if not args:
        sys.exit("usage: validate.py designs.jsonl [--strict]")
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

        if entry.get("license") and entry.get("license") not in VALID_LICENSE:
            warnings.append(
                f"line {lineno} ({entry.get('id', '?')}): license `{entry['license']}` not in known set"
            )

        dc = entry.get("device_class")
        if dc and dc not in VALID_DEVICE_CLASS:
            errors.append(
                f"line {lineno} ({entry.get('id', '?')}): device_class `{dc}` not in taxonomy"
            )

        if entry.get("schema_version") != 1:
            errors.append(
                f"line {lineno} ({entry.get('id', '?')}): schema_version must be 1 (got {entry.get('schema_version')!r})"
            )

        eid = entry.get("id")
        if eid:
            if eid in seen_ids:
                errors.append(f"line {lineno}: duplicate id `{eid}`")
            seen_ids.add(eid)

    quality_failures = []
    if strict:
        for entry in entries:
            if entry.get("draft"):
                continue
            for f in QUALITY_BAR_FIELDS:
                v = entry.get(f)
                if v in (None, "") or (isinstance(v, list) and not v):
                    quality_failures.append(
                        f"{entry['id']}: missing `{f}` (commons-grade entries must have it; flag draft: true if not yet ready)"
                    )

    n = len(entries)
    drafts = sum(1 for e in entries if e.get("draft"))
    commons = n - drafts

    print(f"  Designs:       {n}")
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
