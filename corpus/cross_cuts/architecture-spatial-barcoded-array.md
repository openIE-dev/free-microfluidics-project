---
title: architecture-spatial-barcoded-array
parent: Cross-cuts
layout: default
---

# Cross-cut: `architecture-spatial-barcoded-array`

**9 corpus entries disclose this subsystem.**

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

## Curio Bioscience Curio Seeker (Slide-seq commercial) (2022)

- **id**: `curio-bio-seeker-slideseq`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Curio Bioscience (Broad Institute spinout)
- **disclosure**: Curio Bioscience commercial launch of Slide-seqV2 as Curio Seeker, 2022. https://curiobioscience.com/. Stickels, R. R. et al. Highly sensitive spatial transcriptomics at near-cellular resolution with Slide-seqV2. Nat. Biotechnol. 2021, 39, 313-319. DOI: 10.1038/s41587-020-0739-1.
- **ip status**: patented
- **prior art notes**: Commercialization of Slide-seqV2: a glass puck densely coated with a monolayer of spatially-barcoded ~10 µm beads. Tissue is laid on the puck, RNA captured by adjacent beads, then library-prepped off-puck. Anticipates: bead-monolayer spatial transcriptomic substrates as an alternative to printed barcode grids (Visium); commercialization of an open-published spatial method by the originating lab's spinout, distinct from the 10x/Visium commercialization of Stahl 2016 spatial transcriptomics.

## Spatial multi-omics extensions (2023-2026 academic) (2023)

- **id**: `wu-zhang-2023-spatial-multiomics`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Various — BGI / 10x / Yale Fan lab and others
- **disclosure**: Various 2023-2026 publications extending spatial transcriptomics to spatial proteomics and multi-omics. Representative: Stereo-seq, BGI ST OMNI, 10x Visium HD.
- **ip status**: patented
- **prior art notes**: Composite reference for 2023-onward spatial multi-omics disclosures: sub-cellular spatial transcriptomics (Stereo-seq, Visium HD), integrated spatial transcriptomics + proteomics, and spatial epigenomics. Cumulative architectural disclosures from this period define the current state-of-the-art in spatial-omics microfluidic chip architectures, complementing the foundational 2016 Visium work.

## 10x Genomics Visium HD spatial transcriptomics slide (2023-10-05)

- **id**: `10x-genomics-visium-hd`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: 10x Genomics
- **disclosure**: 10x Genomics Visium HD product launch announcement, 2023-10-05. https://www.10xgenomics.com/products/visium-hd. Oliveira, M. F. et al. Characterization of immune cell populations in the tumor microenvironment of colorectal cancer using high definition spatial profiling. bioRxiv 2024-06-04. DOI: 10.1101/2024.06.04.597233.
- **ip status**: patented
- **prior art notes**: Successor to Visium with photolithographically-defined ~2 µm spatial barcode bins (vs. 55 µm spots in original Visium), enabling near-single-cell resolution while retaining the 'tissue-on-barcoded-grid' architecture. Capture is via a glass slide whose surface is patterned with millions of barcoded oligo-dT regions; tissue placed on top releases mRNA into the barcoded grid, then library prep proceeds off-slide. Anticipates: sub-cellular spatial-barcode arrays at 2 µm pitch, as a converging upper bound for Visium-class spatial transcriptomics; the integration with 10x's CytAssist instrument as an FFPE-compatible workflow.

## Organoid multi-omics on chip (2024 academic work) (2024)

- **id**: `fan-2024-organoid-multiomics`
- **corpus**: academic
- **device class**: organ-on-chip
- **creator**: Various — Fan / Huh / Skardal labs
- **disclosure**: Various 2024 publications combining organoid culture with multi-omics analysis on chip. Representative: Fan group Yale, Huh group Penn, Skardal group Wake Forest.
- **ip status**: patented
- **prior art notes**: Composite reference for 2024-onward organoid + multi-omics integration: organoid culture chips with integrated single-cell sampling, in-line multi-omics measurement, and longitudinal observation. Cumulative disclosures from this period merge the organoids-on-chip lineage with the spatial-omics lineage.

## Curio Trekker spatial cell-tracking platform (2024)

- **id**: `curio-trekker-spatial-celltracking`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Curio Bioscience
- **disclosure**: Curio Bioscience Curio Trekker product launch 2024. https://curiobioscience.com/products/curio-trekker/.
- **ip status**: unknown
- **prior art notes**: Extension of the Slide-seq bead-puck architecture to record cell positional barcodes in vivo: tissue is briefly exposed to a Trekker puck so cells take up positional barcode oligonucleotides, then dissociated and processed by standard scRNA-seq with barcode readout. Anticipates: 'spatial-tag-then-dissociate' architecture for combining standard droplet scRNA-seq with retained positional information, bypassing the resolution limits of in-situ-only readouts.
