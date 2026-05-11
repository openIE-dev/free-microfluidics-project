---
title: combinatorial-split-pool-barcoding
parent: Cross-cuts
layout: default
---

# Cross-cut: `combinatorial-split-pool-barcoding`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2018

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Parse Biosciences Evercode Split-Pool Patent Family (2018)

- **id**: `parse-biosciences-evercode-splitseq-patent-family`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Parse Biosciences / University of Washington
- **disclosure**: US11680253B2 'Methods and compositions for tagging and analyzing single cells' (priority 2017); WO2018136629A1; Parse Biosciences (formerly Split Biosciences) commercial launch 2019
- **ip status**: patented
- **prior art notes**: Discloses combinatorial split-pool barcoding (SPLiT-seq) commercialized as Evercode: cells/nuclei are fixed and permeabilized, then iteratively split across 96-well plates and pooled, with each round appending a per-well barcode oligo via in-cell ligation. After 3-4 rounds, each cell has a unique combinatorial barcode without ever being individually compartmentalized. Anticipates: (a) instrument-free single-cell RNA-seq workflows using only standard microplates and pipettes; (b) any combinatorial-indexing scheme relying on cell as compartment; (c) fixation-compatible scRNA-seq permitting batched, time-pointed sampling. Foundational anchor: Rosenberg et al. 2018 Science 'Single-cell profiling of the developing mouse brain and spinal cord with split-pool barcoding'.

## Scale Biosciences Split-Pool Combinatorial Indexing Patent Family (2021)

- **id**: `scale-bio-split-pool-patent-family`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Scale Biosciences, Inc.
- **disclosure**: WO2021252617A1 'Methods and compositions for combinatorial indexing of single cells' (priority 2020); Scale Biosciences product launch 2022; Cao et al. 2017 Science (academic anchor for sci-RNA-seq)
- **ip status**: patented
- **prior art notes**: Discloses Scale Bio's commercial implementation of combinatorial indexing (sci-RNA-seq lineage from the Shendure lab): three rounds of split-pool labeling using indexed RT primers, indexed ligation oligos, and PCR primers. Distinct from Parse's Evercode in chemical detail (RT vs ligation vs in-cell ligation order, primer chemistry) but architecturally similar. Anticipates: (a) any 3-round combinatorial indexing workflow for million-cell-scale scRNA-seq; (b) the use of fixed nuclei rather than live cells as compartments; (c) commercialization of the academic sci-RNA-seq protocol. Foundational anchor: Cao et al. 2017 Science, Cao et al. 2019 Nature.
