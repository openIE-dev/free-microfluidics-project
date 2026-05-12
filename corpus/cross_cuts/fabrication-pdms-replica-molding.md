---
title: fabrication-pdms-replica-molding
parent: Cross-cuts
layout: default
---

# Cross-cut: `fabrication-pdms-replica-molding`

**6 corpus entries disclose this subsystem.**

Earliest disclosure: 1996-12-12

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Whitesides Soft Lithography Patent Family (1996-12-12)

- **id**: `whitesides-patent-family-soft-lithography`
- **corpus**: academic
- **device class**: printer-tooling
- **creator**: President and Fellows of Harvard College (George Whitesides et al.)
- **disclosure**: US6033928 priority 1996-12-12; US6322951; assigned to President and Fellows of Harvard College
- **ip status**: patented
- **prior art notes**: Harvard/Whitesides foundational soft-lithography patent family. Anchors claims around: (a) replica molding of an elastomeric stamp from a master patterned by photolithography; (b) microcontact printing of a self-assembled monolayer using the stamp; (c) use of PDMS as the elastomer; (d) fabrication of microfluidic structures by sealing a molded PDMS slab against a flat substrate. Companion academic disclosures already in corpus: duffy-1998-pdms-soft-lithography-microfluidics, xia-whitesides-1998-soft-lithography-review, kumar-whitesides-1993-microcontact-printing. Expiry: 2016-2018 for earliest members; the bulk of the technique is now public domain. Defensive: any entity asserting against PDMS replica molding faces 25+ years of public-domain prior art.

## Rapid prototyping of microfluidic systems in PDMS (1998)

- **id**: `duffy-1998-pdms-soft-lithography-microfluidics`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Whitesides group, Harvard
- **disclosure**: Duffy, D. C.; McDonald, J. C.; Schueller, O. J. A.; Whitesides, G. M. Rapid prototyping of microfluidic systems in poly(dimethylsiloxane). Anal. Chem. 1998, 70, 4974–4984. DOI: 10.1021/ac980656z
- **ip status**: public-domain
- **prior art notes**: The paper that turned PDMS soft lithography into the default microfluidics fabrication method for the next 25+ years. Anticipates: SU-8 master mold + PDMS replica casting, oxygen-plasma bonding of PDMS to glass or PDMS, hydrophilic surface treatment by plasma oxidation, and rapid-prototyping iteration of channel designs. Any patent claiming novelty over 'PDMS replica molding from a photoresist master with plasma bonding to substrate' must address this disclosure.

## Quake Lab MLSI Monolithic Membrane Valve Patent Family (2000-04-07)

- **id**: `quake-patent-family-mlsi-monolithic-membrane-valve`
- **corpus**: academic
- **device class**: other
- **creator**: California Institute of Technology (Stephen Quake et al.)
- **disclosure**: US6408878 priority 2000-04-07; US6929030; US7144616; US7704698; US7837946 (Caltech)
- **ip status**: patented
- **prior art notes**: Caltech/Quake monolithic-membrane valve patent family. Anchors claims around: (a) two-layer PDMS device in which a flow channel is occluded by deflection of a thin elastomeric membrane via pressurization of an orthogonal control channel; (b) push-down geometry where the control channel sits above the flow channel; (c) push-up geometry where the control channel sits below; (d) integration of large arrays of such valves on a single monolithic device (microfluidic large-scale integration); (e) peristaltic pump architectures using three valves in series; (f) multiplexer trees that address N flow lines with log2(N) control lines. These claims are the licensing root that Fluidigm built its IFC controller, BioMark dynamic array, Access Array, C1 single-cell, and Helios CyTOF business on. Anticipates virtually any PDMS multilayer monolithic valve device unless distinguished by materials (non-PDMS), actuation (non-pneumatic), or geometry (non-membrane closure). Defensive importance: the underlying Unger 2000 paper (already in corpus as unger-2000-quake-monolithic-membrane-valve) is the academic disclosure; this entry is the patent-family disclosure that maps the asserted claim landscape. Earliest US priority is 2000-04-07. Estimated US expiry 2020-2025 depending on family member.

## OpenWetWare Community Wiki (2005)

- **id**: `openwetware-mit-wiki`
- **corpus**: open
- **device class**: other
- **creator**: MIT (Knight T., Endy D., Smolke C., et al.); OpenWetWare community
- **disclosure**: OpenWetWare launched May 2005 at MIT by Knight T., Endy D., et al.; https://openwetware.org; foundational paper Bobe J., Endy D., 'OpenWetWare: a wiki for sharing biology lab protocols', Yeast 24:s223 (2007)
- **ip status**: open-permissive
- **prior art notes**: Discloses a long-running open protocol archive whose documented procedures for soft lithography, PDMS microfluidic fabrication, paper microfluidics, and on-chip cell culture, with timestamped wiki edit-histories from 2005 onward, are themselves citable prior art. Specifically anticipates protocol claims in many post-2010 patents for 'methods of fabricating PDMS microfluidic devices,' 'methods of bonding PDMS to glass,' and 'protocols for cell culture in microfluidic devices' to the extent these claims read on the OWW protocol pages timestamped before the patent's earliest priority date. Cite OWW page revision URLs (https://openwetware.org/index.php?title=...&oldid=...) for entry-specific anticipation.

## Soft lithography for micro- and nanoscale patterning (Qin, Xia & Whitesides, Nature Protocols, 2010) (2010-03)

- **id**: `whitesides-2010-nature-protocols-pdms-fabrication`
- **corpus**: academic
- **device class**: printer-tooling
- **creator**: Dong Qin, Younan Xia, George M. Whitesides, Harvard
- **disclosure**: Qin, D.; Xia, Y.; Whitesides, G. M. Soft lithography for micro- and nanoscale patterning. Nat. Protoc. 2010, 5 (3), 491-502. DOI: 10.1038/nprot.2009.234.
- **ip status**: public-domain
- **prior art notes**: The widely-followed step-by-step protocol that codified PDMS soft-lithography microfabrication for non-specialist laboratories - the de facto foundry recipe behind a large fraction of academic microfluidic devices. Discloses, in reproducible detail: photomask layout and printing; SU-8 photoresist master fabrication on silicon with feature heights from a few microns to hundreds of microns; degassed-PDMS casting, curing, and demolding; oxygen-plasma activation and irreversible PDMS-glass and PDMS-PDMS bonding; inlet/outlet punching and tubing interfacing; and multilayer alignment for valve chips. Anticipates claims to: standardized PDMS replica-molding microfluidic fabrication workflows; plasma-bonded PDMS-glass channel sealing; SU-8-master-defined microchannel geometries; and the generic rapid-prototyping foundry process. Distinct from existing duffy-1998-pdms-soft-lithography-microfluidics, xia-whitesides-1998-soft-lithography-review, mcdonald-whitesides-2002-pdms-review, and whitesides-2010-mu-pads-systematic; cross-referenced as the published protocol node of the Whitesides soft-lithography lineage (the patented aspects are covered by whitesides-patent-family-soft-lithography).

## 1CellBio inDrop Commercial Reagent System (2017)

- **id**: `1cellbio-indrops-commercial-extension`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: 1CellBio Inc.
- **disclosure**: 1CellBio inDrop product launch 2017; Klein et al., Cell 161:1187 (2015) doi:10.1016/j.cell.2015.04.044 (academic origin)
- **ip status**: patented
- **prior art notes**: Discloses the commercial productization of the inDrops academic protocol including hydrogel-bead format barcoded primer release via UV photo-cleavage in droplet. Anticipates: photo-cleavable barcoded hydrogel beads as droplet co-encapsulation reagents; UV-triggered primer release inside droplets for single-cell RT initiation.
