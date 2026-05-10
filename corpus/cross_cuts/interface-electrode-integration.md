---
title: interface-electrode-integration
parent: Cross-cuts
layout: default
---

# Cross-cut: `interface-electrode-integration`

**8 corpus entries disclose this subsystem.**

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

## Roche Elecsys Electrochemiluminescence Reagent Cassette (1996)

- **id**: `roche-elecsys-ecl-reagent-cassette`
- **corpus**: private
- **device class**: consumable-bulk
- **creator**: Roche Diagnostics (formerly Boehringer Mannheim) / IGEN International (ECL chemistry)
- **disclosure**: Roche/Boehringer Mannheim Elecsys 2010 immunoassay analyzer launch 1996; J. Clin. Lab. Anal. 1998 evaluation; US patents 5,238,808 and 5,310,687 (Boehringer Mannheim ECL cell)
- **ip status**: patented
- **prior art notes**: Discloses a unified reagent cassette format for ECL immunoassay: barcoded multi-vial cassette with streptavidin-paramagnetic-bead phase + biotinylated capture antibody + ruthenium-labeled detection antibody; the analyzer pipettor draws metered volumes from each vial into a disposable measuring cell, incubates with sample, magnetically captures the bead-immune-complex at a platinum working electrode, washes with TPA buffer, and applies an oxidation pulse exciting Ru(bpy)3 ECL emission detected at 620 nm by a PMT. The cassette form factor and ECL chemistry constitute foundational disclosure for: barcoded ratiometric reagent cassettes with on-board lot tracking; ECL-on-electrode with magnetic-bead capture as a sensitivity-amplification fluidic primitive. Element-by-element coverage applicable to all Roche Cobas e-series analyzers (e411, e601, e801, e402, Cobas pro).

## MicroCHIPS / Microchips Biotech Implantable Drug Reservoir Array (1999-01-28)

- **id**: `microchips-biotech-implantable-reservoir`
- **corpus**: private
- **device class**: valve-component
- **creator**: Microchips Biotech Inc. (Langer / Cima MIT spin-out)
- **disclosure**: Santini JT, Cima MJ, Langer R Nature 397:335-338 1999 doi:10.1038/16898; first-in-human Farra R et al. Sci Transl Med 4(122):122ra21 2012 doi:10.1126/scitranslmed.3003276
- **ip status**: patented
- **prior art notes**: Foundational disclosure of an implantable drug-reservoir microchip: silicon substrate with micromachined wells (each holding sub-microliter to nanoliter dose), each well capped by a thin gold membrane that serves both as a hermetic seal and as an anodic electrode. Application of a small potential in chloride-containing biological fluid electrochemically dissolves the chosen membrane, releasing reservoir contents. Anticipates: addressable on-demand microreservoir drug delivery in implantable form; electrochemical-membrane-as-valve architecture; silicon-DRIE fabrication of multi-well drug-storage arrays.

## Cassini Cosmic Dust Analyzer (CDA) — Enceladus Plume Mass Spectra (2004)

- **id**: `cassini-cda-cosmic-dust-analyzer`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Max Planck Institute for Nuclear Physics (MPI-K Heidelberg) / NASA / ESA Cassini-Huygens
- **disclosure**: Srama R et al., 'The Cassini Cosmic Dust Analyzer,' Space Science Reviews 114:465-518 (2004), doi:10.1007/s11214-004-1435-z; Postberg F et al., 'Macromolecular organic compounds from the depths of Enceladus,' Nature 558:564-568 (2018), doi:10.1038/s41586-018-0246-4
- **ip status**: public-domain
- **prior art notes**: Founding flight precedent for in-situ icy-moon plume composition analysis. Element-by-element prior art for: (a) hypervelocity impact + plasma plume + ToF-MS for compositional analysis of micron-scale ice grains in flyby geometry; (b) the dual-mode operation (charge-pulse for particle counting + mass spectrum for composition) on a single sensing area; (c) the post-mission discovery that Enceladus plume material contains complex organics and salts is itself open prior art that any future Enceladus mission cartridge claiming biosignature detection will need to overcome. CDA is the citation grandparent for all icy-moon life-detection cartridges.

## Nova StatStrip Glucose/Ketone Hospital Test Strip (2006)

- **id**: `nova-statstrip-glucose-strip`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Nova Biomedical
- **disclosure**: Nova Biomedical StatStrip Glucose 510(k) K061893 cleared 2006-12; first FDA-cleared glucose strip for critically ill patients (2014 K140509)
- **ip status**: patented
- **prior art notes**: Discloses a multi-electrode glucose test strip with on-strip interferent correction electrodes: in addition to the main GDH-mediator amperometric working electrode, additional working electrodes detect Hct (impedance), oxidizable interferents (acetaminophen, urate, ascorbate, dopamine), and reducing sugars (maltose, galactose, xylose), with the meter algorithm subtracting interferent contribution from glucose readout. Anticipates: multi-channel POC glucose strips with on-strip interferent correction; Hct compensation electrodes integrated into the same capillary chamber; FDA-clearable strip-based POC glucose for critically ill (where interfering substances and abnormal Hct break older single-electrode strips). Foundational to the Nova approach extending to lactate, ketone, and creatinine strips.

## ISS Biomolecule Sequencer (Oxford Nanopore MinION on ISS) (2016)

- **id**: `iss-biomolecule-sequencer-minion`
- **corpus**: open
- **device class**: nanofluidic-chip
- **creator**: NASA Johnson Space Center / Oxford Nanopore Technologies / Houston Methodist
- **disclosure**: Castro-Wallace SL et al., 'Nanopore DNA Sequencing and Genome Assembly on the International Space Station,' Scientific Reports 7:18022 (2017), doi:10.1038/s41598-017-18364-0; NASA ISS Biomolecule Sequencer mission press kit, August 2016
- **ip status**: patented
- **prior art notes**: While the underlying MinION is already covered as 'oxford-nanopore-minion' in the corpus, the spaceflight variant is independent prior art for: (a) the qualification of biological-membrane nanopore arrays for the orbital radiation environment without measurable loss of yield (vs. ground controls), which anticipates patents claiming radiation-hardened or space-qualified single-molecule sequencing cartridges; (b) the ground-to-orbit cold-chain protocol for shipping pre-loaded R9 flow cells (cold pack stability, ambient ISS temperature operation), which anticipates patents on planetary or deep-sea biosensor logistics; (c) the integration of MinION sequencing with WetLab-2 sample prep on station — together these establish the first sample-to-sequence loop performed beyond Earth, and anticipate any patent claim to an integrated 'in-situ sequencing cartridge' for planetary life detection that uses pore-based single-molecule readout. Cross-cite to oxford-nanopore-minion for the underlying device.

## Temperature-controlled chip holder with integrated electrodes for NSS (2026-01-19)

- **id**: `altenburger-2026-temperature-controlled-chip-holder`
- **corpus**: academic
- **device class**: chip-holder
- **creator**: Langhammer group, Chalmers
- **disclosure**: Altenburger, B.; Fritzsche, J.; Langhammer, C. A temperature-controlled chip holder with integrated electrodes for nanofluidic scattering spectroscopy on highly integrated nanofluidic systems. Microsyst. Nanoeng. 2026, 12, 32. DOI: 10.1038/s41378-025-01125-9
- **ip status**: public-domain
- **prior art notes**: Discloses a multifunctional fluidic chip holder integrating: 12 Luer-Lock fluidic ports with O-ring sealing against a 1 cm² Si/SiO2 chip, four series-wired Peltier elements thermally bridged to the chip via an aluminum heat bridge with passive air-gap insulation, electrodes inserted through Luer-T couplings for application of electric fields across the same connection points used for fluid, and an optically transparent acrylic channel plate. Operating range 12 °C to 112 °C with characterized hysteresis curves. Anticipates: combined fluid/electrode insertion through a single Luer-T port, off-chip Peltier-on-frame architecture instead of on-chip resistive heating, and the architectural pattern of treating the holder as the multi-modal periphery of a small chip.
