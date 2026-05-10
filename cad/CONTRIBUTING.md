# Contributing to Free Microfluidics CAD

Thank you for considering a contribution. Before you submit a design,
please read this carefully — the contribution model here is unusual.

## What you are doing when you contribute

**You are depositing a fabricable design plus the metadata needed to
reproduce, evaluate, and cite it.**

The catalog exists because microfluidic chip designs almost never travel
with their publications. Reverse-engineering from figures wastes time
that should be spent improving the design. A deposit here cuts that
time to zero for the next group.

## CC0 dedication

By submitting a contribution you dedicate the metadata to the public
domain under CC0 1.0. Per-file CAD artifacts may carry CC0-1.0,
CERN-OHL-P, or another permissive open-hardware license; declare the
license in the entry's `license` field. Designs encumbered by patents
must flag the patents in `notes` so commercial users can assess
freedom-to-operate.

## What counts as a commons-grade entry

An entry is **commons-grade** (`draft: false`) when it satisfies all
five criteria:

### 1. The CAD artifacts are real

A design is not commons-grade until at least one fabricable artifact is
present in `designs/<id>/`: a GDSII for photolithography masters, a DXF
for laser-cut layers, an STL or STEP for 3D printing, a KiCad project
for embedded electrodes. Empty stubs do not count.

### 2. The intended fabrication path is named

The `intended_fab_recipe` field must point at a recipe in `../fab/` or
name an external process specifically enough that a fab engineer can
reproduce. "PDMS soft-lithography" is too vague; `pdms-su8-soft-
lithography-baseline` (a recipe id in `../fab/`) or "SU-8 2050 100 µm
spin at 1700 RPM, contact-aligner UV cure" is specific enough.

### 3. Validated performance is documented

The `validated_performance` field captures measured outcomes: flow
rates at given pressures, mixing time at given Reynolds, droplet
uniformity CV, throughput, pressure ratings. Numbers, not adjectives.

### 4. The provenance citation resolves to a primary source

The `publication_citation` field, when present, must point at a paper
with a DOI, a patent number, or another retrievable primary reference.
Designs released without a paper still need an attribution chain in
`notes`.

### 5. License is declared per-artifact

Mixed-license deposits are fine (a CC0 mask set with a CERN-OHL-P
controller PCB in the same project); each artifact's license must be
declared explicitly.

## Submitting a draft

Mark the entry `"draft": true` and document in `notes` what work would
be needed to clear the bar. Drafts reserve the slug, capture what is
known, and identify the strengthening work needed. The current 38 seed
designs are mostly drafts because their CAD artifacts are placeholder
stubs awaiting real depositions.

## Practical workflow

1. Run `python3 tools/validate.py designs.jsonl --strict` before
   submitting. This catches structural errors and quality-bar failures.
2. Place the new entry directory at `designs/<id>/` with the actual
   CAD files inside.
3. Append a new line to `designs.jsonl` matching `SCHEMA.md`.
4. Open a pull request.

## Choosing a good slug

The `id` field is a kebab-case slug used in cross-references from
`../fab/`, `../control/`, and `../corpus/`. Pick one that disambiguates
on substrate, geometry, and function:

- `<material>-<function>-<distinguishing-dim>` — e.g.,
  `pdms-flow-focusing-droplet-junction-50um`
- `<material>-<feature>-<context>` — e.g.,
  `glass-electrochemical-microelectrode-array-iso-format`

Slugs are immutable once an entry is referenced by another sub-tree.
Choose carefully.

## Cross-references to other sub-trees

`related_corpus_entries` references prior-art entries in `../corpus/`
this design implements or descends from. `related_fab_recipes`
references recipes in `../fab/` that produce the design. The validator
does not enforce that referenced ids exist (the cross-tree is a
catalog, not a build system), but missing references make the entry
less useful.

## Questions

Open an issue. Discussion of taxonomy, file-format conventions, and
quality-bar calibration is welcome.
