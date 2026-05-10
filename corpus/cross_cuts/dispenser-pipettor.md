---
title: dispenser-pipettor
parent: Cross-cuts
layout: default
---

# Cross-cut: `dispenser-pipettor`

**6 corpus entries disclose this subsystem.**

Earliest disclosure: 1990

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## MicroFab MJ-AT/MJ-AB Piezo-Driven Drop-on-Demand Dispenser Head (1990)

- **id**: `microfab-mj-at-piezo-on-demand-dispenser`
- **corpus**: private
- **device class**: dispenser-pipettor
- **creator**: MicroFab Technologies, Inc.
- **disclosure**: MicroFab Technologies Inc. (Plano, TX) JetLab and MJ-series datasheets; microfab.com; founder David B. Wallace
- **ip status**: patented
- **prior art notes**: Note: an existing microfab-piezo-droplet-dispenser corpus entry exists; this entry pins specific MJ-AT/MJ-AB product lines and the JetLab platform. Discloses a glass-tube DOD dispenser with a radial piezo annulus around a drawn borosilicate glass capillary terminating in a precision orifice (typically 30–80 µm), driven by tunable bipolar waveforms to produce satellite-free single droplets in the 10 pL to 200 pL range. Anticipates: (a) the standard 'research-grade DOD dispenser' format used by virtually all academic inkjet-printing labs, (b) bipolar waveform shaping for satellite suppression, (c) coupled XY-stage (JetLab) platform as a flexible R&D inkjet workbench. Predicate to many subsequent commercial dispensers including SciTech Korea SPJ-100 and TTP Mosquito-derived heads.

## Vanrx SA25 Aseptic Filling Workcell (now Cytiva Microcell Vial Filler) (2015)

- **id**: `vanrx-sa25-aseptic-workcell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Vanrx Pharmasystems Inc. (acquired 2021 by Cytiva)
- **disclosure**: Vanrx Pharmasystems SA25 product launch 2015; US patent US10,723,492B2 (Apparatus and method for aseptic processing, Vanrx, priority 2014); Vanrx acquired by Cytiva 2021-09
- **ip status**: patented
- **prior art notes**: Discloses a robotic aseptic-filling workcell in which pre-sterilized nested RTU vials are handled by a robot inside a VHP-decontaminated isolator; a peristaltic-pump-driven fill train dispenses through a sterile needle (or needle-less) into vials with closed-loop volume control; vials are sealed and crimped within the isolator. Anticipates: robotic gloveless aseptic vial-filling architecture (distinct from rotary filling lines which require human intervention or open transfers); pre-sterilized nested vial format integrated with robotic handling; sub-mL precision fill suitable for small-batch CGT products. Element-by-element: nested vial input + VHP isolator + robot gripper + peristaltic fill train + sterile needle/no-needle dispense + crimp seal + output magazine.

## Twist Bioscience Cell Engineering (Twist Cellomics) (2016)

- **id**: `twist-bioscience-cellomics`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Twist Bioscience Corp.
- **disclosure**: Twist Bioscience S-1 SEC filing 2018; Twist silicon DNA synthesis patent estate US10,384,189B2 (Methods for nucleic acid assembly and high throughput sequencing, priority 2014)
- **ip status**: patented
- **prior art notes**: Discloses a silicon substrate with parallel addressable reaction wells in which phosphoramidite DNA synthesis runs at scale; reagents are routed by integrated microfluidic distribution and printhead-style deposition; output oligos are pooled or selectively retrieved. The Cellomics extension packages synthesized variant libraries with downstream cell-line generation services. Anticipates: silicon-substrate massively-parallel DNA synthesis (distinct from Agilent inkjet-on-glass and from solid-phase column synthesis); subsequent integration of synthesis with cell-line variant manufacturing as a single offering. Element-by-element: silicon reaction-well array + reagent printhead + deprotection/washing fluidics + library retrieval + downstream cell engineering.

## Syntegon Versynta Microbatch / Combotec Filler (2017)

- **id**: `syntegon-versynta-microbatch-filler`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Syntegon Technology GmbH (formerly Bosch Packaging Technology)
- **disclosure**: Bosch Packaging Technology Versynta microbatch product launch 2017 (Bosch Pharma division spun out as Syntegon 2020); Syntegon product literature 2020-2023; EP3437985A1
- **ip status**: patented
- **prior art notes**: Discloses a robotic aseptic-fill workcell targeted at micro-batch / personalized-medicine throughput: robot handles nested RTU vials inside an H2O2-decontaminated isolator; peristaltic-pump dosing manifold dispenses through sterile needles; multi-format adaptability (vials, syringes, cartridges) via tool-changer end-effector. Anticipates: small-batch robotic aseptic filling architecture optimized for sub-1000 vial runs (distinguishable from high-throughput rotary fillers); multi-format dosing in a single workcell. Closely architecturally related to Vanrx SA25 (Cytiva); distinguishable by the multi-format end-effector tooling.

## Synthego CRISPR ePool / Eclipse Platform (2018)

- **id**: `synthego-crispr-epool`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Synthego Corp.
- **disclosure**: Synthego ePool product introduction 2018; Synthego Eclipse Platform whitepaper 2019; US patent application US20200056164A1 (Synthego)
- **ip status**: patented
- **prior art notes**: Discloses a high-throughput sgRNA synthesis architecture in which proprietary chemistry runs on multi-well plates with automated liquid handling; output is QC'd and shipped as either pooled (ePool) or arrayed (single-well) guide libraries. Anticipates: factory-format CRISPR guide manufacturing where the design-to-deliver loop is fully software-defined; combined design-software + plate-format synthesis + QC + shipment of guide libraries against user-specified targets. Note: instrument internals are largely trade-secret; entry strength rests on product literature and pending patent application.

## Thermo Fisher Neon NxT Electroporator (2022)

- **id**: `thermofisher-neon-nxt-electroporator`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Thermo Fisher Scientific (Invitrogen)
- **disclosure**: Thermo Fisher Scientific Neon NxT product launch press release 2022-09; Neon NxT user guide MAN0019022 rev 2.0; predecessor Neon Transfection System (Invitrogen, ~2009) US patent US8,008,065B2 (Pipette-tip-based electroporation)
- **ip status**: patented
- **prior art notes**: Discloses an electroporation device in which the cell suspension is held within a disposable pipette tip whose lower bore contains the field-defining electrodes; aspiration draws cells between the electrodes; the pulse generator fires across the tip electrodes; cells are then dispensed into culture vessels. Anticipates: pipette-tip-format electroporation (distinct from cuvette format), parallelization by multi-channel head, instrument-disposable separation. The NxT update adds 3-channel parallelism and a redesigned electrode tip; underlying electrode-in-pipette architecture is the Invitrogen Neon parent.
