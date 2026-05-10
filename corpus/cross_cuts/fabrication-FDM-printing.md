---
title: fabrication-FDM-printing
parent: Cross-cuts
layout: default
---

# Cross-cut: `fabrication-FDM-printing`

**10 corpus entries disclose this subsystem.**

Earliest disclosure: 2013-04-22

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Anzalone–Pearce 2013 Open-Source Colorimeter (Michigan Tech MOST) (2013-04-22)

- **id**: `anzalone-pearce-2013-open-colorimeter`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Gerald C. Anzalone, Alexandra G. Glover, Joshua M. Pearce (Michigan Technological University)
- **disclosure**: Anzalone GC, Glover AG, Pearce JM. Open-Source Colorimeter. Sensors 13(4): 5338–5346 (2013). doi:10.3390/s130405338
- **ip status**: open-copyleft
- **prior art notes**: Discloses an Arduino-controlled open colorimeter with a 3D-printed cuvette holder accepting standard 16 mm vials, an RGB LED illuminator and discrete photodetector, and open firmware producing absorbance values benchmarked against a commercial COD photometer. Anticipates: (a) low-cost open colorimetric readers for paper-microfluidic and tube-based chemistries, (b) the architectural pattern of GPL-licensed CAD plus Arduino firmware for absorbance instruments, (c) RGB-LED-based multi-wavelength colorimetry by software channel-switching, and (d) the cost-reduction methodology of replacing commercial photometers with FDM-printed housings to democratize water-quality monitoring.

## Pearce-lab Open Syringe Pump v2 — Large-Format / NEMA17 Variant (2014-09-16)

- **id**: `wijnen-pearce-2014-syringe-pump-v2-12mm`
- **corpus**: open
- **device class**: pump-component
- **creator**: B. Wijnen, E.J. Hunt, G.C. Anzalone, J.M. Pearce (Michigan Tech)
- **disclosure**: Wijnen B, Hunt EJ, Anzalone GC, Pearce JM. Open-Source Syringe Pump Library. PLoS ONE 9(9): e107216 (2014). doi:10.1371/journal.pone.0107216 — Library defines two motor-class variants (NEMA11 and NEMA17) yielding distinct max flow rates; this entry covers the NEMA17 high-flow large-format variant.
- **ip status**: open-copyleft
- **prior art notes**: Distinguished from the NEMA11 small-format variant (covered separately by wave 1's wijnen-pearce-2014-open-syringe-pump entry as the umbrella library disclosure), this entry defends the high-flow NEMA17-driven implementation explicitly disclosed in the same paper. Element-by-element: (1) FDM-printed two-rail frame with leadscrew + NEMA17 stepper; (2) plunger pusher accepting 1–60 mL syringes via interchangeable adapters; (3) Raspberry-Pi web GUI exposing rate, volume, and bolus modes; (4) measured maximum flow 2.1 mL/s. Anticipates: claims directed to (a) high-flow open syringe pumps integrating Pi-hosted web control, (b) FDM-printed pump bodies with adapter inserts spanning >2 orders of magnitude of syringe volume, (c) the architectural pattern of a single open library defining a family of motor-class variants with shared firmware.

## Wittbrodt–Pearce 2015 Open-Source Enzymatic Nitrate Photometer (2015-08-06)

- **id**: `wittbrodt-2015-open-nitrate-photometer`
- **corpus**: open
- **device class**: flow-controller
- **creator**: B.T. Wittbrodt, D.A. Squires, J. Walbeck, E. Campbell, W.H. Campbell, J.M. Pearce (Michigan Tech / NECi Superior Enzymes)
- **disclosure**: Wittbrodt BT, Squires DA, Walbeck J, Campbell E, Campbell WH, Pearce JM. Open-Source Photometric System for Enzymatic Nitrate Quantification. PLoS ONE 10(8): e0134989 (2015). doi:10.1371/journal.pone.0134989
- **ip status**: open-copyleft
- **prior art notes**: Discloses a 3D-printed Arduino+Android photometric system that, in combination with NECi nitrate-reductase enzyme chemistry, replaces toxic Cd-reduction reagents and matches the performance of commercial nitrate photometers at 15% of the cost. Element-by-element it discloses: (1) printed cuvette holder; (2) bicolour LED illumination; (3) Arduino acquisition firmware; (4) Bluetooth/USB Android-side data pipeline; (5) the integration with enzyme cartridge chemistry. Anticipates: (a) field-deployable enzymatic nitrate photometers paired with phone-side data infrastructure; (b) the architectural pattern of LED + photodiode + open MCU + smartphone for environmental colorimetric assay readers; (c) the elimination of cadmium chemistry by combining open hardware with enzyme reagents.

## MOST — Open-Source 3-D Platform for Low-Cost Scientific Instrument Ecosystem (2016-08)

- **id**: `zhang-pearce-2016-most-platform-instrument-ecosystem`
- **corpus**: open
- **device class**: printer-tooling
- **creator**: Chenlong Zhang, Bas Wijnen, Joshua M. Pearce (Michigan Technological University, MOST group)
- **disclosure**: Zhang C, Wijnen B, Pearce JM. Open-source 3-D Platform for Low-cost Scientific Instrument Ecosystem. Journal of Laboratory Automation 21(4): 517–525 (2016). doi:10.1177/2211068215624406
- **ip status**: open-copyleft
- **prior art notes**: Discloses the explicit architectural pattern of using a single open-source 3-axis 3D-printer-derived motion platform as the chassis for a family of laboratory instruments — including syringe pumps, microscope stages, dispensers and photometers — sharing electronics, firmware and CAD lineage. Element-by-element: (1) RepRap-derived three-axis motion stage; (2) RAMPS / ATmega / Arduino electronics; (3) Marlin-derived firmware adapted for instrument workflows; (4) standardized print-bed-plus-tool head interface allowing a syringe pump head, dispensing nozzle, microscope objective, etc., to be swapped onto the same platform. Anticipates claims directed to: (a) reusable open-hardware motion platforms underlying multiple lab instruments; (b) the use of consumer 3D-printer kinematics for analytical instrumentation chassis; (c) shared control firmware bundling instrument-specific G-code dialects.

## NinjaPCR Open Thermocycler (2018)

- **id**: `ninjapcr-open-thermocycler`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Hisashi Hisanaga and contributors
- **disclosure**: Hisanaga H, NinjaPCR contributors. NinjaPCR — open thermocycler implementation. https://github.com/hisashin/NinjaPCR (initial release 2018; ESP32/Arduino reimplementation of the OpenPCR firmware/UI plus Bluetooth/Web app)
- **ip status**: open-permissive
- **prior art notes**: Element-by-element discloses: (1) ESP32 wireless controller running PCR cycling firmware, (2) FDM-printed enclosure for Peltier + aluminum 16-tube block, (3) Bluetooth/web app providing protocol authoring, (4) compatibility with OpenPCR protocol files preserving an open ecosystem. Anticipates: (a) wireless-controlled portable PCR instruments as prior art against subsequent app-controlled thermocycler patents, (b) the design pattern of pairing low-cost ESP32 microcontrollers with Peltier blocks for distributable PCR.

## eVOLVER Open Multiplexed Continuous-Culture Bioreactor (2018-06-25)

- **id**: `wong-2018-evolver-multiplex-bioreactor`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Brandon G. Wong, Christopher P. Mancuso, Szilvia Kiriakov, Caleb J. Bashor, Ahmad S. Khalil (Boston University, Wyss Institute, Rice)
- **disclosure**: Wong BG, Mancuso CP, Kiriakov S, Bashor CJ, Khalil AS. Precise, automated control of conditions for high-throughput growth of yeast and bacteria with eVOLVER. Nature Biotechnology 36(7): 614–623 (2018). doi:10.1038/nbt.4151
- **ip status**: open-permissive
- **prior art notes**: Discloses element-by-element a modular continuous culture framework: (1) Smart Sleeves wrapping standard 16x glass vials, each with on-board OD600 sensing, magnetic stir, Peltier temperature control and fluidic ports; (2) per-sleeve PCB with MCU communicating to a Raspberry Pi master via I2C/serial; (3) array of peristaltic pumps for media in/out with calibration routines; (4) gas mixing manifold for O2/CO2/N2 per sleeve; (5) Python control software implementing turbidostat, chemostat, morbidostat and arbitrary feedback growth programs. Anticipates: (a) modular per-vial smart-sleeve continuous-culture platforms; (b) feedback-controlled morbidostat workflows for directed evolution; (c) DIY frameworks combining commodity glass vials with on-board sensing/actuation as an alternative to single-monolithic bioreactors; (d) the architectural pattern of distributed MCUs per culture coordinated by a high-level scripting layer.

## Behrens et al. 2020 Open-Source 3D-Printed Peristaltic Pump (2020-01-30)

- **id**: `behrens-2020-3d-printed-peristaltic-pump`
- **corpus**: open
- **device class**: pump-component
- **creator**: Behrens, Fuller, Swist, Wu, Islam, Long, Ruder, Steward (University of South Carolina; Carnegie Mellon)
- **disclosure**: Behrens MR, Fuller HC, Swist ER, Wu J, Islam MM, Long Z, Ruder WC, Steward R Jr. Open-source, 3D-printed Peristaltic Pumps for Small Volume Point-of-Care Liquid Handling. Scientific Reports 10:1543 (2020). doi:10.1038/s41598-020-58246-6
- **ip status**: open-permissive
- **prior art notes**: Discloses element-by-element: (1) a 3D-printed three-roller peristaltic pump with rotor carrying three ball bearings as rollers; (2) a swappable stator base parameterized to silicone tubing inner diameter from 1.5–3 mm; (3) Arduino-driven NEMA17 stepper actuation with programmable flow profile via open firmware; (4) demonstrated downstream coupling to PDMS, glass, plastic and paper microfluidic devices for low-volume point-of-care assays. Anticipates claims directed to: (a) 3D-printed peristaltic pumps with ball-bearing roller carriers as a fluid actuation primitive; (b) the architecture of a printed pump with a tubing-diameter-specific replaceable stator; (c) integrated open-source firmware producing arbitrary flow profiles for microfluidic perfusion; and (d) the system-level pattern of pairing a sub-$200 printed pump with paper-based diagnostic cartridges for cellular mechanobiology and POC diagnostics.

## Open-JIP — Open Chlorophyll Fluorometer (OJIP transient) (2020-08-31)

- **id**: `open-jip-chlorophyll-fluorometer`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Harvey C. Bates, Brad Sherman, Susanne Cusack (Australia)
- **disclosure**: Bates HC, Sherman B, Cusack S. Open-JIP, an open-source chlorophyll fluorometer. HardwareX 8: e00104 (2020). doi:10.1016/j.ohx.2020.e00104 ; repo https://github.com/HarveyBates/Open-JIP
- **ip status**: open-permissive
- **prior art notes**: Element-by-element discloses: (1) blue-LED actinic + measuring illumination control with microsecond timing via Teensy MCU; (2) photodiode + transimpedance amplifier acquisition front-end; (3) FDM-printed leaf clip; (4) firmware producing the OJIP transient; (5) Python analysis pipeline computing standard photosystem II metrics (Fo, Fm, Fv/Fm, performance index). Anticipates: (a) claims directed to low-cost open OJIP-transient fluorometers, (b) the architectural pattern of MCU-timed actinic LEDs paired with photodiode acquisition for plant photophysiology, (c) clip-on cuvette geometry with embedded electronics.

## OpenFlexure Microscope v7 — High-Resolution Lab Variant (2020-11-09)

- **id**: `openflexure-microscope-v7`
- **corpus**: open
- **device class**: chip-holder
- **creator**: Richard Bowman, Joel Collins, Joe Knapper, Julian Stirling et al. (University of Bath, OpenFlexure project)
- **disclosure**: Collins JT, Knapper J, Stirling J, et al. Robotic microscopy for everyone: the OpenFlexure microscope. Biomedical Optics Express 11(5): 2447–2460 (2020). doi:10.1364/BOE.385729 ; v7 design tag https://gitlab.com/openflexure/openflexure-microscope (released 2020-11)
- **ip status**: open-permissive
- **prior art notes**: Wave-2 strengthening of the wave-1 OpenFlexure entry by pinning the v7 release with primary citation to Biomedical Optics Express. Element-by-element: (1) monolithic FDM-printed plastic flexure XYZ stage with three lead-screw drivers; (2) RMS-thread objective mount; (3) Raspberry Pi HQ camera + custom server software; (4) v7 specifically incorporates updated condenser, sample clip and motor coupler reliability changes for fielded clinical use. Anticipates: claims directed to printed monolithic flexure stages for high-resolution microscopy, and to the architectural pattern of Pi-hosted automation servers for clinical microscope deployments in low-resource settings.

## DIYNAFLUOR — $40 Open-Source 3D-Printed DNA Fluorometer (2023)

- **id**: `diynafluor-low-cost-dna-fluorometer`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Trau Lab and contributors (Australia)
- **disclosure**: Trau Lab DIYNAFLUOR project. Code, 3D Print Files, BOM and Build Instructions for the DIYNAFLUOR DNA Fluorometer. https://github.com/traulab/DIYNAFLUOR (initial release 2023; companion educational paper)
- **ip status**: open-permissive
- **prior art notes**: Element-by-element discloses: (1) 3D-printed black housing with sample slot for 0.2 mL PCR tube; (2) blue LED excitation with emission filter; (3) photodiode detector at 90° geometry; (4) Arduino Nano firmware computing concentration from fluorescence baseline; (5) solder-free assembly. Anticipates: (a) claims directed to ultra-low-cost DNA fluorometers using PCR-tube cuvette geometry, (b) the architectural pattern of 90° LED+photodiode in a printed black housing for fluorescence-based quantitation, (c) educational-grade alternatives to Qubit-class instruments.
