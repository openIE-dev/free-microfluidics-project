---
title: electrostatic-drop-deflection
parent: Cross-cuts
layout: default
---

# Cross-cut: `electrostatic-drop-deflection`

**4 corpus entries disclose this subsystem.**

Earliest disclosure: 1992

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Imaje S8 Master Continuous Inkjet Coder (historical) (1992)

- **id**: `imaje-s8-master-cij-coder-historical`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Imaje S.A. (founded by Jaime Charles)
- **disclosure**: Imaje S.A. (Bourg-les-Valence, France) S8 Master datasheet 1992; Imaje company history (founded 1981, acquired by Markem 2006 forming Markem-Imaje, now Dover)
- **ip status**: patented
- **prior art notes**: Historical anchor for the Imaje (now Markem-Imaje) industrial-coding line. Imaje pioneered French industrial CIJ in parallel to Domino (UK) and Hitachi/KGK (Japan), establishing the European industrial-coder design lineage that would later merge with Markem to form Markem-Imaje. Anticipates: pre-2000 European industrial CIJ printhead architectures using cartridge-based ink supply and 4-line text composition. Important for distinguishing wave-1 Markem-Imaje 9450 (2010s) from this earlier French ancestor; the 9450's product DNA is half Markem (US), half Imaje (FR).

## Hitachi UX-Series Continuous Inkjet Coder (2014)

- **id**: `hitachi-ux-series-cij-coder`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Hitachi Industrial Equipment Systems Co., Ltd.
- **disclosure**: Hitachi Industrial Equipment Systems UX-Series product brochure 2014; Hitachi UX-D160W datasheet rev 2016; SMBC press release on UX line refresh
- **ip status**: patented
- **prior art notes**: Discloses a complete industrial CIJ printhead architecture: piezo crystal stimulating a single nozzle at the Rayleigh frequency to produce uniform monodisperse drops; selective charging electrode synced to drop break-off; high-voltage deflection plates; uncharged-drop catcher and gutter return loop; ink/make-up solvent reservoir with viscosity feedback. Anticipates: any single-nozzle CIJ coder using Hitachi-style charge-tunnel timing reference and gutter-recirculation loop with make-up-solvent dosing under closed-loop viscosity control. The architectural primitive is the closed loop of (drop generation -> selective charging -> deflection -> catcher -> filtered return -> viscosity-corrected re-injection), which together define an industrial-coding CIJ as distinct from a graphic-arts continuous inkjet.

## Domino A-Series A400 Continuous Inkjet Coder (2014)

- **id**: `domino-a400-cij-coder`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Domino Printing Sciences plc (Brother Industries subsidiary since 2015)
- **disclosure**: Domino Printing Sciences A-Series Ax-Series launch 2014; Domino A400i datasheet 2015; Domino A-Series 'i-Tech' whitepaper
- **ip status**: patented
- **prior art notes**: Discloses an industrial CIJ printhead innovation: a positive-pressure air curtain delivered around the nozzle and through the printhead body that scavenges solvent vapor and prevents fugitive-ink-mist accretion on the orifice plate (the dominant failure mode for high-duty-cycle CIJ). Anticipates: industrial CIJ printheads using an integral airflow channel concentric or adjacent to the ink jet to actively keep the orifice plate clean during operation. The architectural primitive is the CleanFlow geometry: an air channel co-routed with the ink delivery channel inside the printhead, terminating at the nozzle face, exhausting through the printhead snout. Also anticipates the modular sealed ink-system cartridge that can be swapped without bleeding the system.

## Hitachi RX2 Continuous Inkjet Coder (2018)

- **id**: `hitachi-rx2-cij-coder`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Hitachi Industrial Equipment Systems Co., Ltd.
- **disclosure**: Hitachi Industrial Equipment Systems RX2 product launch announcement 2018-09; RX-SD160W datasheet 2019
- **ip status**: patented
- **prior art notes**: Successor to UX-series, retaining identical CIJ fluidic primitives but adding: a remote-monitoring telemetry channel publishing pressure, viscosity, ink-level, and break-off-frequency to a cloud endpoint; predictive-maintenance heuristics flagging nozzle clogs from break-off-phase drift. Anticipates: cloud-instrumented industrial inkjets where the printhead is a managed asset and replacement parts are ordered automatically from telemetry. Does NOT add new fluidic mechanisms over UX, but does add the architectural primitive of (CIJ printhead + telemetry channel + predictive-maintenance trigger) as a unit.
