---
title: rfid-authenticated-consumable
parent: Cross-cuts
layout: default
---

# Cross-cut: `rfid-authenticated-consumable`

**1 corpus entries disclose this subsystem.**

Earliest disclosure: 2010

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Linx 7900 Continuous Inkjet Coder (2010)

- **id**: `linx-7900-cij-coder`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Linx Printing Technologies (subsidiary of Danaher Corporation, Product Identification Platform)
- **disclosure**: Linx Printing Technologies 7900-series datasheet 2010 (Linx Printing Technologies Ltd, St Ives, Cambridgeshire UK); Linx Insight ink monitoring whitepaper
- **ip status**: patented
- **prior art notes**: Discloses an industrial CIJ printhead with two notable architectural primitives: (1) a FullFlush automated solvent-purge cycle that washes the nozzle and gutter with make-up fluid on every shutdown, eliminating the manual nozzle-clean ritual that historically dominated CIJ downtime; (2) RFID-tagged ink and make-up cartridges that enforce ink-formulation lock-in and prevent third-party-fluid contamination. Anticipates: industrial CIJ coders with cartridge-RFID lockout and pre-shutdown automated nozzle flush. The architectural primitive is (drop-on-demand purge cycle reusing make-up fluid + RFID-authenticated consumable). Combined with the standard CIJ stack, this defines the modern serviceable industrial coder.
