---
title: valve-capillary-stop
parent: Cross-cuts
layout: default
---

# Cross-cut: `valve-capillary-stop`

**13 corpus entries disclose this subsystem.**

Earliest disclosure: 1805-12-20

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Young 1805 — An Essay on the Cohesion of Fluids (1805-12-20)

- **id**: `young-1805-cohesion-of-fluids`
- **corpus**: academic
- **device class**: other
- **creator**: Thomas Young
- **disclosure**: Young, T. (1805). 'An essay on the cohesion of fluids.' Philosophical Transactions of the Royal Society of London 95: 65-87. doi:10.1098/rstl.1805.0005
- **ip status**: public-domain
- **prior art notes**: Discloses the fundamental force balance at the three-phase (solid-liquid-vapor) contact line and defines the equilibrium contact angle in terms of the three interfacial tensions. This Young equation is the load-bearing relation for: (a) capillary-driven priming of microfluidic channels (paper microfluidics, lateral-flow assays, capillary stop valves); (b) all surface-treatment patents that claim a contact angle range to control wettability; (c) electrowetting devices (which modulate cos(theta) electrically — Lippmann's later equation reduces to a perturbation of Young); (d) hydrophilic/hydrophobic patterning to direct droplet motion. Anticipates any patent claim that recites 'controlling fluid motion by surface energy difference', 'directional flow by contact angle gradient', or 'stop valve formed by hydrophobic boundary' — Young 1805 published the underlying equation in the open literature 220 years prior. Particularly invalidates over-broad surface-energy-control claims that fail to disclose specific non-obvious geometries.

## Laplace 1806 — Mecanique Celeste Supplement on Capillary Action (1806)

- **id**: `laplace-1806-mecanique-celeste-capillarity`
- **corpus**: academic
- **device class**: other
- **creator**: Pierre-Simon Laplace
- **disclosure**: Laplace, P. S. (1806). 'Sur l'action capillaire,' Supplement to Book X of Traite de Mecanique Celeste, Vol. IV. Courcier, Paris. English: Bowditch translation, 1839, vol. IV.
- **ip status**: public-domain
- **prior art notes**: Discloses the Laplace pressure equation: the pressure difference across a curved fluid interface equals surface tension times mean curvature. Together with Young 1805 this forms the Young-Laplace equation, the universal governing relation for: (a) droplet pressure in T-junction and flow-focusing droplet generators; (b) bubble pinch-off and step emulsification; (c) capillary rise and capillary-driven priming in paper microfluidics; (d) Plateau-Rayleigh jet break-up; (e) the pressure threshold for breaking through a hydrophobic stop valve; (f) meniscus pinning at channel expansions and contractions; (g) the entire field of capillary stop valves on centrifugal microfluidic discs. Anticipates any claim that recites 'a pressure-balanced droplet generator', 'a capillary-pressure-driven valve', or 'a curved interface used to meter liquid' — Laplace 1806 published the governing equation 220 years before any microfluidic patent could have been filed.

## Young-Laplace Equation (combined 1805-1806) (1806)

- **id**: `young-laplace-equation-combined`
- **corpus**: academic
- **device class**: other
- **creator**: Thomas Young; Pierre-Simon Laplace
- **disclosure**: Young, T. Phil. Trans. R. Soc. 95, 65-87 (1805); Laplace, P. S. Mecanique Celeste, Supplement to Book X (1806). Combined as DeltaP = gamma(1/R1 + 1/R2) with boundary condition cos(theta) at three-phase line.
- **ip status**: public-domain
- **prior art notes**: Combined Young-Laplace equation is the single most invoked classical result in microfluidic device design: every droplet generator, every capillary-driven assay, every paper-microfluidic device, and every surface-energy patterned channel inherits its quantitative behavior from this equation. As a unified prior-art anchor, the combined equation invalidates broad patents claiming 'surface-tension-driven actuation', 'capillary-pressure metering', 'bursting-pressure valve', 'pressure-controlled droplet sizing', and similar — the relation between curvature, pressure, and surface tension was published before electricity was understood as an EM phenomenon.

## Bond / Eoetvoes Number Bo = rho g L^2 / gamma (1886)

- **id**: `bond-eotvos-number-dimensionless-group`
- **corpus**: academic
- **device class**: other
- **creator**: Lorand Eoetvoes (1886); Wilfrid Noel Bond (1928 dimensionless form)
- **disclosure**: Eoetvoes, R. (1886). 'Ueber den Zusammenhang der Oberflaechenspannung der Fluessigkeiten mit ihrem Molekularvolumen.' Annalen der Physik 263(3): 448-459. doi:10.1002/andp.18862630309. Bond, W. N. (1928). Proc. Phys. Soc. 41, 1.
- **ip status**: public-domain
- **prior art notes**: Bond number explains why microfluidics works at all: at L ~ 100 microns, Bo ~ 10^-3 for water, so gravity is irrelevant and surface tension dominates. This is THE physical foundation for the microfluidic regime; anchors every patent claim that recites 'gravity-independent operation', 'orientation-independent chip', or 'surface-tension-driven liquid handling'. Eoetvoes 1886 (the equivalent group) predates the entire modern microfluidic field by more than a century.

## Abbott Piccolo Xpress / Abaxis disc-format clinical chemistry analyzer (1995)

- **id**: `abbott-piccolo-xpress`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Abaxis (acquired by Zoetis, then Abbott)
- **disclosure**: Abbott Piccolo Xpress (originally Abaxis). https://www.abbott.com
- **ip status**: patented
- **prior art notes**: Centrifugal microfluidic disposable disc with pre-loaded dry reagent wells and integrated optical detection in benchtop reader. Each disc runs a chemistry panel (electrolytes, liver enzymes, kidney function) on 100 µL whole blood in 12 minutes. One of the earliest successful commercial centrifugal microfluidic platforms (1995 launch), predating most academic centrifugal LoD work.

## Abaxis VetScan VS2 veterinary clinical chemistry analyzer (1995)

- **id**: `abaxis-vetscan-vs2`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Abaxis (Zoetis)
- **disclosure**: Abaxis (acquired by Zoetis 2018) VetScan VS2 system; same disc-format as Piccolo Xpress for veterinary use.
- **ip status**: patented
- **prior art notes**: Veterinary-market sibling product of the Piccolo Xpress: same centrifugal microfluidic disc architecture but with veterinary chemistry panels. Reference for the broader veterinary diagnostic cartridge market, which under-indexes in human-medicine prior-art reviews despite using the same architectural primitives.

## Burstein/Tecan LabCD original disc-format platform (1997)

- **id**: `tecan-burstein-labcd`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Burstein Technology (acquired by Tecan)
- **disclosure**: Burstein Technology / Tecan LabCD platform. https://www.tecan.com (LabCD acquired and integrated)
- **ip status**: patented
- **prior art notes**: Pioneering centrifugal microfluidic platform from the late 1990s — predates most academic centrifugal-LoD work. Burstein's CD-format chemistry analyzer used spinning-disc-driven flow, capillary-burst valves, and integrated optical detection in a benchtop reader. Anticipates: many subsequent commercial centrifugal-LoD systems by demonstrating commercial feasibility 5–10 years before the academic literature peaked.

## Gyros Bioaffy CD immunoassay platform (2002)

- **id**: `gyros-bioaffy-cd`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Gyros AB (Sweden)
- **disclosure**: Gyros (now Gyros Protein Technologies) Bioaffy / Gyrolab system. https://www.gyrosproteintechnologies.com
- **ip status**: patented
- **prior art notes**: Centrifugal microfluidic immunoassay platform on injection-molded CD-format substrate. Disposable CDs contain hundreds of parallel affinity-column-format immunoassays driven by spin-rate-controlled centrifugal pumping and capillary-burst valves. Anticipates: lab-on-disc immunoassay architecture, parallel column-format affinity assays under centrifugal flow, and CD-format consumable economics.

## Lab-on-a-CD: centrifugal microfluidics platform (2006)

- **id**: `madou-2006-centrifugal-microfluidics`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Madou group, UC Irvine (and earlier Burstein/Tecan)
- **disclosure**: Madou, M.; Zoval, J.; Jia, G.; Kido, H.; Kim, J.; Kim, N. Lab on a CD. Annu. Rev. Biomed. Eng. 2006, 8, 601–628. DOI: 10.1146/annurev.bioeng.8.061505.095758
- **ip status**: patented
- **prior art notes**: Comprehensive review and synthesis of centrifugal microfluidics: pumping by spin-rate-controlled centrifugal force, valving by capillary-burst pressure thresholds, mixing by Coriolis-aided shaking, and assay sequencing by sequential burst-frequency design. Anticipates: lab-on-disc architecture, capillary-burst valves with threshold rotational frequencies, pumping-as-rotation as a substitute for external pressure, and the commercial pathway commercialized by Gyros (immunoassays), Samsung (Genio), Roche (cobas Liat traces architectural lineage). Among the few papers covering an entire substantive class of microfluidic device.

## Thermoresponsive hydrogel microvalves (2006)

- **id**: `oh-2006-thermoresponsive-microvalve`
- **corpus**: academic
- **device class**: valve-component
- **creator**: Oh, Ahn (SUNY Buffalo / Cincinnati)
- **disclosure**: Oh, K. W.; Ahn, C. H. A review of microvalves. J. Micromech. Microeng. 2006, 16, R13–R39. DOI: 10.1088/0960-1317/16/5/R01
- **ip status**: public-domain
- **prior art notes**: Comprehensive review of microvalves enumerating active (pneumatic, thermal, electrostatic, electromagnetic, piezoelectric, electrochemical, electrowetting) and passive (check, capillary-burst, hydrophobic) categories. Methodologically essential as the unified reference for microvalve prior art across the entire field; useful for invalidity contention against any patent claiming a 'novel microvalve' that turns out to fall within one of the eight active or three passive categories enumerated here.

## Whitesides Paper Microfluidics Patent Family (2007-10-12)

- **id**: `whitesides-patent-family-paper-microfluidics`
- **corpus**: academic
- **device class**: point-of-care-cartridge
- **creator**: President and Fellows of Harvard College (Martinez, Phillips, Carrilho, Whitesides et al.)
- **disclosure**: US7882415 priority 2007-10-12; US8470611; assigned to President and Fellows of Harvard College
- **ip status**: patented
- **prior art notes**: Harvard/Whitesides paper-microfluidics (microPAD) patent family. Anchors claims around: (a) cellulose paper substrate patterned with hydrophobic barriers (initially photoresist, then wax) defining hydrophilic channels for capillary fluid flow; (b) multi-zone paper devices with sample, reaction, and detection regions; (c) colorimetric assay readout via patterned reagent zones; (d) folded 3D paper microfluidic stacks. Companion academic disclosure: martinez-2007-paper-microfluidics, whitesides-2010-mu-pads-systematic. Anticipates paper-microfluidic POC cartridges for nutrition, infectious-disease, urinalysis, and metabolic-panel applications. Expiry: ~2027-2029 for original family.

## Centrifugal Lab-on-a-Disc for Salivary Caries-Risk Biomarker Detection (2018)

- **id**: `lab-on-disc-caries-detection-2018`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Multiple academic groups (KAIST, Madou-derived centrifugal microfluidics community)
- **disclosure**: Park J et al., Sensors and Actuators B: Chemical 268:218-226 (2018); doi:10.1016/j.snb.2018.04.114
- **ip status**: unknown
- **prior art notes**: Discloses a centrifugal lab-on-a-disc dedicated to caries-risk assessment from raw saliva, combining bacterial enumeration with biochemical assays on a single injection-molded disc. Builds on Madou centrifugal microfluidics architecture (entry: madou-2006-centrifugal-microfluidics). Anticipates: dental-chairside CD-format saliva cartridges; integrated bacterial-plus-chemistry caries panels on centrifugal platforms; burst-valve sequencing of multi-step saliva sample prep on disc.

## Sherlock Biosciences SHERLOCK Cartridge (2024)

- **id**: `sherlock-biosciences-sherlock-cartridge-2024`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Sherlock Biosciences Inc.
- **disclosure**: Sherlock Biosciences press release 2024-04 SHERLOCK STI; FDA Breakthrough Designation 2023-12-14; US10266887B2 (Cas13a-based detection)
- **ip status**: patented
- **prior art notes**: Discloses a single-use disposable cartridge that performs CRISPR-based nucleic acid detection (Cas13a or Cas12a collateral cleavage of fluorogenic reporters) entirely without an external instrument. Anticipates: instrument-free CRISPR diagnostic cartridges for STI / respiratory pathogens; lyophilized-on-cartridge isothermal amplification + Cas effector cleavage workflows; consumer point-of-use form factors for at-home or pharmacy testing. Anticipates claims to fully-self-contained CRISPR diagnostic cartridges that combine isothermal amplification with collateral-cleavage readout.
