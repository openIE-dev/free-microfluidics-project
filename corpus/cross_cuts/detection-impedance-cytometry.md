---
title: detection-impedance-cytometry
parent: Cross-cuts
layout: default
---

# Cross-cut: `detection-impedance-cytometry`

**14 corpus entries disclose this subsystem.**

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

## Drew Scientific HemaVet 950 / 1500 Veterinary Hematology Analyzer (1996)

- **id**: `drew-scientific-hemavet-veterinary-cbc`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Drew Scientific (Erba Diagnostics)
- **disclosure**: Drew Scientific HemaVet 850/950 launch ~1996; HemaVet 1500 launch 2003; pivotal multi-species reference distribution publications by Provost, Vet Clin Pathol
- **ip status**: patented
- **prior art notes**: Discloses an impedance-only multi-species veterinary hematology analyzer optimized for low-volume rodent samples (20 µL): single Coulter-principle aperture with species-specific lysing reagents; differential by impedance-histogram peak deconvolution applying species-specific RBC/WBC/PLT volume distribution priors. Anticipates: low-cost impedance-only veterinary hematology suitable for academic/preclinical pharmacology where cost and rodent-sample volume dominate over diff-channel diversity. Distinct from IDEXX ProCyte Dx (impedance + flow cytometry, higher cost, in-clinic) and from Heska Element HT5 (image cytometry). Important architectural anchor for the segment of veterinary/preclinical hematology that doesn't need fluorescence cytometry.

## Abbott Cell-Dyn Sapphire Hematology Optical/Impedance Flow Cell (2003)

- **id**: `abbott-cell-dyn-sapphire-flow-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Abbott Laboratories (Abbott Hematology / Cell-Dyn)
- **disclosure**: Abbott Cell-Dyn Sapphire 510(k) K022428 (cleared 2003-04); peer-reviewed evaluation Bruegel et al., Clin Lab Haematol 2004
- **ip status**: patented
- **prior art notes**: Discloses Multi-Angle Polarized Scatter Separation (MAPSS) optical flow cytometry for white-blood-cell five-part differentiation: hydrodynamically focused single-cell stream illuminated at four angles (intermediate-angle scatter, polarized side scatter, depolarized side scatter, axial light loss) plus 488 nm laser fluorescence channel for retic/NRBC. The fluidic architecture pairs a sheath-focused optical flow cell for WBC/diff/retic with a Coulter-principle sapphire impedance aperture for RBC/PLT in parallel, with shared sample dilution stages. Anticipates: hybrid optical-impedance hematology fluidic stages sharing sample dilution; depolarized side-scatter eosinophil identification via crystalline content; sapphire as orifice material for impedance counting (durability against erosion vs ruby/glass).

## Stago STA R Max Coagulation Analyzer Cuvette Ball Mixer (2007)

- **id**: `stago-sta-r-max-coag-fluidics`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Diagnostica Stago
- **disclosure**: Stago STA R Evolution launch 2007; STA R Max launch 2014; FDA 510(k) K082437; mechanical viscosity detection patent US4319194 (Stago 1982)
- **ip status**: patented
- **prior art notes**: Discloses Stago's signature mechanical clot detection: the assay cuvette contains a small steel ball oscillated by an external rotating magnetic field; as plasma coagulation progresses, viscosity rises, dampening ball oscillation amplitude/phase, sensed by a Hall-effect or coil pickup. Unlike optical (Werfen ACL TOP) or chromogenic (Sysmex CS) detection, the viscosity-based primitive is immune to chyle/hemolysis/icterus optical interference — enabling testing on samples that would fail other analyzers. Anticipates: magneto-mechanical viscosity-based clot detection in disposable cuvettes; the architectural choice of pre-loading the ball into the cuvette during manufacture (vs adding it at runtime). Defines the commercial niche for centers with high pediatric / hemolyzed sample loads.

## Phoenix Mars Lander MECA Wet Chemistry Laboratory (WCL) (2008)

- **id**: `phoenix-meca-wet-chemistry-lab`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: NASA Jet Propulsion Laboratory / Tufts University (Kounaves) / University of Arizona (Hecht PI)
- **disclosure**: Hecht MH et al., 'Detection of Perchlorate and the Soluble Chemistry of Martian Soil at the Phoenix Lander Site,' Science 325(5936):64-67 (2009), doi:10.1126/science.1172466; Kounaves SP et al., 'The MECA Wet Chemistry Laboratory on the 2007 Phoenix Mars Scout Lander,' JGR Planets 114:E00A19 (2009), doi:10.1029/2008JE003084
- **ip status**: public-domain
- **prior art notes**: Discloses a planetary in-situ wet chemistry cartridge architecture: a sealed disposable reaction beaker with integrated multi-ion electrochemical sensor array on the cell wall, dry-stored reagent pellets released by a mechanical dispenser, and a magnetic stir bar for homogenization. Element-by-element prior art for: (a) any cartridge claim that integrates an ISE array on a single beaker wall with a multi-ion readout (Li, Na, K, NH4, Mg, Ca, Cl, NO3, Br, perchlorate-sensitive); (b) the standard-addition titration protocol implemented through sequential dry-pellet dissolution (the BaCl2 -> SO4 turbidity step, the HNO3 acidification step) anticipates patents on dry-reagent diagnostic cartridges that perform sequential reagent additions for water-quality analysis; (c) the integration of cyclic voltammetry on the same beaker as ion-selective potentiometry anticipates multi-modal electrochemical cartridge designs. The Phoenix WCL is one of two flight precedents (with Viking Biology Instrument) for in-situ aqueous chemistry on a planetary surface.

## IDEXX ProCyte Dx Veterinary Hematology Analyzer Optical/Impedance Flow Cell (2010)

- **id**: `idexx-procyte-dx-veterinary-hematology`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: IDEXX Laboratories
- **disclosure**: IDEXX ProCyte Dx launch 2010-09; ProCyte One launch 2020-06
- **ip status**: patented
- **prior art notes**: Discloses an in-clinic veterinary hematology analyzer based on a Sysmex-licensed dual-modality flow cell (impedance + flow cytometry with side scatter and side fluorescence), ported to a compact bench-top form factor with species-specific reagent and algorithm sets. Anticipates: in-clinic veterinary applications of hybrid impedance + optical hematology platforms; the multi-species calibration architecture (RBC volume, MCV, WBC subtype distributions vary substantially across species — the analyzer must select species-specific reference distributions). Important prior art for the veterinary in-clinic hematology market as it differentiates from human-clinical-only platforms (Sysmex XN, Beckman DxH, Mindray BC). Companion to ProCyte One (2020) which uses a different IDEXX-internal optical fluorescent imaging architecture rather than Sysmex licensure.

## Mindray BC-6800 Hematology Analyzer SF Cube Flow Cell (2011)

- **id**: `mindray-bc-6800-hematology-flow-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Shenzhen Mindray Bio-Medical Electronics
- **disclosure**: Mindray BC-6800 launch 2011-11; FDA 510(k) K121734; BC-7500 launch 2018
- **ip status**: patented
- **prior art notes**: Discloses the SF Cube hematology flow-cell architecture: a single sheath-focused stream subjected to both impedance counting (sapphire aperture for RBC/PLT) and downstream optical interrogation by 633 nm laser with side-scatter + dual-wavelength side-fluorescence channels (one for nucleic-acid binding dye discriminating reticulocytes/NRBC, one for cytoplasmic dye discriminating granulocyte subclasses). Three-axis (SSC × SFL1 × SFL2) cytogram enables 5-part diff with built-in IG (immature granulocyte) detection. Anticipates: dual-wavelength fluorescence + scatter cytometry on a single hematology flow cell (independent prior art relative to Sysmex XN/Beckman DxH but architecturally similar) — strengthening the commons against narrow-claim assertions on this design space.

## Sysmex XN-9000 Modular Hematology Track Sample-Aspiration Subsystem (2011)

- **id**: `sysmex-xn-9000-track-hematology`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Sysmex Corporation
- **disclosure**: Sysmex XN-Series launch 2011-09; XN-9000 modular configuration 2013; FDA 510(k) K112763 (XN); extends sysmex-cbc-cartridge entry already in corpus
- **ip status**: patented
- **prior art notes**: Discloses the Sysmex XN-9000 modular hematology track architecture extending the existing sysmex-cbc-cartridge entry (in corpus) with: (1) primary-tube cap-piercing sample aspiration sharing one probe across multiple downstream analyzer modules; (2) the WDF channel using a polymethine fluorescent dye that selectively stains WBC nucleic acid + cytoplasmic granularity, enabling true 5-part diff via two-color cytogram (side scatter × side fluorescence) — replacing the earlier-generation impedance-only differential; (3) the WPC channel using a different polymethine dye selective for blast cells, enabling automated reflexing for hematological malignancy screening; (4) the modular XN-9000 configuration linking up to 6 analyzer modules on a sample-routing track. Anticipates: high-throughput modular hematology with primary-tube cap-piercing + multi-channel optical/impedance + fluorescent intracellular staining for cell classification.

## ISS Biomolecule Sequencer (Oxford Nanopore MinION on ISS) (2016)

- **id**: `iss-biomolecule-sequencer-minion`
- **corpus**: open
- **device class**: nanofluidic-chip
- **creator**: NASA Johnson Space Center / Oxford Nanopore Technologies / Houston Methodist
- **disclosure**: Castro-Wallace SL et al., 'Nanopore DNA Sequencing and Genome Assembly on the International Space Station,' Scientific Reports 7:18022 (2017), doi:10.1038/s41598-017-18364-0; NASA ISS Biomolecule Sequencer mission press kit, August 2016
- **ip status**: patented
- **prior art notes**: While the underlying MinION is already covered as 'oxford-nanopore-minion' in the corpus, the spaceflight variant is independent prior art for: (a) the qualification of biological-membrane nanopore arrays for the orbital radiation environment without measurable loss of yield (vs. ground controls), which anticipates patents claiming radiation-hardened or space-qualified single-molecule sequencing cartridges; (b) the ground-to-orbit cold-chain protocol for shipping pre-loaded R9 flow cells (cold pack stability, ambient ISS temperature operation), which anticipates patents on planetary or deep-sea biosensor logistics; (c) the integration of MinION sequencing with WetLab-2 sample prep on station — together these establish the first sample-to-sequence loop performed beyond Earth, and anticipate any patent claim to an integrated 'in-situ sequencing cartridge' for planetary life detection that uses pore-based single-molecule readout. Cross-cite to oxford-nanopore-minion for the underlying device.

## Beckman Coulter DxH 900 Hematology VCSn Flow Cell (2017)

- **id**: `beckman-coulter-dxh-900-flow-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Beckman Coulter (Danaher)
- **disclosure**: Beckman Coulter DxH 900 launch 2017-08; FDA 510(k) K162970
- **ip status**: patented
- **prior art notes**: Discloses VCSn technology: simultaneous Volume (low-frequency Coulter impedance for DC volume), Conductivity (high-frequency RF impedance probing internal cell density), and 5-angle Light Scatter (axial light loss + multiple side-scatter angles for granularity, lobularity, complexity) in a single hydrodynamically-focused fluidic stage. The fluid path co-locates the impedance aperture and the optical interrogation zone so each cell event is measured by all modalities within microseconds. Anticipates: combined impedance + multi-angle scatter cytometry on a single flow cell for hematology classifier inputs; 'NEW' designation marks redesigned aperture geometry vs the LH series predecessor. Element-by-element: dilution chamber, sheath formation, aperture-with-electrodes, laser interrogation downstream, post-aperture flush.

## Heska Element HT5 Veterinary Hematology Image Cytometry Analyzer (2018)

- **id**: `heska-element-ht5-veterinary-imaging`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Heska Corporation (now Mars Petcare)
- **disclosure**: Heska Element HT5 launch 2018-09; product datasheet; companion Heska 510(k) K200147
- **ip status**: patented
- **prior art notes**: Discloses an in-clinic veterinary hematology analyzer using image cytometry (vs flow cytometry) for the WBC differential: stained WBCs flow through a microfluidic imaging channel under high-magnification CCD imaging, and convolutional-neural-network (CNN)-based image classification produces 5-part diff plus reticulocyte count (since 2019 software updates). Distinguishes from IDEXX ProCyte Dx (Sysmex-licensed flow cytometry), Sysmex XN, Beckman DxH, and Mindray BC-6800 (all flow cytometry-based) by retaining actual cell images for veterinarian review — important in veterinary clinical pathology where edge cases (mast cell tumor mast cells in peripheral blood, exotic species hematology) benefit from image evidence. Anticipates: image-cytometry hematology as an alternative to flow cytometry; CNN-based image classification embedded in a clinical analyzer; the architectural choice of single-cuvette image + impedance hybrid (vs separate multi-channel architecture).

## Ori Biotech IRO cell therapy manufacturing platform (2019)

- **id**: `ori-biotech-iro`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Ori Biotech Ltd
- **disclosure**: Ori Biotech IRO platform. Press launch 2019; commercial availability 2023. https://www.oribiotech.com. Patent family: WO2018229497A1 / US11629322B2 (Ori Biotech Ltd; priority 2017).
- **ip status**: patented
- **prior art notes**: Discloses a closed-cartridge end-to-end CGT manufacturing system architecturally distinguished from Cellares Cell Shuttle and Lonza Cocoon by its emphasis on (a) decentralized hospital-deployable manufacturing rather than centralized factories; (b) in-line cell counting and viability sensing integrated within the cartridge fluidic path; (c) modular multi-cartridge-per-instrument architecture. Anticipates: distributed-manufacturing CGT cartridge instruments; in-cartridge sensor integration for real-time release-criterion monitoring; multi-tenant-batch CGT instruments supporting concurrent patient-specific runs.

## Oxford Nanopore R10.4.1 flow cell (2022-05-19)

- **id**: `ont-r10-4-1-flow-cell`
- **corpus**: private
- **device class**: nanofluidic-chip
- **creator**: Oxford Nanopore Technologies
- **disclosure**: Oxford Nanopore Technologies R10.4.1 / Kit 14 release announcement at London Calling 2022, 2022-05-19. https://nanoporetech.com/.
- **ip status**: patented
- **prior art notes**: Successor flow cell generation to R9.4.1, with the R10.4.1 pore (a dual-reader CsgG-derived protein pore) integrated into the same MinION/GridION/PromethION housing. The fluidic and electronic architecture - lipid bilayer over a MEMS sensor array, ASIC-based real-time current readout - is unchanged; the innovation is the pore itself plus ATP-driven motor changes. Anticipates: per-pore accuracy improvements via dual-reader pores; the architectural pattern of in-place pore upgrades within the same flow cell housing across multiple kit generations.
