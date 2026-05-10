---
title: valve-quake-pneumatic-membrane
parent: Cross-cuts
layout: default
---

# Cross-cut: `valve-quake-pneumatic-membrane`

**14 corpus entries disclose this subsystem.**

Earliest disclosure: 1988

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Silicon piezoelectric micropump (Van Lintel 1988) (1988)

- **id**: `van-lintel-1988-silicon-piezo-pump`
- **corpus**: academic
- **device class**: pump-component
- **creator**: Van Lintel et al. (Univ. Twente)
- **disclosure**: Van Lintel, H. T. G.; van de Pol, F. C. M.; Bouwstra, S. A piezoelectric micropump based on micromachining of silicon. Sens. Actuators 1988, 15, 153–167. DOI: 10.1016/0250-6874(88)87005-7
- **ip status**: patented
- **prior art notes**: Foundational disclosure of silicon-MEMS piezoelectric reciprocating micropump: piezo-actuated diaphragm with passive check valves on inlet and outlet defines pump direction. Predates the µTAS-era explosion by 2 years; predates Quake-valve work by 12 years. Anticipates: silicon-piezo diaphragm as primitive micropump architecture, integrated check-valve micropump topology, and the entire reciprocating-diaphragm micropump category subsequently commercialized by Bartels mp6, TTP Ventus, and Lee Co micropumps.

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

## Microfluidic flow cytometer architectures (academic) (2002)

- **id**: `berkeley-cellium-flow-cytometer-2009`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: Quake group, Caltech
- **disclosure**: Fu, A. Y.; Spence, C.; Scherer, A.; Arnold, F. H.; Quake, S. R. A microfabricated fluorescence-activated cell sorter. Nat. Biotechnol. 1999, 17, 1109–1111. DOI: 10.1038/15095
- **ip status**: patented
- **prior art notes**: The first microfabricated FACS — fluorescence-activated cell sorter on chip. Demonstrated cell sorting at modest throughput (~10 cells/s) with optical interrogation and pneumatic actuation in PDMS. Anticipates: chip-FACS architecture, microfluidic flow cytometry, and the entire chip-based flow cytometry subfield subsequently expanded by Sony SP6800, BD Cytopeia, On-chip Sort, and others.

## Microfluidic protein crystallization in nanoliter chambers (2002)

- **id**: `quake-2003-microfluidic-protein-crystallization`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Quake group, Caltech
- **disclosure**: Hansen, C. L.; Skordalakes, E.; Berger, J. M.; Quake, S. R. A robust and scalable microfluidic metering method that allows protein crystal growth by free interface diffusion. Proc. Natl. Acad. Sci. USA 2002, 99, 16531–16536. DOI: 10.1073/pnas.262485199
- **ip status**: patented
- **prior art notes**: Disclosed PDMS-Quake-valve-based protein crystallization screening: hundreds of nanoliter-scale crystallization chambers in parallel using free-interface diffusion as the supersaturation mechanism. Architectural ancestor of Fluidigm Topaz protein crystallization chip — and of the broader nanoliter-screen / structural-biology automation that competes with Mosquito / Formulatrix dispensers.

## Fluidigm Dynamic Array Integrated Fluidic Circuit (2003)

- **id**: `fluidigm-dynamic-array-ifc`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Fluidigm Corp. (now Standard BioTools)
- **disclosure**: Fluidigm Corp. (now Standard BioTools) Integrated Fluidic Circuit / Dynamic Array. https://www.standardbio.com/products/instruments-and-consumables and Fluidigm IFC patent family.
- **ip status**: patented
- **prior art notes**: Commercial implementation of Quake / Thorsen MLSI (microfluidic large-scale integration) for high-throughput qPCR, single-cell qPCR, and digital PCR. Anticipates: direct architectural lineage from Unger 2000 + Thorsen 2002 to commercial multi-thousand-well qPCR arrays. The corpus exists in part because of the IP positions Fluidigm built around this architecture.

## Magnetic-bead microvalve and pump (2009)

- **id**: `leslie-2009-magnetic-bead-valve`
- **corpus**: academic
- **device class**: valve-component
- **creator**: Landers group, Virginia
- **disclosure**: Leslie, D. C.; Easley, C. J.; Seker, E.; Karlinsey, J. M.; Utz, M.; Begley, M. R.; Landers, J. P. Frequency-specific flow control in microfluidic circuits with passive elastomeric features. Nat. Phys. 2009, 5, 231–235. DOI: 10.1038/nphys1196
- **ip status**: patented
- **prior art notes**: Disclosed elastomeric features whose pressure-deformation response selectively passes flow at specific frequencies — frequency-specific microfluidic logic gates without active elements. Provides a pure-passive alternative to Quake valves for many on-chip control tasks. Anticipates: frequency-domain microfluidic logic, passive frequency filters as flow control, and architectural designs that eliminate external pneumatic control.

## Lung-on-a-chip (2010)

- **id**: `huh-2010-lung-on-chip`
- **corpus**: academic
- **device class**: organ-on-chip
- **creator**: Donald Ingber group, Wyss Institute
- **disclosure**: Huh, D.; Matthews, B. D.; Mammoto, A.; Montoya-Zavala, M.; Hsin, H. Y.; Ingber, D. E. Reconstituting organ-level lung functions on a chip. Science 2010, 328, 1662–1668. DOI: 10.1126/science.1188302
- **ip status**: patented
- **prior art notes**: The foundational organ-on-chip disclosure: lung alveolar-capillary interface reconstituted on a microfluidic chip with cyclic mechanical stretch. Anticipates: dual-channel architecture with intervening porous membrane, mechanical actuation of cell-bearing membranes via pneumatic chambers, perfused human cell co-culture with epithelial-endothelial interfaces. Spawned the Emulate Inc. commercial platform and the entire organ-on-chip field.

## Latching microfluidic valves and digital logic (2010)

- **id**: `weaver-2010-microfluidic-large-scale-integration`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Quake / Horowitz groups, Stanford
- **disclosure**: Weaver, J. A.; Melin, J.; Stark, D.; Quake, S. R.; Horowitz, M. A. Static control logic for microfluidic devices using pressure-gain valves. Nat. Phys. 2010, 6, 218–223. DOI: 10.1038/nphys1513
- **ip status**: patented
- **prior art notes**: Disclosed pressure-gain microfluidic valves enabling combinational logic on chip — microfluidic equivalents of CMOS logic gates. Demonstrates 8-bit shift register and ring oscillator implemented in PDMS. Anticipates: microfluidic-only digital control logic without external addressing electronics, and the architectural goal of a self-contained programmable chip without electronic peripherals.

## Fluidic rectifier and microfluidic memory (2010)

- **id**: `mosadegh-2010-fluidic-rectifier`
- **corpus**: academic
- **device class**: other
- **creator**: Takayama group, Michigan
- **disclosure**: Mosadegh, B.; Kuo, C.-H.; Tung, Y.-C.; Torisawa, Y.; Bersano-Begey, T.; Tavana, H.; Takayama, S. Integrated elastomeric components for autonomous regulation of sequential and oscillatory flow switching in microfluidic devices. Nat. Phys. 2010, 6, 433–437. DOI: 10.1038/nphys1637
- **ip status**: patented
- **prior art notes**: Disclosed elastomeric fluidic-rectifier and oscillator primitives implemented as monolithic-PDMS Quake-valve variants. Provides a microfluidic equivalent of the diode and the relaxation oscillator. Anticipates: monolithic elastomeric fluidic logic substrate, and autonomous-pumping microfluidic chips that operate without external pressure modulation.

## Standard BioTools (formerly Fluidigm) C1 single-cell genomics IFC (2013)

- **id**: `standard-biotools-csg-fluidigm`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Fluidigm (now Standard BioTools)
- **disclosure**: Fluidigm Corp. C1 system (now Standard BioTools). Pollen et al. 2014 Nat. Biotechnol. 32, 1053–1058. DOI: 10.1038/nbt.2967
- **ip status**: patented
- **prior art notes**: Single-cell capture-and-amplify IFC: 96 chambers each receiving exactly one cell by hydrodynamic trap, then automated lysis, RT, and PCR per chamber for downstream sequencing. Architectural ancestor of all subsequent microfluidic-trap single-cell genomics, including 10x Chromium's droplet successor. Largely displaced by droplet platforms after 2015 because of cost-per-cell, but retains use in low-throughput high-fidelity work.

## Emulate Inc. Organ-Chip platform (2014)

- **id**: `emulate-organ-on-chip-platform`
- **corpus**: private
- **device class**: organ-on-chip
- **creator**: Emulate Inc. (Donald Ingber / Wyss spinout)
- **disclosure**: Emulate Inc. (Wyss spinout) Organ-Chip platform; product literature. https://www.emulatebio.com
- **ip status**: patented
- **prior art notes**: Commercial organ-on-chip platform deriving from the Huh 2010 lung-on-chip disclosure. The Zoë instrument provides perfusion and stretch actuation to standard 'Bio-Kit' organ chips. Anticipates: standardized commercial organ-chip cartridge with paired perfusion + cyclic-stretch instrument, and the organ-chip-as-a-product category.

## 3D-printed microfluidic valves and pumps (2017)

- **id**: `kong-2017-3d-printed-microfluidic-valves`
- **corpus**: academic
- **device class**: valve-component
- **creator**: MIT Media Lab / MIT Lincoln Lab
- **disclosure**: Kong, D. S.; Thorsen, T. A.; Babb, J.; Wick, S. T.; Gam, J. J.; Weiss, R.; Carr, P. A. Open-source, community-driven microfluidics with Metafluidics. Nat. Biotechnol. 2017, 35, 523–529. DOI: 10.1038/nbt.3873
- **ip status**: open-permissive
- **prior art notes**: Demonstrated 3D-printed pneumatic membrane valves on SLA-printed substrates, replacing PDMS soft-lithography Quake valves with directly-printed equivalents. Anticipates: 3D-printed pneumatic valve architecture and the broader trend of replacing soft-lithography with single-step 3D printing.

## Multi-resolution DLP-SLA for 2 µm microfluidic channels (2026-02-27)

- **id**: `miner-2026-multi-resolution-3d-printing-microfluidics`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Nordin / Woolley group, BYU
- **disclosure**: Miner, D. S.; Viglione, M. S.; Hooper, K.; Woolley, A. T.; Nordin, G. P. Fast multi-resolution 3D printing of microfluidics: enabling 2 µm channels and ultra-compact mixers. Microsyst. Nanoeng. 2026, 12, 66. DOI: 10.1038/s41378-026-01194-4
- **ip status**: public-domain
- **prior art notes**: Discloses true multi-resolution DLP-SLA in both XY and Z dimensions via dual optical engines (0.75 µm and 15 µm pixel pitch) and dual-UV-absorber resin (NPS + avobenzone) producing 2 µm and 20 µm penetration depths. Anticipates: multi-resolution-in-Z via dual-absorber resin chemistry tuned to two distinct LED spectra (365 nm and 405 nm), embedded high-resolution regions in lower-resolution bulk prints, sub-2-µm enclosed channels in a printable photopolymer, and a 17-nL on-chip diffusive mixer with ±2% uniformity. Patent claims asserting novelty over 'multi-wavelength resin chemistry for spatially-tailored DLP-SLA Z resolution' must address this disclosure.
