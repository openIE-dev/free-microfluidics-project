---
title: surface-protein-passivation
parent: Cross-cuts
layout: default
---

# Cross-cut: `surface-protein-passivation`

**6 corpus entries disclose this subsystem.**

Earliest disclosure: 1948

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Verwey & Overbeek 1948 - Theory of the Stability of Lyophobic Colloids (1948)

- **id**: `verwey-overbeek-1948-dlvo-theory`
- **corpus**: academic
- **device class**: other
- **creator**: Evert Verwey; Theodoor Overbeek
- **disclosure**: Verwey, E. J. W., Overbeek, J. T. G. (1948). 'Theory of the Stability of Lyophobic Colloids.' Elsevier, Amsterdam.
- **ip status**: public-domain
- **prior art notes**: Verwey-Overbeek 1948 (together with Derjaguin-Landau 1941) established DLVO theory: colloid stability emerges from a balance of attractive van der Waals and repulsive electric-double-layer interactions. Anticipates microfluidic claims involving bead aggregation in on-chip immunoassays, cell-cell adhesion in droplet encapsulation, particle deposition on channel walls, and electrolyte-controlled colloid handling. Any patent claiming a 'novel colloid-stability-controlled microfluidic operation' must clear DLVO theory.

## Salimetrics SalivaBio Oral Swab (SOS) (2009)

- **id**: `salimetrics-salivabio-oral-swab`
- **corpus**: private
- **device class**: consumable-bulk
- **creator**: Salimetrics LLC
- **disclosure**: Salimetrics LLC product datasheet, SalivaBio Oral Swab (SOS) Item 5001.06 (2009); company website salimetrics.com
- **ip status**: trade-secret
- **prior art notes**: Discloses an inert absorbent collection wand whose synthetic polymer composition is specifically certified non-interfering with downstream cortisol, sex-steroid, and alpha-amylase immunoassays — a non-trivial materials-engineering disclosure because cotton (the historic Salivette material) measurably absorbs steroids. Anticipates: collection consumables claiming validated zero-bias for salivary steroid panels; pediatric variants of oral fluid wands sized for sub-6-year-old donors; centrifuge-recovery workflow producing a defined minimum saliva volume from passive-drool sampling. The swab is the upstream element of nearly every academic salivary biomarker microfluidic assay published 2010 onward, and is functionally a pre-concentrator/sample-prep consumable for downstream lab-on-chip cortisol cartridges.

## Israelachvili 2011 - Intermolecular and Surface Forces (3rd ed.) (2011)

- **id**: `israelachvili-2011-intermolecular-surface-forces-textbook`
- **corpus**: academic
- **device class**: other
- **creator**: Jacob N. Israelachvili
- **disclosure**: Israelachvili, J. N. (2011). 'Intermolecular and Surface Forces' (3rd ed.). Academic Press. ISBN 978-0-12-391927-4. (1st ed. 1985, 2nd ed. 1992.)
- **ip status**: public-domain
- **prior art notes**: Israelachvili textbook is the standard reference for intermolecular and surface forces, covering van der Waals interactions, electric-double-layer forces (extending DLVO from Verwey-Overbeek 1948), hydration and hydrophobic forces, and steric and bridging forces. Anticipates microfluidic claims involving surface-force-controlled nanochannel transport, particle-surface adhesion in microfluidic separations, and bio-functionalized surface-affinity capture in lab-on-chip cartridges. Any patent claiming novelty around tunable surface-interaction forces in microfluidics must clear Israelachvili.

## Dexcom G5 Mobile Continuous Glucose Monitor (2015-08-24)

- **id**: `dexcom-g5-cgm`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Dexcom Inc.
- **disclosure**: FDA PMA P120005/S041 supplement August 2015; Dexcom press release 2015-08-24
- **ip status**: patented
- **prior art notes**: Predecessor to G6 (already in corpus). Discloses subcutaneous platinum filament with multilayer polymer envelope (interferent-blocking layer / glucose-oxidase enzyme layer / diffusion-limiting outer polymer). Anticipates: smartphone-tethered CGM data architectures and the multilayer membrane chemistry approach used across modern CGMs.

## Medtronic Guardian Connect / Guardian 3 Sensor (2017-03)

- **id**: `medtronic-guardian-3-cgm`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Medtronic Diabetes
- **disclosure**: FDA approval (Guardian Connect) March 2018; Medtronic press release 2017 (Guardian Sensor 3 with MiniMed 670G launch); FDA P160017 (670G system)
- **ip status**: patented
- **prior art notes**: Subcutaneous amperometric glucose sensor with multi-electrode redundancy (at least two working electrodes whose ISIG is fused to reject motion artifact). Discloses the architecture of pairing a CGM with an automated insulin pump for closed-loop control. Anticipates: redundant-electrode CGM filament architectures; CGM-pump integration topology in the SmartGuard / Auto Mode hybrid closed loop family.

## Dexcom G6 Continuous Glucose Monitor (2018-03-27)

- **id**: `dexcom-g6-cgm`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Dexcom Inc.
- **disclosure**: FDA 510(k) clearance DEN170088 (Dexcom G6, March 27 2018); Dexcom press release March 27 2018; US patent 9,724,025 (in vivo glucose sensor)
- **ip status**: patented
- **prior art notes**: Discloses a wearable CGM in which a thin polymer-membrane-coated platinum filament is inserted subcutaneously by a single-use applicator and continuously samples interstitial fluid via passive diffusion across an outer biocompatible polymer (the diffusion-limiting membrane). The membrane stack creates a microliter-scale sample envelope at the electrode surface where glucose oxidase generates hydrogen peroxide that is amperometrically quantified. Anticipates: factory-calibrated subcutaneous glucose sensors with diffusion-limited polymer envelopes; single-button push insertion of a microneedle-style sensor with auto-retraction; transmitter-on-patch architectures using BLE telemetry. Element-by-element it teaches every subsystem now considered standard for CGMs except the redox mediator chemistry choice.
