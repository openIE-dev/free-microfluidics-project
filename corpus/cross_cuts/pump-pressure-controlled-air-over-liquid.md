---
title: pump-pressure-controlled-air-over-liquid
parent: Cross-cuts
layout: default
---

# Cross-cut: `pump-pressure-controlled-air-over-liquid`

**13 corpus entries disclose this subsystem.**

Earliest disclosure: 1953-08-20

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Wallace H. Coulter 1953 Impedance Particle/Cell Counting Patent (Coulter Principle) (1953-08-20)

- **id**: `coulter-1953-impedance-cell-counting-patent`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Wallace H. Coulter (assigned later to Coulter Electronics, now Beckman Coulter / Danaher)
- **disclosure**: Coulter, W.H. US patent application filed 1949-10-20, US2656508A issued 1953-10-20, 'Means for counting particles suspended in a fluid'; Coulter, W.H. 'High speed automatic blood cell counter and cell size analyzer,' Proc. National Electronics Conference vol. 12 pp. 1034-1042 (1956)
- **ip status**: patented
- **prior art notes**: Discloses the foundational electrical-sensing-zone (Coulter principle) particle/cell counting technique: an electrolyte-filled chamber is divided by a small aperture (microfluidic constriction) bridged by an applied DC current; particles passing through the aperture displace electrolyte volume, momentarily increasing aperture impedance and producing voltage pulses whose amplitude is proportional to particle volume. Anticipates: ALL subsequent impedance-based microfluidic cell/particle counters (Coulter Counter Z series, all hematology analyzers using impedance, sub-µm 'tunable resistive pulse sensing' nanopore variants, microfluidic on-chip impedance cytometry). The 1953 patent expired in 1971 (17-year US term at the time), placing the foundational technique in the public domain — but downstream design improvements (sapphire apertures, hybrid optical-impedance, sweep-flow geometry) remain patented in modern instruments. This entry serves as the historical anchor making clear that any modern microfluidic impedance counter has 70+ years of expired-patent prior art to draw on.

## OLS Bio CASY Cell Counter and Analyzer (formerly Innovatis CASY-TT) (1991)

- **id**: `ols-bio-casy-tt-cell-counter`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: OLS Bio (formerly Innovatis AG; Roche Diagnostics divestiture)
- **disclosure**: Innovatis (Bielefeld, Germany) CASY launch 1991; CASY-TT (TwinTechnology) launch 2006; Innovatis acquired by Roche 2008; CASY product line now sold by OLS-Bio (since 2013); Pulsar Coulter-principle patent extension
- **ip status**: patented
- **prior art notes**: Discloses the CASY Pulse Area Analysis variant of Coulter-principle particle counting: instead of peak-amplitude pulse detection (which conflates fast-transit small particles with slow-transit large particles), the CASY integrates each impedance pulse over time, yielding a true volume measurement; importantly, intact cell membranes block the electrolyte from penetrating the cell interior, so live cells appear to have their full hydrodynamic volume, while dead cells with permeabilized membranes appear shrunken to nuclear volume — providing label-free live/dead discrimination. Anticipates: stain-free viability discrimination via electrical sensing zone integration; the architectural choice of Pulse Area Analysis vs amplitude detection in Coulter-derivative instruments; the use of multiple aperture sizes (50, 60, 150 µm) in a single instrument enabling 0.7-200 µm dynamic range in one measurement. Important historical anchor for the bioprocess cell counting market dominated by image cytometry (Vi-CELL) and impedance (CASY) before flow cytometry routine.

## bioMérieux VITEK 2 Microbial ID/AST Test Card Fluidic Wells (2002)

- **id**: `biomerieux-vitek-2-card-fluidics`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: bioMérieux
- **disclosure**: bioMérieux VITEK 2 launch 1999; VITEK 2 Compact 2002; FDA 510(k) K022366; VITEK 2 XL launch 2009
- **ip status**: patented
- **prior art notes**: Discloses an automated microbial ID/AST card-based fluidic system: a credit-card-sized polystyrene cassette containing 64 isolated microwells, each pre-loaded with a different lyophilized substrate (sugars, amino acids, antibiotic dilutions); the card mates with a transfer tube dipped into the bacterial inoculum suspension, and the analyzer's vacuum chamber draws inoculum into all wells simultaneously; the card is then sealed and continuously incubated at 35.5 °C with kinetic optical readout (turbidity at 660 nm + colorimetric pH/redox indicators). Anticipates: vacuum-loaded multi-well microbiology cards as a fluidic primitive for parallel substrate testing; the 'transfer tube + manifold + sealed card' architecture distinguishing VITEK from microtiter plate ID systems. Foundational disclosure for automated clinical microbiology workflows.

## Lee Company / TTP Ventus Disc Pump (2009)

- **id**: `lee-company-disc-pump-piezoelectric`
- **corpus**: private
- **device class**: pump-component
- **creator**: TTP Ventus (TTP plc spinout); now The Lee Company
- **disclosure**: TTP Ventus disc pump technology, originally disclosed via TTP plc / Cambridge UK; commercialized; acquired by The Lee Company. See https://www.theleeco.com/disc-pumps/ and product datasheets.
- **ip status**: patented
- **prior art notes**: Discloses a small-form-factor piezoelectrically driven disc pump generating pressure or vacuum with pulsation-free output and infinite turndown ratio. Standard 'air-over-liquid' actuation pattern: pump moves gas, gas indirectly displaces liquid in tubing or chip. Anticipates: 29-mm-class piezoelectric pneumatic micropumps for diagnostics, infinite-turndown pneumatic actuation, and the air-over-liquid architectural pattern as a substitute for direct liquid pumping in microfluidic instrument design.

## Syrris Asia and Asia 320 modular flow chemistry platform (2010)

- **id**: `syrris-asia-platform`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Syrris Ltd. (Blacktrace Holdings, now Asynt)
- **disclosure**: Syrris Ltd. Asia product launch press release, June 2010; Asia 320 launch 2017; Syrris Asia user manual rev 4 (2014); product brochure https://syrris.com/products/asia-flow-chemistry/
- **ip status**: patented
- **prior art notes**: Distinct from base Syrris-flow-chemistry entry. Discloses (a) 'pressurized-syringe' pump with sealed reservoir and electronic pressure feedback eliminating pulsation typical of HPLC pumps; (b) the FLLEX inline liquid-liquid extraction unit using a hydrophobic porous PTFE membrane to phase-separate organic and aqueous flows continuously without settling tanks; (c) Asia 320 ultra-high-pressure variant for supercritical-like flow chemistry; (d) modular architecture with shared 19-inch rack and tablet-based control software. Anticipates patent claims to pressurized-reservoir pulsation-free pumps for flow chemistry, and to inline membrane LLE within the residence-time loop of a flow reactor.

## Elveflow OB1 pressure controller (2014)

- **id**: `elveflow-ob1-pressure-controller`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Elvesys / Elveflow
- **disclosure**: Elveflow OB1 product datasheet. https://www.elveflow.com/microfluidic-products/microfluidics-flow-control-systems/ob1-pressure-controller/
- **ip status**: trade-secret
- **prior art notes**: Commercial multi-channel pressure controller for microfluidics, providing precise gas-pressure regulation (mbar resolution) to drive air-over-liquid flow in chips. Anticipates: instrument-side pressure regulation as a substitute for syringe pumping, integrated PID feedback on multiple independent reservoirs, and the architectural pattern of decoupling instrument pressure delivery from chip-side fluidics.

## T&R Biofab IB3D / 3DX Multi-Head Bioprinter (2015)

- **id**: `tr-biofab-ib3d-bioprinter`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: T&R Biofab Co., Ltd. (Suwon, South Korea); founded by Prof. Dong-Woo Cho's POSTECH group
- **disclosure**: T&R Biofab Co., Ltd. (Korea) IB3D / 3DX product line; tnrbiofab.com; commercial release ~2015
- **ip status**: patented
- **prior art notes**: Discloses a multi-head bioprinter integrating thermoplastic-extrusion heads (PCL/PLGA scaffold material at melt temperature) with cell-laden hydrogel bioprinting heads (dECM, alginate, GelMA), enabling simultaneous deposition of structural scaffold and cellular components. Anticipates: (a) hybrid melt-extrusion plus low-temperature bioink architecture in a single machine, (b) dECM-bioink workflow productized into a commercial machine (lineage to Cho 2014 dECM Nature Communications paper), (c) Korean-origin bioprinter prior art for industrial scaffold-plus-cell platforms. Note: corpus already references POSTECH microfluidics broadly via postech-microfluidics-suh; this entry pins T&R Biofab specifically.

## CELLINK BIO X Pneumatic Bioprinthead (2016)

- **id**: `cellink-bio-x-pneumatic-printhead`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: CELLINK AB (Gothenburg, Sweden); now part of BICO Group
- **disclosure**: CELLINK BIO X 3D Bioprinter user manual (documents.thermofisher.com/TFS-Assets/ANZ/manuals/cellink-biox-3d-bioprinter-manual.pdf); BIO X pneumatic-printhead product page (cellink.com/product/bio-x-pneumatic-printhead/)
- **ip status**: patented
- **prior art notes**: Discloses a modular pneumatic bioprinthead that mounts on the BIO X bioprinter and accepts disposable polymer cartridges (3 mL or 10 mL) holding cell-laden bioink, with regulated external air pressure as the displacement actuator and an integrated heater on the cartridge wall (up to 65 °C) for temperature-sensitive bioinks. Anticipates: (a) modular swappable head architecture for multi-modal bioprinting on a single base machine (CELLINK BIO X / BIO X6 / BIONOVA) — concrete prior art against later 'modular bioprinter' claims, (b) disposable closed-cartridge bioink supply with integrated heater, (c) external-pneumatic actuation as a cell-friendly drive primitive. The head IS the microfluidic device — defining feature is per-cartridge pressure regulation feeding a small-bore needle producing extruded fibers ranging from ~100 µm to >1 mm.

## ISS WetLab-2 Real-Time RT-PCR on Station (2016)

- **id**: `iss-wetlab-2-rt-pcr-on-station`
- **corpus**: open
- **device class**: lab-on-chip
- **creator**: NASA Ames Research Center / Cepheid (SmartCycler thermal block heritage) / BioRad (CFX-derived optics)
- **disclosure**: Parra M et al., 'Microgravity validation of a novel system for RNA isolation and multiplex quantitative real time PCR analysis of gene expression on the International Space Station,' PLOS ONE 12(9):e0183480 (2017), doi:10.1371/journal.pone.0183480; NASA WetLab-2 facility description, ISS Research Office (2016)
- **ip status**: open-permissive
- **prior art notes**: Discloses an end-to-end RNA-extraction + RT-qPCR cartridge architecture qualified for microgravity. Element-by-element prior art: (a) the closed-cartridge magnetic-bead RNA extraction protocol with no open-air liquid transfer steps anticipates patents claiming aerosol-free spaceflight or BSL-3 nucleic acid extraction cartridges; (b) the validation of paramagnetic-bead binding/wash kinetics in zero-G is published prior art against any patent claiming novel microgravity-compatible bead handling; (c) the integration of off-the-shelf SmartCycler-class Peltier modules with a custom reaction tube format anticipates retrofit spaceflight diagnostic cartridge concepts. Combined with iss-biomolecule-sequencer-minion below, WetLab-2 establishes the full sample-prep + amplification + sequencing chain in spaceflight prior art.

## Mars 2020 Perseverance MOXIE (Mars Oxygen In-Situ Resource Utilization Experiment) (2017)

- **id**: `mars2020-moxie-electrolyzer`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: NASA Jet Propulsion Laboratory / MIT Haystack / Niels Bohr Institute / OxEon Energy
- **disclosure**: Hecht MH et al., 'Mars Oxygen ISRU Experiment (MOXIE),' Space Science Reviews 217:9 (2021), doi:10.1007/s11214-020-00782-8; Hoffman JA et al., 'Mars Oxygen ISRU Experiment (MOXIE)—preparing for human Mars exploration,' Science Advances 8:eabp8636 (2022)
- **ip status**: patented
- **prior art notes**: Discloses an integrated gas-fluidic cartridge architecture for planetary in-situ resource utilization: (a) scroll-compressor + HEPA particulate filter + 3D-printed superalloy manifold + solid-oxide electrolyzer stack + getter scrubber; (b) the gas-handling subsystem operates as a flow-controlled, feedback-loop system with mass-flow sensors at inlet and oxygen-purity sensors at the anode-side outlet. For 102/103 anticipation: the assembly anticipates patents on integrated planetary atmospheric processing cartridges that combine compression, filtration, electrolysis, and getter purification on a single thermally-managed substrate. The 3D-printed manifold subsystem (additively-manufactured Inconel internal flow paths) is itself prior art against any patent claiming additively-manufactured high-temperature gas-flow manifolds for spaceflight chemical reactors. The stack-level current-voltage feedback control across diurnal pressure variations anticipates closed-loop control patents for variable-input ISRU systems.

## OSIRIS-REx TAGSAM (Touch-and-Go Sample Acquisition Mechanism) (2017)

- **id**: `osiris-rex-tagsam-bennu-sample`
- **corpus**: academic
- **device class**: chip-holder
- **creator**: Lockheed Martin Space / NASA Goddard / University of Arizona (D. Lauretta PI)
- **disclosure**: Bierhaus EB et al., 'The OSIRIS-REx Spacecraft and the Touch-and-Go Sample Acquisition Mechanism (TAGSAM),' Space Science Reviews 214:107 (2018), doi:10.1007/s11214-018-0521-6; Lauretta DS et al., 'Asteroid (101955) Bennu in the laboratory: Properties of the sample collected by OSIRIS-REx,' Meteoritics & Planetary Science 59:2453 (2024)
- **ip status**: patented
- **prior art notes**: The TAGSAM head is a gas-fluidized sample acquisition cartridge — relevant to the microfluidics corpus as a non-canonical fluidic system: pressurized N2 jets fluidize asteroid regolith into the collection chamber, then the chamber is sealed with an O-ring against contamination. Element-by-element prior art for: (a) gas-fluidized loose-particulate sampling cartridges with sealed return architecture (anticipates terrestrial industrial fluid-bed dry-sample collectors and bio-aerosol capture cartridges); (b) the integration of multiple sample-capture methods on one head (gas jets + Velcro contact pads) anticipates patents claiming hybrid dry-sampling cartridges; (c) the curation chain from in-flight sealed canister -> Earth-return capsule -> JSC nitrogen glove-box curation establishes a published cleanroom protocol for friable carbonaceous samples that anticipates Mars Sample Return curation patents. Patent citation is for the Lockheed-developed sample capture architecture.

## Abbott i-STAT Alinity Handheld Blood Analysis Cartridge (2018)

- **id**: `abbott-istat-alinity-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Abbott Point of Care
- **disclosure**: Abbott i-STAT Alinity FDA 510(k) K172011 cleared 2018-01-10; product launch press release 2018-02
- **ip status**: patented
- **prior art notes**: Discloses a handheld POC cartridge that integrates: a sealed calibrant pouch ruptured by mechanical bladder actuation, a microfluidic channel transporting fluid past a linear array of thin-film electrochemical biosensors (each with patterned ion-selective membrane or amperometric enzyme layer), an air-segment introduction step that pushes the calibrant past the sensors before driving sample over them (single-point single-fluid calibration), and an electrical interface mating the cartridge sensor pads to the analyzer reader contacts. Anticipates: handheld electrochemistry POC cartridges with pre-loaded liquid calibrant and bladder-driven sample introduction; the i-STAT family extension where the same disposable serves multiple generations of analyzer hardware. Improvements over the i-STAT cg8+ entry (in corpus): updated cartridge optical/RFID identification and connectivity-ready sensor handshake protocol.

## Mars 2020 Perseverance PIXL (Planetary Instrument for X-ray Lithochemistry) (2020)

- **id**: `mars2020-pixl-fluidic-flush`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: NASA Jet Propulsion Laboratory (A. Allwood PI)
- **disclosure**: Allwood AC et al., 'PIXL: Planetary Instrument for X-ray Lithochemistry,' Space Science Reviews 216:134 (2020), doi:10.1007/s11214-020-00767-7
- **ip status**: public-domain
- **prior art notes**: PIXL's microfluidic relevance lies in its low-pressure helium gas purge subsystem and in being the most spatially-resolved astrobiology-grade elemental mapping instrument on another planet. Element-by-element prior art disclosure: (a) gas-purge enclosure of an X-ray beam path on a robotic arm as a workaround for thin-atmosphere absorption losses anticipates patents claiming pressurized-gas-purge atmospheric-isolation envelopes for spectroscopic instruments on planetary rovers, (b) the hexapod 6-DOF micro-positioning system with 50 µm placement repeatability for a microspectroscopy instrument anticipates equivalent industrial precision-fluidic-positioning patents, and (c) PIXL's tight co-registration with SHERLOC's deep-UV map provides prior art for any 'integrated multi-modal arm-mounted astrobiology head' architecture. Co-cite with mars2020-sherloc-spectrometer for the broader Mars 2020 arm-mounted instrument pattern.
