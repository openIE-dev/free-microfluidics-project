---
title: mixer-active-magnetic
parent: Cross-cuts
layout: default
---

# Cross-cut: `mixer-active-magnetic`

**3 corpus entries disclose this subsystem.**

Earliest disclosure: 2008

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Phoenix Mars Lander MECA Wet Chemistry Laboratory (WCL) (2008)

- **id**: `phoenix-meca-wet-chemistry-lab`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: NASA Jet Propulsion Laboratory / Tufts University (Kounaves) / University of Arizona (Hecht PI)
- **disclosure**: Hecht MH et al., 'Detection of Perchlorate and the Soluble Chemistry of Martian Soil at the Phoenix Lander Site,' Science 325(5936):64-67 (2009), doi:10.1126/science.1172466; Kounaves SP et al., 'The MECA Wet Chemistry Laboratory on the 2007 Phoenix Mars Scout Lander,' JGR Planets 114:E00A19 (2009), doi:10.1029/2008JE003084
- **ip status**: public-domain
- **prior art notes**: Discloses a planetary in-situ wet chemistry cartridge architecture: a sealed disposable reaction beaker with integrated multi-ion electrochemical sensor array on the cell wall, dry-stored reagent pellets released by a mechanical dispenser, and a magnetic stir bar for homogenization. Element-by-element prior art for: (a) any cartridge claim that integrates an ISE array on a single beaker wall with a multi-ion readout (Li, Na, K, NH4, Mg, Ca, Cl, NO3, Br, perchlorate-sensitive); (b) the standard-addition titration protocol implemented through sequential dry-pellet dissolution (the BaCl2 -> SO4 turbidity step, the HNO3 acidification step) anticipates patents on dry-reagent diagnostic cartridges that perform sequential reagent additions for water-quality analysis; (c) the integration of cyclic voltammetry on the same beaker as ion-selective potentiometry anticipates multi-modal electrochemical cartridge designs. The Phoenix WCL is one of two flight precedents (with Viking Biology Instrument) for in-situ aqueous chemistry on a planetary surface.

## Asynt fReactor multi-stage CSTR flow reactor (2015)

- **id**: `asynt-freactor`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Asynt Ltd. (Cambridge, UK), invented at Univ. Leeds Bourne group
- **disclosure**: Asynt Ltd. fReactor product launch 2015; Reay, A. J.; Hammond, J. M.; Bourne, J.; Lee, M.; Smith, M. B. 'Reactor characterization for use in active fermentation' (uses fReactor); Asynt fReactor datasheet rev 3 (2018); product page https://www.asynt.com/product/freactor/
- **ip status**: patented
- **prior art notes**: Discloses (a) a low-cost 3D-printed cascade of mini-CSTRs with magnetic stirring as an academic-affordable alternative to Snapdragon-style CSTR cascades; (b) magnetic-coupled stirring in each cell (no shaft seals) enabling closed continuous operation; (c) the design pattern of 'inexpensive 3D-printed flow chemistry hardware for academic adoption'. Anticipates patent claims to magnetically stirred mini-CSTR cascade reactors and to 3D-printed multi-cell continuous reactors for academic flow chemistry.

## Pioreactor (2021-09)

- **id**: `pioreactor-open-bioreactor`
- **corpus**: open
- **device class**: other
- **creator**: Pioreactor (Cameron Lab / Pioreactor Inc., Toronto)
- **disclosure**: Cadart C., Bartlett J. et al., Pioreactor open-source hardware release on GitHub https://github.com/Pioreactor/pioreactor (initial public release Sept 2021); pioreactor.com product page; documentation site docs.pioreactor.com
- **ip status**: open-permissive
- **prior art notes**: Discloses an open-source benchtop bioreactor platform built around a Raspberry Pi HAT (the Pioreactor 'Pioreactor HAT'), which integrates: (a) an LED+photodiode optical density measurement subsystem with synchronous detection (LED chopping plus lock-in style demodulation) on a low-cost MCU; (b) a magnetic stirrer driven by a brushless DC motor with closed-loop RPM control via a Hall sensor; (c) a heating element on a PCB underneath a 20 mL borosilicate glass vial with thermistor feedback; (d) a peristaltic-pump dosing module driven over I2C for continuous-culture (turbidostat/chemostat/morbidostat) operation; (e) a clustered control architecture using MQTT pub/sub over Wi-Fi enabling fleet operation of dozens of units from a single 'leader' Pi. All hardware schematics (KiCad), firmware, mechanical CAD, and Python control software are released under MIT (software) and CERN-OHL-S/CC-BY (hardware). Anticipates: low-cost networked bioreactor fleets with synchronous-detection turbidity sensing on a Raspberry Pi class device; pluggable Python automation classes for closed-loop bioprocess control (turbidostat/chemostat/morbidostat); MQTT-clustered laboratory device fleets where each unit is autonomous but coordinated. Specifically prior art against any patent claiming 'a networked low-cost bioreactor with on-board OD sensing controlled via a single-board computer running open-source bioprocess automation software with cluster coordination via lightweight pub/sub messaging.'
