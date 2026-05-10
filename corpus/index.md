---
title: Home
layout: home
nav_order: 1
description: "A public-domain prior art commons for microfluidics. CC0."
permalink: /
---

# Free Microfluidics Corpus
{: .fs-9 }

A public-domain prior art commons covering microfluidic devices, lab-on-a-chip platforms, nanofluidic systems, droplet and digital microfluidics, integrated components, and commercial products from private companies, open-source repositories, science fiction, and academia.
{: .fs-6 .fw-300 }

[Browse the corpus](browse/){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Cross-cuts](cross_cuts/){: .btn .fs-5 .mb-4 .mb-md-0 .mr-2 }
[GitHub](https://github.com/openIE-dev/free-microfluidics-project){: .btn .fs-5 .mb-4 .mb-md-0 }

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](https://github.com/openIE-dev/free-microfluidics-project/blob/main/LICENSE)

---

**The corpus IS the prior art commons.** Every entry, at the moment of timestamped commit and quarterly release, is a defensive publication. There is no separate commons layer above this catalog — the structured data here, combined with the cryptographic timestamping in `releases/`, is itself the invalidity-contention material.

This corpus is part of the [Free Microfluidics Project](https://github.com/openIE-dev/free-microfluidics-project), a four-layer initiative addressing the legal-citability layer (this corpus), the publication-to-commodity gap (open chip CAD), the in-house fabrication gap (open process recipes), and the instrument layer (open firmware and hardware).

---

## What it covers

| Corpus | Count | Role |
|:---|---:|:---|
| Private | 112 | Patent-thicket holders, commercial cartridges, instrument vendors |
| Academic | 185 | Peer-reviewed disclosures already prior art automatically |
| Fictional | 36 | Narrative depictions of lab-on-chip-equivalents |
| Open | 43 | Open-hardware microfluidics (DropBot, OpenPCR, Poseidon, OpenFlexure, Chi.Bio, eVOLVER, Squid, µManager, Opentrons, Bento Lab, Hackuarium, Genspace, Counter Culture Labs, La Paillasse, Public Lab, …) |
| **Total** | **376** | (375 commons-grade, 1 draft) |

Entries span **1883** (Reynolds pipe-flow transition) through **2026** (DISH volumetric printing; AESOP acoustic-electric poration). Earliest fictional depiction: Huxley's *Brave New World* hatchery (1932). Earliest device-class disclosures: Pohl 1951 (DEP), Terry/Stanford GC chip (1979), Canon Bubble Jet (1979), Tuckerman-Pease silicon microchannel cooling (1981), Boom guanidinium-silica (1990), Manz/Widmer µTAS framing (1990).

This is a seed. Microfluidics is a large field; the corpus should grow into the thousands of entries to be properly representative.

---

## The 92 cross-cuts are the working tool

Each [subsystem cross-cut](cross_cuts/) is a chronologically-ordered list of every disclosing entry, with `prior_art_notes` and `disclosure_citation` ready to drop into an invalidity contention.

| Cross-cut | Earliest | Entries |
|:---|---:|---:|
| [Thermal bubble-jet pumping](cross_cuts/pump-thermal-bubble-jet.html) | 1979 | 2 |
| [PDMS soft lithography](cross_cuts/fabrication-pdms-soft-lithography.html) | 1998 | 8 |
| [Quake monolithic membrane valve](cross_cuts/valve-quake-pneumatic-membrane.html) | 2000 | 4 |
| [Flow-focusing droplet generation](cross_cuts/droplet-flow-focusing-generation.html) | 2003 | 5 |
| [DLP-SLA enclosed channels](cross_cuts/fabrication-dlp-sla-enclosed-channels.html) | 2017 | 2 |
| [Stat-test cartridge architecture](cross_cuts/architecture-stat-test-cartridge.html) | 1966 | 5 |
| [Multiplex cartridge architecture](cross_cuts/architecture-multiplex-cartridge.html) | 2003 | 2 |
| [Acoustic-streaming pumping](cross_cuts/pump-acoustic-streaming.html) | 2026 | 1 |

→ [All 92 cross-cuts](cross_cuts/)

The full schema enumerates 127 cross-cut tags ([SCHEMA.md](SCHEMA.html)); 92 are populated by the seed entries, with the remainder waiting on future contributions.

---

## Provenance

Quarterly releases will carry three independent cryptographic timestamps attesting pre-existence:

- **FreeTSA** (RFC 3161)
- **DigiCert** (RFC 3161)
- **OpenTimestamps** (Bitcoin-anchored)

→ [Release runbook](RELEASE_RUNBOOK.html) · [Timestamping ceremony](TIMESTAMPING.html)

---

## Use it from the command line

```bash
git clone https://github.com/openIE-dev/free-microfluidics-project.git
cd free-microfluidics-project/corpus

# Validate the corpus
python3 tools/validate.py corpus.jsonl --strict

# Look up prior art for a patent-claim phrase
python3 tools/lookup.py "pneumatic membrane valve with elastomeric multilayer"

# List entries that disclose a specific subsystem tag
python3 tools/lookup.py --tag droplet-flow-focusing-generation

# Filter by date and IP status
python3 tools/lookup.py "staggered herringbone mixer" --before 2010 --commons-only

# Scaffold a new entry interactively
python3 tools/new_entry.py
```

---

## How to contribute

See [Contributing](CONTRIBUTING.html). Quality bar is load-bearing — entries that aren't yet defensible should be merged with `draft: true`.

---

Public domain (CC0 1.0). The corpus IS the prior art commons.
