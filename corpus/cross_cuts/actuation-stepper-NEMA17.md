---
title: actuation-stepper-NEMA17
parent: Cross-cuts
layout: default
---

# Cross-cut: `actuation-stepper-NEMA17`

**3 corpus entries disclose this subsystem.**

Earliest disclosure: 2014-09-16

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Pearce-lab Open Syringe Pump v2 — Large-Format / NEMA17 Variant (2014-09-16)

- **id**: `wijnen-pearce-2014-syringe-pump-v2-12mm`
- **corpus**: open
- **device class**: pump-component
- **creator**: B. Wijnen, E.J. Hunt, G.C. Anzalone, J.M. Pearce (Michigan Tech)
- **disclosure**: Wijnen B, Hunt EJ, Anzalone GC, Pearce JM. Open-Source Syringe Pump Library. PLoS ONE 9(9): e107216 (2014). doi:10.1371/journal.pone.0107216 — Library defines two motor-class variants (NEMA11 and NEMA17) yielding distinct max flow rates; this entry covers the NEMA17 high-flow large-format variant.
- **ip status**: open-copyleft
- **prior art notes**: Distinguished from the NEMA11 small-format variant (covered separately by wave 1's wijnen-pearce-2014-open-syringe-pump entry as the umbrella library disclosure), this entry defends the high-flow NEMA17-driven implementation explicitly disclosed in the same paper. Element-by-element: (1) FDM-printed two-rail frame with leadscrew + NEMA17 stepper; (2) plunger pusher accepting 1–60 mL syringes via interchangeable adapters; (3) Raspberry-Pi web GUI exposing rate, volume, and bolus modes; (4) measured maximum flow 2.1 mL/s. Anticipates: claims directed to (a) high-flow open syringe pumps integrating Pi-hosted web control, (b) FDM-printed pump bodies with adapter inserts spanning >2 orders of magnitude of syringe volume, (c) the architectural pattern of a single open library defining a family of motor-class variants with shared firmware.

## Poseidon — Open Syringe Pump and Microscope System (2019-08-28)

- **id**: `edmondson-2018-poseidon-syringe-pump-system`
- **corpus**: open
- **device class**: pump-component
- **creator**: A. Sina Booeshaghi, Eduardo da Veiga Beltrame, Lior Pachter et al. (Caltech)
- **disclosure**: Booeshaghi AS, Beltrame EdV, Bannon D, Gehring J, Pachter L. Principles of open source bioinstrumentation applied to the poseidon syringe pump system. Scientific Reports 9: 12385 (2019). doi:10.1038/s41598-019-48815-9
- **ip status**: open-permissive
- **prior art notes**: Distinct from the Pearce syringe-pump library, Poseidon discloses an integrated multi-channel syringe pump + observation microscope: (1) FDM-printed three-axis frame holding three independent syringe driver modules; (2) common stepper electronics (RAMPS + Marlin firmware) repurposed from 3D-printer ecosystem; (3) integrated Pi-camera arm focusable on a droplet generator junction; (4) Python host software coordinating flow rates and image capture for droplet calibration. Anticipates: (a) integrated multi-channel syringe-pump-plus-microscope cartridges for droplet workflows, (b) the architectural pattern of co-locating optical observation with multi-channel pumping in a single open device, (c) repurposing 3D-printer firmware for laboratory pumping.

## Behrens et al. 2020 Open-Source 3D-Printed Peristaltic Pump (2020-01-30)

- **id**: `behrens-2020-3d-printed-peristaltic-pump`
- **corpus**: open
- **device class**: pump-component
- **creator**: Behrens, Fuller, Swist, Wu, Islam, Long, Ruder, Steward (University of South Carolina; Carnegie Mellon)
- **disclosure**: Behrens MR, Fuller HC, Swist ER, Wu J, Islam MM, Long Z, Ruder WC, Steward R Jr. Open-source, 3D-printed Peristaltic Pumps for Small Volume Point-of-Care Liquid Handling. Scientific Reports 10:1543 (2020). doi:10.1038/s41598-020-58246-6
- **ip status**: open-permissive
- **prior art notes**: Discloses element-by-element: (1) a 3D-printed three-roller peristaltic pump with rotor carrying three ball bearings as rollers; (2) a swappable stator base parameterized to silicone tubing inner diameter from 1.5–3 mm; (3) Arduino-driven NEMA17 stepper actuation with programmable flow profile via open firmware; (4) demonstrated downstream coupling to PDMS, glass, plastic and paper microfluidic devices for low-volume point-of-care assays. Anticipates claims directed to: (a) 3D-printed peristaltic pumps with ball-bearing roller carriers as a fluid actuation primitive; (b) the architecture of a printed pump with a tubing-diameter-specific replaceable stator; (c) integrated open-source firmware producing arbitrary flow profiles for microfluidic perfusion; and (d) the system-level pattern of pairing a sub-$200 printed pump with paper-based diagnostic cartridges for cellular mechanobiology and POC diagnostics.
