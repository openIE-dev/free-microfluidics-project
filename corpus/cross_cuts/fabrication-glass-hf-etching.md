---
title: fabrication-glass-hf-etching
parent: Cross-cuts
layout: default
---

# Cross-cut: `fabrication-glass-hf-etching`

**19 corpus entries disclose this subsystem.**

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

## Pinched injection on glass CE microchips (1994)

- **id**: `jacobson-1994-pinched-injection`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: J. M. Ramsey group, Oak Ridge National Lab
- **disclosure**: Jacobson, S. C.; Hergenroder, R.; Koutny, L. B.; Warmack, R. J.; Ramsey, J. M. Effects of injection schemes and column geometry on the performance of microchip electrophoresis devices. Anal. Chem. 1994, 66, 1107–1113. DOI: 10.1021/ac00079a028
- **ip status**: public-domain
- **prior art notes**: Disclosed pinched-injection geometry for chip CE: a four-port crossed-channel layout with simultaneously pulled sample-and-buffer arms generates a precisely defined sub-nanoliter sample plug. Anticipates: pinched-injection cross geometry as the standard chip-CE injection primitive, used in essentially every subsequent commercial CE chip. Among Ramsey's most-cited microfluidics papers.

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

## Ramsey integrated chip-MS extensions (post-1996) (2000)

- **id**: `ramsey-2000-integrated-chip-ms`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: J. M. Ramsey group, Oak Ridge / UNC Chapel Hill
- **disclosure**: Ramsey, J. M. The burgeoning power of the shrinking laboratory. Nat. Biotechnol. 1999, 17, 1061–1062. (And subsequent Ramsey group papers extending chip-ESI architecture.)
- **ip status**: patented
- **prior art notes**: Post-1996 extensions of the Ramsey chip-ESI architecture: integrated trypsin digestion, on-chip protein-LC, and 2D separations preceding ESI. Cited as the methodological lineage for integrated chip-LC-MS workflows. Cumulative Ramsey-group disclosures define the trajectory from chip-ESI (1996) to commercial chip-LC-MS (Agilent 2005).

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

## uFluidix microfluidic chip fabrication services (2014)

- **id**: `ufluidix-foundry-services`
- **corpus**: open
- **device class**: other
- **creator**: uFluidix Inc.
- **disclosure**: uFluidix microfluidic foundry services. https://www.ufluidix.com
- **ip status**: open-permissive
- **prior art notes**: Commercial microfluidic chip foundry serving the academic research community: PDMS, glass, and thermoplastic chip fabrication services at academic-budget pricing. While uFluidix itself is commercial, the broader 'foundry services for academic microfluidics' ecosystem (including Microfluidic ChipShop, Dolomite, Black Hole Lab) plays a critical role in lowering the barrier for academic groups without in-house fabrication capability.
