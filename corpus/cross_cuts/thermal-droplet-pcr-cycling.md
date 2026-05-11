---
title: thermal-droplet-pcr-cycling
parent: Cross-cuts
layout: default
---

# Cross-cut: `thermal-droplet-pcr-cycling`

**8 corpus entries disclose this subsystem.**

Earliest disclosure: 1999

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Digital PCR (1999)

- **id**: `vogelstein-kinzler-1999-digital-pcr`
- **corpus**: academic
- **device class**: other
- **creator**: Vogelstein, Kinzler (Johns Hopkins)
- **disclosure**: Vogelstein, B.; Kinzler, K. W. Digital PCR. Proc. Natl. Acad. Sci. USA 1999, 96, 9236–9241. DOI: 10.1073/pnas.96.16.9236
- **ip status**: patented
- **prior art notes**: Disclosed digital PCR: dilute the template such that each well contains 0 or 1 copy, run end-point PCR, and count positive wells against Poisson distribution to obtain absolute copy number without a standard curve. Originally implemented in plate format. Anticipates: the entire digital-PCR concept that subsequently was implemented in droplets (Bio-Rad QX/RainDance), microwell arrays (Fluidigm), and chip arrays (Stilla, Thermo). The Bio-Rad QX ddPCR cartridge (separate entry) descends directly from this disclosure as a droplet-format implementation.

## RainDance Technologies DropMaker Patent Family (2002-06-28)

- **id**: `raindance-dropmaker-patent-family`
- **corpus**: private
- **device class**: droplet-generator
- **creator**: RainDance Technologies (acquired by Bio-Rad 2017-03-02)
- **disclosure**: US7708949 priority 2002-06-28; US8772046; US8500053; US8841071 (originally RainDance Technologies, now Bio-Rad)
- **ip status**: patented
- **prior art notes**: RainDance Technologies patent family covering picoliter-droplet generation in fluorinated-oil emulsions. Anchors claims around: (a) flow-focusing or T-junction generation of monodisperse aqueous droplets in fluorinated oil; (b) use of perfluorinated polyether surfactants to stabilize droplets against coalescence; (c) compatibility with PCR thermal cycling; (d) sample-encapsulation rates >1 kHz. Foundation patents acquired by Bio-Rad in March 2017 for approximately $72M (Bio-Rad 8-K 2017-02-01). Anticipates ddPCR / digital droplet-PCR cartridges and droplet-library generators. Existing companion entry raindance-bio-rad-acquisition documents the deal; this entry maps the licensable patent estate.

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

## 10x Genomics vs Bio-Rad Patent Litigation (RainDance basis) (2015-02-12)

- **id**: `tenx-vs-bio-rad-litigation`
- **corpus**: private
- **device class**: other
- **creator**: Bio-Rad Laboratories (plaintiff) vs 10x Genomics (defendant)
- **disclosure**: Bio-Rad Labs v. 10x Genomics, D.Del. 1:15-cv-00152 (filed 2015-02-12); jury verdict 2018-11-13 awarded $24M to Bio-Rad; later judgments, appeals, and 2020 settlement; subsequent N.D.Cal. cases
- **ip status**: patented
- **prior art notes**: Litigation entry. Bio-Rad sued 10x Genomics in D.Del. 1:15-cv-00152 (filed 2015-02-12) asserting RainDance-derived droplet patents (US7708949, US8273573, US8889083 and others) against the Chromium platform. Jury verdict 2018-11-13 awarded $24M with 15% royalty going forward. Multiple parallel cases followed in N.D.Cal. and at the ITC. Settled via cross-license arrangement around 2020. Defensive value: documents the most-litigated case in microfluidics history and establishes the legal interpretation of several RainDance/QuantaLife claim terms. Useful for any party defending against droplet-microfluidic claims.

## Bio-Rad ddPCR Patent Consolidation Position (post-RainDance 2017) (2017-03-02)

- **id**: `biorad-ddpcr-consolidation-position-2017`
- **corpus**: private
- **device class**: other
- **creator**: Bio-Rad Laboratories Inc.
- **disclosure**: Bio-Rad 8-K 2017-02-01 (RainDance acquisition close); Bio-Rad 10-K 2017 IP discussion; combined patent estate analysis
- **ip status**: patented
- **prior art notes**: Consolidation-position entry capturing the post-2017 Bio-Rad ddPCR patent landscape. By March 2017, Bio-Rad held: (a) QuantaLife-originated droplet-PCR patents (acquired 2011); (b) RainDance picoliter-droplet patents (acquired 2017); (c) Bio-Rad-internal continuations and improvements. This combined estate gave Bio-Rad a dominant negotiating position with all parties using droplet partitioning for nucleic-acid quantification, including 10x Genomics (single-cell), Stilla (Naica), Sysmex (RainDrop). Bio-Rad subsequently sued 10x Genomics under multiple counts of patent infringement (10x-genomics-vs-bio-rad-litigation entry below). Defensive value: a one-stop disclosure of the patent positions Bio-Rad used to anchor those suits.

## eVOLVER multi-bioreactor evolution platform (2018)

- **id**: `evolver-klavins`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Khalil group, Boston University
- **disclosure**: Wong, B. G.; Mancuso, C. P.; Kiriakov, S.; Bashor, C. J.; Khalil, A. S. Precise, automated control of conditions for high-throughput growth of yeast and bacteria with eVOLVER. Nat. Biotechnol. 2018, 36, 614–623. DOI: 10.1038/nbt.4151
- **ip status**: open-permissive
- **prior art notes**: Open-hardware 16-vessel parallel bioreactor system with per-vessel temperature, OD, stirring, and feed control. Designed for laboratory directed-evolution and high-throughput growth experiments. Anticipates: massively-parallel addressable bioreactor architecture, open-source bioreactor scaling, and the experimental-evolution use case at academic-budget price points.

## Mission Bio Tapestri PRIM (Pre-Integrated Multi-omics) (2024)

- **id**: `mission-bio-tapestri-prim-2024`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Mission Bio Inc.
- **disclosure**: Mission Bio Tapestri PRIM announcement 2024; product brief; US10745742B2 (Tapestri Two-step encapsulation)
- **ip status**: patented
- **prior art notes**: Discloses extension of Tapestri two-step droplet workflow to add ATAC chromatin accessibility measurement alongside DNA + protein on the same cell. Anticipates: combined DNA + protein + chromatin single-cell assays delivered through two-step droplet encapsulation in a sealed plastic cartridge; sequential picoinjection-based reagent addition for multi-omic single-cell library construction.
