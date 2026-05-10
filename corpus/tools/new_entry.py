#!/usr/bin/env python3
"""new_entry.py — interactive scaffolder for new corpus entries.

Walks a contributor through the schema fields, applies sensible defaults,
validates as it goes, and writes the new entry to a fresh JSONL file
ready to be reviewed and appended to corpus.jsonl via a PR.

Usage:
    python3 tools/new_entry.py             # interactive
    python3 tools/new_entry.py --append    # append to corpus.jsonl directly
                                           # (validate.py + index.py + cross_cuts.py
                                           # still need to run after)

The output is intentionally a separate file (entry-<id>.jsonl) by default,
so you can edit it before merging into the corpus. Run validate.py against
the merged corpus before sending the PR.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

CORPUS_OPTIONS = ["private", "open", "fictional", "academic"]
IP_STATUS_OPTIONS = [
    "patented",
    "trade-secret",
    "open-permissive",
    "open-copyleft",
    "public-domain",
    "fictional",
    "unknown",
]
DEVICE_CLASS_OPTIONS = [
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
]
SUBSTRATE_OPTIONS = [
    "PDMS", "glass", "silicon", "thermoplastic", "paper", "hybrid", "other",
]
FABRICATION_OPTIONS = [
    "soft-lithography",
    "photolithography",
    "dlp-sla",
    "hot-embossing",
    "injection-molding",
    "laser-ablation",
    "xurography",
    "2pp",
    "other",
]
FLOW_REGIME_OPTIONS = [
    "pressure-driven",
    "electrokinetic",
    "acoustic",
    "capillary",
    "centrifugal",
    "digital-droplet",
    "passive",
    "mixed",
]
POWER_OPTIONS = [
    "external-pump",
    "piezo",
    "thermal",
    "passive",
    "battery",
    "tethered",
    "fictional",
    "unknown",
]


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    return s.strip("-")


def existing_ids() -> set:
    p = ROOT / "corpus.jsonl"
    if not p.exists():
        return set()
    return {json.loads(l)["id"] for l in p.read_text().splitlines() if l.strip()}


def known_tags() -> list:
    """Return tags currently in use, sorted by frequency desc."""
    p = ROOT / "corpus.jsonl"
    if not p.exists():
        return []
    counts = {}
    for line in p.read_text().splitlines():
        if not line.strip():
            continue
        e = json.loads(line)
        for t in e.get("disclosed_subsystems") or []:
            counts[t] = counts.get(t, 0) + 1
    return [t for t, _ in sorted(counts.items(), key=lambda x: (-x[1], x[0]))]


def ask(prompt, default=None, required=False, options=None, multi=False, hint=None):
    label = prompt
    if options:
        label += f"\n  options: {', '.join(options)}"
    if hint:
        label += f"\n  ({hint})"
    if default is not None:
        label += f"\n  [default: {default}] "
    else:
        label += "\n> "
    while True:
        try:
            v = input(label).strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.", file=sys.stderr)
            sys.exit(1)
        if not v and default is not None:
            v = default
        if not v:
            if required:
                print("  required.")
                continue
            return None
        if multi:
            return [x.strip() for x in v.split(",") if x.strip()]
        return v


def ask_yes_no(prompt, default=False):
    suffix = " [Y/n] " if default else " [y/N] "
    while True:
        try:
            v = input(prompt + suffix).strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.", file=sys.stderr)
            sys.exit(1)
        if not v:
            return default
        if v in ("y", "yes"):
            return True
        if v in ("n", "no"):
            return False


def ask_float(prompt, default=None):
    v = ask(prompt, default=default)
    if v is None:
        return None
    try:
        return float(v)
    except ValueError:
        print("  not a number; leaving null.")
        return None


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--append", action="store_true",
                   help="append directly to corpus.jsonl after preview")
    p.add_argument("--draft", action="store_true",
                   help="mark draft: true (default if quality bar not yet met)")
    args = p.parse_args()

    print("=" * 60)
    print("  Free Microfluidics Corpus — new entry scaffolder")
    print("=" * 60)
    print()
    print("Walks the v0.2 schema field by field. Press enter to leave")
    print("a non-required field blank. The output is a single JSON line")
    print("ready to merge into corpus.jsonl after review.")
    print()
    print("Quality bar reminder: an entry is commons-grade when")
    print("  - disclosure_citation resolves to a primary source")
    print("  - first_disclosure_date is the earliest defensible date")
    print("  - prior_art_notes is element-by-element 102/103 analysis")
    print("  - sources is non-empty and primary")
    print("Anything below this bar should be flagged draft: true.")
    print()
    input("Press enter to begin… ")
    print()

    entry = {"schema_version": 2}

    # ---- core identity ----
    entry["canonical_name"] = ask(
        "Canonical name", required=True,
        hint="e.g. 'BioFire FilmArray', 'Quake monolithic membrane valve', 'AESOP chip'"
    )

    suggested_id = slugify(entry["canonical_name"])
    seen = existing_ids()
    while True:
        eid = ask("ID (slug, lowercase-with-hyphens)", default=suggested_id, required=True)
        if eid in seen:
            print(f"  '{eid}' already exists — pick another.")
            suggested_id = eid + "-2"
            continue
        if not re.match(r"^[a-z0-9][a-z0-9\-]*[a-z0-9]$", eid):
            print("  ids must be lowercase, alphanumeric + hyphens, no leading/trailing hyphen.")
            continue
        entry["id"] = eid
        break

    aliases = ask("Aliases (comma-separated)", multi=True, hint="other names this is known by")
    if aliases:
        entry["aliases"] = aliases

    entry["corpus"] = ask("Corpus", required=True, options=CORPUS_OPTIONS)
    while entry["corpus"] not in CORPUS_OPTIONS:
        entry["corpus"] = ask(f"Must be one of {CORPUS_OPTIONS}", required=True)

    # ---- disclosure ----
    print()
    print("--- Disclosure ---")
    entry["first_disclosure_date"] = ask(
        "First disclosure date (YYYY, YYYY-MM, or YYYY-MM-DD)", required=True,
        hint="earliest verifiable public disclosure"
    )
    entry["disclosure_citation"] = ask(
        "Disclosure citation", required=True,
        hint="primary source: paper DOI, patent #, datasheet URL, FDA 510(k), product manual"
    )
    entry["creator"] = ask("Creator (person/org/lab/company)", required=True)
    entry["creator_country"] = ask("Creator country (ISO-alpha-2 like US, JP, KR)", hint="optional")

    # ---- device characteristics ----
    print()
    print("--- Device characteristics ---")
    entry["device_class"] = ask("Device class", options=DEVICE_CLASS_OPTIONS, required=True,
                                default="lab-on-chip")
    while entry["device_class"] not in DEVICE_CLASS_OPTIONS:
        entry["device_class"] = ask(f"Must be one of the listed options", required=True)

    entry["substrate_material"] = ask("Substrate material", options=SUBSTRATE_OPTIONS,
                                      hint="leave blank if multi or N/A")
    entry["fabrication_method"] = ask("Fabrication method", options=FABRICATION_OPTIONS)
    entry["channel_geometry"] = ask("Channel geometry",
        hint="e.g. '50 µm wide × 30 µm deep PDMS, 12-channel array'")
    entry["flow_regime"] = ask("Flow regime", options=FLOW_REGIME_OPTIONS, default="pressure-driven")
    entry["chip_footprint_mm"] = ask_float("Chip footprint (mm, characteristic dimension)")
    entry["sample_volume"] = ask("Sample / working volume",
        hint="e.g. '600 aL', '5 µL', '17 nL', leave blank if N/A")
    entry["throughput"] = ask("Throughput",
        hint="e.g. '1000 droplets/s', '200 cells/min', leave blank if N/A")
    entry["power_source"] = ask("Power source", options=POWER_OPTIONS, default="external-pump")

    # ---- application / control / sensing ----
    print()
    print("--- Application / control / sensing ---")
    entry["end_application"] = ask("End application",
        hint="diagnostic | research | bioprocess | drug-delivery | thermal-mgmt | analytical | other")
    entry["control_architecture"] = ask("Control architecture",
        hint="manual | scripted | feedback-controlled | computer-vision-loop | open-loop")
    entry["sensing"] = ask("Sensing summary",
        hint="optical, electrochemical, impedance, acoustic, mass-spec coupled, etc.")
    entry["notable_capabilities"] = ask("Notable capabilities (comma-separated)", multi=True)

    # ---- IP ----
    print()
    print("--- Intellectual property ---")
    entry["ip_status"] = ask("IP status", options=IP_STATUS_OPTIONS, required=True, default="open-permissive")
    while entry["ip_status"] not in IP_STATUS_OPTIONS:
        entry["ip_status"] = ask(f"Must be one of {IP_STATUS_OPTIONS}", required=True)
    if entry["ip_status"] == "patented":
        entry["ip_citations"] = ask("Patent numbers / IDs (comma-separated)", multi=True,
                                    hint="e.g. US7059348B2, EP1547688A1, FDA 510(k) K123456")

    # ---- subsystems / cross-cuts ----
    print()
    print("--- Disclosed subsystems (cross-cut tags) ---")
    print("These determine which prior-art cross-cut chains this entry joins.")
    tags = known_tags()
    if tags:
        print("Top tags currently in use:")
        for t in tags[:15]:
            print(f"  {t}")
        print("…etc. See SCHEMA.md and cross_cuts/INDEX.md for the full taxonomy.")
    else:
        print("Tag list not yet populated. See SCHEMA.md for the full taxonomy.")
    entry["disclosed_subsystems"] = ask("Tags (comma-separated)", multi=True)

    cpc = ask("CPC classifications (comma-separated)", multi=True,
              hint="e.g. B01L 3/00, G01N 27/447, B01F 33/30 — leave empty if uncertain")
    entry["cpc_classifications"] = cpc or []

    # ---- prior art notes ----
    print()
    print("--- Prior art notes ---")
    print("This is the heart of the entry. Element-by-element 102/103")
    print("anticipation analysis. Identifies what claims this disclosure")
    print("could anticipate. Be specific — examiners will read this and")
    print("decide whether to cite it.")
    entry["prior_art_notes"] = ask("Prior art notes",
        hint="multi-sentence; what this disclosure anticipates")

    # ---- lineage ----
    print()
    print("--- Lineage (optional) ---")
    anc = ask("Lineage ancestors (comma-separated entry ids)", multi=True,
              hint="entries this descends from / builds upon")
    des = ask("Lineage descendants (comma-separated entry ids)", multi=True,
              hint="entries that explicitly descend from this one")
    if anc:
        entry["lineage_ancestors"] = anc
    if des:
        entry["lineage_descendants"] = des

    # ---- sources ----
    print()
    print("--- Sources ---")
    sources = ask("Source citations (comma-separated)", multi=True, required=True,
                  hint="primary references; DOIs, patent numbers, datasheet URLs")
    entry["sources"] = sources or []

    # ---- notes / draft ----
    print()
    notes = ask("Free-form notes")
    if notes:
        entry["notes"] = notes

    # Quality bar check
    quality_blockers = []
    if not entry.get("prior_art_notes"):
        quality_blockers.append("prior_art_notes empty")
    if not entry.get("disclosure_citation"):
        quality_blockers.append("disclosure_citation empty")
    if not entry.get("sources"):
        quality_blockers.append("sources empty")

    if args.draft or quality_blockers:
        entry["draft"] = True
        if quality_blockers:
            print()
            print("Quality bar not yet met:")
            for q in quality_blockers:
                print(f"  - {q}")
            print("Marking draft: true.")

    entry["last_updated"] = ask("Last updated (YYYY-MM-DD)",
        default=__import__("datetime").date.today().isoformat())

    # ---- preview ----
    print()
    print("=" * 60)
    print("  Preview")
    print("=" * 60)
    print(json.dumps(entry, indent=2, ensure_ascii=False))
    print()

    if args.append:
        if not ask_yes_no("Append to corpus.jsonl?", default=False):
            print("Aborted before append.")
            return
        with (ROOT / "corpus.jsonl").open("a") as f:
            f.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")
        print(f"  Appended to corpus.jsonl. Now run:")
        print(f"    python3 tools/validate.py corpus.jsonl --strict")
        print(f"    python3 tools/index.py .")
        print(f"    python3 tools/cross_cuts.py")
        print(f"    git add -A && git commit -m 'corpus: add {entry['id']}'")
    else:
        out = ROOT / f"entry-{entry['id']}.jsonl"
        out.write_text(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")
        print(f"  Wrote {out}")
        print()
        print("Review, edit if needed, then merge into corpus.jsonl:")
        print(f"  cat entry-{entry['id']}.jsonl >> corpus.jsonl")
        print(f"  python3 tools/validate.py corpus.jsonl --strict")
        print(f"  python3 tools/index.py .")
        print(f"  python3 tools/cross_cuts.py")
        print(f"  git add -A && git commit -m 'corpus: add {entry['id']}'")
        print(f"  git push origin <your-branch>  # then open a PR")


if __name__ == "__main__":
    main()
