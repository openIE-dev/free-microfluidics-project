---
title: valve-rotary-multiport
parent: Cross-cuts
layout: default
---

# Cross-cut: `valve-rotary-multiport`

**24 corpus entries disclose this subsystem.**

Earliest disclosure: 1976

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Viking 1/2 GCMS and Biology Package (1976)

- **id**: `viking-1976-gcms-biology-experiment`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: NASA / Martin Marietta / MIT (Biemann) / TRW (Biology Instrument)
- **disclosure**: Biemann K et al., 'Search for organic and volatile inorganic compounds in two surface samples from the Chryse Planitia region of Mars,' Science 194(4260):72-76 (1976), doi:10.1126/science.194.4260.72; Klein HP, 'The Viking biological investigation: General aspects,' J. Geophys. Res. 82(28):4677-4680 (1977)
- **ip status**: public-domain
- **prior art notes**: Discloses the architectural pattern of a planetary lander instrument that ingests bulk regolith, partitions it across multiple sealed reaction chambers, perfuses each with a different reagent (water/14C-labeled organics/13CO2 + light), and reads out via three orthogonal detection chains (mass spectrometer, beta scintillator, gas chromatograph thermal conductivity). For 102/103 anticipation purposes this is the founding flight precedent for: (a) integrated regolith-to-GCMS pyrolyzer with sealed sample magazines and oven-thermal-cycling, (b) a multi-modal life detection cartridge concept where one physical sample is interrogated by metabolic, isotope-labeling, and gas-evolution assays in parallel, and (c) the use of Curie-point pyrolysis to volatilize organics for downstream chromatographic separation. Anticipates virtually any later 'in-situ astrobiology cartridge' claim that recites multiple parallel reaction wells with independent reagent injection and orthogonal readouts (e.g., contemporary ELSAH/HOLD/MICA concepts). The Labeled Release positive (chiral-asymmetric heat-killable signal) remains a touchstone for any patent claiming life-detection by metabolic 14C release.

## Inpeco FlexLab Pre-Analytical Sample Transport Track (2003)

- **id**: `inpeco-flexlab-preanalytical-track`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Inpeco SA
- **disclosure**: Inpeco FlexLab product launch 2003 (formerly Bracco Diagnostics laboratory automation); patent family WO2003079030 et seq.
- **ip status**: patented
- **prior art notes**: Discloses pre-analytical sample-handling automation as a microfluidic system at the macro (mL) scale: each patient sample tube is transported individually on a puck through a sequence of modular processing stations; the aliquoter module performs sub-mL precision pipettor metering of plasma/serum into daughter tubes destined for different analyzers, and is microfluidic (sub-mL precision dispensing under primary-tube-derived sample volume budget) at the limit. Anticipates: lab automation as a 'macro-microfluidic' sample-routing problem requiring per-tube identification + per-tube routing + per-tube metered dispensing; the Inpeco architecture (open-vendor track) competes with closed-vendor tracks (Roche cobas connection module, Abbott Accelerator a3600, Siemens Aptio Automation). Foundational for the >$2B/yr lab automation market and for understanding the fluidic-engineering boundary between pre-analytical (macro, tube-level) and analytical (micro, cuvette-level) operations.

## MBARI Environmental Sample Processor (ESP) (2003)

- **id**: `mbari-esp-environmental-sample-processor`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Monterey Bay Aquarium Research Institute (MBARI) (Scholin lab) / McLane Research Laboratories (commercial 2G/3G ESP)
- **disclosure**: Scholin CA et al., 'The Environmental Sample Processor (ESP) — An autonomous robotic device for detecting microorganisms remotely using molecular probe technology,' Proc. OCEANS 2003: 1-7 (2003); Scholin CA et al., 'Remote detection of marine microbes, small invertebrates, harmful algae, and biotoxins using the Environmental Sample Processor (ESP),' Oceanography 22(2):158-167 (2009)
- **ip status**: patented
- **prior art notes**: The ESP is the canonical autonomous oceanographic microfluidic robotic sampler. Element-by-element prior art for: (a) automated puck-carousel architecture with integrated filtration + lysis + sandwich-hybridization assay + chemiluminescent readout in a long-deployment marine-robotic platform; (b) feedback-controlled adaptive sampling where the on-board assay result triggers subsequent sample collection (LRAUV+ESP plume tracking); (c) integration of ddPCR into a marine autonomous vehicle (3G ESP), which anticipates patents on autonomous in-situ qPCR/ddPCR cartridges for environmental monitoring; (d) the sealed puck format with pre-loaded dry/wet reagents stored at ocean depth for months anticipates patents on long-storage diagnostic cartridges in extreme environments. ESP is also the closest terrestrial analog to a planetary in-situ life detection cartridge.

## Cepheid GeneXpert cartridge (2004)

- **id**: `cepheid-genexpert-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Cepheid (Danaher subsidiary)
- **disclosure**: Cepheid GeneXpert system; FDA 510(k) K043510 (2004) and subsequent assay clearances.
- **ip status**: patented
- **prior art notes**: Discloses a disposable cartridge with a rotary valve sequencing reagents through a sample preparation pathway into an optical reaction tube for real-time PCR. Anticipates: rotary-valve / multi-port selector architecture for multi-reagent cartridges, optically interrogated reaction chamber within a closed disposable, and the GeneXpert-style sample-prep + amplification + detection integration that underlies most Cepheid POC products including the Xpert MTB/RIF tuberculosis test.

## Cytiva ÄKTA ready single-use chromatography skid (2009)

- **id**: `cytiva-akta-ready`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Cytiva (Danaher; formerly GE Healthcare)
- **disclosure**: GE Healthcare (now Cytiva) ÄKTA ready launch 2009. Cytiva Application Note 28-9408-25 AB. Underlying single-use flow-path patent family: US8221629B2 (GE Healthcare; priority 2007).
- **ip status**: patented
- **prior art notes**: Discloses a single-use chromatography skid in which the entire wetted flow path (tubing, valves, sensors, filters) is supplied as a pre-assembled gamma-irradiated disposable, eliminating clean-in-place validation between batches. Anticipates: (a) fully single-use chromatography skids as a category, including for CGT viral-vector downstream processing; (b) integration of disposable in-line UV, conductivity, and pH sensors into the chromatography flow path; (c) modular interchangeability between disposable flow paths and pre-packed chromatography columns. The single-use skid pattern is the dominant downstream bioprocessing architecture for new-build AAV and lentivirus manufacturing facilities.

## Sartorius BioSMB continuous multi-column chromatography (2010)

- **id**: `sartorius-biosmb-continuous-chromatography`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Sartorius / Pall (formerly Tarpon Biosystems)
- **disclosure**: Tarpon Biosystems (acquired by Pall 2015; subsequently part of Sartorius portfolio via Danaher BioPharma divestment) BioSMB launch 2010. Bisschops, M. et al. Single-use, continuous-countercurrent, multicolumn chromatography. BioProcess Int. 2009. Patent family: US8057694B2 (Tarpon Biosystems; priority 2008).
- **ip status**: patented
- **prior art notes**: Discloses a multi-column simulated-moving-bed continuous chromatography platform using a single-use disposable diaphragm-valve manifold rather than traditional metal rotary SMB valves. Anticipates: single-use disposable valve manifolds for continuous chromatography; SMB continuous Protein A capture as a CGT/mAb downstream architecture; multi-column countercurrent chromatography integrated with single-use bioprocess trains.

## Tecan Cavro MagniFlex Multi-Channel Pipettor Block (2010)

- **id**: `tecan-cavro-magni-flex-pipettor-block`
- **corpus**: private
- **device class**: dispenser-pipettor
- **creator**: Tecan Group / Cavro Scientific Instruments
- **disclosure**: Tecan Cavro MagniFlex product launch 2010; Cavro Centris syringe pump 2015; widely OEM'd into clinical analyzers and life-science liquid handlers
- **ip status**: patented
- **prior art notes**: Discloses a modular multi-channel precision syringe pipettor block — the OEM fluidic primitive embedded in dozens of commercial clinical and life-science analyzers (including many entries in this corpus expansion: Atellica, Alinity, ACL TOP, Phadia, etc.). The pipettor block integrates: stepper-motor-driven plunger arrays with closed-loop encoder feedback; ceramic rotary distribution valves switching between aspirate/dispense ports; on-board pressure-sensor liquid-level detection; modular 8/12/16/24/96 channel scaling. Anticipates: the standard architecture for sub-µL clinical-grade pipetting that underlies the central-lab analyzer ecosystem; the ceramic-valve + stainless-syringe + stepper-leadscrew triplet as the durability-and-precision tradeoff for high-cycle (>10^7 cycle lifetime) analyzer service. Important commons disclosure because most published analyzer patents discuss assay flow but elide the metering subsystem; this entry establishes the metering primitive as prior art so that downstream synthetic-biology / open-microfluidics platforms can adopt equivalent designs without infringement risk.

## MSL Sample Analysis at Mars (SAM) Wet Chemistry Cell with MTBSTFA Derivatization (2012)

- **id**: `msl-sam-wet-chemistry-cell`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: NASA Goddard Space Flight Center / Honeybee Robotics / GSFC SAM team (P. Mahaffy PI)
- **disclosure**: Mahaffy PR et al., 'The Sample Analysis at Mars Investigation and Instrument Suite,' Space Science Reviews 170:401-478 (2012), doi:10.1007/s11214-012-9879-z; Glavin DP et al., 'Evidence for perchlorates and the origin of chlorinated hydrocarbons detected by SAM at the Rocknest aeolian deposit in Gale Crater,' JGR Planets 118:1955-1973 (2013)
- **ip status**: public-domain
- **prior art notes**: Discloses a sealed reagent-cup architecture for in-situ wet chemistry on a planetary surface: a metal cup with crimped foil seal containing premixed MTBSTFA/DMF derivatization reagent at flight-storage temperature; the cup is mechanically pierced (foil-pierce actuation analogous to terrestrial blister-pack diagnostics), the regolith aliquot is dropped in, and the cup is heated stepwise to release derivatized analytes into the GCMS gas train. For 102/103 anticipation: (a) the foil-pierce + sealed-reagent + thermal-release architecture anticipates any patent claiming a single-use derivatization cartridge for sample-prep before MS, (b) the use of MTBSTFA specifically for in-situ silylation of amino acids/carboxylic acids in the presence of perchlorate oxidizers anticipates Mars/Europa/Enceladus life-detection cartridges that propose perchlorate-tolerant derivatization, and (c) the carousel architecture with mixed wet-chem and pyrolysis-only cups anticipates multi-modal sample-prep cartridges. The post-flight realization that perchlorate combustion was destroying organics during pyrolysis (Glavin 2013) is itself prior art against any claim that perchlorate-mitigation derivatization is novel for astrobiology applications.

## Tecan Fluent automation workstation with Cavro syringe pumps (2014)

- **id**: `tecan-fluent-cavro`
- **corpus**: private
- **device class**: dispenser-pipettor
- **creator**: Tecan Group
- **disclosure**: Tecan Fluent automation workstation product launch 2014. https://www.tecan.com/fluent-automation-workstation. Cavro syringe pump (Tecan subsidiary) datasheets.
- **ip status**: patented
- **prior art notes**: Modular liquid-handling workstation built around Tecan-owned Cavro precision syringe pumps. Cavro pumps are themselves a load-bearing piece of microfluidic prior art: glass-barrel high-resolution syringe pumps with multi-port distribution valves, used by hundreds of OEM instruments for sub-µL precision dispensing. The Fluent integrates Cavro pumps with multi-channel pipetting heads and supports microfluidic chip add-ons. Anticipates: modular automation platforms integrating precision syringe pumps with multi-channel air-displacement heads; the OEM ecosystem of Cavro-pumped instruments (used inside e.g. Roche, BD, Qiagen analyzers).

## Cytiva Sefia S-2000 cell processing system (2015)

- **id**: `cytiva-sefia`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Cytiva (Danaher) / Biosafe SA
- **disclosure**: Cytiva (formerly GE Healthcare; technology originally from Biosafe SA, acquired 2016). Sefia S-2000 product launch 2015. https://www.cytivalifesciences.com/en/us/shop/cell-therapy/instruments/sefia-s-2000-cell-processing-system. Underlying Sepax patent family: US7311849B2 (Biosafe SA; priority 2002).
- **ip status**: patented
- **prior art notes**: Discloses an automated closed-system cell-processing platform built around a single-use centrifugal separation chamber. The chamber spins on a vertical axis while inlet/outlet ports remain stationary via a rotary fluidic interface; cells are concentrated, washed, and reformulated in successive scripted cycles. Anticipates: (a) closed centrifugal-bowl architecture for CGT washing and formulation steps, especially as an interoperable upstream-downstream module in mixed-vendor CAR-T workflows; (b) rotary fluidic-interface valving for connecting stationary tubing to a spinning processing chamber; (c) script-driven multi-step cell processing in a barcode-tracked single-use kit. The Sefia kit is the de facto standard wash/concentrate step in many academic and commercial CAR-T lines including Kymriah and Yescarta.

## ExoMars Rosalind Franklin MOMA (Mars Organic Molecule Analyser) (2017)

- **id**: `exomars-moma-pyr-gcms-ldms`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Max Planck Institute for Solar System Research (MPS) / NASA GSFC / LISA / CNES / ESA / Thales Alenia Space
- **disclosure**: Goesmann F et al., 'The Mars Organic Molecule Analyzer (MOMA) Instrument: Characterization of Organic Material in Martian Sediments,' Astrobiology 17(6-7):655-685 (2017), doi:10.1089/ast.2016.1551
- **ip status**: public-domain
- **prior art notes**: Discloses a hybrid pyrolysis/derivatization/laser-desorption mass-spec instrument with a 32-cell sealed-cup carousel architecture as in-situ sample prep. Element-by-element disclosure: (a) the dual-front-end design (thermal pyrolysis path + UV-LDI path sharing a single ion trap) anticipates patents claiming dual-mode MS sample introduction for planetary life detection; (b) the chiral-column GC train specifically targeting amino-acid enantiomer ratios as a life-detection signature anticipates terrestrial commercial chiral-LC/GC cartridges marketed for biosignature discrimination; (c) the 2-meter subsurface drill aliquot pathway with sealed transfer to a sample carousel anticipates concepts for Europa Lander / Enceladus subsurface sample acquisition; (d) the perchlorate-bypassing LDI ionization mode anticipates any patent claiming non-thermal direct laser ionization for Mars/icy-moon refractory organics. MOMA is the European/American sister architecture to SAM and the most current public-domain disclosure of an integrated pyr-GCMS-LDMS planetary cartridge.

## Molecular Assemblies FAMS Enzymatic DNA Synthesis (2018)

- **id**: `molecular-assemblies-fams-synthesis`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Molecular Assemblies Inc.
- **disclosure**: Molecular Assemblies press release 2018; US10683537B2 priority 2017; Hyman & Efcavitch foundational publications
- **ip status**: patented
- **prior art notes**: Discloses an aqueous enzymatic DNA synthesis system designed around modular fluidic cassettes and a cleavable-terminator nucleotide chemistry distinct from DNA Script and Ansa approaches. Anticipates: variant enzymatic-synthesis chemistries deployed via modular fluidic cartridges with vendor-independent reagent delivery; positioning for DNA-data-storage industrial throughput. Useful as 102 art against claims that conflate cassette modularity with chemistry-specific architecture.

## Microsoft Project Silica + DNA Storage Research Devices (2019-03)

- **id**: `microsoft-dna-storage-research-device`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Microsoft Research + University of Washington Molecular Information Systems Lab
- **disclosure**: Takahashi et al., Sci Rep 9:4998 (2019) doi:10.1038/s41598-019-41228-8 (first end-to-end automated DNA storage demonstration, Microsoft Research); Newman et al., bioRxiv 2019
- **ip status**: patented
- **prior art notes**: Discloses an end-to-end automated DNA-storage platform integrating commercial column synthesis, microfluidic pooling and storage, and Oxford Nanopore read-out, with software encoding/decoding loops closing the cycle. Anticipates: end-to-end DNA storage system architectures that integrate commodity write and read components rather than custom synthesis chemistry; demonstration of practical write-store-read cycles measurable in hours. Useful as 102 prior art for any system claim that does not specifically tie value to a custom write or read chemistry.

## Bruker CellScape (Canopy Biosciences) (2020)

- **id**: `bruker-cellscape-spatial-proteomics`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Bruker Cellular Analysis (formerly Canopy Biosciences)
- **disclosure**: Canopy Biosciences product launch 2020; Bruker acquisition of Canopy Bio 2020-08-31; Hennig et al., Cytometry A 75A:362 (2009), doi:10.1002/cyto.a.20693 (ChipCytometry foundational paper)
- **ip status**: patented
- **prior art notes**: Discloses a sealed plastic flow chip enclosing a tissue section, with integrated fluidic ports for cyclic antibody delivery and bleaching between cycles. Anticipates: ChipCytometry architecture combining a tissue-stage flow chamber with non-destructive iterative photobleaching to deplete fluorescence between cycles (vs chemical stripping in Lunaphore COMET, DNA-removal in CODEX, or laser ablation in MIBI). Anticipates claims to single-chip multiplex immunofluorescence in which the tissue is preserved as a citable physical sample.

## DNA Script SYNTAX Enzymatic DNA Synthesizer (2020)

- **id**: `dna-script-syntax-enzymatic-synthesis`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: DNA Script SAS
- **disclosure**: DNA Script SYNTAX product launch 2020-06-30; Palluk et al., Nat Biotechnol 36:645 (2018) doi:10.1038/nbt.4173; US11236377B2
- **ip status**: patented
- **prior art notes**: Discloses a benchtop microfluidic platform for enzymatic DNA synthesis using engineered TdT-nucleotide conjugates as reversible terminators, with aqueous reagent cycling delivered through a 96-well cartridge. Anticipates: chip-scale enzymatic DNA synthesis architectures that displace phosphoramidite chemistry; integration of tethered-terminator nucleotides with on-cartridge wash and deprotection cycles; benchtop-scale fluidic manifolds for parallel oligo synthesis without organic-waste handling. Anticipates claims to enzymatic synthesis platforms that pair TdT-conjugate nucleotides with aqueous flow cycling.

## Ribbon Biolabs Long DNA Synthesis Platform (2020)

- **id**: `ribbon-biolabs-rna-ligation-synthesis`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Ribbon Biolabs GmbH
- **disclosure**: Ribbon Biolabs Series A press release 2021-09; WO2020100640A1 priority 2018
- **ip status**: patented
- **prior art notes**: Discloses a long-DNA synthesis platform that constructs gene-length sequences by enzymatic ligation of pre-synthesized trimer DNA blocks under controlled fluidic conditions. Anticipates: alternative architectures to per-base synthesis that combine block-libraries with on-instrument fluidic ligation; benchtop synthesis platforms that target >10 kb DNA without PCR. Prior art for claims to ligation-based gene synthesis automated through chip-scale fluidics.

## Lunaphore COMET (2021)

- **id**: `lunaphore-comet-spatial-proteomics`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Lunaphore Technologies SA (acquired by Bio-Techne 2023)
- **disclosure**: Lunaphore COMET product launch 2021; Migliozzi et al., Microsystems & Nanoengineering 5:59 (2019), doi:10.1038/s41378-019-0104-z (precursor LabSat technology); US10761093B2
- **ip status**: patented
- **prior art notes**: Discloses a microfluidic tissue processor that places a thin laminar-flow chamber directly over a glass slide, enabling rapid antibody delivery, washing, and fluorophore quenching cycles in situ on FFPE tissue. Anticipates: microfluidic acceleration of multiplex immunofluorescence by replacing diffusion-limited static incubation with convective laminar exchange; integration of buffer-storage, switching valves, and waste handling for unattended multi-day cycling. Anticipates claims to spatial proteomics systems that combine off-chip imaging with on-chip microfluidic staining/elution cycles, distinguishing from CODEX/PhenoCycler (DNA-barcoded antibody pool) and MIBI (mass-spectrometry imaging) approaches.

## Ansa Biotechnologies Enzymatic DNA Synthesis Platform (2023-06)

- **id**: `ansa-biotechnologies-enzymatic-synthesis`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Ansa Biotechnologies Inc.
- **disclosure**: Ansa Biotechnologies announcement 2023-06-29 of synthesizing world-record 1005 nt enzymatic-only oligo; press release; US11332757B2
- **ip status**: patented
- **prior art notes**: Discloses an enzymatic synthesis platform that pushes oligo length past the historical ~200 nt phosphoramidite barrier through engineered TdT activity and refined fluidic cycling, demonstrating 1005 nt single-oligo synthesis. Anticipates: long enzymatic-oligo synthesis processes integrated with chip-scale fluidic cycling; chemistries with cleavable nucleotides that approach gene-length single-pass synthesis. Useful prior art against claims to enzymatic synthesis platforms that achieve >500 nt single-pass length.

## Resolve Bioscience Molecular Cartography Pro (2024)

- **id**: `resolve-bioscience-molecular-cartography-pro`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Resolve Biosciences GmbH
- **disclosure**: Resolve Bioscience product update 2024; technical brief MC-Pro-001; original MC platform paper Groiss et al., bioRxiv 2021.10.20.464988
- **ip status**: patented
- **prior art notes**: Discloses platform extension of single-molecule FISH spatial transcriptomics with increased panel size and slide footprint, on the same fluidic delivery architecture. Anticipates claims to sub-100 nm lateral resolution spatial transcriptomics through iterative smFISH delivered by on-instrument microfluidics, distinct from amplification-based approaches (Xenium) or sequencing-by-hybridization (CosMx).

## Akoya CODEX Athena (Imaging Bay Update) (2024)

- **id**: `akoya-codex-athena-cytassist-2024`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Akoya Biosciences Inc.
- **disclosure**: Akoya Biosciences press release 2024; PhenoCycler-Fusion product update brief
- **ip status**: patented
- **prior art notes**: Discloses an additional fluidics module (Athena) that off-loads buffer management from the imaging instrument, enabling continuous multi-day cycling. Anticipates split-architecture multiplex-IF systems with separate imaging and fluidic-management modules.

## NanoString CosMx Whole Transcriptome Atlas (WTA) (2024-01)

- **id**: `nanostring-cosmx-wta-2024`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: NanoString Technologies (Bruker Spatial Biology since 2024-05)
- **disclosure**: NanoString/Bruker product launch CosMx WTA, JPM Conference 2024-01; SP-1108 datasheet rev A; AGBT 2024 abstract
- **ip status**: patented
- **prior art notes**: Discloses scaling of CosMx in-situ multiplex from ~1000-plex panels to ~18000-plex whole transcriptome through extended cycling of barcoded oligo reporters delivered by an on-instrument microfluidic system. Anticipates: on-instrument fluidic delivery sequences that perform N>16 hybridization-image-strip cycles on a single mounted slide, with microfluidic reagent storage/manifold and per-slide flowcell sealing; combinatorial barcoding scheme for ~18k targets within manageable optical-readout cycles. Specifically anticipates claims to single-instrument WTA spatial transcriptomics by sequential hybridization (vs SBS-based Xenium or sequencing-by-ligation Visium HD).

## Vizgen MERSCOPE Ultra (2024-04)

- **id**: `vizgen-merscope-ultra`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Vizgen Inc.
- **disclosure**: Vizgen press release 2024-04-15 'MERSCOPE Ultra'; AGBT 2024 abstract; product datasheet SD-0009 rev B
- **ip status**: patented
- **prior art notes**: Extends MERSCOPE platform with larger flowcell footprint and improved encoding chemistry that reduces total fluidic cycles. Anticipates: scaling of MERFISH-based spatial transcriptomics to >0.5 cm^2 tissue per slide using on-instrument microfluidic delivery, and reduced-round encoding schemes compatible with the same imaging hardware. Anticipates claims to high-throughput in-situ-hybridization platforms that combine optical multiplexing with progressively longer panel sizes through chemistry rather than instrument changes.

## 10x Genomics Xenium Prime 5K (2024-10)

- **id**: `10x-xenium-prime-5k`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: 10x Genomics Inc.
- **disclosure**: 10x Genomics Xenium Prime launch 2024-10-23; Xenium Prime user guide CG000760
- **ip status**: patented
- **prior art notes**: Discloses scaling of in-situ sequencing-by-ligation spatial transcriptomics to ~5000-gene panels through extended encoding (more bits per cycle, more cycles) on the unchanged Xenium Analyzer microfluidic platform. Anticipates: panel-scaling-by-chemistry on rolling-circle-amplification ISS platforms; combinatorial barcoding schemes spanning ~5000 targets within practical optical-cycle counts; integration of optional add-on probe panels delivered through the same microfluidic cartridge. Useful as prior art against claims that conflate panel size with hardware redesign.

## Element Biosciences AVITI Cloudbreak (Long-Read) (2024-10)

- **id**: `element-biosciences-aviti-cloudbreak`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Element Biosciences Inc.
- **disclosure**: Element Biosciences press release 2024-10-22; AGBT 2024 'Cloudbreak' presentation; product datasheet EL-DOC-00185
- **ip status**: patented
- **prior art notes**: Discloses chemistry to extend the effective read length of polony sequencing by maintaining physical clustering of related fragments on the same surface region (linked-read approach), then assembling locally during base-calling. Anticipates: long-read sequencing achieved through surface-chemistry-based linkage rather than dedicated long-read instrumentation; reuse of short-read flowcell hardware for >200 bp contiguous reads via spatial linkage. Anticipates claims to long-read methods that depend on surface arrangement and sliding-window assembly within a single SBS flowcell.
