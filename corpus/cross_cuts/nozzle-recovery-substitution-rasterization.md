---
title: nozzle-recovery-substitution-rasterization
parent: Cross-cuts
layout: default
---

# Cross-cut: `nozzle-recovery-substitution-rasterization`

**1 corpus entries disclose this subsystem.**

Earliest disclosure: 2018

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Mimaki TS500P-3200 Industrial Textile Sublimation Printer (2018)

- **id**: `mimaki-tx500p-3200-textile-printer`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Mimaki Engineering Co., Ltd.
- **disclosure**: Mimaki Engineering TS500P-3200 launch 2018; Mimaki industrial textile datasheet
- **ip status**: patented
- **prior art notes**: Discloses an industrial textile inkjet printer with two architecturally significant primitives: (1) NCU - an optical nozzle-check sensor that fires test drops at a sensor and detects missing/misaligned nozzles in real time during production; (2) NRS - the recovery system that, on detecting a missing nozzle, reroutes the rasterized data so an adjacent good nozzle prints the missing pixels using slightly elongated drops, allowing print to continue without stop-clean-restart. Anticipates: any high-throughput piezo inkjet system that uses optical real-time nozzle health sensing combined with raster-level data substitution to maintain throughput in the presence of partial nozzle failure. This is the architectural primitive that distinguishes industrial textile/single-pass inkjet from desktop graphic-arts inkjet, where stop-and-clean is acceptable.
