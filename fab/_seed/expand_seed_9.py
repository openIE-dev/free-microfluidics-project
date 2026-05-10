#!/usr/bin/env python3
"""Ninth expansion of fabrication recipes."""
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
    id="pdms-pegylation-covalent",
    canonical_name="Covalent PEGylation of PDMS surfaces (silane-PEG grafting)",
    aliases=["PEG-PDMS grafting", "covalent PDMS passivation"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="surface-modification",
    substrate_material="PDMS microfluidic channels post-fabrication",
    output_artifact="Covalently-grafted PEG monolayer on PDMS channel walls providing long-term (weeks-to-months) non-fouling surface, in contrast to non-covalent F-127 passivation (24-72 hr).",
    steps=[
        {"order": 1, "action": "Plasma-activate PDMS surface", "parameters": "O2 plasma at 50 W for 30 s; creates surface silanol groups for silane attachment", "duration": "10 min", "notes": "Within ~30 min of plasma activation, perform silanization before hydrophobic recovery"},
        {"order": 2, "action": "Prepare silane-PEG solution", "parameters": "5% v/v methoxy-PEG-silane (typ. PEG MW 5000) in anhydrous toluene; alternatively in 95% ethanol with 5% water for hydrolysis", "duration": "10 min", "notes": "Vendor: Laysan Bio mPEG-Silane MW 5000 typical"},
        {"order": 3, "action": "Inject silane-PEG into channels", "parameters": "fill channels with silane-PEG solution; incubate 2 hr at room temperature", "duration": "2 hr", "notes": "PEG-silane self-assembles into covalent monolayer via Si-O-Si linkage to plasma-activated surface"},
        {"order": 4, "action": "Rinse with toluene", "parameters": "5× channel volume toluene rinse to remove unbound PEG-silane", "duration": "10 min", "notes": ""},
        {"order": 5, "action": "Rinse with ethanol then water", "parameters": "5× channel volume ethanol; 10× channel volume water; final rinse with PBS or use buffer", "duration": "10 min", "notes": ""},
        {"order": 6, "action": "Verify by water contact angle", "parameters": "should drop from ~90° (plasma-activated PDMS, partially recovered) to ~45–60° (PEG monolayer)", "duration": "5 min", "notes": "Optional QC step"},
        {"order": 7, "action": "Use chip", "parameters": "covalently-bound PEG monolayer remains stable for weeks under flow", "duration": "(experiment-dependent)", "notes": "Distinguishes from F-127 (24-72 hr) by orders-of-magnitude longer effective lifetime"},
    ],
    critical_parameters=[
        {"parameter": "PEG-silane molecular weight", "target": "1000–10000 Da", "tolerance": "5000 typical", "failure_at_off_spec": "low MW: limited steric protection; high MW: difficult to dissolve and thread into channels"},
        {"parameter": "Silane-PEG concentration", "target": "5% v/v in toluene", "tolerance": "1–10%", "failure_at_off_spec": "low: incomplete monolayer; high: aggregation, multilayer formation"},
        {"parameter": "Plasma-to-silanization time gap", "target": "<30 min", "tolerance": "<60 min", "failure_at_off_spec": "PDMS recovers hydrophobicity; silane can't bind"},
        {"parameter": "Solvent water content", "target": "anhydrous in toluene; alternatively 5% water in ethanol", "tolerance": "<1% in toluene", "failure_at_off_spec": "wet toluene causes silane homopolymerization in solution rather than surface attachment"},
    ],
    equipment_required=[
        {"instrument_class": "plasma cleaner", "optional_model": "Harrick PDC-32G or equivalent", "notes": ""},
        {"instrument_class": "syringe / pressure setup for solvent flow", "optional_model": "any", "notes": ""},
    ],
    materials_required=[
        {"material": "methoxy-PEG-silane MW 5000", "vendor": "Laysan Bio / Nanocs", "part_number_optional": "mPEG-Silane-5000"},
        {"material": "anhydrous toluene", "vendor": "Sigma", "part_number_optional": "anhydrous toluene"},
        {"material": "ethanol (200-proof)", "vendor": "any", "part_number_optional": None},
    ],
    validated_outcome="Covalently-grafted PEG monolayer with weeks-to-months stability under flow; reduces protein adsorption by >95% in PDMS channels; cell-compatible (non-toxic to most cell lines).",
    failure_modes=[
        {"mode": "Incomplete coverage", "diagnostic_signature": "regions of channel show protein adsorption", "corrective_action": "verify plasma activation; reduce silanization-to-plasma time gap; verify solvent moisture content"},
        {"mode": "Multilayer / aggregate formation", "diagnostic_signature": "channels look cloudy under microscope", "corrective_action": "reduce silane concentration; use anhydrous solvent rigorously"},
        {"mode": "Loss over weeks", "diagnostic_signature": "passivation degrades after months", "corrective_action": "covalent attachment is stable but underlying PDMS may oxidize over time; refresh chip"},
    ],
    related_corpus_entries=["lee-1989-mpc-polymer-passivation", "vroman-effect-1962", "eddington-2008-pdms-peg-grafting"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "pluronic-f127-surface-passivation", "oxygen-plasma-pdms-glass-bonding"],
    publication_citation="Eddington, D. T.; Puccinelli, J. P.; Beebe, D. J. Sens. Actuators B 2006, 114, 170–172",
    sources=[
        "Eddington, D. T. et al. Sens. Actuators B 2006, 114, 170–172",
        "Various follow-up publications on PEG-silane PDMS grafting",
    ],
    notes="Covalent PEGylation is the most durable surface passivation method for PDMS microfluidic chips. The trade-off vs F-127 is fabrication complexity (requires plasma + organic solvent + silane chemistry) but the payoff is weeks-to-months stability rather than 24-72 hr. Critical for long-term cell culture and protein-handling experiments.",
)


with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new recipes to {OUT}")
