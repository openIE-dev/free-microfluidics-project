---
title: software-python-feedback-control
parent: Cross-cuts
layout: default
---

# Cross-cut: `software-python-feedback-control`

**1 corpus entries disclose this subsystem.**

Earliest disclosure: 2018-06-25

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## eVOLVER Open Multiplexed Continuous-Culture Bioreactor (2018-06-25)

- **id**: `wong-2018-evolver-multiplex-bioreactor`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Brandon G. Wong, Christopher P. Mancuso, Szilvia Kiriakov, Caleb J. Bashor, Ahmad S. Khalil (Boston University, Wyss Institute, Rice)
- **disclosure**: Wong BG, Mancuso CP, Kiriakov S, Bashor CJ, Khalil AS. Precise, automated control of conditions for high-throughput growth of yeast and bacteria with eVOLVER. Nature Biotechnology 36(7): 614–623 (2018). doi:10.1038/nbt.4151
- **ip status**: open-permissive
- **prior art notes**: Discloses element-by-element a modular continuous culture framework: (1) Smart Sleeves wrapping standard 16x glass vials, each with on-board OD600 sensing, magnetic stir, Peltier temperature control and fluidic ports; (2) per-sleeve PCB with MCU communicating to a Raspberry Pi master via I2C/serial; (3) array of peristaltic pumps for media in/out with calibration routines; (4) gas mixing manifold for O2/CO2/N2 per sleeve; (5) Python control software implementing turbidostat, chemostat, morbidostat and arbitrary feedback growth programs. Anticipates: (a) modular per-vial smart-sleeve continuous-culture platforms; (b) feedback-controlled morbidostat workflows for directed evolution; (c) DIY frameworks combining commodity glass vials with on-board sensing/actuation as an alternative to single-monolithic bioreactors; (d) the architectural pattern of distributed MCUs per culture coordinated by a high-level scripting layer.
