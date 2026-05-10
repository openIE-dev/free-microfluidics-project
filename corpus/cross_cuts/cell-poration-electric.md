---
title: cell-poration-electric
parent: Cross-cuts
layout: default
---

# Cross-cut: `cell-poration-electric`

**14 corpus entries disclose this subsystem.**

Earliest disclosure: 2001

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Lonza Nucleofector (classic 2b/2S cuvette platform) (2001)

- **id**: `lonza-nucleofector-classic`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Amaxa GmbH (acquired 2008 by Lonza)
- **disclosure**: Amaxa GmbH product introduction 2001; US patent US7,332,332B2 (Nucleofection method, priority 2002); EP1390518B1; Lonza acquired Amaxa 2008
- **ip status**: patented
- **prior art notes**: Discloses a low-volume polypropylene cuvette with parallel electrodes, used in conjunction with proprietary buffer compositions and program-defined pulse waveforms (the 'nucleofection' protocol set) that drive cargo delivery into the nucleus of non-dividing cells. The patent estate covers the buffer + waveform combinations as well as the cuvette geometry. Anticipates: kit-format electroporation where the cuvette+buffer+waveform are jointly specified per cell type; programmable pulse generator with cell-specific protocols; insert-molded electrode-bearing disposable cuvette as the closed-disposable element. Predecessor architecture for the 4D-Nucleofector and 4D-LV continuous-flow variants.

## MaxCyte STX Scalable Transfection System (2007)

- **id**: `maxcyte-stx-flow-electroporation`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: MaxCyte Inc.
- **disclosure**: MaxCyte Inc. STX product launch 2007; US patent US7,029,916B2 (Flow electroporation chamber, granted 2006, priority 2002); MaxCyte Inc. SEC S-1 (2021)
- **ip status**: patented
- **prior art notes**: Discloses a flow-through electroporation chamber: cells in suspension are pumped between parallel planar electrodes spaced for uniform field; pulse generator delivers shaped electric pulses to volumes of cells transiting the chamber; cargo (DNA/RNA/protein) is co-suspended; output collected sterile downstream. Anticipates: continuous-flow electroporation as alternative to cuvette-batch (Lonza Nucleofector predecessor architecture); use of disposable single-use chamber decoupled from reusable instrument body; protocol-library transfer between research-scale (STX) and GMP-scale (GTx) processing assemblies. Element-by-element: peristaltic infeed + parallel-plate disposable chamber + pulse forming network + sterile collection bag.

## Bio-Rad Gene Pulser MXcell Electroporation System (2007)

- **id**: `biorad-gene-pulser-mxcell`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Bio-Rad Laboratories
- **disclosure**: Bio-Rad Gene Pulser MXcell product launch 2007; Bio-Rad Bulletin 5447 (MXcell brochure); US patent US7,799,555B2 (Apparatus and method for electroporating cells in a multi-well plate, Bio-Rad)
- **ip status**: patented
- **prior art notes**: Discloses an electroporation plate in which each well of a 96-well array contains an integrated electrode pair, addressed by a multiplexed pulse generator that can fire well-by-well or row-by-row with independent waveforms. Anticipates: multi-well-plate-format electroporation (distinct from cuvette and pipette-tip formats), where the entire 96-well plate acts as the disposable, and the instrument programs distinct conditions per well — enabling high-throughput protocol screening. Element-by-element: 96-well disposable + per-well electrode pair + multiplexed pulse forming network + plate-handling registration.

## MaxCyte GTx Flow Electroporation System (2014)

- **id**: `maxcyte-gtx-gmp-electroporator`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: MaxCyte Inc.
- **disclosure**: MaxCyte GTx CE-mark and 510(k) clearance documentation 2014; MaxCyte Inc. SEC S-1 (2021); US patent US7,029,916B2 (parent flow-electroporation chamber)
- **ip status**: patented
- **prior art notes**: GMP-grade variant of the STX flow-electroporation chamber, packaged with traceable single-use assembly and 21 CFR Part 11 control electronics. Anticipates: closed-system clinical electroporation of patient-derived cells where the entire fluid path is single-use, sterile-welded to upstream apheresis bag and downstream wash/formulation, controlled by a regulated audit-trail electronics stack. Element-by-element: weldable inlet + disposable parallel-plate chamber + sterile collection bag + GMP audit-trail SCADA. Distinguishable from MaxCyte STX (research-grade) by the GMP cartridge and software, not the underlying electrochemistry.

## MaxCyte ATx Flow Electroporation System (2018)

- **id**: `maxcyte-atx-assay-electroporator`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: MaxCyte Inc.
- **disclosure**: MaxCyte ATx product launch 2018; MaxCyte Inc. annual report 2019; parent US7,029,916B2
- **ip status**: patented
- **prior art notes**: Bench-scale flow-electroporation variant intended for assay-throughput cell engineering rather than research-scale (STX) or GMP (GTx). Anticipates the existence of a downward-scaled disposable processing assembly that preserves the parallel-plate field-uniformity geometry while reducing cell load to assay-relevant volumes. Same element decomposition as STX/GTx (peristaltic infeed + disposable chamber + pulse generator + sterile collection), differing only in chamber dimensions and cell-volume range.

## Lonza 4D-Nucleofector LV (Large Volume) (2018)

- **id**: `lonza-4d-nucleofector-lv`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Lonza Cologne GmbH (formerly Amaxa)
- **disclosure**: Lonza 4D-Nucleofector LV Unit product launch 2018; Lonza Bioscience product datasheet rev 2019; US patent US10,584,331B2 (Methods for high efficiency transfection, assigned Lonza Cologne, 2020)
- **ip status**: patented
- **prior art notes**: Scale-up of the cuvette-format Nucleofector to clinical volumes via large disposable processing chamber that preserves the field uniformity, buffer composition, and pulse waveform of the research-scale 4D-Nucleofector. Anticipates: GMP-grade large-volume electroporation where the protocol library validated at research scale transfers to clinical scale via a geometrically-similar disposable cassette (the same architectural pattern as the MaxCyte STX→GTx scale chain). Element-by-element: closed disposable cassette + planar electrodes + buffer-defined cell suspension + waveform library + sterile collection. Distinguishable from MaxCyte by being semi-batch rather than continuous flow.

## Berkeley Lights Lightning Optofluidic System (2019)

- **id**: `berkeley-lights-lightning`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Berkeley Lights Inc. (now PhenomeX)
- **disclosure**: Berkeley Lights Lightning product launch 2019; Berkeley Lights S-1 SEC filing 2020-06; OptoElectroPositioning patent estate US9,023,628B2
- **ip status**: patented
- **prior art notes**: Variant of the Berkeley Lights OptoSelect / Beacon architecture in which the optoelectronic positioning array is paired with on-chip imaging and a transfection workflow within the NanoPen chambers — distinct from the original Beacon (cell-line development focus) by including transfection-after-isolation as a single integrated workflow. Anticipates: optoelectronic-positioning chip extended with on-chip transfection events triggered after single-cell isolation; combined imaging + delivery in the same chamber array. Element-by-element: photoconductor array + NanoPen chamber + objective + on-chip pulse/cargo flush + clonal recovery export.

## Inscripta Onyx Digital Genome Engineering Platform (2019)

- **id**: `inscripta-onyx-genome-engineering`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Inscripta Inc.
- **disclosure**: Inscripta Onyx product launch 2019; Inscripta MAD7 nuclease publication: Garst et al., 'Genome-wide engineering of E. coli using CREATE,' Nat Biotechnol 35:48 (2017); Inscripta SEC filings; US patent US10,808,254B2 (Inscripta nucleic acid engineering systems)
- **ip status**: patented
- **prior art notes**: Discloses an integrated cassette that runs the full CREATE (CRISPR-Enabled Trackable genome Engineering) workflow: cells and editing oligo libraries loaded; on-cassette electroporation delivers libraries; outgrowth chambers with media routing; downstream selection and collection. Anticipates: closed-cassette automated bacterial/yeast genome-engineering workflows; on-cartridge electroporation followed by on-cartridge cell-growth in shared fluid path; the broader 'design-build-test in one box' microbial editing factory architecture. Element-by-element: oligo input + cell input + on-cassette electroporation + outgrowth chamber with feed/bleed + selection chamber + collection bag.

## Beam Therapeutics Base-Editing Manufacturing Platform (2019)

- **id**: `beam-therapeutics-base-editing-mfg`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Beam Therapeutics Inc.
- **disclosure**: Beam Therapeutics SEC S-1 (2020-01); Komor et al. 'Programmable editing of a target base in genomic DNA without double-stranded DNA cleavage,' Nature 533:420 (2016); Beam patent estate US10,167,457B2 (Cytidine deaminase fusion)
- **ip status**: patented
- **prior art notes**: Process disclosure: closed-system ex vivo base-editing manufacturing in which patient-derived CD34+ HSPCs are processed through a sterile fluid train comprising apheresis input → CD34 enrichment (CliniMACS-class) → activation/expansion in single-use bag → MaxCyte GTx flow electroporation with base-editor mRNA + sgRNA → wash/formulation → cryopreservation. Anticipates: closed-cartridge base-editing manufacturing where the editing reagent (mRNA-encoded base editor + sgRNA, not a viral vector) is electroporated into HSPCs in a single-use sterile train. Distinguishable from CRISPR/Cas9 manufacturing by the specific base-editor reagent identity, but the fluidic/process architecture is shared. Element-by-element: apheresis weld + CD34 affinity column + expansion bag + MaxCyte GTx EP + wash/concentration + cryo bag.

## Caribou Biosciences CB-010/CB-011 chRDNA Manufacturing (2020)

- **id**: `caribou-biosciences-cb-001-mfg`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Caribou Biosciences Inc.
- **disclosure**: Caribou Biosciences SEC S-1 (2021-07); ClinicalTrials.gov NCT04637763 (CB-010 ANTLER); Caribou patent estate US11,053,481B2 (chRDNA Cas9 hybrid guides)
- **ip status**: patented
- **prior art notes**: Process disclosure for allogeneic CAR-T manufacturing: healthy-donor leukapheresis → CD3 affinity column → activation in bag/G-Rex → MaxCyte GTx electroporation with chRDNA + Cas9 RNP for multiplex knockout → lentiviral or AAV CAR transduction → expansion in perfusion bioreactor → wash/formulation → cryopreservation. Anticipates: closed-train allogeneic CAR-T workflows that combine multiplex chRDNA-mediated knockouts with viral CAR insertion in a single sterile fluid path. The chRDNA reagent is the differentiating IP element; the fluidic train architecture overlaps with other allogeneic CAR-T processes.

## Resilience CGT Manufacturing Platform (2020)

- **id**: `resilience-cgt-manufacturing-platform`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: National Resilience Inc.
- **disclosure**: National Resilience Inc. company launch 2020-11; Resilience press releases 2021-2023; multiple acquisitions including Ology Biosciences (CGT), Mibelle Biochemistry, Boston Children's pDNA facility
- **ip status**: trade-secret
- **prior art notes**: Process disclosure: Resilience operates a multi-modality CGT CDMO with shared infrastructure for mRNA-LNP (microfluidic mixer + TFF), AAV (iCellis or suspension + chromatography), lentivirus (suspension + TFF + chromatography), plasmid (fermenter + chromatography), and cell therapy (closed-train MaxCyte/CliniMACS-class workflows). The microfluidic content is the cumulative content of the modality-specific trains; Resilience's platform-level disclosure is the digital-twin orchestration across sites and the unified materials-management infrastructure. Trade-secret heavy; entry rests on press releases and public manufacturing capability disclosures.

## Thermo Fisher Neon NxT Electroporator (2022)

- **id**: `thermofisher-neon-nxt-electroporator`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Thermo Fisher Scientific (Invitrogen)
- **disclosure**: Thermo Fisher Scientific Neon NxT product launch press release 2022-09; Neon NxT user guide MAN0019022 rev 2.0; predecessor Neon Transfection System (Invitrogen, ~2009) US patent US8,008,065B2 (Pipette-tip-based electroporation)
- **ip status**: patented
- **prior art notes**: Discloses an electroporation device in which the cell suspension is held within a disposable pipette tip whose lower bore contains the field-defining electrodes; aspiration draws cells between the electrodes; the pulse generator fires across the tip electrodes; cells are then dispensed into culture vessels. Anticipates: pipette-tip-format electroporation (distinct from cuvette format), parallelization by multi-channel head, instrument-disposable separation. The NxT update adds 3-channel parallelism and a redesigned electrode tip; underlying electrode-in-pipette architecture is the Invitrogen Neon parent.

## Miltenyi CliniMACS Prodigy Adapt module (2023)

- **id**: `miltenyi-prodigy-adapt`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Miltenyi Biotec
- **disclosure**: Miltenyi Biotec CliniMACS Prodigy Adapt product launch. https://www.miltenyibiotec.com/global/en/products/clinimacs-prodigy-adapt.html (announced 2023; references parent CliniMACS Prodigy patent family).
- **ip status**: patented
- **prior art notes**: Extension module to the CliniMACS Prodigy closed-cartridge platform that adds higher-throughput and adaptable process steps for allogeneic cell therapies (gene-edited NK, iPSC-derived, off-the-shelf CAR-T). Architecturally significant as the first commercial closed cartridge to integrate selection, activation, transduction/electroporation, expansion, formulation, and fill-finish for allogeneic products in a single disposable. Anticipates: closed-cartridge architectures supporting multi-modal gene delivery (lentiviral, electroporation, chemical) and continuous selection across multiple cell types within one disposable; modular extensions to GMP cartridge platforms.

## AESOP: acoustic-electric shear orbiting poration (2026-04-09)

- **id**: `zhang-2026-aesop-acoustic-electric-poration`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: Abraham P. Lee group, UC Irvine
- **disclosure**: Zhang, M.; Taravatfard, A. Z.; Aghaamoo, M.; Lee, A. P. Sequential intracellular delivery of genetic coding molecules using an acoustic electric microfluidic platform. Lab Chip 2026, advance article. DOI: 10.1039/D5LC00941C
- **ip status**: patented
- **prior art notes**: Discloses an acoustic-electric microfluidic platform for sequential intracellular transfection without external pumping. Anticipates: arrays of acoustic microstreaming vortices generated by oscillating air-liquid interfaces (trapped bubbles driven by piezoactuation) for cell trapping, simultaneous use of the same acoustic field for sequential reagent exchange, combined mechanical shear + electric field poration as a single transfection step, and 7× efficiency gain over co-transfection for plasmid DNA + Cas9 RNP delivery. Single physical mechanism (acoustic streaming) collapses three subsystems (cell trap, fluid handler, transfection actuator).
