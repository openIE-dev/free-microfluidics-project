---
title: CMOS-electrode-pixel-array
parent: Cross-cuts
layout: default
---

# Cross-cut: `CMOS-electrode-pixel-array`

**3 corpus entries disclose this subsystem.**

Earliest disclosure: 2003-12

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Manaresi 2003 CMOS DEP Cage Array (DEPArray foundation) (2003-12)

- **id**: `manaresi-2003-deparray-cmos-foundation`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: Manaresi, Romani, Medoro, Tartagni, Guerrieri (U Bologna / Silicon Biosystems)
- **disclosure**: Manaresi N., Romani A., Medoro G., Altomare L., Leonardi A., Tartagni M., Guerrieri R., IEEE Journal of Solid-State Circuits 38(12):2297-2305 (2003), doi:10.1109/JSSC.2003.819171
- **ip status**: patented
- **prior art notes**: Foundational JSSC paper disclosing a CMOS chip with a 320x320 array of individually addressable electrodes capable of generating, translating, and merging closed DEP potential cages around individual cells. Anticipates: (i) all subsequent CMOS-DEP single-cell platforms (DEPArray, Cambridge/Imperial DEP-on-CMOS work); (ii) the translation-by-sequential-activation mechanism for moving caged cells across the chip surface; (iii) the integration of CMOS readout circuitry with biological-fluid-compatible passivation. Direct ancestor of menarini-deparray and menarini-silicon-biosystems-deparray-nxt.

## Menarini Silicon Biosystems DEPArray NxT (2016)

- **id**: `menarini-silicon-biosystems-deparray-nxt`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Menarini Silicon Biosystems (formerly Silicon Biosystems SpA, Bologna)
- **disclosure**: Menarini Silicon Biosystems DEPArray NxT launch 2016; Peeters D. J. et al. Br J Cancer 108:1358 (2013); US patent 7,425,253
- **ip status**: patented
- **prior art notes**: DEPArray NxT discloses a CMOS chip whose surface is patterned with thousands of independently addressable electrode pixels capable of generating individual closed DEP potential cages; cells loaded into the chamber are trapped one-per-cage and can be visualized fluorescently then released individually for downstream single-cell sequencing. Anticipates: (i) CMOS-integrated DEP cage arrays for single-cell isolation; (ii) image-based gating with addressable individual cell recovery; (iii) the upgrade path from DEPArray V1 (this entry covers NxT) with improved electrode pixel density. Distinguished from menarini-deparray (existing entry) by NxT generation hardware.

## Cambridge / Imperial College DEP-on-CMOS Single-Cell Chip (2020)

- **id**: `cambridge-imperial-dep-on-cmos-2020`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: Cambridge / Imperial College DEP-on-CMOS academic groups (Toumazou, Mason, Demosthenous)
- **disclosure**: Hsu C.-H., Manaresi N., et al. (representative), Lab on a Chip 20:3009 (2020), doi:10.1039/D0LC00424C; Toumazou C. group Imperial College EPSRC reports 2018-2022
- **ip status**: open-permissive
- **prior art notes**: Cambridge/Imperial DEP-on-CMOS work discloses an academic generation of CMOS-integrated active-pixel DEP arrays produced via standard foundry processes with post-processing of bio-compatible passivation and a microfluidic cap. Anticipates: (i) the migration of DEPArray-style architectures (manaresi-2003-deparray-cmos-foundation) into commodity CMOS foundry processes; (ii) co-located impedance sensing per pixel for closed-loop DEP control; (iii) scaling DEP cage arrays to >100,000 pixels via deep-submicron CMOS. Open-access lineage parallel to Menarini DEPArray NxT.
