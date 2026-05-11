---
title: thermal-pcr-cycling
parent: Cross-cuts
layout: default
---

# Cross-cut: `thermal-pcr-cycling`

**34 corpus entries disclose this subsystem.**

Earliest disclosure: 1936

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Damkoehler Numbers Da_I, Da_II (1936)

- **id**: `damkohler-numbers-dimensionless-group`
- **corpus**: academic
- **device class**: other
- **creator**: Gerhard Damkoehler
- **disclosure**: Damkoehler, G. (1936). 'Einfluesse der Stroemung, Diffusion und des Waermeueberganges auf die Leistung von Reaktionsoefen.' Z. Elektrochem. 42(12): 846-862.
- **ip status**: public-domain
- **prior art notes**: Damkoehler numbers govern every continuous-flow microreactor: Da_I sets conversion as a function of flow rate; Da_II sets whether the reactor is reaction- or diffusion-limited. Anchors: (a) all flow-chemistry microreactor patents reciting residence-time control; (b) on-chip enzymatic-assay timing claims; (c) on-chip PCR amplification residence-time engineering; (d) heterogeneous catalysis microreactors. Any patent claim that recites 'tunable conversion via residence-time modulation' is anticipated by Damkoehler scaling.

## Silicon-based miniature PCR thermal cycler (Northrup 1993) (1993)

- **id**: `northrup-1993-silicon-pcr-microreactor`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Northrup group, Lawrence Livermore
- **disclosure**: Northrup, M. A.; Ching, M. T.; White, R. M.; Watson, R. T. DNA amplification with a microfabricated reaction chamber. Proc. Transducers '93, 1993, 924–926.
- **ip status**: patented
- **prior art notes**: The first demonstration of PCR in a silicon microfabricated reaction chamber with integrated heater. Predates Wittwer's commercial RapidCycler and Manz's continuous-flow PCR; the architectural ancestor of all subsequent silicon-microreactor PCR work. Among the foundational references in chip-format molecular diagnostics — disclosed five years before the µTAS-era PCR chip explosion.

## LightCycler real-time rapid PCR (Wittwer 1997) (1997)

- **id**: `wittwer-1997-rapid-cycler`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Wittwer group, University of Utah / Idaho Technology / Roche
- **disclosure**: Wittwer, C. T.; Herrmann, M. G.; Moss, A. A.; Rasmussen, R. P. Continuous fluorescence monitoring of rapid cycle DNA amplification. BioTechniques 1997, 22, 130–138. DOI: 10.2144/97221bi01
- **ip status**: patented
- **prior art notes**: Disclosed rapid-cycle real-time PCR with continuous fluorescence monitoring during thermal cycling, in glass capillary tubes for fast heat transfer. Architectural ancestor of every real-time PCR cartridge: the framing that PCR + real-time fluorescence reading enables quantitative analysis from a single closed reaction. The Wittwer-Idaho-Technology lineage produced the LightCycler (acquired by Roche 1997) and via the BioFire spinout (2003) the FilmArray cartridge. One of the most consequential academic-to-commercial transitions in molecular diagnostics.

## Continuous-flow PCR on chip (Kopp 1998) (1998)

- **id**: `quake-1997-pcr-on-chip`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Manz group, Imperial College
- **disclosure**: Kopp, M. U.; de Mello, A. J.; Manz, A. Chemical amplification: continuous-flow PCR on a chip. Science 1998, 280, 1046–1048. DOI: 10.1126/science.280.5366.1046
- **ip status**: patented
- **prior art notes**: Disclosed continuous-flow PCR on chip: serpentine glass channel passes through three temperature zones (denature/anneal/extend), with the number of cycles equal to the number of channel passes through each zone. Anticipates: spatial-temperature-zone PCR architecture as alternative to time-domain thermal cycling, and the entire continuous-flow PCR subfield. Architectural ancestor of many subsequent flow-PCR designs.

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

## MBARI Environmental Sample Processor (ESP) (2003)

- **id**: `mbari-esp-environmental-sample-processor`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Monterey Bay Aquarium Research Institute (MBARI) (Scholin lab) / McLane Research Laboratories (commercial 2G/3G ESP)
- **disclosure**: Scholin CA et al., 'The Environmental Sample Processor (ESP) — An autonomous robotic device for detecting microorganisms remotely using molecular probe technology,' Proc. OCEANS 2003: 1-7 (2003); Scholin CA et al., 'Remote detection of marine microbes, small invertebrates, harmful algae, and biotoxins using the Environmental Sample Processor (ESP),' Oceanography 22(2):158-167 (2009)
- **ip status**: patented
- **prior art notes**: The ESP is the canonical autonomous oceanographic microfluidic robotic sampler. Element-by-element prior art for: (a) automated puck-carousel architecture with integrated filtration + lysis + sandwich-hybridization assay + chemiluminescent readout in a long-deployment marine-robotic platform; (b) feedback-controlled adaptive sampling where the on-board assay result triggers subsequent sample collection (LRAUV+ESP plume tracking); (c) integration of ddPCR into a marine autonomous vehicle (3G ESP), which anticipates patents on autonomous in-situ qPCR/ddPCR cartridges for environmental monitoring; (d) the sealed puck format with pre-loaded dry/wet reagents stored at ocean depth for months anticipates patents on long-storage diagnostic cartridges in extreme environments. ESP is also the closest terrestrial analog to a planetary in-situ life detection cartridge.

## Quake Digital PCR Microfluidic Patent Family (2003-04-03)

- **id**: `quake-patent-family-digital-pcr-on-chip`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: California Institute of Technology / Stanford (Stephen Quake et al.)
- **disclosure**: US7459315 priority 2003-04-03; US8124032; US8252539 (Caltech / Stanford-derived inventors)
- **ip status**: patented
- **prior art notes**: Quake-group digital-PCR patent family covering on-chip partitioning of a nucleic-acid sample into a large array of independent reactors followed by amplification and Poisson-statistical absolute quantification. Anchors claims around: (a) MLSI valve isolation of an array of nL/pL reaction chambers; (b) loading dilute template such that chambers contain 0 or 1 target by Poisson distribution; (c) thermal cycling and end-point fluorescence readout per chamber; (d) absolute quantification by counting positive partitions. Different family from droplet-based ddPCR (RainDance/QuantaLife/Bio-Rad lineage) but co-anticipates the absolute-quantification claim space. Vogelstein-Kinzler 1999 (vogelstein-kinzler-1999-digital-pcr) is the conceptual prior art. This patent family fed Fluidigm BioMark digital-array chemistry. Expiry: family members 2023-2026.

## Cepheid GeneXpert cartridge (2004)

- **id**: `cepheid-genexpert-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Cepheid (Danaher subsidiary)
- **disclosure**: Cepheid GeneXpert system; FDA 510(k) K043510 (2004) and subsequent assay clearances.
- **ip status**: patented
- **prior art notes**: Discloses a disposable cartridge with a rotary valve sequencing reagents through a sample preparation pathway into an optical reaction tube for real-time PCR. Anticipates: rotary-valve / multi-port selector architecture for multi-reagent cartridges, optically interrogated reaction chamber within a closed disposable, and the GeneXpert-style sample-prep + amplification + detection integration that underlies most Cepheid POC products including the Xpert MTB/RIF tuberculosis test.

## Fluidigm BioMark Dynamic Array Chemistry Patent Family (2004)

- **id**: `fluidigm-patent-family-biomark-dynamic-array`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Fluidigm Corporation (now Standard BioTools)
- **disclosure**: US7820427; US8420017; US8475743; US9663819 (Fluidigm Corporation)
- **ip status**: patented
- **prior art notes**: Fluidigm BioMark Dynamic Array patent family. Anchors claims around: (a) two-axis valve matrix combinatorially addressing N x M reaction chambers from N samples and M assays; (b) MLSI valves isolating each reaction chamber after combinatorial loading; (c) thermal cycling and end-point fluorescence per chamber; (d) specific 48.48 / 96.96 / 192.24 array geometries. Anticipates combinatorial qPCR microfluidic chips and high-multiplex digital PCR cartridges. Companion to existing fluidigm-dynamic-array-ifc entry. Expiry: 2024-2028 across family.

## Field-deployable agricultural pathogen detection cartridges (Cady 2003 lineage) (2005)

- **id**: `cady-2003-agricultural-pathogen-cartridge`
- **corpus**: academic
- **device class**: point-of-care-cartridge
- **creator**: Various — Cady (Cornell) / Lampe lineage
- **disclosure**: Cady, N. C. et al. Real-time PCR detection of Listeria monocytogenes using an integrated microfluidic platform. Sens. Actuators B Chem. 2005, 107, 332–341. DOI: 10.1016/j.snb.2004.10.022
- **ip status**: patented
- **prior art notes**: Foundational disclosure of agricultural / food-pathogen detection on integrated microfluidic platform: Listeria monocytogenes detection from food matrix by integrated lyse-extract-amplify-detect cartridge. Anticipates: agricultural-context integrated-PCR-cartridge architecture, distinct from clinical cartridges by emphasizing food-matrix sample-prep upstream. Underlies subsequent commercial efforts by Neogen, 3M Petrifilm, and academic agricultural-pathogen-cartridge programs.

## BioFire FilmArray multiplex PCR cartridge (2008)

- **id**: `biofire-filmarray-multiplex-pcr-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: BioFire Diagnostics (Idaho Technology origin); BioMérieux subsidiary
- **disclosure**: Idaho Technology Inc. (now BioFire Diagnostics, BioMérieux). FilmArray system. FDA 510(k) clearances K103175 (2011) and subsequent panels.
- **ip status**: patented
- **prior art notes**: Discloses a single-use disposable cartridge integrating sample preparation, nucleic acid extraction, multiplex nested PCR, and array-based detection in a closed pouch format. Anticipates: blister-pack on-cartridge reagent storage, foil-piercing actuation, multilayer thermoplastic lamination as a fabrication path for point-of-care molecular diagnostics, integrated thermal cycling within a sealed pouch, and the architectural pattern of 'sample-in / answer-out' multiplex IVD cartridges. The dominant commercial implementation in syndromic panel testing.

## Neogen Atlas food pathogen detection cartridge (2008)

- **id**: `neogen-atlas-pathogen`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Neogen Corporation
- **disclosure**: Neogen Corporation Atlas / GeneQuence pathogen detection. https://www.neogen.com
- **ip status**: patented
- **prior art notes**: Major commercial food-pathogen detection platform: cartridge-format integrated sample prep + amplification + detection for Salmonella, Listeria, E. coli O157:H7, and other foodborne pathogens. The food-safety POC cartridge segment is dominated by Neogen, 3M Petrifilm, BioControl, and Hygiena — all with substantial cartridge-architecture patent estates.

## Roche cobas Liat point-of-care cartridge (2009)

- **id**: `roche-cobas-liat-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: IQuum (acquired by Roche 2014)
- **disclosure**: IQuum (later acquired by Roche) cobas Liat system. FDA 510(k) K123251 (2014) for influenza assay. https://diagnostics.roche.com/global/en/products/instruments/cobas-liat.html
- **ip status**: patented
- **prior art notes**: Disclosed a flexible-tube cartridge format with sequential compartments separated by external pinch valves, allowing reagent staging and PCR thermal cycling without rigid microfluidic channels. Anticipates: flex-tube-as-microfluidic-substrate, external-pinch-valve actuation as substitute for on-chip valves, and the architectural simplification of POC molecular diagnostics by eliminating injection-molded fluidic complexity.

## OpenPCR open-source thermal cycler (2010)

- **id**: `openpcr-thermal-cycler`
- **corpus**: open
- **device class**: flow-controller
- **creator**: OpenPCR (Chai Biotech founders)
- **disclosure**: OpenPCR project, Tito Jankowski / Josh Perfetto. https://openpcr.org
- **ip status**: open-permissive
- **prior art notes**: Open-source desktop thermal cycler ($600 BOM, $599 kit) with full schematics and firmware released under permissive license. Anticipates: open-hardware thermal cycler architecture, prosumer-grade molecular biology instrumentation outside institutional purchase channels, and the broader category of open-source life-science instruments. Predates Arduino-microbiology by a few years.

## Thermo Fisher TaqPath / Applied Biosystems QuantStudio cartridge (2010)

- **id**: `thermo-taqpath-cartridge`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Thermo Fisher Scientific (Applied Biosystems / Life Technologies)
- **disclosure**: Thermo Fisher Scientific TaqPath family and QuantStudio instruments. https://www.thermofisher.com
- **ip status**: patented
- **prior art notes**: High-throughput lab-format qPCR cartridges spanning 96-well, 384-well, and 7K Array Card formats, with TaqMan probe chemistry. Architecturally a successor to traditional PCR plates with lab-automation integration. Significant for the FDA-authorized COVID-19 TaqPath test which became the dominant US laboratory-format SARS-CoV-2 PCR.

## Hologic Panther / Panther Fusion Multiplex PCR Cartridge System (2012)

- **id**: `hologic-panther-fusion-cartridge`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Hologic / Gen-Probe
- **disclosure**: Hologic Panther launch 2012-04; Panther Fusion launch 2017-09; FDA 510(k) K112113 (Panther); K173494 (Fusion module)
- **ip status**: patented
- **prior art notes**: Discloses the Panther/Fusion fluidic architecture: random-access processing of single-use Aptima Target Capture tubes containing magnetic capture oligonucleotide-functionalized beads — the bead/capture-oligo hybridizes the target nucleic acid before any amplification, washing away interferents (e.g., for urine and vaginal swab matrices); released targets are transferred to amplification tubes for either TMA (Panther main module: chemiluminescent detection via hybridization protection assay HPA) or RT-PCR (Panther Fusion module: real-time fluorescent multiplex). Anticipates: true random-access molecular analyzers integrating target capture + amplification + detection in a continuous single-tube workflow; HPA dual-kinetic-assay chemiluminescence as a non-amplification-coupled detection alternative to fluorescence; architectural separation of TMA and PCR onto distinct modules sharing the same sample handler.

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

## GenMark ePlex cartridge (2014)

- **id**: `genmark-eplex-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: GenMark Diagnostics (acquired by Roche 2021)
- **disclosure**: GenMark Diagnostics (now Roche) ePlex system. FDA 510(k) K161312 and family. https://www.genmarkdx.com/eplex/
- **ip status**: patented
- **prior art notes**: Disclosed a multiplex molecular diagnostic cartridge integrating sample prep, PCR amplification, and electrochemical detection on a printed gold electrode array (eSensor technology). Anticipates: electrochemical-array detection as alternative to optical fluorescence in syndromic POC molecular diagnostics, and the architectural pattern of integrating eSensor-style detection within a self-contained cartridge.

## The ODIN DIY Genetic Engineering Kits (2015)

- **id**: `the-odin-diy-genetic-eng-kits`
- **corpus**: open
- **device class**: other
- **creator**: The ODIN (Josiah Zayner)
- **disclosure**: The ODIN founded 2015 by Josiah Zayner; first public DIY CRISPR kit released 2016; https://www.the-odin.com; documented in Zayner J., 'A Step-by-Step Guide to DIY CRISPR' (2016 e-book) and extensive press coverage (NYT, Wired, MIT Tech Review)
- **ip status**: open-permissive
- **prior art notes**: Discloses retail distribution of complete molecular-biology workflows to non-institutional users, including microfluidic-adjacent open hardware (PCR thermocycler, gel rig, mini-centrifuge) bundled with reagents and step-by-step protocols. The ODIN's open documentation of its kits' hardware (BOMs, schematics) and its written protocols are prior art against post-2016 'consumer molecular biology kit' patents and against many 'low-cost integrated PCR-and-gel cartridge' claims. Specifically anticipates: any patent claiming 'a consumer-grade integrated genetic engineering kit comprising thermocycling, electrophoresis, and reagent components.'

## Bento Bioworks Bento Lab portable PCR + electrophoresis (2016)

- **id**: `bento-bio-engineer`
- **corpus**: open
- **device class**: point-of-care-cartridge
- **creator**: Bento Bioworks Ltd.
- **disclosure**: Bento Bioworks Bento Lab. https://www.bento.bio
- **ip status**: open-permissive
- **prior art notes**: Portable laboratory in a briefcase combining centrifuge, PCR thermal cycler, and gel electrophoresis with open-source documentation. Sub-$2k consumer price point. Reference for the broader 'lab-in-a-box' movement bringing molecular biology infrastructure to citizen scientists, classrooms, and field-deployed contexts.

## ISS WetLab-2 Real-Time RT-PCR on Station (2016)

- **id**: `iss-wetlab-2-rt-pcr-on-station`
- **corpus**: open
- **device class**: lab-on-chip
- **creator**: NASA Ames Research Center / Cepheid (SmartCycler thermal block heritage) / BioRad (CFX-derived optics)
- **disclosure**: Parra M et al., 'Microgravity validation of a novel system for RNA isolation and multiplex quantitative real time PCR analysis of gene expression on the International Space Station,' PLOS ONE 12(9):e0183480 (2017), doi:10.1371/journal.pone.0183480; NASA WetLab-2 facility description, ISS Research Office (2016)
- **ip status**: open-permissive
- **prior art notes**: Discloses an end-to-end RNA-extraction + RT-qPCR cartridge architecture qualified for microgravity. Element-by-element prior art: (a) the closed-cartridge magnetic-bead RNA extraction protocol with no open-air liquid transfer steps anticipates patents claiming aerosol-free spaceflight or BSL-3 nucleic acid extraction cartridges; (b) the validation of paramagnetic-bead binding/wash kinetics in zero-G is published prior art against any patent claiming novel microgravity-compatible bead handling; (c) the integration of off-the-shelf SmartCycler-class Peltier modules with a custom reaction tube format anticipates retrofit spaceflight diagnostic cartridge concepts. Combined with iss-biomolecule-sequencer-minion below, WetLab-2 establishes the full sample-prep + amplification + sequencing chain in spaceflight prior art.

## Bento Lab Portable PCR + Centrifuge + Gel Workstation (2016-04)

- **id**: `bento-lab-portable-pcr-bento-bio`
- **corpus**: open
- **device class**: other
- **creator**: Bento Bioworks Ltd. (Wolfenden B., Boeing P.)
- **disclosure**: Bento Lab Kickstarter campaign launched April 2016 by Bento Bioworks Ltd. (London) — Bethan Wolfenden, Philipp Boeing; https://www.bento.bio; product first shipped 2017
- **ip status**: patented
- **prior art notes**: Existing corpus entry 'bento-bio-engineer' covers Bento at the brand level. This entry pins the original Bento Lab product as a specific, dated disclosure (April 2016 Kickstarter, with public BOM/teardowns subsequently published) of an integrated portable thermocycler+centrifuge+gel-electrophoresis workstation. Specifically anticipates: 'portable integrated molecular-biology workstation' patent claims that read on the combination of <3 kg form factor, integrated thermocycler with PCR-tube format, integrated centrifuge with PCR-tube/strip format, integrated horizontal gel-electrophoresis with built-in transilluminator, and smartphone-app-driven thermocycling programs. Discloses element-by-element each of these subsystems in their integrated single-enclosure architecture.

## Cepheid Xpress (rapid GeneXpert) cartridge (2017)

- **id**: `cepheid-xpress-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Cepheid (Danaher)
- **disclosure**: Cepheid Xpert Xpress family — rapid versions of the GeneXpert cartridge with reduced runtime via streamlined sample prep.
- **ip status**: patented
- **prior art notes**: Newer family of Cepheid GeneXpert cartridges optimized for sub-30-minute runtime: Xpert Xpress Flu/RSV, Xpert Xpress SARS-CoV-2, Xpert Xpress Strep A. Architecturally identical to original GeneXpert cartridge with optimized chemistry (faster amplification cycles, multiplexed assays).

## Abbott Alinity m Molecular Diagnostics Sample-to-Result Cartridge (2017)

- **id**: `abbott-alinity-m-molecular-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Abbott Laboratories (Abbott Molecular)
- **disclosure**: Abbott Alinity m CE-IVD launch 2018; FDA 510(k) K191601 (HBV viral load); product datasheet 2018-09
- **ip status**: patented
- **prior art notes**: Discloses a tip-and-vessel cartridge architecture for magnetic-bead nucleic-acid extraction integrated with on-board real-time PCR amplification: a disposable plastic tip aspirates sample, mixes with lysis buffer and silica-coated magnetic beads, and the bead pellet is washed and eluted in a thermally cycled microreactor instrumented with multiplex fluorescence detection. Anticipates: random-access viral load PCR with single-use extraction tips, eliminating cross-contamination of the analyzer fluid path; per-sample disposable amplification well used as the optical detection cuvette; pre-loaded reagent strip with foil-pierce sequencing. Distinct from Cepheid GeneXpert (corpus) in extraction modality (tip-suspended vs glass-fiber column) and from Roche Cobas Liat (corpus) in modular continuous queueing.

## Visby Medical PCR cartridge (2018)

- **id**: `visby-medical-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Visby Medical (formerly Click Diagnostics)
- **disclosure**: Visby Medical respiratory and STI tests. FDA 510(k) family. https://www.visbymedical.com
- **ip status**: patented
- **prior art notes**: Single-use, palm-sized PCR cartridge with integrated optical detection and battery power; the test result is read by visual inspection of color-coded LEDs without requiring an instrument. Architecturally distinguished from Lucira (isothermal LAMP) by using true PCR thermal cycling on disposable. Anticipates: instrument-free thermal-cycled PCR cartridge with embedded heater and battery, and the device-disposable-as-instrument architectural collapse.

## Open Bioeconomy Lab (2018)

- **id**: `open-bioeconomy-lab-africa`
- **corpus**: open
- **device class**: other
- **creator**: Open Bioeconomy Lab (Molloy J. et al.); Mboalab (Cameroon); Kumasi Hive (Ghana)
- **disclosure**: Open Bioeconomy Lab founded 2018 by Jenny Molloy (U Cambridge) with partners in Ghana and Cameroon; https://openbioeconomy.org; ReClone enzyme distribution network site https://reclone.org
- **ip status**: public-domain
- **prior art notes**: Discloses open-source release of molecular-biology enzymes and distributed-manufacturing protocols for low-resource settings. Relevance to the microfluidics commons: many of the released protocols are explicitly designed to be executed in low-cost open microfluidic / chromatography hardware, and OBL is the de-facto distribution backbone for many post-2020 DIY-bio reagent kits used in open microfluidic LAMP/PCR cartridges. Specifically anticipates: any patent claiming 'distributed manufacturing of molecular biology reagents at point-of-use in low-resource settings via open hardware purification stacks.'

## Tecan DreamPrep NGS Sample Prep (2018)

- **id**: `tecan-dreamprep-ngs`
- **corpus**: private
- **device class**: dispenser-pipettor
- **creator**: Tecan Group
- **disclosure**: Tecan DreamPrep NGS launch 2018; product brochure 1505-PB-1808-EN
- **ip status**: patented
- **prior art notes**: Discloses a pre-configured NGS-library-prep automation workflow on the Tecan Fluent platform, integrating SPRI magnetic-bead size selection with low-volume pipetting and thermal cycling for 96-sample throughput. Anticipates: pre-validated sequencing-library-prep automation workflows that pair Air Displacement Pipetting with magnetic-bead size selection; sub-10-uL library preparation at production scale.

## DnaNudge / NudgeBox Rapid Cartridge PCR System (2020-03)

- **id**: `dnanudge-rapid-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: DnaNudge Ltd. (Imperial College London spin-out)
- **disclosure**: Gibani MM et al. Lancet Microbe 1(7):e300-e307 2020 doi:10.1016/S2666-5247(20)30121-X (CovidNudge clinical evaluation); UK MHRA authorization
- **ip status**: patented
- **prior art notes**: Discloses a self-contained sample-to-answer PCR cartridge integrating swab-input, lysis, RT-PCR, and fluorescence detection. Originally a consumer DTC nutrigenomics product (NudgeBox at point of sale in supermarkets), repurposed for COVID-19. Anticipates: consumer-genomics sample-to-answer cartridges; supermarket point-of-sale DNA testing topology; reuse of consumer-genomics cartridge designs for infectious-disease detection.

## Camena Bioscience gSynth Enzymatic DNA Synthesis (2021)

- **id**: `camena-bioscience-gsynth`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Camena Bioscience Ltd.
- **disclosure**: Camena Bioscience product launch 2021; WO2019/166791 priority 2018
- **ip status**: patented
- **prior art notes**: Discloses an enzymatic gene-synthesis platform combining short pre-made oligonucleotide blocks with controlled in-vitro assembly under chip-scale fluidic delivery. Anticipates claims to hybrid block-and-extend synthesis architectures with on-platform thermocycling.

## Visby Medical Sexual Health Test Cartridge (2021-08)

- **id**: `visby-medical-sexual-health-test-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Visby Medical Inc.
- **disclosure**: Visby Medical FDA 510(k) K201013 cleared 2021-08-04; US10434511B2 priority 2014; expansion to OTC test FDA 2024
- **ip status**: patented
- **prior art notes**: Discloses a palm-sized disposable PCR cartridge integrating sample lysis, thermocycling, fluorescent detection, and visible result indication entirely within the consumable, with battery-powered electronics and no separate reader instrument. Anticipates: instrument-free PCR cartridges for STI detection where the disposable contains all hardware including LEDs, photodiodes, microcontroller, and battery; OTC molecular diagnostic form factors that fit the consumer-test point-of-purchase model. Anticipates claims to single-cartridge molecular tests where the consumable itself implements thermocycling and optical detection.

## Telesis Bio BioXp 9600 Benchtop DNA Synthesis (2022-02)

- **id**: `telesis-bioxp-9600-benchtop-synthesis`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Telesis Bio Inc. (formerly Codex DNA / SGI-DNA)
- **disclosure**: Telesis Bio (formerly Codex DNA) BioXp 9600 launch 2022-02-15; US10632445B2
- **ip status**: patented
- **prior art notes**: Discloses a benchtop fully-integrated cartridge that performs oligo pooling, Gibson assembly, error correction, amplification, and cloning entirely within a sealed disposable cartridge with on-board thermal cycling and fluidic delivery. Anticipates: end-to-end benchtop gene synthesis as a sealed-cartridge product; integration of complete Gibson-assembly workflow within a single point-of-use disposable; user-friendly DNA-on-demand platform architectures distinct from service bureau model. Anticipates claims to benchtop gene synthesizers that combine sealed reagent storage with multi-step enzymatic assembly inside a single cartridge.

## Environmental microbiome sample-to-sequencing cartridges (2024 academic) (2024)

- **id**: `environmental-microbiome-cartridge-2024`
- **corpus**: academic
- **device class**: point-of-care-cartridge
- **creator**: Various groups
- **disclosure**: Various 2024-2026 publications on environmental microbiome sample-to-sequencing integrated cartridges.
- **ip status**: patented
- **prior art notes**: Composite reference for emerging sample-to-sequencing microbiome cartridges: lyse-extract-amplify-sequence in integrated disposable cartridges for soil, water, and air microbiome surveillance. The combination of long-read sequencing (Oxford Nanopore MinION) with cartridge-format sample prep enables true field-deployable microbiome analysis.
