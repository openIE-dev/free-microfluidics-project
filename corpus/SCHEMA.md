---
title: Schema
layout: default
nav_order: 4
---

# Free Microfluidics Corpus — Schema v0.2

## Status

v0.2 is the initial public release of the Free Microfluidics Corpus and
adopts the same prior-art-commons architecture pioneered by the Free
Humanoid Corpus. The corpus is the commons; the schema is load-bearing
because every field is part of the disclosure.

## Purpose

A structured catalog of every microfluidic device, lab-on-a-chip system,
nanofluidic platform, droplet/digital-microfluidics architecture, integrated
component (valves, pumps, mixers, separators), academic disclosure, fictional
laboratory-on-chip depiction, and commercial product whose function depends
on small-channel fluid handling.

**The corpus IS the prior art commons.** Every entry, at the moment of
merge and timestamp, is a public disclosure of the engineering, design,
and prior art it describes. `prior_art_notes` is not editorial commentary
— it is the element-by-element analysis a competent examiner or
invalidity-contention attorney could cite.

The corpus serves three functions, in priority order:

1. **Defensive publication.** Every entry, at the moment of merge and timestamp,
   is a public disclosure. This collapses the latency between *demonstrated*
   (in a publication or product) and *legally citable* (as 102/103 prior art).
2. **Design space map.** What has been imagined, what has been built, what has
   been claimed, and where the gaps are. Microfluidics has a peculiarly large
   gap between published technique and commodity component; the corpus exists
   in part to shrink it.
3. **Citation graph.** Who built on whom, what lineage each design belongs to,
   what intellectual debts are owed. PDMS soft lithography, droplet
   microfluidics, digital microfluidics, and integrated chip-scale automation
   each have their canonical ancestors; the corpus makes those explicit.

## Quality bar for entries

An entry is not done when the schema fields are filled. An entry is done when:

- `disclosure_citation` resolves to a primary source verifiable by a third party.
- `first_disclosure_date` is defensible against challenge — earliest verifiable
  public disclosure, not earliest plausible date.
- `prior_art_notes` reads as a 102/103 anticipation analysis someone unrelated
  to us could cite without rewriting. It identifies specific subsystems disclosed
  and what claims those disclosures could anticipate.
- `sources` cite primary references (papers, books, patents, datasheets, product
  manuals), not Wikipedia or aggregators, except where the aggregator is itself
  the primary source.
- For patented entries, `ip_citations` lists actual patent numbers, and
  `prior_art_notes` points back at anticipating prior art entries by id.

Entries below this bar may be merged with a `draft: true` flag to make
incremental progress visible, but they do not yet count as commons material.

## License posture

CC0-1.0. The corpus itself is public domain dedication. Individual entries cite
their sources but the structured catalog is unencumbered.

## Timestamping

Because the corpus is the commons, the timestamp of disclosure for each entry
must be defensible. Git commit timestamps alone are insufficient for legal
purposes — they can be rewritten and are not third-party attested.

Required timestamping infrastructure (mirrored from Free Humanoid Corpus):

- **RFC 3161 timestamping** of every release tag via at least two recognized
  Time Stamping Authorities (e.g., FreeTSA, DigiCert TSA). Signature artifacts
  committed alongside the release.
- **OpenTimestamps** anchoring of release commits to Bitcoin (free, decentralized,
  cryptographically strong attestation of pre-existence).
- **Periodic releases** tagged at minimum quarterly so that newly-merged entries
  receive third-party-attested timestamps within a bounded window.
- **Submission to discoverable indices**: Google Patents non-patent literature
  corpus, IP.com Prior Art Database, and any other indices examiners actually
  search.

A commons that examiners cannot find when searching does not invalidate anything.
Discoverability is not optional.

## Entry schema

Each entry is one record. Required fields are marked [R], optional [O].

```
id                      [R]  slug, kebab-case, globally unique within corpus
canonical_name          [R]  the name most commonly used in literature/marketing
aliases                 [O]  list of alternate names, model numbers, codenames
corpus                  [R]  one of: private | open | fictional | academic
first_disclosure_date   [R]  ISO 8601 date or year; earliest verifiable public reference
disclosure_citation     [R]  source for the first_disclosure_date (DOI, ISBN, URL, patent #, datasheet)
creator                 [R]  company / lab / studio / author / collective
creator_country         [O]  ISO country code of creator
device_class            [R]  see device_class taxonomy below
substrate_material      [O]  PDMS | glass | silicon | thermoplastic | paper | hybrid | other
fabrication_method      [O]  soft-lithography | photolithography | dlp-sla | hot-embossing |
                             injection-molding | laser-ablation | xurography | 2pp | other
channel_geometry        [O]  free text: smallest channel dimension, aspect ratio, network topology
flow_regime             [O]  pressure-driven | electrokinetic | acoustic | capillary |
                             centrifugal | digital-droplet | passive | mixed
chip_footprint_mm       [O]  characteristic linear dimension of the chip in mm if disclosed
sample_volume           [O]  characteristic working volume (e.g., "10 nL", "600 aL", "5 µL")
throughput              [O]  if disclosed (e.g., "1000 droplets/s", "200 cells/min")
power_source            [O]  external pumps | piezo | thermal | passive | battery | tethered
end_application         [O]  diagnostic | research | bioprocess | drug-delivery |
                             industrial | analytical | thermal-mgmt | other | mixed
control_architecture    [O]  manual | scripted | feedback-controlled | computer-vision-loop |
                             AI-controlled | open-loop
sensing                 [O]  optical, electrochemical, impedance, acoustic, mass-spec coupled, etc.
notable_capabilities    [O]  list of disclosed/claimed capabilities
ip_status               [R]  patented | open-permissive | open-copyleft | public-domain |
                             fictional | trade-secret | unknown
ip_citations            [O]  patent numbers, license identifiers, repo URLs, FDA 510(k) numbers
prior_art_notes         [O]  what subsystems/claims this entry could anticipate as 102/103 prior art
lineage_ancestors       [O]  ids of entries this design descends from
lineage_descendants     [O]  ids of entries that descend from this (filled in later passes)
sources                 [R]  list of citations (papers, books, articles, repos, datasheets, manuals)
notes                   [O]  free-text observations
disclosed_subsystems    [O]  structured tags identifying specific subsystems disclosed
                             (see subsystem taxonomy below); enables targeted prior art search
cpc_classifications     [O]  CPC classification codes for examiner discoverability
                             (e.g., "B01L 3/00" microfluidic devices, "G01N 27/447" capillary
                             electrophoresis, "B01F 13/00" mixers)
draft                   [O]  boolean; true if the entry has not yet cleared the quality bar
schema_version          [R]  integer matching schema spec version
last_updated            [R]  ISO 8601 date
```

## Device class taxonomy

The high-level partition. An entry has exactly one `device_class`. If you find
yourself wanting to assign two, use the dominant one and tag the secondary
behavior in `disclosed_subsystems`.

- `lab-on-chip` — integrated multi-step assay or analytical platform
- `point-of-care-cartridge` — single-use disposable cartridge, often diagnostic
- `organ-on-chip` — tissue-construct or vasculature-mimicking platform
- `droplet-generator` — emulsion or droplet-library producer
- `digital-microfluidics` — electrowetting on dielectric, addressable droplet
  manipulation
- `single-cell-platform` — single-cell trapping, sorting, sequencing prep
- `nanofluidic-chip` — sub-micron channel platform
- `pump-component` — discrete pump or pumping mechanism (commercial or
  on-chip primitive)
- `valve-component` — discrete valve, valve array, or membrane valve mechanism
- `mixer-component` — micromixer (passive, active, herringbone, etc.)
- `separator-component` — separation primitive (DLD, acoustic, dielectrophoretic,
  inertial focusing, magnetic)
- `flow-controller` — pressure or flow regulator, syringe pump, controller
  electronics
- `chip-holder` — interface hardware (sample stage, manifold, optical access)
- `printer-tooling` — fabrication tooling that produces microfluidic devices
  (3D printers, mold makers, hot-embossing presses)
- `consumable-bulk` — reagents, surface-treatment kits, sealing films
- `inkjet-printhead` — including thermal and piezoelectric printheads (the
  largest commercial microfluidic deployment)
- `cooling-substrate` — microchannel coolers, two-phase chip-cooling primitives
- `dispenser-pipettor` — automated liquid handling at sub-µL precision
- `fictional-laboratory` — narrative depictions of lab-on-chip equivalents
- `other` — escape hatch with explanation in notes

## IP status definitions

- `patented` — known patents asserted, with patent numbers
- `open-permissive` — MIT, BSD, Apache, CERN-OHL-P, etc.
- `open-copyleft` — GPL, CERN-OHL-S, etc.
- `public-domain` — CC0 or equivalent dedication, or expired protection
- `fictional` — exists only in narrative; copyright on the depiction may exist
  but the engineering description is unencumbered as prior art
- `trade-secret` — capability disclosed but mechanism not (BioFire FilmArray
  cartridges, Theranos-era claims, many commercial lab-on-chip cartridges)
- `unknown` — needs investigation

## Subsystem taxonomy

Tags applied to `disclosed_subsystems` to enable targeted prior art search. An
entry tags every subsystem it discloses with enough specificity to cite. Tags
are append-only to preserve cross-entry searchability.

**Fabrication**
- `fabrication-pdms-soft-lithography`
- `fabrication-pdms-replica-molding`
- `fabrication-glass-anodic-bonding`
- `fabrication-glass-thermal-bonding`
- `fabrication-glass-hf-etching`
- `fabrication-silicon-drie`
- `fabrication-silicon-koh-etching`
- `fabrication-su8-photoresist`
- `fabrication-thermoplastic-injection-molding`
- `fabrication-thermoplastic-hot-embossing`
- `fabrication-thermoplastic-laser-cutting`
- `fabrication-paper-microfluidics`
- `fabrication-xurography`
- `fabrication-dlp-sla-enclosed-channels`
- `fabrication-2pp-direct-write`
- `fabrication-multi-resolution-3d-printing`
- `fabrication-volumetric-3d-printing`
- `fabrication-multilayer-lamination`
- `fabrication-cyclic-olefin-copolymer`

**Pumping and flow drive**
- `pump-syringe-driven`
- `pump-pressure-controlled-air-over-liquid`
- `pump-peristaltic-on-chip`
- `pump-membrane-pneumatic`
- `pump-piezoelectric-disc`
- `pump-piezoelectric-stack`
- `pump-electroosmotic`
- `pump-electrohydrodynamic`
- `pump-capillary-passive`
- `pump-centrifugal-rotational`
- `pump-thermal-bubble-jet`
- `pump-acoustic-streaming`
- `pump-solenoid-displacement`
- `pump-stepper-volumetric`

**Valves**
- `valve-quake-pneumatic-membrane`
- `valve-doormat-style`
- `valve-torque-actuated`
- `valve-thermal-paraffin`
- `valve-magnetic`
- `valve-burst-frangible`
- `valve-electrowetting`
- `valve-capillary-stop`
- `valve-check`
- `valve-rotary-multiport`

**Mixing**
- `mixer-passive-serpentine`
- `mixer-passive-staggered-herringbone`
- `mixer-passive-tesla`
- `mixer-passive-split-recombine`
- `mixer-passive-interleaved-streams`
- `mixer-active-acoustic`
- `mixer-active-electrokinetic`
- `mixer-active-magnetic`
- `mixer-tpms-embedded`

**Separation and sorting**
- `separation-deterministic-lateral-displacement`
- `separation-pinched-flow-fractionation`
- `separation-inertial-focusing`
- `separation-acoustophoresis`
- `separation-dielectrophoresis`
- `separation-magnetophoresis`
- `separation-capillary-electrophoresis`
- `separation-isoelectric-focusing`
- `separation-affinity-capture`
- `separation-membrane-filtration-on-chip`
- `separation-size-exclusion-chromatography`

**Droplets and digital microfluidics**
- `droplet-t-junction-generation`
- `droplet-flow-focusing-generation`
- `droplet-coflow-generation`
- `droplet-step-emulsification`
- `droplet-double-emulsion`
- `droplet-on-demand`
- `droplet-merging-electrocoalescence`
- `droplet-splitting-bifurcation`
- `droplet-sorting-fluorescence-activated`
- `dmf-electrowetting-on-dielectric`
- `dmf-addressable-electrode-array`

**Detection and sensing on chip**
- `detection-fluorescence-on-chip`
- `detection-electrochemical-on-chip`
- `detection-impedance-cytometry`
- `detection-surface-plasmon-resonance-on-chip`
- `detection-nanofluidic-scattering-spectroscopy`
- `detection-mass-spec-electrospray-coupled`
- `detection-raman-on-chip`
- `detection-label-free-imaging`

**Cell handling**
- `cell-trap-hydrodynamic`
- `cell-trap-acoustic-streaming-vortex`
- `cell-trap-dielectrophoretic`
- `cell-trap-microwell-array`
- `cell-poration-electric`
- `cell-poration-mechanical-shear`
- `cell-poration-acoustic`
- `cell-poration-photothermal`
- `cell-encapsulation-droplet`
- `cell-organoid-perfusion`

**Thermal management**
- `thermal-on-chip-peltier`
- `thermal-on-chip-resistive-heater`
- `thermal-pcr-cycling`
- `thermal-droplet-pcr-cycling`
- `thermal-isothermal-amplification`
- `thermal-microchannel-cooling-electronics`
- `thermal-two-phase-cooling`
- `thermal-jet-impingement`

**Interface and packaging**
- `interface-luer-lock-port`
- `interface-o-ring-seal`
- `interface-fluidic-edge-connector`
- `interface-blister-pack-reagent-storage`
- `interface-foil-pierce-actuation`
- `interface-pressure-manifold`
- `interface-optical-window-borofloat`
- `interface-electrode-integration`

**Surface chemistry**
- `surface-pdms-plasma-bonding`
- `surface-protein-passivation`
- `surface-hydrophilic-treatment`
- `surface-superhydrophobic-patterning`
- `surface-functionalization-silane`
- `surface-functionalization-thiol-gold`

**Materials**
- `material-pdms-base`
- `material-cyclic-olefin-polymer`
- `material-pmma-acrylic`
- `material-polycarbonate`
- `material-pegda-photoresin`
- `material-borofloat-glass`
- `material-quartz`
- `material-paper-cellulose`
- `material-thermal-bonding-films`

**System architecture**
- `architecture-stat-test-cartridge`
- `architecture-multiplex-cartridge`
- `architecture-droplet-library-screening`
- `architecture-organ-on-chip-vasculature`
- `architecture-body-on-chip-coupled-organs`
- `architecture-process-analytical-technology`
- `architecture-on-chip-incubator`
- `architecture-mass-production-volumetric-print`

This taxonomy is expected to grow. New tags are added with provenance — the
first entry to introduce a tag documents it in `notes`.

## Storage format

Master corpus: `corpus.jsonl` — one JSON object per line, append-only, git-tracked.
Per-corpus mirrors: `private.jsonl`, `open.jsonl`, `fictional.jsonl`, `academic.jsonl`.
Index: `CORPUS_INDEX.md` — generated, alphabetical by canonical_name with id and one-line summary.
Lineage graph: `lineage.json` — derived, ancestor/descendant DAG.

## Versioning

Schema version increments on breaking changes. Entries carry `schema_version` so
older entries can be migrated. v0.2 is the starting point for this corpus.
