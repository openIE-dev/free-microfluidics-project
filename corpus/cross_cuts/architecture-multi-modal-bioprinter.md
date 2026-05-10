---
title: architecture-multi-modal-bioprinter
parent: Cross-cuts
layout: default
---

# Cross-cut: `architecture-multi-modal-bioprinter`

**3 corpus entries disclose this subsystem.**

Earliest disclosure: 2014

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## 3D Bioprinting Solutions FABION Multi-Material Bioprinter (2014)

- **id**: `3d-bioprinting-solutions-fabion`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: 3D Bioprinting Solutions LLC (Moscow, sister to INVITRO clinical lab network)
- **disclosure**: 3D Bioprinting Solutions (Moscow, Russia) FABION launch 2014; FABION printer datasheet; FABION 2 announcement 2018
- **ip status**: patented
- **prior art notes**: Russian bioprinter platform notable for the Organ.Aut spinoff, which used magnetic-levitation assembly (rather than extrusion) of cell aggregates in microgravity aboard the ISS. The terrestrial FABION uses conventional multi-printhead extrusion. Anticipates: multi-material bioprinters with 5+ printhead positions and temperature-controlled cartridges; separately, anticipates magnetic-levitation cell-aggregate assembly bioprinting in microgravity (Organ.Aut variant). Important prior art for both terrestrial multi-modal bioprinting and microgravity tissue assembly claims.

## BICO BIO X Pneumatic / Thermoplastic / Photocuring Printhead Family (extended) (2017)

- **id**: `bico-bio-x-pneumatic-printhead-extended`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: BICO Group AB (CELLINK division)
- **disclosure**: CELLINK BIO X launch 2017; BIO X printhead family technical specifications 2018; CELLINK printhead datasheets covering pneumatic, thermoplastic, photocuring, electromagnetic-droplet, syringe-pump variants
- **ip status**: patented
- **prior art notes**: Extension to wave 1 cellink-bio-x-pneumatic-printhead. Discloses the broader BIO X printhead architectural family: a single XYZ frame (the BIO X printer) accepts a range of interchangeable printhead tools, each implementing different deposition physics (pneumatic extrusion, thermoplastic FDM, photocuring extrusion, electromagnetic droplet, syringe pump). Anticipates: bioprinters using a tool-changer architecture where multiple deposition modalities share a common positioning stage and registration frame, allowing a single build to combine extrusion + droplet + photocuring deposition in registered coordinates. The architectural primitive is (common XYZ frame + interchangeable tool-mount + registered tool-coordinate-system + multiple deposition-physics tools) as a complete multi-modal bioprinter category.

## BICO BIO X6 Six-Tool Bioprinter (2019)

- **id**: `bico-bio-x6-six-tool-bioprinter`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: BICO Group AB (CELLINK division)
- **disclosure**: CELLINK BIO X6 launch 2019; BIO X6 product datasheet 2019
- **ip status**: patented
- **prior art notes**: Discloses a bioprinter architecture extending the multi-modal printhead concept to 6 simultaneous tool positions on a shared frame. Anticipates: bioprinters with N-position tool changers (N>=6) where each position can mount any of multiple deposition modalities. Defends against bioprinter claims based on the count of simultaneous deposition tools. The architectural primitive is the (N>=6 tool changer + registered tool coordinate system + automated mid-build tool change) configuration as a complete multi-material multi-modal bioprinter.
