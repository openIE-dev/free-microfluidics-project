---
title: interface-fluidic-edge-connector
parent: Cross-cuts
layout: default
---

# Cross-cut: `interface-fluidic-edge-connector`

**6 corpus entries disclose this subsystem.**

Earliest disclosure: 1984-10-23

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Screen-printed electrode (SPE) fabrication for biosensors and glucose strips (1984-10-23)

- **id**: `screen-printed-biosensor-electrode-deposition`
- **corpus**: private
- **device class**: printer-tooling
- **creator**: MediSense (now Abbott), Genetics International; ink suppliers DuPont (silver/silver-chloride and carbon pastes), Sun Chemical/Gwent Group, Acheson/Henkel; screen printers DEK, EKRA, Asys
- **disclosure**: US4545382A Sensor for components of a liquid mixture (Higgins, Hill & Plotkin, Genetics International / MediSense - the foundational screen-printed enzyme-electrode glucose strip); see also Cass et al., Ferrocene-mediated enzyme electrode for amperometric determination of glucose, Anal. Chem. 56, 667 (1984).
- **ip status**: patented
- **prior art notes**: Discloses screen-mesh thick-film deposition used to fabricate patterned electrochemical electrodes plus a laminated sub-5-microliter capillary reaction chamber - the canonical screen-printed biosensor strip. Anticipates claims to (a) screen-printed working/counter/reference electrode set on a flexible substrate for amperometric biosensing; (b) overprinted dried enzyme-mediator reagent layer on a screen-printed working electrode; (c) laminated spacer/cover defining a capillary-fill blood chamber over screen-printed electrodes. Foundational prior art for glucose-strip and screen-printed-immunosensor patents (Abbott, Roche, LifeScan, Bayer/Ascensia).

## SparkFun / Pumping Lemma open microfluidic 'brick' connectors (2017)

- **id**: `sparkfun-microfluidic-bricks`
- **corpus**: open
- **device class**: consumable-bulk
- **creator**: Pumping Lemma / open community
- **disclosure**: Pumping Lemma microfluidic bricks open-source connector system; community release. Various Hackaday and instructable disclosures from 2017 onward.
- **ip status**: public-domain
- **prior art notes**: Disclosed standardized modular interlocking microfluidic 'brick' connectors enabling rapid prototyping of fluidic networks from reusable parts. Anticipates: modular microfluidic interconnect standard for rapid hobbyist / educational fluidic-network prototyping.

## LumiraDx Point-of-Care Platform Microfluidic Test Strip (2017)

- **id**: `lumiradx-platform-microfluidic-strip`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: LumiraDx Limited
- **disclosure**: LumiraDx Platform CE-IVD launch 2017-12; SARS-CoV-2 Ag EUA 2020-08-18; INR strip 510(k) K191167; D-dimer 510(k) K203049
- **ip status**: patented
- **prior art notes**: Discloses a unified POC platform architecture: a single handheld electromechanical reader (with electrical contacts, optical excitation, and pneumatic/mechanical actuators) accepts a family of injection-molded microfluidic test strips, each pre-loaded with assay-specific dry reagents in metered zones along a capillary-driven flow path. The strip-level architecture pattern: sample inlet → capillary metering → dry-reagent rehydration mixer → optional incubation serpentine → detection chamber (electrochemical for INR/glucose; fluorescence for SARS-CoV-2 Ag, NT-proBNP, hsTnI). Anticipates: single-reader-multi-assay POC platforms using injection-molded microfluidic strips with assay-class-specific detection chambers; the commercial scaling pattern of strip manufacturing as the unit-economics enabler for menu breadth. Differs from i-STAT (single class: electrochemistry) and Sofia (single class: fluorescent immunoassay) by spanning electrochemistry + fluorescence on the same instrument.

## Abbott i-STAT Alinity Handheld Blood Analysis Cartridge (2018)

- **id**: `abbott-istat-alinity-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Abbott Point of Care
- **disclosure**: Abbott i-STAT Alinity FDA 510(k) K172011 cleared 2018-01-10; product launch press release 2018-02
- **ip status**: patented
- **prior art notes**: Discloses a handheld POC cartridge that integrates: a sealed calibrant pouch ruptured by mechanical bladder actuation, a microfluidic channel transporting fluid past a linear array of thin-film electrochemical biosensors (each with patterned ion-selective membrane or amperometric enzyme layer), an air-segment introduction step that pushes the calibrant past the sensors before driving sample over them (single-point single-fluid calibration), and an electrical interface mating the cartridge sensor pads to the analyzer reader contacts. Anticipates: handheld electrochemistry POC cartridges with pre-loaded liquid calibrant and bladder-driven sample introduction; the i-STAT family extension where the same disposable serves multiple generations of analyzer hardware. Improvements over the i-STAT cg8+ entry (in corpus): updated cartridge optical/RFID identification and connectivity-ready sensor handshake protocol.

## Jubilee Open-Source Multi-Tool Motion Platform (2022-04)

- **id**: `vasquez-2022-jubilee-toolchanger-platform`
- **corpus**: open
- **device class**: dispenser-pipettor
- **creator**: Machine Agency (University of Washington — Galloway, Vargas-Hernandez et al.)
- **disclosure**: Vasquez J.E., Vargas-Hernandez S., Atencia J., Bohnstedt B., Galloway K.C. et al. (Machine Agency, U Washington), 'Jubilee: An extensible machine for multi-tool fabrication and automation', HardwareX 11:e00266 (April 2022); doi:10.1016/j.ohx.2022.e00266; https://jubilee3d.com; https://github.com/machineagency/jubilee
- **ip status**: open-permissive
- **prior art notes**: Discloses a kinematically-coupled toolchanging gantry intended specifically for laboratory automation as well as additive manufacturing. Tools dock to a parking station and are picked up by the head via a three-pin kinematic mount that achieves repeatable sub-10-um pose; each tool is electrically connected via spring-pin contacts when docked. The publication and accompanying repository disclose: pipette tool, syringe-pump tool, micro-pipettor tool, camera tool, and demonstrate liquid-handling protocols implemented as G-code. Anticipates: laboratory toolchanging architectures where pipette/syringe/sensor tools are mechanically and electrically interchangeable on a single gantry under unified motion-control firmware; multi-modal lab-on-gantry workflows (e.g., aspirate, image, dispense, measure pH) executed as G-code; integration of OpenFlexure-style microscope payloads as toolchanger heads.

## NanoString CosMx Whole Transcriptome Atlas (WTA) (2024-01)

- **id**: `nanostring-cosmx-wta-2024`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: NanoString Technologies (Bruker Spatial Biology since 2024-05)
- **disclosure**: NanoString/Bruker product launch CosMx WTA, JPM Conference 2024-01; SP-1108 datasheet rev A; AGBT 2024 abstract
- **ip status**: patented
- **prior art notes**: Discloses scaling of CosMx in-situ multiplex from ~1000-plex panels to ~18000-plex whole transcriptome through extended cycling of barcoded oligo reporters delivered by an on-instrument microfluidic system. Anticipates: on-instrument fluidic delivery sequences that perform N>16 hybridization-image-strip cycles on a single mounted slide, with microfluidic reagent storage/manifold and per-slide flowcell sealing; combinatorial barcoding scheme for ~18k targets within manageable optical-readout cycles. Specifically anticipates claims to single-instrument WTA spatial transcriptomics by sequential hybridization (vs SBS-based Xenium or sequencing-by-ligation Visium HD).
