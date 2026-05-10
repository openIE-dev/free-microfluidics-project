---
title: architecture-multiplex-cartridge
parent: Cross-cuts
layout: default
---

# Cross-cut: `architecture-multiplex-cartridge`

**72 corpus entries disclose this subsystem.**

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

## Iain M. Banks Culture autodoc / medical bay (1987)

- **id**: `banks-culture-autodoc`
- **corpus**: fictional
- **device class**: fictional-laboratory
- **creator**: Iain M. Banks
- **disclosure**: Banks, I. M. Consider Phlebas. Macmillan, London, 1987. ISBN 0-333-44138-9. Autodocs further developed across the Culture sequence: The Player of Games (1988, ISBN 0-333-47110-5), Use of Weapons (1990, ISBN 0-316-90309-X), Excession (1996, ISBN 1-85723-394-8), Look to Windward (2000, ISBN 1-84149-027-8), Surface Detail (2010, ISBN 978-0-316-12340-2).
- **ip status**: fictional
- **prior art notes**: Long-running narrative depiction across 9+ Culture novels (1987-2012) of fully integrated bedside clinical platforms that perform: continuous whole-body biochemical assay; AI-driven differential diagnosis; on-demand synthesis of arbitrary therapeutics from elemental feedstock; targeted intracellular delivery; and neural-feedback-loop intervention. Banks's autodocs are described in repeated technical detail (e.g., Use of Weapons chapter dealing with Zakalwe's repair; Surface Detail's Lededje resurrection sequences) as integrated chemistry-on-demand systems with sub-cellular precision. Doctrinally citable as 102/103 prior art for the architectural class 'autonomous bedside platform combining real-time multi-analyte assay with on-demand synthesis of patient-specific therapeutics under closed-loop AI control'. The Vornado v. Hunter Fan precedent (a category disclosure need not be enabling to anticipate) makes this directly citable against any patent attempting to claim that architectural pattern as a generic invention.

## Quidel Triage MeterPro Immunoassay Cartridge (1995)

- **id**: `quidel-triage-meterpro-fluorescence-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Quidel (formerly Biosite, then Alere)
- **disclosure**: Biosite Triage launch 1995 (drug-of-abuse panel); Triage BNP first cardiac assay 2000-11 (FDA 510(k) K003425); Quidel acquisition of Alere/Biosite Triage 2017; ongoing assays through 2020s
- **ip status**: patented
- **prior art notes**: Discloses the Biosite Triage cartridge as the original quantitative fluorescent lateral flow immunoassay POC architecture: a hybrid cartridge integrating an injection-molded fluidic frame (sample addition, capillary metering, conjugate rehydration zone) with a nitrocellulose lateral-flow membrane carrying capture-antibody-coated test lines, all read by a benchtop fluorescence meter performing time-resolved fluorescence (TRF) on Eu-chelate labels (or fluorescent latex). Anticipates: quantitative-vs-qualitative lateral flow POC architecture using fluorescent labels and meter-based readout; the BNP/NT-proBNP heart-failure POC market built on this primitive (2000s); the cartridge-frame-plus-membrane fabrication pattern that influenced Sofia, BD Veritor (in corpus), Alere/Abbott IM, and Quidel's modern POC line. Foundational architectural disclosure dating to 1995.

## Roche Elecsys Electrochemiluminescence Reagent Cassette (1996)

- **id**: `roche-elecsys-ecl-reagent-cassette`
- **corpus**: private
- **device class**: consumable-bulk
- **creator**: Roche Diagnostics (formerly Boehringer Mannheim) / IGEN International (ECL chemistry)
- **disclosure**: Roche/Boehringer Mannheim Elecsys 2010 immunoassay analyzer launch 1996; J. Clin. Lab. Anal. 1998 evaluation; US patents 5,238,808 and 5,310,687 (Boehringer Mannheim ECL cell)
- **ip status**: patented
- **prior art notes**: Discloses a unified reagent cassette format for ECL immunoassay: barcoded multi-vial cassette with streptavidin-paramagnetic-bead phase + biotinylated capture antibody + ruthenium-labeled detection antibody; the analyzer pipettor draws metered volumes from each vial into a disposable measuring cell, incubates with sample, magnetically captures the bead-immune-complex at a platinum working electrode, washes with TPA buffer, and applies an oxidation pulse exciting Ru(bpy)3 ECL emission detected at 620 nm by a PMT. The cassette form factor and ECL chemistry constitute foundational disclosure for: barcoded ratiometric reagent cassettes with on-board lot tracking; ECL-on-electrode with magnetic-bead capture as a sensitivity-amplification fluidic primitive. Element-by-element coverage applicable to all Roche Cobas e-series analyzers (e411, e601, e801, e402, Cobas pro).

## Drew Scientific HemaVet 950 / 1500 Veterinary Hematology Analyzer (1996)

- **id**: `drew-scientific-hemavet-veterinary-cbc`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Drew Scientific (Erba Diagnostics)
- **disclosure**: Drew Scientific HemaVet 850/950 launch ~1996; HemaVet 1500 launch 2003; pivotal multi-species reference distribution publications by Provost, Vet Clin Pathol
- **ip status**: patented
- **prior art notes**: Discloses an impedance-only multi-species veterinary hematology analyzer optimized for low-volume rodent samples (20 µL): single Coulter-principle aperture with species-specific lysing reagents; differential by impedance-histogram peak deconvolution applying species-specific RBC/WBC/PLT volume distribution priors. Anticipates: low-cost impedance-only veterinary hematology suitable for academic/preclinical pharmacology where cost and rodent-sample volume dominate over diff-channel diversity. Distinct from IDEXX ProCyte Dx (impedance + flow cytometry, higher cost, in-clinic) and from Heska Element HT5 (image cytometry). Important architectural anchor for the segment of veterinary/preclinical hematology that doesn't need fluorescence cytometry.

## MicroCHIPS / Microchips Biotech Implantable Drug Reservoir Array (1999-01-28)

- **id**: `microchips-biotech-implantable-reservoir`
- **corpus**: private
- **device class**: valve-component
- **creator**: Microchips Biotech Inc. (Langer / Cima MIT spin-out)
- **disclosure**: Santini JT, Cima MJ, Langer R Nature 397:335-338 1999 doi:10.1038/16898; first-in-human Farra R et al. Sci Transl Med 4(122):122ra21 2012 doi:10.1126/scitranslmed.3003276
- **ip status**: patented
- **prior art notes**: Foundational disclosure of an implantable drug-reservoir microchip: silicon substrate with micromachined wells (each holding sub-microliter to nanoliter dose), each well capped by a thin gold membrane that serves both as a hermetic seal and as an anodic electrode. Application of a small potential in chloride-containing biological fluid electrochemically dissolves the chosen membrane, releasing reservoir contents. Anticipates: addressable on-demand microreservoir drug delivery in implantable form; electrochemical-membrane-as-valve architecture; silicon-DRIE fabrication of multi-well drug-storage arrays.

## bioMérieux VITEK 2 Microbial ID/AST Test Card Fluidic Wells (2002)

- **id**: `biomerieux-vitek-2-card-fluidics`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: bioMérieux
- **disclosure**: bioMérieux VITEK 2 launch 1999; VITEK 2 Compact 2002; FDA 510(k) K022366; VITEK 2 XL launch 2009
- **ip status**: patented
- **prior art notes**: Discloses an automated microbial ID/AST card-based fluidic system: a credit-card-sized polystyrene cassette containing 64 isolated microwells, each pre-loaded with a different lyophilized substrate (sugars, amino acids, antibiotic dilutions); the card mates with a transfer tube dipped into the bacterial inoculum suspension, and the analyzer's vacuum chamber draws inoculum into all wells simultaneously; the card is then sealed and continuously incubated at 35.5 °C with kinetic optical readout (turbidity at 660 nm + colorimetric pH/redox indicators). Anticipates: vacuum-loaded multi-well microbiology cards as a fluidic primitive for parallel substrate testing; the 'transfer tube + manifold + sealed card' architecture distinguishing VITEK from microtiter plate ID systems. Foundational disclosure for automated clinical microbiology workflows.

## Neal Asher Polity autodoc (2002)

- **id**: `asher-polity-autodoc`
- **corpus**: fictional
- **device class**: fictional-laboratory
- **creator**: Neal Asher
- **disclosure**: Asher, N. The Skinner. Macmillan, London, 2002. ISBN 0-333-90160-4. Polity autodocs developed across the Spatterjay trilogy, Brass Man (2005), Polity Agent (2006), Hilldiggers (2007), Shadow of the Scorpion (2008), Dark Intelligence (2015), The Soldier (2018).
- **ip status**: fictional
- **prior art notes**: Asher's Polity autodocs are the most extensively-described autonomous bedside platforms in published SF — he repeatedly devotes pages of technical exposition to their internal subsystems, including microfluidic distribution networks, integrated synthesis chambers, multi-arm surgical end-effectors, and AI-supervised differential diagnosis. Architecturally discloses every subsystem of an integrated bedside autonomous trauma-care platform: real-time multi-analyte assay; on-demand drug synthesis; mechanical surgical intervention; tissue printing; and neural-interface diagnostic capability. The Polity series collectively constitutes a multi-decade fictional design exercise of this device category. Particularly strong 102 prior art for portable / field-deployable autodoc patents because Asher specifically depicts both hospital-grade and field-grade variants.

## Theranos Edison / miniLab cartridge (claimed) (2003)

- **id**: `theranos-promised-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Theranos Inc.
- **disclosure**: Theranos Inc. patent filings beginning 2003 (US7635594B2 and family); SEC v. Theranos litigation record.
- **ip status**: patented
- **prior art notes**: Patent filings disclosed an asserted single-cartridge multi-test blood diagnostic platform from finger-stick volumes. The filings stand as 102/103 art regardless of whether the company successfully reduced to practice; many subsequent POC-blood patents must contend with these filings as anticipating prior art for 'finger-stick-volume multi-assay cartridge as architecture.' Inclusion in this corpus is not an endorsement of the product's claimed performance.

## Abbott Cell-Dyn Sapphire Hematology Optical/Impedance Flow Cell (2003)

- **id**: `abbott-cell-dyn-sapphire-flow-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Abbott Laboratories (Abbott Hematology / Cell-Dyn)
- **disclosure**: Abbott Cell-Dyn Sapphire 510(k) K022428 (cleared 2003-04); peer-reviewed evaluation Bruegel et al., Clin Lab Haematol 2004
- **ip status**: patented
- **prior art notes**: Discloses Multi-Angle Polarized Scatter Separation (MAPSS) optical flow cytometry for white-blood-cell five-part differentiation: hydrodynamically focused single-cell stream illuminated at four angles (intermediate-angle scatter, polarized side scatter, depolarized side scatter, axial light loss) plus 488 nm laser fluorescence channel for retic/NRBC. The fluidic architecture pairs a sheath-focused optical flow cell for WBC/diff/retic with a Coulter-principle sapphire impedance aperture for RBC/PLT in parallel, with shared sample dilution stages. Anticipates: hybrid optical-impedance hematology fluidic stages sharing sample dilution; depolarized side-scatter eosinophil identification via crystalline content; sapphire as orifice material for impedance counting (durability against erosion vs ruby/glass).

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

## Leica Bond-III automated immunohistochemistry stainer (2007)

- **id**: `leica-bond-iii-staining`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Leica Biosystems (Danaher)
- **disclosure**: Leica Biosystems Bond-III. https://www.leicabiosystems.com
- **ip status**: patented
- **prior art notes**: Automated immunohistochemistry (IHC) stainer with cartridge-format reagent dispensers and slide-format flow chamber. Used widely in pathology labs worldwide. The Bond cartridge architecture is microfluidic-equivalent at scale: each tissue slide becomes a flow chamber for sequential reagent washes via the integrated dispenser. Reference for the broader pathology-automation cartridge segment.

## Roche Cobas 6000 Modular Analyzer Fluidic Track (2007)

- **id**: `roche-cobas-6000-modular-fluidics`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Roche Diagnostics
- **disclosure**: Roche Diagnostics Cobas 6000 product launch 2007; AACC product showcase; FDA 510(k) K072321 (c501 module)
- **ip status**: patented
- **prior art notes**: Discloses a modular clinical analyzer fluidics architecture: a single primary-tube sample-handling rail introduces blood/serum/plasma to multiple specialized assay modules (photometric c501 with permanent cuvette wheel; electrochemiluminescence e601 with disposable ECL cups containing electrode-paramagnetic-bead capture). The c501 module uses a thermostatted rotary cuvette wheel with washable permanent cuvettes; the e601 uses single-use polypropylene assay cups with integrated read-while-flow ECL detection at a Pt working electrode. Anticipates: hybrid permanent-cuvette + disposable-cup analyzer trains; ruthenium-tag ECL detection in disposable cups with paramagnetic bead capture and on-electrode wash; modular interconnect of clinical chemistry and immunoassay sharing primary-tube sample handler.

## Stago STA R Max Coagulation Analyzer Cuvette Ball Mixer (2007)

- **id**: `stago-sta-r-max-coag-fluidics`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Diagnostica Stago
- **disclosure**: Stago STA R Evolution launch 2007; STA R Max launch 2014; FDA 510(k) K082437; mechanical viscosity detection patent US4319194 (Stago 1982)
- **ip status**: patented
- **prior art notes**: Discloses Stago's signature mechanical clot detection: the assay cuvette contains a small steel ball oscillated by an external rotating magnetic field; as plasma coagulation progresses, viscosity rises, dampening ball oscillation amplitude/phase, sensed by a Hall-effect or coil pickup. Unlike optical (Werfen ACL TOP) or chromogenic (Sysmex CS) detection, the viscosity-based primitive is immune to chyle/hemolysis/icterus optical interference — enabling testing on samples that would fail other analyzers. Anticipates: magneto-mechanical viscosity-based clot detection in disposable cuvettes; the architectural choice of pre-loading the ball into the cuvette during manufacture (vs adding it at runtime). Defines the commercial niche for centers with high pediatric / hemolyzed sample loads.

## BioFire FilmArray multiplex PCR cartridge (2008)

- **id**: `biofire-filmarray-multiplex-pcr-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: BioFire Diagnostics (Idaho Technology origin); BioMérieux subsidiary
- **disclosure**: Idaho Technology Inc. (now BioFire Diagnostics, BioMérieux). FilmArray system. FDA 510(k) clearances K103175 (2011) and subsequent panels.
- **ip status**: patented
- **prior art notes**: Discloses a single-use disposable cartridge integrating sample preparation, nucleic acid extraction, multiplex nested PCR, and array-based detection in a closed pouch format. Anticipates: blister-pack on-cartridge reagent storage, foil-piercing actuation, multilayer thermoplastic lamination as a fabrication path for point-of-care molecular diagnostics, integrated thermal cycling within a sealed pouch, and the architectural pattern of 'sample-in / answer-out' multiplex IVD cartridges. The dominant commercial implementation in syndromic panel testing.

## Siemens RAPIDPoint 500 Blood Gas Cartridge (2008)

- **id**: `siemens-rapidpoint-500-blood-gas-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Siemens Healthineers (formerly Bayer Diagnostics)
- **disclosure**: Siemens RAPIDPoint 500 510(k) K080776 cleared 2008; product datasheet 2008-09; predecessor RAPIDLab 1265 patents (Bayer Diagnostics)
- **ip status**: patented
- **prior art notes**: Discloses an all-in-one POC blood gas cartridge integrating: thick-film potentiometric ISE array (pH, pCO2, pNa, pK, pCa, pCl), amperometric pO2 + glucose + lactate enzyme electrodes, and a multi-wavelength CO-oximetry cuvette for total Hb fractionation, all sharing a peristaltic-pump-driven flow path; reagent/calibrant/wash bags integrated into the cartridge body and pierced by mechanical actuators inside the analyzer; auto-calibration runs between samples without user intervention; cartridge-resident sample volume <100 µL. Anticipates: long-life POC blood-gas cartridges with on-board reagent storage and integrated CO-oximetry — the architectural pattern dominating ICU/ER/OR analyzers. Differs from Werfen GEM Premier (separate entry) in cartridge design (Siemens' 'measurement cartridge' separates sensors from reagents).

## Thermo Fisher Phadia 2500 Allergy/Autoimmune ImmunoCAP Cartridge (2008)

- **id**: `thermo-fisher-phadia-2500-immunoassay`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Thermo Fisher Scientific (formerly Phadia AB / Pharmacia Diagnostics)
- **disclosure**: Phadia 2500 launch 2008; Phadia 5000 launch 2009; FDA 510(k) K071727 (Phadia 250 predecessor); ImmunoCAP first cleared 1989
- **ip status**: patented
- **prior art notes**: Discloses the ImmunoCAP solid-phase fluorescent enzyme immunoassay: a cellulose-based 3D porous matrix in a capsule, derivatized with allergen, providing massively expanded surface area (vs flat-bottom microtiter wells) for IgE binding kinetics; the capsule is the disposable assay element, transported through automated wash, conjugate, and substrate steps in a Phadia rotor analyzer. Anticipates: 3D porous solid-phase immunoassay matrices as the binding-kinetics primitive distinguishing allergy testing (which requires capturing very low IgE concentrations against extract heterogeneity); the WHO IgE calibration traceability that established Phadia/ImmunoCAP as the global allergy reference. Element-by-element architectural disclosure relevant to all derivative ImmunoCAP assays (Phadia 100, 250, 1000, 2500, 5000).

## Sartorius ambr 15 microbioreactor system (2009)

- **id**: `sartorius-ambr-15`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Sartorius Stedim Biotech (formerly TAP Biosystems)
- **disclosure**: TAP Biosystems (acquired by Sartorius 2013) ambr 15 launch 2009. Bareither, R.; Pollard, D. A review of advanced small-scale parallel bioreactor technology for accelerated process development. Biotechnol. Prog. 2011, 27:2-14. doi:10.1002/btpr.522. Patent family: US8501462B2 (TAP Biosystems; priority 2007).
- **ip status**: patented
- **prior art notes**: Discloses a parallel-array microbioreactor system in which 24-48 single-use stirred-tank vessels of 10-15 mL working volume are simultaneously controlled with individual DO, pH, temperature, and gas-mix feedback, fed and sampled by a robotic pipettor. Anticipates: (a) parallel-microbioreactor process development as a category, including for CGT cell-line characterization; (b) robotic-pipettor-fed parallel small-scale stirred-tank arrays; (c) computer-vision and impedance-based monitoring of individual microbioreactor wells for AI-driven design-of-experiment process optimization.

## Roche Cobas u 411 Urine Test Strip Reflectance Fluidic Path (2009)

- **id**: `roche-cobas-u-411-urinalysis-strip-fluidics`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Roche Diagnostics
- **disclosure**: Roche Cobas u 411 product launch 2009; CE-IVD; predecessor: Boehringer Mannheim Reflotron (1986). FDA 510(k) K093266
- **ip status**: patented
- **prior art notes**: Discloses an automated reflectance urinalysis fluidic system: hopper-fed test strip dispenser, robotic positioning of strip under sample probe, sub-100 µL urine aliquot deposition onto each reagent pad, capillary wicking spread, and time-resolved reflectance read at multiple wavelengths through a moving optical head. Anticipates: dry-pad reagent strip + automated dose/read fluidic primitive for urinalysis (the dominant POC urinalysis architecture); reflectance correction for sample color (urobilinogen/bilirubin); the fluidic challenge of metering 25-50 µL droplets onto each of 11 absorbent pads without bleed-over.

## Roche MagNA Pure 96 Magnetic-Bead Nucleic Acid Extraction Cartridge (2009)

- **id**: `roche-magna-pure-96-extraction-cartridge`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Roche Molecular Systems
- **disclosure**: Roche MagNA Pure 96 product launch 2009-09; CE-IVD; product datasheet; FDA 510(k) K141195 (DNA/RNA extraction)
- **ip status**: patented
- **prior art notes**: Discloses a magnetic-bead nucleic acid extraction architecture using a magnetic rod inserted into and retracted from a tip-shrouded sleeve to capture/release silica-coated magnetic beads in successive wells of lysis, wash, and elution buffers — the 'Magtration'-style fluid handling distinct from open-well aspirate-based magnetic transfer. Anticipates: 96-well moving-magnet pipettor extraction systems; the 'tip-comb' format where each magnetic rod is sleeved by a disposable polypropylene tip preventing cross-contamination of the rod itself. Workflow improvement over manual Boom 1990 silica extraction (already in corpus, ID boom-1990-silica-magnetic-extraction).

## Radiometer ABL90 FLEX Blood Gas Analyzer Sensor Cassette (2009)

- **id**: `radiometer-abl90-flex-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Radiometer Medical (Danaher)
- **disclosure**: Radiometer ABL90 FLEX launch 2009-09; FDA 510(k) K093103; ABL90 FLEX PLUS update 2014
- **ip status**: patented
- **prior art notes**: Discloses a POC blood gas cartridge architecture distinguished by: (1) separable Sensor Cassette and Solution Pack — the user can replace one without the other based on usage profile, optimizing cost; (2) ultra-low 65 µL sample volume enabling neonatal capillary collection; (3) high-spectral-resolution CO-oximetry (256-wavelength photodiode array spectrophotometer in lieu of fixed-filter approach), enabling better discrimination of fetal Hb, sulfhemoglobin, and high MetHb fractions. The ABL90 family represents the third-generation Radiometer architecture (succeeding ABL700 series and ABL800). Anticipates: cartridge-and-pack separation as a fluidic-engineering pattern for cost-of-ownership optimization; high-spectral-resolution POC CO-oximetry; sub-100 µL POC blood gas + CO-oximetry. Companion to ABL800 FLEX (high-throughput central-lab variant).

## Ventana DISCOVERY ULTRA automated IHC stainer (2010)

- **id**: `ventana-discovery-ihc`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Roche Ventana Medical Systems
- **disclosure**: Roche Ventana Medical Systems DISCOVERY ULTRA. https://diagnostics.roche.com
- **ip status**: patented
- **prior art notes**: Automated IHC stainer competing with Leica Bond. Same architectural pattern: cartridge-format reagent dispensers + slide-format flow chamber + multi-reagent sequential wash. Roche Ventana cumulative patent estate covers much of the IHC automation market.

## Werfen ACL TOP 750 Coagulation Analyzer Optical Cuvette Train (2010)

- **id**: `werfen-acl-top-750-coag-optical`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Instrumentation Laboratory / Werfen
- **disclosure**: Instrumentation Laboratory ACL TOP 700 launch 2010; ACL TOP 750 launch 2014; FDA 510(k) K141728
- **ip status**: patented
- **prior art notes**: Discloses an optical-detection coagulation analyzer with a four-wavelength LED illumination + photodiode receiver per cuvette: 405 nm for clot turbidity (PT/aPTT) and chromogenic substrate absorbance (e.g., antithrombin); 575 nm correction wavelength for hemoglobin/icterus interference; 671 nm for immunoturbidimetric (D-dimer); 810 nm for HIL flagging and longer-wavelength immunoturbidimetric. The fluid handler integrates automated cap piercing, primary-tube sampling, automated dilutions, and on-board reagent reconstitution. Anticipates: multi-wavelength optical coag detection consolidating clot/chromogenic/immunoturbidimetric assays in a single-cuvette format; HIL flagging by absorbance ratiometry. Direct competitor architecture to Stago (mechanical) and Sysmex CS series.

## DiaSorin LIAISON XL Immunoassay Magnetic Bead Cuvette (2010)

- **id**: `diasorin-liaison-xl-magnetic-bead-cuvette`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: DiaSorin S.p.A.
- **disclosure**: DiaSorin LIAISON XL launch 2010-04; FDA 510(k) K100796 (25-OH Vitamin D), K113036 (BNP)
- **ip status**: patented
- **prior art notes**: Discloses an isoluminol-based flash chemiluminescence immunoassay analyzer using PMP capture: cuvette receives sample + PMP-coated capture antibody + isoluminol-conjugated detection antibody, magnetic capture and wash, then injection of trigger reagent (peroxide-base) generates isoluminol oxidation flash detected by PMT. The cuvette is single-use; the analyzer pipettor and magnet stations are washed between samples. Anticipates: isoluminol (vs acridinium ester, vs ECL ruthenium) as the chemiluminescence label class for high-throughput immunoassay; the global Vitamin D testing market built on this fluidic primitive (since 25-OH-D Total assay's 2010 standardization). Distinct from Roche Elecsys (ECL) and Beckman DxI (alkaline phosphatase + dioxetane glow).

## IDEXX ProCyte Dx Veterinary Hematology Analyzer Optical/Impedance Flow Cell (2010)

- **id**: `idexx-procyte-dx-veterinary-hematology`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: IDEXX Laboratories
- **disclosure**: IDEXX ProCyte Dx launch 2010-09; ProCyte One launch 2020-06
- **ip status**: patented
- **prior art notes**: Discloses an in-clinic veterinary hematology analyzer based on a Sysmex-licensed dual-modality flow cell (impedance + flow cytometry with side scatter and side fluorescence), ported to a compact bench-top form factor with species-specific reagent and algorithm sets. Anticipates: in-clinic veterinary applications of hybrid impedance + optical hematology platforms; the multi-species calibration architecture (RBC volume, MCV, WBC subtype distributions vary substantially across species — the analyzer must select species-specific reference distributions). Important prior art for the veterinary in-clinic hematology market as it differentiates from human-clinical-only platforms (Sysmex XN, Beckman DxH, Mindray BC). Companion to ProCyte One (2020) which uses a different IDEXX-internal optical fluorescent imaging architecture rather than Sysmex licensure.

## Beckman Coulter AU5800 Clinical Chemistry Analyzer Cuvette Wheel (2011)

- **id**: `beckman-coulter-au5800-cuvette-wheel`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Beckman Coulter (Danaher), originally Olympus Diagnostics
- **disclosure**: Beckman Coulter AU5800 product launch 2011-07; legacy: Olympus AU640/2700 since mid-1990s; FDA 510(k) K112094
- **ip status**: patented
- **prior art notes**: Discloses the canonical Olympus-AU clinical chemistry fluidics: a 165-cuvette permanent fused-quartz wheel in a 37 °C water bath, indexed past a multi-channel pipettor and a 13-wavelength photometer (340-800 nm); each cuvette is washed and air-dried in a programmed wash station between assay cycles. The fluid handler uses ceramic-piston syringes for sub-microliter dispense precision (1 µL reagent metering uncertainty < 1%); per-cuvette mixing is via paddle stirrer that descends, oscillates, and is washed in a separate station. Anticipates: the dominant 'permanent cuvette wheel + multi-pipettor + multi-wavelength photometer' fluidics architecture for >50% of central-lab clinical chemistry installations globally. Element-by-element: wash/dry station, cuvette indexing, ceramic-piston metering, paddle-stirrer mixing, in-cuvette photometric kinetics. Distinct from Roche c-series (cuvette material/wash) and Abbott Alinity c (wheel size, throughput).

## Mindray BC-6800 Hematology Analyzer SF Cube Flow Cell (2011)

- **id**: `mindray-bc-6800-hematology-flow-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Shenzhen Mindray Bio-Medical Electronics
- **disclosure**: Mindray BC-6800 launch 2011-11; FDA 510(k) K121734; BC-7500 launch 2018
- **ip status**: patented
- **prior art notes**: Discloses the SF Cube hematology flow-cell architecture: a single sheath-focused stream subjected to both impedance counting (sapphire aperture for RBC/PLT) and downstream optical interrogation by 633 nm laser with side-scatter + dual-wavelength side-fluorescence channels (one for nucleic-acid binding dye discriminating reticulocytes/NRBC, one for cytoplasmic dye discriminating granulocyte subclasses). Three-axis (SSC × SFL1 × SFL2) cytogram enables 5-part diff with built-in IG (immature granulocyte) detection. Anticipates: dual-wavelength fluorescence + scatter cytometry on a single hematology flow cell (independent prior art relative to Sysmex XN/Beckman DxH but architecturally similar) — strengthening the commons against narrow-claim assertions on this design space.

## Quanterix Simoa HD-X / HD-1 Single-Molecule Array Bead Cartridge (2011)

- **id**: `quanterix-simoa-hd-x-bead-cartridge`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Quanterix Corporation
- **disclosure**: Quanterix Simoa HD-1 launch 2014-02 (commercial); HD-X launch 2017-09; founding paper Rissin et al. Nat. Biotechnol. 2010 (already in corpus as rissin-2010-quanterix-simoa); FDA 510(k) K181616 (Simoa Nf-Light)
- **ip status**: patented
- **prior art notes**: Discloses the commercial Simoa fluidic platform: capture beads functionalized with antibody capture single-molecule analyte; bead suspension is loaded onto an injection-molded cyclic-olefin-polymer femtoliter microwell array disc (each array contains ~216,000 50 fL wells, sized to seat exactly one bead per well); fluorocarbon oil seals each well, isolating it as a digital reaction chamber; β-galactosidase-mediated cleavage of RGP in 'on' wells produces resorufin fluorescence detectable by CCD imaging — enabling binary single-molecule counting (digital ELISA). Anticipates: commercial-scale single-molecule immunoassay cartridges with sealed femtoliter wells; 24-array disposable disc format; the architectural pattern of bead-as-capture + microwell-as-digital-counter + oil-seal-as-isolation that defines digital immunoassay. Companion (Sherman et al. patent family) covers the 24-array disc geometry and bead-loading pipettor sequence not detailed in the academic Rissin 2010 paper.

## Sysmex XN-9000 Modular Hematology Track Sample-Aspiration Subsystem (2011)

- **id**: `sysmex-xn-9000-track-hematology`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Sysmex Corporation
- **disclosure**: Sysmex XN-Series launch 2011-09; XN-9000 modular configuration 2013; FDA 510(k) K112763 (XN); extends sysmex-cbc-cartridge entry already in corpus
- **ip status**: patented
- **prior art notes**: Discloses the Sysmex XN-9000 modular hematology track architecture extending the existing sysmex-cbc-cartridge entry (in corpus) with: (1) primary-tube cap-piercing sample aspiration sharing one probe across multiple downstream analyzer modules; (2) the WDF channel using a polymethine fluorescent dye that selectively stains WBC nucleic acid + cytoplasmic granularity, enabling true 5-part diff via two-color cytogram (side scatter × side fluorescence) — replacing the earlier-generation impedance-only differential; (3) the WPC channel using a different polymethine dye selective for blast cells, enabling automated reflexing for hematological malignancy screening; (4) the modular XN-9000 configuration linking up to 6 analyzer modules on a sample-routing track. Anticipates: high-throughput modular hematology with primary-tube cap-piercing + multi-channel optical/impedance + fluorescent intracellular staining for cell classification.

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

## MSL Sample Analysis at Mars (SAM) Wet Chemistry Cell with MTBSTFA Derivatization (2012)

- **id**: `msl-sam-wet-chemistry-cell`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: NASA Goddard Space Flight Center / Honeybee Robotics / GSFC SAM team (P. Mahaffy PI)
- **disclosure**: Mahaffy PR et al., 'The Sample Analysis at Mars Investigation and Instrument Suite,' Space Science Reviews 170:401-478 (2012), doi:10.1007/s11214-012-9879-z; Glavin DP et al., 'Evidence for perchlorates and the origin of chlorinated hydrocarbons detected by SAM at the Rocknest aeolian deposit in Gale Crater,' JGR Planets 118:1955-1973 (2013)
- **ip status**: public-domain
- **prior art notes**: Discloses a sealed reagent-cup architecture for in-situ wet chemistry on a planetary surface: a metal cup with crimped foil seal containing premixed MTBSTFA/DMF derivatization reagent at flight-storage temperature; the cup is mechanically pierced (foil-pierce actuation analogous to terrestrial blister-pack diagnostics), the regolith aliquot is dropped in, and the cup is heated stepwise to release derivatized analytes into the GCMS gas train. For 102/103 anticipation: (a) the foil-pierce + sealed-reagent + thermal-release architecture anticipates any patent claiming a single-use derivatization cartridge for sample-prep before MS, (b) the use of MTBSTFA specifically for in-situ silylation of amino acids/carboxylic acids in the presence of perchlorate oxidizers anticipates Mars/Europa/Enceladus life-detection cartridges that propose perchlorate-tolerant derivatization, and (c) the carousel architecture with mixed wet-chem and pyrolysis-only cups anticipates multi-modal sample-prep cartridges. The post-flight realization that perchlorate combustion was destroying organics during pyrolysis (Glavin 2013) is itself prior art against any claim that perchlorate-mitigation derivatization is novel for astrobiology applications.

## Dako Omnis IHC / ISH stainer (2013)

- **id**: `dako-omnis-stainer`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Agilent Dako
- **disclosure**: Agilent Dako Omnis. https://www.agilent.com/en/products/dako
- **ip status**: patented
- **prior art notes**: Third major IHC automation platform competing with Leica Bond and Ventana DISCOVERY. Architectural sibling — cartridge dispensers + slide flow chambers. Reference for the broader pathology automation patent thicket.

## Sartorius ambr 250 high-throughput single-use bioreactor (2013)

- **id**: `sartorius-ambr-250`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Sartorius Stedim Biotech
- **disclosure**: TAP Biosystems / Sartorius ambr 250 launch 2013. Tai, M. et al. ambr 250 use in CHO cell process development. Biotechnol. Prog. 2015, 31:1388-1395. doi:10.1002/btpr.2142. Patent family extends from US8501462B2.
- **ip status**: patented
- **prior art notes**: Mid-scale parallel-array stirred-tank microbioreactor system bridging the ambr 15 and pilot-scale bioreactors. Anticipates: scale-down models of 2000 L commercial bioreactors implemented as parallel 100-250 mL single-use vessels with matched mixing and aeration characteristics, used as the FDA-recognized scale-down qualification approach for bioprocess development. The ambr 250 HT perfusion variant additionally anticipates integration of single-use cell-retention devices (ATF/TFF) into a parallel-array small-scale platform.

## GenMark ePlex cartridge (2014)

- **id**: `genmark-eplex-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: GenMark Diagnostics (acquired by Roche 2021)
- **disclosure**: GenMark Diagnostics (now Roche) ePlex system. FDA 510(k) K161312 and family. https://www.genmarkdx.com/eplex/
- **ip status**: patented
- **prior art notes**: Disclosed a multiplex molecular diagnostic cartridge integrating sample prep, PCR amplification, and electrochemical detection on a printed gold electrode array (eSensor technology). Anticipates: electrochemical-array detection as alternative to optical fluorescence in syndromic POC molecular diagnostics, and the architectural pattern of integrating eSensor-style detection within a self-contained cartridge.

## CODEX multiplexed antibody imaging (Akoya CODEX/PhenoCycler) (2014)

- **id**: `goldman-2014-codex-akoya`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Nolan group, Stanford / Akoya Biosciences
- **disclosure**: Goltsev, Y.; Samusik, N.; Kennedy-Darling, J.; Bhate, S.; Hale, M.; Vazquez, G.; Black, S.; Nolan, G. P. Deep profiling of mouse splenic architecture with CODEX multiplexed imaging. Cell 2018, 174, 968–981.e15. DOI: 10.1016/j.cell.2018.07.010
- **ip status**: patented
- **prior art notes**: Disclosed iterative-fluidic-cycling multiplexed immunofluorescence: oligonucleotide-tagged antibodies are revealed sequentially by complementary fluorophore-coupled reporters delivered through an automated fluidic cycler atop a tissue-section flow cell. Anticipates: iterative-fluidic-multiplexing architecture for spatial proteomics, and the Akoya PhenoCycler commercial platform.

## Haemonetics TEG 6s Thromboelastography Microfluidic Cartridge (2014)

- **id**: `mindray-teg-6s-thromboelastography-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Haemonetics Corporation
- **disclosure**: Haemonetics TEG 6s 510(k) K151967 cleared 2017-02 (US); CE-IVD 2014; technology origin: Cora Healthcare acquired by Haemonetics 2010
- **ip status**: patented
- **prior art notes**: Discloses a microfluidic cartridge-based viscoelastic hemostasis analyzer using mechanical resonance frequency detection rather than the historic torque-pin method (TEG 5000, ROTEM): the cartridge is excited by piezoelectric driver at ~0.06 Hz; an LED illuminates the blood-air meniscus inside each microwell; clot formation increases mechanical coupling between the resonating cartridge wall and the meniscus, modulating the meniscus position which is detected by photodiode displacement sensor — yielding a TEG-equivalent amplitude trace (R, K, alpha, MA) without any moving torque pin in the blood. Anticipates: cartridge-resident viscoelastic hemostasis testing eliminating the cup-and-pin mechanism; the architectural choice of resonance-shift detection enabling vibration tolerance suitable for transport / cardiac OR. Distinct from ROTEM sigma (Werfen) which uses electromechanical detection in a similar cartridge format.

## Sysmex CS-2500 / CN-6000 Coagulation Analyzer Multi-Wavelength Cuvette (2014)

- **id**: `sysmex-cs-2500-coag-automated`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Sysmex Corporation (in partnership with Siemens for hemostasis menu)
- **disclosure**: Sysmex CS-2500 launch 2014-04; CN-6000 (next-gen) launch 2018; FDA 510(k) K140617 (CS-2500)
- **ip status**: patented
- **prior art notes**: Discloses a coagulation analyzer with pre-analytical HIL flagging integrated into the same cuvette as the assay measurement: before reagent dispense, the analyzer reads plasma absorbance at 340/405/575/660/800 nm to detect hemoglobin (free Hb >0.2 g/dL), bilirubin, and lipid scattering, allowing the analyzer to skip or reflex assays whose chemistry is invalidated by interference (e.g., D-dimer immunoturbidimetric is invalidated by lipemia). The five-wavelength optical detection consolidates clot turbidity (PT/aPTT), chromogenic substrate hydrolysis (chromogenic factor activity), and immunoturbidimetric (D-dimer, antithrombin antigen) in a single cuvette type. Anticipates: pre-analytical HIL detection in the assay cuvette as a fluidic-engineering primitive enabling reflex routing; multi-wavelength optical detection consolidating diverse coag chemistries in one cuvette; the Sysmex/Siemens partnership architecture (Sysmex hardware + Siemens HemosIL-equivalent reagent menu).

## Takara Bio iCell8 cx Single-Cell System (Wafergen) (2014)

- **id**: `takara-icell8-cx`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Wafergen Biosystems / Takara Bio
- **disclosure**: Wafergen Biosystems ICELL8 launch 2014; acquired by Takara Bio 2018. https://www.takarabio.com/products/automation-systems/icell8-system-and-software. Goldstein, L. D. et al. Massively parallel nanowell-based single-cell gene expression profiling. BMC Genomics 2017, 18, 519. DOI: 10.1186/s12864-017-3893-1.
- **ip status**: patented
- **prior art notes**: Image-guided single-cell dispensing into a silicon nanowell chip: a MultiSample NanoDispenser deposits ~50 nL droplets across a 5,184-well chip, on-chip imaging identifies single-cell-containing wells, and only those wells receive downstream reagents. Anticipates: image-guided 'select-then-dispense' single-cell architectures, distinct from Poisson-loaded microwell or droplet platforms; integration of computer-vision feedback into the cell-loading step. The 'pick-only-the-good-wells' architecture is a meaningful prior-art point against later image-feedback single-cell systems (e.g., Cytena, NanoCellect).

## Werfen GEM Premier 5000 Blood Gas Multi-Use Cartridge (2015)

- **id**: `werfen-gem-premier-5000-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Instrumentation Laboratory / Werfen
- **disclosure**: Werfen GEM Premier 5000 launch 2015-12; FDA 510(k) K151867; predecessor entry: instrumentation-laboratory-gem-premier (already in corpus, GEM Premier 4000)
- **ip status**: patented
- **prior art notes**: Discloses a self-contained 'Multi-Use' blood gas cartridge integrating sensors, reagents, calibrants, and waste in a single disposable; the analyzer hardware is reduced to a peristaltic pump, optical bench, electrical interface, and barcode/RFID reader. The cartridge architecture eliminates the user-serviced reagent/waste/sensor reservoirs that defined earlier blood gas analyzers, producing a sealed-system architecture comparable to Siemens RAPIDPoint 500 (separate entry) — with key differentiator: GEM uses a single integrated cartridge whereas Siemens separates 'measurement cartridge' from 'reagent cartridge.' The Werfen iQM (and iQM2) protocol replaces traditional periodic external QC with continuous on-cartridge QC sample passes between patient samples. Anticipates: fully sealed POC blood gas cartridges with on-board waste containment; continuous-QC architectures replacing periodic 2-3 level external QC; cartridge as the disposable failure-mode boundary.

## Epicore Biosystems Microfluidic Sweat Sensor Patch (2016-11-23)

- **id**: `epicore-biosystems-sweat-patch`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Epicore Biosystems Inc. (Northwestern / Rogers spin-out)
- **disclosure**: Koh A et al. Sci Transl Med 8(366):366ra165 2016 doi:10.1126/scitranslmed.aaf2593 (already in corpus as koh-rogers-2016-epidermal-microfluidic — this entry covers the Epicore commercial product line spun out from Rogers lab)
- **ip status**: patented
- **prior art notes**: Commercial product line built around the Rogers-lab epidermal microfluidic platform (academic disclosure already covered by koh-rogers-2016-epidermal-microfluidic). Discloses skin-adhered PDMS patches with sub-millimeter serpentine channels routing sweat into discrete colorimetric assay chambers (chloride, glucose, lactate, pH) that change color as sweat fills them, read by smartphone camera. Anticipates: capillary-driven sweat sample collection at gland scale (microliter volumes); multi-analyte colorimetric reservoir architecture in a wearable patch; Gatorade Gx and Connected Hydration commercial implementations.

## Abbott Alinity i Immunoassay Analyzer Fluidic Subsystem (2017)

- **id**: `abbott-alinity-i-immunoassay-fluidics`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Abbott Laboratories (Abbott Diagnostics Division)
- **disclosure**: Abbott Diagnostics Alinity i product launch press release 2017-09-19; Alinity i Operations Manual; FDA 510(k) K163388
- **ip status**: patented
- **prior art notes**: Discloses a continuous-access central-laboratory immunoassay analyzer with a single-use injection-molded reaction vessel (RV) per assay, a multi-arm robotic pipettor performing sample/diluent/microparticle/conjugate aspiration in metered sub-microliter volumes, an in-RV magnetic-bead capture wash station, and an integrated chemiluminescent detection cuvette. The fluidic architecture distinguishes from Architect i2000 (already in corpus, ID abbott-architect-i2000) by replacing the shared cuvette wash circuit with disposable RVs, eliminating cross-contamination paths. Anticipates: walk-away CMIA cartridge architectures using one-disposable-per-test with integrated mag-bead wash and flash chemiluminescence detection in the same vessel. Element-by-element coverage of: disposable PP reaction-vessel arrays presented in continuous queue; sample probe + reagent probes co-located over RV stations; pre-trigger and trigger reagent dispense; integrated PMT detection well.

## Abbott Alinity c Clinical Chemistry Analyzer Cuvette Wheel (2017)

- **id**: `abbott-alinity-c-clinical-chemistry-fluidics`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Abbott Laboratories
- **disclosure**: Abbott Diagnostics Alinity c product launch 2017-09-19; FDA 510(k) K163387
- **ip status**: patented
- **prior art notes**: Discloses a thermostatted reaction cuvette wheel with permanent fused-quartz cuvettes, a multi-channel sample/reagent pipettor metering with sub-microliter precision via ceramic syringes, an in-place wash/dry station between assay cycles, and an in-line ion-selective-electrode (ISE) module fed by the same primary sample probe. Anticipates: high-throughput central-lab photometric chemistry analyzers using a fixed-cuvette rotary wheel + spectrophotometer reading at multiple wavelengths through each cuvette as it rotates past a fixed light source; ISE module sharing pipettor metering with photometric channel. Differs from Roche Cobas c (in corpus) in cuvette material (fused quartz vs glass), wash sequence, and integration with Alinity i shared sample track.

## Abbott Alinity m Molecular Diagnostics Sample-to-Result Cartridge (2017)

- **id**: `abbott-alinity-m-molecular-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Abbott Laboratories (Abbott Molecular)
- **disclosure**: Abbott Alinity m CE-IVD launch 2018; FDA 510(k) K191601 (HBV viral load); product datasheet 2018-09
- **ip status**: patented
- **prior art notes**: Discloses a tip-and-vessel cartridge architecture for magnetic-bead nucleic-acid extraction integrated with on-board real-time PCR amplification: a disposable plastic tip aspirates sample, mixes with lysis buffer and silica-coated magnetic beads, and the bead pellet is washed and eluted in a thermally cycled microreactor instrumented with multiplex fluorescence detection. Anticipates: random-access viral load PCR with single-use extraction tips, eliminating cross-contamination of the analyzer fluid path; per-sample disposable amplification well used as the optical detection cuvette; pre-loaded reagent strip with foil-pierce sequencing. Distinct from Cepheid GeneXpert (corpus) in extraction modality (tip-suspended vs glass-fiber column) and from Roche Cobas Liat (corpus) in modular continuous queueing.

## Siemens Atellica CH 930 Clinical Chemistry Analyzer Cuvette Ring (2017)

- **id**: `siemens-atellica-ch-930-cuvette-ring`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Siemens Healthineers
- **disclosure**: Siemens Healthineers Atellica Solution launch 2017-02 (AACC); FDA 510(k) K163289
- **ip status**: patented
- **prior art notes**: Discloses a clinical analyzer fluidics architecture distinguished by magnetic-levitation-style sample tube transport (Atellica Magline): individual sample pucks ride on a programmable magnetic transport surface, allowing bidirectional, multi-speed routing without a continuous conveyor belt — pucks queue at any module entry point. The CH 930 module uses a 240-position permanent acrylic cuvette ring with thermal bath, a multi-channel pipettor metering reagent and sample, and a 13-wavelength photometer reading each cuvette as it indexes past the optical bench. Anticipates: magnetic-puck random-access sample transport for clinical analyzer trains (vs continuous belt); reagent container with embedded RFID for lot/expiry tracking on each load. Primary distinction from Roche Cobas 6000 and Abbott Alinity is the puck-based transport — a discrete-element sample handler.

## Siemens Atellica IM 1300 Immunoassay Analyzer Acridinium Cuvette Module (2017)

- **id**: `siemens-atellica-im-1300-immunoassay`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Siemens Healthineers
- **disclosure**: Siemens Healthineers Atellica Solution launch 2017-02; FDA 510(k) K163328
- **ip status**: patented
- **prior art notes**: Discloses an acridinium-ester chemiluminescence immunoassay fluidic module on the Atellica platform: paramagnetic latex particles (PMP) coated with capture antibody mix with sample and acridinium-labeled detection antibody in a single-use polystyrene cuvette; magnetic capture wash sequence; trigger-reagent injection (H2O2 acid + NaOH base) generates acridinium oxidation flash detected by PMT in 1-2 second integration window. Anticipates: combined CH/IM analyzer trains sharing Magline puck transport but using distinct cuvette/detection chemistries per module; PMP-vs-streptavidin-bead capture phase as a fluidic-engineering choice; flash chemiluminescence (vs ECL) as a competing detection primitive. Centroid of the Siemens immunoassay legacy from Centaur, Centaur XP, ADVIA Centaur to Atellica.

## Beckman Coulter DxH 900 Hematology VCSn Flow Cell (2017)

- **id**: `beckman-coulter-dxh-900-flow-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Beckman Coulter (Danaher)
- **disclosure**: Beckman Coulter DxH 900 launch 2017-08; FDA 510(k) K162970
- **ip status**: patented
- **prior art notes**: Discloses VCSn technology: simultaneous Volume (low-frequency Coulter impedance for DC volume), Conductivity (high-frequency RF impedance probing internal cell density), and 5-angle Light Scatter (axial light loss + multiple side-scatter angles for granularity, lobularity, complexity) in a single hydrodynamically-focused fluidic stage. The fluid path co-locates the impedance aperture and the optical interrogation zone so each cell event is measured by all modalities within microseconds. Anticipates: combined impedance + multi-angle scatter cytometry on a single flow cell for hematology classifier inputs; 'NEW' designation marks redesigned aperture geometry vs the LH series predecessor. Element-by-element: dilution chamber, sheath formation, aperture-with-electrodes, laser interrogation downstream, post-aperture flush.

## LumiraDx Point-of-Care Platform Microfluidic Test Strip (2017)

- **id**: `lumiradx-platform-microfluidic-strip`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: LumiraDx Limited
- **disclosure**: LumiraDx Platform CE-IVD launch 2017-12; SARS-CoV-2 Ag EUA 2020-08-18; INR strip 510(k) K191167; D-dimer 510(k) K203049
- **ip status**: patented
- **prior art notes**: Discloses a unified POC platform architecture: a single handheld electromechanical reader (with electrical contacts, optical excitation, and pneumatic/mechanical actuators) accepts a family of injection-molded microfluidic test strips, each pre-loaded with assay-specific dry reagents in metered zones along a capillary-driven flow path. The strip-level architecture pattern: sample inlet → capillary metering → dry-reagent rehydration mixer → optional incubation serpentine → detection chamber (electrochemical for INR/glucose; fluorescence for SARS-CoV-2 Ag, NT-proBNP, hsTnI). Anticipates: single-reader-multi-assay POC platforms using injection-molded microfluidic strips with assay-class-specific detection chambers; the commercial scaling pattern of strip manufacturing as the unit-economics enabler for menu breadth. Differs from i-STAT (single class: electrochemistry) and Sofia (single class: fluorescent immunoassay) by spanning electrochemistry + fluorescence on the same instrument.

## BD Rhapsody single-cell analysis system (2017)

- **id**: `bd-rhapsody-microwell`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: BD Biosciences (Cellular Research)
- **disclosure**: Fan, H. C., Fu, G. K., Fodor, S. P. A. Combinatorial labeling of single cells for gene expression cytometry. Science 2015, 347, 1258367. DOI: 10.1126/science.1258367. BD Rhapsody product launch press release, 2017 (BD acquired Cellular Research 2015).
- **ip status**: patented
- **prior art notes**: Microwell-array cartridge that loads single cells and barcoded capture beads pairwise into ~200k Poisson-loaded picoliter wells by gravity. Lysis is performed in-well, mRNA hybridizes to bead-bound poly-T capture probes, then beads are pooled for off-cartridge cDNA synthesis. Anticipates: pairwise cell+bead microwell loading at picoliter scale as an alternative to droplet co-encapsulation; the architecture explicitly trades throughput for elimination of moving fluidic parts. The Cellular Research / Fodor 2015 disclosure is the academic anchor for any microwell-based single-cell barcoding claim. Direct competitor architecture to 10x Chromium and HIVE.

## ExoMars Rosalind Franklin MOMA (Mars Organic Molecule Analyser) (2017)

- **id**: `exomars-moma-pyr-gcms-ldms`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Max Planck Institute for Solar System Research (MPS) / NASA GSFC / LISA / CNES / ESA / Thales Alenia Space
- **disclosure**: Goesmann F et al., 'The Mars Organic Molecule Analyzer (MOMA) Instrument: Characterization of Organic Material in Martian Sediments,' Astrobiology 17(6-7):655-685 (2017), doi:10.1089/ast.2016.1551
- **ip status**: public-domain
- **prior art notes**: Discloses a hybrid pyrolysis/derivatization/laser-desorption mass-spec instrument with a 32-cell sealed-cup carousel architecture as in-situ sample prep. Element-by-element disclosure: (a) the dual-front-end design (thermal pyrolysis path + UV-LDI path sharing a single ion trap) anticipates patents claiming dual-mode MS sample introduction for planetary life detection; (b) the chiral-column GC train specifically targeting amino-acid enantiomer ratios as a life-detection signature anticipates terrestrial commercial chiral-LC/GC cartridges marketed for biosignature discrimination; (c) the 2-meter subsurface drill aliquot pathway with sealed transfer to a sample carousel anticipates concepts for Europa Lander / Enceladus subsurface sample acquisition; (d) the perchlorate-bypassing LDI ionization mode anticipates any patent claiming non-thermal direct laser ionization for Mars/icy-moon refractory organics. MOMA is the European/American sister architecture to SAM and the most current public-domain disclosure of an integrated pyr-GCMS-LDMS planetary cartridge.

## Heska Element HT5 Veterinary Hematology Image Cytometry Analyzer (2018)

- **id**: `heska-element-ht5-veterinary-imaging`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Heska Corporation (now Mars Petcare)
- **disclosure**: Heska Element HT5 launch 2018-09; product datasheet; companion Heska 510(k) K200147
- **ip status**: patented
- **prior art notes**: Discloses an in-clinic veterinary hematology analyzer using image cytometry (vs flow cytometry) for the WBC differential: stained WBCs flow through a microfluidic imaging channel under high-magnification CCD imaging, and convolutional-neural-network (CNN)-based image classification produces 5-part diff plus reticulocyte count (since 2019 software updates). Distinguishes from IDEXX ProCyte Dx (Sysmex-licensed flow cytometry), Sysmex XN, Beckman DxH, and Mindray BC-6800 (all flow cytometry-based) by retaining actual cell images for veterinarian review — important in veterinary clinical pathology where edge cases (mast cell tumor mast cells in peripheral blood, exotic species hematology) benefit from image evidence. Anticipates: image-cytometry hematology as an alternative to flow cytometry; CNN-based image classification embedded in a clinical analyzer; the architectural choice of single-cuvette image + impedance hybrid (vs separate multi-channel architecture).

## Parse Biosciences Evercode split-pool single-cell kit (2018-04-13)

- **id**: `parse-biosciences-evercode`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Parse Biosciences (formerly Split Biosciences)
- **disclosure**: Rosenberg, A. B. et al. Single-cell profiling of the developing mouse brain and spinal cord with split-pool barcoding. Science 2018, 360, 176-182. DOI: 10.1126/science.aam8999. Parse Biosciences (Split Biosciences) commercial launch 2019.
- **ip status**: patented
- **prior art notes**: Combinatorial split-pool barcoding kit derived from the SPLiT-seq method (Rosenberg & Roco 2018). Each cell or nucleus is fixed and permeabilized, then distributed across plate wells through 3-4 sequential rounds of in-cell barcode oligo ligation/RT; the cell itself is the compartment, no droplet generator or microwell chip is required. Anticipates: instrument-free, plate-based combinatorial single-cell barcoding architectures; fixable-sample workflows for single-cell RNA-seq that decouple sample collection from library prep; the architectural distinction from 10x Chromium (no droplet microfluidics, only multichannel pipettors and 96-well plates) enabling sub-$1 per-cell economics at >100k cell scale. Also anticipates instrument-side passive fluidic handling consisting solely of plate transfer and centrifugation.

## MGI DNBSEQ-T7 flow cell (2018-10)

- **id**: `mgi-dnbseq-t7-flow-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: MGI Tech (BGI)
- **disclosure**: MGI Tech DNBSEQ-T7 launch at ICG-13, October 2018. https://en.mgi-tech.com/products/instruments_info/4/.
- **ip status**: patented
- **prior art notes**: High-throughput DNB-array sequencing instrument with four parallel patterned silicon flow cells. Each flow cell carries a high-density spot pattern matched to the nanoball size; nanoballs deposit one-per-spot for combinatorial probe-anchor-ligation sequencing. Anticipates: parallel-flow-cell ultra-throughput sequencer architectures, multi-flow-cell scheduling and reagent sharing, and the patterned-spot-plus-nanoball architecture at T7 scale. Distinguishes the T7 generation from the smaller G400 and the original DNBSEQ flow cell.

## Ori Biotech IRO cell therapy manufacturing platform (2019)

- **id**: `ori-biotech-iro`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Ori Biotech Ltd
- **disclosure**: Ori Biotech IRO platform. Press launch 2019; commercial availability 2023. https://www.oribiotech.com. Patent family: WO2018229497A1 / US11629322B2 (Ori Biotech Ltd; priority 2017).
- **ip status**: patented
- **prior art notes**: Discloses a closed-cartridge end-to-end CGT manufacturing system architecturally distinguished from Cellares Cell Shuttle and Lonza Cocoon by its emphasis on (a) decentralized hospital-deployable manufacturing rather than centralized factories; (b) in-line cell counting and viability sensing integrated within the cartridge fluidic path; (c) modular multi-cartridge-per-instrument architecture. Anticipates: distributed-manufacturing CGT cartridge instruments; in-cartridge sensor integration for real-time release-criterion monitoring; multi-tenant-batch CGT instruments supporting concurrent patient-specific runs.

## Biolinq Intradermal Microneedle CGM Patch (2019)

- **id**: `biolinq-intradermal-microneedle-cgm`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Biolinq Inc. (formerly Electrozyme)
- **disclosure**: Biolinq Inc. corporate disclosures; clinical trial NCT04790344 2021; Krishnan SR et al. for Biolinq founder publications
- **ip status**: patented
- **prior art notes**: Discloses a CGM patch in which an array of solid silicon microneedles is functionalized as electrochemical glucose sensors operating directly in epidermal interstitial fluid (~500 micron depth). The microneedle array is the sensor and the fluid envelope at the tip is the microfluidic. Anticipates: intradermal-microneedle-array CGM architectures; multi-microneedle redundant electrochemical sensing topologies; sub-dermal painless biosensor patches.

## Resolve Biosciences Molecular Cartography (2020)

- **id**: `resolve-bioscience-molecular-cartography`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Resolve Biosciences
- **disclosure**: Resolve Biosciences Molecular Cartography platform. https://resolvebiosciences.com/. Groiss, S. et al. Highly resolved spatial transcriptomics for detection of rare cell populations. bioRxiv 2021.10.11.463936. DOI: 10.1101/2021.10.11.463936.
- **ip status**: patented
- **prior art notes**: Subcellular-resolution spatial transcriptomics using sequential single-molecule FISH on a perfusion fluidic platform. Architecturally adjacent to MERSCOPE (Vizgen) and CosMx (NanoString) but with distinct decoding chemistry (Resolve uses a smaller number of imaging rounds with high-fidelity probe-pair decoding). Anticipates: alternative encoding schemes for multiplexed in-situ-hybridization spatial transcriptomics; a European competitor in the hybridization-cycle spatial omics race.

## Singleron Matrix microwell single-cell platform (2020)

- **id**: `singleron-matrix-microwell`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Singleron Biotechnologies
- **disclosure**: Singleron Biotechnologies Matrix product launch 2020. https://singleronbio.com/. Dura, B. et al. scFTD-seq: freeze-thaw lysis based, portable approach toward high-density scRNA-seq. Nucleic Acids Res. 2019, 47, e16. DOI: 10.1093/nar/gky1173 (foundational microwell architecture).
- **ip status**: unknown
- **prior art notes**: Microwell-array single-cell platform analogous to BD Rhapsody and HIVE: cells and barcoded beads gravity-loaded into picoliter microwells in a thermoplastic chip, lysed in-well, and beads collected magnetically. Anticipates: the architectural convergence on picoliter-microwell-plus-barcoded-bead single-cell prep across multiple vendors and geographies, which is a major prior-art counter to broad claims attempting to monopolize that architecture.

## Beckman Coulter DxI 9000 Access Immunoassay Reaction Vessel Track (2021)

- **id**: `beckman-coulter-dxi-9000-immunoassay`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Beckman Coulter (Danaher)
- **disclosure**: Beckman Coulter DxI 9000 launch 2021-09; FDA 510(k) K223188 (cleared 2023)
- **ip status**: patented
- **prior art notes**: Discloses a single-use reaction vessel immunoassay analyzer optimized for cardiac STAT throughput: each RV is loaded onto a continuous track, receives sample + PMP-conjugated capture antibody + alkaline-phosphatase-labeled detection antibody via independently controlled pipettors, undergoes magnet-station capture and wash within the same RV (no transfer), and is moved to the dioxetane-substrate dispense and PMT integration station. Anticipates: high-throughput single-use RV immunoassay tracks with in-vessel PMP wash; alkaline-phosphatase + Lumi-Phos 530 dioxetane chemiluminescence substrate (alternative to acridinium ester and ECL); the centralized fluidic path where sample-and-reagent transit is robotic but each RV is the immutable assay vessel. Foundational fluidic difference from Roche e-series (ECL on electrode) and Abbott Architect (CMIA flash on washed wells) — Beckman uses prolonged glow chemiluminescence integrated for 4-5 seconds.

## Vizgen MERSCOPE platform (2021-05-19)

- **id**: `vizgen-merscope`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Vizgen Inc.
- **disclosure**: Vizgen MERSCOPE product launch press release 2021-05-19. https://vizgen.com/. Chen, K. H. et al. Spatially resolved, highly multiplexed RNA profiling in single cells. Science 2015, 348, aaa6090. DOI: 10.1126/science.aaa6090.
- **ip status**: patented
- **prior art notes**: Commercial MERFISH (Multiplexed Error-Robust FISH) platform from the Zhuang lab spinout. A perfusion flow cell over the tissue cycles fluorescent readout probes; combinatorial barcodes encoded across N rounds yield 2^N - error-corrected transcript identities. Anticipates: error-robust combinatorial in-situ hybridization-cycle architectures distinct from CosMx (which uses encoded probe pools differently); the architectural pattern of an open-top perfusion chamber clamped over a slide for many-cycle in-situ fluorescence.

## Gatorade Gx Sweat Patch (2021-08-25)

- **id**: `gatorade-gx-sweat-patch`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Epicore Biosystems Inc. for PepsiCo Gatorade
- **disclosure**: PepsiCo Gatorade press release 2021-08-25; Epicore Biosystems product disclosure
- **ip status**: patented
- **prior art notes**: Consumer-branded variant of the Epicore epidermal sweat patch. Same microfluidic architecture as the Rogers-lab disclosure (capillary-routed sweat into colorimetric reservoirs) but commercialized for athletic consumer market. Anticipates: consumer wellness business models for one-time-use microfluidic patches; smartphone-as-reader colorimetric quantification of sweat sodium and volume.

## Nix Hydration Biosensor (2021-09-22)

- **id**: `nix-hydration-biosensor`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Nix Biosensors Inc.
- **disclosure**: Nix Inc. product launch 2021; Reinertsen E et al. founder publications; product manual rev 1
- **ip status**: patented
- **prior art notes**: Discloses a single-use sweat patch with a passive microfluidic network distributing sweat to colorimetric reagent pads, with a reusable optical reader puck snapping onto the patch and streaming hydration estimates to phone. The reader sees absorbance changes as sweat fills successive chambers. Anticipates: hybrid disposable-patch-plus-reusable-reader microfluidic architectures; capillary-routed colorimetric hydration tracking.

## NanoString CosMx Spatial Molecular Imager (2022)

- **id**: `nanostring-cosmx`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: NanoString Technologies (Bruker)
- **disclosure**: NanoString CosMx Spatial Molecular Imager. He et al. 2022 Nat. Biotechnol. 40, 1794–1806.
- **ip status**: patented
- **prior art notes**: Iterative-fluidic-cycling single-cell spatial transcriptomics on intact tissue: encoded fluorescent probes hybridized to mRNA in tissue are revealed across multiple imaging cycles. Architecturally similar to Akoya CODEX but for transcripts rather than proteins. Anticipates: in-situ-hybridization-cycle architecture for single-cell-resolution spatial transcriptomics.

## Multiply Labs robotic cell therapy manufacturing (2022)

- **id**: `multiply-labs-robotic-cgt`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Multiply Labs Inc.
- **disclosure**: Multiply Labs press release 2022 (UCSF collaboration on robotic CAR-T manufacturing). https://www.multiplylabs.com. Patent family: US11186815B2 (Multiply Labs; priority 2020) and continuations.
- **ip status**: patented
- **prior art notes**: Discloses an integration architecture in which standard third-party GMP cell-therapy instruments (centrifuges, bioreactors, cartridge platforms) are operated by robotic arms rather than humans, enabling a software-orchestrated 'instrument cluster' as the unit of CGT manufacture. Anticipates: (a) robot-operated multi-instrument CGT manufacturing architectures using stock vendor hardware rather than purpose-built monolithic systems; (b) closed-isolator-housed robotic CGT cells; (c) software-orchestrated parallel multi-patient batch scheduling on shared physical instruments. Architecturally orthogonal to Cellares/Lonza/Miltenyi: those compress process steps into a monolithic cartridge; Multiply Labs preserves modularity by automating the human in the loop.

## Cellipont Bioservices cell therapy CDMO platform (2022)

- **id**: `cellipont-bioservices-cdmo`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Cellipont Bioservices
- **disclosure**: Cellipont Bioservices launch (rebrand of CellReady, 2022). https://www.cellipont.com. Process disclosures: ISBT 128 process documentation packages.
- **ip status**: trade-secret
- **prior art notes**: CDMO operating cell-therapy manufacturing using a curated multi-vendor instrument stack. Process knowledge is largely trade-secret but the organizational architecture (CDMO operating standardized multi-vendor CGT lines for sponsor-agnostic clinical and commercial supply) is itself part of the public CGT-manufacturing prior art and a relevant reference for sponsor-vs-CDMO-vs-in-house make-or-buy decisions.

## Scale Biosciences single-cell split-pool kit (2022)

- **id**: `scale-bio-split-pool-kit`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Scale Biosciences
- **disclosure**: Scale Biosciences product launch 2022. https://scale.bio/. Founders from Cellular Research / BD lineage.
- **ip status**: patented
- **prior art notes**: Plate-based 3-round combinatorial-indexing kit for single-cell RNA, ATAC, and methylation. Each round of indexing distributes fixed nuclei across 96 or 384 wells; total barcode space grows multiplicatively (>10^7). Anticipates: combinatorial indexing as a scaling strategy that bypasses droplet-microfluidic single-cell instruments; multi-omic single-cell prep using the same combinatorial backbone. Distinguishes from Parse Evercode by emphasis on epigenomic assays (ATAC, methylation) in addition to RNA.

## Dragonfly Mass Spectrometer (DraMS) for Titan (2022)

- **id**: `dragonfly-drams-titan-mass-spec`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: NASA Goddard Space Flight Center / Johns Hopkins APL / DraMS team (M. Trainer PI)
- **disclosure**: Trainer MG et al., 'Dragonfly: Investigating the Surface Composition of Titan,' Planetary Science Journal 3:218 (2022), doi:10.3847/PSJ/ac8e9d; Grubisic A et al., 'DraMS: Architecture and capabilities of the Dragonfly Mass Spectrometer,' International Astronautical Congress IAC-22 (2022)
- **ip status**: public-domain
- **prior art notes**: Discloses the MOMA-derivative architecture adapted for Titan operation. Element-by-element prior art: (a) the cryogenic-surface-to-MS sample handling chain (DrACO drill -> sealed cryotransfer -> warmed pyrolysis oven -> ion trap MS) anticipates patents on cryogenic-sample mass-spec sample-introduction cartridges; (b) the pulse-frequency tuning of the 266 nm UV-LDI source for nitrile/tholin chemistry anticipates LDI-MS patents claiming optimized parameters for nitrogen-rich complex organics; (c) the integration of MS with a flying lander (drone) platform, including vibration-tolerance qualification of the linear ion trap, anticipates patents on platform-integrated mass spectrometers for non-rover planetary missions. Co-cite with exomars-moma-pyr-gcms-ldms for the heritage instrument.

## Akoya Biosciences PhenoCycler-Fusion (2022-04-26)

- **id**: `akoya-phenocycler-fusion`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Akoya Biosciences
- **disclosure**: Akoya Biosciences PhenoCycler-Fusion product launch press release 2022-04-26. https://www.akoyabio.com. Combination of CODEX iterative-fluorescence cycling (Goldman 2018) with the Fusion high-speed scanner.
- **ip status**: patented
- **prior art notes**: Integrated automation of CODEX (Goldman 2018) iterative DNA-tag-cycled antibody staining: a perfusion fluidic chamber clamps over a tissue slide, automated reagent cycling adds and cleaves DNA-conjugated antibodies, and the high-speed Fusion scanner images the slide between cycles. Anticipates: integrated tissue-slide perfusion-and-image-cycle architectures; CODEX productization with automated fluidics, distinguishing from earlier manual or microscope-mounted CODEX implementations.

## PacBio Revio SMRT Cell (2022-10-26)

- **id**: `pacbio-revio-smrt-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Pacific Biosciences
- **disclosure**: Pacific Biosciences Revio system launch press release 2022-10-26. https://www.pacb.com/revio/. Eid, J. et al. Real-time DNA sequencing from single polymerase molecules. Science 2009, 323, 133-138. DOI: 10.1126/science.1162986 (SMRT foundational).
- **ip status**: patented
- **prior art notes**: Successor SMRT cell to the Sequel II SMRT cell, scaled to ~25 million zero-mode waveguides per cell (vs. ~8 million prior) on a single silicon die, enabling 4 cells to be processed simultaneously by the Revio instrument. Anticipates: the next-generation scaling of ZMW-array nanofluidic sequencing chips, including denser packing, parallel-cell architectures, and the tighter coupling of optical readout with on-chip nanofluidics.

## Miltenyi CliniMACS Prodigy Adapt module (2023)

- **id**: `miltenyi-prodigy-adapt`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Miltenyi Biotec
- **disclosure**: Miltenyi Biotec CliniMACS Prodigy Adapt product launch. https://www.miltenyibiotec.com/global/en/products/clinimacs-prodigy-adapt.html (announced 2023; references parent CliniMACS Prodigy patent family).
- **ip status**: patented
- **prior art notes**: Extension module to the CliniMACS Prodigy closed-cartridge platform that adds higher-throughput and adaptable process steps for allogeneic cell therapies (gene-edited NK, iPSC-derived, off-the-shelf CAR-T). Architecturally significant as the first commercial closed cartridge to integrate selection, activation, transduction/electroporation, expansion, formulation, and fill-finish for allogeneic products in a single disposable. Anticipates: closed-cartridge architectures supporting multi-modal gene delivery (lentiviral, electroporation, chemical) and continuous selection across multiple cell types within one disposable; modular extensions to GMP cartridge platforms.

## Standard BioTools Hyperion XTi imaging mass cytometer (2023)

- **id**: `standard-biotools-hyperion-xti`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Standard BioTools (formerly Fluidigm)
- **disclosure**: Standard BioTools Hyperion XTi product launch 2023. https://www.standardbio.com/products/instruments/hyperion-xti.
- **ip status**: patented
- **prior art notes**: Successor instrument to Hyperion: tissue stained with metal-isotope-labeled antibodies, then laser-ablated pixel-by-pixel into a stream that feeds a CyTOF mass cytometer. Anticipates: improved-throughput mass-spec spatial proteomics, including the upgraded fluidic transfer line and higher repetition-rate ablation. Combined with Hyperion and CyTOF this is the dominant mass-spec spatial-proteomics architecture; the corpus entry distinguishes the XTi-specific throughput improvements over the original Hyperion.

## Akoya CODEX Athena (PhenoImager Athena) (2024)

- **id**: `akoya-codex-athena`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Akoya Biosciences
- **disclosure**: Akoya Biosciences PhenoImager Athena product announcement, 2024. https://www.akoyabio.com.
- **ip status**: unknown
- **prior art notes**: Translational-research / clinical-grade configuration of the CODEX iterative-fluidic-cycling spatial-protein platform, with workflow tailored for FFPE clinical specimens at higher throughput than PhenoCycler-Fusion. Anticipates: clinical-grade configurations of cycled-fluorescence spatial proteomics that focus on regulatory / diagnostic-development workflows rather than discovery research.
