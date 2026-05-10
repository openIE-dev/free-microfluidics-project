---
title: vat-photopolymerization
parent: Cross-cuts
layout: default
---

# Cross-cut: `vat-photopolymerization`

**3 corpus entries disclose this subsystem.**

Earliest disclosure: 2015

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Carbon Digital Light Synthesis (DLS / CLIP) Resin 3D Printer (2015)

- **id**: `carbon-dls-clip-resin-printer`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Carbon Inc. (Joseph DeSimone, Stanford / UNC)
- **disclosure**: Carbon Inc. CLIP technology disclosure Science 2015 (Tumbleston et al, Science 347:1349-1352, doi:10.1126/science.aaa2397); Carbon M1 launch 2016; M2 launch 2017
- **ip status**: patented
- **prior art notes**: Borderline microfluidic - included because the architectural primitive (oxygen-inhibited dead zone + continuous resin flow into the cure window + continuous Z-motion of build platform) constitutes a microfluidic system: the dead zone is a sub-100-micron-thick liquid layer with active flow replenishment, and resin flow into the dead zone is the rate-limiting step for print speed. Discloses: (1) the oxygen-permeable Teflon AF window creating a dead zone of un-cured resin; (2) continuous-Z-motion eliminating the peel cycle; (3) the resin-flow microfluidic problem of refilling the dead zone fast enough. Anticipates: any vat-photopolymerization system using an oxygen-inhibited window or similar dead-zone strategy with continuous Z motion and resin replenishment microfluidics. Foundational CLIP/DLS prior art.

## Cellbricks BioCarrier Bioprinter Platform (2018)

- **id**: `cellbricks-biocarrier-bioprinter`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Cellbricks GmbH
- **disclosure**: Cellbricks GmbH (Berlin) BioCarrier launch 2018; Cellbricks tissue-printing technology disclosure
- **ip status**: patented
- **prior art notes**: Discloses a DLP-bioprinter architectural innovation: the build platform is itself a microfluidic carrier chip with integrated perfusion channels, so the printed tissue is perfusable from the moment printing finishes (no manual transfer to a separate organ-on-chip). Anticipates: bioprinters that print directly onto microfluidic perfusion-substrate chips, eliminating the print-then-transfer-to-perfusion-system step that historically dominates organ-on-chip workflow. The architectural primitive is (DLP projection + cell-laden photocurable resin + microfluidic perfusion chip as build platform) producing perfusable tissue constructs in a single integrated workflow.

## CELLINK BIONOVA Digital Light Processing Bioprinter (2020)

- **id**: `cellink-bionova-stereolithography-bioprinter`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: BICO Group AB (CELLINK division, technology via acquisition of Visikol/CytoSurge bioprinting assets)
- **disclosure**: CELLINK BIONOVA launch 2020; BIONOVA X datasheet 2021
- **ip status**: patented
- **prior art notes**: Discloses a bioprinter architecture distinct from extrusion or droplet: digital light processing projects a UV pattern into a vat of cell-laden photocurable resin, curing each layer in seconds regardless of feature complexity. Anticipates: bioprinters using DLP projection of UV light into vats of cell-laden photocurable bioinks. Critical prior art for any DLP-bioprinting claim, including resolution and layer-rate claims. The architectural primitive is the (DMD UV projector + cell-laden photocurable resin vat + Z-axis build platform + per-layer image-based exposure) configuration applied to viable cells, with the engineering challenge being phototoxicity management and uniform cure across cell-bearing volumes.
