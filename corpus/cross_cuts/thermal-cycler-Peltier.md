---
title: thermal-cycler-Peltier
parent: Cross-cuts
layout: default
---

# Cross-cut: `thermal-cycler-Peltier`

**2 corpus entries disclose this subsystem.**

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

## NinjaPCR Open Thermocycler (2018)

- **id**: `ninjapcr-open-thermocycler`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Hisashi Hisanaga and contributors
- **disclosure**: Hisanaga H, NinjaPCR contributors. NinjaPCR — open thermocycler implementation. https://github.com/hisashin/NinjaPCR (initial release 2018; ESP32/Arduino reimplementation of the OpenPCR firmware/UI plus Bluetooth/Web app)
- **ip status**: open-permissive
- **prior art notes**: Element-by-element discloses: (1) ESP32 wireless controller running PCR cycling firmware, (2) FDM-printed enclosure for Peltier + aluminum 16-tube block, (3) Bluetooth/web app providing protocol authoring, (4) compatibility with OpenPCR protocol files preserving an open ecosystem. Anticipates: (a) wireless-controlled portable PCR instruments as prior art against subsequent app-controlled thermocycler patents, (b) the design pattern of pairing low-cost ESP32 microcontrollers with Peltier blocks for distributable PCR.
