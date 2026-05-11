---
title: fabrication-thermoplastic-laser-cutting
parent: Cross-cuts
layout: default
---

# Cross-cut: `fabrication-thermoplastic-laser-cutting`

**9 corpus entries disclose this subsystem.**

Earliest disclosure: 2002

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## MIT Center for Bits and Atoms / Fab Lab Network (2002)

- **id**: `openfoundry-cba-fab-lab-network`
- **corpus**: open
- **device class**: other
- **creator**: MIT Center for Bits and Atoms (Gershenfeld N. et al.); Fab Foundation
- **disclosure**: Gershenfeld N., MIT Center for Bits and Atoms founded 2001; first Fab Lab established 2002 (MIT/India); 'Fab: The Coming Revolution on Your Desktop' (Basic Books 2005, ISBN 978-0-465-02745-0); https://cba.mit.edu; https://fabfoundation.org; https://fablabs.io
- **ip status**: open-permissive
- **prior art notes**: Discloses a globally distributed shared-fabrication network with standardized capability that has, since 2002, hosted hundreds of community microfluidic device builds (xurography PMMA chips, paper microfluidics, laser-cut acrylic stacks). The Fab Academy student archive is itself a citable prior-art trove for low-cost fabricated microfluidic devices. Anticipates: distributed-manufacturing models for microfluidic devices, laser-cut/CNC-milled microfluidic device classes, and the institutional pattern of community labs equipped with standardized open fabrication tools.

## Nova StatStrip Glucose/Ketone Hospital Test Strip (2006)

- **id**: `nova-statstrip-glucose-strip`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Nova Biomedical
- **disclosure**: Nova Biomedical StatStrip Glucose 510(k) K061893 cleared 2006-12; first FDA-cleared glucose strip for critically ill patients (2014 K140509)
- **ip status**: patented
- **prior art notes**: Discloses a multi-electrode glucose test strip with on-strip interferent correction electrodes: in addition to the main GDH-mediator amperometric working electrode, additional working electrodes detect Hct (impedance), oxidizable interferents (acetaminophen, urate, ascorbate, dopamine), and reducing sugars (maltose, galactose, xylose), with the meter algorithm subtracting interferent contribution from glucose readout. Anticipates: multi-channel POC glucose strips with on-strip interferent correction; Hct compensation electrodes integrated into the same capillary chamber; FDA-clearable strip-based POC glucose for critically ill (where interfering substances and abnormal Hct break older single-electrode strips). Foundational to the Nova approach extending to lactate, ketone, and creatinine strips.

## ALine integrated multilayer flow cells (laminate microfluidics) (2010)

- **id**: `aline-integrated-flowcell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: ALine Inc.
- **disclosure**: ALine Inc. integrated multilayer microfluidic flow cells. https://alineinc.com/. ALine Inc. founded 2002 as a contract designer / manufacturer for laminate-based microfluidic devices.
- **ip status**: patented
- **prior art notes**: Lamination-based microfluidic manufacturing: stacked laser-cut PMMA / COC layers with pressure-sensitive-adhesive interlayers form integrated flow cells, including embedded blister reagent pouches and burst valves. Anticipates: PSA-laminate manufacturing as a third major microfluidic fabrication process category alongside soft lithography and thermoplastic injection molding; the architectural pattern of a CRO/CDMO providing both prototyping and production-scale runs of laminate flow cells. Many commercial diagnostic cartridges (including OEM cards inside larger systems) are ALine-built or ALine-architected.

## Pearce Lab MOST Open Scientific Hardware Suite (2012)

- **id**: `pearce-most-open-hardware-suite`
- **corpus**: open
- **device class**: other
- **creator**: Joshua M. Pearce (Michigan Technological University), MOST research group
- **disclosure**: Pearce J.M., 'Building Research Equipment with Free, Open-Source Hardware', Science 337:1303-1304 (2012), doi:10.1126/science.1228183; Pearce J.M., 'Open-Source Lab' (Elsevier 2014, ISBN 978-0-12-410462-4); https://www.appropedia.org/Category:MOST
- **ip status**: open-copyleft
- **prior art notes**: Discloses a foundational suite of >50 published open lab instruments from a single research group, including: open syringe pump (already cataloged separately), open peristaltic pump, open colorimeter, open spectrophotometer, open mass-balance, open magnetic stirrer hot-plate, open shaker incubator, open laser-cut/3D-printed centrifuge, open optical-density meter, open temperature-controlled stage. Each is published with full BOM, parametric CAD (typically OpenSCAD), firmware, and calibration data. Together these constitute a substantial fraction of the post-2012 open lab-equipment commons. Citable as 102 prior art against many commercial 'low-cost lab instrument' patents from 2014-2024. Specifically anticipates the architectural pattern of a research lab releasing its full instrument library as a coordinated commons under permissive licenses.

## Diagenode Megaruptor Mechanical DNA Shearing (2014)

- **id**: `diagenode-megaruptor-bead-shear`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Diagenode SA
- **disclosure**: Diagenode Megaruptor product launch 2014; product manual; Megaruptor 3 launch 2018
- **ip status**: patented
- **prior art notes**: Discloses a microfluidic shear-based DNA fragmentation platform using flow through narrow constrictions to produce reproducible long-DNA fragment distributions for long-read library prep. Anticipates: hydrodynamic-shear DNA fragmentation as a microfluidic-channel design class with channel-geometry-determined fragment-length distributions.

## Wijnen / Pearce Lab Open-Source Syringe Pump (2014-09-22)

- **id**: `wijnen-pearce-2014-open-syringe-pump`
- **corpus**: open
- **device class**: pump-component
- **creator**: Bas Wijnen, Joshua M. Pearce (Michigan Technological University, MOST/Open Sustainability Technology Lab)
- **disclosure**: Wijnen B., Hunt E.J., Anzalone G.C., Pearce J.M., 'Open-source syringe pump library', PLoS ONE 9(9):e107216, 22 Sept 2014; doi:10.1371/journal.pone.0107216; design files at https://www.appropedia.org/Open-source_syringe_pump
- **ip status**: open-copyleft
- **prior art notes**: Discloses a fully open-source 3D-printable syringe pump library: a NEMA 17 stepper motor drives an Acme threaded rod that translates a printed pusher block on linear rods, displacing a standard medical syringe. Control is via Arduino + a RepRap-style stepper driver, with G-code or serial command input. The publication releases STL/OpenSCAD parametric source, BOM with Digi-Key part numbers, calibration script, and benchmarks volumetric accuracy (<1% over 0.5-30 mL range) and minimum dispensable volume. CC-BY-SA / GPL release. Anticipates: any patent claim covering '3D-printed syringe pump assemblies driven by a stepper-motor-and-leadscrew with open firmware controlling dispense rate by step count' as of Sept 2014. Foundational prior art for the entire 'open syringe pump' lineage including Poseidon (which explicitly cites it), countless thesis instruments, and the Klipper-driven syringe pump line. Element-by-element discloses: parametric printed frame, leadscrew-translated syringe pusher, syringe-barrel clamping, microstepping volume calibration, and parallelization by chaining drivers on a single MCU.

## Carolina Biological Supply Microfluidic Teaching Kit (Lab-on-a-Chip Investigation) (2016)

- **id**: `carolina-biological-microfluidic-teaching-kit`
- **corpus**: private
- **device class**: consumable-bulk
- **creator**: Carolina Biological Supply Company
- **disclosure**: Carolina Biological Supply Company catalog 'Lab-on-a-Chip Investigation' kit; carolina.com
- **ip status**: trade-secret
- **prior art notes**: Discloses a packaged classroom microfluidics kit for high-school and intro-college biology, including chips, dyes, and instructor materials. Anticipates: educational chip-and-curriculum bundles for high-school biology; gravity-driven flow as pedagogical alternative to syringe pumps in teaching.

## Microneedle Ocular Patch for Posterior-Segment Drug Delivery (2020)

- **id**: `thakur-2020-microneedle-ocular-patch`
- **corpus**: academic
- **device class**: point-of-care-cartridge
- **creator**: Multiple academic groups (Donnelly lab Queen's Belfast; Prausnitz lab Georgia Tech)
- **disclosure**: Thakur Singh RR et al., Acta Biomaterialia 108:294-306 (2020); doi:10.1016/j.actbio.2020.03.039
- **ip status**: patented
- **prior art notes**: Discloses ocular microneedle patches as an alternative to intravitreal injection for delivering anti-VEGF, corticosteroid, and small-molecule therapeutics to the posterior eye. Hollow variants integrate microfluidic channels for active perfusion. Anticipates: ocular microneedle patches with integrated microfluidic perfusion; trans-scleral sustained-release microneedle architectures; eye-drop-replacement consumer microneedle formats including the speculative Verily/EyeDrop ML systems.

## Nix Hydration Biosensor (2021-09-22)

- **id**: `nix-hydration-biosensor`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: Nix Biosensors Inc.
- **disclosure**: Nix Inc. product launch 2021; Reinertsen E et al. founder publications; product manual rev 1
- **ip status**: patented
- **prior art notes**: Discloses a single-use sweat patch with a passive microfluidic network distributing sweat to colorimetric reagent pads, with a reusable optical reader puck snapping onto the patch and streaming hydration estimates to phone. The reader sees absorbance changes as sweat fills successive chambers. Anticipates: hybrid disposable-patch-plus-reusable-reader microfluidic architectures; capillary-routed colorimetric hydration tracking.
