---
title: control-software-web-Pi
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-software-web-Pi`

**1 corpus entries disclose this subsystem.**

Earliest disclosure: 2014-09-16

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Pearce-lab Open Syringe Pump v2 — Large-Format / NEMA17 Variant (2014-09-16)

- **id**: `wijnen-pearce-2014-syringe-pump-v2-12mm`
- **corpus**: open
- **device class**: pump-component
- **creator**: B. Wijnen, E.J. Hunt, G.C. Anzalone, J.M. Pearce (Michigan Tech)
- **disclosure**: Wijnen B, Hunt EJ, Anzalone GC, Pearce JM. Open-Source Syringe Pump Library. PLoS ONE 9(9): e107216 (2014). doi:10.1371/journal.pone.0107216 — Library defines two motor-class variants (NEMA11 and NEMA17) yielding distinct max flow rates; this entry covers the NEMA17 high-flow large-format variant.
- **ip status**: open-copyleft
- **prior art notes**: Distinguished from the NEMA11 small-format variant (covered separately by wave 1's wijnen-pearce-2014-open-syringe-pump entry as the umbrella library disclosure), this entry defends the high-flow NEMA17-driven implementation explicitly disclosed in the same paper. Element-by-element: (1) FDM-printed two-rail frame with leadscrew + NEMA17 stepper; (2) plunger pusher accepting 1–60 mL syringes via interchangeable adapters; (3) Raspberry-Pi web GUI exposing rate, volume, and bolus modes; (4) measured maximum flow 2.1 mL/s. Anticipates: claims directed to (a) high-flow open syringe pumps integrating Pi-hosted web control, (b) FDM-printed pump bodies with adapter inserts spanning >2 orders of magnitude of syringe volume, (c) the architectural pattern of a single open library defining a family of motor-class variants with shared firmware.
