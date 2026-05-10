---
title: neural-network-particle-classification
parent: Cross-cuts
layout: default
---

# Cross-cut: `neural-network-particle-classification`

**3 corpus entries disclose this subsystem.**

Earliest disclosure: 2015

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## IDEXX SediVue Dx Urine Sediment Analyzer (2015)

- **id**: `idexx-sedivue-dx-urinalysis-ml`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: IDEXX Laboratories, Inc.
- **disclosure**: IDEXX SediVue Dx product launch 2015; IDEXX operator's guide; US patent 9,470,673 (capillary-fed sediment imaging cuvette); US patent 10,533,990 (deep-learning sediment classification)
- **ip status**: patented
- **prior art notes**: Discloses a microfluidic urinalysis cartridge consisting of an injection-molded thermoplastic cuvette with a defined sedimentation chamber and optical viewing window. Sample is drawn by capillary action, allowed to sediment briefly, then imaged through brightfield/darkfield optics; a convolutional neural network classifies sediment particles. Anticipates: the architectural pattern of disposable optical-window microfluidic cuvettes coupled with on-instrument deep-learning classification of imaged particles; capillary-fed sedimentation chambers with defined geometry for in-clinic urine sediment analysis; and end-to-end POC-cartridge-plus-neural-net urinalysis workflows.

## Heska Element AIM (Automated Image Microscopy) (2019)

- **id**: `heska-element-aim-image-cytometry`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Heska Corporation
- **disclosure**: Heska Element AIM product launch 2019; Heska operator's manual; US patent 10,176,360 (deep-learning blood-smear classification)
- **ip status**: patented
- **prior art notes**: Discloses a Heska-branded automated digital microscopy platform that captures whole-slide images of stained blood, fecal, and cytology slides and applies a convolutional neural network for cell classification and morphology flagging. Anticipates: cartridge-style microscope-slide consumables paired with on-instrument deep-learning differential counting; veterinary cytology workflows in which AI flagging triggers cloud second-opinion review; and the architectural pattern of a smear-slide as a passive microfluidic substrate for automated POC image analysis.

## Zoetis Vetscan Imagyst AI Diagnostic Platform (extended) (2020)

- **id**: `zoetis-imagyst-ai-fecal-blood-smear`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Zoetis Inc.
- **disclosure**: Zoetis Imagyst product launch 2020; Zoetis Imagyst Fecal/Blood-Smear/Equine FEC application notes; US patent 11,049,242 (Antech AI parasitology, joint program)
- **ip status**: patented
- **prior art notes**: Extends earlier Imagyst entry to cover the Fecal Flotation, Blood-Smear, Ear-Cytology, and Equine FEC modules. Discloses an automated z-stack scanning microscope that uploads tile sets to a cloud CNN for parasite ova counting and cytology classification; the slide and coverslip act as a passive microfluidic substrate. Anticipates: cloud-CNN-back-ended POC veterinary cytology architectures; multi-application reuse of a single robotic microscope for parasitology and morphology workflows; and the pattern of station+cloud split between sample handling and AI inference.
