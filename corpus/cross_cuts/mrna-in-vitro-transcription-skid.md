---
title: mrna-in-vitro-transcription-skid
parent: Cross-cuts
layout: default
---

# Cross-cut: `mrna-in-vitro-transcription-skid`

**8 corpus entries disclose this subsystem.**

Earliest disclosure: 1998

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Promega CellfreeIVT mRNA In-Vitro Transcription Kit (1998)

- **id**: `promega-cellfree-ivt`
- **corpus**: private
- **device class**: consumable-bulk
- **creator**: Promega Corporation
- **disclosure**: Promega RiboMAX product launch ~1998 (catalog records); Promega T7 RiboMAX Express datasheet rev 2024
- **ip status**: trade-secret
- **prior art notes**: Discloses a kit-format research-grade T7 RNAP IVT system, providing a benchmark workflow for downstream mRNA process-development scale-up. Anticipates: kit-format IVT workflows that customers later scale up to GMP via CDMO partners; functions as the entry point for research-to-clinical mRNA workflows.

## New England Biolabs GMP-grade T7 RNA Polymerase + Capping Enzymes (2018)

- **id**: `neb-gmp-t7-rnap`
- **corpus**: private
- **device class**: consumable-bulk
- **creator**: New England Biolabs, Inc.
- **disclosure**: NEB GMP-grade T7 RNAP product launch 2018; NEB Rowley MA GMP facility opening 2020; NEB IVT systems product datasheet rev 2024
- **ip status**: trade-secret
- **prior art notes**: Discloses GMP-grade enzymatic reagents (T7 RNA polymerase, VCC, RNase inhibitor, DNase I) supporting industrial mRNA IVT manufacturing. Anticipates: GMP-grade enzyme-supply architectures for mRNA manufacturing where a single supplier provides the full enzyme cocktail (RNAP + capping + nuclease + inhibitor) under DMF, simplifying CDMO supply-chain qualification. Pre-dates pandemic-era mRNA scale-up; NEB's enzymes are upstream of much of the wave-3 mRNA manufacturing ecosystem. Process detail of NEB's recombinant expression and purification is trade-secret.

## Moderna Norwood mRNA Continuous-Process Platform (2018-07)

- **id**: `moderna-norwood-mrna-platform`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Moderna, Inc.
- **disclosure**: Moderna press release 2018-07-17 (MTC opening, Norwood MA); Moderna S-1 2018-12-07 IPO filing (USSEC)
- **ip status**: patented
- **prior art notes**: Discloses a unified GMP mRNA platform consolidating IVT, capping, purification (oligo-dT or HPLC), TFF, and downstream LNP encapsulation by microfluidic rapid-mixing into a single facility template, with the same equipment supporting personalized cancer vaccines and pandemic-scale vaccines. Anticipates: facility-template architectures for mRNA manufacturing where the same upstream IVT skid + downstream LNP mixer feeds both small-batch personalized and large-batch pandemic outputs through software-driven recipe selection rather than physical retooling. Pre-dates much of the industry's pandemic-era scale-up literature, as Moderna disclosed the platform 18+ months before SARS-CoV-2.

## TriLink BioTechnologies CleanCap GMP Capping Reagent (2018-07)

- **id**: `trilink-cleancap-gmp`
- **corpus**: private
- **device class**: consumable-bulk
- **creator**: TriLink BioTechnologies (Maravai LifeSciences)
- **disclosure**: Henderson et al. Curr Protoc 2018 doi:10.1002/cpnc.58 (CleanCap analog disclosure); TriLink product launch 2018; US10,519,189B2 issued 2019-12-31
- **ip status**: patented
- **prior art notes**: Discloses a trinucleotide cap analog (m7G(5')ppp(5')AmpG, branded CleanCap AG) that participates as the +1 initiator in T7-RNAP-driven IVT and yields >94% Cap1-capped mRNA in a single co-transcriptional step, replacing the two-step Vaccinia-Capping-Complex enzymatic capping previously required for therapeutic mRNA. Anticipates: any IVT process using co-transcriptional trinucleotide cap analogs for therapeutic mRNA manufacturing; the manufacturing-process implication is that downstream IVT skids can omit a dedicated VCC enzymatic capping unit operation, simplifying microfluidic / continuous IVT designs by removing one buffer-exchange step. Cited by both BNT162b2 and mRNA-1273 process disclosures.

## BioNTech Marburg mRNA Continuous IVT Manufacturing Line (2020-09)

- **id**: `biontech-marburg-mrna-continuous-ivt`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: BioNTech SE
- **disclosure**: BioNTech press release 2020-09-17 (Marburg site acquisition from Novartis); BioNTech 20-F 2020 filing (USSEC); Pfizer-BioNTech BNT162b2 EUA briefing FDA 2020-12-10
- **ip status**: patented
- **prior art notes**: Discloses an industrial-scale mRNA manufacturing train integrating: (a) plasmid linearization, (b) T7-RNAP-driven in-vitro transcription using modified nucleotides (N1-methylpseudouridine), (c) DNase digestion, (d) tangential-flow filtration, (e) downstream microfluidic LNP formulation by aqueous-organic solvent rapid mixing in a T- or impingement-jet mixer, (f) buffer-exchange diafiltration, (g) sterile fill. Anticipates: industrial mRNA-vaccine manufacturing trains combining IVT with downstream microfluidic LNP encapsulation in a single GMP suite; specifically the architectural pattern of upstream-IVT-skid feeding a downstream-LNP-mixer-skid via in-line buffer exchange. Marburg's specific contribution: industrial-scale (multi-100L IVT batches) demonstrating that lab-scale microfluidic LNP mixing scales via parallel jet-mixer arrays rather than monolithic scale-up.

## Resilience (National Resilience) mRNA CDMO Platform (2020-11)

- **id**: `resilience-mrna-cdmo`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: National Resilience, Inc.
- **disclosure**: Resilience launch press release 2020-11-23; Boston Globe coverage 2021-04-14; Resilience site profile (Marlborough MA mRNA suite)
- **ip status**: trade-secret
- **prior art notes**: Discloses a CDMO-architecture mRNA platform combining licensed IVT chemistry, internal plasmid linearization, and microfluidic LNP encapsulation in a multi-tenant facility model. Anticipates: outsourced multi-tenant mRNA manufacturing facility architectures where a single suite supports multiple biopharma clients via campaign-mode changeovers rather than dedicated lines. Process detail is largely trade-secret; entry reserves slug and captures public facility architecture.

## Ginkgo Bioworks Cell-Free IVT Enzyme Foundry (2021-09)

- **id**: `ginkgo-bioworks-ivt-enzymes`
- **corpus**: private
- **device class**: consumable-bulk
- **creator**: Ginkgo Bioworks Holdings, Inc.
- **disclosure**: Ginkgo Bioworks SPAC 8-K 2021-09-17 (Soaring Eagle merger); Ginkgo 10-K 2022; Ginkgo press release 2022-04 (Aldevron-IVT enzyme partnership)
- **ip status**: patented
- **prior art notes**: Discloses an engineered-strain foundry that develops and supplies improved IVT enzymes (T7 RNAP variants, capping enzymes) via CRISPR-free strain engineering. Anticipates: strain-engineering-as-a-service architectures supplying improved IVT enzyme variants to mRNA manufacturers; specifically the workflow of customer-specified-IVT-enzyme-spec → in-silico variant design → strain construction → fermentation → purified-enzyme delivery. CRISPR-free aspect is regulatory-friendly for therapeutic enzyme supply.

## Quantoom Biosciences Ntensify mRNA-LNP Platform (2022-06)

- **id**: `univercells-quantoom-ntensify`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Quantoom Biosciences (Univercells SA subsidiary)
- **disclosure**: Quantoom Biosciences launch press release 2022-06-21; Univercells corporate announcement; CEPI grant announcement 2023-02-06
- **ip status**: patented
- **prior art notes**: Discloses a containerized end-to-end mRNA-LNP manufacturing skid integrating IVT, in-process purification, and microfluidic LNP encapsulation, sized for LMIC and distributed manufacturing. Anticipates: small-footprint integrated mRNA manufacturing modules designed for pandemic preparedness deployment; specifically the architectural pattern of one cabinet containing both upstream IVT and downstream LNP mixer with shared in-line buffer exchange. Distinct from BioNTech Marburg (industrial monolithic) and Moderna Norwood (multi-bay facility) by being a single-skid drop-in module.
