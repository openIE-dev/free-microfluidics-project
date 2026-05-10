# Free Microfluidics Fab

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

A CC0 catalog of microfluidic fabrication recipes. Each entry is a
step-by-step procedure documented to a level a competent process engineer
can reproduce, with critical-parameter ranges, equipment requirements,
validated outcomes, and known failure modes.

Part of the [Free Microfluidics Project](https://github.com/openIE-dev/free-microfluidics-project).

**Status: seeded (25 recipes, 24 commons-grade, 1 draft).** Schema is in
place, validation tooling is functional, and 25 seed recipes are
documented to a level a competent process engineer can reproduce. The
catalog spans benchtop-realizable processes from PDMS soft lithography
through DLP-SLA enclosed-channel printing through 2pp direct-write.

## Why this exists

Microfluidic fabrication is folkloric. Recipes circulate as Word documents
between collaborating groups, in supplementary information of papers
(typically inadequate), and in the accumulated muscle memory of a few
senior cleanroom staff. Reproducing a published device often requires
re-deriving the recipe from incomplete description, with substantial
trial and error.

The pattern parallels what TSMC PDKs solved for semiconductors: structured,
versioned process documentation that travels with designs. There is no
analog in microfluidics. This repo is an attempt at one.

The benchtop-realizability mandate is critical: recipes here must be
reproducible without a Class 100 cleanroom. Where cleanroom-grade
equivalents exist (e.g., spin coater + mask aligner + UV LED instead of
contact aligner with mercury lamp), the recipe documents the substitution.

## What's in here

```
SCHEMA.md           — recipe-entry schema
recipes.jsonl       — master catalog (one JSON object per line)
recipes/            — extended recipe documentation, one subdirectory per id
INDEX.md            — generated alphabetical index
tools/
  validate.py       — schema and quality-bar enforcement
LICENSE             — CC0-1.0
```

## Quick start

```bash
git clone https://github.com/openIE-dev/free-microfluidics-project.git
cd free-microfluidics-project/fab

# Validate the catalog
python3 tools/validate.py recipes.jsonl --strict
```

## What's seeded

The 25 seed recipes span PDMS soft lithography, DLP-SLA enclosed-channel
printing, glass HF etching and bonding, hot embossing, multilayer
lamination, paper microfluidics patterning, electrode integration,
2pp direct-write, plasma surface activation, and silanization workflows.
Recipe classes covered include: `pdms-soft-lithography`,
`dlp-sla-enclosed-channels`, `glass-photolithography`, `glass-bonding`,
`electrode-integration`, `multilayer-lamination`, `2pp-direct-write`.

The seed recipes are populated with reasonable defaults from published
sources; they should be confirmed or refined by contributors with
hands-on experience. The 1 draft entry needs additional critical-parameter
documentation before it clears the commons-grade bar.

## Contributing

If you have a fabrication recipe that:
- works in your hands or your lab's hands (validated),
- is documented well enough that a competent process engineer can reproduce,
- is yours to dedicate (most recipes are not patentable as recipes; check
  for patent-encumbered process steps),

…it belongs here. Open a PR with:

1. A new line appended to `recipes.jsonl` matching `SCHEMA.md`.
2. Optionally, extended narrative in `recipes/<id>/RECIPE.md`.
3. The line passing `python3 tools/validate.py recipes.jsonl --strict`.

## License

CC0-1.0 across the catalog metadata and recipe text. Where a recipe
implements a patented process, the entry's `notes` field flags the
relevant patents so commercial users can assess freedom-to-operate.

---

Public domain (CC0 1.0). Part of the
[Free Microfluidics Project](https://github.com/openIE-dev/free-microfluidics-project).
