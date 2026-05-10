#!/usr/bin/env python3
"""validate.py — schema and quality-bar validation for instruments.jsonl.

Usage:
    python3 tools/validate.py instruments.jsonl
    python3 tools/validate.py instruments.jsonl --strict   # gate releases

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
    "instrument_class",
    "purpose",
    "hardware_artifacts",
    "bill_of_materials",
    "sources",
    "schema_version",
)

VALID_INSTRUMENT_CLASS = {
    "pressure-controller",
    "syringe-pump",
    "peristaltic-pump-driver",
    "ewod-driver",
    "thermal-cycler",
    "microfluidic-thermostat",
    "optical-readout-board",
    "impedance-readout-board",
    "acoustic-driver",
    "acoustic-electric-driver",
    "flow-rate-sensor",
    "bubble-detector",
    "chip-holder",
    "valve-bank-controller",
    "multi-channel-controller",
    "other",
}

QUALITY_BAR_FIELDS = (
    "hardware_artifacts",
    "bill_of_materials",
    "purpose",
)


def main():
    args = sys.argv[1:]
    strict = "--strict" in args
    args = [a for a in args if not a.startswith("--")]
    if not args:
        sys.exit("usage: validate.py instruments.jsonl [--strict]")
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

        ic = entry.get("instrument_class")
        if ic and ic not in VALID_INSTRUMENT_CLASS:
            errors.append(
                f"line {lineno} ({entry.get('id', '?')}): instrument_class `{ic}` not in taxonomy"
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

    print(f"  Instruments:   {n}")
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
