---
title: droplet-flow-focusing-generation
parent: Cross-cuts
layout: default
---

# Cross-cut: `droplet-flow-focusing-generation`

**45 corpus entries disclose this subsystem.**

Earliest disclosure: 1806

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

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

## Plateau-Rayleigh instability (combined droplet-formation theory) (1879)

- **id**: `plateau-rayleigh-instability-combined`
- **corpus**: academic
- **device class**: other
- **creator**: Joseph Plateau (1873); Lord Rayleigh (1879)
- **disclosure**: Combined: Plateau, J. (1873). 'Statique experimentale et theorique des liquides soumis aux seules forces moleculaires.' Gauthier-Villars, Paris. AND Rayleigh, Lord (1879). 'On the instability of jets.' Proc. London Math. Soc. 10: 4-13.
- **ip status**: public-domain
- **prior art notes**: Combined entry for the Plateau-Rayleigh instability, the foundational classical theory underlying every microfluidic droplet generator (T-junction, flow-focusing, co-flow, step-emulsification). Plateau 1873 (experimental anchor on existence of the instability) plus Rayleigh 1879 (analytical derivation of the most-unstable wavelength) together publish 'a liquid jet breaks into droplets at a wavelength determined by surface tension and inertia' in the public literature 150 years before any droplet-microfluidic patent. Anticipates any patent claim reciting droplet-size selection from a continuous jet - Plateau-Rayleigh predicts the wavelength and growth rate. Combined entry exists so the dual-anchor citation is searchable as a single prior-art reference.

## Capillary Number Ca = mu U / gamma (1928)

- **id**: `capillary-number-dimensionless-group`
- **corpus**: academic
- **device class**: other
- **creator**: tradition (group structure implicit since 19th-century capillary-flow work)
- **disclosure**: Bond, W. N. (1928). 'The use of dimensionless equations.' Proc. Phys. Soc. London 41(1): 1-16; named by Taylor in subsequent capillary-flow literature. Implicit in Tate 1864, Plateau 1873, Rayleigh 1879 work on droplet break-up.
- **ip status**: public-domain
- **prior art notes**: Capillary number is the controlling parameter for every droplet generator. The dripping-to-jetting transition, the squeezing-to-shearing transition in T-junctions, and the droplet-size scaling laws in flow-focusing devices are all functions of Ca. Anchors: (a) all droplet-generator patents that recite a flow-rate-to-droplet-size scaling (Anna 2003, Thorsen 2002, Garstecki 2006); (b) co-flow droplet sizing claims; (c) step-emulsification regime maps. Any patent claim that recites operating conditions in terms of viscosity, velocity, and surface tension is anticipated by the capillary-number scaling.

## Tomotika 1935 - On the instability of a cylindrical thread of a viscous liquid surrounded by another viscous fluid (1935)

- **id**: `tomotika-1935-droplet-breakup-theory`
- **corpus**: academic
- **device class**: other
- **creator**: Susumu Tomotika
- **disclosure**: Tomotika, S. (1935). 'On the instability of a cylindrical thread of a viscous liquid surrounded by another viscous fluid.' Proc. R. Soc. A 150(870): 322-337. doi:10.1098/rspa.1935.0104
- **ip status**: public-domain
- **prior art notes**: Tomotika 1935 extends the Plateau-Rayleigh instability (1873/1879, both in corpus) to viscous cylindrical threads surrounded by a second viscous fluid - the canonical flow-focusing/co-flow droplet-generator geometry at microscale. Anticipates any patent claim reciting droplet-size selection by viscosity ratio, viscous-jet breakup in microfluidic flow-focusing channels, or wavelength-keyed droplet diameter prediction - all reduce to Tomotika scaling.

## Bretherton 1961 - The motion of long bubbles in tubes (1961)

- **id**: `bretherton-1961-bubble-in-tube`
- **corpus**: academic
- **device class**: other
- **creator**: Francis P. Bretherton
- **disclosure**: Bretherton, F. P. (1961). 'The motion of long bubbles in tubes.' J. Fluid Mech. 10(2): 166-188. doi:10.1017/S0022112061000160
- **ip status**: public-domain
- **prior art notes**: Discloses the canonical scaling for a confined-bubble system: thin liquid film thickness, bubble velocity offset from mean flow, and capillary pressure drop across the bubble - all functions of Ca = mu*U/gamma. Anticipates microfluidic claims involving Taylor-flow segmented gas-liquid reactors, bubble-trains in segmented-flow microreactors, on-chip oxygenation, gas-liquid heat-exchange microchannels, and bubble-based mixing enhancement claims keyed to film-thickness control. Any patent that claims a quantitative relationship between bubble velocity and channel film thickness, or that uses Ca^(2/3) scaling to predict performance, is anticipated by Bretherton 1961.

## Taylor 1964 - Disintegration of water drops in an electric field (Taylor cone) (1964)

- **id**: `taylor-1964-electrified-cone-electrospray`
- **corpus**: academic
- **device class**: other
- **creator**: Sir Geoffrey Ingram Taylor
- **disclosure**: Taylor, G. I. (1964). 'Disintegration of water drops in an electric field.' Proc. R. Soc. A 280(1382): 383-397. doi:10.1098/rspa.1964.0151
- **ip status**: public-domain
- **prior art notes**: Taylor 1964 derives the conical interface (Taylor cone) of a charged-fluid meniscus at the verge of jet emission. Foundational paper for electrospray ionization mass spectrometry (the Fenn 1989 prize-winning method), electrohydrodynamic droplet generation on chip, electrospinning of polymer fibers via microfluidic emitters, and Taylor-cone microfluidic emitter arrays for mass-spectrometry interfacing. Anticipates any patent claim reciting 'conical electrified meniscus emitting a jet at a threshold voltage' or 'electrospray emitter integrated with microfluidic chip'.

## Levenspiel 1972 - Chemical Reaction Engineering (2nd ed.) (1972)

- **id**: `levenspiel-1972-chemical-reaction-engineering`
- **corpus**: academic
- **device class**: other
- **creator**: Octave Levenspiel
- **disclosure**: Levenspiel, O. (1972). 'Chemical Reaction Engineering' (2nd ed.). John Wiley & Sons. ISBN 978-0-471-53016-8.
- **ip status**: public-domain
- **prior art notes**: Levenspiel 1972 is the canonical reactor-engineering textbook. The reactor archetypes - CSTR, PFR, packed-bed, batch - are ancestors of every microfluidic reactor disclosure: droplet reactors implement a discrete PFR; on-chip mixing chambers are CSTRs; packed-bead immunoassay chambers are packed-bed reactors. Anticipates microfluidic claims reciting residence-time control, mixing-vs-reaction selectivity arguments, or reactor-archetype-based device topology. Any patent that frames a microfluidic device as a 'CSTR-on-chip' or 'PFR-on-chip' is anticipated as to its reactor-engineering framing by Levenspiel.

## RainDance Technologies DropMaker Patent Family (2002-06-28)

- **id**: `raindance-dropmaker-patent-family`
- **corpus**: private
- **device class**: droplet-generator
- **creator**: RainDance Technologies (acquired by Bio-Rad 2017-03-02)
- **disclosure**: US7708949 priority 2002-06-28; US8772046; US8500053; US8841071 (originally RainDance Technologies, now Bio-Rad)
- **ip status**: patented
- **prior art notes**: RainDance Technologies patent family covering picoliter-droplet generation in fluorinated-oil emulsions. Anchors claims around: (a) flow-focusing or T-junction generation of monodisperse aqueous droplets in fluorinated oil; (b) use of perfluorinated polyether surfactants to stabilize droplets against coalescence; (c) compatibility with PCR thermal cycling; (d) sample-encapsulation rates >1 kHz. Foundation patents acquired by Bio-Rad in March 2017 for approximately $72M (Bio-Rad 8-K 2017-02-01). Anticipates ddPCR / digital droplet-PCR cartridges and droplet-library generators. Existing companion entry raindance-bio-rad-acquisition documents the deal; this entry maps the licensable patent estate.

## Flow-focusing droplet generation in microfluidic devices (2003)

- **id**: `anna-2003-flow-focusing-droplet`
- **corpus**: academic
- **device class**: droplet-generator
- **creator**: Anna, Bontoux, Stone (Harvard)
- **disclosure**: Anna, S. L.; Bontoux, N.; Stone, H. A. Formation of dispersions using 'flow focusing' in microchannels. Appl. Phys. Lett. 2003, 82, 364–366. DOI: 10.1063/1.1537519
- **ip status**: public-domain
- **prior art notes**: Established flow-focusing droplet generation as a parallel architecture to the T-junction. Disclosed: a continuous-phase fluid focuses a dispersed-phase stream through a constriction, forming droplets at controllable rates and sizes. This geometry underlies most modern droplet platforms (10x Genomics-style microfluidic chips, Bio-Rad ddPCR generators, etc.).

## iGEM Foundation Distribution Kit (2003)

- **id**: `igem-distribution-kit`
- **corpus**: open
- **device class**: other
- **creator**: iGEM Foundation (originally MIT — Endy, Knight, Smolke, Rettberg)
- **disclosure**: iGEM founded as MIT IAP course 2003; first formal distribution kit 2004; iGEM Foundation incorporated 2012; https://igem.org; Registry of Standard Biological Parts http://parts.igem.org; key paper Smolke C., 'Building outside of the box: iGEM and the BioBricks Foundation', Nat Biotechnol 27:1099 (2009)
- **ip status**: open-permissive
- **prior art notes**: Discloses an annual mass-distribution of standardized DNA parts under permissive license, plus a public registry of their characterizations. Relevance to microfluidics commons: hundreds of iGEM projects 2007-2024 have published microfluidic device designs (paper microfluidics, droplet generators, lab-on-chip cartridges) on the iGEM wiki under CC-BY licenses; these wiki pages are themselves a substantial body of prior art for low-cost microfluidic education kits, point-of-care biosensors, and student-built droplet generators. Specifically anticipates the 'student-built point-of-care diagnostic with cell-free expression on paper or in droplets' design pattern many times over since 2010.

## Quake Lab Droplet Flow-Focusing Patent Family (2003-09-15)

- **id**: `quake-patent-family-droplet-flow-focusing`
- **corpus**: academic
- **device class**: droplet-generator
- **creator**: President and Fellows of Harvard College (Anna, Bontoux, Stone, Quake)
- **disclosure**: US7268167 priority 2003-09-15; US7375085; both assigned originally to President and Fellows of Harvard College
- **ip status**: patented
- **prior art notes**: Harvard-anchored patent family covering hydrodynamic flow-focusing droplet generation. Anchors claims around: (a) a microfluidic device with an inner phase channel meeting two outer continuous-phase channels at an orifice; (b) generation of monodisperse droplets via Rayleigh-Plateau breakup at the orifice; (c) independent control of droplet diameter via continuous-phase flow rate while inner-phase flow rate sets generation frequency; (d) chip geometry compatible with PDMS soft lithography. Anticipates flow-focusing droplet-generator chips in microfluidic context. Underlying Anna 2003 paper (anna-2003-flow-focusing-droplet) is the published companion. The patent family was a precursor for the licensing chains that fed RainDance, QuantaLife, and 10x Genomics droplet platforms. Expiry: ~2023-2024 for earliest members, but continuations may extend coverage on specific geometries.

## Microfluidic alginate microbead generation (2007)

- **id**: `choi-weitz-2007-alginate-microbead`
- **corpus**: academic
- **device class**: droplet-generator
- **creator**: various — Lee, Weitz, Doyle (early 2000s contributions)
- **disclosure**: Choi, C.-H.; Jung, J.-H.; Rhee, Y. W.; Kim, D.-P.; Shim, S.-E.; Lee, C.-S. Generation of monodisperse alginate microbeads and in situ encapsulation of cell in microfluidic device. Biomed. Microdevices 2007, 9, 855–862. DOI: 10.1007/s10544-007-9098-7
- **ip status**: patented
- **prior art notes**: Foundational disclosure of microfluidic alginate microbead generation: aqueous alginate flow-focused into oil with downstream calcium-mediated gelation produces monodisperse alginate microbeads suitable for cell encapsulation. Anticipates: alginate-as-microbead-substrate-in-droplet-microfluidics, which became the backbone of single-cell sequencing platforms (Drop-seq, inDrops, Tapestri) where the bead encapsulates barcoding oligos.

## RainDance Technologies droplet platform (acquired by Bio-Rad) (2008)

- **id**: `raindance-bio-rad-acquisition`
- **corpus**: private
- **device class**: droplet-generator
- **creator**: RainDance Technologies (acquired by Bio-Rad 2017)
- **disclosure**: RainDance Technologies (acquired by Bio-Rad 2017). Brouzes 2009 commercialization. https://www.bio-rad.com
- **ip status**: patented
- **prior art notes**: Commercial pioneer in droplet microfluidics for high-throughput screening and ddPCR (RainDrop ddPCR), absorbed into Bio-Rad's portfolio in 2017. The combined RainDance + QuantaLife (Bio-Rad's earlier ddPCR acquisition) IP estate is the dominant patent thicket in droplet-format diagnostics and the foundational portfolio behind Bio-Rad QX ddPCR.

## Dolomite Microfluidics droplet generation system (2009)

- **id**: `dolomite-microfluidics-droplet-system`
- **corpus**: private
- **device class**: droplet-generator
- **creator**: Dolomite Microfluidics (Blacktrace Holdings)
- **disclosure**: Dolomite Microfluidics droplet system; product literature. https://www.dolomite-microfluidics.com
- **ip status**: patented
- **prior art notes**: Glass-based commercial droplet generation chips and instruments aimed at research and bioprocess users. Anticipates: glass droplet-junction chips as commodity components, integration with Mitos pressure pumps, and the modular off-the-shelf microfluidics product category as opposed to bespoke PDMS chips.

## Droplet microfluidic technology for single-cell high-throughput screening (2009)

- **id**: `brouzes-2009-droplet-screening`
- **corpus**: academic
- **device class**: droplet-generator
- **creator**: RainDance Technologies / Perrimon lab
- **disclosure**: Brouzes, E.; Medkova, M.; Savenelli, N.; Marran, D.; Twardowski, M.; Hutchison, J. B.; Rothberg, J. M.; Link, D. R.; Perrimon, N.; Samuels, M. L. Droplet microfluidic technology for single-cell high-throughput screening. Proc. Natl. Acad. Sci. USA 2009, 106, 14195–14200. DOI: 10.1073/pnas.0903542106
- **ip status**: patented
- **prior art notes**: Established droplet microfluidics for single-cell HTS by combining flow-focusing droplet generation, on-droplet barcoding, fluorescence-activated droplet sorting (FADS), and downstream analysis. Anticipates: barcoded droplet libraries for combinatorial screening, droplet sorting at kHz rates with electrocoalescence, and the directed-evolution / single-cell-screen workflows commercialized by RainDance and absorbed into Bio-Rad's portfolio.

## Quake/Stanford Bead-in-Droplet Single-Cell Encapsulation Patent Family (2010)

- **id**: `quake-patent-family-bead-droplet-single-cell`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: Board of Trustees of the Leland Stanford Junior University (Quake et al.) and co-inventors
- **disclosure**: US8748094; US9695468; US9856530 and continuations (Stanford / co-assigned with collaborators)
- **ip status**: patented
- **prior art notes**: Stanford/Quake-group patent family on bead-in-droplet single-cell barcoding. Anchors claims around: (a) microfluidic flow-focusing co-encapsulation of a single cell with a single barcoded primer-bearing bead in an oil-in-water droplet; (b) bead-bound oligonucleotide barcodes with cell-barcode + UMI + capture-sequence regions; (c) in-droplet lysis followed by mRNA capture on the bead; (d) bulk recovery of beads for downstream pooled library construction. Macosko 2015 Drop-seq (macosko-2015-drop-seq) is the publication-disclosure analog using the Broad/McCarroll lineage; this entry maps the licensable Stanford patent estate that 10x Genomics used as one input for the Chromium platform. Anticipates single-cell sequencing prep cartridges that use co-encapsulation of cell+bead in droplets.

## Bio-Rad QX Droplet Digital PCR system (2011)

- **id**: `bio-rad-qx-ddpcr-system`
- **corpus**: private
- **device class**: droplet-generator
- **creator**: Bio-Rad / QuantaLife
- **disclosure**: Bio-Rad Laboratories QX100/QX200 ddPCR systems. Hindson et al. 2011 Anal. Chem. 83, 8604–8610. DOI: 10.1021/ac202028g
- **ip status**: patented
- **prior art notes**: Discloses an integrated commercial workflow for droplet digital PCR: cartridge-based generation of ~20,000 monodisperse droplets per sample, off-chip thermal cycling, and droplet-by-droplet fluorescence readout. Anticipates: the digital-PCR workflow as a discrete commercial category, integration of injection-molded droplet-generation cartridges with an instrument-side flow controller, and a sample-to-answer ddPCR system architecture.

## Bio-Rad Acquisition of QuantaLife 2011 (QX200 ddPCR Origin) (2011-09-06)

- **id**: `biorad-quantalife-acquisition-2011`
- **corpus**: private
- **device class**: other
- **creator**: QuantaLife Inc. (acquired by Bio-Rad)
- **disclosure**: Bio-Rad press release 2011-09-06; deal value $162M cash plus $35M earnout; QuantaLife technology became QX100/QX200 product line
- **ip status**: patented
- **prior art notes**: Consolidation event. Documents Bio-Rad's 2011-09-06 acquisition of QuantaLife (initial $162M plus $35M earnout). The QuantaLife technology, originally developed by Bill Colston and team (formerly Lawrence Livermore), became the Bio-Rad QX100 and QX200 droplet-digital PCR product line (existing entry: bio-rad-qx-ddpcr-system). Six years later, Bio-Rad's 2017 acquisition of RainDance (raindance-bio-rad-acquisition, $72M) consolidated the second major ddPCR patent estate. The combined QuantaLife + RainDance IP gave Bio-Rad a dominant ddPCR market position, which became the basis for Bio-Rad's litigation against 10x Genomics. Defensive value: maps the patent-assignment chain.

## Broad Institute Drop-seq Patent Family (Macosko / McCarroll lineage) (2013-04-26)

- **id**: `broad-institute-drop-seq-patent-family`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: Broad Institute / Harvard / Steve McCarroll laboratory
- **disclosure**: US10221442 priority 2014; US20170029873; WO2014210353 (Broad Institute / Harvard / Steve McCarroll lab)
- **ip status**: patented
- **prior art notes**: Broad Institute / Harvard / McCarroll lab patent family for Drop-seq. Anchors claims around: (a) microfluidic flow-focusing co-encapsulation of a single cell with a single barcoded bead and lysis buffer in an aqueous-in-oil droplet; (b) bead-bound primer architecture (PCR handle + cell barcode + UMI + poly-T capture); (c) cell lysis in droplet with mRNA capture by bead; (d) bead recovery and pooled cDNA library construction. Companion academic disclosure already in corpus: macosko-2015-drop-seq. This entry maps the patent estate that 10x Genomics licensed (one of multiple licenses underlying the Chromium platform) and that Broad Institute can assert against unauthorized commercial implementations. Defensive value: timestamps the academic Macosko 2015 paper plus the Broad-assigned patent family as combined 102/103 prior art for any droplet-based single-cell barcoding implementation.

## Aspect Biosystems RX1 Lab-on-a-Printer microfluidic bioprinter (2014)

- **id**: `aspect-biosystems-rx1`
- **corpus**: private
- **device class**: printer-tooling
- **creator**: Aspect Biosystems
- **disclosure**: Aspect Biosystems Lab-on-a-Printer. https://www.aspectbiosystems.com
- **ip status**: patented
- **prior art notes**: Microfluidic print-head bioprinter combining flow-focusing fiber generation with multi-material extrusion. Architecturally distinct from Cellink/Allevi extrusion bioprinters by integrating microfluidic mixing and crosslinking into the print head itself. Anticipates: in-print-head microfluidic mixing for tissue-construct printing.

## 10x Genomics Chromium GEM-X Bead-Barcoding Patent Family (2014-04-10)

- **id**: `tenx-genomics-chromium-gem-patent-family`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: 10x Genomics Inc. (with Broad Institute licensed background)
- **disclosure**: US10221442 priority 2012-04-10 (Broad-licensed); 10x-internal: US9694361; US9701957; US10357771; US10752950; US11248267 (10x Genomics)
- **ip status**: patented
- **prior art notes**: 10x Genomics Chromium / GEM (Gel-bead-in-Emulsion) patent family. Anchors claims around: (a) microfluidic flow-focusing co-encapsulation of a single cell with a single barcoded gel bead and lysis reagents in an aqueous droplet within fluorinated oil; (b) gel-bead chemistry releasing barcoded primers in-droplet; (c) cell-barcode + UMI + capture-sequence architecture; (d) recovery of barcoded cDNA for bulk library construction; (e) Chromium chip and Chromium X instrument hardware. Several family members (notably US10221442) trace to Broad Institute Macosko / Drop-seq priority that 10x licensed. Anticipates and is anticipated by Quake/Stanford bead-droplet single-cell family (quake-patent-family-bead-droplet-single-cell). Companion existing entries: 10x-genomics-chromium-controller, macosko-2015-drop-seq.

## Drop-seq single-cell RNA sequencing (2015)

- **id**: `macosko-2015-drop-seq`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: Macosko, McCarroll lab, Broad Institute
- **disclosure**: Macosko, E. Z. et al. Highly parallel genome-wide expression profiling of individual cells using nanoliter droplets. Cell 2015, 161, 1202–1214. DOI: 10.1016/j.cell.2015.05.002
- **ip status**: public-domain
- **prior art notes**: Anticipates: co-encapsulation of single cells with barcoded beads in droplets via flow-focusing, lysis-on-bead chemistry, downstream pooled sequencing with barcode demultiplexing. Together with InDrops (Klein et al. 2015), this is the technical foundation of the modern single-cell genomics ecosystem, including the commercial 10x Genomics Chromium platform.

## inDrops: droplet-based barcoding for single-cell transcriptomics (2015)

- **id**: `klein-2015-indrops`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: Klein, Weitz, Kirschner labs (Harvard)
- **disclosure**: Klein, A. M.; Mazutis, L.; Akartuna, I.; Tallapragada, N.; Veres, A.; Li, V.; Peshkin, L.; Weitz, D. A.; Kirschner, M. W. Droplet barcoding for single-cell transcriptomics applied to embryonic stem cells. Cell 2015, 161, 1187–1201. DOI: 10.1016/j.cell.2015.04.044
- **ip status**: public-domain
- **prior art notes**: Published one week after Drop-seq; together they establish single-cell droplet RNA-seq as a category. inDrops uses hydrogel-encapsulated barcodes (rather than Drop-seq's polystyrene beads), an architectural choice subsequently inherited by 1Cell-Bio's commercial inDrops platform. Both papers anticipate: massively parallel single-cell RNA-seq via droplet co-encapsulation, but with different bead chemistries that anchor distinct patent positions.

## Barcoded hydrogel beads for single-cell RNA-seq (2015)

- **id**: `rotem-zilionis-2015-barcoded-bead`
- **corpus**: academic
- **device class**: droplet-generator
- **creator**: Klein / Mazutis / Weitz (Harvard)
- **disclosure**: Klein, A. M.; Mazutis, L.; et al. (inDrops paper, see klein-2015-indrops). Zilionis, R. et al. Single-cell barcoding and sequencing using droplet microfluidics. Nat. Protoc. 2017, 12, 44–73.
- **ip status**: public-domain
- **prior art notes**: Disclosed barcoded-hydrogel-bead manufacturing for single-cell RNA-seq: split-and-pool synthesis on alginate beads in microfluidic encapsulation produces a library of beads each bearing a unique barcode, used in inDrops and similar platforms. Anticipates: split-pool-bead-barcoding architecture, which became central to the inDrops and 10x Chromium commercial platforms.

## 10x Genomics vs Bio-Rad Patent Litigation (RainDance basis) (2015-02-12)

- **id**: `tenx-vs-bio-rad-litigation`
- **corpus**: private
- **device class**: other
- **creator**: Bio-Rad Laboratories (plaintiff) vs 10x Genomics (defendant)
- **disclosure**: Bio-Rad Labs v. 10x Genomics, D.Del. 1:15-cv-00152 (filed 2015-02-12); jury verdict 2018-11-13 awarded $24M to Bio-Rad; later judgments, appeals, and 2020 settlement; subsequent N.D.Cal. cases
- **ip status**: patented
- **prior art notes**: Litigation entry. Bio-Rad sued 10x Genomics in D.Del. 1:15-cv-00152 (filed 2015-02-12) asserting RainDance-derived droplet patents (US7708949, US8273573, US8889083 and others) against the Chromium platform. Jury verdict 2018-11-13 awarded $24M with 15% royalty going forward. Multiple parallel cases followed in N.D.Cal. and at the ITC. Settled via cross-license arrangement around 2020. Defensive value: documents the most-litigated case in microfluidics history and establishes the legal interpretation of several RainDance/QuantaLife claim terms. Useful for any party defending against droplet-microfluidic claims.

## 10x Genomics Chromium controller and Next GEM chip (2016)

- **id**: `10x-genomics-chromium-controller`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: 10x Genomics
- **disclosure**: 10x Genomics Chromium platform; product literature and Zheng et al. 2017 Nat. Commun. 8, 14049. DOI: 10.1038/ncomms14049
- **ip status**: patented
- **prior art notes**: Commercial single-cell encapsulation platform: Chromium controller drives flow-focusing geometry on a disposable Next GEM chip, co-encapsulating cells with barcoded gel beads in droplets for downstream sequencing. Anticipates: high-throughput parallel droplet generation in a disposable thermoplastic cartridge driven by an instrument-side pneumatic pressure source, the gel-bead-in-droplet architecture for barcoded single-cell genomics, and the integration of microfluidic droplet generation with a turnkey commercial instrument workflow. Encumbered by an aggressive patent thicket; corpus entry exists to enable invalidity analysis.

## 1CellBio inDrop platform (commercial inDrops) (2016)

- **id**: `1cellbio-indrops-commercial`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: 1CellBio Inc.
- **disclosure**: 1CellBio inDrop System commercial release 2016. https://1cell-bio.com/. Klein, A. M. et al. Droplet barcoding for single-cell transcriptomics applied to embryonic stem cells. Cell 2015, 161, 1187-1201. DOI: 10.1016/j.cell.2015.05.044.
- **ip status**: patented
- **prior art notes**: Commercial implementation of inDrops (Klein 2015): single cells co-encapsulated with photo-cleavable hydrogel barcoded beads in a PDMS flow-focusing chip driven by external syringe pumps. Anticipates: the academic-spinout commercialization path for single-cell barcoding, the use of dissolvable hydrogel beads as barcode carriers (vs. solid beads in Drop-seq), and the lower-cost open-architecture alternative to 10x Chromium. Many academic labs run this directly off the Klein 2015 paper without 1CellBio hardware.

## Stilla Naica System Crystal Digital PCR Patent Family (2016)

- **id**: `stilla-naica-crystal-digital-pcr-patent-family`
- **corpus**: private
- **device class**: other
- **creator**: Stilla Technologies
- **disclosure**: WO2017046257A1 (Stilla Technologies, priority 2015-09-15); US10744506B2 'Method and apparatus for performing digital assays using polydisperse droplets'; Stilla Naica System product launch 2016
- **ip status**: patented
- **prior art notes**: Discloses a chamber-free 'crystal' digital PCR architecture in which an aqueous sample is partitioned into a 2D monolayer of monodisperse droplets confined between two parallel surfaces inside a microfluidic chip. The chip integrates a flow-focusing droplet generator with an immobilization chamber whose gap height is matched to droplet diameter so that droplets self-organize into a hexagonally close-packed 2D crystal. Anticipates: (a) any digital PCR architecture relying on geometrically constrained 2D droplet arrays for thermal cycling and image-based digital readout; (b) integrated single-chip dPCR cartridges with on-chip droplet generation, thermal cycling, and multi-color fluorescence imaging without an external droplet reader; (c) the use of close-packing density rather than addressed wells for partitioning. Material relevant to claims of Bio-Rad QX-series patents asserting required chambered/well architectures.

## Sphere Fluidics Cyto-Mine Single-Cell Analysis System (2017)

- **id**: `sphere-fluidics-cyto-mine-acoustic-droplet-sorting`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Sphere Fluidics Limited (Cambridge UK; Huck/Edel academic origins)
- **disclosure**: Sphere Fluidics Cyto-Mine launch press release 2017; Mazutis L., Gilbert J., Ung W. L., Weitz D. A., Griffiths A. D., Heyman J. A., Nature Protocols 8:870 (2013), doi:10.1038/nprot.2013.046; US patent 9,486,803
- **ip status**: patented
- **prior art notes**: Cyto-Mine discloses an integrated single-cell platform using PDMS picodroplet generation, on-chip incubation, fluorogenic assay readout, and dielectrophoretic sort of selected droplets into recovery wells. Anticipates: (i) integrated cartridge platforms combining droplet generation, incubation, image-based assay, and DEP sort in a single workflow; (ii) DEP droplet sorting at >300 Hz integrated with picodroplet microfluidics; (iii) cell-line and antibody discovery workflows fully on-cartridge. Adjacent to Berkeley Lights Beacon (different actuation: OEP vs droplet+DEP).

## Sphere Fluidics Cyto-Mine single-cell screening platform (2017)

- **id**: `sphere-fluidics-cytomine`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Sphere Fluidics
- **disclosure**: Sphere Fluidics Cyto-Mine product launch 2017. https://spherefluidics.com/.
- **ip status**: patented
- **prior art notes**: Integrated picodroplet workflow for single-cell antibody discovery and clonal cell-line selection: cells encapsulated in flow-focusing droplets together with reporters, droplets imaged in flow for fluorescence signal, target droplets sorted dielectrophoretically into recovery wells. Anticipates: end-to-end automated picodroplet single-cell screening cartridges - droplet generation, incubation, fluorescence-activated sorting - integrated in a single instrument. Important commercial prior art for the picodroplet cell-line-development workflow.

## Namocell Hana Single Cell Dispenser (2017)

- **id**: `namocell-hana-single-cell-dispenser`
- **corpus**: private
- **device class**: dispenser-pipettor
- **creator**: Namocell Inc. (acquired by Bio-Rad 2021)
- **disclosure**: Namocell Inc. product launch 2017 (Stanford spinout, Bio-Rad acquisition 2021); US10625259B2 priority 2014
- **ip status**: patented
- **prior art notes**: Discloses a disposable cartridge implementing pressure-driven flow-focusing droplet ejection coupled to a real-time fluorescence detector that gates each droplet's destination plate well based on cell count and fluorescence intensity. Anticipates: integrated single-use cell sorter that delivers verified single cells into target wells without sheath-fluid contamination paths; disposable plastic equivalent of a sterile FACS sort with deposition recorded per well. Specifically anticipates claims to single-cell printers that combine flow-focusing droplet generation with downstream fluorescence-based well assignment.

## 1CellBio inDrop Commercial Reagent System (2017)

- **id**: `1cellbio-indrops-commercial-extension`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: 1CellBio Inc.
- **disclosure**: 1CellBio inDrop product launch 2017; Klein et al., Cell 161:1187 (2015) doi:10.1016/j.cell.2015.04.044 (academic origin)
- **ip status**: patented
- **prior art notes**: Discloses the commercial productization of the inDrops academic protocol including hydrogel-bead format barcoded primer release via UV photo-cleavage in droplet. Anticipates: photo-cleavable barcoded hydrogel beads as droplet co-encapsulation reagents; UV-triggered primer release inside droplets for single-cell RT initiation.

## uFluidix Open Educational Chip Kit (2017)

- **id**: `ufluidix-educational-chip-kit`
- **corpus**: open
- **device class**: consumable-bulk
- **creator**: uFluidix Inc.
- **disclosure**: uFluidix Inc. educational product page; ufluidix.com/education
- **ip status**: open-permissive
- **prior art notes**: Discloses an open undergrad microfluidic kit including PDMS chip designs (droplet, gradient, herringbone) released under permissive license. Anticipates: open-source educational microfluidic chip libraries; reference designs for undergraduate teaching of canonical microfluidic primitives.

## Mission Bio Tapestri Droplet Single-Cell DNA Patent Family (2017)

- **id**: `mission-bio-tapestri-droplet-scdna-patent-family`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Mission Bio, Inc.
- **disclosure**: US10619204B2 'Methods for single cell genetic analysis' (priority 2015-11); WO2017106777A1; Mission Bio Tapestri platform launch 2018
- **ip status**: patented
- **prior art notes**: Discloses Mission Bio's two-step droplet workflow distinct from the 10x Chromium GEM single-droplet co-encapsulation: cells are first encapsulated and lysed inside droplets, then a second droplet containing barcoded primers, polymerase, and dNTPs is electrocoalesced with the lysate droplet to perform targeted multiplex PCR per cell. Anticipates: (a) two-step electrocoalescence-based single-cell barcoding workflows; (b) targeted scDNA-seq via in-droplet multiplex PCR rather than whole-transcriptome amplification; (c) injection-molded cartridges that integrate two sequential droplet generators with an electrode-equipped coalescence channel.

## Bio-Rad ddPCR Patent Consolidation Position (post-RainDance 2017) (2017-03-02)

- **id**: `biorad-ddpcr-consolidation-position-2017`
- **corpus**: private
- **device class**: other
- **creator**: Bio-Rad Laboratories Inc.
- **disclosure**: Bio-Rad 8-K 2017-02-01 (RainDance acquisition close); Bio-Rad 10-K 2017 IP discussion; combined patent estate analysis
- **ip status**: patented
- **prior art notes**: Consolidation-position entry capturing the post-2017 Bio-Rad ddPCR patent landscape. By March 2017, Bio-Rad held: (a) QuantaLife-originated droplet-PCR patents (acquired 2011); (b) RainDance picoliter-droplet patents (acquired 2017); (c) Bio-Rad-internal continuations and improvements. This combined estate gave Bio-Rad a dominant negotiating position with all parties using droplet partitioning for nucleic-acid quantification, including 10x Genomics (single-cell), Stilla (Naica), Sysmex (RainDrop). Bio-Rad subsequently sued 10x Genomics under multiple counts of patent infringement (10x-genomics-vs-bio-rad-litigation entry below). Defensive value: a one-stop disclosure of the patent positions Bio-Rad used to anchor those suits.

## Mission Bio Tapestri single-cell DNA sequencing (2018)

- **id**: `mission-bio-tapestri`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Mission Bio
- **disclosure**: Mission Bio Tapestri platform. https://missionbio.com/tapestri/
- **ip status**: patented
- **prior art notes**: Two-step droplet workflow for single-cell DNA sequencing: cells encapsulated, lysed, and tagged in primary droplets; PCR products extracted and re-emulsified for amplicon sequencing. Anticipates: serial-emulsion architecture in single-cell genomics workflows, distinguishing Mission Bio's IP position from 10x Genomics' single-emulsion approach.

## Stilla Naica Sapphire Chip Mask Architecture Patent Family (2018)

- **id**: `stilla-naica-sapphire-chip-patent`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Stilla Technologies
- **disclosure**: Stilla Technologies Sapphire chip product release 2018; WO2019207090A1; US11364502B2 'Microfluidic chip architecture with optimized phase actuation'
- **ip status**: patented
- **prior art notes**: Discloses the Sapphire chip's micro-channel mask topology in which a single sample inlet branches via passive hydrodynamic resistors to four parallel flow-focusing junctions, each feeding a distinct 2D crystal observation chamber. Anticipates claims directed to: (a) parallelized partitioning networks with shared oil source and per-sample passive flow division; (b) a single injection-molded chip carrying multiple independent dPCR reactions without active valving; (c) the use of a serpentine pre-mix region upstream of flow-focusing junctions for emulsion stabilization. Includes mask drawings sufficient to enable fabrication of equivalent COC parts at 100-200 micrometer feature sizes.

## Namocell Pala Single Cell Dispenser (2020)

- **id**: `namocell-pala-single-cell-dispenser`
- **corpus**: private
- **device class**: dispenser-pipettor
- **creator**: Namocell Inc. (Bio-Rad)
- **disclosure**: Namocell Pala datasheet 2020; Bio-Rad press 2021; US patent family above
- **ip status**: patented
- **prior art notes**: Extends Hana design to 5-color fluorescence and explicit doublet discrimination by per-droplet image analysis. Anticipates claims to disposable-cartridge multi-color cell sorters with image-based event verification and per-deposit traceability metadata for regulated single-cell-cloning workflows (cell-line provenance documentation under USP/ICH guidelines).

## CARMEN Combinatorial Arrayed Reactions for Multiplexed Evaluation Patent Family (2020-04-29)

- **id**: `quake-broad-carmen-multiplex-prep-patent`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: Broad Institute / Harvard (Sabeti, Myhrvold, Ackerman)
- **disclosure**: US Provisional 62/892,447; published as WO2021022045A1 (Broad Institute / Harvard)
- **ip status**: patented
- **prior art notes**: Broad Institute patent family covering CARMEN (Combinatorial Arrayed Reactions for Multiplexed Evaluation of Nucleic acids). Anchors claims around: (a) microfluidic platform for high-throughput multiplexed nucleic-acid detection using fluorescent-color-coded droplets; (b) merging of sample droplets with CRISPR-Cas13 detection-reagent droplets; (c) automated identification of droplet pairs by color barcode; (d) parallel detection of >100 pathogens per chip. Ackerman et al. Nature 2020 (myhrvold-zhang-2018-shine-crispr-on-paper covers SHINE; CARMEN is distinct) provides the academic disclosure. Defensive interest: Broad Institute is the assertive licensor in CRISPR diagnostics; this patent family overlaps Mammoth/Sherlock claim space and any droplet-pairing combinatorial diagnostic.

## Machine-learning-driven droplet generator design (Lashkaripour 2021/2024) (2021)

- **id**: `lashkaripour-2024-ml-droplet-design`
- **corpus**: academic
- **device class**: droplet-generator
- **creator**: Densmore lab, Boston University
- **disclosure**: Lashkaripour, A.; Rodriguez, C.; Mehdipour, N.; Mardian, R.; McIntyre, D.; Ortiz, L.; Campbell, J.; Densmore, D. Machine learning enables design automation of microfluidic flow-focusing droplet generation. Nat. Commun. 2021, 12, 25. DOI: 10.1038/s41467-020-20284-z
- **ip status**: open-permissive
- **prior art notes**: Disclosed DAFD (Design Automation of Fluid Dynamics): ML model trained on microfluidic experimental data predicts flow-focusing droplet generator geometry from desired droplet size and rate. Anticipates: ML-as-design-automation for microfluidic chip geometry, and the broader trend of replacing CFD simulation with trained models for microfluidic design.

## DAFD — Design Automation of Flow-Focusing Droplet Generators (2021-01-06)

- **id**: `lashkaripour-2021-dafd-droplet-design-automation`
- **corpus**: open
- **device class**: droplet-generator
- **creator**: Ali Lashkaripour, Douglas Densmore et al. (Boston University CIDAR Lab)
- **disclosure**: Lashkaripour A, Rodriguez C, Mehdipour N, Mardian R, McIntyre D, Ortiz L, Campbell J, Densmore D. Machine learning enables design automation of microfluidic flow-focusing droplet generation. Nature Communications 12: 25 (2021). doi:10.1038/s41467-020-20284-z
- **ip status**: open-permissive
- **prior art notes**: Discloses element-by-element an inverse-design pipeline: (1) parameterized geometry of a flow-focusing droplet generator, (2) supervised ML model trained on experimental droplet datasets predicting diameter and generation rate, (3) automated search over geometry + flow rates given user-specified targets, (4) public web deployment generating ready-to-fabricate device files, (5) successor versions covering versatility/stability metrics and aqueous-in-oil + oil-in-aqueous double emulsions. Anticipates: (a) ML inverse-design claims for droplet-microfluidic devices, (b) automated design of double-emulsion generators, (c) cloud-deployed microfluidic CAD generating chip files from performance specs, (d) using neural ensembles plus search algorithms to deliver targeted droplet morphology — published two-plus years before most commercial assertions in this niche.

## Fluent BioSciences PIPseq particle-templated emulsification (2022-02-01)

- **id**: `fluent-biosciences-pipseq`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Fluent BioSciences
- **disclosure**: Clark, I. C. et al. Microfluidics-free single-cell genomics with templated emulsification. Nat. Biotechnol. 2023, 41, 1557-1566. DOI: 10.1038/s41587-023-01685-z. Fluent BioSciences product launch 2022.
- **ip status**: patented
- **prior art notes**: PIPseq replaces flow-focusing droplet generation with templated emulsification: pre-formed hydrogel particles carrying barcoded oligos are mixed with cells and oil in a tube, then vortexed; the hydrogel particle becomes the template that nucleates a uniform aqueous droplet around each particle. Anticipates: chip-free droplet-template emulsification for single-cell barcoding, reducing the sample-prep instrument to a vortexer. Major prior-art consequence: invalidates broad claims requiring 'microfluidic flow-focusing' as the necessary droplet-generation mechanism for high-throughput single-cell barcoding. Originated in the Adam Abate lab (UCSF).

## Mission Bio Tapestri PRIM (Pre-Integrated Multi-omics) (2024)

- **id**: `mission-bio-tapestri-prim-2024`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Mission Bio Inc.
- **disclosure**: Mission Bio Tapestri PRIM announcement 2024; product brief; US10745742B2 (Tapestri Two-step encapsulation)
- **ip status**: patented
- **prior art notes**: Discloses extension of Tapestri two-step droplet workflow to add ATAC chromatin accessibility measurement alongside DNA + protein on the same cell. Anticipates: combined DNA + protein + chromatin single-cell assays delivered through two-step droplet encapsulation in a sealed plastic cartridge; sequential picoinjection-based reagent addition for multi-omic single-cell library construction.

## DAFD 3.0 — Double-Emulsion Droplet Design Automation (2024-01-02)

- **id**: `lashkaripour-2024-dafd-double-emulsion`
- **corpus**: open
- **device class**: droplet-generator
- **creator**: Ali Lashkaripour, Polly Fordyce, Douglas Densmore et al. (Stanford / Boston University)
- **disclosure**: Lashkaripour A, McIntyre DP, Calhoun SGK, Krauth K, Densmore D, Fordyce PM. Design automation of microfluidic single and double emulsion droplets with machine learning. Nature Communications 15: 83 (2024). doi:10.1038/s41467-023-44068-3
- **ip status**: open-permissive
- **prior art notes**: Distinct from the 2021 DAFD 1.0 disclosure, this entry pins the 2024 extension to double emulsions. Element-by-element discloses: (1) parameterised geometry library for single + double-emulsion flow-focusing devices, (2) consensus ensemble ML model trained on experimental droplet datasets, (3) automated search returning device geometry + flow-rate setpoints for user-targeted single or double-emulsion morphology, (4) open web deployment generating fab-ready files. Anticipates: claims directed to inverse-design of double-emulsion droplet generators, ML-driven design automation for W/O/W and O/W/O architectures, and cloud-served device-design APIs covering both emulsion classes.
