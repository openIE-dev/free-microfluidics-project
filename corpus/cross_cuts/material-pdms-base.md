---
title: material-pdms-base
parent: Cross-cuts
layout: default
---

# Cross-cut: `material-pdms-base`

**8 corpus entries disclose this subsystem.**

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

## PDMS-Glass Plasma Bonding Methodology Patent Family (1999)

- **id**: `whitesides-patent-pdms-glass-plasma-bonding`
- **corpus**: academic
- **device class**: other
- **creator**: President and Fellows of Harvard College (Whitesides group)
- **disclosure**: Method disclosed in Duffy et al. Anal. Chem. 1998 (doi:10.1021/ac980656z) and Whitesides-group continuations; no enforceable composition-of-matter patent broadly asserted; covered in US6645432 (related apparatus) and Harvard practice notes
- **ip status**: public-domain
- **prior art notes**: Defensive entry recording the PDMS-glass oxygen-plasma bonding methodology as effectively public-domain. Anchors negative-claim status that: (a) exposing PDMS surface to O2 or air plasma to generate silanol groups; (b) bringing such activated surface into contact with similarly treated borosilicate glass; (c) forming Si-O-Si covalent bonds creating an irreversible, leak-tight seal — none of these are validly patentable in 2026 because the technique was disclosed in Duffy 1998 and was widely practiced before the priority date of any later assertion. Defensive value: any patent attempting to claim O2-plasma PDMS-glass bonding can be invalidated by Duffy 1998 plus this disclosure timestamp. Cited apparatus patent US6645432 covers a specific plasma-chamber implementation, not the general method.

## Quake Lab MLSI Monolithic Membrane Valve Patent Family (2000-04-07)

- **id**: `quake-patent-family-mlsi-monolithic-membrane-valve`
- **corpus**: academic
- **device class**: other
- **creator**: California Institute of Technology (Stephen Quake et al.)
- **disclosure**: US6408878 priority 2000-04-07; US6929030; US7144616; US7704698; US7837946 (Caltech)
- **ip status**: patented
- **prior art notes**: Caltech/Quake monolithic-membrane valve patent family. Anchors claims around: (a) two-layer PDMS device in which a flow channel is occluded by deflection of a thin elastomeric membrane via pressurization of an orthogonal control channel; (b) push-down geometry where the control channel sits above the flow channel; (c) push-up geometry where the control channel sits below; (d) integration of large arrays of such valves on a single monolithic device (microfluidic large-scale integration); (e) peristaltic pump architectures using three valves in series; (f) multiplexer trees that address N flow lines with log2(N) control lines. These claims are the licensing root that Fluidigm built its IFC controller, BioMark dynamic array, Access Array, C1 single-cell, and Helios CyTOF business on. Anticipates virtually any PDMS multilayer monolithic valve device unless distinguished by materials (non-PDMS), actuation (non-pneumatic), or geometry (non-membrane closure). Defensive importance: the underlying Unger 2000 paper (already in corpus as unger-2000-quake-monolithic-membrane-valve) is the academic disclosure; this entry is the patent-family disclosure that maps the asserted claim landscape. Earliest US priority is 2000-04-07. Estimated US expiry 2020-2025 depending on family member.

## Quake Lab Droplet Flow-Focusing Patent Family (2003-09-15)

- **id**: `quake-patent-family-droplet-flow-focusing`
- **corpus**: academic
- **device class**: droplet-generator
- **creator**: President and Fellows of Harvard College (Anna, Bontoux, Stone, Quake)
- **disclosure**: US7268167 priority 2003-09-15; US7375085; both assigned originally to President and Fellows of Harvard College
- **ip status**: patented
- **prior art notes**: Harvard-anchored patent family covering hydrodynamic flow-focusing droplet generation. Anchors claims around: (a) a microfluidic device with an inner phase channel meeting two outer continuous-phase channels at an orifice; (b) generation of monodisperse droplets via Rayleigh-Plateau breakup at the orifice; (c) independent control of droplet diameter via continuous-phase flow rate while inner-phase flow rate sets generation frequency; (d) chip geometry compatible with PDMS soft lithography. Anticipates flow-focusing droplet-generator chips in microfluidic context. Underlying Anna 2003 paper (anna-2003-flow-focusing-droplet) is the published companion. The patent family was a precursor for the licensing chains that fed RainDance, QuantaLife, and 10x Genomics droplet platforms. Expiry: ~2023-2024 for earliest members, but continuations may extend coverage on specific geometries.

## Wilson Wolf G-Rex gas-permeable bioreactor (2007)

- **id**: `wilson-wolf-grex`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Wilson Wolf Manufacturing
- **disclosure**: Vera, J.F. et al. Accelerated production of antigen-specific T cells for preclinical and clinical applications using gas-permeable rapid expansion cultureware (G-Rex). J. Immunother. 2010, 33(3):305-15. doi:10.1097/CJI.0b013e3181c0c3cb. Earlier disclosure: US7745209B2 (Wilson, J.; priority 2005).
- **ip status**: patented
- **prior art notes**: Discloses a closed gas-permeable cell-culture vessel using a thin silicone bottom membrane to permit O2/CO2 transfer from below while supporting a deep static medium column above the cells. Enables T-cell expansion at densities and absolute cell numbers an order of magnitude beyond conventional flask geometries without active pumping or perfusion. Anticipates: (a) gas-permeable membrane bottoms for closed cell-therapy expansion vessels; (b) static-perfusion-free CAR-T expansion architecture; (c) integrated Luer-and-tubing harness for closed-system aseptic transfer between expansion vessel and downstream wash/concentrate steps. As nominal architectural ancestor to G-Rex-equivalent compartments inside Lonza Cocoon, Cellares Cell Shuttle, and Miltenyi CliniMACS Prodigy, the G-Rex line is the workhorse for academic and most commercial CAR-T expansion.

## Replenish Inc. Ophthalmic MEMS Drug Delivery Micropump (2008)

- **id**: `replenish-mems-ophthalmic-micropump`
- **corpus**: private
- **device class**: pump-component
- **creator**: Replenish Inc. (USC Doheny / Meng spin-out)
- **disclosure**: Lo R, Li PY, Saati S, Agrawal RN, Humayun MS, Meng E Biomed Microdevices 11(5):959-970 2009 doi:10.1007/s10544-009-9313-9
- **ip status**: patented
- **prior art notes**: Discloses a fully implantable ophthalmic micropump in which an electrolysis pair generates gas that deflects a parylene/silicone membrane separating the gas chamber from a drug reservoir, expelling sub-microliter drug volumes through a tubing cannula into the vitreous humor via a passive check valve. Anticipates: electrolysis-actuated implantable micropump architectures; nanoliter-resolution chronic ophthalmic drug delivery; parylene-C as combined fluidic and membrane material in implants.

## ForSight Vision5 Helios Bimatoprost Insert (Periocular Ring) (2014-10-30)

- **id**: `forsight-vision5-helios-ring`
- **corpus**: private
- **device class**: other
- **creator**: ForSight Vision5 Inc.
- **disclosure**: Brandt JD et al. Ophthalmology 123(8):1685-1694 2016 doi:10.1016/j.ophtha.2016.04.026; ForSight Vision5 patent family
- **ip status**: patented
- **prior art notes**: Comparator entry. Not a true microfluidic device but interfaces directly with the tear-film microfluidic at the ocular surface, releasing bimatoprost by zero-order diffusion. Anticipates: drug-eluting periocular ring architectures and the topology of using tear-film natural microfluidics as the distribution layer.
