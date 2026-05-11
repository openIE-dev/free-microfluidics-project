---
title: dmf-addressable-electrode-array
parent: Cross-cuts
layout: default
---

# Cross-cut: `dmf-addressable-electrode-array`

**7 corpus entries disclose this subsystem.**

Earliest disclosure: 2000

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Electrowetting-based actuation of liquid droplets for microfluidic applications (2000)

- **id**: `pollack-2000-electrowetting-droplet`
- **corpus**: academic
- **device class**: digital-microfluidics
- **creator**: Pollack, Fair, Shenderov (Duke)
- **disclosure**: Pollack, M. G.; Fair, R. B.; Shenderov, A. D. Electrowetting-based actuation of liquid droplets for microfluidic applications. Appl. Phys. Lett. 2000, 77, 1725–1726. DOI: 10.1063/1.1308534
- **ip status**: patented
- **prior art notes**: The foundational disclosure of electrowetting-on-dielectric (EWOD) for digital microfluidics. Demonstrated discrete water-droplet transport across an addressable electrode array under voltage control. Anticipates: addressable-electrode array DMF architecture, DC + AC EWOD actuation modes, droplet-merge / droplet-split / droplet-dispense as primitives, and the Advanced Liquid Logic / Illumina commercial DMF lineage. Together with Cho 2003 it defines the EWOD field.

## Creating, transporting, cutting, and merging liquid droplets by electrowetting-based actuation (2003)

- **id**: `cho-2003-creating-transporting-cutting-merging`
- **corpus**: academic
- **device class**: digital-microfluidics
- **creator**: C.-J. Kim group, UCLA
- **disclosure**: Cho, S. K.; Moon, H.; Kim, C.-J. Creating, transporting, cutting, and merging liquid droplets by electrowetting-based actuation for digital microfluidic circuits. J. Microelectromech. Syst. 2003, 12, 70–80. DOI: 10.1109/JMEMS.2002.807467
- **ip status**: patented
- **prior art notes**: Companion foundational paper to Pollack 2000, expanding the primitive set of EWOD operations from transport to creation, cutting, and merging — i.e., the full droplet-circuit calculus. Anticipates: complete DMF instruction set (dispense, transport, split, merge), and the framing of DMF as 'digital microfluidic circuits' analogous to digital electronic circuits.

## Advanced Liquid Logic / Illumina NeoPrep digital microfluidics (2007)

- **id**: `advanced-liquid-logic-illumina-dmf`
- **corpus**: private
- **device class**: digital-microfluidics
- **creator**: Advanced Liquid Logic (acquired by Illumina)
- **disclosure**: Advanced Liquid Logic (acquired by Illumina 2013). NeoPrep system launched 2014.
- **ip status**: patented
- **prior art notes**: Commercial implementation of EWOD digital microfluidics for nucleic acid library preparation, automating a previously manual NGS sample-prep workflow on a disposable EWOD cartridge. The platform was discontinued by Illumina in 2017 but the IP position survives. Anticipates: EWOD as commercial NGS sample-prep automation, and the disposable-cartridge form factor for DMF.

## DropBot open-source digital microfluidics platform (2013)

- **id**: `dropbot-open-source-dmf`
- **corpus**: open
- **device class**: digital-microfluidics
- **creator**: Wheeler group, University of Toronto
- **disclosure**: Fobel, R.; Fobel, C.; Wheeler, A. R. DropBot: an open-source digital microfluidics control system with precise control of electrostatic driving force and instantaneous drop velocity measurement. Appl. Phys. Lett. 2013, 102, 193513. DOI: 10.1063/1.4807118
- **ip status**: open-permissive
- **prior art notes**: Disclosed an open-source DMF (digital microfluidics) control system with software, electronics, and reference EWOD chip designs released under permissive license. Anticipates: open-source EWOD instrument architecture, real-time droplet velocity feedback as a control primitive, and Python-based DMF protocol scripting.

## Illumina NeoPrep digital-microfluidic NGS library prep (2014-09-30)

- **id**: `advanced-liquid-logic-illumina-neoprep`
- **corpus**: private
- **device class**: digital-microfluidics
- **creator**: Illumina (Advanced Liquid Logic acquisition)
- **disclosure**: Illumina NeoPrep launch press release 2014-09-30; product withdrawn 2017. Pamula, V. K. et al. Advanced Liquid Logic digital microfluidic platform for sample prep. https://www.illumina.com (archived).
- **ip status**: patented
- **prior art notes**: First commercial DMF-based NGS library prep instrument: Illumina productized the Advanced Liquid Logic EWOD platform to perform end-to-end TruSeq-style library prep on 16 samples in parallel using ~700 nL droplets. Discontinued 2017 due to library-quality issues, but the disclosed architecture remains useful prior art for any later DMF-based NGS library prep claim. Anticipates: large-cohort DMF library prep on a PCB-substrate EWOD array; the 'cartridge-top + reusable electrode-bottom' architecture for DMF.

## Nuclera eProtein Discovery Platform (2022-09-01)

- **id**: `nuclera-eprotein-platform`
- **corpus**: private
- **device class**: digital-microfluidics
- **creator**: Nuclera Ltd. (Cambridge, UK; Aaron Wheeler EWOD lineage)
- **disclosure**: Nuclera Ltd. product launch announcement 2022-09; nuclera.com; Wheeler AR et al., founding patents WO2014047523A1
- **ip status**: patented
- **prior art notes**: Discloses a commercial EWOD cartridge benchtop instrument that combines cell-free protein synthesis with on-chip bead-based affinity purification. Builds on Wheeler-lab EWOD prior art. Anticipates: EWOD cartridges integrating cell-free protein synthesis; benchtop bead-purification on digital microfluidic platforms; the architectural pattern of disposable PCB-electrode cartridges for protein-engineering workflows.

## Volta Labs Desktop digital microfluidics library prep (2023)

- **id**: `volta-labs-desktop`
- **corpus**: private
- **device class**: digital-microfluidics
- **creator**: Volta Labs
- **disclosure**: Volta Labs Desktop product launch 2023. https://voltalabs.com/. Spun out of MIT Sambasivan / Wang lab work on EWOD library prep.
- **ip status**: patented
- **prior art notes**: Commercial digital-microfluidics instrument focused on NGS library prep: an EWOD electrode array under an oil-coated glass top moves discrete reagent droplets through library-prep steps without bulk channels or pipettors. Anticipates: post-Illumina-DMF-acquisition (Advanced Liquid Logic) commercial DMF for genomics; integration with kit chemistries (NEB UltraExpress) tuned for the DMF format. Major prior art point: that EWOD library prep can match conventional library quality at production NGS scale - a claim several competitors will want to make.
