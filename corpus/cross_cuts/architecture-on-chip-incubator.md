---
title: architecture-on-chip-incubator
parent: Cross-cuts
layout: default
---

# Cross-cut: `architecture-on-chip-incubator`

**7 corpus entries disclose this subsystem.**

Earliest disclosure: 1932

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Brave New World Bokanovsky-process embryo hatchery (1932)

- **id**: `brave-new-world-bokanovsky-process`
- **corpus**: fictional
- **device class**: fictional-laboratory
- **creator**: Aldous Huxley
- **disclosure**: Huxley, A. Brave New World. Chatto & Windus, London, 1932.
- **ip status**: fictional
- **prior art notes**: Detailed narrative depiction of an industrialized embryo-cultivation facility with continuous-flow conveyor processing, in vitro fertilization at scale, and parallel automation of human reproductive biology. Predates IVF by 46 years and modern bioreactor design by decades. Doctrinally relevant for invalidity contention against patents claiming 'industrial-scale automated parallel cell culture' as a generic category.

## bioMérieux VITEK 2 Microbial ID/AST Test Card Fluidic Wells (2002)

- **id**: `biomerieux-vitek-2-card-fluidics`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: bioMérieux
- **disclosure**: bioMérieux VITEK 2 launch 1999; VITEK 2 Compact 2002; FDA 510(k) K022366; VITEK 2 XL launch 2009
- **ip status**: patented
- **prior art notes**: Discloses an automated microbial ID/AST card-based fluidic system: a credit-card-sized polystyrene cassette containing 64 isolated microwells, each pre-loaded with a different lyophilized substrate (sugars, amino acids, antibiotic dilutions); the card mates with a transfer tube dipped into the bacterial inoculum suspension, and the analyzer's vacuum chamber draws inoculum into all wells simultaneously; the card is then sealed and continuously incubated at 35.5 °C with kinetic optical readout (turbidity at 660 nm + colorimetric pH/redox indicators). Anticipates: vacuum-loaded multi-well microbiology cards as a fluidic primitive for parallel substrate testing; the 'transfer tube + manifold + sealed card' architecture distinguishing VITEK from microtiter plate ID systems. Foundational disclosure for automated clinical microbiology workflows.

## BD BACTEC FX Blood Culture Bottle Fluorescence Detection (referenced; predominantly BD product) (2008)

- **id**: `biomerieux-bactec-fx-bottle-fluorescence`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Becton Dickinson (BD Diagnostics)
- **disclosure**: BD BACTEC FX launch 2008; FDA 510(k) K081298; BACTEC fluorescent CO2 sensor patent US4945060 (1990)
- **ip status**: patented
- **prior art notes**: Discloses non-invasive optical detection of microbial growth in blood culture bottles via a polymer-embedded fluorescent CO2-sensitive dye disk bonded to the bottle's interior bottom; CO2 produced by metabolizing organisms diffuses into the polymer matrix, lowering pH, increasing protonation of the dye and shifting fluorescence emission. The reader monitors each bottle every 10 minutes via LED illumination through the bottle bottom and PMT detection of dye fluorescence. Anticipates: optical-bottom growth-monitoring blood culture systems (vs the displaced colorimetric Bactec NR system requiring needle-stick CO2 sampling); the architectural pattern of disposable bottle-as-sensor with continuous external optical readout — the fluidic-engineering primitive being reagent-free monitoring through a polymer membrane.

## Open Insulin Foundation (2015)

- **id**: `open-insulin-foundation`
- **corpus**: open
- **device class**: other
- **creator**: Open Insulin Foundation (Di Franco A., Loop J. et al.)
- **disclosure**: Open Insulin Project founded 2015 at Counter Culture Labs (Oakland) by Anthony Di Franco et al.; spun out as Open Insulin Foundation 2020; https://openinsulin.org; documented in Selk Bio (2018), Wired (2017), and the GitLab repo https://gitlab.com/open-insulin
- **ip status**: open-copyleft
- **prior art notes**: Discloses an open-source process for producing biosimilar insulin in a community-lab setting, including: cloning of proinsulin into E. coli BL21 / Pichia, fermentation in low-cost (Chi.Bio / Pioreactor scale) bioreactors, lysis, refolding, and IMAC + ion-exchange purification on open-hardware chromatography. The published protocols and process flowsheets are intentionally a 102/103 publication against any 'small-batch insulin production' patent. Specifically prior art against any post-2018 patent claiming 'a community-scale or distributed insulin production process using benchtop bioreactors and open chromatography hardware.'

## Kim Stanley Robinson Aurora generation-ship life-support cell handling (2015)

- **id**: `ksr-aurora-life-support`
- **corpus**: fictional
- **device class**: fictional-laboratory
- **creator**: Kim Stanley Robinson
- **disclosure**: Robinson, K. S. Aurora. Orbit, New York, 2015. ISBN 978-0-316-09810-6.
- **ip status**: fictional
- **prior art notes**: Aurora (2015) provides extensive technical exposition on closed-cycle generation-ship life-support including bioreactor cell handling, ecological homeostasis, and automated substrate maintenance. Robinson's depiction includes specific failure modes and chemistry-management challenges that constitute element-level disclosure of long-duration closed-cycle biological-platform architecture. §102 category disclosure of 'long-duration closed-cycle biological life-support platform with automated cell-and-substrate maintenance'. Relevant prior art for bioreactor-platform patents claiming long-duration autonomous operation as a novel architectural property.

## Pioreactor (2021-09)

- **id**: `pioreactor-open-bioreactor`
- **corpus**: open
- **device class**: other
- **creator**: Pioreactor (Cameron Lab / Pioreactor Inc., Toronto)
- **disclosure**: Cadart C., Bartlett J. et al., Pioreactor open-source hardware release on GitHub https://github.com/Pioreactor/pioreactor (initial public release Sept 2021); pioreactor.com product page; documentation site docs.pioreactor.com
- **ip status**: open-permissive
- **prior art notes**: Discloses an open-source benchtop bioreactor platform built around a Raspberry Pi HAT (the Pioreactor 'Pioreactor HAT'), which integrates: (a) an LED+photodiode optical density measurement subsystem with synchronous detection (LED chopping plus lock-in style demodulation) on a low-cost MCU; (b) a magnetic stirrer driven by a brushless DC motor with closed-loop RPM control via a Hall sensor; (c) a heating element on a PCB underneath a 20 mL borosilicate glass vial with thermistor feedback; (d) a peristaltic-pump dosing module driven over I2C for continuous-culture (turbidostat/chemostat/morbidostat) operation; (e) a clustered control architecture using MQTT pub/sub over Wi-Fi enabling fleet operation of dozens of units from a single 'leader' Pi. All hardware schematics (KiCad), firmware, mechanical CAD, and Python control software are released under MIT (software) and CERN-OHL-S/CC-BY (hardware). Anticipates: low-cost networked bioreactor fleets with synchronous-detection turbidity sensing on a Raspberry Pi class device; pluggable Python automation classes for closed-loop bioprocess control (turbidostat/chemostat/morbidostat); MQTT-clustered laboratory device fleets where each unit is autonomous but coordinated. Specifically prior art against any patent claiming 'a networked low-cost bioreactor with on-board OD sensing controlled via a single-board computer running open-source bioprocess automation software with cluster coordination via lightweight pub/sub messaging.'

## Annalee Newitz The Terraformers terraforming biological-platform infrastructure (2023)

- **id**: `newitz-terraformers-bio-platform`
- **corpus**: fictional
- **device class**: fictional-laboratory
- **creator**: Annalee Newitz
- **disclosure**: Newitz, A. The Terraformers. Tor Books, New York, 2023. ISBN 978-1-250-22802-9.
- **ip status**: fictional
- **prior art notes**: The Terraformers (2023) depicts in detail planetary-scale ecological-engineering platforms operated by the Environmental Rescue Team, including long-duration ecosystem monitoring, engineered-species deployment, and integrated bio-platform infrastructure. Architectural category disclosure of 'planetary-scale long-duration ecological-engineering bioplatform with integrated monitoring and deployment infrastructure'.
