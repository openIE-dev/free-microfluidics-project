---
title: valve-rotary-multiport
parent: Cross-cuts
layout: default
---

# Cross-cut: `valve-rotary-multiport`

**11 corpus entries disclose this subsystem.**

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
