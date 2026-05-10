---
title: continuous-jet-Rayleigh-breakup
parent: Cross-cuts
layout: default
---

# Cross-cut: `continuous-jet-Rayleigh-breakup`

**8 corpus entries disclose this subsystem.**

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

## KGK (Konishi Engineering) Jet Series Continuous Inkjet Coder (1995)

- **id**: `kgk-jet-cij-coder`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: KGK Co., Ltd. (Konishi Engineering)
- **disclosure**: KGK Co. Ltd. (Konishi Engineering) corporate history 1995; CCS-3000 product datasheet; KGK Jetrix product brochure 2005
- **ip status**: patented
- **prior art notes**: Japanese CIJ implementation with full Hitachi-equivalent fluidic stack but distinct mechanical packaging: integrated reservoir+pump+printhead unit using KGK's compact pump and a proprietary nozzle anti-clog drying cap. Anticipates: industrial CIJ coders with integrated single-enclosure ink-reservoir + pump + printhead form factors targeting Japanese SMEs.

## Linx 7900 Continuous Inkjet Coder (2010)

- **id**: `linx-7900-cij-coder`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Linx Printing Technologies (subsidiary of Danaher Corporation, Product Identification Platform)
- **disclosure**: Linx Printing Technologies 7900-series datasheet 2010 (Linx Printing Technologies Ltd, St Ives, Cambridgeshire UK); Linx Insight ink monitoring whitepaper
- **ip status**: patented
- **prior art notes**: Discloses an industrial CIJ printhead with two notable architectural primitives: (1) a FullFlush automated solvent-purge cycle that washes the nozzle and gutter with make-up fluid on every shutdown, eliminating the manual nozzle-clean ritual that historically dominated CIJ downtime; (2) RFID-tagged ink and make-up cartridges that enforce ink-formulation lock-in and prevent third-party-fluid contamination. Anticipates: industrial CIJ coders with cartridge-RFID lockout and pre-shutdown automated nozzle flush. The architectural primitive is (drop-on-demand purge cycle reusing make-up fluid + RFID-authenticated consumable). Combined with the standard CIJ stack, this defines the modern serviceable industrial coder.

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

## Domino A-Series A300 Continuous Inkjet Coder (2014)

- **id**: `domino-a300-cij-coder`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Domino Printing Sciences plc
- **disclosure**: Domino A300 product launch 2014; Domino A-Series A300+ datasheet 2017
- **ip status**: patented
- **prior art notes**: Entry-tier sibling of A400 sharing the CleanFlow printhead technology and i-Tech ink system. Anticipates: industrial CIJ coders using a common high-end printhead module across an entire price-tiered product line, with throughput and reservoir capacity differentiating SKUs.

## Linx 8900 Continuous Inkjet Coder (2015)

- **id**: `linx-8900-cij-coder`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Linx Printing Technologies (Danaher)
- **disclosure**: Linx 8900 product brochure 2015; PPMA 2015 product show announcement
- **ip status**: patented
- **prior art notes**: Extension of Linx 7900 stack: same fluidic primitives, but adds an integrated capacitive touchscreen HMI with WYSIWYG message preview and a tool-less ink/solvent cartridge change. Anticipates: industrial CIJ coders with capacitive-touchscreen-driven message authoring and tool-less consumable swap as a single integrated assembly.

## Hitachi RX2 Continuous Inkjet Coder (2018)

- **id**: `hitachi-rx2-cij-coder`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Hitachi Industrial Equipment Systems Co., Ltd.
- **disclosure**: Hitachi Industrial Equipment Systems RX2 product launch announcement 2018-09; RX-SD160W datasheet 2019
- **ip status**: patented
- **prior art notes**: Successor to UX-series, retaining identical CIJ fluidic primitives but adding: a remote-monitoring telemetry channel publishing pressure, viscosity, ink-level, and break-off-frequency to a cloud endpoint; predictive-maintenance heuristics flagging nozzle clogs from break-off-phase drift. Anticipates: cloud-instrumented industrial inkjets where the printhead is a managed asset and replacement parts are ordered automatically from telemetry. Does NOT add new fluidic mechanisms over UX, but does add the architectural primitive of (CIJ printhead + telemetry channel + predictive-maintenance trigger) as a unit.
