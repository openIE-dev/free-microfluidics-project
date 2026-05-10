---
title: software-open-source-acquisition
parent: Cross-cuts
layout: default
---

# Cross-cut: `software-open-source-acquisition`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2020-05

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## OpenRAMAN Open-Source Raman Spectrometer (2020-05)

- **id**: `openraman-low-cost-raman-spectrometer`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Luc Cogniaux et al. (Belgium)
- **disclosure**: Cogniaux L (Open-Raman.org). OpenRAMAN — low-cost, high-performance, open-source Raman spectrometer. https://www.open-raman.org/ (initial public release 2020-05; mirror https://github.com/samyk/openraman)
- **ip status**: open-permissive
- **prior art notes**: Element-by-element discloses: (1) Czerny-Turner spectrograph optical layout with documented part list, (2) 532 nm DPSS laser excitation path with notch-filter Raman selection, (3) Toshiba TCD1304 linear CCD acquisition board firmware + USB host, (4) Python control + spectrum-export software. Anticipates: (a) claims directed to low-cost open-bench Raman spectrometers, (b) the architectural pattern of pairing TCD1304-class CCDs with open Czerny-Turner benches for sub-€2k Raman, (c) DIY drug-identification spectrometer kits for forensic and field deployment.

## Squid — Simplifying Quantitative Imaging Platform Development and Deployment (2020-12-29)

- **id**: `li-prakash-2020-squid-imaging-platform`
- **corpus**: open
- **device class**: chip-holder
- **creator**: Hongquan Li, Deepak Krishnamurthy, Ethan Li, Pranav Vyas, Nibha Akireddy, Chew Chai, Manu Prakash (Stanford / Cephla)
- **disclosure**: Li H, Krishnamurthy D, Li E, Vyas P, Akireddy N, Chai C, Prakash M. Squid: Simplifying Quantitative Imaging Platform Development and Deployment. bioRxiv 2020.12.28.424613 (2020). doi:10.1101/2020.12.28.424613
- **ip status**: open-permissive
- **prior art notes**: Discloses element-by-element a fully open modular microscope platform: (1) modular optomechanical core supporting brightfield, darkfield, phase contrast and 5-channel fluorescence with LED or laser excitation; (2) compact integrated XYZ stage with laser autofocus; (3) open firmware controlling motion, illumination and camera triggering with sub-frame latency; (4) software framework supporting tile scans, automated focus, and downstream ML classification. Subsequent Squid+ v2 release (2023+) extends with FN25 optical train and high-NA wide-field operation. Anticipates: (a) open modular microscope architectures aimed at point-of-care pathology; (b) integrated laser-autofocus modules in low-cost imagers; (c) the architectural pattern of an open firmware/software stack pairing with commodity industrial cameras to deliver Nikon/Olympus-class throughput at a fraction of the cost.
