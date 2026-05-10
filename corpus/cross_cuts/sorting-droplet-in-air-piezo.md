---
title: sorting-droplet-in-air-piezo
parent: Cross-cuts
layout: default
---

# Cross-cut: `sorting-droplet-in-air-piezo`

**4 corpus entries disclose this subsystem.**

Earliest disclosure: 2013

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Sony SH800 Microfluidic Cell Sorter (2013)

- **id**: `sony-sh800-microfluidic-cell-sorter`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Sony Biotechnology Inc. (formerly iCyt acquisition)
- **disclosure**: Sony Biotechnology SH800 launch 2013; product brochure SH800S; US patent 9,134,221
- **ip status**: patented
- **prior art notes**: SH800 discloses a flow cytometric cell sorter built around a single-use, factory-aligned microfluidic sort chip integrating the flow cell, nozzle, and piezoelectric droplet break-off transducer. Anticipates: (i) disposable-microfluidic-chip cell sorters with chip-encoded calibration parameters; (ii) cartridge-based contamination isolation in FACS workflows; (iii) automated nozzle-size selection via cartridge ID. Lineage-distinct from BD FACSAria (manual stainless nozzle) and NanoCellect WOLF (cartridge with no droplet-in-air sort).

## ThinkCyte VisionSort / Image-Activated Cell Sorter (Ota 2018) (2018-06)

- **id**: `ota-thinkcyte-2018-image-activated-sort`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: Sadao Ota et al. (U Tokyo, ThinkCyte)
- **disclosure**: Nitta N., Sugimura T., Isozaki A., Mikami H., Hiraki K., Sakuma S., Iino T., Arai F., Endo T., Fujiwaki Y., Fukuzawa H., Hase M., Hayakawa T., Hiramatsu K., Hoshino Y., Inaba M., Inoue T., Ito T., Karakawa H., Kasai Y., Koizumi K., Lee S., Lei C., Li M., Maeno T., Matsusaka S., Murakami D., Nakagawa A., Oguchi Y., Oikawa M., Ota T., et al., Cell 175:266 (2018), doi:10.1016/j.cell.2018.08.028
- **ip status**: patented
- **prior art notes**: Discloses an image-activated cell sorter (IACS) in which a high-frame-rate camera or compressed-sensing optical system captures cell images on the fly, a GPU performs deep-learning classification within the residence time, and a piezo droplet sorter executes the decision. Anticipates: (i) image-triggered FACS architectures generally; (ii) closed-loop GPU-inference sort pipelines; (iii) ghost cytometry compressed-sensing optical front-ends. Academic ancestor of bd-facsdiscover-s8-imaging-sorter and ThinkCyte VisionSort commercial product.

## Beckman Coulter CytoFLEX SRT Cell Sorter (2020)

- **id**: `beckman-cytoflex-srt-microfluidic-sort`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Beckman Coulter Life Sciences
- **disclosure**: Beckman Coulter Life Sciences CytoFLEX SRT launch 2020; product brochure CYTOFLEX-SRT-BR-EN-V2; US patent 9,470,617
- **ip status**: patented
- **prior art notes**: CytoFLEX SRT discloses a benchtop cell sorter with avalanche-photodiode-array detection (WDM optical bench) and piezo-driven droplet deflection sort, packaged in a compact form factor for research labs. Anticipates: (i) compact APD-array detection bench layouts in cell sorters; (ii) the WDM optical decomposition of fluorescence signals; (iii) productized benchtop sort instruments distinct from full FACS towers. Sister to Sony SH800 and Cytek Aurora CS but with different detection optics.

## BD FACSDiscover S8 Imaging Cell Sorter (2022-12)

- **id**: `bd-facsdiscover-s8-imaging-sorter`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Becton Dickinson (BD) Biosciences
- **disclosure**: BD Biosciences FACSDiscover S8 launch press release Dec 2022; CellView Image Technology white paper 2022; Schraivogel D. et al. (BD/EMBL collaboration) Science 375:315 (2022), doi:10.1126/science.abj3013
- **ip status**: patented
- **prior art notes**: BD FACSDiscover S8 discloses a flow cytometric sorter that acquires a high-content image (multispectral fluorescence + scatter) of every passing cell at >15,000 cells/sec and uses image-derived features (subcellular localization, morphology) as sort decision inputs. Anticipates: (i) imaging-enabled FACS with sub-millisecond image classification feeding the sort decision; (ii) integration of spectral unmixing with imaging in a flow stream; (iii) use of image-based machine-learning sort gates. Predecessor academic disclosures: Schraivogel 2022 Science (Image-Activated Cell Sorting at EMBL), and ThinkCyte VisionSort (Ota 2018 Science).
