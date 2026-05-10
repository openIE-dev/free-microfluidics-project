---
title: software-ML-inverse-design
parent: Cross-cuts
layout: default
---

# Cross-cut: `software-ML-inverse-design`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2021-01-06

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## DAFD — Design Automation of Flow-Focusing Droplet Generators (2021-01-06)

- **id**: `lashkaripour-2021-dafd-droplet-design-automation`
- **corpus**: open
- **device class**: droplet-generator
- **creator**: Ali Lashkaripour, Douglas Densmore et al. (Boston University CIDAR Lab)
- **disclosure**: Lashkaripour A, Rodriguez C, Mehdipour N, Mardian R, McIntyre D, Ortiz L, Campbell J, Densmore D. Machine learning enables design automation of microfluidic flow-focusing droplet generation. Nature Communications 12: 25 (2021). doi:10.1038/s41467-020-20284-z
- **ip status**: open-permissive
- **prior art notes**: Discloses element-by-element an inverse-design pipeline: (1) parameterized geometry of a flow-focusing droplet generator, (2) supervised ML model trained on experimental droplet datasets predicting diameter and generation rate, (3) automated search over geometry + flow rates given user-specified targets, (4) public web deployment generating ready-to-fabricate device files, (5) successor versions covering versatility/stability metrics and aqueous-in-oil + oil-in-aqueous double emulsions. Anticipates: (a) ML inverse-design claims for droplet-microfluidic devices, (b) automated design of double-emulsion generators, (c) cloud-deployed microfluidic CAD generating chip files from performance specs, (d) using neural ensembles plus search algorithms to deliver targeted droplet morphology — published two-plus years before most commercial assertions in this niche.

## DAFD 3.0 — Double-Emulsion Droplet Design Automation (2024-01-02)

- **id**: `lashkaripour-2024-dafd-double-emulsion`
- **corpus**: open
- **device class**: droplet-generator
- **creator**: Ali Lashkaripour, Polly Fordyce, Douglas Densmore et al. (Stanford / Boston University)
- **disclosure**: Lashkaripour A, McIntyre DP, Calhoun SGK, Krauth K, Densmore D, Fordyce PM. Design automation of microfluidic single and double emulsion droplets with machine learning. Nature Communications 15: 83 (2024). doi:10.1038/s41467-023-44068-3
- **ip status**: open-permissive
- **prior art notes**: Distinct from the 2021 DAFD 1.0 disclosure, this entry pins the 2024 extension to double emulsions. Element-by-element discloses: (1) parameterised geometry library for single + double-emulsion flow-focusing devices, (2) consensus ensemble ML model trained on experimental droplet datasets, (3) automated search returning device geometry + flow-rate setpoints for user-targeted single or double-emulsion morphology, (4) open web deployment generating fab-ready files. Anticipates: claims directed to inverse-design of double-emulsion droplet generators, ML-driven design automation for W/O/W and O/W/O architectures, and cloud-served device-design APIs covering both emulsion classes.
