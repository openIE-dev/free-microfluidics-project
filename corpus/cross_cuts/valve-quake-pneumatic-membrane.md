---
title: valve-quake-pneumatic-membrane
parent: Cross-cuts
layout: default
---

# Cross-cut: `valve-quake-pneumatic-membrane`

**25 corpus entries disclose this subsystem.**

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

## Olympus Medical fluidic endoscopy patent family (1995)

- **id**: `olympus-medical-fluidic-patents`
- **corpus**: private
- **device class**: other
- **creator**: Olympus Corporation
- **disclosure**: Olympus Medical Systems endoscope fluidic patents (Olympus Corporation 1990s-present)
- **ip status**: patented
- **prior art notes**: Olympus endoscope fluidic patent family covers integrated irrigation/aspiration fluidic manifold with cross-patient isolation. Anticipates claims directed to endoscope-channel multi-channel fluidic manifolds with cross-patient sterile isolation.

## Quake monolithic pneumatic membrane valve and pump (2000)

- **id**: `unger-2000-quake-monolithic-membrane-valve`
- **corpus**: academic
- **device class**: valve-component
- **creator**: Stephen Quake group, Caltech
- **disclosure**: Unger, M. A.; Chou, H.-P.; Thorsen, T.; Scherer, A.; Quake, S. R. Monolithic microfabricated valves and pumps by multilayer soft lithography. Science 2000, 288, 113–116. DOI: 10.1126/science.288.5463.113
- **ip status**: patented
- **prior art notes**: Foundational disclosure of pneumatically actuated elastomeric membrane valves built monolithically into a multilayer PDMS chip. By cyclically actuating three valves in series, a peristaltic pump is realized. This is the architectural ancestor of essentially every subsequent on-chip pneumatic valve and pump. Anticipates: pneumatic membrane valve (control channel + thin membrane + flow channel), peristaltic pumping by sequential valve actuation, large-scale integrated chip-scale fluidic circuits. Subsequent papers (Nordin 2017, Sanchez Noriega 2021) re-implement the same architecture in 3D-printed photopolymer.

## Quake Lab MLSI Monolithic Membrane Valve Patent Family (2000-04-07)

- **id**: `quake-patent-family-mlsi-monolithic-membrane-valve`
- **corpus**: academic
- **device class**: other
- **creator**: California Institute of Technology (Stephen Quake et al.)
- **disclosure**: US6408878 priority 2000-04-07; US6929030; US7144616; US7704698; US7837946 (Caltech)
- **ip status**: patented
- **prior art notes**: Caltech/Quake monolithic-membrane valve patent family. Anchors claims around: (a) two-layer PDMS device in which a flow channel is occluded by deflection of a thin elastomeric membrane via pressurization of an orthogonal control channel; (b) push-down geometry where the control channel sits above the flow channel; (c) push-up geometry where the control channel sits below; (d) integration of large arrays of such valves on a single monolithic device (microfluidic large-scale integration); (e) peristaltic pump architectures using three valves in series; (f) multiplexer trees that address N flow lines with log2(N) control lines. These claims are the licensing root that Fluidigm built its IFC controller, BioMark dynamic array, Access Array, C1 single-cell, and Helios CyTOF business on. Anticipates virtually any PDMS multilayer monolithic valve device unless distinguished by materials (non-PDMS), actuation (non-pneumatic), or geometry (non-membrane closure). Defensive importance: the underlying Unger 2000 paper (already in corpus as unger-2000-quake-monolithic-membrane-valve) is the academic disclosure; this entry is the patent-family disclosure that maps the asserted claim landscape. Earliest US priority is 2000-04-07. Estimated US expiry 2020-2025 depending on family member.

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

## Fluidigm Integrated Fluidic Circuit Controller Patent Family (2002)

- **id**: `fluidigm-patent-family-ifc-controller`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Fluidigm Corporation (now Standard BioTools)
- **disclosure**: US7307802; US7195670; US7691333; US7906072; US8163492 (Fluidigm Corporation, now Standard BioTools)
- **ip status**: patented
- **prior art notes**: Fluidigm patent family covering the IFC controller (the workhorse benchtop instrument for all Fluidigm chip products). Anchors claims around: (a) pneumatic manifold delivering individually-addressable pressurized control lines to a multilayer PDMS chip seated on a holder; (b) integrated thermal cycling stage; (c) optical readout integration with chip alignment; (d) sequential-loading protocols leveraging MLSI multiplexer trees. Built on the Caltech-licensed Quake MLSI valve patent family (quake-patent-family-mlsi-monolithic-membrane-valve). Anticipates pneumatically-actuated chip-controller benchtop instruments for elastomeric microfluidic chips. Expiry: 2022-2030 across family.

## Fluidigm Dynamic Array Integrated Fluidic Circuit (2003)

- **id**: `fluidigm-dynamic-array-ifc`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Fluidigm Corp. (now Standard BioTools)
- **disclosure**: Fluidigm Corp. (now Standard BioTools) Integrated Fluidic Circuit / Dynamic Array. https://www.standardbio.com/products/instruments-and-consumables and Fluidigm IFC patent family.
- **ip status**: patented
- **prior art notes**: Commercial implementation of Quake / Thorsen MLSI (microfluidic large-scale integration) for high-throughput qPCR, single-cell qPCR, and digital PCR. Anticipates: direct architectural lineage from Unger 2000 + Thorsen 2002 to commercial multi-thousand-well qPCR arrays. The corpus exists in part because of the IP positions Fluidigm built around this architecture.

## Quake Digital PCR Microfluidic Patent Family (2003-04-03)

- **id**: `quake-patent-family-digital-pcr-on-chip`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: California Institute of Technology / Stanford (Stephen Quake et al.)
- **disclosure**: US7459315 priority 2003-04-03; US8124032; US8252539 (Caltech / Stanford-derived inventors)
- **ip status**: patented
- **prior art notes**: Quake-group digital-PCR patent family covering on-chip partitioning of a nucleic-acid sample into a large array of independent reactors followed by amplification and Poisson-statistical absolute quantification. Anchors claims around: (a) MLSI valve isolation of an array of nL/pL reaction chambers; (b) loading dilute template such that chambers contain 0 or 1 target by Poisson distribution; (c) thermal cycling and end-point fluorescence readout per chamber; (d) absolute quantification by counting positive partitions. Different family from droplet-based ddPCR (RainDance/QuantaLife/Bio-Rad lineage) but co-anticipates the absolute-quantification claim space. Vogelstein-Kinzler 1999 (vogelstein-kinzler-1999-digital-pcr) is the conceptual prior art. This patent family fed Fluidigm BioMark digital-array chemistry. Expiry: family members 2023-2026.

## Fluidigm BioMark Dynamic Array Chemistry Patent Family (2004)

- **id**: `fluidigm-patent-family-biomark-dynamic-array`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Fluidigm Corporation (now Standard BioTools)
- **disclosure**: US7820427; US8420017; US8475743; US9663819 (Fluidigm Corporation)
- **ip status**: patented
- **prior art notes**: Fluidigm BioMark Dynamic Array patent family. Anchors claims around: (a) two-axis valve matrix combinatorially addressing N x M reaction chambers from N samples and M assays; (b) MLSI valves isolating each reaction chamber after combinatorial loading; (c) thermal cycling and end-point fluorescence per chamber; (d) specific 48.48 / 96.96 / 192.24 array geometries. Anticipates combinatorial qPCR microfluidic chips and high-multiplex digital PCR cartridges. Companion to existing fluidigm-dynamic-array-ifc entry. Expiry: 2024-2028 across family.

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

## Fluidigm C1 single-cell auto prep system (2012)

- **id**: `fluidigm-c1-singlecell`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Fluidigm Corp. (now Standard BioTools)
- **disclosure**: Fluidigm Corp. C1 Single-Cell Auto Prep System product launch 2012. Pollen, A. A. et al. Low-coverage single-cell mRNA sequencing reveals cellular heterogeneity and activated signaling pathways in developing cerebral cortex. Nat. Biotechnol. 2014, 32, 1053-1058. DOI: 10.1038/nbt.2967.
- **ip status**: patented
- **prior art notes**: Pre-droplet commercial single-cell platform: a multilayer PDMS IFC with hydrodynamic capture sites and Quake-valve-controlled reagent chambers performs lysis, reverse transcription, and pre-amplification for 96 (or 800) single cells in parallel. Anticipates: integrated-valve-array single-cell prep architectures; the predecessor approach to droplet-based single-cell prep, with much lower throughput but full-length cDNA. The Pollen 2014 paper (and dozens of similar single-cell papers in 2013-2016) all use the C1; this is the architectural anchor for any 'integrated single-cell mRNA prep on chip' claim before droplets dominated.

## Standard BioTools (formerly Fluidigm) C1 single-cell genomics IFC (2013)

- **id**: `standard-biotools-csg-fluidigm`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Fluidigm (now Standard BioTools)
- **disclosure**: Fluidigm Corp. C1 system (now Standard BioTools). Pollen et al. 2014 Nat. Biotechnol. 32, 1053–1058. DOI: 10.1038/nbt.2967
- **ip status**: patented
- **prior art notes**: Single-cell capture-and-amplify IFC: 96 chambers each receiving exactly one cell by hydrodynamic trap, then automated lysis, RT, and PCR per chamber for downstream sequencing. Architectural ancestor of all subsequent microfluidic-trap single-cell genomics, including 10x Chromium's droplet successor. Largely displaced by droplet platforms after 2015 because of cost-per-cell, but retains use in low-throughput high-fidelity work.

## Formulatrix Mantis and Tempest nanoliter dispensers (2013)

- **id**: `formulatrix-mantis-tempest`
- **corpus**: private
- **device class**: dispenser-pipettor
- **creator**: Formulatrix
- **disclosure**: Formulatrix Mantis liquid handler product literature. https://formulatrix.com/liquid-handling-systems/mantis-liquid-handler/. Tempest launch ~2017.
- **ip status**: patented
- **prior art notes**: Disposable-microfluidic-chip dispenser: each chip carries pneumatic diaphragm valves that meter and dispense nanoliter reagent volumes from off-chip reservoirs. Mantis is the lower-throughput single-channel system; Tempest is a 96-channel rack of identical metering primitives. Anticipates: the architectural pattern of putting the dispense metering primitive on a disposable consumable rather than on a fixed instrument syringe, which categorically eliminates carryover; the use of pneumatic diaphragm valves as the metering element in nanoliter dispensing; the chip-on-instrument architecture for low-volume reagent dispensing as an alternative to acoustic (Echo) or piezo (Mosquito) approaches.

## Emulate Inc. Organ-Chip platform (2014)

- **id**: `emulate-organ-on-chip-platform`
- **corpus**: private
- **device class**: organ-on-chip
- **creator**: Emulate Inc. (Donald Ingber / Wyss spinout)
- **disclosure**: Emulate Inc. (Wyss spinout) Organ-Chip platform; product literature. https://www.emulatebio.com
- **ip status**: patented
- **prior art notes**: Commercial organ-on-chip platform deriving from the Huh 2010 lung-on-chip disclosure. The Zoë instrument provides perfusion and stretch actuation to standard 'Bio-Kit' organ chips. Anticipates: standardized commercial organ-chip cartridge with paired perfusion + cyclic-stretch instrument, and the organ-chip-as-a-product category.

## nScrypt 3Dn-Tissue bioprinter (2014)

- **id**: `nscrypt-3dn-tissue`
- **corpus**: private
- **device class**: printer-tooling
- **creator**: nScrypt Inc.
- **disclosure**: nScrypt Inc. 3Dn-Tissue launch ~2014 (built on Microdispensing nFD technology, ca. 2002). https://www.nscrypt.com. Patent family: US7338613B2 (nScrypt; priority 2002 SmartPump).
- **ip status**: patented
- **prior art notes**: Discloses a high-precision dispense bioprinter built on the nScrypt SmartPump piezo-valve dispensing technology, capable of multi-material printing of cells, hydrogels, and conductive inks. Anticipates: piezo-valve-actuated multi-material bioprinters that combine biological and electronic inks in a single platform; 3Dn-Tissue-class bioprinters as the platform for combining bioprinting with on-construct sensor printing.

## Bhattacharjee 2016 3D-Printed Microfluidics Toolkit (2016-04)

- **id**: `bhattacharjee-2016-3d-printed-microfluidics`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Albert Folch lab (U Washington); Bhattacharjee N., Urrios A., Kang S.
- **disclosure**: Bhattacharjee N., Urrios A., Kang S., Folch A., 'The upcoming 3D-printing revolution in microfluidics', Lab on a Chip 16:1720-1742 (2016); doi:10.1039/C6LC00163G; companion review and design library
- **ip status**: open-permissive
- **prior art notes**: Discloses a comprehensive 3D-printed microfluidics design toolkit with free downloadable CAD files including: pressure-actuated membrane valves, T-junction droplet generators, herringbone mixers, and serpentine reactors all printable on commodity DLP-SLA printers using PEGDA-based resins. Specifically anticipates patents post-2016 claiming '3D-printed pneumatic membrane microvalves for microfluidic devices' and 'libraries of 3D-printable microfluidic components distributed as parametric CAD files.' Element-by-element discloses the membrane-deflection valve geometry achievable in stereolithography, the choice of biocompatible PEGDA resins, and the calibration of channel dimensions against printer pixel pitch.

## 3D-printed microfluidic valves and pumps (2017)

- **id**: `kong-2017-3d-printed-microfluidic-valves`
- **corpus**: academic
- **device class**: valve-component
- **creator**: MIT Media Lab / MIT Lincoln Lab
- **disclosure**: Kong, D. S.; Thorsen, T. A.; Babb, J.; Wick, S. T.; Gam, J. J.; Weiss, R.; Carr, P. A. Open-source, community-driven microfluidics with Metafluidics. Nat. Biotechnol. 2017, 35, 523–529. DOI: 10.1038/nbt.3873
- **ip status**: open-permissive
- **prior art notes**: Demonstrated 3D-printed pneumatic membrane valves on SLA-printed substrates, replacing PDMS soft-lithography Quake valves with directly-printed equivalents. Anticipates: 3D-printed pneumatic valve architecture and the broader trend of replacing soft-lithography with single-step 3D printing.

## Mathies/Quinn 2017 Microchip Capillary Electrophoresis for Mars Amino Acid Detection (2017)

- **id**: `mathies-quinn-2017-microchip-ce-mars-amino-acids`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Richard Mathies group (UC Berkeley) / Peter Willis (NASA JPL) / Maria Mora (NASA JPL) / Aaron Noell
- **disclosure**: Mora MF et al., 'Toward total automation of microfluidics for extraterrestrial in situ analysis,' Anal. Chem. 83:8636 (2011); Mora MF et al. (Mathies/Quinn group), 'Capillary electrophoresis amino acid sensitivity from a chip-based instrument,' Electrophoresis 38:2982 (2017), doi:10.1002/elps.201700110
- **ip status**: patented
- **prior art notes**: The Mathies/Quinn line of work is the most extensively-published academic flight-prototype for microfluidic life detection on Mars and icy moons. Element-by-element prior art: (a) the integration of programmable PDMS-on-glass membrane valves with on-chip CE separation for extraterrestrial sample analysis anticipates any patent claiming integrated sample-prep + electrophoretic-separation + LIF cartridges for planetary instruments; (b) the published parts-per-trillion sensitivity for fluorescamine-labeled amino acids in a portable / battery-powered instrument anticipates patents claiming similar sensitivity in handheld biosensors; (c) chiral separation as a biosignature-discrimination strategy on a microchip CE format anticipates any patent claiming D/L enantiomer microfluidic separation for biosignature detection. The Mora 2011/2017 papers also disclose the architectural pattern of a fully-automated 'Mars Organic Analyzer' (MOA) cartridge.

## Inscripta Onyx Digital Genome Engineering Platform (2019)

- **id**: `inscripta-onyx-genome-engineering`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Inscripta Inc.
- **disclosure**: Inscripta Onyx product launch 2019; Inscripta MAD7 nuclease publication: Garst et al., 'Genome-wide engineering of E. coli using CREATE,' Nat Biotechnol 35:48 (2017); Inscripta SEC filings; US patent US10,808,254B2 (Inscripta nucleic acid engineering systems)
- **ip status**: patented
- **prior art notes**: Discloses an integrated cassette that runs the full CREATE (CRISPR-Enabled Trackable genome Engineering) workflow: cells and editing oligo libraries loaded; on-cassette electroporation delivers libraries; outgrowth chambers with media routing; downstream selection and collection. Anticipates: closed-cassette automated bacterial/yeast genome-engineering workflows; on-cartridge electroporation followed by on-cartridge cell-growth in shared fluid path; the broader 'design-build-test in one box' microbial editing factory architecture. Element-by-element: oligo input + cell input + on-cassette electroporation + outgrowth chamber with feed/bleed + selection chamber + collection bag.

## Multi-resolution DLP-SLA for 2 µm microfluidic channels (2026-02-27)

- **id**: `miner-2026-multi-resolution-3d-printing-microfluidics`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Nordin / Woolley group, BYU
- **disclosure**: Miner, D. S.; Viglione, M. S.; Hooper, K.; Woolley, A. T.; Nordin, G. P. Fast multi-resolution 3D printing of microfluidics: enabling 2 µm channels and ultra-compact mixers. Microsyst. Nanoeng. 2026, 12, 66. DOI: 10.1038/s41378-026-01194-4
- **ip status**: public-domain
- **prior art notes**: Discloses true multi-resolution DLP-SLA in both XY and Z dimensions via dual optical engines (0.75 µm and 15 µm pixel pitch) and dual-UV-absorber resin (NPS + avobenzone) producing 2 µm and 20 µm penetration depths. Anticipates: multi-resolution-in-Z via dual-absorber resin chemistry tuned to two distinct LED spectra (365 nm and 405 nm), embedded high-resolution regions in lower-resolution bulk prints, sub-2-µm enclosed channels in a printable photopolymer, and a 17-nL on-chip diffusive mixer with ±2% uniformity. Patent claims asserting novelty over 'multi-wavelength resin chemistry for spatially-tailored DLP-SLA Z resolution' must address this disclosure.
