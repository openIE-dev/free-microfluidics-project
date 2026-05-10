# Free Microfluidics CAD — Schema v0.1

## Status

v0.1 is the initial scaffold. Schema is expected to evolve once the seed
designs expose inadequacies. New fields are added with provenance — the
first design to exercise a new field documents it in `notes`.

## Purpose

A structured catalog of CC0-licensed microfluidic chip designs. Each entry
points to the actual CAD files (GDSII, DXF, STL, KiCad) plus the structured
metadata an examiner, fabricator, or reviewer needs to assess fit, cost,
and compatibility.

The schema is design-centric (one entry = one chip design at one resolution
of one fabrication path). Variants and forks live as separate entries with
explicit `lineage_ancestors`.

## Quality bar

A design is commons-grade when:

- `cad_files` resolves to actual downloadable files committed in this repo
  or referenced by stable URL (Zenodo, OSF, persistent GitHub release).
- `fabrication_path` is specified concretely enough that a competent
  fabrication facility can reproduce it (e.g., "SU-8 2050 master,
  spin 50 µm, develop 6 min, PDMS 10:1 cured 60 min @ 65 °C, plasma
  bond to 1 mm Schott Borofloat").
- `validated_performance` cites a publication, an internal report, or a
  characterization protocol with measured values.
- `license` is CC0-1.0 or compatible (CERN-OHL-P, MIT-equivalent for CAD).
  Designs requiring license payment to use are not commons-grade.

Designs below this bar may be merged with `draft: true`.

## License posture

CC0-1.0 for the metadata catalog. Individual CAD files may carry their own
permissive license (CERN-OHL-P, etc.) — the `license` field captures this
explicitly per design.

## Entry schema

Each entry is one record. Required fields are marked [R], optional [O].

```
id                      [R]  slug, kebab-case, globally unique
canonical_name          [R]  the name most commonly used
aliases                 [O]  list of alternate names
designer                [R]  person, lab, or org
designer_country        [O]  ISO country code
license                 [R]  CC0-1.0 | CERN-OHL-P | MIT | other-permissive
                             | encumbered-do-not-use
license_notes           [O]  free-text license clarification
device_class            [R]  same taxonomy as corpus SCHEMA.md device_class
fabrication_path        [R]  concrete recipe: substrate, masking, bonding,
                             cure parameters, etc.
substrate_material      [O]  PDMS | glass | silicon | thermoplastic | paper |
                             hybrid | other
channel_geometry        [R]  smallest dimension, depths, aspect ratios,
                             topology
chip_footprint_mm       [O]  characteristic linear dimension
cad_files               [R]  list of CAD file paths (relative to repo) or
                             stable URLs; format declared per file
cad_format              [O]  GDSII | DXF | STL | STEP | KLayout | KiCad |
                             OpenSCAD | mixed
mask_count              [O]  for photolithographic processes: number of
                             mask layers
validated_performance   [O]  measured outcomes: flow rates, mixing time,
                             droplet uniformity, pressure ratings
related_corpus_entries  [O]  ids in ../corpus/ this design implements or
                             descends from
related_fab_recipes     [O]  ids in ../fab/ this design requires
disclosed_subsystems    [O]  same taxonomy as corpus SCHEMA.md;
                             enables targeted prior art mapping
publication_citation    [O]  primary citation if the design is from a
                             paper; CC0-equivalent statement if released
                             directly
sources                 [R]  references, including paper DOIs, repo URLs,
                             characterization reports
notes                   [O]  free-text observations
draft                   [O]  boolean
schema_version          [R]  integer matching schema spec version
last_updated            [R]  ISO 8601 date
```

## Storage format

Master catalog: `designs.jsonl` — one JSON object per line, append-only,
git-tracked.

CAD files live under `designs/<id>/` directories alongside the JSONL row
that references them.

Index: `INDEX.md` — generated, alphabetical by canonical_name with id and
one-line summary.

## Versioning

Schema version increments on breaking changes. Entries carry
`schema_version` so older entries can be migrated. Forks of a design that
diverge in geometry get a new id, not a version bump on the original.
