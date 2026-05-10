---
title: pump-peristaltic-on-chip
parent: Cross-cuts
layout: default
---

# Cross-cut: `pump-peristaltic-on-chip`

**18 corpus entries disclose this subsystem.**

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

## Beckman Vi-CELL XR Cell Viability Trypan Blue Cuvette (2003)

- **id**: `beckman-vi-cell-xr-cell-viability-cuvette`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Beckman Coulter (Danaher)
- **disclosure**: Beckman Coulter Vi-CELL XR launch 2003; product datasheet; pharmaceutical bioprocess QC adoption (USP <90>)
- **ip status**: patented
- **prior art notes**: Discloses an automated Trypan Blue dye-exclusion cell viability instrument with a flow-cell-capillary image-based discrimination architecture: peristaltic pump aspirates sample from cup, mixes 1:1 with Trypan Blue, transports plug into a 100-µm-deep glass flow capillary positioned in the focal plane of a 10x microscope objective with CCD imaging, and applies image-based discrimination (membrane-intact cells exclude dye and appear bright; membrane-compromised cells absorb dye and appear dark blue). The instrument autoflushes between samples. Anticipates: image-based Trypan Blue cell viability automation for bioreactor monitoring; CHO/Sf9/HEK QC use as a pharmacopeial method; the architectural choice of flow-cell + brightfield imaging vs flow cytometry + propidium iodide for the same endpoint.

## MBARI Environmental Sample Processor (ESP) (2003)

- **id**: `mbari-esp-environmental-sample-processor`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Monterey Bay Aquarium Research Institute (MBARI) (Scholin lab) / McLane Research Laboratories (commercial 2G/3G ESP)
- **disclosure**: Scholin CA et al., 'The Environmental Sample Processor (ESP) — An autonomous robotic device for detecting microorganisms remotely using molecular probe technology,' Proc. OCEANS 2003: 1-7 (2003); Scholin CA et al., 'Remote detection of marine microbes, small invertebrates, harmful algae, and biotoxins using the Environmental Sample Processor (ESP),' Oceanography 22(2):158-167 (2009)
- **ip status**: patented
- **prior art notes**: The ESP is the canonical autonomous oceanographic microfluidic robotic sampler. Element-by-element prior art for: (a) automated puck-carousel architecture with integrated filtration + lysis + sandwich-hybridization assay + chemiluminescent readout in a long-deployment marine-robotic platform; (b) feedback-controlled adaptive sampling where the on-board assay result triggers subsequent sample collection (LRAUV+ESP plume tracking); (c) integration of ddPCR into a marine autonomous vehicle (3G ESP), which anticipates patents on autonomous in-situ qPCR/ddPCR cartridges for environmental monitoring; (d) the sealed puck format with pre-loaded dry/wet reagents stored at ocean depth for months anticipates patents on long-storage diagnostic cartridges in extreme environments. ESP is also the closest terrestrial analog to a planetary in-situ life detection cartridge.

## Siemens RAPIDPoint 500 Blood Gas Cartridge (2008)

- **id**: `siemens-rapidpoint-500-blood-gas-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Siemens Healthineers (formerly Bayer Diagnostics)
- **disclosure**: Siemens RAPIDPoint 500 510(k) K080776 cleared 2008; product datasheet 2008-09; predecessor RAPIDLab 1265 patents (Bayer Diagnostics)
- **ip status**: patented
- **prior art notes**: Discloses an all-in-one POC blood gas cartridge integrating: thick-film potentiometric ISE array (pH, pCO2, pNa, pK, pCa, pCl), amperometric pO2 + glucose + lactate enzyme electrodes, and a multi-wavelength CO-oximetry cuvette for total Hb fractionation, all sharing a peristaltic-pump-driven flow path; reagent/calibrant/wash bags integrated into the cartridge body and pierced by mechanical actuators inside the analyzer; auto-calibration runs between samples without user intervention; cartridge-resident sample volume <100 µL. Anticipates: long-life POC blood-gas cartridges with on-board reagent storage and integrated CO-oximetry — the architectural pattern dominating ICU/ER/OR analyzers. Differs from Werfen GEM Premier (separate entry) in cartridge design (Siemens' 'measurement cartridge' separates sensors from reagents).

## Radiometer ABL90 FLEX Blood Gas Analyzer Sensor Cassette (2009)

- **id**: `radiometer-abl90-flex-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Radiometer Medical (Danaher)
- **disclosure**: Radiometer ABL90 FLEX launch 2009-09; FDA 510(k) K093103; ABL90 FLEX PLUS update 2014
- **ip status**: patented
- **prior art notes**: Discloses a POC blood gas cartridge architecture distinguished by: (1) separable Sensor Cassette and Solution Pack — the user can replace one without the other based on usage profile, optimizing cost; (2) ultra-low 65 µL sample volume enabling neonatal capillary collection; (3) high-spectral-resolution CO-oximetry (256-wavelength photodiode array spectrophotometer in lieu of fixed-filter approach), enabling better discrimination of fetal Hb, sulfhemoglobin, and high MetHb fractions. The ABL90 family represents the third-generation Radiometer architecture (succeeding ABL700 series and ABL800). Anticipates: cartridge-and-pack separation as a fluidic-engineering pattern for cost-of-ownership optimization; high-spectral-resolution POC CO-oximetry; sub-100 µL POC blood gas + CO-oximetry. Companion to ABL800 FLEX (high-throughput central-lab variant).

## BioTek MultiFlo FX dispenser (2010)

- **id**: `biotek-multiflo-flx-dispenser`
- **corpus**: private
- **device class**: dispenser-pipettor
- **creator**: BioTek (acquired by Agilent 2019)
- **disclosure**: Agilent Technologies BioTek MultiFlo FX. https://www.agilent.com
- **ip status**: patented
- **prior art notes**: Microplate dispenser/washer with peristaltic-pump-based reagent dispensing into 96/384/1536-well plates. Reference for the broader 'plate-format dispenser' product category that competes with Echo acoustic dispensing on cost and fluid compatibility (more inclusive of viscous fluids that Echo handles poorly).

## Pearce Lab MOST Open Scientific Hardware Suite (2012)

- **id**: `pearce-most-open-hardware-suite`
- **corpus**: open
- **device class**: other
- **creator**: Joshua M. Pearce (Michigan Technological University), MOST research group
- **disclosure**: Pearce J.M., 'Building Research Equipment with Free, Open-Source Hardware', Science 337:1303-1304 (2012), doi:10.1126/science.1228183; Pearce J.M., 'Open-Source Lab' (Elsevier 2014, ISBN 978-0-12-410462-4); https://www.appropedia.org/Category:MOST
- **ip status**: open-copyleft
- **prior art notes**: Discloses a foundational suite of >50 published open lab instruments from a single research group, including: open syringe pump (already cataloged separately), open peristaltic pump, open colorimeter, open spectrophotometer, open mass-balance, open magnetic stirrer hot-plate, open shaker incubator, open laser-cut/3D-printed centrifuge, open optical-density meter, open temperature-controlled stage. Each is published with full BOM, parametric CAD (typically OpenSCAD), firmware, and calibration data. Together these constitute a substantial fraction of the post-2012 open lab-equipment commons. Citable as 102 prior art against many commercial 'low-cost lab instrument' patents from 2014-2024. Specifically anticipates the architectural pattern of a research lab releasing its full instrument library as a coordinated commons under permissive licenses.

## WISSARD / SALSA Subglacial Antarctic Microbial Samplers (2014)

- **id**: `wissard-salsa-subglacial-microbe-sampler`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: WISSARD project (Whillans Ice Stream Subglacial Access Research Drilling) / SALSA project (Subglacial Antarctic Lakes Scientific Access) / NSF funded multi-institution
- **disclosure**: Christner BC et al., 'A microbial ecosystem beneath the West Antarctic ice sheet,' Nature 512:310-313 (2014), doi:10.1038/nature13667; Priscu JC et al., 'Scientific access into Mercer Subglacial Lake: scientific objectives, drilling operations and initial observations,' Annals of Glaciology 62:340-352 (2021)
- **ip status**: open-permissive
- **prior art notes**: Discloses the cleanest-published terrestrial protocol for retrieving microbiologically-pristine subsurface aqueous samples — the most directly cited prior art for any future Europa/Enceladus subsurface life detection mission. Element-by-element: (a) hot-water drill with multi-stage HEPA + 0.2 µm filtration + UV-C sterilization of drill water anticipates patents claiming planetary subsurface drilling fluid sterilization architectures; (b) Sterivex closed-cartridge format with sealed inlet/outlet for downstream nucleic acid extraction without breaking sterility anticipates planetary sample-handling cartridges that must preserve sterility from sample-take through analysis; (c) the published clean-tent protocols and contamination-control budgets are open prior art that any 'planetary protection' patent would have to overcome. WISSARD/SALSA are the gold standard for terrestrial-analog subsurface-ocean sampling.

## Beta Bionics iLet Bionic Pancreas (2014-06-15)

- **id**: `beta-bionics-ilet-bionic-pancreas`
- **corpus**: private
- **device class**: pump-component
- **creator**: Beta Bionics Inc.
- **disclosure**: Russell SJ et al. N Engl J Med 371(4):313-325 2014 doi:10.1056/NEJMoa1314474; FDA 510(k) K223846 May 2023
- **ip status**: patented
- **prior art notes**: Discloses an automated closed-loop insulin (or insulin+glucagon) delivery system with simplified user interface (weight-only initialization) and adaptive control. The pumping mechanism uses prefilled microliter-resolution cartridges. Anticipates: zero-input bionic-pancreas closed-loop architectures; the user-experience pattern of weight-only initialization for an autonomous pump; bi-hormonal microliter glucagon delivery alongside insulin.

## Werfen GEM Premier 5000 Blood Gas Multi-Use Cartridge (2015)

- **id**: `werfen-gem-premier-5000-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Instrumentation Laboratory / Werfen
- **disclosure**: Werfen GEM Premier 5000 launch 2015-12; FDA 510(k) K151867; predecessor entry: instrumentation-laboratory-gem-premier (already in corpus, GEM Premier 4000)
- **ip status**: patented
- **prior art notes**: Discloses a self-contained 'Multi-Use' blood gas cartridge integrating sensors, reagents, calibrants, and waste in a single disposable; the analyzer hardware is reduced to a peristaltic pump, optical bench, electrical interface, and barcode/RFID reader. The cartridge architecture eliminates the user-serviced reagent/waste/sensor reservoirs that defined earlier blood gas analyzers, producing a sealed-system architecture comparable to Siemens RAPIDPoint 500 (separate entry) — with key differentiator: GEM uses a single integrated cartridge whereas Siemens separates 'measurement cartridge' from 'reagent cartridge.' The Werfen iQM (and iQM2) protocol replaces traditional periodic external QC with continuous on-cartridge QC sample passes between patient samples. Anticipates: fully sealed POC blood gas cartridges with on-board waste containment; continuous-QC architectures replacing periodic 2-3 level external QC; cartridge as the disposable failure-mode boundary.

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

## OpenFlexure Pump (Stirling et al. 2020) (2020-06)

- **id**: `openflexure-pump-stirling-2020`
- **corpus**: open
- **device class**: pump-component
- **creator**: Stirling J., Bowman R. (U Bath), OpenFlexure Project
- **disclosure**: Stirling J., Bumke K., Collins J., Bowman R., 'A printed flexure peristaltic pump for low-cost open-hardware microscopy', Wellcome Open Research (2020); https://gitlab.com/openflexure/openflexure-microscope and https://gitlab.com/bath_open_instrumentation_group/pneumatic-sample-stage; companion preprint at https://arxiv.org/abs/2007.10336
- **ip status**: open-copyleft
- **prior art notes**: Discloses a fully 3D-printed peristaltic pump in which the rollers and the housing form a single flexure printed assembly that compresses silicone tubing. Anticipates patents post-2020 claiming '3D-printed peristaltic pumps with monolithic flexure roller cages' or 'low-cost pumps integrated with OpenFlexure-style open microscopes for live-cell perfusion.' Element-by-element discloses the printed cage geometry, the stepper-driven roller assembly, the silicone tubing routing, and the Arduino firmware for closed-loop flow-rate setting against an empirical calibration curve. Existing corpus entry 'open-flexure-pump' covered the broader OpenFlexure pump family; this entry pins the Stirling 2020 specific design with its primary publication.

## BongoPump Open Liquid-Handling Pump (2022)

- **id**: `open-bioworks-bongo-pump`
- **corpus**: open
- **device class**: pump-component
- **creator**: Open Bioworks community (post-OpenLH spinoff)
- **disclosure**: Open Bioworks GitHub release: https://github.com/Open-Bioworks/BongoPump (2022); design files and BOM publicly available
- **ip status**: open-permissive
- **prior art notes**: Discloses a 3D-printable 3-roller peristaltic pump head with a printed roller cage that fits standard silicone tubing of specified inner diameter. The pump is driven by a NEMA 17 stepper through a printed planetary reduction; control firmware is an Arduino sketch exposing serial-set RPM and direction commands. Documentation provides flow-rate-vs-RPM calibration tables for two tubing sizes. CC-BY / MIT release. Anticipates: any 3D-printed peristaltic pump claim post-2022 with planetary reduction and direct stepper drive; companion piece to Wijnen-Pearce syringe pump for the lineage of fully-open lab pumps. Specifically anticipates patent claims to 'a peristaltic pump head fabricated entirely from FFF-printed parts integrated into an open liquid-handling robot.'
