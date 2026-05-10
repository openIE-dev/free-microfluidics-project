#!/usr/bin/env python3
"""Seventh expansion of fabrication recipes."""
import json
from pathlib import Path

OUT = Path(__file__).parent / "recipes.jsonl"
ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("last_updated", "2026-05-09")
    kw.setdefault("license", "CC0-1.0")
    ENTRIES.append(kw)


add(
    id="herringbone-mixer-fabrication-baseline",
    canonical_name="Staggered herringbone mixer fabrication (Stroock-Whitesides architecture)",
    aliases=["herringbone mixer fab", "Stroock SHM fabrication"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="pdms-soft-lithography",
    substrate_material="PDMS bonded to glass slide; SU-8 master with two-step photolithography",
    output_artifact="PDMS chip with staggered herringbone mixer features for chaotic mixing in laminar flow regimes; mixing length ~5–15× channel width.",
    steps=[
        {"order": 1, "action": "Design two-layer mask", "parameters": "Layer 1 (channel base) is the main flow channel 200 µm × 100 µm. Layer 2 (herringbones) is 50 µm-deep grooves on channel ceiling at 45° angles, alternating between two herringbone orientations every 6 cycles", "duration": "1 hr", "notes": "Two-layer photolithography is required because herringbone features sit on top of the main flow channel"},
        {"order": 2, "action": "Spin-coat first SU-8 layer (channel base)", "parameters": "SU-8 2050 at 3000 rpm for ~50 µm; soft-bake 65 °C 2 min then 95 °C 5 min", "duration": "20 min", "notes": ""},
        {"order": 3, "action": "Expose first layer", "parameters": "365 nm i-line UV through first mask, 150 mJ/cm²; PEB 65/95 °C two-step", "duration": "15 min", "notes": "Do NOT develop yet — second layer goes on top"},
        {"order": 4, "action": "Spin-coat second SU-8 layer (herringbones)", "parameters": "SU-8 2025 at 3000 rpm for ~25 µm on top of first layer; soft-bake 65/95 °C", "duration": "20 min", "notes": "Second layer crosslinks to first only where exposed"},
        {"order": 5, "action": "Expose second layer", "parameters": "Align herringbone mask to first-layer channel features using mask aligner; expose 75 mJ/cm²; PEB", "duration": "15 min", "notes": "Alignment accuracy critical — misaligned herringbones reduce mixing efficiency"},
        {"order": 6, "action": "Develop both layers", "parameters": "PGMEA developer 5–10 min with agitation; IPA rinse; DI rinse; N2 dry; hard bake 180 °C 30 min", "duration": "20 min", "notes": ""},
        {"order": 7, "action": "Cast PDMS replica", "parameters": "10:1 PDMS poured over master, degassed, cured 60 min @ 65 °C; PDMS now has channels with herringbone-grooved ceilings", "duration": "1.5 hr", "notes": "Note: when bonded channel-side-down, herringbones become floor features — this is conventional"},
        {"order": 8, "action": "Bond to glass", "parameters": "O2 plasma activation; place on glass slide channel-side-down; 30 min @ 80 °C bake", "duration": "1 hr", "notes": ""},
    ],
    critical_parameters=[
        {"parameter": "Herringbone groove depth", "target": "1/3 of channel height", "tolerance": "±20%", "failure_at_off_spec": "shallow grooves: insufficient chaotic mixing; deep grooves: dead zones, particle trapping"},
        {"parameter": "Herringbone angle", "target": "45° relative to flow", "tolerance": "±10°", "failure_at_off_spec": "off-angle reduces mixing efficiency"},
        {"parameter": "Layer alignment", "target": "<10 µm misalignment", "tolerance": "<25 µm", "failure_at_off_spec": "misaligned grooves reduce mixing efficiency by ~20% per 10 µm of offset"},
        {"parameter": "Cycle period", "target": "6 herringbones per orientation, alternating", "tolerance": "exact (per design)", "failure_at_off_spec": "non-canonical patterns reduce efficiency or alter mixing length"},
    ],
    equipment_required=[
        {"instrument_class": "spin coater", "optional_model": None, "notes": ""},
        {"instrument_class": "UV mask aligner with alignment stage", "optional_model": "Suss MA6 / EVG 620", "notes": "alignment accuracy critical for two-layer photolithography"},
        {"instrument_class": "hotplates", "optional_model": "Torrey Pines or equivalent", "notes": ""},
        {"instrument_class": "plasma cleaner", "optional_model": "Harrick PDC-32G or equivalent", "notes": "for PDMS-glass bonding"},
    ],
    materials_required=[
        {"material": "SU-8 2050 photoresist (channel layer)", "vendor": "MicroChem / Kayaku", "part_number_optional": "SU-8 2050"},
        {"material": "SU-8 2025 photoresist (herringbone layer)", "vendor": "MicroChem / Kayaku", "part_number_optional": "SU-8 2025"},
        {"material": "Sylgard 184 PDMS", "vendor": "Dow", "part_number_optional": None},
        {"material": "glass microscope slides", "vendor": "any", "part_number_optional": None},
    ],
    validated_outcome="Reproduces herringbone mixer geometry with 50 µm groove depth on 100 µm × 200 µm flow channels; achieves chaotic mixing within ~10 channel-widths of mixer entry. Critical fabrication step for mRNA-LNP synthesis (Precision Nanosystems NanoAssemblr architecture).",
    failure_modes=[
        {"mode": "Layer misalignment", "diagnostic_signature": "herringbones not centered on channel", "corrective_action": "improve mask aligner accuracy; use alignment marks rather than visual alignment"},
        {"mode": "Second layer delamination", "diagnostic_signature": "herringbone features peel off during develop", "corrective_action": "soft-bake first layer enough to maintain integrity but not so much that second-layer adhesion suffers; verify PEB temperature"},
        {"mode": "Mixing inefficiency", "diagnostic_signature": "incomplete mixing in finished chip", "corrective_action": "verify groove depth (1/3 of channel height); check angle accuracy; verify cycle alternation pattern matches Stroock 2002"},
    ],
    related_corpus_entries=["stroock-2002-staggered-herringbone-mixer", "microfluidic-mrna-vaccine-formulation", "precision-nanosystems-nanoassemblr"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "su8-master-baseline", "oxygen-plasma-pdms-glass-bonding"],
    publication_citation="Stroock et al. 2002 Science 295, 647 (foundational herringbone mixer)",
    sources=[
        "Stroock, A. D. et al. Chaotic mixer for microchannels. Science 2002, 295, 647–651",
    ],
    notes="Critical recipe — the staggered herringbone mixer is the canonical microfluidic mixing element used in mRNA-LNP vaccine manufacturing (Precision Nanosystems NanoAssemblr) and most microfluidic nanoparticle synthesis. The two-layer photolithography requirement is the main fabrication challenge.",
)

add(
    id="pluronic-f127-surface-passivation",
    canonical_name="Pluronic F-127 PEO-PPO-PEO surface passivation for cell-culture chips",
    aliases=["Pluronic F-127 coating", "F-127 passivation"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="surface-modification",
    substrate_material="PDMS / glass / thermoplastic microfluidic channels",
    output_artifact="Non-fouling Pluronic F-127 monolayer adsorbed on hydrophobic surfaces, providing 24–72 hr cell-culture-compatible passivation against protein adsorption and cell adhesion.",
    steps=[
        {"order": 1, "action": "Prepare F-127 solution", "parameters": "5% w/v Pluronic F-127 in DI water or PBS; sterilize via 0.22 µm filter; can be stored at 4 °C up to 2 weeks", "duration": "30 min", "notes": "F-127 is a triblock PEO-PPO-PEO copolymer; the PPO block adsorbs to hydrophobic surfaces, presenting PEO hydrophilic blocks outward"},
        {"order": 2, "action": "Wet channels with 100% IPA", "parameters": "fill channels with isopropanol; allow 5 min wetting", "duration": "10 min", "notes": "Removes air pockets and ensures complete surface contact"},
        {"order": 3, "action": "Replace IPA with water", "parameters": "flush 10× channel volume with DI water", "duration": "10 min", "notes": ""},
        {"order": 4, "action": "Apply F-127 solution", "parameters": "fill channels with 5% F-127 solution; incubate 2 hr at room temperature or 30 min at 37 °C", "duration": "2 hr", "notes": "Longer incubation gives denser PEO brush"},
        {"order": 5, "action": "Rinse", "parameters": "flush 10× channel volume with sterile PBS or cell culture medium", "duration": "10 min", "notes": "Removes excess F-127; bound monolayer remains"},
        {"order": 6, "action": "Verify by water contact angle", "parameters": "measure water contact angle on reference surface treated identically; should drop from ~110° (untreated PDMS) to ~30–40° (F-127 treated)", "duration": "5 min", "notes": "Optional QC step"},
        {"order": 7, "action": "Use immediately for cell culture", "parameters": "load cells in growth medium", "duration": "(experiment-dependent)", "notes": "F-127 monolayer effective for 24–72 hr; reapply for longer experiments"},
    ],
    critical_parameters=[
        {"parameter": "F-127 concentration", "target": "5% w/v", "tolerance": "1% to 10%", "failure_at_off_spec": "low: incomplete coverage; high: aggregation, but not toxic"},
        {"parameter": "Incubation time", "target": "2 hr at RT or 30 min at 37 °C", "tolerance": ">30 min", "failure_at_off_spec": "shorter: incomplete coverage; longer: no harm"},
        {"parameter": "Substrate hydrophobicity", "target": "hydrophobic", "tolerance": "needed for PPO adsorption", "failure_at_off_spec": "F-127 will not bind effectively to hydrophilic substrates"},
        {"parameter": "Effective lifetime", "target": "24–72 hr", "tolerance": "depends on flow rate", "failure_at_off_spec": "longer experiments require re-treatment or covalent passivation alternatives"},
    ],
    equipment_required=[
        {"instrument_class": "syringe or pressure pump for flushing", "optional_model": "any", "notes": ""},
        {"instrument_class": "incubator or hotplate (optional)", "optional_model": None, "notes": "for 37 °C incubation"},
    ],
    materials_required=[
        {"material": "Pluronic F-127", "vendor": "Sigma-Aldrich / BASF", "part_number_optional": "P2443 (Sigma)"},
        {"material": "0.22 µm syringe filter", "vendor": "any", "part_number_optional": None},
        {"material": "DI water or PBS", "vendor": "any", "part_number_optional": None},
    ],
    validated_outcome="Reduces protein adsorption by >90% and prevents cell adhesion for 24–72 hr in PDMS channels; cell-compatible (non-toxic at 5% F-127, biocompatible for short-term cell experiments).",
    failure_modes=[
        {"mode": "Incomplete surface coverage", "diagnostic_signature": "cells adhere to chip walls", "corrective_action": "longer incubation; verify chip is fully wet; verify F-127 solution concentration"},
        {"mode": "Loss of effectiveness over time", "diagnostic_signature": "passivation degrades after 48 hr", "corrective_action": "re-apply F-127; switch to covalent passivation (PEG-grafted PDMS) for longer experiments"},
        {"mode": "Cell viability issues", "diagnostic_signature": "cell death after F-127 treatment", "corrective_action": "verify F-127 grade (cell-culture-tested); reduce concentration; rinse more thoroughly before cell loading"},
    ],
    related_corpus_entries=["lee-1989-mpc-polymer-passivation", "vroman-effect-1962", "eddington-2008-pdms-peg-grafting"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline"],
    publication_citation="Various — F-127 as PDMS surfactant is a well-established protocol",
    sources=[
        "Lee, J. N.; Park, C.; Whitesides, G. M. Solvent compatibility of poly(dimethylsiloxane)-based microfluidic devices. Anal. Chem. 2003, 75, 6544–6554",
        "Sigma-Aldrich Pluronic F-127 datasheet",
    ],
    notes="Pluronic F-127 is the simplest and most widely-used non-covalent passivation method for PDMS microfluidic chips. Effective for short-term cell culture and protein-handling experiments. For longer experiments or chemical-resistance applications, covalent passivation (PEG-grafted PDMS, parylene coating, or NOA substrate) is preferred.",
)


with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new recipes to {OUT}")
