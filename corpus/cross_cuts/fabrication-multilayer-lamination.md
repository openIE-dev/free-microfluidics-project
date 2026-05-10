---
title: fabrication-multilayer-lamination
parent: Cross-cuts
layout: default
---

# Cross-cut: `fabrication-multilayer-lamination`

**4 corpus entries disclose this subsystem.**

Earliest disclosure: 2000

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Quake monolithic pneumatic membrane valve and pump (2000)

- **id**: `unger-2000-quake-monolithic-membrane-valve`
- **corpus**: academic
- **device class**: valve-component
- **creator**: Stephen Quake group, Caltech
- **disclosure**: Unger, M. A.; Chou, H.-P.; Thorsen, T.; Scherer, A.; Quake, S. R. Monolithic microfabricated valves and pumps by multilayer soft lithography. Science 2000, 288, 113–116. DOI: 10.1126/science.288.5463.113
- **ip status**: patented
- **prior art notes**: Foundational disclosure of pneumatically actuated elastomeric membrane valves built monolithically into a multilayer PDMS chip. By cyclically actuating three valves in series, a peristaltic pump is realized. This is the architectural ancestor of essentially every subsequent on-chip pneumatic valve and pump. Anticipates: pneumatic membrane valve (control channel + thin membrane + flow channel), peristaltic pumping by sequential valve actuation, large-scale integrated chip-scale fluidic circuits. Subsequent papers (Nordin 2017, Sanchez Noriega 2021) re-implement the same architecture in 3D-printed photopolymer.

## Microfluidic large-scale integration (2002)

- **id**: `thorsen-2002-microfluidic-large-scale-integration`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Quake group, Caltech
- **disclosure**: Thorsen, T.; Maerkl, S. J.; Quake, S. R. Microfluidic large-scale integration. Science 2002, 298, 580–584. DOI: 10.1126/science.1076996
- **ip status**: patented
- **prior art notes**: Demonstrated 'microfluidic large-scale integration' — thousands of Quake valves operated as binary multiplexers to address hundreds of chambers from a few control lines. The conceptual analog of VLSI for microfluidics. Anticipates: hierarchical valve multiplexing for chamber-array addressing (n chambers from O(log n) control lines), and the architectural model that underlies Fluidigm IFCs and most chip-scale microfluidic automation. Companion to Unger 2000 valve disclosure; together they define MLSI.

## Fluidigm Dynamic Array Integrated Fluidic Circuit (2003)

- **id**: `fluidigm-dynamic-array-ifc`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Fluidigm Corp. (now Standard BioTools)
- **disclosure**: Fluidigm Corp. (now Standard BioTools) Integrated Fluidic Circuit / Dynamic Array. https://www.standardbio.com/products/instruments-and-consumables and Fluidigm IFC patent family.
- **ip status**: patented
- **prior art notes**: Commercial implementation of Quake / Thorsen MLSI (microfluidic large-scale integration) for high-throughput qPCR, single-cell qPCR, and digital PCR. Anticipates: direct architectural lineage from Unger 2000 + Thorsen 2002 to commercial multi-thousand-well qPCR arrays. The corpus exists in part because of the IP positions Fluidigm built around this architecture.

## BioFire FilmArray multiplex PCR cartridge (2008)

- **id**: `biofire-filmarray-multiplex-pcr-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: BioFire Diagnostics (Idaho Technology origin); BioMérieux subsidiary
- **disclosure**: Idaho Technology Inc. (now BioFire Diagnostics, BioMérieux). FilmArray system. FDA 510(k) clearances K103175 (2011) and subsequent panels.
- **ip status**: patented
- **prior art notes**: Discloses a single-use disposable cartridge integrating sample preparation, nucleic acid extraction, multiplex nested PCR, and array-based detection in a closed pouch format. Anticipates: blister-pack on-cartridge reagent storage, foil-piercing actuation, multilayer thermoplastic lamination as a fabrication path for point-of-care molecular diagnostics, integrated thermal cycling within a sealed pouch, and the architectural pattern of 'sample-in / answer-out' multiplex IVD cartridges. The dominant commercial implementation in syndromic panel testing.
