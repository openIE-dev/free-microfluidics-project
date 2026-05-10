---
title: pump-peristaltic-on-chip
parent: Cross-cuts
layout: default
---

# Cross-cut: `pump-peristaltic-on-chip`

**8 corpus entries disclose this subsystem.**

Earliest disclosure: 1989

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Silicon piezoelectric peristaltic micropump (Smits 1989) (1989)

- **id**: `smits-1989-piezo-peristaltic-pump`
- **corpus**: academic
- **device class**: pump-component
- **creator**: Jan Smits (Twente)
- **disclosure**: Smits, J. G. Piezoelectric micropump with three valves working peristaltically. Sens. Actuators A 1990, 21, 203–206. DOI: 10.1016/0924-4247(90)85039-7
- **ip status**: patented
- **prior art notes**: Disclosed silicon piezoelectric peristaltic micropump with three actively-actuated valves working in sequence to peristaltically drive fluid. Architectural alternative to Van Lintel's check-valve diaphragm topology. Anticipates: peristaltic-on-silicon-MEMS pumping, sequential-actuation valve architecture, and the broader 'all-valves-pumped' (no passive check valves) topology subsequently demonstrated by Berg/Quake.

## Quake monolithic pneumatic membrane valve and pump (2000)

- **id**: `unger-2000-quake-monolithic-membrane-valve`
- **corpus**: academic
- **device class**: valve-component
- **creator**: Stephen Quake group, Caltech
- **disclosure**: Unger, M. A.; Chou, H.-P.; Thorsen, T.; Scherer, A.; Quake, S. R. Monolithic microfabricated valves and pumps by multilayer soft lithography. Science 2000, 288, 113–116. DOI: 10.1126/science.288.5463.113
- **ip status**: patented
- **prior art notes**: Foundational disclosure of pneumatically actuated elastomeric membrane valves built monolithically into a multilayer PDMS chip. By cyclically actuating three valves in series, a peristaltic pump is realized. This is the architectural ancestor of essentially every subsequent on-chip pneumatic valve and pump. Anticipates: pneumatic membrane valve (control channel + thin membrane + flow channel), peristaltic pumping by sequential valve actuation, large-scale integrated chip-scale fluidic circuits. Subsequent papers (Nordin 2017, Sanchez Noriega 2021) re-implement the same architecture in 3D-printed photopolymer.

## BioTek MultiFlo FX dispenser (2010)

- **id**: `biotek-multiflo-flx-dispenser`
- **corpus**: private
- **device class**: dispenser-pipettor
- **creator**: BioTek (acquired by Agilent 2019)
- **disclosure**: Agilent Technologies BioTek MultiFlo FX. https://www.agilent.com
- **ip status**: patented
- **prior art notes**: Microplate dispenser/washer with peristaltic-pump-based reagent dispensing into 96/384/1536-well plates. Reference for the broader 'plate-format dispenser' product category that competes with Echo acoustic dispensing on cost and fluid compatibility (more inclusive of viscous fluids that Echo handles poorly).

## Pumpy peristaltic pump (open-hardware) (2017)

- **id**: `ufluidix-pumpy`
- **corpus**: open
- **device class**: pump-component
- **creator**: Pumpy community / uFluidix
- **disclosure**: Pumpy peristaltic pump open-source design. https://github.com/pumpy
- **ip status**: open-permissive
- **prior art notes**: Open-hardware peristaltic pump design with 3D-printable mechanical parts and Arduino control firmware. Sub-$100 BOM. Anticipates: prosumer peristaltic-pump category, with Arduino + stepper motor + 3D-printed roller assembly as standard architecture.

## Chi.Bio open-hardware bioreactor (2018)

- **id**: `chibio-bioreactor`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Steel et al., Oxford / Imperial
- **disclosure**: Steel, H.; Habgood, R.; Kelly, C.; Papachristodoulou, A. In situ characterisation and manipulation of biological systems with Chi.Bio. PLOS Biol. 2020, 18, e3000794. DOI: 10.1371/journal.pbio.3000794
- **ip status**: open-permissive
- **prior art notes**: Open-hardware bioreactor with integrated optical density measurement, fluorescence detection, peristaltic pumping, and feedback-controlled environment. ~$700 BOM. Anticipates: prosumer-grade closed-loop bioreactor for synthetic biology, with feedback control between sensors and actuators built into a benchtop form factor. Strong IP-clearing significance for the small-bioreactor space.

## eVOLVER multi-bioreactor evolution platform (2018)

- **id**: `evolver-klavins`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Khalil group, Boston University
- **disclosure**: Wong, B. G.; Mancuso, C. P.; Kiriakov, S.; Bashor, C. J.; Khalil, A. S. Precise, automated control of conditions for high-throughput growth of yeast and bacteria with eVOLVER. Nat. Biotechnol. 2018, 36, 614–623. DOI: 10.1038/nbt.4151
- **ip status**: open-permissive
- **prior art notes**: Open-hardware 16-vessel parallel bioreactor system with per-vessel temperature, OD, stirring, and feed control. Designed for laboratory directed-evolution and high-throughput growth experiments. Anticipates: massively-parallel addressable bioreactor architecture, open-source bioreactor scaling, and the experimental-evolution use case at academic-budget price points.

## Open replicator-style microfluidic pump (3D-printed peristaltic) (2019)

- **id**: `open-microfluidic-pump-pdf-replicator`
- **corpus**: open
- **device class**: pump-component
- **creator**: Various community contributions
- **disclosure**: Various community designs — derived from Pumpy / Pearce open-source pumps. github community contributions.
- **ip status**: open-permissive
- **prior art notes**: Sub-$50 entirely 3D-printed peristaltic pump community designs. Architectural extension of OpenFlexure / Pumpy concepts to all-3D-printed mechanical assemblies (no machined parts). Reference for the broader 'fully 3D-printed microfluidic instrumentation' trajectory enabled by hobbyist FDM 3D printers.

## OpenFlexure pump (open-hardware peristaltic) (2020)

- **id**: `open-flexure-pump`
- **corpus**: open
- **device class**: pump-component
- **creator**: various — Wijnen 2014 / OpenFlexure community
- **disclosure**: Wijnen, B.; Hunt, E. J.; Anzalone, G. C.; Pearce, J. M. Open-source syringe pump library. PLOS ONE 2014, 9, e107216. (And subsequent OpenFlexure peristaltic variants.)
- **ip status**: open-permissive
- **prior art notes**: Reference open-hardware peristaltic pump documented in PLOS ONE and subsequent open-source projects. Sub-$50 BOM for a working peristaltic pump usable for microfluidic applications including bioreactor feed and chip perfusion. Anticipates: extreme-low-cost peristaltic pump as open-hardware, reproducibly built by undergraduates or DIY-bio enthusiasts.
