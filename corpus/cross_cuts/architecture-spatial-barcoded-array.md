---
title: architecture-spatial-barcoded-array
parent: Cross-cuts
layout: default
---

# Cross-cut: `architecture-spatial-barcoded-array`

**6 corpus entries disclose this subsystem.**

Earliest disclosure: 2016

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Spatial transcriptomics (Visium / Slide-seq ancestors) (2016)

- **id**: `staahl-2016-spatial-transcriptomics`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Lundeberg group, Stockholm / 10x Genomics Visium
- **disclosure**: Ståhl, P. L. et al. Visualization and analysis of gene expression in tissue sections by spatial transcriptomics. Science 2016, 353, 78–82. DOI: 10.1126/science.aaf2403
- **ip status**: patented
- **prior art notes**: Disclosed spatial transcriptomics: a glass slide patterned with spatially-barcoded oligonucleotide capture probes, on which a tissue section is mounted and permeabilized to capture mRNA at known x,y positions. Anticipates: spatial-barcode-grid architecture for transcriptomics, and the 10x Genomics Visium / Visium HD platforms which extended the resolution from 100 µm to sub-cellular scale. Microfluidic in the sense that diffusion-mediated capture is the operative transport mechanism.

## NanoString GeoMx Digital Spatial Profiler (2019)

- **id**: `nanostring-geomx`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: NanoString Technologies (acquired by Bruker 2024)
- **disclosure**: NanoString GeoMx Digital Spatial Profiler. Merritt et al. 2020 Nat. Biotechnol. 38, 586–599.
- **ip status**: patented
- **prior art notes**: Tissue-section spatial profiling using UV-cleavable oligo-tagged probes, micro-aspiration of cleaved barcodes from operator-defined regions of interest, and downstream readout on the NanoString nCounter platform. Anticipates: micro-aspiration-from-tissue spatial profiling architecture, distinct from the Visium spatial-barcode-grid approach.

## Slide-seq spatial transcriptomics on bead arrays (2019)

- **id**: `rodriques-2019-slide-seq`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Macosko lab, Broad Institute
- **disclosure**: Rodriques, S. G. et al. Slide-seq: a scalable technology for measuring genome-wide expression at high spatial resolution. Science 2019, 363, 1463–1467. DOI: 10.1126/science.aaw1219
- **ip status**: patented
- **prior art notes**: Disclosed Slide-seq: 10 µm-resolution spatial transcriptomics by transferring tissue sections onto rubber-pucks coated with barcoded oligo beads with known spatial coordinates. Architectural alternative to 10x Visium (which uses lithographically-patterned spots). Anticipates: random-bead-array spatial transcriptomics, sub-cellular-resolution spatial-omics on chip-format substrates.

## DBiT-seq spatial multi-omics on chip (2020)

- **id**: `liu-fan-2020-dbit-seq`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: R. Fan group, Yale
- **disclosure**: Liu, Y. et al. High-spatial-resolution multi-omics sequencing via deterministic barcoding in tissue. Cell 2020, 183, 1665–1681.e18. DOI: 10.1016/j.cell.2020.10.026
- **ip status**: patented
- **prior art notes**: Disclosed DBiT-seq: deterministic-barcoding-in-tissue using two orthogonal sets of barcoded reagent flows through PDMS microfluidic channels pressed onto tissue, defining a 50 × 50 grid of 50 µm × 50 µm spatial barcodes. Anticipates: PDMS-microchannel-defined spatial barcoding architecture as alternative to spotted-array (Visium) and random-bead (Slide-seq) approaches.

## Spatial multi-omics extensions (2023-2026 academic) (2023)

- **id**: `wu-zhang-2023-spatial-multiomics`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Various — BGI / 10x / Yale Fan lab and others
- **disclosure**: Various 2023-2026 publications extending spatial transcriptomics to spatial proteomics and multi-omics. Representative: Stereo-seq, BGI ST OMNI, 10x Visium HD.
- **ip status**: patented
- **prior art notes**: Composite reference for 2023-onward spatial multi-omics disclosures: sub-cellular spatial transcriptomics (Stereo-seq, Visium HD), integrated spatial transcriptomics + proteomics, and spatial epigenomics. Cumulative architectural disclosures from this period define the current state-of-the-art in spatial-omics microfluidic chip architectures, complementing the foundational 2016 Visium work.

## Organoid multi-omics on chip (2024 academic work) (2024)

- **id**: `fan-2024-organoid-multiomics`
- **corpus**: academic
- **device class**: organ-on-chip
- **creator**: Various — Fan / Huh / Skardal labs
- **disclosure**: Various 2024 publications combining organoid culture with multi-omics analysis on chip. Representative: Fan group Yale, Huh group Penn, Skardal group Wake Forest.
- **ip status**: patented
- **prior art notes**: Composite reference for 2024-onward organoid + multi-omics integration: organoid culture chips with integrated single-cell sampling, in-line multi-omics measurement, and longitudinal observation. Cumulative disclosures from this period merge the organoids-on-chip lineage with the spatial-omics lineage.
