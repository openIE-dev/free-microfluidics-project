# Free Microfluidics Project

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

A four-layer initiative addressing the structural latency in microfluidics
between *what has been demonstrated*, *what can be bought as a commodity*,
and *what can be built in-house*.

The microfluidics field has, over thirty years, accumulated an unusually
large gap between published technique and accessible practice. Compared to
adjacent fields like semiconductors (TSMC PDKs, OpenROAD), molecular biology
(Addgene, NEB), or open-source software (PyPI, crates.io), microfluidics has
no equivalent clearinghouse for designs, recipes, or reference instruments.
This project is an attempt to assemble one.

The methodology mirrors the [Free Humanoid Corpus](https://openie-dev.github.io/free-humanoid-corpus/),
extended into four parallel CC0 repositories addressing different layers of
the latency problem.

## The four layers

```
┌─────────────────────────────────────────────────────────────────────┐
│                       free-microfluidics-project                     │
│                  (umbrella docs, governance, releases)               │
└─────────────────────────────────────────────────────────────────────┘
       │                  │                  │                  │
       ▼                  ▼                  ▼                  ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   corpus    │    │     cad     │    │     fab     │    │   control   │
│ prior-art   │    │ chip designs│    │  fabrication│    │ instrument  │
│  commons    │    │ (chip CAD)  │    │   recipes   │    │ firmware/HW │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
  legal-citability    publication →     commodity →        instrument
       layer        commodity gap     in-house gap            layer
```

Each repo is independently usable, CC0, and structurally similar
(SCHEMA.md, validate.py, JSONL master file, cross-cut indexing where
applicable, quarterly timestamped releases).

### [`corpus/`](corpus/) — Free Microfluidics Corpus
**Status: seeded (376 entries, 92 cross-cuts, 1883–2026)**

A structured prior-art commons. Every entry is a defensive publication
citable as 102/103 prior art at the moment of timestamped release.
Subsystem cross-cuts make the corpus a working invalidity-search tool
indexed by fabrication, pumping, valves, mixers, separators, droplets,
detection, cell handling, thermal management, interfaces, and architecture.

This sub-tree is the most mature; it mirrors the Free Humanoid Corpus
structurally with a 376-entry seed (375 commons-grade, 1 draft) and the
full quality-bar / timestamping / Jekyll scaffolding.

### [`cad/`](cad/) — Free Microfluidics CAD
**Status: seeded (38 designs, all draft pending CAD-file population)**

A CC0 catalog of microfluidic chip designs. Each entry includes the
device geometry (CAD files: GDSII, DXF, STL, KiCad), the intended
fabrication path, the validated performance characteristics, and the
provenance (paper, lab, license). Targets PDMS soft-lithography masters,
glass photolithography mask sets, thermoplastic injection-mold tooling,
and DLP-SLA print files.

The intent is to be the Addgene-equivalent for microfluidic chip designs
— a place where a working group can deposit a validated design and any
other group can fabricate it.

### [`fab/`](fab/) — Free Microfluidics Fab
**Status: seeded (25 recipes, 24 commons-grade, 1 draft)**

A CC0 catalog of microfluidic fabrication processes. Each entry is a
step-by-step process recipe with critical-parameter documentation,
equipment requirements, validated outcomes, and known failure modes.
Covers SU-8 master mold processing, PDMS replica molding and bonding,
glass HF etching, thermoplastic hot embossing, paper microfluidics
patterning, DLP-SLA enclosed-channel printing, and benchtop nanofluidic
fab.

The intent parallels the OpenIE GAA process spec for semiconductors:
benchtop-realizable, critical-parameters-explicit fabrication procedures
that work outside a foundry.

### [`control/`](control/) — Free Microfluidics Control
**Status: seeded (32 instruments, all draft pending hardware/firmware artifacts)**

A CC0 catalog of microfluidic instrument designs: pressure controllers,
syringe pumps, EWOD drivers, thermal cyclers, optical readout boards,
and the firmware that runs them. KiCad PCBs, Rust firmware, mechanical
CAD. The DropBot reference platform is the closest existing analog;
this aims for production-grade open-source instrumentation across the
whole microfluidic toolchain.

## Governance

CC0 across every repo. Contribution model is described per-repo in each
`CONTRIBUTING.md`. The umbrella repo coordinates:

- Quarterly synchronized releases across all four sub-repos
- Cross-repo references (corpus entries can cite CAD designs; CAD entries
  can cite fab recipes; fab recipes can cite control instruments)
- Triple-cryptographic timestamping (FreeTSA + DigiCert + OpenTimestamps)
  applied uniformly

## Naming and scope

The project name reflects the OpenIE convention (open infrastructure
projects in domains where IP and standards have ossified). It is part of
the [OpenIE](https://openie.dev) family alongside the silicon, compute,
corridor, and humanoid projects.

## License

CC0-1.0 across all four sub-repos. See each repo's `LICENSE` for the
formal dedication.

## What this is not

- A research lab. It is a clearinghouse for work that already exists.
- A standards body. The schemas are descriptive, not prescriptive.
- A commercial venture. CC0 means no royalties, no licensing, no
  exclusivity.
- A wiki. Every entry is structured against a fixed schema and gated by
  a quality bar enforced by `validate.py --strict`.

## How to start using it

```bash
git clone https://github.com/openIE-dev/free-microfluidics-project.git
cd free-microfluidics-project

# The corpus is the most populated; explore it first
cd corpus
python3 tools/lookup.py "pneumatic membrane valve"
python3 tools/lookup.py --tag droplet-flow-focusing-generation

# CAD, fab, and control are seeded — see each README for status and
# what shape of contribution turns drafts into commons-grade entries.
cd ../cad      && cat README.md
cd ../fab      && cat README.md
cd ../control  && cat README.md
```

## How to contribute

Each repo has its own `CONTRIBUTING.md`. The corpus is the most mature
and the easiest place to start: pick a paper, a product, or a fictional
depiction not yet in the corpus, run `python3 tools/new_entry.py`, and
open a PR.

For CAD/fab/control: the seed entries are mostly placeholders pending
real artifacts (CAD files, validated recipe parameters, firmware/PCBs).
If you have a chip design already in CC0 status, a working fab recipe
documented to publication quality, or an open-source instrument with
mature firmware, those are exactly the contributions that flip drafts
into commons-grade entries.

---

Public domain (CC0 1.0). Part of [OpenIE](https://openie.dev).
