# Free Microfluidics Control — Schema v0.1

## Status

v0.1 is the initial scaffold. Schema is expected to evolve as the seed
instrument exposes inadequacies.

## Purpose

A structured catalog of CC0 microfluidic instrument designs: pressure
controllers, syringe pumps, EWOD drivers, thermal cyclers, optical readout
boards, and the firmware that runs them. Each entry includes the actual
hardware and firmware artifacts plus the structured metadata needed to
build, calibrate, and use the instrument.

The DropBot project (Wheeler group, University of Toronto) is the closest
existing analog. This repo aims for a broader catalog spanning the entire
microfluidic toolchain.

## Quality bar

An instrument design is commons-grade when:

- `hardware_artifacts` resolves to actual KiCad / mechanical CAD / BOM
  files committed in this repo or referenced by stable URL.
- `firmware_artifacts` resolves to actual source code with a buildable
  toolchain documented.
- `validated_performance` cites a publication, internal report, or
  characterization protocol with measured values (pressure resolution,
  flow rate range, thermal stability, etc.).
- `bill_of_materials` lists actual parts with vendor and part numbers
  sufficient to source them.
- `license` is CC0-1.0 or compatible permissive license (CERN-OHL-P
  for hardware, MIT/Apache for firmware).

Designs below this bar may be merged with `draft: true`.

## License posture

CC0-1.0 for the catalog metadata. Hardware artifacts (PCBs, mechanical
CAD) typically use CERN-OHL-P or CC0-1.0; firmware typically uses MIT,
Apache-2.0, or CC0-1.0. The `license` field captures this per artifact.

## Entry schema

Each entry is one record. Required fields are marked [R], optional [O].

```
id                      [R]  slug, kebab-case, globally unique
canonical_name          [R]  the name most commonly used
aliases                 [O]  list of alternate names
designer                [R]  person, lab, or org
designer_country        [O]  ISO country code
license                 [R]  CC0-1.0 | CERN-OHL-P | MIT | Apache-2.0 |
                             other-permissive | mixed
license_notes           [O]  per-artifact license clarification
instrument_class        [R]  see instrument class taxonomy below
purpose                 [R]  brief description of what the instrument does
hardware_artifacts      [R]  list of {path_or_url, format, license}
                             (KiCad PCBs, mechanical CAD, enclosure STL)
firmware_artifacts      [O]  list of {path_or_url, language, license}
                             (Rust, C, MicroPython, etc.)
software_artifacts      [O]  list of host-side software, libraries, GUIs
bill_of_materials       [R]  list of {part, vendor, part_number,
                             quantity, unit_cost_usd}
build_difficulty        [O]  hobbyist | intermediate | professional |
                             cleanroom-required
estimated_cost_usd      [O]  total parts cost
validated_performance   [O]  measured outcomes
related_cad_designs     [O]  ids in ../cad/ this instrument interfaces
                             with
related_fab_recipes     [O]  ids in ../fab/ this instrument enables or
                             relies on
related_corpus_entries  [O]  ids in ../corpus/ this design implements or
                             descends from
publication_citation    [O]  primary citation if from a paper
sources                 [R]  references
notes                   [O]  free-text including patent-encumbrance flags
draft                   [O]  boolean
schema_version          [R]  integer matching schema spec version
last_updated            [R]  ISO 8601 date
```

## Instrument class taxonomy

- `pressure-controller` — gas-pressure regulators (single or multi-channel)
- `syringe-pump` — open syringe pumps
- `peristaltic-pump-driver` — peristaltic-pump driver hardware
- `ewod-driver` — digital microfluidics electrode driver
- `thermal-cycler` — PCR thermal cycler
- `microfluidic-thermostat` — Peltier-based on-chip thermal control
- `optical-readout-board` — fluorescence / colorimetric readout
- `impedance-readout-board` — coulter / cytometry electronics
- `acoustic-driver` — piezo or surface-acoustic-wave drivers
- `acoustic-electric-driver` — combined platforms (e.g., AESOP-style)
- `flow-rate-sensor` — inline flow sensors
- `bubble-detector` — inline bubble detection
- `chip-holder` — instrument-side chip mount with fluidic / electrical /
  thermal interfaces
- `valve-bank-controller` — pneumatic valve manifold drivers
- `multi-channel-controller` — orchestrating instrument for full assay
  workflows
- `other` — escape hatch with explanation in notes

## Storage format

Master catalog: `instruments.jsonl` — one JSON object per line, append-only.

Hardware and firmware live under `instruments/<id>/` directories alongside
the JSONL row.

## Versioning

Schema version increments on breaking changes. Forks with substantive
hardware or firmware divergence get a new id, not a version bump.
