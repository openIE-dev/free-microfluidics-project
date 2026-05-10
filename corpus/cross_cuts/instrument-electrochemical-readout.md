---
title: instrument-electrochemical-readout
parent: Cross-cuts
layout: default
---

# Cross-cut: `instrument-electrochemical-readout`

**4 corpus entries disclose this subsystem.**

Earliest disclosure: 2015-10-29

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## DStat — Open-Source Potentiostat for Electroanalysis and Integration (2015-10-29)

- **id**: `dryden-2015-dstat-open-potentiostat`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Michael D. M. Dryden, Aaron R. Wheeler (University of Toronto, Wheeler Microfluidics Laboratory)
- **disclosure**: Dryden MDM, Wheeler AR. DStat: A Versatile, Open-Source Potentiostat for Electroanalysis and Integration. PLoS ONE 10(10): e0140349 (2015). doi:10.1371/journal.pone.0140349
- **ip status**: open-permissive
- **prior art notes**: Discloses element-by-element a complete open-hardware potentiostat targeted explicitly at integration with microfluidic systems: (1) USB-powered single-board potentiostat with picoampere current measurement, (2) instrumentation amplifier + SAR ADC analog front-end, (3) open-source firmware and Python control GUI, (4) demonstrated bidirectional integration with the DropBot open digital-microfluidic controller for combined electrowetting actuation and electrochemical readout. Anticipates claims directed to: (a) open potentiostat hardware integrated with on-chip electrochemical detection; (b) software-coordinated combinations of digital microfluidic actuation with simultaneous electroanalytical measurement; (c) low-current cyclic voltammetry instrumentation for lab-on-chip biosensors; and (d) the architectural pattern of pairing a commodity potentiostat with an open digital microfluidic controller through documented serial/USB protocol.

## IO Rodeo Rodeostat Open-Source Potentiostat (2017)

- **id**: `iorodeo-rodeostat-open-potentiostat`
- **corpus**: open
- **device class**: flow-controller
- **creator**: IO Rodeo Inc. (Pasadena, CA)
- **disclosure**: IO Rodeo. Rodeostat: open source potentiostat. https://iorodeo.com/products/rodeostat ; design files https://github.com/iorodeo/potentiostat (initial release 2017)
- **ip status**: open-copyleft
- **prior art notes**: Wave-2 distinct entry for the IO Rodeo Rodeostat as a long-running commercial-but-fully-open potentiostat lineage (the in-corpus io-rodeo entry covered the company; this entry pins the Rodeostat product). Element-by-element: (1) Teensy MCU driving DAC + transimpedance amplifier potentiostat front-end on shield-form PCB, (2) selectable current ranges via gain-switching, (3) BSD firmware with documented serial protocol, (4) Python and browser host clients. Anticipates: claims directed to USB-tethered potentiostat shields for arbitrary microcontroller hosts; commercial-and-open potentiostat product lines as prior art against subsequent enclosure attempts.

## UWED — Universal Wireless Electrochemical Detector for Smartphones (2018-04-12)

- **id**: `ainla-2018-uwed-wireless-potentiostat`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Alar Ainla et al., George M. Whitesides group (Harvard)
- **disclosure**: Ainla A, Mousavi MPS, Tsaloglou MN, Redston J, Bell JG, Fernández-Abedul MT, Whitesides GM. Open-Source Potentiostat for Wireless Electrochemical Detection with Smartphones. Anal. Chem. 90(10): 6240–6246 (2018). doi:10.1021/acs.analchem.8b00850
- **ip status**: open-permissive
- **prior art notes**: Element-by-element discloses: (1) BLE-equipped potentiostat PCB with documented analog front-end including DAC, transimpedance amplifier and instrumentation amp; (2) Android application implementing parameter control, real-time visualization and cloud upload; (3) tested with paper-microfluidic glucose, lactate and chloride sensors. Anticipates: (a) claims directed to wireless smartphone-tethered potentiostats for paper-microfluidic readers, (b) the architectural pattern of BLE-MCU + analog front-end + smartphone host as a defensible primitive in connected POC electrochemistry, (c) integration of cloud upload pipelines with disposable paper electrochemical cartridges.

## PSoC-Stat Single-Chip Open Potentiostat (2018-08-14)

- **id**: `lopin-2018-psoc-stat-potentiostat`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Prattana Lopin, Kyle V. Lopin
- **disclosure**: Lopin P, Lopin KV. PSoC-Stat: A single chip open source potentiostat based on a Programmable System on a Chip. PLoS ONE 13(8): e0201353 (2018). doi:10.1371/journal.pone.0201353
- **ip status**: open-permissive
- **prior art notes**: Element-by-element discloses the use of a single Cypress PSoC 5LP chip's programmable analog blocks (op-amps, DACs, ADCs) to implement a complete potentiostat without external PCB. Configuration files, firmware, and Python host GUI are released open. Anticipates: (a) claims directed to single-chip system-on-chip implementations of potentiostats using programmable analog routing, (b) component-list-free distribution patterns for educational electrochemistry hardware, (c) cloud-distributed PSoC configuration files as bitstream prior art.
