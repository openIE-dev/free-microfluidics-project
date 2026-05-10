---
title: interface-smartphone-android
parent: Cross-cuts
layout: default
---

# Cross-cut: `interface-smartphone-android`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2015-08-06

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Wittbrodt–Pearce 2015 Open-Source Enzymatic Nitrate Photometer (2015-08-06)

- **id**: `wittbrodt-2015-open-nitrate-photometer`
- **corpus**: open
- **device class**: flow-controller
- **creator**: B.T. Wittbrodt, D.A. Squires, J. Walbeck, E. Campbell, W.H. Campbell, J.M. Pearce (Michigan Tech / NECi Superior Enzymes)
- **disclosure**: Wittbrodt BT, Squires DA, Walbeck J, Campbell E, Campbell WH, Pearce JM. Open-Source Photometric System for Enzymatic Nitrate Quantification. PLoS ONE 10(8): e0134989 (2015). doi:10.1371/journal.pone.0134989
- **ip status**: open-copyleft
- **prior art notes**: Discloses a 3D-printed Arduino+Android photometric system that, in combination with NECi nitrate-reductase enzyme chemistry, replaces toxic Cd-reduction reagents and matches the performance of commercial nitrate photometers at 15% of the cost. Element-by-element it discloses: (1) printed cuvette holder; (2) bicolour LED illumination; (3) Arduino acquisition firmware; (4) Bluetooth/USB Android-side data pipeline; (5) the integration with enzyme cartridge chemistry. Anticipates: (a) field-deployable enzymatic nitrate photometers paired with phone-side data infrastructure; (b) the architectural pattern of LED + photodiode + open MCU + smartphone for environmental colorimetric assay readers; (c) the elimination of cadmium chemistry by combining open hardware with enzyme reagents.

## UWED — Universal Wireless Electrochemical Detector for Smartphones (2018-04-12)

- **id**: `ainla-2018-uwed-wireless-potentiostat`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Alar Ainla et al., George M. Whitesides group (Harvard)
- **disclosure**: Ainla A, Mousavi MPS, Tsaloglou MN, Redston J, Bell JG, Fernández-Abedul MT, Whitesides GM. Open-Source Potentiostat for Wireless Electrochemical Detection with Smartphones. Anal. Chem. 90(10): 6240–6246 (2018). doi:10.1021/acs.analchem.8b00850
- **ip status**: open-permissive
- **prior art notes**: Element-by-element discloses: (1) BLE-equipped potentiostat PCB with documented analog front-end including DAC, transimpedance amplifier and instrumentation amp; (2) Android application implementing parameter control, real-time visualization and cloud upload; (3) tested with paper-microfluidic glucose, lactate and chloride sensors. Anticipates: (a) claims directed to wireless smartphone-tethered potentiostats for paper-microfluidic readers, (b) the architectural pattern of BLE-MCU + analog front-end + smartphone host as a defensible primitive in connected POC electrochemistry, (c) integration of cloud upload pipelines with disposable paper electrochemical cartridges.
