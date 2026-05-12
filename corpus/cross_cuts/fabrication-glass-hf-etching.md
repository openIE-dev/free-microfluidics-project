---
title: fabrication-glass-hf-etching
parent: Cross-cuts
layout: default
---

# Cross-cut: `fabrication-glass-hf-etching`

**30 corpus entries disclose this subsystem.**

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

## Reservoir-on-chip etched-glass micromodel for enhanced oil recovery and pore-scale flow (1983-08-01)

- **id**: `reservoir-on-chip-etched-glass-micromodel`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: academic and oil-industry research (Lenormand at IFP/CNRS; Mattax & Kyte at Humble Oil; later Stanford, Univ. of Texas, Imperial College, Shell/Total/BP/ExxonMobil micromodel labs; commercialized via Micronit, Dolomite, Stratum Reservoir)
- **disclosure**: Lenormand, Touboul & Zarcone, Numerical models and experiments on immiscible displacements in porous media, J. Fluid Mech. 189, 165 (1988); earlier etched-glass micromodel work by Mattax & Kyte (1961) Ever see a waterflood?, Oil & Gas J., and Lenormand et al. (1983); modern lab-on-chip micromodels reviewed in Lifton, Microfluidics: an enabling screening technology for enhanced oil recovery, Lab Chip 16, 1777 (2016).
- **ip status**: open-permissive
- **prior art notes**: Discloses an etched two-dimensional pore-throat network chip with controllable geometry and wettability for visualizing pore-scale multiphase displacement and screening EOR fluids. Anticipates claims to (a) etched-glass/silicon micromodel reproducing reservoir-rock pore topology for multiphase-flow imaging; (b) microfluidic screening of enhanced-oil-recovery chemical formulations by direct observation of incremental recovery; (c) wettability-patterned pore-network chip for capillary-trapping studies; (d) micromodel-based validation of pore-network/DNS reservoir-flow simulations. Foundational and prior-art-rich; limits later patents claiming generic reservoir-on-chip devices.

## Manz / Ciba-Geigy original µTAS patent (1990 priority) (1990)

- **id**: `manz-1992-ciba-geigy-mu-tas-patent-original`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Andreas Manz, Hans-Michael Widmer (Ciba-Geigy AG, Basel)
- **disclosure**: Manz, A. et al. EP0497077A1 / WO9217767A1: Process for separating substances by capillary electrophoresis on chip. Priority date 1991, filed 1992 by Ciba-Geigy AG.
- **ip status**: patented
- **prior art notes**: The seminal Ciba-Geigy patent estate filed by Manz and Widmer covering chip-format capillary electrophoresis with electroosmotic pumping. The 1990 priority date predates the Manz 1990 academic paper publication, making this patent family the dominant foundational IP for chip CE. Ciba-Geigy (later Novartis) held this patent estate through expiry in 2010-2012, generating significant licensing revenue from chip-CE-based instruments. Doctrinally critical: any patent asserting novelty for chip-format electrokinetic separation must address this prior art chain.

## OLS Bio CASY Cell Counter and Analyzer (formerly Innovatis CASY-TT) (1991)

- **id**: `ols-bio-casy-tt-cell-counter`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: OLS Bio (formerly Innovatis AG; Roche Diagnostics divestiture)
- **disclosure**: Innovatis (Bielefeld, Germany) CASY launch 1991; CASY-TT (TwinTechnology) launch 2006; Innovatis acquired by Roche 2008; CASY product line now sold by OLS-Bio (since 2013); Pulsar Coulter-principle patent extension
- **ip status**: patented
- **prior art notes**: Discloses the CASY Pulse Area Analysis variant of Coulter-principle particle counting: instead of peak-amplitude pulse detection (which conflates fast-transit small particles with slow-transit large particles), the CASY integrates each impedance pulse over time, yielding a true volume measurement; importantly, intact cell membranes block the electrolyte from penetrating the cell interior, so live cells appear to have their full hydrodynamic volume, while dead cells with permeabilized membranes appear shrunken to nuclear volume — providing label-free live/dead discrimination. Anticipates: stain-free viability discrimination via electrical sensing zone integration; the architectural choice of Pulse Area Analysis vs amplitude detection in Coulter-derivative instruments; the use of multiple aperture sizes (50, 60, 150 µm) in a single instrument enabling 0.7-200 µm dynamic range in one measurement. Important historical anchor for the bioprocess cell counting market dominated by image cytometry (Vi-CELL) and impedance (CASY) before flow cytometry routine.

## Capillary electrophoresis on a microchip (1992)

- **id**: `harrison-1992-cap-electrophoresis-on-chip`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: D. Jed Harrison, Andreas Manz et al.
- **disclosure**: Harrison, D. J.; Manz, A.; Fan, Z.; Lüdi, H.; Widmer, H. M. Capillary electrophoresis and sample injection systems integrated on a planar glass chip. Anal. Chem. 1992, 64, 1926–1932. DOI: 10.1021/ac00041a030
- **ip status**: public-domain
- **prior art notes**: First demonstration of capillary electrophoresis with sample injection integrated on a planar glass chip. Anticipates: integrated electrokinetic separation, T-injector geometry for plug formation, glass-glass thermal bonding for chip sealing, and on-chip electrochemical or fluorescence detection coupled to electrophoretic separation. Patent claims asserting novelty over CE-on-chip as a category run into this disclosure.

## High-speed separation of antisense oligonucleotides on a micromachined capillary electrophoresis device (1993)

- **id**: `effenhauser-1993-glass-microchip-electrophoresis`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Manz group, Ciba-Geigy / Hewlett-Packard
- **disclosure**: Effenhauser, C. S.; Manz, A.; Widmer, H. M. Glass chips used as micro-reactors for chemical synthesis and electrophoresis. Anal. Chem. 1993, 65, 2637–2642. DOI: 10.1021/ac00067a015
- **ip status**: public-domain
- **prior art notes**: Demonstrated practical high-speed separation of oligonucleotides on a glass micromachined CE chip. With Harrison 1992 establishes glass chip CE as a working analytical technique rather than a curiosity. Anticipates: glass-CE as the workhorse architecture for the first commercial chip electrophoresis systems (Agilent 2100 Bioanalyzer, Caliper LabChip).

## Electroosmotic injection / pumping on chip CE (1993)

- **id**: `harrison-1993-electroosmotic-cycling`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Harrison group, Alberta
- **disclosure**: Harrison, D. J.; Fluri, K.; Seiler, K.; Fan, Z.; Effenhauser, C. S.; Manz, A. Micromachining a miniaturized capillary electrophoresis-based chemical analysis system on a chip. Science 1993, 261, 895–897. DOI: 10.1126/science.261.5123.895
- **ip status**: public-domain
- **prior art notes**: Companion to Harrison 1992 / Manz 1990 establishing electroosmotic pumping on glass CE chips. Demonstrated reproducible voltage-controlled fluid handling on-chip without mechanical pumps — pure electrokinetic transport with sub-nanoliter sample plug definition. Anticipates: voltage-as-pump for chip CE, programmable electrokinetic flow control, and the electroosmotic pumping paradigm that became the de facto fluid-handling method for chip CE before pressure-driven systems took over.

## Micromachining a miniaturized capillary electrophoresis-based chemical analysis system on a chip (Harrison, Fluri, Seiler, Fan, Effenhauser, Manz, 1993) (1993-08-13)

- **id**: `harrison-1993-science-mu-tas-chip`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: D. Jed Harrison (Alberta), Andreas Manz (Ciba-Geigy), and coworkers
- **disclosure**: Harrison, D. J.; Fluri, K.; Seiler, K.; Fan, Z.; Effenhauser, C. S.; Manz, A. Micromachining a miniaturized capillary electrophoresis-based chemical analysis system on a chip. Science 1993, 261 (5123), 895-897. DOI: 10.1126/science.261.5123.895.
- **ip status**: public-domain
- **prior art notes**: The landmark demonstration of an integrated capillary-electrophoresis chemical-analysis microchip - electrokinetically controlled sample handling, on-chip injection at a channel intersection, electrophoretic separation in HF-etched glass channels, and laser-induced-fluorescence detection - establishing the planar-glass uTAS platform that dominated the next decade. Discloses: a cross/double-T channel network with multiple reservoirs; voltage-program-controlled electrokinetic sample injection, separation, and dilution entirely by switching electrode potentials with no moving parts; sub-nL defined injection volumes; and integrated optical detection. Anticipates claims to: electrokinetically valved sample injection at channel intersections; multi-reservoir voltage-programmed CE microchips; HF-etched glass CE channel networks; and integrated LIF detection on a CE chip. Distinct companion to existing harrison-1992-cap-electrophoresis-on-chip and harrison-1993-electroosmotic-cycling entries; cross-referenced. Ancestor of jacobson-1994-pinched-injection, effenhauser-1993-glass-microchip-electrophoresis, mathies-1995-radial-cap-array, and burns-1998-integrated-dna-analysis-device.

## Pinched injection on glass CE microchips (1994)

- **id**: `jacobson-1994-pinched-injection`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: J. M. Ramsey group, Oak Ridge National Lab
- **disclosure**: Jacobson, S. C.; Hergenroder, R.; Koutny, L. B.; Warmack, R. J.; Ramsey, J. M. Effects of injection schemes and column geometry on the performance of microchip electrophoresis devices. Anal. Chem. 1994, 66, 1107–1113. DOI: 10.1021/ac00079a028
- **ip status**: public-domain
- **prior art notes**: Disclosed pinched-injection geometry for chip CE: a four-port crossed-channel layout with simultaneously pulled sample-and-buffer arms generates a precisely defined sub-nanoliter sample plug. Anticipates: pinched-injection cross geometry as the standard chip-CE injection primitive, used in essentially every subsequent commercial CE chip. Among Ramsey's most-cited microfluidics papers.

## Ultra-high-speed DNA fragment separations using microfabricated capillary array electrophoresis chips (Woolley & Mathies, 1994) (1994-11-22)

- **id**: `woolley-mathies-1994-microfabricated-capillary-array-electrophoresis`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Adam T. Woolley & Richard A. Mathies, UC Berkeley
- **disclosure**: Woolley, A. T.; Mathies, R. A. Ultra-high-speed DNA fragment separations using microfabricated capillary array electrophoresis chips. Proc. Natl. Acad. Sci. U.S.A. 1994, 91 (24), 11348-11352. DOI: 10.1073/pnas.91.24.11348.
- **ip status**: public-domain
- **prior art notes**: Demonstrated DNA-fragment electrophoretic separations on a glass microchip with a sieving polymer matrix achieving separations in seconds-to-minutes, and laid the groundwork for microfabricated capillary-array electrophoresis (CAE) for high-throughput DNA sizing and sequencing. Discloses: HF-etched glass channels filled with replaceable polymer sieving matrices for size separation of dsDNA; high-field ultra-fast electrophoresis enabled by efficient Joule-heat dissipation in shallow channels; on-chip LIF detection; and the scaling toward parallel channel arrays read by a scanning confocal detector. Anticipates claims to: polymer-sieving DNA separations in microchannels; high-field rapid microchip electrophoresis; capillary-array electrophoresis on a single substrate; and confocal-scanner readout of parallel separation channels. Distinct companion to existing mathies-1995-radial-cap-array; cross-referenced. Ancestor of microchip DNA-sequencing and high-throughput-genotyping platforms.

## Radial capillary-array electrophoresis chip (1995)

- **id**: `mathies-1995-radial-cap-array`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: R. A. Mathies group, UC Berkeley
- **disclosure**: Woolley, A. T.; Mathies, R. A. Ultra-high-speed DNA sequencing using capillary electrophoresis chips. Anal. Chem. 1995, 67, 3676–3680. DOI: 10.1021/ac00116a010
- **ip status**: patented
- **prior art notes**: Demonstrated 96-channel radial CE array on a single 100-mm glass wafer for parallel DNA sequencing reads. Anticipates: radial-channel-array architecture for parallel CE, glass-chip-as-replacement-for-slab-gel for sequencing, and the Caliper LabChip / Agilent Bioanalyzer commercial platforms. Established the wafer-scale parallelism paradigm in chip CE.

## Electrospray ionization from a microchip CE column (1996)

- **id**: `ramsey-1996-electrospray-on-chip`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: J. M. Ramsey group, Oak Ridge National Lab
- **disclosure**: Ramsey, R. S.; Ramsey, J. M. Generating electrospray from microchip devices using electroosmotic pumping. Anal. Chem. 1997, 69, 1174–1178. DOI: 10.1021/ac961013o
- **ip status**: patented
- **prior art notes**: First demonstration of electrospray ionization directly from a glass microchip channel, enabling chip-based CE-MS. Anticipates: chip-to-MS interface architecture, electroosmotic-pumped ESI without external pump, and the entire chip-MS coupling field commercialized by Advion (Triversa NanoMate) and integrated into Agilent and Waters chip-LC products.

## Caliper LabChip / ACLA chip technology (acquired by Ciba-Geigy lineage) (1996)

- **id**: `caliper-acla-chip-1999`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Caliper Technologies → Caliper Life Sciences → PerkinElmer
- **disclosure**: Caliper Life Sciences (formerly Caliper Technologies) LabChip platform; acquired by PerkinElmer 2011. https://www.perkinelmer.com
- **ip status**: patented
- **prior art notes**: Foundational commercial implementation of glass chip CE for protein and nucleic acid separation. The Caliper LabChip platform was the dominant academic-research chip CE platform 2000-2010 before being eclipsed by capillary instruments. Caliper held a substantial patent estate covering chip-format separations, integrated multi-channel architectures, and droplet manipulation. Acquired by PerkinElmer 2011; underlies many commercial DNA / RNA / protein gel-equivalent chip products.

## Drew Scientific HemaVet 950 / 1500 Veterinary Hematology Analyzer (1996)

- **id**: `drew-scientific-hemavet-veterinary-cbc`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Drew Scientific (Erba Diagnostics)
- **disclosure**: Drew Scientific HemaVet 850/950 launch ~1996; HemaVet 1500 launch 2003; pivotal multi-species reference distribution publications by Provost, Vet Clin Pathol
- **ip status**: patented
- **prior art notes**: Discloses an impedance-only multi-species veterinary hematology analyzer optimized for low-volume rodent samples (20 µL): single Coulter-principle aperture with species-specific lysing reagents; differential by impedance-histogram peak deconvolution applying species-specific RBC/WBC/PLT volume distribution priors. Anticipates: low-cost impedance-only veterinary hematology suitable for academic/preclinical pharmacology where cost and rodent-sample volume dominate over diff-channel diversity. Distinct from IDEXX ProCyte Dx (impedance + flow cytometry, higher cost, in-clinic) and from Heska Element HT5 (image cytometry). Important architectural anchor for the segment of veterinary/preclinical hematology that doesn't need fluorescence cytometry.

## Continuous-flow PCR on chip (Kopp 1998) (1998)

- **id**: `quake-1997-pcr-on-chip`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Manz group, Imperial College
- **disclosure**: Kopp, M. U.; de Mello, A. J.; Manz, A. Chemical amplification: continuous-flow PCR on a chip. Science 1998, 280, 1046–1048. DOI: 10.1126/science.280.5366.1046
- **ip status**: patented
- **prior art notes**: Disclosed continuous-flow PCR on chip: serpentine glass channel passes through three temperature zones (denature/anneal/extend), with the number of cycles equal to the number of channel passes through each zone. Anticipates: spatial-temperature-zone PCR architecture as alternative to time-domain thermal cycling, and the entire continuous-flow PCR subfield. Architectural ancestor of many subsequent flow-PCR designs.

## Chemical amplification: continuous-flow PCR on a chip (Kopp, de Mello & Manz, 1998) (1998-05-15)

- **id**: `kopp-1998-continuous-flow-pcr-on-chip`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Martin U. Kopp, Andrew J. de Mello, Andreas Manz, Imperial College London
- **disclosure**: Kopp, M. U.; de Mello, A. J.; Manz, A. Chemical amplification: continuous-flow PCR on a chip. Science 1998, 280 (5366), 1046-1048. DOI: 10.1126/science.280.5366.1046.
- **ip status**: public-domain
- **prior art notes**: Introduced continuous-flow (flow-through) PCR: instead of cycling the temperature of a static chamber, the reaction mixture is pumped through a serpentine microchannel that repeatedly traverses three zones held at fixed denaturation, annealing, and extension temperatures, so the time-domain thermal protocol becomes a spatial one - removing thermal-ramp limits and enabling very fast amplification. Discloses: spatially-multiplexed isothermal-zone architecture for thermal cycling; cycle number set by channel geometry (number of passes); cycle time set by flow rate and zone-segment lengths; and the elimination of bulk-heater thermal mass as the rate limit. Anticipates claims to: continuous-flow / flow-through nucleic-acid amplification microdevices; fixed-temperature-zone serpentine PCR chips; flow-rate-controlled cycling kinetics; and spatial-domain implementations of any cyclic thermal protocol. Companion to wilding-shoffner-kricka-1994-pcr-in-silicon-microstructures and northrup-1993-silicon-pcr-microreactor (static-chamber predecessors); ancestor of droplet-PCR and microfluidic digital-PCR throughput architectures.

## Ramsey integrated chip-MS extensions (post-1996) (2000)

- **id**: `ramsey-2000-integrated-chip-ms`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: J. M. Ramsey group, Oak Ridge / UNC Chapel Hill
- **disclosure**: Ramsey, J. M. The burgeoning power of the shrinking laboratory. Nat. Biotechnol. 1999, 17, 1061–1062. (And subsequent Ramsey group papers extending chip-ESI architecture.)
- **ip status**: patented
- **prior art notes**: Post-1996 extensions of the Ramsey chip-ESI architecture: integrated trypsin digestion, on-chip protein-LC, and 2D separations preceding ESI. Cited as the methodological lineage for integrated chip-LC-MS workflows. Cumulative Ramsey-group disclosures define the trajectory from chip-ESI (1996) to commercial chip-LC-MS (Agilent 2005).

## Khandurina 2000 integrated system for rapid PCR-based DNA analysis in microfluidic devices (2000-06-09)

- **id**: `khandurina-2000-integrated-pcr-ce-microfluidic`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: J. Michael Ramsey group, Oak Ridge National Laboratory
- **disclosure**: Khandurina, J.; McKnight, T. E.; Jacobson, S. C.; Waters, L. C.; Foote, R. S.; Ramsey, J. M. Integrated system for rapid PCR-based DNA analysis in microfluidic devices. Anal. Chem. 2000, 72, 2995-3000. DOI: 10.1021/ac991471a
- **ip status**: public-domain
- **prior art notes**: A canonical integrated-PCR-CE-on-glass paper from the Ramsey lab (the Oak Ridge / later UNC microchip-CE foundry). Discloses a monolithic glass microchip integrating a sub-microliter PCR chamber with an on-chip capillary electrophoresis separation channel, isolated during thermal cycling by a hydrogel/porous-membrane valve, with electrokinetic transfer of the amplification product into the separation channel and laser-induced-fluorescence sizing - the whole assay in ~20 minutes. Anticipates claims to: integration of a thermal-cycled amplification chamber and an electrophoretic separation channel on a single etched-glass substrate; gel/membrane valves that block bulk flow but pass ions/small molecules to decouple a reaction chamber from a downstream channel; and electrokinetic injection of PCR product directly from an on-chip reactor into an on-chip separation column. Foundational for the integrated-genetic-analysis-microchip lineage (Lagally 2001, Mathies MOA, commercial sample-to-answer chips).

## Lagally 2001 single-molecule DNA amplification and analysis in an integrated microfluidic device (2001-01-04)

- **id**: `lagally-2001-single-molecule-pcr-microfluidic`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Richard A. Mathies group, UC Berkeley
- **disclosure**: Lagally, E. T.; Medintz, I.; Mathies, R. A. Single-molecule DNA amplification and analysis in an integrated microfluidic device. Anal. Chem. 2001, 73, 565-570. DOI: 10.1021/ac001026b
- **ip status**: public-domain
- **prior art notes**: A milestone integrated-microfluidics paper: single-molecule (single-template) PCR amplification in a nanoliter on-chip reactor with integrated thin-film heater and resistance-temperature-detector, monolithically coupled to an on-chip capillary electrophoresis column for product analysis - the conceptual ancestor of digital PCR done in a microfabricated device. Anticipates claims to: amplification from a statistically single DNA molecule loaded by limiting dilution into a nanoliter chamber; integrated resistive heating + RTD temperature feedback in a glass PCR microchip; and monolithic integration of single-molecule amplification with electrophoretic readout. Cited as a foundational reference for integrated genetic analysis microsystems and for chip-format digital PCR.

## Dielectrophoresis-based separation of human cancer cells from blood (2002)

- **id**: `gascoyne-2002-dep-cancer-cells`
- **corpus**: academic
- **device class**: separator-component
- **creator**: Gascoyne group, MD Anderson
- **disclosure**: Gascoyne, P. R. C.; Vykoukal, J. Particle separation by dielectrophoresis. Electrophoresis 2002, 23, 1973–1983. DOI: 10.1002/1522-2683(200207)23:13<1973::AID-ELPS1973>3.0.CO;2-1
- **ip status**: patented
- **prior art notes**: Established practical DEP-FFF (dielectrophoretic field-flow fractionation) for cell separation, particularly CTC enrichment from blood. Demonstrates positive-DEP capture of cancer cells against negative-DEP blood cells using castellated electrode arrays. Anticipates: castellated-electrode-array DEP architecture, DEP-FFF as a continuous-flow separation method, and the commercial DEPArray and ApoCell platforms.

## Little Things Factory glass microreactor (LTF-MS, LTF-V) (2005)

- **id**: `little-things-factory-mikroreaktor`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Little Things Factory GmbH
- **disclosure**: Little Things Factory GmbH (Ilmenau, DE) product brochure 2005; Hessel, V.; Hardt, S.; Löwe, H. Chemical Micro Process Engineering: Fundamentals, Modelling and Reactions, Wiley-VCH, 2004 (cites LTF); LTF product catalog rev 2018; product page https://www.ltf-gmbh.com
- **ip status**: patented
- **prior art notes**: Discloses an off-the-shelf catalog of standardized borosilicate-glass microreactor chips (T-mixer, V-mixer, HEX with integrated heat exchanger, residence-time meanders) in two standard footprints — a 'commodity glass chip' supplier providing the substrates that other vendors (Future Chemistry, Chemtrix Labtrix, Syrris) integrate into their platforms. Anticipates patent claims to standardized-footprint glass microreactor chip families and to integrated-heat-exchanger glass microreactor plates ('HEX' variants).

## Skelley 2005 microdevice for amino-acid biomarker detection and analysis on Mars (Mars Organic Analyzer) (2005-01-25)

- **id**: `skelley-2005-mars-organic-analyzer-microdevice`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Richard A. Mathies group, UC Berkeley (with NASA JPL, Scripps)
- **disclosure**: Skelley, A. M.; Scherer, J. R.; Aubrey, A. D.; Grover, W. H.; Ivester, R. H. C.; Ehrenfreund, P.; Grunthaner, F. J.; Bada, J. L.; Mathies, R. A. Development and evaluation of a microdevice for amino acid biomarker detection and analysis on Mars. Proc. Natl. Acad. Sci. U.S.A. 2005, 102, 1041-1046. DOI: 10.1073/pnas.0406798102
- **ip status**: public-domain
- **prior art notes**: Discloses the Mars Organic Analyzer: a portable glass-microchip capillary-electrophoresis instrument that automatically derivatizes (fluorescamine), dilutes, and chirally separates amino acids with laser-induced-fluorescence detection at parts-per-trillion sensitivity, using monolithic pneumatic microvalves/pumps for sample handling, validated in the Atacama Desert as a Mars analog. Anticipates claims to: portable microchip-CE instruments for in-situ extraterrestrial organic/biomarker analysis; on-chip fluorogenic derivatization coupled to electrophoretic chiral separation; integration of membrane-valve fluid handling with CE-LIF in a field/space-deployable package; and amino-acid enantiomeric-ratio measurement as a biosignature on a chip. Foundational for the Mathies-lab planetary-instrument lineage and the ExoMars MOMA microfluidics. Related to mathies-quinn-2017-microchip-ce-mars-amino-acids (later automation work).

## Janasek 2006 scaling and the design of miniaturized chemical-analysis systems (2006-07-27)

- **id**: `janasek-manz-2006-scaling-miniaturized-analysis-systems`
- **corpus**: academic
- **device class**: other
- **creator**: Andreas Manz group, ISAS Dortmund
- **disclosure**: Janasek, D.; Franzke, J.; Manz, A. Scaling and the design of miniaturized chemical-analysis systems. Nature 2006, 442, 374-380. DOI: 10.1038/nature05059
- **ip status**: public-domain
- **prior art notes**: The definitive scaling-laws treatment of miniaturized chemical analysis: it works through how separation resolution, mixing time, thermal transport, reaction kinetics and detection limits scale with channel dimensions, showing where miniaturization wins (faster diffusive mixing and equilibration, higher field strengths and efficiency in electrophoresis, lower thermal mass) and where it loses (mass-limited detection). As prior art it anticipates claims to: design methodologies that size microchannel features against target analytical performance via dimensional scaling; and the general principle that electrokinetic separation and diffusion-limited operations benefit from scale reduction. Companion to manz 1990 microTAS and stone-2004-engineering-flows-microfluidics. From the Manz group (ISAS Dortmund), originator of microTAS.

## deMello 2006 control and detection of chemical reactions in microfluidic systems (2006-07-27)

- **id**: `demello-2006-control-detection-chemical-reactions-microfluidic`
- **corpus**: academic
- **device class**: other
- **creator**: Andrew J. deMello group, Imperial College London
- **disclosure**: deMello, A. J. Control and detection of chemical reactions in microfluidic systems. Nature 2006, 442, 394-402. DOI: 10.1038/nature05062
- **ip status**: public-domain
- **prior art notes**: The Nature-insight review of doing and watching chemistry in microfluidic systems: rapid passive/active mixing, tight thermal control, segmented-flow and droplet microreactors, residence-time control by channel length and flow rate, and the full menu of on-chip and chip-hyphenated detection (fluorescence, absorbance, electrochemistry, electrospray-MS, microcoil-NMR). As a unified prior-art statement it anticipates claims to: microreactor architectures for kinetic control via mixing/thermal/residence-time engineering; segmented-flow reactors with downstream-position-encoded reaction time; and integration of microfluidic reactors with named detection modalities. Companion to song-ismagilov-2003-plug-based-reaction-networks and stone-2004-engineering-flows-microfluidics.

## Corning Advanced-Flow Reactor G1 (2007)

- **id**: `corning-advanced-flow-reactor-g1`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Corning Incorporated
- **disclosure**: Lavric, E. D.; Woehl, P. Advanced-Flow Glass Reactors for Seamless Scale-Up. Chimica Oggi - Chemistry Today 2009, 27 (3); Corning Inc. Advanced-Flow Reactors product brochure (Corning AFR G1, 2007); US patent 7,939,033 'Honeycomb microchannel reactor design'
- **ip status**: patented
- **prior art notes**: Discloses a borosilicate glass microreactor module composed of stacked etched plates with a 'heart-shaped' (HEART) mixing/heat-transfer geometry that produces repeated splitting and recombination of the reagent stream within sub-millimeter channels. Heat-transfer fluid flows in adjacent channels, enabling kW/L heat removal. Anticipates: (a) the heart/teardrop micro-mixer geometry as a manufacturable industrial micromixer with isothermal control of fast exotherms; (b) numbering-up by stacking thin glass plates rather than scale-up by enlarging channels; (c) continuous-flow production-grade reactor with all wetted parts borosilicate glass for chemical compatibility; (d) integration of heat-exchange and reaction in the same fluidic plate using counter-current cross-flow architecture. Should be cited against any later patent claiming heart/teardrop split-and-recombine mixers in stacked glass plates for continuous chemistry.

## Future Chemistry FlowStart Evo and FlowSyn (FutureChem BV) (2008)

- **id**: `future-chemistry-flowstart`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Future Chemistry BV (Nijmegen, NL)
- **disclosure**: Future Chemistry BV product launch FlowStart 2008; van der Linden, J. J. M.; Hilberink, P. W.; Kronenburg, C. M. P.; Kemperman, G. J. 'Investigation of the Moffatt-Swern oxidation in a continuous flow microreactor system' Org. Process Res. Dev. 2008, 12, 911–920; Future Chemistry datasheet rev 2010
- **ip status**: patented
- **prior art notes**: Discloses an educational/screening-grade glass microreactor platform with: (a) Peltier-cooled chip holder integrated with pump electronics to enable continuous flow at -40 °C (Swern oxidation, lithiation chemistry); (b) clamped borosilicate chip with sequential T-mixer geometry; (c) protocolized 'reaction starter kits' enabling teaching of flow chemistry by reproducing well-known wet-chemistry exemplars. Anticipates patent claims directed to integrated cryogenic chip holders for continuous-flow chemistry, and education-grade flow chemistry packages bundling chip, pump, holder, and protocol library.

## Chemtrix Labtrix S1 (2009)

- **id**: `chemtrix-labtrix-s1`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Chemtrix BV
- **disclosure**: Chemtrix BV product launch, Labtrix Start (2008) and Labtrix S1 (2009); Hessel, V.; Cortese, B.; de Croon, M. H. J. M. 'Novel process windows — concept, proposition and evaluation methodology, and intensified superheated processing' Chem. Eng. Sci. 2011, 66, 1426–1448; Chemtrix Labtrix S1 datasheet 2009
- **ip status**: patented
- **prior art notes**: Discloses a clamped silicon-glass and all-glass microreactor chip platform with: (a) screw-clamped O-ring fluidic interface allowing rapid swapping of reaction-chip designs without re-plumbing; (b) integrated heated stage controlling chip temperature ±0.1 °C; (c) standardized footprint enabling library of chip designs (T-mixer, split-recombine, residence-time loop) all interchangeable; (d) chip-and-clamp architecture amenable to small-volume reaction screening prior to numbering-up via Plantrix sister product. Anticipates patent claims directed to interchangeable microreactor chip stages with clamped fluidic seals and integrated thermal control.

## Du 2009 SlipChip (2009-06-25)

- **id**: `du-ismagilov-2009-slipchip`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Rustem F. Ismagilov group, University of Chicago
- **disclosure**: Du, W.; Li, L.; Nichols, K. P.; Ismagilov, R. F. SlipChip. Lab Chip 2009, 9, 2286-2292. DOI: 10.1039/b908978k
- **ip status**: public-domain
- **prior art notes**: Discloses the SlipChip: two plates bearing complementary patterns of wells and connecting ducts, separated by a lubricating fluid, where simple relative sliding re-routes which wells connect to which - thereby metering nanoliter aliquots, exposing reagents to one another, and initiating hundreds-to-thousands of reactions in parallel without any valves, pumps, or external control. Anticipates claims to: valveless/pumpless microfluidic metering and combinatorial fluid routing by relative translation of two patterned plates with an intervening immiscible lubricant; instrument-free multistep assay cartridges (PCR, immunoassay, crystallization screen) actuated by a slip motion; and digital nucleic-acid quantification by one-step partitioning of a sample into a well array. HIGH-PRIORITY anchor - the SlipChip underlies a family of instrument-light diagnostics and digital-assay products. Ismagilov plug/slip lineage (descends conceptually from song-ismagilov-2003-plug-based-reaction-networks).

## uFluidix microfluidic chip fabrication services (2014)

- **id**: `ufluidix-foundry-services`
- **corpus**: open
- **device class**: other
- **creator**: uFluidix Inc.
- **disclosure**: uFluidix microfluidic foundry services. https://www.ufluidix.com
- **ip status**: open-permissive
- **prior art notes**: Commercial microfluidic chip foundry serving the academic research community: PDMS, glass, and thermoplastic chip fabrication services at academic-budget pricing. While uFluidix itself is commercial, the broader 'foundry services for academic microfluidics' ecosystem (including Microfluidic ChipShop, Dolomite, Black Hole Lab) plays a critical role in lowering the barrier for academic groups without in-house fabrication capability.

## Stanford Microfluidics Foundry 2024 (2024)

- **id**: `stanford-microfluidics-foundry-2024`
- **corpus**: academic
- **device class**: printer-tooling
- **creator**: Stanford Microfluidics Foundry (Stanford SNF / Stanford BioE)
- **disclosure**: Stanford Microfluidics Foundry 2024 capability update on foundry.stanford.edu.
- **ip status**: open-permissive
- **prior art notes**: Discloses university-hosted microfluidics fab service offering SU-8 master, glass DRIE, and 2PP capabilities for academic researchers. Anticipates university-foundry-as-service microfluidic-fabrication ecosystem claims.
