---
title: cell-encapsulation-droplet
parent: Cross-cuts
layout: default
---

# Cross-cut: `cell-encapsulation-droplet`

**18 corpus entries disclose this subsystem.**

Earliest disclosure: 2007

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Microfluidic alginate microbead generation (2007)

- **id**: `choi-weitz-2007-alginate-microbead`
- **corpus**: academic
- **device class**: droplet-generator
- **creator**: various — Lee, Weitz, Doyle (early 2000s contributions)
- **disclosure**: Choi, C.-H.; Jung, J.-H.; Rhee, Y. W.; Kim, D.-P.; Shim, S.-E.; Lee, C.-S. Generation of monodisperse alginate microbeads and in situ encapsulation of cell in microfluidic device. Biomed. Microdevices 2007, 9, 855–862. DOI: 10.1007/s10544-007-9098-7
- **ip status**: patented
- **prior art notes**: Foundational disclosure of microfluidic alginate microbead generation: aqueous alginate flow-focused into oil with downstream calcium-mediated gelation produces monodisperse alginate microbeads suitable for cell encapsulation. Anticipates: alginate-as-microbead-substrate-in-droplet-microfluidics, which became the backbone of single-cell sequencing platforms (Drop-seq, inDrops, Tapestri) where the bead encapsulates barcoding oligos.

## Organovo NovoGen MMX Bioprinter Dual Extrusion Bioprinthead (2009)

- **id**: `organovo-novogen-mmx-bioprinter-dual-head`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Organovo Inc. with Invetech Pty Ltd (Australia)
- **disclosure**: Organovo / Invetech NovoGen MMX commercial introduction 2009; PMC 'arrival of commercial bioprinters' review (PMC7582003); US patent portfolio commencing US7651665
- **ip status**: patented
- **prior art notes**: Discloses a bioprinter with two extrusion-style printheads, each comprising a glass capillary fitted with a motorized metallic piston that aspirates a cell-laden hydrogel (e.g., PEGDA, alginate) and subsequently dispenses it under coordinated motion of an X-Z stage; an integrated UV/light source crosslinks the deposited fiber. Anticipates: (a) dual-head extrusion bioprinting with one head for support material and one for cell-laden ink, (b) piston-in-capillary as the cell-friendly displacement primitive, (c) inline crosslink step coupled to the motion path. Predicate to subsequent commercial bioprinters from CELLINK, RegenHU, Aspect, T&R Biofab, and others, all of which iterate on this multi-head extrusion architecture.

## OpenPlant — Cambridge / John Innes Synthetic-Biology Initiative (2014-09)

- **id**: `openplant-cambridge-norwich-synthetic`
- **corpus**: open
- **device class**: other
- **creator**: Haseloff lab (U of Cambridge), Patron lab (Earlham/John Innes), Sainsbury Laboratory
- **disclosure**: OpenPlant Initiative launched September 2014; BBSRC/EPSRC Synthetic Biology Research Centre award; https://www.openplant.org; founding paper: Patron N.J. et al., 'Standards for plant synthetic biology', New Phytologist 208 (2015) 13-19, doi:10.1111/nph.13532
- **ip status**: open-permissive
- **prior art notes**: Discloses an open synthetic-biology initiative and parts library specifically chartered to release reagents, protocols, and tools under permissive licenses. Relevance to microfluidics: OpenPlant publishes open protocols for protoplast generation and single-cell microfluidic encapsulation in Marchantia and Arabidopsis, and partners with the Cambridge biomakespace on shared microfluidic equipment. Anticipates: open distribution models for synthetic-biology kits including microfluidic protocols for protoplast handling; the institutional pattern of releasing both wet-lab parts and instrument designs under aligned open licenses.

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

## T&R Biofab IB3D / 3DX Multi-Head Bioprinter (2015)

- **id**: `tr-biofab-ib3d-bioprinter`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: T&R Biofab Co., Ltd. (Suwon, South Korea); founded by Prof. Dong-Woo Cho's POSTECH group
- **disclosure**: T&R Biofab Co., Ltd. (Korea) IB3D / 3DX product line; tnrbiofab.com; commercial release ~2015
- **ip status**: patented
- **prior art notes**: Discloses a multi-head bioprinter integrating thermoplastic-extrusion heads (PCL/PLGA scaffold material at melt temperature) with cell-laden hydrogel bioprinting heads (dECM, alginate, GelMA), enabling simultaneous deposition of structural scaffold and cellular components. Anticipates: (a) hybrid melt-extrusion plus low-temperature bioink architecture in a single machine, (b) dECM-bioink workflow productized into a commercial machine (lineage to Cho 2014 dECM Nature Communications paper), (c) Korean-origin bioprinter prior art for industrial scaffold-plus-cell platforms. Note: corpus already references POSTECH microfluidics broadly via postech-microfluidics-suh; this entry pins T&R Biofab specifically.

## 10x Genomics Chromium controller and Next GEM chip (2016)

- **id**: `10x-genomics-chromium-controller`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: 10x Genomics
- **disclosure**: 10x Genomics Chromium platform; product literature and Zheng et al. 2017 Nat. Commun. 8, 14049. DOI: 10.1038/ncomms14049
- **ip status**: patented
- **prior art notes**: Commercial single-cell encapsulation platform: Chromium controller drives flow-focusing geometry on a disposable Next GEM chip, co-encapsulating cells with barcoded gel beads in droplets for downstream sequencing. Anticipates: high-throughput parallel droplet generation in a disposable thermoplastic cartridge driven by an instrument-side pneumatic pressure source, the gel-bead-in-droplet architecture for barcoded single-cell genomics, and the integration of microfluidic droplet generation with a turnkey commercial instrument workflow. Encumbered by an aggressive patent thicket; corpus entry exists to enable invalidity analysis.

## CELLINK BIO X Pneumatic Bioprinthead (2016)

- **id**: `cellink-bio-x-pneumatic-printhead`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: CELLINK AB (Gothenburg, Sweden); now part of BICO Group
- **disclosure**: CELLINK BIO X 3D Bioprinter user manual (documents.thermofisher.com/TFS-Assets/ANZ/manuals/cellink-biox-3d-bioprinter-manual.pdf); BIO X pneumatic-printhead product page (cellink.com/product/bio-x-pneumatic-printhead/)
- **ip status**: patented
- **prior art notes**: Discloses a modular pneumatic bioprinthead that mounts on the BIO X bioprinter and accepts disposable polymer cartridges (3 mL or 10 mL) holding cell-laden bioink, with regulated external air pressure as the displacement actuator and an integrated heater on the cartridge wall (up to 65 °C) for temperature-sensitive bioinks. Anticipates: (a) modular swappable head architecture for multi-modal bioprinting on a single base machine (CELLINK BIO X / BIO X6 / BIONOVA) — concrete prior art against later 'modular bioprinter' claims, (b) disposable closed-cartridge bioink supply with integrated heater, (c) external-pneumatic actuation as a cell-friendly drive primitive. The head IS the microfluidic device — defining feature is per-cartridge pressure regulation feeding a small-bore needle producing extruded fibers ranging from ~100 µm to >1 mm.

## 1CellBio inDrop platform (commercial inDrops) (2016)

- **id**: `1cellbio-indrops-commercial`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: 1CellBio Inc.
- **disclosure**: 1CellBio inDrop System commercial release 2016. https://1cell-bio.com/. Klein, A. M. et al. Droplet barcoding for single-cell transcriptomics applied to embryonic stem cells. Cell 2015, 161, 1187-1201. DOI: 10.1016/j.cell.2015.05.044.
- **ip status**: patented
- **prior art notes**: Commercial implementation of inDrops (Klein 2015): single cells co-encapsulated with photo-cleavable hydrogel barcoded beads in a PDMS flow-focusing chip driven by external syringe pumps. Anticipates: the academic-spinout commercialization path for single-cell barcoding, the use of dissolvable hydrogel beads as barcode carriers (vs. solid beads in Drop-seq), and the lower-cost open-architecture alternative to 10x Chromium. Many academic labs run this directly off the Klein 2015 paper without 1CellBio hardware.

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

## Mission Bio Tapestri single-cell DNA sequencing (2018)

- **id**: `mission-bio-tapestri`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Mission Bio
- **disclosure**: Mission Bio Tapestri platform. https://missionbio.com/tapestri/
- **ip status**: patented
- **prior art notes**: Two-step droplet workflow for single-cell DNA sequencing: cells encapsulated, lysed, and tagged in primary droplets; PCR products extracted and re-emulsified for amplicon sequencing. Anticipates: serial-emulsion architecture in single-cell genomics workflows, distinguishing Mission Bio's IP position from 10x Genomics' single-emulsion approach.

## Microfluidic cell therapy manufacturing (CAR-T scale-up) (2018)

- **id**: `microfluidic-cell-therapy-manufacturing`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: various — Melosh lab Stanford / commercial CAR-T
- **disclosure**: Tay, A.; Melosh, N. Mechanical stimulation after centrifuge-free nanoelectroporation drastically improves cell viability and gene transfer. Nano Lett. 2017, 17, 886–892. (And subsequent commercial CAR-T cell-therapy microfluidic platforms.)
- **ip status**: patented
- **prior art notes**: Recent academic and commercial work on microfluidic cell therapy manufacturing: T cell activation, transfection, and expansion in flow-through microfluidic devices for CAR-T and other adoptive cell therapies. Anticipates: closed-system microfluidic cell therapy manufacturing platforms (e.g., Cellares, Lonza Cocoon) that integrate microfluidic-equivalent cell handling at GMP scale.

## Microfluidic electroporation for cell therapy manufacturing (2018)

- **id**: `microfluidic-electroporation-cell-therapy`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: Various — Sharei (SQZ), Kwong, Melosh labs
- **disclosure**: Various publications on microfluidic mechanical and electrical-poration for non-viral gene delivery to cells. Representative: SQZ Biotechnologies cell-squeeze platform; Kwong et al. 2014 Nano Lett. for nanoneedle approach.
- **ip status**: patented
- **prior art notes**: Microfluidic constriction-based mechanical poration: cells passing through narrow constriction transiently form membrane pores, allowing delivery of macromolecules without electrical field. Architectural alternative to electroporation for non-viral cell engineering. Underlies SQZ Biotechnologies (acquired 2024) and several academic spinout efforts.

## Parse Biosciences Evercode split-pool single-cell kit (2018-04-13)

- **id**: `parse-biosciences-evercode`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Parse Biosciences (formerly Split Biosciences)
- **disclosure**: Rosenberg, A. B. et al. Single-cell profiling of the developing mouse brain and spinal cord with split-pool barcoding. Science 2018, 360, 176-182. DOI: 10.1126/science.aam8999. Parse Biosciences (Split Biosciences) commercial launch 2019.
- **ip status**: patented
- **prior art notes**: Combinatorial split-pool barcoding kit derived from the SPLiT-seq method (Rosenberg & Roco 2018). Each cell or nucleus is fixed and permeabilized, then distributed across plate wells through 3-4 sequential rounds of in-cell barcode oligo ligation/RT; the cell itself is the compartment, no droplet generator or microwell chip is required. Anticipates: instrument-free, plate-based combinatorial single-cell barcoding architectures; fixable-sample workflows for single-cell RNA-seq that decouple sample collection from library prep; the architectural distinction from 10x Chromium (no droplet microfluidics, only multichannel pipettors and 96-well plates) enabling sub-$1 per-cell economics at >100k cell scale. Also anticipates instrument-side passive fluidic handling consisting solely of plate transfer and centrifugation.

## Scale Biosciences single-cell split-pool kit (2022)

- **id**: `scale-bio-split-pool-kit`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Scale Biosciences
- **disclosure**: Scale Biosciences product launch 2022. https://scale.bio/. Founders from Cellular Research / BD lineage.
- **ip status**: patented
- **prior art notes**: Plate-based 3-round combinatorial-indexing kit for single-cell RNA, ATAC, and methylation. Each round of indexing distributes fixed nuclei across 96 or 384 wells; total barcode space grows multiplicatively (>10^7). Anticipates: combinatorial indexing as a scaling strategy that bypasses droplet-microfluidic single-cell instruments; multi-omic single-cell prep using the same combinatorial backbone. Distinguishes from Parse Evercode by emphasis on epigenomic assays (ATAC, methylation) in addition to RNA.

## Fluent BioSciences PIPseq particle-templated emulsification (2022-02-01)

- **id**: `fluent-biosciences-pipseq`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Fluent BioSciences
- **disclosure**: Clark, I. C. et al. Microfluidics-free single-cell genomics with templated emulsification. Nat. Biotechnol. 2023, 41, 1557-1566. DOI: 10.1038/s41587-023-01685-z. Fluent BioSciences product launch 2022.
- **ip status**: patented
- **prior art notes**: PIPseq replaces flow-focusing droplet generation with templated emulsification: pre-formed hydrogel particles carrying barcoded oligos are mixed with cells and oil in a tube, then vortexed; the hydrogel particle becomes the template that nucleates a uniform aqueous droplet around each particle. Anticipates: chip-free droplet-template emulsification for single-cell barcoding, reducing the sample-prep instrument to a vortexer. Major prior-art consequence: invalidates broad claims requiring 'microfluidic flow-focusing' as the necessary droplet-generation mechanism for high-throughput single-cell barcoding. Originated in the Adam Abate lab (UCSF).
