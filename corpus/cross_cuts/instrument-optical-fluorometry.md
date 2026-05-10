---
title: instrument-optical-fluorometry
parent: Cross-cuts
layout: default
---

# Cross-cut: `instrument-optical-fluorometry`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2020-08-31

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Open-JIP — Open Chlorophyll Fluorometer (OJIP transient) (2020-08-31)

- **id**: `open-jip-chlorophyll-fluorometer`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Harvey C. Bates, Brad Sherman, Susanne Cusack (Australia)
- **disclosure**: Bates HC, Sherman B, Cusack S. Open-JIP, an open-source chlorophyll fluorometer. HardwareX 8: e00104 (2020). doi:10.1016/j.ohx.2020.e00104 ; repo https://github.com/HarveyBates/Open-JIP
- **ip status**: open-permissive
- **prior art notes**: Element-by-element discloses: (1) blue-LED actinic + measuring illumination control with microsecond timing via Teensy MCU; (2) photodiode + transimpedance amplifier acquisition front-end; (3) FDM-printed leaf clip; (4) firmware producing the OJIP transient; (5) Python analysis pipeline computing standard photosystem II metrics (Fo, Fm, Fv/Fm, performance index). Anticipates: (a) claims directed to low-cost open OJIP-transient fluorometers, (b) the architectural pattern of MCU-timed actinic LEDs paired with photodiode acquisition for plant photophysiology, (c) clip-on cuvette geometry with embedded electronics.

## DIYNAFLUOR — $40 Open-Source 3D-Printed DNA Fluorometer (2023)

- **id**: `diynafluor-low-cost-dna-fluorometer`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Trau Lab and contributors (Australia)
- **disclosure**: Trau Lab DIYNAFLUOR project. Code, 3D Print Files, BOM and Build Instructions for the DIYNAFLUOR DNA Fluorometer. https://github.com/traulab/DIYNAFLUOR (initial release 2023; companion educational paper)
- **ip status**: open-permissive
- **prior art notes**: Element-by-element discloses: (1) 3D-printed black housing with sample slot for 0.2 mL PCR tube; (2) blue LED excitation with emission filter; (3) photodiode detector at 90° geometry; (4) Arduino Nano firmware computing concentration from fluorescence baseline; (5) solder-free assembly. Anticipates: (a) claims directed to ultra-low-cost DNA fluorometers using PCR-tube cuvette geometry, (b) the architectural pattern of 90° LED+photodiode in a printed black housing for fluorescence-based quantitation, (c) educational-grade alternatives to Qubit-class instruments.
