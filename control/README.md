# Free Microfluidics Control

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

A CC0 catalog of microfluidic instrument designs: hardware, firmware, and
host-side software for the controllers, drivers, and readout boards that
turn microfluidic chips into functioning systems.

Part of the [Free Microfluidics Project](https://github.com/openIE-dev/free-microfluidics-project).

**Status: seeded (32 instruments, all draft).** Schema is in place,
validation tooling is functional, and 32 seed instruments are populated
covering pressure controllers, syringe pumps, EWOD drivers, valve banks,
thermal cyclers, and optical readout boards. Most carry empty hardware
and firmware stubs — flipping an instrument from draft to commons-grade
requires real KiCad sources, working firmware, and a BOM.

## Why this exists

Microfluidic chips are inert without instrumentation. A chip needs pressure
regulators, syringe pumps, valve drivers, thermal control, optical or
electrochemical readout, and a host-side controller orchestrating the
assay. Every academic group reinvents some subset of this stack; commercial
options are expensive and closed.

The DropBot platform from the Wheeler group at Toronto is the most
prominent open-source instrumentation effort, focused on digital
microfluidics. It demonstrates the model works. This repo aims for a
broader catalog covering the rest of the microfluidic toolchain — pressure
controllers, syringe pumps, valve banks, thermal cyclers, fluorescence
readers — at production-grade quality.

The architectural assumption is that microfluidic instruments are
fundamentally simple, and the ones that aren't simple are made artificially
complex by closed firmware and proprietary protocols. CC0 hardware + CC0
firmware + clean documentation should be sufficient for any working group
to assemble a complete microfluidic instrumentation stack.

## What's in here

```
SCHEMA.md             — instrument-entry schema
instruments.jsonl     — master catalog (one JSON object per line)
instruments/          — hardware/firmware artifacts, one subdirectory per id
INDEX.md              — generated alphabetical index
tools/
  validate.py         — schema and quality-bar enforcement
LICENSE               — CC0-1.0
```

## Quick start

```bash
git clone https://github.com/openIE-dev/free-microfluidics-project.git
cd free-microfluidics-project/control

# Validate the catalog
python3 tools/validate.py instruments.jsonl --strict

# Browse the seed instruments
ls instruments/
```

## What's seeded

The 32 seed instruments span pressure controllers (STM32-class),
syringe pumps, EWOD drivers (DropBot-derivative), valve-bank controllers,
thermal cyclers, fluorescence and PMT readout boards, dielectrophoresis
drivers, droplet-generator controllers, ESI HV controllers, Bluetooth
point-of-care readers, imaging stages, Coulter counters, and process
monitors for cell-therapy applications. Instrument classes covered:
`pressure-controller`, `syringe-pump`, `ewod-driver`,
`valve-bank-controller`, `thermal-cycler`, `other`.

The seed instruments are *placeholder templates*: schema entries are
real, but the actual KiCad / firmware / mechanical CAD files are empty
stubs awaiting community contribution.

## Contributing

If you have a microfluidic instrument design that:
- works (validated by you or your group),
- is yours to dedicate (CC0 / CERN-OHL-P / permissive license you can release),
- has KiCad or equivalent open-format CAD (no Eagle/Altium-only),
- has firmware in an open language (Rust, C, MicroPython, Arduino-C++ all OK),

…it belongs here. Open a PR with:

1. A new directory `instruments/<id>/` with hardware, firmware, BOM, docs.
2. A new line appended to `instruments/instruments.jsonl` matching `SCHEMA.md`.
3. The line passing `python3 tools/validate.py instruments.jsonl --strict`.

## License

CC0-1.0 across the catalog metadata. Hardware artifacts may carry
CERN-OHL-P or CC0; firmware may carry MIT/Apache/CC0. The `license` field
on each entry captures the per-artifact picture.

---

Public domain (CC0 1.0). Part of the
[Free Microfluidics Project](https://github.com/openIE-dev/free-microfluidics-project).
