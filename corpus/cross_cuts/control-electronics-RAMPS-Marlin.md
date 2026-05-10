---
title: control-electronics-RAMPS-Marlin
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-electronics-RAMPS-Marlin`

**1 corpus entries disclose this subsystem.**

Earliest disclosure: 2019-08-28

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Poseidon — Open Syringe Pump and Microscope System (2019-08-28)

- **id**: `edmondson-2018-poseidon-syringe-pump-system`
- **corpus**: open
- **device class**: pump-component
- **creator**: A. Sina Booeshaghi, Eduardo da Veiga Beltrame, Lior Pachter et al. (Caltech)
- **disclosure**: Booeshaghi AS, Beltrame EdV, Bannon D, Gehring J, Pachter L. Principles of open source bioinstrumentation applied to the poseidon syringe pump system. Scientific Reports 9: 12385 (2019). doi:10.1038/s41598-019-48815-9
- **ip status**: open-permissive
- **prior art notes**: Distinct from the Pearce syringe-pump library, Poseidon discloses an integrated multi-channel syringe pump + observation microscope: (1) FDM-printed three-axis frame holding three independent syringe driver modules; (2) common stepper electronics (RAMPS + Marlin firmware) repurposed from 3D-printer ecosystem; (3) integrated Pi-camera arm focusable on a droplet generator junction; (4) Python host software coordinating flow rates and image capture for droplet calibration. Anticipates: (a) integrated multi-channel syringe-pump-plus-microscope cartridges for droplet workflows, (b) the architectural pattern of co-locating optical observation with multi-channel pumping in a single open device, (c) repurposing 3D-printer firmware for laboratory pumping.
