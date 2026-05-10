---
title: fluorescence-detection-multi-color
parent: Cross-cuts
layout: default
---

# Cross-cut: `fluorescence-detection-multi-color`

**8 corpus entries disclose this subsystem.**

Earliest disclosure: 2003

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## ABI 3130xl Genetic Analyzer (2003)

- **id**: `abi-3130xl-ce`
- **corpus**: private
- **device class**: separator-component
- **creator**: Applied Biosystems (now ThermoFisher Scientific)
- **disclosure**: Applied Biosystems 3130xl user guide 4359571; product launch 2003-04.
- **ip status**: patented
- **prior art notes**: Predecessor of the ABI 3500. Discloses: user-assembled fused-silica capillary array of 16 lanes, manually loaded into the instrument; polymer (POP-4 / POP-7) hydraulic syringe loading; argon-ion or solid-state laser excitation with 5-dye spectral filter set; auto-sampler with 96/384-well plate compatibility. Anticipates: the entire CODIS-compliant 13-loci forensic STR architecture as it was practiced 2003-2010; manually-replaceable capillary arrays; 5-dye fluorescence detection on capillary CE.

## Applied Biosystems 7500 Real-Time PCR System (2005)

- **id**: `abi-7500-real-time-pcr`
- **corpus**: private
- **device class**: consumable-bulk
- **creator**: Applied Biosystems (now ThermoFisher Scientific)
- **disclosure**: Applied Biosystems 7500 user guide 4387784; product launch 2005.
- **ip status**: patented
- **prior art notes**: The ABI 7500 is a workhorse real-time PCR instrument, used in forensic labs primarily for Quantifiler human DNA quantitation prior to STR amplification. Discloses: 96-well plate format with optical film seal (the relevant 'microfluidic-equivalent' element); 5-color spectral filter wheel for multiplex qPCR; Peltier block thermal cycling; CCD-based fluorescence detection with internal ROX normalization. Anticipates: 96-well plate qPCR with 5-color detection; standardized forensic DNA quantitation workflows that gate STR amplification (Quantifiler -> dilute to optimal input -> amplify); the architectural pattern of separate quantitation and amplification platforms in the forensic pipeline.

## ThermoFisher 3500 / 3500xL Genetic Analyzer CE (2010)

- **id**: `thermofisher-3500-ce`
- **corpus**: private
- **device class**: separator-component
- **creator**: Applied Biosystems / Life Technologies (now ThermoFisher Scientific)
- **disclosure**: Applied Biosystems 3500 user guide 4401661; Wenz et al., Forensic Sci. Int. Genet. Suppl. 2011, 3, e25-e26; product launch 2010.
- **ip status**: patented
- **prior art notes**: Workhorse 8/24-capillary CE instrument that replaced the ABI 3130xl as the dominant US forensic CE platform. Discloses: factory-assembled capillary array with RFID consumable tracking (lot tracking for QC and chain-of-custody compliance); spectral matrix calibration via on-instrument Spectral Module; argon-ion laser excitation replaced with longer-wavelength solid-state laser; integrated 6-dye filter wheel optimized for Identifiler Plus / GlobalFiler / PowerPlex Fusion. Anticipates: RFID-tracked consumables on forensic CE for chain-of-custody; expanded 6-dye chemistry on capillary CE; the architectural envelope into which all 3500-class STR profiling fit through the 2010s.

## ThermoFisher RapidHIT 200 Human DNA Identification System (2012-09)

- **id**: `thermofisher-rapidhit-200`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: IntegenX (acquired by ThermoFisher Scientific 2014)
- **disclosure**: IntegenX RapidHIT 200 product launch ICHA 2012; Hopwood et al., Forensic Sci. Int. Genet. 2013, 7, 1-2. DOI:10.1016/j.fsigen.2012.08.007; ThermoFisher acquired IntegenX 2014; user manual MAN0014654.
- **ip status**: patented
- **prior art notes**: Discloses a sealed disposable cartridge integrating: (i) buccal swab/blood-spot lysis chamber; (ii) magnetic-bead DNA extraction; (iii) multiplex STR PCR amplification of CODIS loci using GlobalFiler Express chemistry; (iv) on-board capillary electrophoresis with multi-color fluorescence detection; (v) automated allele-call generation. Anticipates: integrated forensic-grade STR cartridges performing the full sample-to-profile workflow in <2 hr without operator intervention; pneumatic actuation of laminate-sealed reaction wells in a forensic context; incorporation of internal positive/negative controls per cartridge to satisfy ASCLD-LAB chain-of-custody. The combination of CODIS-compliant 13-loci output with field-deployable form factor anticipates booking-station rapid DNA workflows.

## ANDE 6C Rapid DNA Identification System (2014)

- **id**: `ande-6c-rapid-dna`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: ANDE Corporation (formerly NetBio / Network Biosystems)
- **disclosure**: Tan et al., Investig. Genet. 2013, 4, 16. DOI:10.1186/2041-2223-4-16; FBI NDIS approval for ANDE 6C 2017-08-09; ANDE Corp Operator's Manual 2019
- **ip status**: patented
- **prior art notes**: Discloses two cartridge variants: A-Chip (arrestee/known reference) and I-Chip (forensic crime scene swab/blood/cigarette butt evidence). Each chip integrates: (i) on-chip lysis with chaotrope, (ii) silica-bead solid-phase DNA purification, (iii) multiplex PCR (PowerPlex 16HS or FlexPlex 27 chemistry on-chip), (iv) high-resolution glass-channel capillary electrophoresis with 6-dye fluorescence detection, (v) automated FAIRS expert system allele call. Distinguishes from RapidHIT in glass-bonded CE channels (vs all-thermoplastic CE) for higher resolution. Anticipates: rugged forensic STR cartridges with glass-bonded CE for resolution-critical low-template work; mass-disaster DVI (Disaster Victim Identification) deployment of cartridge-based DNA; combined arrestee and crime-scene workflows on a single platform with chemistry differentiation.

## Promega PowerPlex Fusion 6C STR Amplification Cartridge (2015-09)

- **id**: `promega-powerplex-fusion-6c-cartridge`
- **corpus**: private
- **device class**: consumable-bulk
- **creator**: Promega Corporation
- **disclosure**: Ensenberger et al., Forensic Sci. Int. Genet. 2016, 21, 134-144. DOI:10.1016/j.fsigen.2015.12.011; Promega technical manual TMD039.
- **ip status**: patented
- **prior art notes**: Reagent-and-chemistry side of the forensic Rapid DNA stack: a freeze-dried multiplex STR amplification kit prepackaged for cartridge integration on RapidHIT 200, RapidHIT ID, ANDE 6C, and Spectrum Compact CE. Discloses: 27-loci 6-dye STR multiplex covering the CODIS Expanded Core (20 loci required FBI 2017) plus international loci; lyophilized master mix matched to on-cartridge rehydration volumes; 6-dye fluorophore labeling matched to Spectrum/3500/RapidHIT 6-dye detection optics. Anticipates: pre-lyophilized multiplex STR reagents formulated for cartridge-integrated forensic platforms; the chemistry-cartridge interface enabling cross-instrument compatibility (one chemistry, multiple cartridge form factors).

## ThermoFisher RapidHIT ID DNA Booking System (2017-09)

- **id**: `thermofisher-rapidhit-id`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: ThermoFisher Scientific
- **disclosure**: ThermoFisher Scientific press release Sept 2017; FBI NDIS approval letter 2018-05; Della Manna et al., Forensic Sci. Int. Genet. 2016, 25, 145-156. DOI:10.1016/j.fsigen.2016.08.008
- **ip status**: patented
- **prior art notes**: Single-sample variant of RapidHIT 200, redesigned as a coffeepod-style cartridge for booking-station deployment. Discloses miniaturized integration of all RapidHIT 200 subsystems (extraction, amplification, CE, detection) into a single-use disposable, with full instrument footprint <1 cubic foot. Anticipates: single-cartridge, single-sample forensic STR profiling with sub-2-hour turnaround at non-laboratory deployment sites (police booking stations). The cartridge geometry anticipates closed-system designs that satisfy CODIS NDIS chain-of-custody at the suspect-intake point.

## Promega Spectrum Compact CE System (2020-06)

- **id**: `promega-spectrum-compact-ce`
- **corpus**: private
- **device class**: separator-component
- **creator**: Promega Corporation
- **disclosure**: Promega Spectrum Compact CE technical manual TM543; Romsos et al., Forensic Sci. Int. Synergy 2021, 3, 100156; product launch 2020.
- **ip status**: patented
- **prior art notes**: Discloses a 4-capillary CE instrument that replaces the previously dominant ABI 3500 architecture with a single-cartridge design where the fused-silica capillary array, polymer reservoir, and buffer reservoirs ship pre-assembled and are user-replaced as a unit. Disposable cartridge eliminates the manual capillary array installation that historically required factory service or specialist training. Anticipates: cartridge-style replacement of CE consumables (capillary + polymer + buffer) in forensic STR analysis; 6-dye detection optics matched to PowerPlex Fusion 6C; small-footprint forensic CE for satellite labs and field-forward use. The combination of pre-assembled cartridge plus 6-dye optics anticipates non-CapEx-intensive distributed forensic CE.
