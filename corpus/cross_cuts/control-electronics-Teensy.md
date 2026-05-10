---
title: control-electronics-Teensy
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-electronics-Teensy`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2017

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## IO Rodeo Rodeostat Open-Source Potentiostat (2017)

- **id**: `iorodeo-rodeostat-open-potentiostat`
- **corpus**: open
- **device class**: flow-controller
- **creator**: IO Rodeo Inc. (Pasadena, CA)
- **disclosure**: IO Rodeo. Rodeostat: open source potentiostat. https://iorodeo.com/products/rodeostat ; design files https://github.com/iorodeo/potentiostat (initial release 2017)
- **ip status**: open-copyleft
- **prior art notes**: Wave-2 distinct entry for the IO Rodeo Rodeostat as a long-running commercial-but-fully-open potentiostat lineage (the in-corpus io-rodeo entry covered the company; this entry pins the Rodeostat product). Element-by-element: (1) Teensy MCU driving DAC + transimpedance amplifier potentiostat front-end on shield-form PCB, (2) selectable current ranges via gain-switching, (3) BSD firmware with documented serial protocol, (4) Python and browser host clients. Anticipates: claims directed to USB-tethered potentiostat shields for arbitrary microcontroller hosts; commercial-and-open potentiostat product lines as prior art against subsequent enclosure attempts.

## Open-JIP — Open Chlorophyll Fluorometer (OJIP transient) (2020-08-31)

- **id**: `open-jip-chlorophyll-fluorometer`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Harvey C. Bates, Brad Sherman, Susanne Cusack (Australia)
- **disclosure**: Bates HC, Sherman B, Cusack S. Open-JIP, an open-source chlorophyll fluorometer. HardwareX 8: e00104 (2020). doi:10.1016/j.ohx.2020.e00104 ; repo https://github.com/HarveyBates/Open-JIP
- **ip status**: open-permissive
- **prior art notes**: Element-by-element discloses: (1) blue-LED actinic + measuring illumination control with microsecond timing via Teensy MCU; (2) photodiode + transimpedance amplifier acquisition front-end; (3) FDM-printed leaf clip; (4) firmware producing the OJIP transient; (5) Python analysis pipeline computing standard photosystem II metrics (Fo, Fm, Fv/Fm, performance index). Anticipates: (a) claims directed to low-cost open OJIP-transient fluorometers, (b) the architectural pattern of MCU-timed actinic LEDs paired with photodiode acquisition for plant photophysiology, (c) clip-on cuvette geometry with embedded electronics.
