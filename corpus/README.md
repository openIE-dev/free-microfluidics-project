# Free Microfluidics Corpus

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

A structured prior art commons covering microfluidic devices, lab-on-a-chip
platforms, nanofluidic systems, droplet and digital microfluidics architectures,
integrated components (valves, pumps, mixers, separators), academic disclosures,
fictional laboratory-on-chip depictions, and commercial products whose function
depends on small-channel fluid handling.

**The corpus IS the prior art commons.** Every entry, at the moment of
timestamped commit and quarterly release, is a defensive publication. There
is no separate commons layer above this catalog — the structured data here,
combined with the cryptographic timestamping in `releases/`, is itself the
invalidity-contention material.

This corpus exists because microfluidics has a peculiarly large gap between
*demonstrated technique* (the published / shipped state of the art) and
*commodity component* (what anyone with a PO can buy). The gap closes more
slowly than in adjacent fields like semiconductors (TSMC PDKs) or molecular
biology (Addgene). The corpus collapses the legal-citability latency for
everything in between.

The methodology is identical to the [Free Humanoid Corpus](https://openie-dev.github.io/free-humanoid-corpus/);
this is the second instance of the same template, demonstrating the structure
generalizes.

## License

CC0-1.0. Public domain dedication. See [LICENSE](LICENSE).

## What's in here

```
SCHEMA.md           — schema spec (currently v0.2)
README.md           — this file
TIMESTAMPING.md     — release ceremony for cryptographic timestamping
RELEASE_RUNBOOK.md  — step-by-step quarterly release instructions
CONTRIBUTING.md     — how to add entries

corpus.jsonl        — master corpus (one JSON object per line)
private.jsonl       — generated mirror, entries with corpus="private"
open.jsonl          — generated mirror
fictional.jsonl     — generated mirror
academic.jsonl      — generated mirror

CORPUS_INDEX.md     — generated alphabetical index
lineage.json        — generated ancestor/descendant DAG

cross_cuts/         — generated per-subsystem prior art views
  INDEX.md          — table of all cross-cuts with counts
  <tag>.md          — chronological view of all entries disclosing <tag>

tools/
  validate.py       — schema and quality-bar enforcement
  index.py          — generates CORPUS_INDEX.md, lineage.json, per-corpus mirrors
  cross_cuts.py     — generates cross_cuts/
  lookup.py         — patent-claim → ranked prior art entries
  new_entry.py      — interactive scaffolder for new entries
  verify_release.sh — third-party verification harness for tagged releases

_seed/              — one-shot seed-generator scripts; kept for provenance,
                      not used at steady state
```

## Quick start

```bash
git clone https://github.com/openIE-dev/free-microfluidics-project.git
cd free-microfluidics-project/corpus

# Validate the corpus
python3 tools/validate.py corpus.jsonl --strict

# Look up prior art for a patent-claim phrase
python3 tools/lookup.py "pneumatic membrane valve with elastomeric multilayer"

# List entries that disclose a specific tag
python3 tools/lookup.py --tag droplet-flow-focusing-generation

# Filter by date and ip status
python3 tools/lookup.py "staggered herringbone mixer" --before 2010 --commons-only

# Scaffold a new entry interactively, then submit as a PR
python3 tools/new_entry.py
```

## What it covers (initial release)

| Corpus | Count | Role |
|:---|---:|:---|
| Private | 112 | Patent-thicket holders, commercial cartridges, instrument vendors |
| Academic | 185 | Peer-reviewed disclosures already prior art automatically |
| Fictional | 36 | Narrative depictions of lab-on-chip-equivalents |
| Open | 43 | Open-hardware microfluidics (DropBot, OpenPCR, Poseidon, OpenFlexure, Chi.Bio, eVOLVER, Squid, µManager, Public Lab, Bento Lab, Hackuarium, Genspace, Counter Culture Labs, La Paillasse, Opentrons, etc.) |
| **Total** | **376** | (375 commons-grade, 1 draft) |

Entries span **1883** (Reynolds pipe-flow transition) through **2026**
(DISH volumetric printing; AESOP acoustic-electric poration). The
foundational fluid-mechanics anchors (Reynolds 1883, Taylor-Aris 1953,
Purcell 1977) predate microfluidics but every microfluidic theory paper
implicitly cites them; including them makes the prior-art chain
verifiable back to the roots. The earliest fictional depiction is
Huxley's Brave New World hatchery (1932); the earliest device-class
disclosures are Pohl 1951 (DEP), Terry/Stanford GC chip (1979), Canon
Bubble Jet (1979), Tuckerman-Pease silicon microchannel cooling (1981),
Boom guanidinium-silica nucleic-acid extraction (1990), and Manz/Widmer
µTAS framing plus Manz CE-on-chip (both 1990).

The corpus is still a seed. Microfluidics is a large field and the
corpus should grow into the thousands of entries to be properly
representative. The 376 entries here cover: inertial microfluidics, DEP,
EWOD, centrifugal lab-on-disc, sequencing flow cells (Illumina, Ion
Torrent, ONT, PacBio, Quantum-Si, Element, Singular), spatial
transcriptomics (Visium, GeoMx, CosMx, CODEX), digital PCR, multi-organ-
on-chip, optofluidics, fluidic logic, cartridges (cobas Liat, ePlex,
Lucira, BinaxNOW, BD Veritor, Piccolo Xpress), open hardware (DropBot,
OpenPCR, Poseidon, OpenFlexure, Chi.Bio, eVOLVER, Squid, µManager,
OpenSPIM, Opentrons, Bento Lab, Hackuarium, Genspace, Counter Culture
Labs, La Paillasse, Public Lab), and fictional depictions (Star Trek,
Hitchhiker's, Star Wars, Seveneves, Diaspora, Halo, GitS, Wildfire).

## Cross-cuts: the working tool

Each [subsystem cross-cut](cross_cuts/INDEX.md) is a chronologically-ordered
list of every disclosing entry, with `prior_art_notes` and
`disclosure_citation` ready to drop into an invalidity contention.

The seed populates **92** cross-cuts spanning fabrication, pumping, valves,
mixing, separation, droplets, detection, cell handling, thermal management,
interfaces, surface chemistry, materials, and system architecture. The full
schema enumerates 127 cross-cut tags (see [SCHEMA.md](SCHEMA.md)); the
remaining tags will populate as more entries are merged.

A few highlights from the seed:

| Tag | Earliest | Notable entries |
|:---|---:|:---|
| [`fabrication-pdms-soft-lithography`](cross_cuts/fabrication-pdms-soft-lithography.md) | 1998 | Duffy → Quake → 10x lineage |
| [`droplet-flow-focusing-generation`](cross_cuts/droplet-flow-focusing-generation.md) | 2003 | Anna → Drop-seq → ddPCR → 10x |
| [`valve-quake-pneumatic-membrane`](cross_cuts/valve-quake-pneumatic-membrane.md) | 2000 | Unger → Thorsen MLSI → Fluidigm |
| [`separation-inertial-focusing`](cross_cuts/separation-inertial-focusing.md) | 2007 | Di Carlo → CTC-iChip |
| [`dmf-electrowetting-on-dielectric`](cross_cuts/dmf-electrowetting-on-dielectric.md) | 2000 | Pollack → Cho → ALL/Illumina |
| [`thermal-microchannel-cooling-electronics`](cross_cuts/thermal-microchannel-cooling-electronics.md) | 1981 | Tuckerman-Pease |
| [`fabrication-volumetric-3d-printing`](cross_cuts/fabrication-volumetric-3d-printing.md) | 2019 | CAL → DISH |
| [`architecture-stat-test-cartridge`](cross_cuts/architecture-stat-test-cartridge.md) | 1966 | Tricorder → BioFire/Cepheid/Abbott/Lucira |

## How is this different from a database or wiki?

A wiki is editorial. A database is a lookup table. This is a *defensive
publication*: every entry, structured against a fixed schema, timestamped
cryptographically at quarterly release, exists to be cited.

The structural commitments matter:

1. **Schema-bound, machine-checkable.** Every entry passes `validate.py
   --strict` or it does not get merged. Quality bar fields are load-bearing,
   not decorative.
2. **Cross-cut-indexed.** Every disclosed subsystem is tagged; the
   cross-cut files are the working prior-art search surface.
3. **Cryptographically timestamped.** Each quarterly release carries
   triple-redundant attestations (FreeTSA, DigiCert, Bitcoin via
   OpenTimestamps) so the disclosure date is defensible against challenge.
4. **CC0.** No license to read, ingest, mirror, embed, train on, or cite.
   The corpus exists to be used.

## How to contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). The short version:

1. Run `python3 tools/new_entry.py` to scaffold a new entry.
2. Review and edit the resulting `entry-<id>.jsonl`.
3. Append to `corpus.jsonl`, run `python3 tools/validate.py corpus.jsonl --strict`,
   then `python3 tools/index.py .` and `python3 tools/cross_cuts.py`.
4. Open a PR.

Quality-bar entries that aren't yet defensible should be merged with
`draft: true` so incremental progress is visible without polluting the
commons-grade pool.

## Why microfluidics

Microfluidics stopped being a technique in the early 2000s and became a
*substrate*. The way "electronics" did in the 1960s. Nobody who works in
electronics expects to share peers with another person who works in
electronics; the field is too big and too fragmented. Microfluidics is the
same. It now spans cell biology, point-of-care diagnostics, semiconductor
analogs (digital microfluidics), chemical synthesis, drug delivery,
hydraulics, inkjet, organ-on-chip, single-cell sequencing prep, droplet
libraries for directed evolution, fuel cells, two-phase chip cooling, and
more.

The bigger problem the corpus is designed to address is the *latency between
layers*: techniques demonstrated in academic publications, commodity
components shipped with datasheets, and end products that contain
microfluidics invisibly. There's no compiler from the publication layer to
the commodity layer, and no decompiler from the product layer back to the
publications it descends from. This corpus is an attempt at the prior-art
substrate that lets at least the legal layer move at the speed of
disclosure.

---

Public domain (CC0 1.0). The corpus IS the prior art commons.
