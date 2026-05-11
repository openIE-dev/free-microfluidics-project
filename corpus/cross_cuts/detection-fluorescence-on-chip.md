---
title: detection-fluorescence-on-chip
parent: Cross-cuts
layout: default
---

# Cross-cut: `detection-fluorescence-on-chip`

**126 corpus entries disclose this subsystem.**

Earliest disclosure: 1916

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Smoluchowski 1916 — Diffusion-Controlled Coagulation Theory (1916)

- **id**: `smoluchowski-1916-diffusion-coagulation`
- **corpus**: academic
- **device class**: other
- **creator**: Marian Smoluchowski
- **disclosure**: Smoluchowski, M. v. (1916). 'Drei Vortraege ueber Diffusion, Brownsche Bewegung und Koagulation von Kolloidteilchen.' Physikalische Zeitschrift 17: 557-571 and 585-599.
- **ip status**: public-domain
- **prior art notes**: Smoluchowski's diffusion-controlled rate constant is the upper bound on every on-chip biochemical reaction rate. Anticipates: (a) immunoassay binding-time predictions in microfluidic devices (the Sqalli-Houssini bound on antibody capture); (b) DNA-target hybridization rates on microfluidic biosensors; (c) particle-aggregation assay timing claims; (d) molecular-beacon and aptamer-binding cartridge claims that rest on diffusion-limited kinetics. Any patent claim to 'rapid diagnosis by surface-capture in a microchannel' is bounded above by Smoluchowski 1916 and cannot claim novelty over the diffusion-limited rate.

## Sysmex hematology analyzer flow cell (1968)

- **id**: `sysmex-cbc-cartridge`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Sysmex Corporation (Kobe, Japan)
- **disclosure**: Sysmex Corporation hematology analyzer family (XN-1000, XN-2000, etc.). https://www.sysmex.com
- **ip status**: patented
- **prior art notes**: Microfluidic flow-cell architecture for clinical hematology counting (CBC differential): Coulter-impedance counting + flow cytometry + reagent mixing on integrated cartridge. Sysmex is the dominant global hematology analyzer vendor with a long history of flow-cell innovation predating the µTAS era. The flow-cell architectures used in modern Sysmex XN-series instruments are direct descendants of 1970s-era Coulter Counter and Technicon SMA designs but at substantially smaller scale.

## bioMérieux VIDAS 3 Solid Phase Receptacle (SPR) Immunoassay Cone (1990)

- **id**: `biomerieux-vidas-3-spr-cone`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: bioMérieux
- **disclosure**: bioMérieux VIDAS launch 1990 (pioneering ELFA technology); VIDAS 3 launch 2014; FDA 510(k) K133769
- **ip status**: patented
- **prior art notes**: Discloses the bioMérieux SPR (Solid Phase Receptacle) format: a polypropylene cone shaped like a pipette tip whose inner surface is pre-coated with capture antibody; the analyzer's micropipettor docks onto the cone and uses it as both pipette and solid phase, drawing sample and reagents in/out from a sealed reagent strip with 6-10 pre-loaded wells (sample well, wash wells, conjugate well, substrate well). Anticipates: integrated pipette-as-solid-phase fluidic primitive eliminating separate microtiter plate coating; sealed reagent strips with foil seal pierced by the SPR mating action; ELFA (Enzyme-Linked Fluorescent Assay) using MUP→4-methylumbelliferone for sub-pg/mL sensitivity in a single-strip format. Foundational architectural disclosure dating to 1990 — relevant prior art for many subsequent disposable-cartridge-with-pipette-cone architectures (e.g., Biotech / VIDAS-derivative platforms).

## Affymetrix (now Thermo Fisher) GeneChip Patent Estate (1991)

- **id**: `affymetrix-genechip-patent-estate`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Affymetrix Inc. (acquired by Thermo Fisher Scientific 2016)
- **disclosure**: US5445934 (Fodor et al., priority 1989); US5510270; US5800992; US6022963 (Affymetrix; acquired by Thermo Fisher 2016-03-31 for $1.3B)
- **ip status**: patented
- **prior art notes**: Affymetrix GeneChip patent estate. Anchors claims around: (a) photolithographic in situ synthesis of oligonucleotide arrays on a glass substrate using photolabile protecting groups (Fodor 1991 Science paper, US5445934 priority 1989); (b) high-density spatially-addressable microarrays for hybridization-based nucleic-acid analysis; (c) GeneChip-format mask-based or maskless light-directed synthesis. Affymetrix acquired by Thermo Fisher 2016-03-31 for approximately $1.3B. Foundational core patents largely expired by 2009-2014 (17/20-year terms from 1989-1994 priorities). Defensive value: anchors public-domain status of basic photolithographic-array fabrication. Anticipates almost all DNA microarray fabrication approaches that use light-directed synthesis. Companion: this estate is also relevant prior art for spatial-transcriptomics capture arrays (10x Visium).

## Quidel Triage MeterPro Immunoassay Cartridge (1995)

- **id**: `quidel-triage-meterpro-fluorescence-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Quidel (formerly Biosite, then Alere)
- **disclosure**: Biosite Triage launch 1995 (drug-of-abuse panel); Triage BNP first cardiac assay 2000-11 (FDA 510(k) K003425); Quidel acquisition of Alere/Biosite Triage 2017; ongoing assays through 2020s
- **ip status**: patented
- **prior art notes**: Discloses the Biosite Triage cartridge as the original quantitative fluorescent lateral flow immunoassay POC architecture: a hybrid cartridge integrating an injection-molded fluidic frame (sample addition, capillary metering, conjugate rehydration zone) with a nitrocellulose lateral-flow membrane carrying capture-antibody-coated test lines, all read by a benchtop fluorescence meter performing time-resolved fluorescence (TRF) on Eu-chelate labels (or fluorescent latex). Anticipates: quantitative-vs-qualitative lateral flow POC architecture using fluorescent labels and meter-based readout; the BNP/NT-proBNP heart-failure POC market built on this primitive (2000s); the cartridge-frame-plus-membrane fabrication pattern that influenced Sofia, BD Veritor (in corpus), Alere/Abbott IM, and Quidel's modern POC line. Foundational architectural disclosure dating to 1995.

## Mettler-Toledo InPro 6800 / 6850 Dissolved Oxygen Sensor (1995)

- **id**: `mettler-toledo-inpro-6800-do`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Mettler-Toledo Process Analytics
- **disclosure**: Mettler-Toledo InPro 6800 polarographic DO sensor product introduction mid-1990s; InPro 6850 optical successor introduced ~2010; Mettler-Toledo Process Analytics product literature; US patent US7,022,505B1 (Mettler-Toledo, optical oxygen sensor)
- **ip status**: patented
- **prior art notes**: Discloses two architectures: the InPro 6800 implements a Clark-cell polarographic DO measurement (Pt cathode, Ag/AgCl anode, electrolyte-filled chamber, PTFE gas-permeable membrane); the InPro 6850 implements a luminescence-lifetime optical DO measurement (luminophore in polymer matrix, LED excitation, photodiode detection of fluorescence-decay phase shift). Anticipates: paired polarographic and optical DO architectures with shared probe-body form factor and digital ISM interface, allowing process-development to validate either sensor type in interchangeable ports. Element-by-element: probe body + sensing element (membrane + electrolyte / optical spot) + signal-processing electronics + digital interface.

## LightCycler real-time rapid PCR (Wittwer 1997) (1997)

- **id**: `wittwer-1997-rapid-cycler`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Wittwer group, University of Utah / Idaho Technology / Roche
- **disclosure**: Wittwer, C. T.; Herrmann, M. G.; Moss, A. A.; Rasmussen, R. P. Continuous fluorescence monitoring of rapid cycle DNA amplification. BioTechniques 1997, 22, 130–138. DOI: 10.2144/97221bi01
- **ip status**: patented
- **prior art notes**: Disclosed rapid-cycle real-time PCR with continuous fluorescence monitoring during thermal cycling, in glass capillary tubes for fast heat transfer. Architectural ancestor of every real-time PCR cartridge: the framing that PCR + real-time fluorescence reading enables quantitative analysis from a single closed reaction. The Wittwer-Idaho-Technology lineage produced the LightCycler (acquired by Roche 1997) and via the BioFire spinout (2003) the FilmArray cartridge. One of the most consequential academic-to-commercial transitions in molecular diagnostics.

## Illumina Patent Estate Post-Solexa Acquisition (Bridge Amplification + SBS) (1997)

- **id**: `illumina-patent-estate-post-solexa`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Illumina Inc. (acquired Solexa 2007-01-26)
- **disclosure**: US7771970 (priority via Solexa 1997); US8158346; US8071739; US7115400; US6306597 (Illumina via Solexa acquisition 2007 for $600M)
- **ip status**: patented
- **prior art notes**: Illumina patent estate post-Solexa. Anchors claims around: (a) lawn of oligonucleotide capture probes covalently attached to flow-cell glass surface; (b) bridge amplification creating clonal clusters via templated extension between adjacent surface-bound primers; (c) reversible-terminator nucleotides with cleavable fluorescent labels enabling cycle-by-cycle sequencing; (d) flow-cell hardware with patterned-wells (HiSeq X, NovaSeq) for ordered-cluster geometry. Existing companion: bentley-2008-illumina-flow-cell. Anticipates clonal-cluster generation chemistry on flow-cell. Several core members are at or near expiry; this entry timestamps the public-domain transition. Illumina's enforcement actions against BGI/MGI, Element Biosciences, and Singular Genomics (separate litigation entries) all assert subsets of this estate.

## Microfluidic flow cytometer architectures (academic) (2002)

- **id**: `berkeley-cellium-flow-cytometer-2009`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: Quake group, Caltech
- **disclosure**: Fu, A. Y.; Spence, C.; Scherer, A.; Arnold, F. H.; Quake, S. R. A microfabricated fluorescence-activated cell sorter. Nat. Biotechnol. 1999, 17, 1109–1111. DOI: 10.1038/15095
- **ip status**: patented
- **prior art notes**: The first microfabricated FACS — fluorescence-activated cell sorter on chip. Demonstrated cell sorting at modest throughput (~10 cells/s) with optical interrogation and pneumatic actuation in PDMS. Anticipates: chip-FACS architecture, microfluidic flow cytometry, and the entire chip-based flow cytometry subfield subsequently expanded by Sony SP6800, BD Cytopeia, On-chip Sort, and others.

## Fluidigm Integrated Fluidic Circuit Controller Patent Family (2002)

- **id**: `fluidigm-patent-family-ifc-controller`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Fluidigm Corporation (now Standard BioTools)
- **disclosure**: US7307802; US7195670; US7691333; US7906072; US8163492 (Fluidigm Corporation, now Standard BioTools)
- **ip status**: patented
- **prior art notes**: Fluidigm patent family covering the IFC controller (the workhorse benchtop instrument for all Fluidigm chip products). Anchors claims around: (a) pneumatic manifold delivering individually-addressable pressurized control lines to a multilayer PDMS chip seated on a holder; (b) integrated thermal cycling stage; (c) optical readout integration with chip alignment; (d) sequential-loading protocols leveraging MLSI multiplexer trees. Built on the Caltech-licensed Quake MLSI valve patent family (quake-patent-family-mlsi-monolithic-membrane-valve). Anticipates pneumatically-actuated chip-controller benchtop instruments for elastomeric microfluidic chips. Expiry: 2022-2030 across family.

## Pacific Biosciences SMRT Cell Patent Family (2002)

- **id**: `pacbio-smrt-cell-patent-family`
- **corpus**: private
- **device class**: nanofluidic-chip
- **creator**: Pacific Biosciences of California Inc.
- **disclosure**: US7170050; US7476503; US7906284; US10208329; US7820983 (Pacific Biosciences)
- **ip status**: patented
- **prior art notes**: Pacific Biosciences SMRT Cell patent family. Anchors claims around: (a) array of sub-wavelength (~70 nm) zero-mode waveguides on a fused-silica substrate clad with aluminum; (b) single-molecule polymerase tethered at the bottom of each ZMW; (c) phospholinked nucleotides emitting wavelength-distinct fluorescence on incorporation; (d) total-internal-reflection-style illumination with confocal-zone selectivity per ZMW; (e) Revio (existing entry pacbio-revio-smrt-cell) and Sequel II form factors. Companion existing entry: eid-2009-pacbio-smrt. Anticipates ZMW-based single-molecule sequencing chips and any nanofluidic chip with a sub-wavelength aperture array for single-molecule confinement.

## Abbott Cell-Dyn Sapphire Hematology Optical/Impedance Flow Cell (2003)

- **id**: `abbott-cell-dyn-sapphire-flow-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Abbott Laboratories (Abbott Hematology / Cell-Dyn)
- **disclosure**: Abbott Cell-Dyn Sapphire 510(k) K022428 (cleared 2003-04); peer-reviewed evaluation Bruegel et al., Clin Lab Haematol 2004
- **ip status**: patented
- **prior art notes**: Discloses Multi-Angle Polarized Scatter Separation (MAPSS) optical flow cytometry for white-blood-cell five-part differentiation: hydrodynamically focused single-cell stream illuminated at four angles (intermediate-angle scatter, polarized side scatter, depolarized side scatter, axial light loss) plus 488 nm laser fluorescence channel for retic/NRBC. The fluidic architecture pairs a sheath-focused optical flow cell for WBC/diff/retic with a Coulter-principle sapphire impedance aperture for RBC/PLT in parallel, with shared sample dilution stages. Anticipates: hybrid optical-impedance hematology fluidic stages sharing sample dilution; depolarized side-scatter eosinophil identification via crystalline content; sapphire as orifice material for impedance counting (durability against erosion vs ruby/glass).

## MBARI Environmental Sample Processor (ESP) (2003)

- **id**: `mbari-esp-environmental-sample-processor`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Monterey Bay Aquarium Research Institute (MBARI) (Scholin lab) / McLane Research Laboratories (commercial 2G/3G ESP)
- **disclosure**: Scholin CA et al., 'The Environmental Sample Processor (ESP) — An autonomous robotic device for detecting microorganisms remotely using molecular probe technology,' Proc. OCEANS 2003: 1-7 (2003); Scholin CA et al., 'Remote detection of marine microbes, small invertebrates, harmful algae, and biotoxins using the Environmental Sample Processor (ESP),' Oceanography 22(2):158-167 (2009)
- **ip status**: patented
- **prior art notes**: The ESP is the canonical autonomous oceanographic microfluidic robotic sampler. Element-by-element prior art for: (a) automated puck-carousel architecture with integrated filtration + lysis + sandwich-hybridization assay + chemiluminescent readout in a long-deployment marine-robotic platform; (b) feedback-controlled adaptive sampling where the on-board assay result triggers subsequent sample collection (LRAUV+ESP plume tracking); (c) integration of ddPCR into a marine autonomous vehicle (3G ESP), which anticipates patents on autonomous in-situ qPCR/ddPCR cartridges for environmental monitoring; (d) the sealed puck format with pre-loaded dry/wet reagents stored at ocean depth for months anticipates patents on long-storage diagnostic cartridges in extreme environments. ESP is also the closest terrestrial analog to a planetary in-situ life detection cartridge.

## Battlestar Galactica Galactica sickbay (Doc Cottle's bay) (2003)

- **id**: `bsg-galactica-sickbay-cottle`
- **corpus**: fictional
- **device class**: fictional-laboratory
- **creator**: Ronald D. Moore / Universal Television
- **disclosure**: Battlestar Galactica miniseries (Sci Fi 2003) and series (2004-2009).
- **ip status**: fictional
- **prior art notes**: Galactica sickbay depicted across many episodes as a multi-bed military medical bay with manual+automated diagnostics, the Cylon detection assay (an explicit cellular-level diagnostic), pregnancy tests with Cylon-specific markers, and surgical interventions. Defensive prior art for: military-grade triage bay architecture and species/origin-discriminating cellular assays at the bedside.

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

## ARROW liquid-core optical waveguide on chip (2004)

- **id**: `schmidt-hawkins-arrow-waveguide`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Schmidt (UCSC), Hawkins (BYU)
- **disclosure**: Yin, D.; Schmidt, H.; Barber, J. P.; Hawkins, A. R. Integrated ARROW waveguides with hollow cores. Opt. Express 2004, 12, 2710–2715. DOI: 10.1364/OPEX.12.002710
- **ip status**: patented
- **prior art notes**: Disclosed antiresonant reflecting optical waveguide (ARROW) with a hollow core that can be filled with sample fluid: a liquid-core waveguide enabling guided light through the analyte itself. Anticipates: liquid-core integrated waveguides, on-chip absorbance/fluorescence in-line analysis without external optical components, and ultra-sensitive single-molecule detection by guided-mode interaction. Foundational architecture for chip-integrated optical detection.

## Fluidigm BioMark Dynamic Array Chemistry Patent Family (2004)

- **id**: `fluidigm-patent-family-biomark-dynamic-array`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Fluidigm Corporation (now Standard BioTools)
- **disclosure**: US7820427; US8420017; US8475743; US9663819 (Fluidigm Corporation)
- **ip status**: patented
- **prior art notes**: Fluidigm BioMark Dynamic Array patent family. Anchors claims around: (a) two-axis valve matrix combinatorially addressing N x M reaction chambers from N samples and M assays; (b) MLSI valves isolating each reaction chamber after combinatorial loading; (c) thermal cycling and end-point fluorescence per chamber; (d) specific 48.48 / 96.96 / 192.24 array geometries. Anticipates combinatorial qPCR microfluidic chips and high-multiplex digital PCR cartridges. Companion to existing fluidigm-dynamic-array-ifc entry. Expiry: 2024-2028 across family.

## 454 Life Sciences PicoTiterPlate sequencing (2005)

- **id**: `margulies-2005-454-picotiterplate`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: 454 Life Sciences (acquired by Roche 2007)
- **disclosure**: Margulies, M. et al. Genome sequencing in microfabricated high-density picolitre reactors. Nature 2005, 437, 376–380. DOI: 10.1038/nature03959
- **ip status**: patented
- **prior art notes**: Disclosed PicoTiterPlate: a fiber-optic faceplate etched into ~1.6M picoliter wells, each loaded with a single template-loaded bead for emulsion-PCR-amplified pyrosequencing. The first commercial massively parallel sequencing platform (2005); discontinued 2016. Architectural ancestor of every microwell-array-based NGS platform that followed (Ion Torrent, BGI, Singular Genomics).

## Theranos Cartridge Patent Family (2005)

- **id**: `theranos-cartridge-patent-family`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Theranos Inc. (defunct 2018; patents reassigned)
- **disclosure**: US7888125 priority 2005-03-24; US7494770; US8088593; US8158430; US8283155 (Theranos Inc., post-bankruptcy assignments to Fortress Investment Group / Labrador Diagnostics)
- **ip status**: patented
- **prior art notes**: Theranos cartridge patent family. Anchors claims around: (a) handheld disposable diagnostic cartridge accepting finger-stick blood; (b) integrated reagent-storage, sample-prep, and detection chambers; (c) on-cartridge assay scheduling and barcode identification; (d) wireless data return to a central reader. Notable for two reasons: (1) the patents were granted but the corresponding products never demonstrated the claimed performance (FDA correspondence and later trial testimony established this); (2) post-bankruptcy the patents were reassigned to Fortress Investment Group / Labrador Diagnostics, which asserted them against working diagnostic companies (notably BioFire) during the COVID pandemic, drawing significant criticism. Defensive value is high: Theranos patent disclosures contain extensive claim language but minimal enabling disclosure, making them weak as offensive prior art but useful as anti-claim-scope ammunition for any cartridge integrator to cite as evidence that broad cartridge claims are not novel. Companion existing entry: theranos-promised-cartridge documents the marketing claim; this entry catalogs the asserted IP.

## McDevitt Nano-Bio-Chip for Salivary Periodontal and Cardiac Biomarker Detection (2005)

- **id**: `christodoulides-2005-nano-bio-chip-perio`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: John T. McDevitt group (Univ. Texas Austin / Rice / NYU)
- **disclosure**: Christodoulides N, Mohanty S, Miller CS, et al., Lab on a Chip 5:261-269 (2005); doi:10.1039/B414194F
- **ip status**: patented
- **prior art notes**: Discloses a programmable bead-based fluidic cassette in which agarose beads functionalized with capture antibodies are arranged in etched silicon microwells under a sealed flow channel. The architecture is configurable per assay by changing bead loading. Anticipates: configurable bead-array microfluidic immunoassay cartridges; salivary periodontal disease panels using multiplex bead capture; bead-array p-BNC architectures for any saliva or serum panel; the broader 'electronic taste chip' lineage.

## Developing optofluidic technology through the fusion of microfluidics and optics (2006)

- **id**: `psaltis-2006-optofluidic-review`
- **corpus**: academic
- **device class**: other
- **creator**: Psaltis (Caltech), Quake (Caltech), Yang (Caltech)
- **disclosure**: Psaltis, D.; Quake, S. R.; Yang, C. Developing optofluidic technology through the fusion of microfluidics and optics. Nature 2006, 442, 381–386. DOI: 10.1038/nature05060
- **ip status**: public-domain
- **prior art notes**: Framing review establishing 'optofluidics' as a research program: the integration of microfluidics with optical waveguides, lasers, lenses, and resonators to make tunable photonic devices. Anticipates: liquid-core optical waveguides (ARROW), tunable microfluidic lenses, and integrated detection on-chip. Methodological review that defined the optofluidics field.

## Singulex Erenna single-molecule counting immunoassay (2006)

- **id**: `todd-singulex-erenna-2006`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Singulex Inc.
- **disclosure**: Todd, J.; Freese, B.; Lu, A.; Held, D.; Morey, J.; Livingston, R.; Goix, P. Ultrasensitive flow-based immunoassays using single-molecule counting. Clin. Chem. 2007, 53, 1990–1995. DOI: 10.1373/clinchem.2007.091181
- **ip status**: patented
- **prior art notes**: Disclosed single-molecule counting immunoassay: fluorescent immunocomplexes flow through a confocal interrogation volume in a microfluidic capillary, generating discrete photon bursts that are individually counted rather than ensemble-integrated. Anticipates: capillary-flow single-molecule counting as immunoassay-detection mode (sub-femtomolar sensitivity), and one of the architectural paths now embodied in Quanterix Simoa (microwell counting) and Singulex (capillary counting). Singulex was acquired by EMD Millipore 2018; the architectural disclosures remain part of the foundational prior-art for ultrasensitive POC immunoassays.

## Roche Cobas 6000 Modular Analyzer Fluidic Track (2007)

- **id**: `roche-cobas-6000-modular-fluidics`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Roche Diagnostics
- **disclosure**: Roche Diagnostics Cobas 6000 product launch 2007; AACC product showcase; FDA 510(k) K072321 (c501 module)
- **ip status**: patented
- **prior art notes**: Discloses a modular clinical analyzer fluidics architecture: a single primary-tube sample-handling rail introduces blood/serum/plasma to multiple specialized assay modules (photometric c501 with permanent cuvette wheel; electrochemiluminescence e601 with disposable ECL cups containing electrode-paramagnetic-bead capture). The c501 module uses a thermostatted rotary cuvette wheel with washable permanent cuvettes; the e601 uses single-use polypropylene assay cups with integrated read-while-flow ECL detection at a Pt working electrode. Anticipates: hybrid permanent-cuvette + disposable-cup analyzer trains; ruthenium-tag ECL detection in disposable cups with paramagnetic bead capture and on-electrode wash; modular interconnect of clinical chemistry and immunoassay sharing primary-tube sample handler.

## ISS Lab-on-Chip Application Development Portable Test System (LOCAD-PTS) (2007)

- **id**: `iss-locad-pts-handheld-bioassay`
- **corpus**: academic
- **device class**: point-of-care-cartridge
- **creator**: NASA Marshall Space Flight Center / Charles River Laboratories (Endosafe-PTS) / University of Surrey
- **disclosure**: Maule J et al., 'Rapid culture-independent microbial analysis aboard the International Space Station (ISS) Stage Two: Quantifying microbial Burden,' Astrobiology 9(8):759-775 (2009), doi:10.1089/ast.2008.0319; Morris HC et al., 'Lab-on-a-Chip Application Development Portable Test System (LOCAD-PTS) on the International Space Station,' SAE Tech. Paper 2007-01-3142 (2007)
- **ip status**: patented
- **prior art notes**: LOCAD-PTS is the spaceflight derivative of the Charles River Endosafe PTS handheld endotoxin tester. Microfluidic prior art disclosed: (a) the 4-channel parallel capillary-driven cartridge with lyophilized LAL/glucan-detection reagents and integrated optical absorbance window is itself prior art for any cartridge claiming similar handheld bioburden / pyrogen testing in resource-constrained environments (spaceflight, military forward operating, deep-sea); (b) the qualification of the cartridge for microgravity operation (no syringe / no positive pressure source — purely capillary wicking) is prior art for capillary-driven point-of-care cartridges that are deliberately pump-free for environments where pumping is failure-prone; (c) the published ISS protocol for swab-elute-load-read in <15 min anticipates cartridge-based environmental microbial monitoring patents for industrial and built-environment applications. The Charles River Endosafe US patents are the IP citations; the spaceflight qualification is open-published.

## Illumina Solexa sequencing flow cell (2008)

- **id**: `bentley-2008-illumina-flow-cell`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Bentley et al., Illumina / Solexa
- **disclosure**: Bentley, D. R. et al. Accurate whole human genome sequencing using reversible terminator chemistry. Nature 2008, 456, 53–59. DOI: 10.1038/nature07517
- **ip status**: patented
- **prior art notes**: Foundational disclosure of the Illumina sequencing flow cell: a glass channel with patterned oligo lawn supporting bridge amplification, reversible-terminator sequencing chemistry, and per-channel optical scanning. Architecturally a microfluidic device, although it is rarely classified as one in microfluidics literature. Anticipates: patterned-flow-cell architecture for massively parallel single-molecule chemistry, and the entire Illumina commercial sequencing platform that dominated the genomics market 2010–2025.

## BD BACTEC FX Blood Culture Bottle Fluorescence Detection (referenced; predominantly BD product) (2008)

- **id**: `biomerieux-bactec-fx-bottle-fluorescence`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Becton Dickinson (BD Diagnostics)
- **disclosure**: BD BACTEC FX launch 2008; FDA 510(k) K081298; BACTEC fluorescent CO2 sensor patent US4945060 (1990)
- **ip status**: patented
- **prior art notes**: Discloses non-invasive optical detection of microbial growth in blood culture bottles via a polymer-embedded fluorescent CO2-sensitive dye disk bonded to the bottle's interior bottom; CO2 produced by metabolizing organisms diffuses into the polymer matrix, lowering pH, increasing protonation of the dye and shifting fluorescence emission. The reader monitors each bottle every 10 minutes via LED illumination through the bottle bottom and PMT detection of dye fluorescence. Anticipates: optical-bottom growth-monitoring blood culture systems (vs the displaced colorimetric Bactec NR system requiring needle-stick CO2 sampling); the architectural pattern of disposable bottle-as-sensor with continuous external optical readout — the fluidic-engineering primitive being reagent-free monitoring through a polymer membrane.

## Thermo Fisher Phadia 2500 Allergy/Autoimmune ImmunoCAP Cartridge (2008)

- **id**: `thermo-fisher-phadia-2500-immunoassay`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Thermo Fisher Scientific (formerly Phadia AB / Pharmacia Diagnostics)
- **disclosure**: Phadia 2500 launch 2008; Phadia 5000 launch 2009; FDA 510(k) K071727 (Phadia 250 predecessor); ImmunoCAP first cleared 1989
- **ip status**: patented
- **prior art notes**: Discloses the ImmunoCAP solid-phase fluorescent enzyme immunoassay: a cellulose-based 3D porous matrix in a capsule, derivatized with allergen, providing massively expanded surface area (vs flat-bottom microtiter wells) for IgE binding kinetics; the capsule is the disposable assay element, transported through automated wash, conjugate, and substrate steps in a Phadia rotor analyzer. Anticipates: 3D porous solid-phase immunoassay matrices as the binding-kinetics primitive distinguishing allergy testing (which requires capturing very low IgE concentrations against extract heterogeneity); the WHO IgE calibration traceability that established Phadia/ImmunoCAP as the global allergy reference. Element-by-element architectural disclosure relevant to all derivative ImmunoCAP assays (Phadia 100, 250, 1000, 2500, 5000).

## ChemoMetec NucleoCounter NC-200 / NC-3000 Single-Use Cassette (2008)

- **id**: `chemometec-nucleocounter-nc-200-cassette`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: ChemoMetec A/S
- **disclosure**: ChemoMetec NucleoCounter NC-3000 launch 2008; NC-200 launch 2014; cell viability via DAPI fluorescence imaging
- **ip status**: patented
- **prior art notes**: Discloses the Via-1 single-use cassette architecture: a sealed disposable microfluidic chamber pre-loaded with acridine orange (AO, all-cells stain) + DAPI (dead-cells stain), with an integrated piston-syringe for user-driven 60 µL sample aspiration, optical window for CCD imaging, and embedded lot/calibration QR code. The NucleoCounter platform replaces flow-cell hematology-style cell counting with a static-chamber image-cytometry primitive — eliminating clogging issues with clumpy bioreactor samples. Anticipates: image-cytometry single-use cassette format for biopharma cell counting; lysis-free total + viable cell count using AO+DAPI fluorescence imaging; the 21 CFR Part 11 GMP-traceable single-cassette workflow (audit trail per cassette). Distinguishes from Beckman Vi-CELL (Trypan Blue + brightfield + flow cell) by static-chamber + fluorescence approach.

## Real-time DNA sequencing from single polymerase molecules (PacBio SMRT) (2009)

- **id**: `eid-2009-pacbio-smrt`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Pacific Biosciences
- **disclosure**: Eid, J. et al. Real-time DNA sequencing from single polymerase molecules. Science 2009, 323, 133–138. DOI: 10.1126/science.1162986
- **ip status**: patented
- **prior art notes**: Disclosed Single-Molecule Real-Time (SMRT) sequencing using zero-mode waveguides (ZMWs) — sub-wavelength metal apertures that confine fluorescence excitation to zeptoliter-scale volumes around individual immobilized polymerases. Anticipates: ZMW-array architecture, single-molecule fluorescence sequencing without amplification, and the long-read sequencing market commercialized by PacBio.

## Single molecule arrays (Simoa) for ultrasensitive immunoassay (2010)

- **id**: `rissin-2010-quanterix-simoa`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Walt group, Tufts / Quanterix
- **disclosure**: Rissin, D. M. et al. Single-molecule enzyme-linked immunosorbent assay detects serum proteins at subfemtomolar concentrations. Nat. Biotechnol. 2010, 28, 595–599. DOI: 10.1038/nbt.1641
- **ip status**: patented
- **prior art notes**: Disclosed single-molecule immunoassay (Simoa): trap individual antibody-functionalized beads in femtoliter microwells, isolate by oil overlay to digitize fluorogenic-substrate signal per bead. Anticipates: femtoliter-microwell-array architecture for digital ELISA, oil-isolated chamber arrays for single-molecule chemistry, and the Quanterix HD-X / SR-X commercial platforms. Sub-femtomolar protein detection in serum.

## Quidel Sofia rapid immunoassay cartridge (2010)

- **id**: `quidel-sofia-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Quidel Corporation (now QuidelOrtho)
- **disclosure**: Quidel Corporation Sofia immunoassay platform. https://www.quidel.com
- **ip status**: patented
- **prior art notes**: Lateral-flow immunoassay cartridge with fluorescence-based signal amplification and dedicated benchtop reader. Architecturally a hybrid between visual lateral-flow and instrumented LFA. Used widely for influenza and respiratory virus rapid testing in primary-care settings.

## BGI MGI DNBSEQ sequencer flow cell (2010)

- **id**: `bgi-mgi-dnbseq-flowcell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Complete Genomics (acquired by BGI 2013) / MGI
- **disclosure**: Drmanac, R. et al. Human genome sequencing using unchained base reads on self-assembling DNA nanoarrays. Science 2010, 327, 78–81. DOI: 10.1126/science.1181498
- **ip status**: patented
- **prior art notes**: DNA nanoball (DNB) sequencing: rolling-circle-amplified DNA nanoballs spotted on patterned silicon arrays for combinatorial probe-anchor-ligation sequencing. Architecturally distinct from Illumina (bridge amplification) and Ion Torrent (clonal microwell) by using pre-amplified template nanoballs. The dominant non-Illumina sequencing platform globally by deployed instrument count, particularly outside the US market. Anticipates: nanoball-array architecture for high-density sequencing, and the architectural diversity of post-2010 short-read sequencer platforms.

## Smartphone-based microscopy and microfluidic imaging (Ozcan 2010) (2010)

- **id**: `ozcan-2010-smartphone-microscopy`
- **corpus**: academic
- **device class**: other
- **creator**: Ozcan group, UCLA
- **disclosure**: Tseng, D.; Mudanyali, O.; Oztoprak, C.; Isikman, S. O.; Sencan, I.; Yaglidere, O.; Ozcan, A. Lensfree microscopy on a cellphone. Lab Chip 2010, 10, 1787–1792. DOI: 10.1039/C003477B
- **ip status**: patented
- **prior art notes**: Foundational disclosure of smartphone-based lensless holographic microscopy for chip imaging: a sample on a microfluidic chip is illuminated by an LED placed atop a smartphone camera, producing a holographic shadow that is computationally reconstructed into an image. Anticipates: smartphone-as-microscope architecture for field-deployable microfluidic diagnostics, lensless computational imaging on chip, and the entire smartphone-based POC imaging subfield. Underlies dozens of subsequent academic and commercial efforts (Cellscope, Nuralogix, Ozcan-spinout commercial products).

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

## Hamilton Arc Intelligent Sensors (pH, DO, ORP, conductivity) (2010)

- **id**: `hamilton-arc-sensors`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Hamilton Bonaduz AG
- **disclosure**: Hamilton Bonaduz AG Arc sensor platform launch 2010; Hamilton Arc View 3 product datasheet; product literature 2012-2023
- **ip status**: patented
- **prior art notes**: Discloses an intelligent-sensor architecture where the calibration data, signal conditioning electronics, and digital communication interface are all resident in the probe head, allowing the probe to be moved between transmitters without recalibration. The VisiFerm DO variant uses an optical-spot fluorescence-quenching architecture in which a luminophore is excited and the lifetime of fluorescence quenching is proportional to dissolved oxygen — supports both stainless and single-use (patch) form factors. Anticipates: digital intelligent-sensor architecture for bioprocess PAT (distinguishable from analog probes whose calibration lives in the transmitter); luminescence-lifetime DO measurement compatible with single-use bioreactor patch sensors.

## ChemoMetec NucleoCounter NC-3000 (Image Cytometer) (2010)

- **id**: `chemometec-nucleocounter-nc-3000`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: ChemoMetec A/S
- **disclosure**: ChemoMetec A/S NC-3000 product launch 2010; product literature 2012-2023; ChemoMetec patent estate US8,309,025B1 (Cassette for cell counting based on fluorescent staining)
- **ip status**: patented
- **prior art notes**: Discloses a fluorescence imaging cytometer in which a disposable polycarbonate cassette is pre-loaded with lyophilized AO (acridine orange, total nuclei) and DAPI (membrane-impermeable, dead-cell nuclei) dyes; sample is loaded by capillary action; the NC-3000 instrument acquires 8-channel fluorescence images and counts total/dead cells with viability calculation. Distinguishable from NC-200 (single-channel viability only) by the 8-channel image cytometry capability. Anticipates: closed-cassette image-cytometry architecture with pre-loaded fluorescent stains for bioprocess viability/density measurement; multi-assay panel via cassette-format extensibility. Element-by-element: capillary-fill cassette + lyophilized stain + epi-fluorescence imaging + cell-counting algorithm.

## Crescendo Bioscience Vectra DA Multi-Biomarker Disease Activity Test (2010)

- **id**: `crescendo-vectra-da-test`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Crescendo Bioscience Inc. (Myriad Genetics from 2014)
- **disclosure**: Centola M et al., PLOS ONE 8:e60635 (2013); doi:10.1371/journal.pone.0060635; Crescendo Bioscience product literature (acquired by Myriad Genetics 2014); CMS LCD L34416
- **ip status**: patented
- **prior art notes**: Discloses a 12-plex serum-biomarker chemiluminescence cartridge (built on Meso Scale Discovery flow cells) with disease-activity-score algorithmic output for rheumatoid arthritis. Anticipates: clinical-grade multiplex chemiluminescence cartridges with reportable composite scores; serum-biomarker microfluidic flow-cell architectures coupled to ML/regression scoring algorithms.

## Bio-Rad QX Droplet Digital PCR system (2011)

- **id**: `bio-rad-qx-ddpcr-system`
- **corpus**: private
- **device class**: droplet-generator
- **creator**: Bio-Rad / QuantaLife
- **disclosure**: Bio-Rad Laboratories QX100/QX200 ddPCR systems. Hindson et al. 2011 Anal. Chem. 83, 8604–8610. DOI: 10.1021/ac202028g
- **ip status**: patented
- **prior art notes**: Discloses an integrated commercial workflow for droplet digital PCR: cartridge-based generation of ~20,000 monodisperse droplets per sample, off-chip thermal cycling, and droplet-by-droplet fluorescence readout. Anticipates: the digital-PCR workflow as a discrete commercial category, integration of injection-molded droplet-generation cartridges with an instrument-side flow controller, and a sample-to-answer ddPCR system architecture.

## Bio-Techne / ProteinSimple Simple Western (capillary western) (2011)

- **id**: `proteinsimple-westernblot-simple-western`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: ProteinSimple (acquired by Bio-Techne)
- **disclosure**: Bio-Techne ProteinSimple Simple Western platform. https://www.bio-techne.com/p/simple-western/wes
- **ip status**: patented
- **prior art notes**: Capillary-format automated western blot replacement: protein separation by SDS capillary electrophoresis, UV-induced covalent immobilization to capillary wall, antibody probing, and chemiluminescence detection — all on a single instrument with disposable capillary cartridges. Anticipates: capillary-immobilization westerns, automated multi-step immunodetection on a microfluidic-equivalent capillary substrate, and the broader trend of replacing manual molecular biology bench protocols with cartridge-format automation.

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

## Pearce Lab MOST Open Scientific Hardware Suite (2012)

- **id**: `pearce-most-open-hardware-suite`
- **corpus**: open
- **device class**: other
- **creator**: Joshua M. Pearce (Michigan Technological University), MOST research group
- **disclosure**: Pearce J.M., 'Building Research Equipment with Free, Open-Source Hardware', Science 337:1303-1304 (2012), doi:10.1126/science.1228183; Pearce J.M., 'Open-Source Lab' (Elsevier 2014, ISBN 978-0-12-410462-4); https://www.appropedia.org/Category:MOST
- **ip status**: open-copyleft
- **prior art notes**: Discloses a foundational suite of >50 published open lab instruments from a single research group, including: open syringe pump (already cataloged separately), open peristaltic pump, open colorimeter, open spectrophotometer, open mass-balance, open magnetic stirrer hot-plate, open shaker incubator, open laser-cut/3D-printed centrifuge, open optical-density meter, open temperature-controlled stage. Each is published with full BOM, parametric CAD (typically OpenSCAD), firmware, and calibration data. Together these constitute a substantial fraction of the post-2012 open lab-equipment commons. Citable as 102 prior art against many commercial 'low-cost lab instrument' patents from 2014-2024. Specifically anticipates the architectural pattern of a research lab releasing its full instrument library as a coordinated commons under permissive licenses.

## Smartphone-based photonic-crystal biosensor (2013)

- **id**: `zhang-cunningham-2014-smartphone-photonic-detection`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Cunningham group, UIUC
- **disclosure**: Gallegos, D.; Long, K. D.; Yu, H.; Clark, P. P.; Lin, Y.; George, S.; Nath, P.; Cunningham, B. T. Label-free biodetection using a smartphone. Lab Chip 2013, 13, 2124–2132. DOI: 10.1039/C3LC40991K
- **ip status**: patented
- **prior art notes**: Disclosed smartphone-based label-free biosensor: photonic-crystal resonant reflectance read by smartphone camera through diffraction-grating-based spectrometer attachment. Anticipates: photonic-crystal biosensor + smartphone optical readout, distinct architectural family from camera-based imaging POC tests.

## Profusa Lumee implantable hydrogel oxygen sensor (2014)

- **id**: `profusa-lumee-implantable`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Profusa Inc.
- **disclosure**: Profusa Inc. Lumee Oxygen Platform. https://profusa.com
- **ip status**: patented
- **prior art notes**: Implantable subcutaneous hydrogel-encapsulated phosphorescent oxygen sensor with optical readout through skin. Architecturally a tissue-resident microfluidic-equivalent that performs continuous biosensing without extracorporeal sample handling. Anticipates: implantable-hydrogel sensor as a category, optical-readout-through-skin architecture, and the broader 'continuous tissue biosensor' product class.

## Sysmex CS-2500 / CN-6000 Coagulation Analyzer Multi-Wavelength Cuvette (2014)

- **id**: `sysmex-cs-2500-coag-automated`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Sysmex Corporation (in partnership with Siemens for hemostasis menu)
- **disclosure**: Sysmex CS-2500 launch 2014-04; CN-6000 (next-gen) launch 2018; FDA 510(k) K140617 (CS-2500)
- **ip status**: patented
- **prior art notes**: Discloses a coagulation analyzer with pre-analytical HIL flagging integrated into the same cuvette as the assay measurement: before reagent dispense, the analyzer reads plasma absorbance at 340/405/575/660/800 nm to detect hemoglobin (free Hb >0.2 g/dL), bilirubin, and lipid scattering, allowing the analyzer to skip or reflex assays whose chemistry is invalidated by interference (e.g., D-dimer immunoturbidimetric is invalidated by lipemia). The five-wavelength optical detection consolidates clot turbidity (PT/aPTT), chromogenic substrate hydrolysis (chromogenic factor activity), and immunoturbidimetric (D-dimer, antithrombin antigen) in a single cuvette type. Anticipates: pre-analytical HIL detection in the assay cuvette as a fluidic-engineering primitive enabling reflex routing; multi-wavelength optical detection consolidating diverse coag chemistries in one cuvette; the Sysmex/Siemens partnership architecture (Sysmex hardware + Siemens HemosIL-equivalent reagent menu).

## Vapourtec R-Series with UV-150 photochemical reactor and V-3 peristaltic pump (2014)

- **id**: `vapourtec-r-series-uv-150`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Vapourtec Ltd.
- **disclosure**: Vapourtec UV-150 photochemical reactor product launch 2014; Williams, J. D.; Nakano, M.; Gérardy, R.; Rincón, J. A.; García-Losada, P.; Mateos, C.; Hawkins, J. M.; Jensen, K. F.; Monbaliu, J.-C. M.; Kappe, C. O. 'Finding the perfect match: a combined computational and experimental study toward efficient and scalable photosensitized [2+2] cycloadditions in flow' Org. Process Res. Dev. 2019, 23, 78–87; Vapourtec V-3 peristaltic pump datasheet 2017
- **ip status**: patented
- **prior art notes**: Distinct from base vapourtec-flow-chemistry entry. Discloses (a) jacketed-tubing photochemical reactor architecture, with FEP tubing wound on quartz immersion well, swappable medium-pressure mercury or LED lamp; (b) integration of slurry-tolerant peristaltic V-3 pump within the same R-series electrical/communication backbone, enabling solid-handling reactions in continuous flow that historically required batch reactors; (c) the architectural pattern of plug-and-play modules sharing a USB-controlled bus. Anticipates patent claims directed to fluoropolymer-tubing photoreactors with switchable-wavelength lamp jackets, and to slurry-tolerant peristaltic pumps integrated into commercial flow chemistry rigs.

## Takara Bio iCell8 cx Single-Cell System (Wafergen) (2014)

- **id**: `takara-icell8-cx`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Wafergen Biosystems / Takara Bio
- **disclosure**: Wafergen Biosystems ICELL8 launch 2014; acquired by Takara Bio 2018. https://www.takarabio.com/products/automation-systems/icell8-system-and-software. Goldstein, L. D. et al. Massively parallel nanowell-based single-cell gene expression profiling. BMC Genomics 2017, 18, 519. DOI: 10.1186/s12864-017-3893-1.
- **ip status**: patented
- **prior art notes**: Image-guided single-cell dispensing into a silicon nanowell chip: a MultiSample NanoDispenser deposits ~50 nL droplets across a 5,184-well chip, on-chip imaging identifies single-cell-containing wells, and only those wells receive downstream reagents. Anticipates: image-guided 'select-then-dispense' single-cell architectures, distinct from Poisson-loaded microwell or droplet platforms; integration of computer-vision feedback into the cell-loading step. The 'pick-only-the-good-wells' architecture is a meaningful prior-art point against later image-feedback single-cell systems (e.g., Cytena, NanoCellect).

## Jana Care Aina Portable Diagnostic Device (2014)

- **id**: `jana-care-aina-portable-device`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Jana Care Inc.
- **disclosure**: Jana Care Inc. product launches 2014-2017; company technical brochures; FDA 510(k) K191498 (Aina HbA1c test) 2019
- **ip status**: patented
- **prior art notes**: Discloses a smartphone-tethered POC diagnostic platform whose disposable element is a lateral-flow or microfluidic test strip and whose reader is a reusable optical pod. Capillary blood applied to the strip, optics quantify color development from immunoassay or enzymatic chemistry. Anticipates: smartphone-tethered consumer POC test architectures; reader-pod-plus-disposable-strip business model in low-resource settings.

## 10x Genomics Xenium In-Situ Patent Family (2014)

- **id**: `tenx-genomics-xenium-in-situ-patent-family`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: 10x Genomics Inc. (acquired ReadCoor 2020-10-12 for $350M and Cartana 2020-11-23)
- **disclosure**: US10227639 (ReadCoor / Wyss Institute origin); US11459611; US11788123 (10x Genomics post-acquisition); US10227639 priority 2014
- **ip status**: patented
- **prior art notes**: 10x Genomics Xenium / In Situ patent family. Combines the ReadCoor (Wyss Institute, George Church origin) FISSEQ technology and the Cartana (Mats Nilsson origin) padlock-probe in-situ chemistry. Anchors claims around: (a) padlock probes targeting specific transcripts; (b) rolling-circle amplification of bound padlocks creating amplicons in tissue; (c) sequential hybridization rounds with fluorescent decoder probes; (d) decoding amplicon barcodes to identify transcripts at subcellular resolution; (e) Xenium Analyzer fluidic / imaging instrument. Existing companion entries: 10x-xenium-prime-5k, vizgen-merscope (competitor), resolve-bioscience-molecular-cartography (competitor). 10x has asserted parts of this family against Vizgen and Resolve.

## Berkeley Lights Beacon optofluidic platform (2016)

- **id**: `berkeley-lights-beacon`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Berkeley Lights / PhenomeX / Bruker
- **disclosure**: Berkeley Lights Inc. Beacon platform launch 2016. Le, K. et al. A novel mammalian cell line development platform utilizing nanofluidics and optoelectro positioning technology. Biotechnol. Prog. 2018, 34:1438-1446. doi:10.1002/btpr.2690. Foundational optoelectronic-tweezers patent: US7612355B2 (UC Berkeley, Wu et al.; priority 2003).
- **ip status**: patented
- **prior art notes**: Discloses an optofluidic single-cell platform: an OptoSelect chip combines a photoconductive layer with patterned electrodes such that a projected light pattern induces local dielectrophoretic forces sufficient to translate individual cells into and out of nanoliter pen chambers. Within each pen, individual cells can be cultured, assayed for secretion (e.g., antibody titer via fluorescent bead reporter), and selectively retrieved. Anticipates: (a) optoelectronic-tweezer single-cell manipulation in commercial nanofluidic chips; (b) in-chip clonal expansion and secretion-assay workflows for hybridoma/B-cell antibody discovery and biopharma cell-line development; (c) optofluidic CGT applications including TCR/CAR T-cell functional screening at single-cell resolution.

## Berkeley Lights Beacon (PhenomeX, now Bruker) optofluidic platform (2016)

- **id**: `phenomex-beacon-bli`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Berkeley Lights / PhenomeX (Bruker)
- **disclosure**: Berkeley Lights Beacon system launch 2016. Le, K. et al. A novel mammalian cell line development platform utilizing nanofluidics and OptoElectro Positioning technology. Biotechnol. Prog. 2018, 34, 1438-1446. DOI: 10.1002/btpr.2690. PhenomeX rebrand 2022; acquired by Bruker 2023.
- **ip status**: patented
- **prior art notes**: Optoelectronic-positioning (OEP) single-cell array: a CMOS-photoconductor chip with overlaid microfluidic NanoPen chambers, where projected light patterns generate localized electric-field dielectrophoretic forces that move single cells into individual NanoPens. In-pen assays (proliferation, antibody secretion) are imaged on-instrument; selected clones can be exported. Anticipates: light-addressed dielectrophoretic single-cell handling on a CMOS substrate; the integration of a photoconductor-based DEP positioner with a closed microfluidic NanoPen array for clonal cell-line development; the broader category of light-driven addressable cell-handling chips. Acquisition trajectory (Berkeley Lights -> PhenomeX -> Bruker) and the breadth of the patent family make this a significant prior-art anchor.

## ISS WetLab-2 Real-Time RT-PCR on Station (2016)

- **id**: `iss-wetlab-2-rt-pcr-on-station`
- **corpus**: open
- **device class**: lab-on-chip
- **creator**: NASA Ames Research Center / Cepheid (SmartCycler thermal block heritage) / BioRad (CFX-derived optics)
- **disclosure**: Parra M et al., 'Microgravity validation of a novel system for RNA isolation and multiplex quantitative real time PCR analysis of gene expression on the International Space Station,' PLOS ONE 12(9):e0183480 (2017), doi:10.1371/journal.pone.0183480; NASA WetLab-2 facility description, ISS Research Office (2016)
- **ip status**: open-permissive
- **prior art notes**: Discloses an end-to-end RNA-extraction + RT-qPCR cartridge architecture qualified for microgravity. Element-by-element prior art: (a) the closed-cartridge magnetic-bead RNA extraction protocol with no open-air liquid transfer steps anticipates patents claiming aerosol-free spaceflight or BSL-3 nucleic acid extraction cartridges; (b) the validation of paramagnetic-bead binding/wash kinetics in zero-G is published prior art against any patent claiming novel microgravity-compatible bead handling; (c) the integration of off-the-shelf SmartCycler-class Peltier modules with a custom reaction tube format anticipates retrofit spaceflight diagnostic cartridge concepts. Combined with iss-biomolecule-sequencer-minion below, WetLab-2 establishes the full sample-prep + amplification + sequencing chain in spaceflight prior art.

## Senseonics Eversense Implantable Continuous Glucose Monitor (2016-05)

- **id**: `senseonics-eversense-implantable-cgm`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Senseonics Holdings Inc.
- **disclosure**: CE-Mark 2016; FDA PMA P160048 June 2018; Senseonics 10-K filings
- **ip status**: patented
- **prior art notes**: Discloses a fully implantable cylindrical sensor whose active element is a fluorescent boronic-acid-functionalized hydrogel that reversibly binds glucose; an external on-skin transmitter powers and interrogates the implant via near-infrared excitation through the skin. The hydrogel acts as the microfluidic envelope: interstitial fluid diffuses in and out, glucose binding modulates fluorescence quenching. Anticipates: long-term implantable glucose biosensors using non-enzymatic recognition; transcutaneous optical readout of subcutaneous polymer biosensors; the entire device class of implantable hydrogel-based sensors interrogated by skin-mounted readers.

## Epicore Biosystems Microfluidic Sweat Sensor Patch (2016-11-23)

- **id**: `epicore-biosystems-sweat-patch`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Epicore Biosystems Inc. (Northwestern / Rogers spin-out)
- **disclosure**: Koh A et al. Sci Transl Med 8(366):366ra165 2016 doi:10.1126/scitranslmed.aaf2593 (already in corpus as koh-rogers-2016-epidermal-microfluidic — this entry covers the Epicore commercial product line spun out from Rogers lab)
- **ip status**: patented
- **prior art notes**: Commercial product line built around the Rogers-lab epidermal microfluidic platform (academic disclosure already covered by koh-rogers-2016-epidermal-microfluidic). Discloses skin-adhered PDMS patches with sub-millimeter serpentine channels routing sweat into discrete colorimetric assay chambers (chloride, glucose, lactate, pH) that change color as sweat fills them, read by smartphone camera. Anticipates: capillary-driven sweat sample collection at gland scale (microliter volumes); multi-analyte colorimetric reservoir architecture in a wearable patch; Gatorade Gx and Connected Hydration commercial implementations.

## Bionano Genomics Saphyr optical genome mapping (2017)

- **id**: `nanofluidics-bionano-saphyr`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Bionano Genomics
- **disclosure**: Bionano Genomics Saphyr system. https://bionano.com
- **ip status**: patented
- **prior art notes**: Disclosed nanochannel-array chip that linearizes individual long DNA molecules in fluorescently-labeled form for optical genome mapping. Anticipates: nanochannel-array architecture for single-molecule DNA elongation, and label-pattern detection of long-range structural variation invisible to short-read sequencing.

## BGI / MGI cartridge product family extensions (2017)

- **id**: `bgi-mgi-cartridge-extensions`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: BGI / MGI Tech
- **disclosure**: BGI MGI subsidiary product family. https://en.mgi-tech.com
- **ip status**: patented
- **prior art notes**: MGI Tech is BGI's sequencing-instrument subsidiary; cumulative MGI cartridge product family (DNBSEQ-T7, DNBSEQ-G400, etc.) extends the original Complete Genomics DNB technology with multiple instrument configurations. Together with native Chinese semiconductor manufacturing, MGI is positioned to compete with Illumina globally. Cumulative cartridge architectural disclosures from this family expand the broader sequencing-cartridge prior art.

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

## Mathies/Quinn 2017 Microchip Capillary Electrophoresis for Mars Amino Acid Detection (2017)

- **id**: `mathies-quinn-2017-microchip-ce-mars-amino-acids`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Richard Mathies group (UC Berkeley) / Peter Willis (NASA JPL) / Maria Mora (NASA JPL) / Aaron Noell
- **disclosure**: Mora MF et al., 'Toward total automation of microfluidics for extraterrestrial in situ analysis,' Anal. Chem. 83:8636 (2011); Mora MF et al. (Mathies/Quinn group), 'Capillary electrophoresis amino acid sensitivity from a chip-based instrument,' Electrophoresis 38:2982 (2017), doi:10.1002/elps.201700110
- **ip status**: patented
- **prior art notes**: The Mathies/Quinn line of work is the most extensively-published academic flight-prototype for microfluidic life detection on Mars and icy moons. Element-by-element prior art: (a) the integration of programmable PDMS-on-glass membrane valves with on-chip CE separation for extraterrestrial sample analysis anticipates any patent claiming integrated sample-prep + electrophoretic-separation + LIF cartridges for planetary instruments; (b) the published parts-per-trillion sensitivity for fluorescamine-labeled amino acids in a portable / battery-powered instrument anticipates patents claiming similar sensitivity in handheld biosensors; (c) chiral separation as a biosignature-discrimination strategy on a microchip CE format anticipates any patent claiming D/L enantiomer microfluidic separation for biosignature detection. The Mora 2011/2017 papers also disclose the architectural pattern of a fully-automated 'Mars Organic Analyzer' (MOA) cartridge.

## Namocell Hana Single Cell Dispenser (2017)

- **id**: `namocell-hana-single-cell-dispenser`
- **corpus**: private
- **device class**: dispenser-pipettor
- **creator**: Namocell Inc. (acquired by Bio-Rad 2021)
- **disclosure**: Namocell Inc. product launch 2017 (Stanford spinout, Bio-Rad acquisition 2021); US10625259B2 priority 2014
- **ip status**: patented
- **prior art notes**: Discloses a disposable cartridge implementing pressure-driven flow-focusing droplet ejection coupled to a real-time fluorescence detector that gates each droplet's destination plate well based on cell count and fluorescence intensity. Anticipates: integrated single-use cell sorter that delivers verified single cells into target wells without sheath-fluid contamination paths; disposable plastic equivalent of a sterile FACS sort with deposition recorded per well. Specifically anticipates claims to single-cell printers that combine flow-focusing droplet generation with downstream fluorescence-based well assignment.

## Pacific Biosciences vs Oxford Nanopore Patent Litigation 2017-2024 (2017-02-23)

- **id**: `pacbio-vs-oxford-nanopore-litigation`
- **corpus**: private
- **device class**: other
- **creator**: Pacific Biosciences (plaintiff) vs Oxford Nanopore Technologies (defendant)
- **disclosure**: Pacific Biosciences v. Oxford Nanopore, D.Del. 1:17-cv-00275 (filed 2017-02-23); ITC investigation 337-TA-1062; UK High Court [2017]; Federal Circuit appeals 2019-2024
- **ip status**: patented
- **prior art notes**: Litigation entry. PacBio sued Oxford Nanopore in 2017 in D.Del., the ITC, and the UK High Court asserting that ONT's MinION nanopore-sequencing technology infringed PacBio's single-molecule sequencing patents. Cases proceeded for seven years. Most rulings favored ONT: PacBio's broad single-molecule sequencing claims were narrowed or invalidated; ONT prevailed in UK; ITC investigation 337-TA-1062 closed favorably for ONT. Settled around 2024. Defensive value: invalidates broad-scope claims to 'single-molecule sequencing in general' and confirms that PacBio's enforceable scope is essentially limited to ZMW-specific implementations. Useful for any nanopore or single-molecule sequencing developer.

## Chi.Bio open-hardware bioreactor (2018)

- **id**: `chibio-bioreactor`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Steel et al., Oxford / Imperial
- **disclosure**: Steel, H.; Habgood, R.; Kelly, C.; Papachristodoulou, A. In situ characterisation and manipulation of biological systems with Chi.Bio. PLOS Biol. 2020, 18, e3000794. DOI: 10.1371/journal.pbio.3000794
- **ip status**: open-permissive
- **prior art notes**: Open-hardware bioreactor with integrated optical density measurement, fluorescence detection, peristaltic pumping, and feedback-controlled environment. ~$700 BOM. Anticipates: prosumer-grade closed-loop bioreactor for synthetic biology, with feedback control between sensors and actuators built into a benchtop form factor. Strong IP-clearing significance for the small-bioreactor space.

## Heska Element HT5 Veterinary Hematology Image Cytometry Analyzer (2018)

- **id**: `heska-element-ht5-veterinary-imaging`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Heska Corporation (now Mars Petcare)
- **disclosure**: Heska Element HT5 launch 2018-09; product datasheet; companion Heska 510(k) K200147
- **ip status**: patented
- **prior art notes**: Discloses an in-clinic veterinary hematology analyzer using image cytometry (vs flow cytometry) for the WBC differential: stained WBCs flow through a microfluidic imaging channel under high-magnification CCD imaging, and convolutional-neural-network (CNN)-based image classification produces 5-part diff plus reticulocyte count (since 2019 software updates). Distinguishes from IDEXX ProCyte Dx (Sysmex-licensed flow cytometry), Sysmex XN, Beckman DxH, and Mindray BC-6800 (all flow cytometry-based) by retaining actual cell images for veterinarian review — important in veterinary clinical pathology where edge cases (mast cell tumor mast cells in peripheral blood, exotic species hematology) benefit from image evidence. Anticipates: image-cytometry hematology as an alternative to flow cytometry; CNN-based image classification embedded in a clinical analyzer; the architectural choice of single-cuvette image + impedance hybrid (vs separate multi-channel architecture).

## Mars 2020 Perseverance SHERLOC (Scanning Habitable Environments with Raman & Luminescence for Organics & Chemicals) (2018)

- **id**: `mars2020-sherloc-spectrometer`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: NASA Jet Propulsion Laboratory / Photon Systems Inc. (deep-UV laser)
- **disclosure**: Bhartia R et al., 'Perseverance's Scanning Habitable Environments with Raman and Luminescence for Organics and Chemicals (SHERLOC) Investigation,' Space Science Reviews 217:58 (2021), doi:10.1007/s11214-021-00812-z; Beegle LW et al., '2018 SHERLOC instrument briefing'
- **ip status**: public-domain
- **prior art notes**: Although SHERLOC has minimal classical fluidics, it is a load-bearing prior art entry for the broader 'in-situ life detection' patent landscape because it discloses (a) a deep-UV resonance-Raman + native-fluorescence dual-mode standoff cartridge architecture as an alternative to wet-chemistry GCMS for organic detection, (b) a co-mounted optical micrometer (WATSON) providing context imaging for spectroscopic point picks, and (c) the use of polymer/fabric witness samples on the calibration target as a vehicle for additional in-flight prior-art disclosure (the spacesuit Vectran/polycarbonate samples become public-domain prior art for astronaut suit polymers by virtue of being launched). For invalidation purposes, SHERLOC anticipates any claim to a deep-UV (sub-260 nm) raster-Raman cartridge for biosignature detection or any claim to a combined Raman/LIF standoff astrobiology head with mineralogical context co-imaging.

## Nexcelom Cellaca PLX (and MX) Image Cytometer (2018)

- **id**: `nexcelom-cellaca-plx`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Nexcelom Bioscience LLC (now Revvity)
- **disclosure**: Nexcelom Bioscience Cellaca MX product launch 2018; Cellaca PLX (high-throughput plate version) launched 2021; US patent US10,222,373B2 (Nexcelom, cell counting cassette); Nexcelom acquired by PerkinElmer (now Revvity) 2021
- **ip status**: patented
- **prior art notes**: Discloses a multi-well disposable counting plate format for image cytometry: each well has an integrated optical-quality bottom window; the instrument acquires brightfield + AO/PI fluorescence images per well in parallel; total count, viable count, and viability are computed per well. The Cellaca PLX increases parallelism to 96-well plate format. Anticipates: plate-format parallel image cytometry (vs serial single-cassette NC-200/NC-3000); high-throughput cell-counting suitable for bioprocess sampling at scale. Element-by-element: multi-well disposable plate + per-well stain + multi-channel imaging + per-well cell-count algorithm.

## MGI DNBSEQ-T7 flow cell (2018-10)

- **id**: `mgi-dnbseq-t7-flow-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: MGI Tech (BGI)
- **disclosure**: MGI Tech DNBSEQ-T7 launch at ICG-13, October 2018. https://en.mgi-tech.com/products/instruments_info/4/.
- **ip status**: patented
- **prior art notes**: High-throughput DNB-array sequencing instrument with four parallel patterned silicon flow cells. Each flow cell carries a high-density spot pattern matched to the nanoball size; nanoballs deposit one-per-spot for combinatorial probe-anchor-ligation sequencing. Anticipates: parallel-flow-cell ultra-throughput sequencer architectures, multi-flow-cell scheduling and reagent sharing, and the patterned-spot-plus-nanoball architecture at T7 scale. Distinguishes the T7 generation from the smaller G400 and the original DNBSEQ flow cell.

## MGI DNBSEQ-G400 flow cell (2019)

- **id**: `mgi-dnbseq-g400-flow-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: MGI Tech (BGI)
- **disclosure**: MGI Tech DNBSEQ-G400 product launch 2019. https://en.mgi-tech.com/products/instruments_info/3/.
- **ip status**: patented
- **prior art notes**: Mid-throughput sibling of T7; same DNB-on-patterned-silicon architecture at smaller scale, intended for clinical and translational labs. Anticipates: the explicit segmentation of the same core flow-cell architecture into clinical-mid and discovery-high configurations within one product family, parallel to Illumina's NextSeq vs. NovaSeq segmentation.

## Berkeley Lights Lightning Optofluidic System (2019)

- **id**: `berkeley-lights-lightning`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Berkeley Lights Inc. (now PhenomeX)
- **disclosure**: Berkeley Lights Lightning product launch 2019; Berkeley Lights S-1 SEC filing 2020-06; OptoElectroPositioning patent estate US9,023,628B2
- **ip status**: patented
- **prior art notes**: Variant of the Berkeley Lights OptoSelect / Beacon architecture in which the optoelectronic positioning array is paired with on-chip imaging and a transfection workflow within the NanoPen chambers — distinct from the original Beacon (cell-line development focus) by including transfection-after-isolation as a single integrated workflow. Anticipates: optoelectronic-positioning chip extended with on-chip transfection events triggered after single-cell isolation; combined imaging + delivery in the same chamber array. Element-by-element: photoconductor array + NanoPen chamber + objective + on-chip pulse/cargo flush + clonal recovery export.

## Vernier Microfluidics Sensor Bundle for Education (2019)

- **id**: `vernier-microfluidics-kit`
- **corpus**: private
- **device class**: consumable-bulk
- **creator**: Vernier Science Education
- **disclosure**: Vernier Software & Technology catalog 'Microfluidics' lab manual; vernier.com
- **ip status**: trade-secret
- **prior art notes**: Discloses a microfluidic teaching chip bundled with logging optical/pH sensors for data-acquisition curricula. Anticipates: microfluidic-plus-data-logger education bundles; sensor-instrumented microfluidic teaching cartridges.

## Illumina vs BGI/MGI Patent Litigation 2019-2022 (2019-06-27)

- **id**: `illumina-vs-bgi-litigation`
- **corpus**: private
- **device class**: other
- **creator**: Illumina Inc. (plaintiff) vs BGI Genomics / Complete Genomics / MGI Tech (defendants)
- **disclosure**: Illumina v. BGI, D.Del. 1:19-cv-01201 (filed 2019-06-27); ITC 337-TA-1167; UK High Court actions; settled 2022
- **ip status**: patented
- **prior art notes**: Litigation entry. Illumina sued BGI / Complete Genomics / MGI Tech in 2019 in multiple jurisdictions (D.Del., ITC, UK High Court) alleging that BGI's DNBSEQ flow cells (existing entries: bgi-mgi-dnbseq-flowcell, bgi-mgi-cartridge-extensions) infringed Illumina's flow-cell and SBS chemistry patents. Settled 2022 with a cross-license that allowed MGI sequencers to enter the US market with royalties paid to Illumina. Defensive value: established the enforceable scope of Illumina's flow-cell claims and confirmed that DNB-rolling-circle clonal amplification on patterned arrays is distinct enough from bridge-amplification to be patentable separately.

## Squid open-hardware microscopy platform (2020)

- **id**: `squid-microscope`
- **corpus**: open
- **device class**: other
- **creator**: Prakash Lab, Stanford (Hongquan Li, Deepak Krishnamurthy, et al.)
- **disclosure**: Hongquan Li, Deepak Krishnamurthy, et al. (Prakash Lab Stanford). https://github.com/hongquanli/octopi-research and https://squid-imaging.org
- **ip status**: open-permissive
- **prior art notes**: Open-hardware microscopy platform with multi-axis stage, autofocus, multiple imaging modalities (brightfield, fluorescence, phase) and integration with microfluidic chips. Modular and reconfigurable. Anticipates: open-hardware microscopy for high-throughput cell-imaging on chip, replacing $50k-$200k commercial systems with sub-$10k builds. Important reference for any chip-imaging-based microfluidic platform.

## Deep learning for microfluidic imaging diagnostics (Ballard/Ozcan 2020) (2020)

- **id**: `ballard-ozcan-2020-machine-learning-imaging`
- **corpus**: academic
- **device class**: other
- **creator**: Ozcan group, UCLA
- **disclosure**: Ballard, Z. S.; Brown, C.; Madni, A. M.; Ozcan, A. Machine learning and computation-enabled intelligent sensor design. Nat. Mach. Intell. 2021, 3, 556–565. DOI: 10.1038/s42256-021-00360-9
- **ip status**: patented
- **prior art notes**: Methodological framing of deep-learning-augmented microfluidic and POC sensors: ML for image enhancement, multiplexed assay readout, anomaly detection, and computational reconstruction of holographic data. Anticipates: ML-enabled POC microfluidic assays as a category, distinct from non-ML approaches by orders-of-magnitude improvement in sensitivity and specificity. Sets methodological framework for any 'AI-enhanced microfluidic diagnostic' patent claim.

## Resolve Biosciences Molecular Cartography (2020)

- **id**: `resolve-bioscience-molecular-cartography`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Resolve Biosciences
- **disclosure**: Resolve Biosciences Molecular Cartography platform. https://resolvebiosciences.com/. Groiss, S. et al. Highly resolved spatial transcriptomics for detection of rare cell populations. bioRxiv 2021.10.11.463936. DOI: 10.1101/2021.10.11.463936.
- **ip status**: patented
- **prior art notes**: Subcellular-resolution spatial transcriptomics using sequential single-molecule FISH on a perfusion fluidic platform. Architecturally adjacent to MERSCOPE (Vizgen) and CosMx (NanoString) but with distinct decoding chemistry (Resolve uses a smaller number of imaging rounds with high-fidelity probe-pair decoding). Anticipates: alternative encoding schemes for multiplexed in-situ-hybridization spatial transcriptomics; a European competitor in the hybridization-cycle spatial omics race.

## Namocell Pala Single Cell Dispenser (2020)

- **id**: `namocell-pala-single-cell-dispenser`
- **corpus**: private
- **device class**: dispenser-pipettor
- **creator**: Namocell Inc. (Bio-Rad)
- **disclosure**: Namocell Pala datasheet 2020; Bio-Rad press 2021; US patent family above
- **ip status**: patented
- **prior art notes**: Extends Hana design to 5-color fluorescence and explicit doublet discrimination by per-droplet image analysis. Anticipates claims to disposable-cartridge multi-color cell sorters with image-based event verification and per-deposit traceability metadata for regulated single-cell-cloning workflows (cell-line provenance documentation under USP/ICH guidelines).

## Logos Biosystems LUNA-FX7 Automated Cell Counter (2020)

- **id**: `logos-luna-fx7`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Logos Biosystems Inc.
- **disclosure**: Logos Biosystems LUNA-FX7 product launch 2020; user manual rev 2.0; predecessor LUNA-II product literature 2014-2019
- **ip status**: patented
- **prior art notes**: Discloses a compact image-cytometer with a multi-chamber disposable slide (8 wells per slide) and three-channel fluorescence imaging for bioprocess/research cell counting. Architecturally similar to NucleoCounter NC-3000 and Cellaca MX; differentiated by slide form factor and 3-channel fluorescence (vs 8-channel NC-3000 or 24-well Cellaca). Anticipates: compact bench-top image-cytometer with multi-chamber disposable slide and multi-channel fluorescence for combined viability + reporter-gene measurement.

## Thermo Fisher Countess 3 / Countess 3 FL Automated Cell Counter (2020)

- **id**: `thermofisher-countess-3`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Thermo Fisher Scientific (Invitrogen)
- **disclosure**: Thermo Fisher Scientific Countess 3 product launch 2020; Countess II original launch 2014; user guide MAN0019150 rev 1.0; predecessor patent estate US8,481,332B2 (Invitrogen, Countess hemocytometer slide)
- **ip status**: patented
- **prior art notes**: Discloses an automated hemocytometer architecture in which a disposable two-chamber slide is loaded by capillary action with sample + trypan blue stain (or unstained for fluorescence); the instrument autofocuses, acquires brightfield + optional fluorescence images, segments cells, and computes total/dead/viable counts. The Countess 3 generation adds two-channel fluorescence and improved imaging optics. Anticipates: automated brightfield+fluorescence cell-counting on a disposable hemocytometer slide with embedded counting chambers. Element-by-element: disposable slide + brightfield/fluorescence imaging + autofocus + cell-segmentation algorithm + count display.

## DnaNudge / NudgeBox Rapid Cartridge PCR System (2020-03)

- **id**: `dnanudge-rapid-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: DnaNudge Ltd. (Imperial College London spin-out)
- **disclosure**: Gibani MM et al. Lancet Microbe 1(7):e300-e307 2020 doi:10.1016/S2666-5247(20)30121-X (CovidNudge clinical evaluation); UK MHRA authorization
- **ip status**: patented
- **prior art notes**: Discloses a self-contained sample-to-answer PCR cartridge integrating swab-input, lysis, RT-PCR, and fluorescence detection. Originally a consumer DTC nutrigenomics product (NudgeBox at point of sale in supermarkets), repurposed for COVID-19. Anticipates: consumer-genomics sample-to-answer cartridges; supermarket point-of-sale DNA testing topology; reuse of consumer-genomics cartridge designs for infectious-disease detection.

## CARMEN Combinatorial Arrayed Reactions for Multiplexed Evaluation Patent Family (2020-04-29)

- **id**: `quake-broad-carmen-multiplex-prep-patent`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: Broad Institute / Harvard (Sabeti, Myhrvold, Ackerman)
- **disclosure**: US Provisional 62/892,447; published as WO2021022045A1 (Broad Institute / Harvard)
- **ip status**: patented
- **prior art notes**: Broad Institute patent family covering CARMEN (Combinatorial Arrayed Reactions for Multiplexed Evaluation of Nucleic acids). Anchors claims around: (a) microfluidic platform for high-throughput multiplexed nucleic-acid detection using fluorescent-color-coded droplets; (b) merging of sample droplets with CRISPR-Cas13 detection-reagent droplets; (c) automated identification of droplet pairs by color barcode; (d) parallel detection of >100 pathogens per chip. Ackerman et al. Nature 2020 (myhrvold-zhang-2018-shine-crispr-on-paper covers SHINE; CARMEN is distinct) provides the academic disclosure. Defensive interest: Broad Institute is the assertive licensor in CRISPR diagnostics; this patent family overlaps Mammoth/Sherlock claim space and any droplet-pairing combinatorial diagnostic.

## 10x Genomics Acquisition of ReadCoor (in situ sequencing) 2020 (2020-10-12)

- **id**: `tenx-readcoor-acquisition-2020`
- **corpus**: private
- **device class**: other
- **creator**: 10x Genomics Inc.
- **disclosure**: 10x Genomics 8-K filed 2020-10-12; total consideration approximately $350M cash plus stock
- **ip status**: patented
- **prior art notes**: Consolidation event entry. 10x Genomics 8-K 2020-10-12 documents the acquisition of ReadCoor Inc. (Wyss Institute / George Church spinout) for approximately $350M. ReadCoor's FISSEQ in-situ sequencing IP, combined with the November 2020 Cartana acquisition, formed the technical and patent basis for the Xenium platform launched 2022. Useful as IP-due-diligence reference and as anchor for tenx-genomics-xenium-in-situ-patent-family. Note that 10x then asserted these acquired patents against Vizgen and Resolve Biosciences (see related litigation entries).

## Aspendia cardiac POC cartridge (sub-femtomolar troponin) (2021)

- **id**: `aspendia-cardiac-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Quanterix Aspendia / various
- **disclosure**: Quanterix-acquired Aspendia / various 2020s ultrasensitive troponin POC cartridges.
- **ip status**: patented
- **prior art notes**: Composite reference for emerging POC cardiac biomarker cartridges achieving sub-femtomolar (single-molecule-counting class) sensitivity for high-sensitivity troponin and similar markers. Architectural successor to ELISA-format cartridges by leveraging Simoa-style single-molecule detection in disposable cartridge form factor. Active subfield 2020-onward.

## Beckman Coulter DxI 9000 Access Immunoassay Reaction Vessel Track (2021)

- **id**: `beckman-coulter-dxi-9000-immunoassay`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Beckman Coulter (Danaher)
- **disclosure**: Beckman Coulter DxI 9000 launch 2021-09; FDA 510(k) K223188 (cleared 2023)
- **ip status**: patented
- **prior art notes**: Discloses a single-use reaction vessel immunoassay analyzer optimized for cardiac STAT throughput: each RV is loaded onto a continuous track, receives sample + PMP-conjugated capture antibody + alkaline-phosphatase-labeled detection antibody via independently controlled pipettors, undergoes magnet-station capture and wash within the same RV (no transfer), and is moved to the dioxetane-substrate dispense and PMT integration station. Anticipates: high-throughput single-use RV immunoassay tracks with in-vessel PMP wash; alkaline-phosphatase + Lumi-Phos 530 dioxetane chemiluminescence substrate (alternative to acridinium ester and ECL); the centralized fluidic path where sample-and-reagent transit is robotic but each RV is the immutable assay vessel. Foundational fluidic difference from Roche e-series (ECL on electrode) and Abbott Architect (CMIA flash on washed wells) — Beckman uses prolonged glow chemiluminescence integrated for 4-5 seconds.

## Kraken Sense KRAKEN1 Automated Pathogen Detection System (2021)

- **id**: `kraken-sense-pathogen-detection`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Kraken Sense Inc.
- **disclosure**: Kraken Sense Inc. product literature; krakensense.com; CES 2022 disclosure
- **ip status**: patented
- **prior art notes**: Discloses an automated industrial water-pathogen monitoring cartridge that performs concentration, lysis, LAMP amplification, and detection from large-volume water samples. Anticipates: automated industrial-water pathogen monitoring cartridges; LAMP-on-cartridge with upstream filtration concentration; IoT-connected food-safety monitoring with disposable cartridges.

## Olive Diagnostics KG Toilet-Mounted Urine Optical Analyzer (2021)

- **id**: `olive-diagnostics-kg`
- **corpus**: private
- **device class**: other
- **creator**: Olive Diagnostics Ltd.
- **disclosure**: Olive Diagnostics Ltd. product launch 2021; olivedx.com; CE mark 2022
- **ip status**: patented
- **prior art notes**: Discloses a passive in-toilet optical urine analyzer that monitors a free-flowing urine stream rather than collecting a discrete sample. Anticipates: passive in-toilet urinalysis architectures; consumable-free continuous urinalysis using optical interrogation of free flow; the architectural pattern of clip-on bathroom-fixture biosensors for continuous biomarker monitoring.

## Talis One COVID-19 Test Cartridge (2021-02)

- **id**: `talis-one-covid-19-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Talis Biomedical Corp.
- **disclosure**: Talis Biomedical FDA EUA application 2021-02 (rejected); product literature; US11103864B2
- **ip status**: patented
- **prior art notes**: Discloses a fully-integrated POC molecular test cartridge combining magnetic-bead extraction with RT-LAMP amplification within a credit-card-sized disposable, paired with a benchtop reader. Anticipates: integrated extraction-plus-amplification POC cartridges in flat planar form factor; magnetic-bead-based on-cartridge sample prep paired with RT-LAMP. Useful prior art against POC cartridge claims that combine sample-prep and amplification within a flat single-use disposable.

## Vizgen MERSCOPE platform (2021-05-19)

- **id**: `vizgen-merscope`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Vizgen Inc.
- **disclosure**: Vizgen MERSCOPE product launch press release 2021-05-19. https://vizgen.com/. Chen, K. H. et al. Spatially resolved, highly multiplexed RNA profiling in single cells. Science 2015, 348, aaa6090. DOI: 10.1126/science.aaa6090.
- **ip status**: patented
- **prior art notes**: Commercial MERFISH (Multiplexed Error-Robust FISH) platform from the Zhuang lab spinout. A perfusion flow cell over the tissue cycles fluorescent readout probes; combinatorial barcodes encoded across N rounds yield 2^N - error-corrected transcript identities. Anticipates: error-robust combinatorial in-situ hybridization-cycle architectures distinct from CosMx (which uses encoded probe pools differently); the architectural pattern of an open-top perfusion chamber clamped over a slide for many-cycle in-situ fluorescence.

## Clearblue Connected Digital Pregnancy Test (Bluetooth) (2021-06)

- **id**: `clearblue-connected-digital-pregnancy`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: SPD Swiss Precision Diagnostics GmbH (Procter & Gamble / Abbott JV)
- **disclosure**: SPD Swiss Precision Diagnostics product launch 2021; Clearblue Connected technical brochure
- **ip status**: patented
- **prior art notes**: Discloses a consumer lateral-flow pregnancy test with on-board electronic optical readout and Bluetooth telemetry. Lateral-flow nitrocellulose strip is the microfluidic substrate; conjugate pad releases gold-labeled hCG antibodies, sample wicks across capture line, photodetector quantifies optical density. Anticipates: connected-consumer lateral-flow architectures; smartphone-paired single-use diagnostic disposables.

## Visby Medical Sexual Health Test Cartridge (2021-08)

- **id**: `visby-medical-sexual-health-test-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Visby Medical Inc.
- **disclosure**: Visby Medical FDA 510(k) K201013 cleared 2021-08-04; US10434511B2 priority 2014; expansion to OTC test FDA 2024
- **ip status**: patented
- **prior art notes**: Discloses a palm-sized disposable PCR cartridge integrating sample lysis, thermocycling, fluorescent detection, and visible result indication entirely within the consumable, with battery-powered electronics and no separate reader instrument. Anticipates: instrument-free PCR cartridges for STI detection where the disposable contains all hardware including LEDs, photodiodes, microcontroller, and battery; OTC molecular diagnostic form factors that fit the consumer-test point-of-purchase model. Anticipates claims to single-cartridge molecular tests where the consumable itself implements thermocycling and optical detection.

## Pioreactor (2021-09)

- **id**: `pioreactor-open-bioreactor`
- **corpus**: open
- **device class**: other
- **creator**: Pioreactor (Cameron Lab / Pioreactor Inc., Toronto)
- **disclosure**: Cadart C., Bartlett J. et al., Pioreactor open-source hardware release on GitHub https://github.com/Pioreactor/pioreactor (initial public release Sept 2021); pioreactor.com product page; documentation site docs.pioreactor.com
- **ip status**: open-permissive
- **prior art notes**: Discloses an open-source benchtop bioreactor platform built around a Raspberry Pi HAT (the Pioreactor 'Pioreactor HAT'), which integrates: (a) an LED+photodiode optical density measurement subsystem with synchronous detection (LED chopping plus lock-in style demodulation) on a low-cost MCU; (b) a magnetic stirrer driven by a brushless DC motor with closed-loop RPM control via a Hall sensor; (c) a heating element on a PCB underneath a 20 mL borosilicate glass vial with thermistor feedback; (d) a peristaltic-pump dosing module driven over I2C for continuous-culture (turbidostat/chemostat/morbidostat) operation; (e) a clustered control architecture using MQTT pub/sub over Wi-Fi enabling fleet operation of dozens of units from a single 'leader' Pi. All hardware schematics (KiCad), firmware, mechanical CAD, and Python control software are released under MIT (software) and CERN-OHL-S/CC-BY (hardware). Anticipates: low-cost networked bioreactor fleets with synchronous-detection turbidity sensing on a Raspberry Pi class device; pluggable Python automation classes for closed-loop bioprocess control (turbidostat/chemostat/morbidostat); MQTT-clustered laboratory device fleets where each unit is autonomous but coordinated. Specifically prior art against any patent claiming 'a networked low-cost bioreactor with on-board OD sensing controlled via a single-board computer running open-source bioprocess automation software with cluster coordination via lightweight pub/sub messaging.'

## Nix Hydration Biosensor (2021-09-22)

- **id**: `nix-hydration-biosensor`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Nix Biosensors Inc.
- **disclosure**: Nix Inc. product launch 2021; Reinertsen E et al. founder publications; product manual rev 1
- **ip status**: patented
- **prior art notes**: Discloses a single-use sweat patch with a passive microfluidic network distributing sweat to colorimetric reagent pads, with a reusable optical reader puck snapping onto the patch and streaming hydration estimates to phone. The reader sees absorbance changes as sweat fills successive chambers. Anticipates: hybrid disposable-patch-plus-reusable-reader microfluidic architectures; capillary-routed colorimetric hydration tracking.

## Detect Inc. COVID-19 RT-LAMP Cartridge (2021-10)

- **id**: `detect-inc-covid-19-rt-lamp-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Detect Inc.
- **disclosure**: Detect Inc. FDA EUA 2021-10-29 (originally Homodyne Health); product user manual rev 2
- **ip status**: patented
- **prior art notes**: Discloses a hub-and-cartridge isothermal-amplification consumer molecular diagnostic with reusable heater/reader and disposable reagent cartridge, FDA-EUA-cleared for at-home COVID-19. Anticipates: hub-and-cartridge consumer OTC molecular test architectures that decouple a reusable heater/optics module from disposable single-use cartridges; FDA-EUA-cleared RT-LAMP at-home tests targeting respiratory pathogens.

## Illumina vs Singular Genomics Patent Litigation (Singular won 2024) (2021-12-13)

- **id**: `illumina-vs-singular-genomics-litigation`
- **corpus**: private
- **device class**: other
- **creator**: Illumina Inc. (plaintiff) vs Singular Genomics Systems Inc. (defendant)
- **disclosure**: Illumina v. Singular Genomics, D.Del. 1:21-cv-01798 (filed 2021-12-13); jury verdict and PTAB IPR rulings favoring Singular, 2024
- **ip status**: patented
- **prior art notes**: Litigation entry. Illumina sued Singular Genomics in D.Del. 1:21-cv-01798 (2021-12-13) alleging G4 flow-cell and SBS chemistry infringement (existing entry: singular-genomics-g4). Singular largely won at trial and at PTAB, with several asserted Illumina claims invalidated. Defensive value high: this is one of the first major-vendor losses for Illumina on flow-cell IP and significantly narrows the enforceable scope of the post-Solexa estate. Useful for any sequencing-flow-cell developer.

## Element Biosciences AVITI sequencer flow cell (2022)

- **id**: `element-biosciences-aviti`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Element Biosciences
- **disclosure**: Element Biosciences AVITI system. https://www.elementbiosciences.com
- **ip status**: patented
- **prior art notes**: Patterned-flow-cell sequencer using avidite chemistry — a polymer-tethered fluorescent reporter for sequencing-by-synthesis distinct from Illumina's reversible terminator. Architecturally a flow cell similar to Illumina but with patent-free chemistry. Part of the post-2020 Illumina-IP-expiry wave of competing patterned-flow-cell sequencers.

## Singular Genomics G4 sequencer flow cell (2022)

- **id**: `singular-genomics-g4`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Singular Genomics
- **disclosure**: Singular Genomics G4 system. https://www.singulargenomics.com
- **ip status**: patented
- **prior art notes**: Patterned-flow-cell sequencer with parallel-flow-cell architecture for fast turnaround. Part of the post-2020 wave of Illumina alternatives. Microfluidically very similar to AVITI and Illumina; differentiation is in chemistry and instrument throughput.

## Quantum-Si Platinum protein sequencer (2022)

- **id**: `quantum-si-platinum`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Quantum-Si (founded by Jonathan Rothberg)
- **disclosure**: Quantum-Si Platinum system. https://www.quantum-si.com
- **ip status**: patented
- **prior art notes**: CMOS chip for single-molecule protein sequencing using time-domain fluorescence lifetime detection on a chip with millions of waveguide-coupled wells. Architectural cousin to PacBio ZMWs but with CMOS readout and a different chemistry (N-terminal aminopeptidase cycling). Anticipates: integrated-CMOS-photonic protein sequencing chip, time-domain detection on integrated photodetectors.

## Illumina vs Element Biosciences Patent Litigation (settled 2024) (2022-04-04)

- **id**: `illumina-vs-element-biosciences-litigation`
- **corpus**: private
- **device class**: other
- **creator**: Illumina Inc. (plaintiff) vs Element Biosciences Inc. (defendant)
- **disclosure**: Illumina v. Element Biosciences, D.Del. 1:22-cv-00410 (filed 2022-04-04); settled 2024
- **ip status**: patented
- **prior art notes**: Litigation entry. Illumina sued Element Biosciences in D.Del. 1:22-cv-00410 (2022-04-04) asserting flow-cell and SBS chemistry patents against the Element AVITI sequencer (existing entries: element-biosciences-aviti, element-biosciences-aviti-cloudbreak). Settled 2024 (terms partly confidential) with Element continuing to operate. Defensive value: documents which Illumina patents were asserted against a non-bridge-amplification competitor (Element uses Avidity sequencing chemistry, distinct from SBS).

## Akoya Biosciences PhenoCycler-Fusion (2022-04-26)

- **id**: `akoya-phenocycler-fusion`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Akoya Biosciences
- **disclosure**: Akoya Biosciences PhenoCycler-Fusion product launch press release 2022-04-26. https://www.akoyabio.com. Combination of CODEX iterative-fluorescence cycling (Goldman 2018) with the Fusion high-speed scanner.
- **ip status**: patented
- **prior art notes**: Integrated automation of CODEX (Goldman 2018) iterative DNA-tag-cycled antibody staining: a perfusion fluidic chamber clamps over a tissue slide, automated reagent cycling adds and cleaves DNA-conjugated antibodies, and the high-speed Fusion scanner images the slide between cycles. Anticipates: integrated tissue-slide perfusion-and-image-cycle architectures; CODEX productization with automated fluidics, distinguishing from earlier manual or microscope-mounted CODEX implementations.

## OpenFlexure Delta Stage (2022-05)

- **id**: `openflexure-deltastage-2022`
- **corpus**: open
- **device class**: other
- **creator**: OpenFlexure Project (Bowman lab, U of Bath; Sharkey lab, U of Glasgow)
- **disclosure**: Wadsworth W., Knapper J., Stirling J., Collins J.T., Bowman R. (Bath / Glasgow), 'Open-source 3D-printed delta-stage microscope for fluorescence and biofluidic experiments', published as part of OpenFlexure project releases at https://openflexure.org/projects/deltastage/; companion paper Knapper et al., Wellcome Open Research 7:65 (2022); https://gitlab.com/openflexure/openflexure-microscope
- **ip status**: open-copyleft
- **prior art notes**: Discloses a 3D-printable delta-kinematic flexure stage as a successor to the original OpenFlexure microscope's monolithic body. Three printed flexure arms meet at a movable platform; each arm is actuated by a stepper motor through a 3D-printed gear reduction, and the geometry resolves into XYZ stage motion. Designed explicitly to host on-stage microfluidic devices for live-cell imaging, with provision for perfusion tubing through the stage. Anticipates any post-2022 claim to 'a 3D-printed delta-flexure microscope stage suitable for hosting microfluidic devices' or 'a fully 3D-printable XYZ flexure stage with sub-micron repeatability for biological imaging.'

## 10x Genomics vs Vizgen Patent Litigation (in situ) (2022-05-09)

- **id**: `tenx-vs-vizgen-litigation`
- **corpus**: private
- **device class**: other
- **creator**: 10x Genomics + Harvard (plaintiffs) vs Vizgen (defendant)
- **disclosure**: 10x Genomics Inc. and President and Fellows of Harvard College v. Vizgen Inc., D.Del. 1:22-cv-00595 (filed 2022-05-09)
- **ip status**: patented
- **prior art notes**: Litigation entry. 10x Genomics + Harvard sued Vizgen in D.Del. 1:22-cv-00595 (filed 2022-05-09) asserting in-situ sequencing and MERFISH-related patents against Vizgen's MERSCOPE platform. Vizgen counterclaimed for IPR challenges and antitrust. Existing companion entries: vizgen-merscope, 10x-xenium-prime-5k, tenx-genomics-xenium-in-situ-patent-family. Defensive value: documents the patent-positions 10x asserts in spatial transcriptomics and the IPR challenges Vizgen brought.

## 10x Genomics vs Resolve Biosciences Patent Litigation (2022-05-09)

- **id**: `tenx-vs-resolve-bioscience-litigation`
- **corpus**: private
- **device class**: other
- **creator**: 10x Genomics + Harvard (plaintiffs) vs Resolve Biosciences (defendant)
- **disclosure**: 10x Genomics Inc. v. Resolve Biosciences GmbH, D.Del. 1:22-cv-00594 (filed 2022-05-09)
- **ip status**: patented
- **prior art notes**: Litigation entry, parallel to 10x v. Vizgen. 10x Genomics + Harvard sued Resolve Biosciences in D.Del. 1:22-cv-00594 (filed 2022-05-09) asserting overlapping in-situ patents against Resolve's Molecular Cartography platform (existing entry: resolve-bioscience-molecular-cartography). Companion: tenx-vs-vizgen-litigation. Together the two suits indicate 10x's strategy of broad enforcement of its acquired Cartana/ReadCoor IP against all in-situ spatial competitors.

## Ultima Genomics UG 100 wafer-format flow cell (2022-05-31)

- **id**: `ultima-genomics-ug100-wafer`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Ultima Genomics
- **disclosure**: Almogy, G. et al. Cost-efficient whole genome sequencing using a novel mostly natural sequencing-by-synthesis approach. bioRxiv 2022.05.29.493900. DOI: 10.1101/2022.05.29.493900. Ultima Genomics commercial unveiling 2022-05-31.
- **ip status**: patented
- **prior art notes**: Radically different sequencing flow cell architecture: instead of a sealed glass channel, sequencing happens on the open surface of a 200 mm silicon wafer, with reagents distributed by spinning the wafer (centrifugal flow) and washed away likewise. Anticipates: open-substrate / centrifugal-flow sequencing flow cells; wafer-scale (rather than die-scale) sequencing substrates; the explicit elimination of channel walls in massively parallel sequencing. Fundamental architectural prior art for any open-substrate sequencing flow cell claim.

## PacBio Revio SMRT Cell (2022-10-26)

- **id**: `pacbio-revio-smrt-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Pacific Biosciences
- **disclosure**: Pacific Biosciences Revio system launch press release 2022-10-26. https://www.pacb.com/revio/. Eid, J. et al. Real-time DNA sequencing from single polymerase molecules. Science 2009, 323, 133-138. DOI: 10.1126/science.1162986 (SMRT foundational).
- **ip status**: patented
- **prior art notes**: Successor SMRT cell to the Sequel II SMRT cell, scaled to ~25 million zero-mode waveguides per cell (vs. ~8 million prior) on a single silicon die, enabling 4 cells to be processed simultaneously by the Revio instrument. Anticipates: the next-generation scaling of ZMW-array nanofluidic sequencing chips, including denser packing, parallel-cell architectures, and the tighter coupling of optical readout with on-chip nanofluidics.

## PacBio Onso short-read sequencer flow cell (2022-10-26)

- **id**: `pacbio-onso-shortread`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Pacific Biosciences (Omniome lineage)
- **disclosure**: Pacific Biosciences Onso system launch (acquired Omniome 2021); press release 2022-10-26. https://www.pacb.com/onso/. Drmanac, R. comparison data 2023.
- **ip status**: patented
- **prior art notes**: Short-read sequencer using sequencing-by-binding chemistry (Omniome): polymerase forms a stable but non-extending complex with the correct nucleotide, identity is read optically, then the polymerase is allowed to extend. The flow cell is a patterned glass surface analogous to Illumina's, but with chemistry not encumbered by Illumina's reversible-terminator IP. Anticipates: SBB short-read flow cells as a third architectural family alongside Illumina-class reversible terminators (Element AVITI, Singular G4 also in this space) and DNB arrays (BGI/MGI).

## openSPIN-EM Open Spinning-Disc / Light-Sheet Hybrid (2023)

- **id**: `openspin-em-2023`
- **corpus**: open
- **device class**: other
- **creator**: openSPIM consortium (extended by Lin et al. and other community contributors)
- **disclosure**: Multiple academic releases under the SPIM Genie / openSPIM umbrella (Pitrone et al. 2013 for openSPIM precedent; openSPIN-EM extension via the Lin lab and others 2023); https://openspim.org and forks
- **ip status**: open-permissive
- **prior art notes**: Discloses extensions to the openSPIM open-source light-sheet platform (already covered in corpus as openspim-microscope) including spinning-disc and patterned-illumination variants, designed for perfused-sample imaging. The relevant disclosure for microfluidics is the documented sample-chamber holders that integrate an open microfluidic perfusion device into the light-sheet imaging path; this provides anticipating prior art for 'integrated light-sheet imaging of microfluidically perfused organoids/embryos using open hardware.'

## Withings U-Scan Toilet-Bowl Urine Analyzer (consumer) (2023-01-04)

- **id**: `withings-u-scan`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Withings (Nokia Health)
- **disclosure**: Withings press release CES 2023, 2023-01-04; Withings U-Scan product page; withings.com/u-scan
- **ip status**: patented
- **prior art notes**: Discloses a consumer toilet-bowl-mounted device with a rotating microfluidic reagent-pad wheel: each use draws ~30 µL urine by capillary action onto the next test pad, which is then optically read and the wheel rotates to advance to a fresh pad. The 100-test-per-cartridge architecture and rotating reagent wheel anticipate: consumer in-toilet microfluidic diagnostics with multi-shot consumables; rotating-wheel passive-microfluidic reagent indexing; the architectural pattern of capillary-fed colorimetric urinalysis with downstream camera readout. CES 2023 launch makes this the first consumer microfluidic in-toilet device.

## Lucira Check-It Flu+COVID Home Test (2023-02)

- **id**: `lucira-check-it-flu-covid-test`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Lucira Health (acquired by Pfizer 2023)
- **disclosure**: Lucira Health FDA EUA 2023-02-24 first OTC home test for both Flu and COVID-19; US10864522B2
- **ip status**: patented
- **prior art notes**: Discloses an extension of the Lucira self-contained RT-LAMP cartridge architecture to multiplex (Flu A/B + COVID-19) detection within the single OTC disposable. Anticipates: multiplexed RT-LAMP at-home OTC POC molecular tests within fully-self-contained battery-powered consumable cartridges; the regulatory pathway demonstration (first OTC dual-pathogen molecular test cleared by FDA under EUA).

## Science Jubilee Lab-Automation Fork (2024)

- **id**: `sonderegger-2024-science-jubilee`
- **corpus**: open
- **device class**: dispenser-pipettor
- **creator**: Machine Agency (University of Washington); Sonderegger, Doherty, Vasquez, Galloway
- **disclosure**: Sonderegger B., Doherty B., Vasquez J., Galloway K. et al., 'Science Jubilee: an open-source toolchanging platform for liquid handling, imaging, and automation in the laboratory', HardwareX 17:e00510 (March 2024); doi:10.1016/j.ohx.2024.e00510; https://github.com/machineagency/science_jubilee
- **ip status**: open-permissive
- **prior art notes**: Discloses an open-source benchtop laboratory robot built on the Jubilee toolchanging gantry with a Python automation API (`science_jubilee`) that exposes high-level liquid-handling primitives (`pipette.transfer(...)`, `camera.capture(...)`, `fluorometer.read(...)`) over the Duet HTTP/JSON-RPC interface. Tool catalog includes an air-displacement pipette tool, a syringe tool, a top-down imaging tool, a fluorometer tool, and a microplate manipulator. The repository ships protocol scripts demonstrating colorimetric assays and bacterial dispensing. Anticipates: open-source liquid handlers using toolchanging gantries with interchangeable pipette and syringe heads, programmed in Python with high-level transfer/aspirate/dispense primitives. Specifically prior art against patents claiming proprietary 'multi-modal benchtop lab robots with hot-swappable fluidic and optical tools controlled by a single host script.'

## Akoya CODEX Athena (PhenoImager Athena) (2024)

- **id**: `akoya-codex-athena`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Akoya Biosciences
- **disclosure**: Akoya Biosciences PhenoImager Athena product announcement, 2024. https://www.akoyabio.com.
- **ip status**: unknown
- **prior art notes**: Translational-research / clinical-grade configuration of the CODEX iterative-fluidic-cycling spatial-protein platform, with workflow tailored for FFPE clinical specimens at higher throughput than PhenoCycler-Fusion. Anticipates: clinical-grade configurations of cycled-fluorescence spatial proteomics that focus on regulatory / diagnostic-development workflows rather than discovery research.

## Resolve Bioscience Molecular Cartography Pro (2024)

- **id**: `resolve-bioscience-molecular-cartography-pro`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Resolve Biosciences GmbH
- **disclosure**: Resolve Bioscience product update 2024; technical brief MC-Pro-001; original MC platform paper Groiss et al., bioRxiv 2021.10.20.464988
- **ip status**: patented
- **prior art notes**: Discloses platform extension of single-molecule FISH spatial transcriptomics with increased panel size and slide footprint, on the same fluidic delivery architecture. Anticipates claims to sub-100 nm lateral resolution spatial transcriptomics through iterative smFISH delivered by on-instrument microfluidics, distinct from amplification-based approaches (Xenium) or sequencing-by-hybridization (CosMx).

## Ultima Genomics UG100 W-series Wafer Flow Cell (2024)

- **id**: `ultima-genomics-100ug-100w-wafer-flowcell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Ultima Genomics Inc.
- **disclosure**: Ultima Genomics product update 2024; AGBT 2024 abstract; US11434531B2 / US11486003B2 (Ultima open-substrate sequencing patents)
- **ip status**: patented
- **prior art notes**: Discloses a sequencing-by-synthesis architecture in which a 200 mm patterned silicon wafer is spun on a chuck while reagents are dispensed centrally and distributed by centrifugal force to all bead-binding sites simultaneously. Anticipates: open-substrate massively parallel sequencing dispensing reagents by radial centrifugal coating instead of channelized flow; pairing of wafer-scale TDI line-scan imaging with patterned bead anchors; wafer-format scale-up of sequencing throughput by enlarging the substrate rather than increasing channel density. Distinguishes from all enclosed-flowcell sequencers (Illumina, Element, MGI) and is itself unanticipated by them. The W-series specifically scales to a 200 mm wafer (vs prior UG100 chip).

## Sherlock Biosciences SHERLOCK Cartridge (2024)

- **id**: `sherlock-biosciences-sherlock-cartridge-2024`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Sherlock Biosciences Inc.
- **disclosure**: Sherlock Biosciences press release 2024-04 SHERLOCK STI; FDA Breakthrough Designation 2023-12-14; US10266887B2 (Cas13a-based detection)
- **ip status**: patented
- **prior art notes**: Discloses a single-use disposable cartridge that performs CRISPR-based nucleic acid detection (Cas13a or Cas12a collateral cleavage of fluorogenic reporters) entirely without an external instrument. Anticipates: instrument-free CRISPR diagnostic cartridges for STI / respiratory pathogens; lyophilized-on-cartridge isothermal amplification + Cas effector cleavage workflows; consumer point-of-use form factors for at-home or pharmacy testing. Anticipates claims to fully-self-contained CRISPR diagnostic cartridges that combine isothermal amplification with collateral-cleavage readout.

## NanoString CosMx Whole Transcriptome Atlas (WTA) (2024-01)

- **id**: `nanostring-cosmx-wta-2024`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: NanoString Technologies (Bruker Spatial Biology since 2024-05)
- **disclosure**: NanoString/Bruker product launch CosMx WTA, JPM Conference 2024-01; SP-1108 datasheet rev A; AGBT 2024 abstract
- **ip status**: patented
- **prior art notes**: Discloses scaling of CosMx in-situ multiplex from ~1000-plex panels to ~18000-plex whole transcriptome through extended cycling of barcoded oligo reporters delivered by an on-instrument microfluidic system. Anticipates: on-instrument fluidic delivery sequences that perform N>16 hybridization-image-strip cycles on a single mounted slide, with microfluidic reagent storage/manifold and per-slide flowcell sealing; combinatorial barcoding scheme for ~18k targets within manageable optical-readout cycles. Specifically anticipates claims to single-instrument WTA spatial transcriptomics by sequential hybridization (vs SBS-based Xenium or sequencing-by-ligation Visium HD).

## Vizgen MERSCOPE Ultra (2024-04)

- **id**: `vizgen-merscope-ultra`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Vizgen Inc.
- **disclosure**: Vizgen press release 2024-04-15 'MERSCOPE Ultra'; AGBT 2024 abstract; product datasheet SD-0009 rev B
- **ip status**: patented
- **prior art notes**: Extends MERSCOPE platform with larger flowcell footprint and improved encoding chemistry that reduces total fluidic cycles. Anticipates: scaling of MERFISH-based spatial transcriptomics to >0.5 cm^2 tissue per slide using on-instrument microfluidic delivery, and reduced-round encoding schemes compatible with the same imaging hardware. Anticipates claims to high-throughput in-situ-hybridization platforms that combine optical multiplexing with progressively longer panel sizes through chemistry rather than instrument changes.

## Vizgen MERFISH 2 Encoding Chemistry (2024-04)

- **id**: `vizgen-merfish-2-chemistry`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Vizgen Inc.
- **disclosure**: Vizgen MERSCOPE Ultra technical note 2024; updated assay protocol AP-0042 rev 1
- **ip status**: patented
- **prior art notes**: Discloses an updated MERFISH encoding scheme that allocates more bits per imaging cycle (multi-color combinatorial decoding) and uses higher-affinity LNA-modified readout probes for shorter hybridization. Anticipates: chemistry-only improvements to in-situ hybridization throughput on existing microfluidic delivery hardware; increased information-per-cycle scaling that defers the need for new fluidic platforms. Useful as 102 art against claims that tie panel-scaling improvements to specific microfluidic instrument architectures.

## 10x Genomics Xenium Prime 5K (2024-10)

- **id**: `10x-xenium-prime-5k`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: 10x Genomics Inc.
- **disclosure**: 10x Genomics Xenium Prime launch 2024-10-23; Xenium Prime user guide CG000760
- **ip status**: patented
- **prior art notes**: Discloses scaling of in-situ sequencing-by-ligation spatial transcriptomics to ~5000-gene panels through extended encoding (more bits per cycle, more cycles) on the unchanged Xenium Analyzer microfluidic platform. Anticipates: panel-scaling-by-chemistry on rolling-circle-amplification ISS platforms; combinatorial barcoding schemes spanning ~5000 targets within practical optical-cycle counts; integration of optional add-on probe panels delivered through the same microfluidic cartridge. Useful as prior art against claims that conflate panel size with hardware redesign.

## Element Biosciences AVITI Cloudbreak (Long-Read) (2024-10)

- **id**: `element-biosciences-aviti-cloudbreak`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Element Biosciences Inc.
- **disclosure**: Element Biosciences press release 2024-10-22; AGBT 2024 'Cloudbreak' presentation; product datasheet EL-DOC-00185
- **ip status**: patented
- **prior art notes**: Discloses chemistry to extend the effective read length of polony sequencing by maintaining physical clustering of related fragments on the same surface region (linked-read approach), then assembling locally during base-calling. Anticipates: long-read sequencing achieved through surface-chemistry-based linkage rather than dedicated long-read instrumentation; reuse of short-read flowcell hardware for >200 bp contiguous reads via spatial linkage. Anticipates claims to long-read methods that depend on surface arrangement and sliding-window assembly within a single SBS flowcell.
