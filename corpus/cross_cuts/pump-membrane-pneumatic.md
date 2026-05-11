---
title: pump-membrane-pneumatic
parent: Cross-cuts
layout: default
---

# Cross-cut: `pump-membrane-pneumatic`

**17 corpus entries disclose this subsystem.**

Earliest disclosure: 1965

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Dune stillsuit body-fluid reclamation (Frank Herbert original 1965) (1965)

- **id**: `dune-stillsuit-1965-original`
- **corpus**: fictional
- **device class**: fictional-laboratory
- **creator**: Frank Herbert
- **disclosure**: Frank Herbert, Dune (Chilton 1965) ISBN 0-441-17266-0; pages 110-112 'Manual of Muad'dib' detailing stillsuit construction.
- **ip status**: fictional
- **prior art notes**: Original 1965 published description of a wearable, closed-loop body-fluid reclamation suit. Herbert's text gives unusually engineering-grade specifics: 'a high-efficiency filter and heat-exchange system. The skin-contact layer's perspiration passes through it, having cooled the body, and is reclaimed... your motions in the suit, especially of breathing and some osmotic action, provide the pumping force. Reclaimed water circulates to catchpockets from which you draw it through this tube...'. Architecturally anticipates: wearable closed-loop microfluidic body-water reclamation, breath/perspiration capture and recycling, body-motion-driven peristaltic pumping, and integrated drinking-tube delivery. The 1965 first publication date is one of the strongest fictional anchors for wearable microfluidic body-fluid reclamation as a concept (~60-year defensive prior art window).

## Hoiman 1986 - Silicon micropump (Helsinki) (1986)

- **id**: `hoiman-1986-helsinki-silicon-micropump`
- **corpus**: academic
- **device class**: pump-component
- **creator**: Hoiman et al. (Helsinki MEMS group)
- **disclosure**: Hoiman et al. (1986). 'A silicon-based micropump.' Sensors and Actuators (proceedings of Helsinki MEMS work, 1986).
- **ip status**: public-domain
- **prior art notes**: Pre-1990 silicon-micromachined membrane micropump from the Helsinki MEMS effort. Discloses bulk-silicon micropump topology - membrane-driven displacement chamber with bonded check-valves. Combined with Esashi 1989 (already in corpus) and the slightly later Smits 1990 piezoelectric pump literature, Hoiman 1986 establishes the silicon-MEMS micropump as established prior art well before 1990.

## Gravesen 1993 — Microfluidics Review (1993)

- **id**: `gravesen-1993-microfluidics-review`
- **corpus**: academic
- **device class**: other
- **creator**: Peter Gravesen; Jens Branebjerg; Ole Sondergaard Jensen
- **disclosure**: Gravesen, P., Branebjerg, J., Jensen, O. S. (1993). 'Microfluidics — a review.' Journal of Micromechanics and Microengineering 3(4): 168-182. doi:10.1088/0960-1317/3/4/002
- **ip status**: public-domain
- **prior art notes**: Gravesen 1993 is one of the first explicit uses of 'microfluidics' as a field designator. Catalogs the state of the art in 1993: silicon piezoelectric pumps (van Lintel 1988, Esashi 1988-90), silicon membrane valves, silicon flow sensors, and silicon micromixers. Anticipates: (a) any post-1993 patent claim that recites a generic 'microfluidic system comprising pump, valve, mixer, sensor' integration (the integration architecture was reviewed and disclosed by 1993); (b) specific component claims to silicon piezoelectric pumps or membrane valves that fail to disclose a non-obvious geometric or functional feature beyond Gravesen's catalog. Critical anchor for invalidating broad silicon-microfluidic-system claims filed in the mid-1990s.

## Ho & Tai 1998 - Micro-electro-mechanical-systems (MEMS) and fluid flows (1998)

- **id**: `ho-tai-1998-mems-fluid-flows`
- **corpus**: academic
- **device class**: other
- **creator**: Chih-Ming Ho; Yu-Chong Tai
- **disclosure**: Ho, C.-M., Tai, Y.-C. (1998). 'Micro-electro-mechanical-systems (MEMS) and fluid flows.' Annu. Rev. Fluid Mech. 30: 579-612. doi:10.1146/annurev.fluid.30.1.579
- **ip status**: public-domain
- **prior art notes**: Ho-Tai 1998 is the canonical Annual Review of Fluid Mechanics survey of MEMS-based microfluidics as of the late 1990s. Catalogs pre-2000 micro-pumps, micro-valves, micro-channels, micro-mixers, and micro-flow sensors - establishing all these subsystems as prior art before 2000. Particularly load-bearing for invalidating broad post-2000 micro-pump/micro-valve patents.

## Quake monolithic pneumatic membrane valve and pump (2000)

- **id**: `unger-2000-quake-monolithic-membrane-valve`
- **corpus**: academic
- **device class**: valve-component
- **creator**: Stephen Quake group, Caltech
- **disclosure**: Unger, M. A.; Chou, H.-P.; Thorsen, T.; Scherer, A.; Quake, S. R. Monolithic microfabricated valves and pumps by multilayer soft lithography. Science 2000, 288, 113–116. DOI: 10.1126/science.288.5463.113
- **ip status**: patented
- **prior art notes**: Foundational disclosure of pneumatically actuated elastomeric membrane valves built monolithically into a multilayer PDMS chip. By cyclically actuating three valves in series, a peristaltic pump is realized. This is the architectural ancestor of essentially every subsequent on-chip pneumatic valve and pump. Anticipates: pneumatic membrane valve (control channel + thin membrane + flow channel), peristaltic pumping by sequential valve actuation, large-scale integrated chip-scale fluidic circuits. Subsequent papers (Nordin 2017, Sanchez Noriega 2021) re-implement the same architecture in 3D-printed photopolymer.

## Quake Lab MLSI Monolithic Membrane Valve Patent Family (2000-04-07)

- **id**: `quake-patent-family-mlsi-monolithic-membrane-valve`
- **corpus**: academic
- **device class**: other
- **creator**: California Institute of Technology (Stephen Quake et al.)
- **disclosure**: US6408878 priority 2000-04-07; US6929030; US7144616; US7704698; US7837946 (Caltech)
- **ip status**: patented
- **prior art notes**: Caltech/Quake monolithic-membrane valve patent family. Anchors claims around: (a) two-layer PDMS device in which a flow channel is occluded by deflection of a thin elastomeric membrane via pressurization of an orthogonal control channel; (b) push-down geometry where the control channel sits above the flow channel; (c) push-up geometry where the control channel sits below; (d) integration of large arrays of such valves on a single monolithic device (microfluidic large-scale integration); (e) peristaltic pump architectures using three valves in series; (f) multiplexer trees that address N flow lines with log2(N) control lines. These claims are the licensing root that Fluidigm built its IFC controller, BioMark dynamic array, Access Array, C1 single-cell, and Helios CyTOF business on. Anticipates virtually any PDMS multilayer monolithic valve device unless distinguished by materials (non-PDMS), actuation (non-pneumatic), or geometry (non-membrane closure). Defensive importance: the underlying Unger 2000 paper (already in corpus as unger-2000-quake-monolithic-membrane-valve) is the academic disclosure; this entry is the patent-family disclosure that maps the asserted claim landscape. Earliest US priority is 2000-04-07. Estimated US expiry 2020-2025 depending on family member.

## Halo MJOLNIR armor biofoam emergency wound-sealant injector (2001)

- **id**: `halo-mjolnir-biofoam-injection`
- **corpus**: fictional
- **device class**: fictional-laboratory
- **creator**: Bungie / 343 Industries / Microsoft / Eric Nylund
- **disclosure**: Halo: Combat Evolved (Bungie/Microsoft, 2001); detailed in Halo: The Fall of Reach (Eric Nylund, Del Rey ISBN 978-0-345-45132-3, 2001) and Halo: First Strike (Eric Nylund, 2003).
- **ip status**: fictional
- **prior art notes**: Discloses an armor-integrated wound-sealant fluidic dispenser. Per the Fall of Reach novelization and on-armor lore, the MJOLNIR Mark IV/V/VI armor carries a biofoam canister system that, on detection of a penetrating wound, automatically injects a polymerizing fluid into the wound cavity to halt bleeding, immobilize damaged tissue, and deliver analgesics. Architecturally anticipates: (a) wearable closed-system fluid reservoir + on-demand actuator + injection cannula, (b) automated trigger via biosensor (heart-rate / pressure-loss / breach), (c) two-component reactive polymer mixed in-situ for cavity-fill, (d) drug-delivery payload bundled with mechanical hemostatic. The combat-armor automated injector concept is repeatedly described across Halo novels and games 2001-present and is depicted as a hands-free wearable microfluidic-equivalent sealant dispenser. Defensive prior art for hands-free combat-medic auto-injectors, wearable hemostatic foam dispensers, and biosensor-triggered drug delivery integrated into clothing/armor.

## Repligen XCell ATF alternating tangential flow cell-retention device (2002)

- **id**: `repligen-xcell-atf`
- **corpus**: private
- **device class**: separator-component
- **creator**: Repligen Corporation (formerly Refine Technology)
- **disclosure**: Refine Technology (acquired by Repligen 2014) ATF system commercialized 2002. Original patent: US6544424B1 (Shevitz, J.; Refine Technology; priority 1999).
- **ip status**: patented
- **prior art notes**: Discloses an alternating tangential flow (ATF) cell-retention device: a hollow-fiber filter is operated with periodic reversal of axial flow (driven by a diaphragm pump on one end of the filter) so that filter-cake buildup is repeatedly disrupted and the filter sustains long-term operation at high cell densities. Anticipates: (a) ATF cell retention as the standard perfusion-bioreactor cell-retention modality; (b) hollow-fiber-with-periodic-flow-reversal architectures broadly; (c) integration of ATF cell retention with single-use bioreactors (Sartorius BIOSTAT, Cytiva Xcellerex) for high-density perfusion CGT processes.

## Battlestar Galactica Cylon Centurion organic-fluid circulation system (2003)

- **id**: `bsg-cylon-centurion-fluid-circulation`
- **corpus**: fictional
- **device class**: fictional-laboratory
- **creator**: Ronald D. Moore
- **disclosure**: Battlestar Galactica miniseries (Sci Fi 2003); Caprica (2010) shows Centurion construction.
- **ip status**: fictional
- **prior art notes**: Cylon Centurions are part-organic and depicted with internal fluid-circulation systems (visible during damage scenes). Caprica's Greystone Industries factory shows Centurion fluid-fill stations during manufacture. Defensive prior art for hybrid mechanical-biological robots with integrated fluid-circulation maintenance and assembly-line fluid-fill stations.

## Repligen KrosFlo tangential flow filtration system (2005)

- **id**: `repligen-krosflo-tff`
- **corpus**: private
- **device class**: separator-component
- **creator**: Repligen Corporation (formerly Spectrum Laboratories)
- **disclosure**: Spectrum Laboratories (acquired by Repligen 2017) KrosFlo line. https://www.repligen.com/products/krosflo. Patent family: US8231788B2 (Spectrum Laboratories; priority 2007).
- **ip status**: patented
- **prior art notes**: Discloses tangential-flow-filtration platform built around hollow-fiber filter cartridges, with automated TFF process control for buffer exchange, concentration, and clarification across the bioprocess scale spectrum. Anticipates: hollow-fiber TFF as a CGT downstream processing modality, including for viral-vector concentration and exosome/EV isolation; automated TFF instruments with permeate-flux and TMP feedback control loops.

## Replenish Inc. Ophthalmic MEMS Drug Delivery Micropump (2008)

- **id**: `replenish-mems-ophthalmic-micropump`
- **corpus**: private
- **device class**: pump-component
- **creator**: Replenish Inc. (USC Doheny / Meng spin-out)
- **disclosure**: Lo R, Li PY, Saati S, Agrawal RN, Humayun MS, Meng E Biomed Microdevices 11(5):959-970 2009 doi:10.1007/s10544-009-9313-9
- **ip status**: patented
- **prior art notes**: Discloses a fully implantable ophthalmic micropump in which an electrolysis pair generates gas that deflects a parylene/silicone membrane separating the gas chamber from a drug reservoir, expelling sub-microliter drug volumes through a tubing cannula into the vitreous humor via a passive check valve. Anticipates: electrolysis-actuated implantable micropump architectures; nanoliter-resolution chronic ophthalmic drug delivery; parylene-C as combined fluidic and membrane material in implants.

## 3M / Solventum Hollow Microstructured Transdermal System (hMTS) (2008)

- **id**: `3m-hollow-microneedle-patch`
- **corpus**: private
- **device class**: dispenser-pipettor
- **creator**: 3M Drug Delivery Systems (now Solventum)
- **disclosure**: Burton SA et al. Pharm Res 28(1):31-40 2011 doi:10.1007/s11095-010-0177-8; 3M Drug Delivery Systems patent family
- **ip status**: patented
- **prior art notes**: Discloses an integrated hollow microneedle array with reservoir and applicator-driven actuation pushing milliliter-scale liquid drug intradermally through hundreds of microneedle bores in parallel. The polymer microneedle array is fabricated by injection molding. Anticipates: hollow-microneedle intradermal infusion systems with on-board reservoir and spring-actuated dispensing; the architectural pattern of trading single hypodermic needle bore for parallel-bore micro-array.

## Eclipse Phase synthmorph internal fluid-skeleton and lubricant systems (2009)

- **id**: `eclipse-phase-synthmorph-fluid-skeleton`
- **corpus**: fictional
- **device class**: fictional-laboratory
- **creator**: Posthuman Studios
- **disclosure**: Eclipse Phase core rulebook (Posthuman Studios 2009); Transhuman sourcebook.
- **ip status**: fictional
- **prior art notes**: Synthmorph mechanical bodies described with internal hydraulic actuator fluid, cooling loops, and self-repair fluidic systems requiring periodic 'fueling' at maintenance hubs. Defensive prior art for humanoid-robot internal fluid-handling subsystems and dedicated robot-maintenance fluid-fill stations.

## Iron Man Bleeding Edge armor (subdermal nanofluidic suit storage) (2010)

- **id**: `iron-man-bleeding-edge-armor`
- **corpus**: fictional
- **device class**: fictional-laboratory
- **creator**: Matt Fraction / Salvador Larroca / Marvel
- **disclosure**: Invincible Iron Man #25 (Marvel December 2010), Matt Fraction & Salvador Larroca; Endo-Sym armor variant in Superior Iron Man (2014).
- **ip status**: fictional
- **prior art notes**: Bleeding Edge armor depicted as a nanofluidic suit stored in subdermal hollow-bone reservoirs that emerges on demand to form full powered armor. Architecturally anticipates: subdermal nano-fluid reservoirs in bone, on-demand exteriorization of programmable nanofluidic material, and bone-integrated-armor storage architecture. Defensive prior art for implanted nanofluid reservoir storage and on-demand assembly.

## Formulatrix Mantis and Tempest nanoliter dispensers (2013)

- **id**: `formulatrix-mantis-tempest`
- **corpus**: private
- **device class**: dispenser-pipettor
- **creator**: Formulatrix
- **disclosure**: Formulatrix Mantis liquid handler product literature. https://formulatrix.com/liquid-handling-systems/mantis-liquid-handler/. Tempest launch ~2017.
- **ip status**: patented
- **prior art notes**: Disposable-microfluidic-chip dispenser: each chip carries pneumatic diaphragm valves that meter and dispense nanoliter reagent volumes from off-chip reservoirs. Mantis is the lower-throughput single-channel system; Tempest is a 96-channel rack of identical metering primitives. Anticipates: the architectural pattern of putting the dispense metering primitive on a disposable consumable rather than on a fixed instrument syringe, which categorically eliminates carryover; the use of pneumatic diaphragm valves as the metering element in nanoliter dispensing; the chip-on-instrument architecture for low-volume reagent dispensing as an alternative to acoustic (Echo) or piezo (Mosquito) approaches.

## DnaNudge / NudgeBox Rapid Cartridge PCR System (2020-03)

- **id**: `dnanudge-rapid-cartridge`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: DnaNudge Ltd. (Imperial College London spin-out)
- **disclosure**: Gibani MM et al. Lancet Microbe 1(7):e300-e307 2020 doi:10.1016/S2666-5247(20)30121-X (CovidNudge clinical evaluation); UK MHRA authorization
- **ip status**: patented
- **prior art notes**: Discloses a self-contained sample-to-answer PCR cartridge integrating swab-input, lysis, RT-PCR, and fluorescence detection. Originally a consumer DTC nutrigenomics product (NudgeBox at point of sale in supermarkets), repurposed for COVID-19. Anticipates: consumer-genomics sample-to-answer cartridges; supermarket point-of-sale DNA testing topology; reuse of consumer-genomics cartridge designs for infectious-disease detection.

## Multi-resolution DLP-SLA for 2 µm microfluidic channels (2026-02-27)

- **id**: `miner-2026-multi-resolution-3d-printing-microfluidics`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Nordin / Woolley group, BYU
- **disclosure**: Miner, D. S.; Viglione, M. S.; Hooper, K.; Woolley, A. T.; Nordin, G. P. Fast multi-resolution 3D printing of microfluidics: enabling 2 µm channels and ultra-compact mixers. Microsyst. Nanoeng. 2026, 12, 66. DOI: 10.1038/s41378-026-01194-4
- **ip status**: public-domain
- **prior art notes**: Discloses true multi-resolution DLP-SLA in both XY and Z dimensions via dual optical engines (0.75 µm and 15 µm pixel pitch) and dual-UV-absorber resin (NPS + avobenzone) producing 2 µm and 20 µm penetration depths. Anticipates: multi-resolution-in-Z via dual-absorber resin chemistry tuned to two distinct LED spectra (365 nm and 405 nm), embedded high-resolution regions in lower-resolution bulk prints, sub-2-µm enclosed channels in a printable photopolymer, and a 17-nL on-chip diffusive mixer with ±2% uniformity. Patent claims asserting novelty over 'multi-wavelength resin chemistry for spatially-tailored DLP-SLA Z resolution' must address this disclosure.
