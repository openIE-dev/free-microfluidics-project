# Contributing to Free Microfluidics Control

Thank you for considering a contribution. Before you submit an
instrument design, please read this carefully — the contribution
model here is unusual.

## What you are doing when you contribute

**You are publishing a complete instrument: hardware (KiCad PCB,
mechanical CAD), firmware (Rust, C, MicroPython, Arduino-C++), host-
side software, BOM, and the documentation needed to build, calibrate,
and operate it.**

The catalog exists because every academic group reinvents some subset
of the microfluidic instrumentation stack — pressure regulators,
syringe pumps, valve banks, EWOD drivers, thermal cyclers, optical
readout — and commercial alternatives are expensive and closed. The
DropBot platform proves the open-instrument model works; this catalog
broadens it to the rest of the toolchain.

## CC0 dedication

By submitting a contribution you dedicate the metadata to the public
domain under CC0 1.0. Per-artifact licenses may differ:

- **Hardware**: CC0-1.0 or CERN-OHL-P preferred; CERN-OHL-S/W
  acceptable
- **Firmware**: MIT, Apache-2.0, BSD, or CC0
- **Mechanical CAD**: CC0-1.0 or CERN-OHL-P preferred; FreeCAD/STEP
  source format strongly preferred over proprietary

Declare each artifact's license in the entry's `license` field.
Closed-format-only deposits (Eagle without KiCad migration, Altium
without source files) are rejected — the catalog is for open
instruments.

## What counts as a commons-grade entry

An entry is **commons-grade** (`draft: false`) when it satisfies all
five criteria:

### 1. The hardware is fabricable from the deposit

KiCad project files (or compatible open-source EDA), gerbers, BOM with
specific part numbers and at least one supplier, mechanical CAD in
STEP or open native format, and assembly notes adequate for someone
who has not built the instrument before. Empty stubs do not count.

### 2. The firmware builds and runs

Source code in a repo (or in `instruments/<id>/firmware/`), a build
recipe that works on a clean machine, and a known-good firmware image
hash. "Firmware exists internally" is not commons-grade.

### 3. Validated performance is documented

The `validated_performance` field captures measured outcomes: pressure
range and resolution, flow accuracy, valve switching speed, thermal
ramp rate, optical SNR, etc. Numbers, not adjectives.

### 4. The build difficulty is honest

The `build_difficulty` field (`hobbyist | intermediate | professional
| cleanroom-required`) sets contributor expectations. An instrument
that requires a reflow oven plus stencil printing is not "hobbyist"
even if the parts are cheap.

### 5. The estimated cost is real

The `estimated_cost_usd` field is the actual current parts cost, not
a hopeful target. Round trips through Mouser / Digikey / LCSC carts
are the source of truth.

## Submitting a draft

Mark the entry `"draft": true` and document in `notes` what work would
be needed to clear the bar. The current 32 seed instruments are all
draft because their hardware and firmware artifacts are placeholder
stubs awaiting real depositions.

## Practical workflow

1. Run `python3 tools/validate.py instruments.jsonl --strict` before
   submitting. This catches structural errors and quality-bar failures.
2. Place the new instrument directory at `instruments/<id>/` with
   subdirectories for `hardware/`, `firmware/`, `mechanical/`, `bom/`,
   and `docs/`.
3. Append a new line to `instruments.jsonl` matching `SCHEMA.md`.
4. Open a pull request.

## Choosing a good slug

The `id` field is a kebab-case slug used in cross-references from
`../cad/`, `../fab/`, and `../corpus/`. Pick one that disambiguates
on instrument class, MCU/processor, and any distinguishing capability:

- `<descriptor>-<class>-<mcu-or-platform>` — e.g.,
  `dual-channel-pressure-controller-stm32`,
  `open-ewod-driver-dropbot-derivative`
- `open-<class>-<distinguishing-feature>` — e.g.,
  `open-fluorescence-detector-pmt`, `open-coulter-counter`

Slugs are immutable once an entry is referenced by another sub-tree.
Choose carefully.

## Cross-references to other sub-trees

`related_cad_designs` references chip designs in `../cad/` this
instrument interfaces with. `related_fab_recipes` references recipes
in `../fab/` this instrument enables or relies on.
`related_corpus_entries` references prior-art entries in `../corpus/`
this design implements or descends from.

## Questions

Open an issue. Discussion of instrument-class taxonomy, hardware
license conventions, and quality-bar calibration is welcome.
