---
title: control-electronics-Arduino
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-electronics-Arduino`

**6 corpus entries disclose this subsystem.**

Earliest disclosure: 2010-09

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## OpenPCR Open-Source Thermal Cycler (Chai Bio / Perl + Salzberg) (2010-09)

- **id**: `openpcr-chai-2010-thermal-cycler`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Tito Jankowski, Josh Perfetto (Chai Biotechnologies, San Francisco)
- **disclosure**: Perl T, Salzberg J. OpenPCR: open-source PCR thermal cycler. https://openpcr.org (Kickstarter campaign 2010-09; design files released 2011). Build instructions and CAD/firmware archived at https://openpcr.org/design/
- **ip status**: open-permissive
- **prior art notes**: Despite some overlap with the existing entry openpcr-thermal-cycler in the corpus (which covers OpenPCR generically), this entry pins the originating Chai Biotechnologies disclosure with primary citation to the 2010 Kickstarter and the openpcr.org engineering documentation set. Element-by-element: (1) Peltier-driven aluminum block holding 16 tubes; (2) heated lid; (3) Arduino Uno controller with open firmware in C++; (4) Windows/macOS GUI driving cycling protocols; (5) public, kit-form open BOM and CAD. Anticipates: (a) consumer-priced open thermal cyclers as defensive prior art against subsequent patents on low-cost PCR machines for citizen science and field use; (b) the architectural pattern of Peltier + heated lid + Arduino + cross-platform GUI distributed as a kit.

## Anzalone–Pearce 2013 Open-Source Colorimeter (Michigan Tech MOST) (2013-04-22)

- **id**: `anzalone-pearce-2013-open-colorimeter`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Gerald C. Anzalone, Alexandra G. Glover, Joshua M. Pearce (Michigan Technological University)
- **disclosure**: Anzalone GC, Glover AG, Pearce JM. Open-Source Colorimeter. Sensors 13(4): 5338–5346 (2013). doi:10.3390/s130405338
- **ip status**: open-copyleft
- **prior art notes**: Discloses an Arduino-controlled open colorimeter with a 3D-printed cuvette holder accepting standard 16 mm vials, an RGB LED illuminator and discrete photodetector, and open firmware producing absorbance values benchmarked against a commercial COD photometer. Anticipates: (a) low-cost open colorimetric readers for paper-microfluidic and tube-based chemistries, (b) the architectural pattern of GPL-licensed CAD plus Arduino firmware for absorbance instruments, (c) RGB-LED-based multi-wavelength colorimetry by software channel-switching, and (d) the cost-reduction methodology of replacing commercial photometers with FDM-printed housings to democratize water-quality monitoring.

## Wittbrodt–Pearce 2015 Open-Source Enzymatic Nitrate Photometer (2015-08-06)

- **id**: `wittbrodt-2015-open-nitrate-photometer`
- **corpus**: open
- **device class**: flow-controller
- **creator**: B.T. Wittbrodt, D.A. Squires, J. Walbeck, E. Campbell, W.H. Campbell, J.M. Pearce (Michigan Tech / NECi Superior Enzymes)
- **disclosure**: Wittbrodt BT, Squires DA, Walbeck J, Campbell E, Campbell WH, Pearce JM. Open-Source Photometric System for Enzymatic Nitrate Quantification. PLoS ONE 10(8): e0134989 (2015). doi:10.1371/journal.pone.0134989
- **ip status**: open-copyleft
- **prior art notes**: Discloses a 3D-printed Arduino+Android photometric system that, in combination with NECi nitrate-reductase enzyme chemistry, replaces toxic Cd-reduction reagents and matches the performance of commercial nitrate photometers at 15% of the cost. Element-by-element it discloses: (1) printed cuvette holder; (2) bicolour LED illumination; (3) Arduino acquisition firmware; (4) Bluetooth/USB Android-side data pipeline; (5) the integration with enzyme cartridge chemistry. Anticipates: (a) field-deployable enzymatic nitrate photometers paired with phone-side data infrastructure; (b) the architectural pattern of LED + photodiode + open MCU + smartphone for environmental colorimetric assay readers; (c) the elimination of cadmium chemistry by combining open hardware with enzyme reagents.

## MboaLab Open-Source Microbiology Incubator (2018)

- **id**: `mboalab-open-incubator-microbiology`
- **corpus**: open
- **device class**: chip-holder
- **creator**: MboaLab (Yaoundé, Cameroon — Thomas Mboa Nkoudou and team) with Open Bioeconomy Lab (Cambridge UK)
- **disclosure**: MboaLab / Open Bioeconomy Lab. Open Source Incubator for Microbiology. https://openbioeconomy.org/outputs/open-source-incubator-for-microbiology/ (project funded by GOSH Build Free and Open Science Hardware grant 2018; repo https://github.com/FOSH-following-demand/Incubator)
- **ip status**: open-permissive
- **prior art notes**: Discloses an open-hardware microbiology incubator explicitly designed for low-resource African contexts: (1) thermally insulated locally-machinable chamber, (2) PTC-resistive heating element with PID temperature control via an Arduino-class MCU, (3) fan-driven internal air circulation, (4) door-switch and over-temperature safety interlocks, (5) public BOM/CAD/firmware with build instructions translated into French. Anticipates: (a) low-cost open incubator hardware as 102/103 prior art against subsequent commercial DIY incubator IP, (b) the architectural pattern of locally-fabricable bio-instrument designs targeting sub-Saharan supply chains, (c) PID-controlled PTC heater + fan + insulated box as a defensible primitive in DIY bioscience.

## Behrens et al. 2020 Open-Source 3D-Printed Peristaltic Pump (2020-01-30)

- **id**: `behrens-2020-3d-printed-peristaltic-pump`
- **corpus**: open
- **device class**: pump-component
- **creator**: Behrens, Fuller, Swist, Wu, Islam, Long, Ruder, Steward (University of South Carolina; Carnegie Mellon)
- **disclosure**: Behrens MR, Fuller HC, Swist ER, Wu J, Islam MM, Long Z, Ruder WC, Steward R Jr. Open-source, 3D-printed Peristaltic Pumps for Small Volume Point-of-Care Liquid Handling. Scientific Reports 10:1543 (2020). doi:10.1038/s41598-020-58246-6
- **ip status**: open-permissive
- **prior art notes**: Discloses element-by-element: (1) a 3D-printed three-roller peristaltic pump with rotor carrying three ball bearings as rollers; (2) a swappable stator base parameterized to silicone tubing inner diameter from 1.5–3 mm; (3) Arduino-driven NEMA17 stepper actuation with programmable flow profile via open firmware; (4) demonstrated downstream coupling to PDMS, glass, plastic and paper microfluidic devices for low-volume point-of-care assays. Anticipates claims directed to: (a) 3D-printed peristaltic pumps with ball-bearing roller carriers as a fluid actuation primitive; (b) the architecture of a printed pump with a tubing-diameter-specific replaceable stator; (c) integrated open-source firmware producing arbitrary flow profiles for microfluidic perfusion; and (d) the system-level pattern of pairing a sub-$200 printed pump with paper-based diagnostic cartridges for cellular mechanobiology and POC diagnostics.

## DIYNAFLUOR — $40 Open-Source 3D-Printed DNA Fluorometer (2023)

- **id**: `diynafluor-low-cost-dna-fluorometer`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Trau Lab and contributors (Australia)
- **disclosure**: Trau Lab DIYNAFLUOR project. Code, 3D Print Files, BOM and Build Instructions for the DIYNAFLUOR DNA Fluorometer. https://github.com/traulab/DIYNAFLUOR (initial release 2023; companion educational paper)
- **ip status**: open-permissive
- **prior art notes**: Element-by-element discloses: (1) 3D-printed black housing with sample slot for 0.2 mL PCR tube; (2) blue LED excitation with emission filter; (3) photodiode detector at 90° geometry; (4) Arduino Nano firmware computing concentration from fluorescence baseline; (5) solder-free assembly. Anticipates: (a) claims directed to ultra-low-cost DNA fluorometers using PCR-tube cuvette geometry, (b) the architectural pattern of 90° LED+photodiode in a printed black housing for fluorescence-based quantitation, (c) educational-grade alternatives to Qubit-class instruments.
