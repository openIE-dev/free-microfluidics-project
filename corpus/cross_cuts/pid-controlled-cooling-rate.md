---
title: pid-controlled-cooling-rate
parent: Cross-cuts
layout: default
---

# Cross-cut: `pid-controlled-cooling-rate`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 1980s

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Thermo Scientific CryoMed Controlled-Rate Freezer (TSV Series) (1980s)

- **id**: `cryomed-tsv-controlled-rate-freezer`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Thermo Fisher Scientific Inc. (CryoMed brand)
- **disclosure**: Forma Scientific CryoMed (acquired by Thermo Scientific); CryoMed 7452 datasheet rev 2024
- **ip status**: trade-secret
- **prior art notes**: Discloses a CryoMed-branded family of LN2-vapor-injection controlled-rate freezers, providing a US alternative to Planer Kryo for CGT cryopreservation. Anticipates: vendor-diverse LN2-vapor-injection controlled-rate freezer ecosystem; the architectural pattern is essentially identical to Planer (LN2 vapor + thermocouple + PID), but multi-vendor availability is critical for global CGT manufacturing supply-chain redundancy.

## Planer Plc Kryo 1060 Controlled-Rate Freezer (1990s)

- **id**: `planer-kryo-1060-controlled-rate-freezer`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Planer Plc (Asahi Kasei subsidiary)
- **disclosure**: Planer Plc Kryo series controlled-rate freezers (UK) launched 1990s; Kryo 1060 datasheet rev 2024
- **ip status**: patented
- **prior art notes**: Discloses a liquid-nitrogen-vapor-injection controlled-rate freezer with PID-controlled cooling-rate feedback, supporting user-programmable multi-step cooling profiles for CGT and reproductive cell cryopreservation. Anticipates: LN2-vapor-injection controlled-rate freezer architectures for CGT cryopreservation; specifically the architectural pattern of insulated-chamber + LN2-vapor-injection-valve + thermocouple-feedback PID control, contrasting with thermoelectric (Asymptote) approaches. Higher cooling-rate capability than Peltier systems makes Planer suitable for protocols requiring >5°C/min cooling.
