---
title: cell-encapsulation-droplet
parent: Cross-cuts
layout: default
---

# Cross-cut: `cell-encapsulation-droplet`

**8 corpus entries disclose this subsystem.**

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

## 10x Genomics Chromium controller and Next GEM chip (2016)

- **id**: `10x-genomics-chromium-controller`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: 10x Genomics
- **disclosure**: 10x Genomics Chromium platform; product literature and Zheng et al. 2017 Nat. Commun. 8, 14049. DOI: 10.1038/ncomms14049
- **ip status**: patented
- **prior art notes**: Commercial single-cell encapsulation platform: Chromium controller drives flow-focusing geometry on a disposable Next GEM chip, co-encapsulating cells with barcoded gel beads in droplets for downstream sequencing. Anticipates: high-throughput parallel droplet generation in a disposable thermoplastic cartridge driven by an instrument-side pneumatic pressure source, the gel-bead-in-droplet architecture for barcoded single-cell genomics, and the integration of microfluidic droplet generation with a turnkey commercial instrument workflow. Encumbered by an aggressive patent thicket; corpus entry exists to enable invalidity analysis.

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
