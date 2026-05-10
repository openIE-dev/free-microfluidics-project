---
title: architecture-stat-test-cartridge
parent: Cross-cuts
layout: default
---

# Cross-cut: `architecture-stat-test-cartridge`

**28 corpus entries disclose this subsystem.**

Earliest disclosure: 1966

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Star Trek medical tricorder (1966)

- **id**: `star-trek-tricorder-medical`
- **corpus**: fictional
- **device class**: fictional-laboratory
- **creator**: Gene Roddenberry; Desilu / NBC
- **disclosure**: Star Trek (original series), 1966–1969, NBC. Medical tricorder appears across the series as Dr. McCoy's diagnostic instrument.
- **ip status**: fictional
- **prior art notes**: Long-running narrative depiction of a handheld diagnostic instrument performing rapid multiplexed measurements on a single patient sample. Cited (notably during the X-Prize Tricorder competition framing) as the conceptual ancestor of handheld point-of-care diagnostic devices. As 102 prior art for 'handheld portable multiplex medical diagnostic instrument as a category', Star Trek's depiction predates every commercial implementation by decades.

## i-STAT cartridge family (CHEM8+, CG8+, etc.) (1992)

- **id**: `i-stat-cartridge-cg8plus`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: i-STAT Corporation (Abbott Point of Care)
- **disclosure**: i-STAT Corporation (acquired by Abbott 2003). i-STAT 1 system and cartridge family. FDA approval mid-1990s.
- **ip status**: patented
- **prior art notes**: Foundational disclosure of integrated-blood-gas-and-chemistry POC cartridge: a single-use cartridge with sample-handling chamber, calibrant pouch, electrochemical sensor array, and reagent reservoirs in injection-molded thermoplastic. The i-STAT cartridge is among the longest-running and highest-volume POC cartridges in clinical use (1990s onward). Anticipates: integrated-biochemistry-cartridge architecture combining electrolyte, blood gas, and metabolite measurements in a single bedside device.

## Werfen GEM Premier 5000 blood gas cartridge (2002)

- **id**: `instrumentation-laboratory-gem-premier`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Instrumentation Laboratory (Werfen)
- **disclosure**: Werfen Instrumentation Laboratory GEM Premier system. https://www.werfen.com
- **ip status**: patented
- **prior art notes**: Cartridge-based blood gas analyzer with extended on-cartridge calibration and quality control. The GEM Premier cartridge contains all reagents, calibrants, and waste reservoirs sufficient for several hundred patient samples before replacement. Architectural cousin of i-STAT and Siemens epoc but at higher per-cartridge throughput. Reference for the multi-sample-cartridge POC blood gas segment.

## Theranos Edison / miniLab cartridge (claimed) (2003)

- **id**: `theranos-promised-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Theranos Inc.
- **disclosure**: Theranos Inc. patent filings beginning 2003 (US7635594B2 and family); SEC v. Theranos litigation record.
- **ip status**: patented
- **prior art notes**: Patent filings disclosed an asserted single-cartridge multi-test blood diagnostic platform from finger-stick volumes. The filings stand as 102/103 art regardless of whether the company successfully reduced to practice; many subsequent POC-blood patents must contend with these filings as anticipating prior art for 'finger-stick-volume multi-assay cartridge as architecture.' Inclusion in this corpus is not an endorsement of the product's claimed performance.

## Cepheid GeneXpert cartridge (2004)

- **id**: `cepheid-genexpert-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Cepheid (Danaher subsidiary)
- **disclosure**: Cepheid GeneXpert system; FDA 510(k) K043510 (2004) and subsequent assay clearances.
- **ip status**: patented
- **prior art notes**: Discloses a disposable cartridge with a rotary valve sequencing reagents through a sample preparation pathway into an optical reaction tube for real-time PCR. Anticipates: rotary-valve / multi-port selector architecture for multi-reagent cartridges, optically interrogated reaction chamber within a closed disposable, and the GeneXpert-style sample-prep + amplification + detection integration that underlies most Cepheid POC products including the Xpert MTB/RIF tuberculosis test.

## Field-deployable agricultural pathogen detection cartridges (Cady 2003 lineage) (2005)

- **id**: `cady-2003-agricultural-pathogen-cartridge`
- **corpus**: academic
- **device class**: point-of-care-cartridge
- **creator**: Various — Cady (Cornell) / Lampe lineage
- **disclosure**: Cady, N. C. et al. Real-time PCR detection of Listeria monocytogenes using an integrated microfluidic platform. Sens. Actuators B Chem. 2005, 107, 332–341. DOI: 10.1016/j.snb.2004.10.022
- **ip status**: patented
- **prior art notes**: Foundational disclosure of agricultural / food-pathogen detection on integrated microfluidic platform: Listeria monocytogenes detection from food matrix by integrated lyse-extract-amplify-detect cartridge. Anticipates: agricultural-context integrated-PCR-cartridge architecture, distinct from clinical cartridges by emphasizing food-matrix sample-prep upstream. Underlies subsequent commercial efforts by Neogen, 3M Petrifilm, and academic agricultural-pathogen-cartridge programs.

## Siemens epoc Blood Analysis System cartridge (2006)

- **id**: `epoc-blood-gas-analyzer`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Epocal (acquired by Siemens / now part of Siemens Healthineers)
- **disclosure**: Siemens Healthineers epoc system. https://www.siemens-healthineers.com
- **ip status**: patented
- **prior art notes**: POC blood gas / chemistry / hematology cartridge with disposable test card and Bluetooth-connected reader. Architectural cousin of i-STAT in the same product category. Smaller cartridge form factor and Bluetooth-rather-than-direct-instrument architecture are differentiators.

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

## Heska veterinary POC cartridge platform (2010)

- **id**: `heska-veterinary-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Heska Corporation (acquired by Antech / Mars Petcare 2023)
- **disclosure**: Heska Corporation Element series. https://www.heska.com
- **ip status**: patented
- **prior art notes**: Veterinary POC cartridge platform spanning blood chemistry, hematology, and infectious disease testing. Architecturally similar to human-medicine i-STAT and Piccolo Xpress but tuned for veterinary species and workflows. Reference for the broader veterinary POC cartridge market, which under-indexes in human-medicine prior-art reviews.

## Abbott ID NOW isothermal amplification cartridge (2014)

- **id**: `abbott-id-now-isothermal-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Alere Inc.; now Abbott Diagnostics
- **disclosure**: Alere i / Abbott ID NOW. FDA 510(k) and EUA clearances. https://www.globalpointofcare.abbott/en/product-details/id-now.html
- **ip status**: patented
- **prior art notes**: Discloses a small-format isothermal nucleic acid amplification cartridge for ~15-minute molecular diagnostics, eliminating thermal cycling hardware. Anticipates: nicking-enzyme-amplification-reaction (NEAR) chemistry on a disposable cartridge, isothermal POC molecular testing for influenza/strep/SARS-CoV-2, and the architectural pattern of substituting fast isothermal chemistry for cartridge-level thermal cycling complexity.

## GenMark ePlex cartridge (2014)

- **id**: `genmark-eplex-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: GenMark Diagnostics (acquired by Roche 2021)
- **disclosure**: GenMark Diagnostics (now Roche) ePlex system. FDA 510(k) K161312 and family. https://www.genmarkdx.com/eplex/
- **ip status**: patented
- **prior art notes**: Disclosed a multiplex molecular diagnostic cartridge integrating sample prep, PCR amplification, and electrochemical detection on a printed gold electrode array (eSensor technology). Anticipates: electrochemical-array detection as alternative to optical fluorescence in syndromic POC molecular diagnostics, and the architectural pattern of integrating eSensor-style detection within a self-contained cartridge.

## Cue Health Monitoring System cartridge (2014)

- **id**: `cue-health-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Cue Health Inc. (formerly Mesa Biotech)
- **disclosure**: Cue Health Inc. Cue COVID-19 Test for Home and Over The Counter Use. FDA EUA June 2021. https://cuehealth.com
- **ip status**: patented
- **prior art notes**: Cartridge-based isothermal NAAT (nucleic acid amplification test) platform with integrated electrochemical detection and Bluetooth readout to smartphone app. Lucira/Detect competitor, with the differentiating architecture being electrochemical (vs Lucira's colorimetric) detection. Anticipates: smartphone-mediated cartridge readout as a category, integrated isothermal-NAAT-with-electrochemistry on disposable cartridge.

## T2 Biosystems T2Dx cartridge (2014)

- **id**: `t2-biosystems-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: T2 Biosystems
- **disclosure**: T2 Biosystems T2Dx Instrument and T2Candida / T2Bacteria Panels. FDA approval September 2014.
- **ip status**: patented
- **prior art notes**: Cartridge platform using T2MR (magnetic resonance) detection for sepsis-causing pathogen identification directly from whole blood without culture. Anticipates: NMR-based detection on cartridge as alternative to fluorescence/electrochemistry, and the bacteremia-from-whole-blood-without-culture clinical positioning.

## Miltenyi CliniMACS Prodigy cell therapy platform (2014)

- **id**: `miltenyi-clinimacs-prodigy`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Miltenyi Biotec
- **disclosure**: Miltenyi Biotec CliniMACS Prodigy. https://www.miltenyibiotec.com
- **ip status**: patented
- **prior art notes**: The first widely-deployed closed-cartridge cell therapy manufacturing platform, predating Lonza Cocoon and Cellares Cell Shuttle. Used for academic CAR-T manufacturing at most major academic medical centers worldwide. Architectural ancestor of the CAR-T-manufacturing-on-cartridge product category.

## Cepheid Xpress (rapid GeneXpert) cartridge (2017)

- **id**: `cepheid-xpress-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Cepheid (Danaher)
- **disclosure**: Cepheid Xpert Xpress family — rapid versions of the GeneXpert cartridge with reduced runtime via streamlined sample prep.
- **ip status**: patented
- **prior art notes**: Newer family of Cepheid GeneXpert cartridges optimized for sub-30-minute runtime: Xpert Xpress Flu/RSV, Xpert Xpress SARS-CoV-2, Xpert Xpress Strep A. Architecturally identical to original GeneXpert cartridge with optimized chemistry (faster amplification cycles, multiplexed assays).

## Lonza Cocoon CAR-T cell therapy platform (2017)

- **id**: `lonza-cocoon-cell-therapy`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Lonza Group
- **disclosure**: Lonza Cocoon Platform. https://www.lonza.com
- **ip status**: patented
- **prior art notes**: Closed-cartridge cell therapy manufacturing platform — same product category as Cellares Cell Shuttle and Miltenyi CliniMACS Prodigy. The cell therapy manufacturing cartridge segment is one of the fastest-growing commercial microfluidic markets (2020-onward).

## Visby Medical PCR cartridge (2018)

- **id**: `visby-medical-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Visby Medical (formerly Click Diagnostics)
- **disclosure**: Visby Medical respiratory and STI tests. FDA 510(k) family. https://www.visbymedical.com
- **ip status**: patented
- **prior art notes**: Single-use, palm-sized PCR cartridge with integrated optical detection and battery power; the test result is read by visual inspection of color-coded LEDs without requiring an instrument. Architecturally distinguished from Lucira (isothermal LAMP) by using true PCR thermal cycling on disposable. Anticipates: instrument-free thermal-cycled PCR cartridge with embedded heater and battery, and the device-disposable-as-instrument architectural collapse.

## Lucira Health Check It home COVID-19 isothermal molecular test (2020)

- **id**: `lucira-home-covid-test`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Lucira Health (acquired by Pfizer 2023)
- **disclosure**: Lucira Health Check It / All-In-One COVID-19 Test Kit. FDA EUA December 2020 (first FDA-authorized at-home molecular COVID-19 test). https://www.fda.gov/media/143810/download
- **ip status**: patented
- **prior art notes**: The first FDA-authorized at-home molecular COVID-19 test, demonstrating that LAMP isothermal amplification + colorimetric readout could be packaged into a fully self-contained $50-class disposable. Anticipates: complete self-contained battery-powered isothermal molecular diagnostic at consumer price points, integrated colorimetric readout without optical instrumentation, and the architectural collapse of the molecular diagnostics stack from $30k cartridge readers to single-use disposables.

## Qiagen QIAreach POC molecular cartridge (2020)

- **id**: `qiagen-qiareach-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Qiagen N.V.
- **disclosure**: Qiagen QIAreach Anti-SARS-CoV-2 Total. https://www.qiagen.com
- **ip status**: patented
- **prior art notes**: Qiagen's POC molecular and serology cartridge platform: cassette-format consumable with eHub portable reader. The QIAreach platform is positioned for low- and middle-income-country deployment, with significant deployment during COVID-19 in resource-limited settings. Reference for the broader Qiagen patent estate in POC cartridge architecture.

## Institut Pasteur CRISPR cartridge work (academic) (2020)

- **id**: `pasteur-crispr-cartridge-academic`
- **corpus**: academic
- **device class**: point-of-care-cartridge
- **creator**: Various Pasteur lineage groups
- **disclosure**: Various Institut Pasteur publications 2020-2024 on CRISPR-cartridge POC diagnostic development.
- **ip status**: patented
- **prior art notes**: Composite reference for European CRISPR-cartridge academic work centered at Institut Pasteur, complementing US (Sherlock, Mammoth, Broad) and academic-to-commercial pipelines. The Pasteur lineage is particularly strong in tropical disease applications (Plasmodium, dengue, chikungunya) where CRISPR cartridge architectures have specific advantages.

## Aspendia cardiac POC cartridge (sub-femtomolar troponin) (2021)

- **id**: `aspendia-cardiac-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Quanterix Aspendia / various
- **disclosure**: Quanterix-acquired Aspendia / various 2020s ultrasensitive troponin POC cartridges.
- **ip status**: patented
- **prior art notes**: Composite reference for emerging POC cardiac biomarker cartridges achieving sub-femtomolar (single-molecule-counting class) sensitivity for high-sensitivity troponin and similar markers. Architectural successor to ELISA-format cartridges by leveraging Simoa-style single-molecule detection in disposable cartridge form factor. Active subfield 2020-onward.

## Cellares Cell Shuttle CAR-T manufacturing platform (2022)

- **id**: `cellares-cell-shuttle`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Cellares Corporation
- **disclosure**: Cellares Corporation Cell Shuttle. https://www.cellares.com
- **ip status**: patented
- **prior art notes**: Industrial-scale CAR-T cell therapy manufacturing platform with cartridge-based closed-system processing of patient cells: activation, transduction, expansion, and harvest in a single disposable cartridge. Anticipates: GMP-scale microfluidic-equivalent cell therapy manufacturing as a category. Architectural cousin of Lonza Cocoon and Miltenyi CliniMACS Prodigy.

## Mammoth Biosciences DETECTR BOOST cartridge (2022)

- **id**: `mammoth-detectr-boost-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Mammoth Biosciences
- **disclosure**: Mammoth Biosciences DETECTR BOOST. https://mammoth.bio
- **ip status**: patented
- **prior art notes**: Commercial DETECTR-platform CRISPR cartridge: integrated sample-prep, RPA amplification, Cas12a-based detection in single-use cartridge format. Anticipates: high-throughput automated CRISPR diagnostic cartridges as a commercial product category. Companion to academic disclosures (Chen 2018 DETECTR foundational, Myhrvold 2018 SHINE) by establishing instrument-format CRISPR-cartridge architecture.

## Sherlock Biosciences INSPECTR cartridge (2023)

- **id**: `sherlock-biosciences-inspectr`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Sherlock Biosciences
- **disclosure**: Sherlock Biosciences INSPECTR product family. https://sherlock.bio
- **ip status**: patented
- **prior art notes**: Commercial SHERLOCK-platform CRISPR cartridge: SHERLOCK Cas13-based detection in single-use cartridge with smartphone or instrument readout. Direct architectural cousin of Mammoth DETECTR BOOST but with Cas13 enzyme and different sample-prep chemistry. Reference for the broader CRISPR-cartridge product category alongside the academic foundational disclosures.

## SHUGA POC molecular diagnostic cartridge (2024 demonstration) (2024)

- **id**: `kaminski-shuga-cartridge-2024`
- **corpus**: academic
- **device class**: point-of-care-cartridge
- **creator**: Various — Sabeti / Zhang Broad lineage
- **disclosure**: Various 2024 publications on next-generation CRISPR-cartridge POC diagnostics. Representative: Kaminski/Sabeti lab Broad Institute SHERLOCK-cartridge work.
- **ip status**: patented
- **prior art notes**: Composite reference for the 2024-onward wave of CRISPR-cartridge POC diagnostic disclosures: integrated sample-prep + RPA/LAMP amplification + Cas12/Cas13 detection in single-use cartridges with smartphone or instrument readout. Architectural extension of the Lucira/Visby/Cue isothermal-NAAT cartridge family with CRISPR-based detection chemistry replacing fluorescent or colorimetric direct-readout. Multiple academic and commercial efforts active in this space.

## Environmental microbiome sample-to-sequencing cartridges (2024 academic) (2024)

- **id**: `environmental-microbiome-cartridge-2024`
- **corpus**: academic
- **device class**: point-of-care-cartridge
- **creator**: Various groups
- **disclosure**: Various 2024-2026 publications on environmental microbiome sample-to-sequencing integrated cartridges.
- **ip status**: patented
- **prior art notes**: Composite reference for emerging sample-to-sequencing microbiome cartridges: lyse-extract-amplify-sequence in integrated disposable cartridges for soil, water, and air microbiome surveillance. The combination of long-read sequencing (Oxford Nanopore MinION) with cartridge-format sample prep enables true field-deployable microbiome analysis.
