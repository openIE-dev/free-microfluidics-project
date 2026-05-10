---
title: MEMS-vapor-cell-anodically-bonded
parent: Cross-cuts
layout: default
---

# Cross-cut: `MEMS-vapor-cell-anodically-bonded`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2011-01-19

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Microsemi SA.45s Chip-Scale Atomic Clock (CSAC) (2011-01-19)

- **id**: `microsemi-csac-sa45s`
- **corpus**: private
- **device class**: nanofluidic-chip
- **creator**: Symmetricom (acquired by Microsemi 2013, then Microchip Technology 2018)
- **disclosure**: Lutwak et al., Proc. PTTI 2007 (Symmetricom CSAC); Microsemi (formerly Symmetricom) SA.45s datasheet 098-00026-000; commercial launch 2011-01.
- **ip status**: patented
- **prior art notes**: First commercial chip-scale atomic clock. Microfluidic-relevant content: the MEMS Cs vapor cell is genuinely a sealed nanofluidic structure containing controlled-pressure cesium vapor + N2 buffer gas, with optical access for VCSEL probing. Discloses: anodically-bonded silicon-glass-silicon vapor cell with internal cesium-azide pellet that is laser-decomposed to fill the cell; optically-pumped Cs D1 transition with coherent population trapping (CPT) detection; full RF locking electronics in <16 cm^3 module. Anticipates: MEMS-fabricated atomic vapor cells as the chip-scale-clock building block; the architectural pattern of MEMS vapor cell + VCSEL + photodiode + RF feedback as the standard CSAC design that has been replicated by all subsequent commercial CSACs (Vescent, Honeywell, AccuBeat).

## Vescent Photonics Compact Cs Vapor Cell Atomic Clock (2018)

- **id**: `vescent-csac`
- **corpus**: private
- **device class**: nanofluidic-chip
- **creator**: Vescent Photonics Inc.
- **disclosure**: Vescent Photonics Inc. corporate disclosures 2018; SBIR contracts AFRL FA9453-18.
- **ip status**: patented
- **prior art notes**: Vescent's chip-scale atomic clock and atomic-physics platform uses an extended-cavity diode laser (ECDL) instead of the VCSEL in the SA.45s. Vapor cell remains MEMS-fabricated. Discloses: MEMS Cs/Rb vapor cell architecture; ECDL laser source with sub-MHz linewidth; modular packaging suitable for integration into atom-interferometer payloads. Anticipates: ECDL-based CSAC architecture as an alternative to VCSEL-CSAC for higher-stability applications; the architectural pattern of CSAC modules as building blocks for portable atom interferometers and quantum gravimeters.
