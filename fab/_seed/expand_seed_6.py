#!/usr/bin/env python3
"""Sixth expansion of fabrication recipes."""
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
    id="parylene-cvd-coating-baseline",
    canonical_name="Parylene-C CVD conformal coating for microfluidic chips",
    aliases=["parylene coating", "parylene-C CVD"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="surface-modification",
    substrate_material="any rigid microfluidic substrate (glass, silicon, thermoplastic, PDMS post-fabrication)",
    output_artifact="Conformal pinhole-free parylene-C polymer coating, 0.1 µm to 10 µm thickness, providing chemical resistance, biocompatibility, and electrical insulation for chip surfaces.",
    steps=[
        {"order": 1, "action": "Mask non-coating regions", "parameters": "if selective coating needed, apply tape or photoresist to mask connector contact pads and access ports", "duration": "15 min", "notes": "Parylene coats EVERYTHING including masking interface; pre-define masked areas carefully"},
        {"order": 2, "action": "Load parylene dimer", "parameters": "load di-para-xylylene dimer (C16H16) into vaporizer chamber: 1 g dimer per ~0.5 µm coating thickness on standard substrate area", "duration": "5 min", "notes": "Specialty Coating Systems PDS 2010 / 2035 typical"},
        {"order": 3, "action": "Pump down chamber", "parameters": "evacuate to <50 mTorr base pressure", "duration": "30 min", "notes": "Pinhole-free coating requires good vacuum"},
        {"order": 4, "action": "Vaporize dimer", "parameters": "heat dimer chamber to 150–175 °C; sublimes dimer to gas phase", "duration": "10 min", "notes": ""},
        {"order": 5, "action": "Pyrolyze dimer to monomer", "parameters": "gas passes through pyrolysis tube at 680 °C, breaking C16H16 dimer into two reactive C8H8 monomers", "duration": "continuous during deposition", "notes": "This is the chemical step that distinguishes parylene from other vapor-deposition polymers"},
        {"order": 6, "action": "Deposition onto substrate", "parameters": "monomer enters room-temperature deposition chamber; polymerizes spontaneously upon contact with substrate", "duration": "1 hr per µm of coating", "notes": "Conformal coating: no line-of-sight requirement, coats inside microchannels"},
        {"order": 7, "action": "Vent and unload", "parameters": "vent chamber; remove substrate; remove masking", "duration": "30 min", "notes": ""},
    ],
    critical_parameters=[
        {"parameter": "Vaporizer temperature", "target": "150–175 °C", "tolerance": "±10 °C", "failure_at_off_spec": "low: incomplete vaporization; high: dimer decomposition"},
        {"parameter": "Pyrolysis temperature", "target": "680 °C", "tolerance": "±20 °C", "failure_at_off_spec": "low: incomplete dimer cleavage, no polymer; high: monomer decomposition"},
        {"parameter": "Chamber base pressure", "target": "<50 mTorr", "tolerance": "<100 mTorr", "failure_at_off_spec": "high pressure: pinholes from gas-phase contaminants"},
        {"parameter": "Coating thickness", "target": "set by dimer mass", "tolerance": "±10%", "failure_at_off_spec": "thickness sets dielectric strength + chemical resistance"},
    ],
    equipment_required=[
        {"instrument_class": "parylene CVD coater", "optional_model": "Specialty Coating Systems PDS 2010 / PDS 2035 / Diener Comelec", "notes": "$30k–$100k commercial; rare in academic labs but available at most cleanroom user facilities"},
    ],
    materials_required=[
        {"material": "parylene-C dimer", "vendor": "Specialty Coating Systems / Para Tech", "part_number_optional": "Galxyl C / SCS"},
        {"material": "parylene-N dimer (alternative)", "vendor": "Specialty Coating Systems", "part_number_optional": "Galxyl N"},
    ],
    validated_outcome="Conformal pinhole-free coating at 0.1 µm to 10 µm thickness; >1 GΩ insulation resistance; biocompatible (USP Class VI grade for parylene-C); chemical resistance to most organic solvents.",
    failure_modes=[
        {"mode": "Pinholes at substrate features", "diagnostic_signature": "leakage current at sharp edges or contamination sites", "corrective_action": "thicker coating; clean substrate before deposition; verify chamber base pressure"},
        {"mode": "Adhesion failure", "diagnostic_signature": "coating peels off substrate", "corrective_action": "silane adhesion promoter (A-174) before coating"},
        {"mode": "Coating cracks under thermal cycling", "diagnostic_signature": "fine cracks in coating after temperature change", "corrective_action": "thinner coating; use parylene-N (lower modulus) for thermal-cycled applications"},
    ],
    related_corpus_entries=["ewod-cartridge-fabrication-baseline", "lee-1989-mpc-polymer-passivation"],
    related_fab_recipes=["ewod-cartridge-fabrication-baseline"],
    publication_citation="Gorham 1966 (parylene-C CVD foundational disclosure)",
    sources=[
        "Gorham, W. F. A new general synthetic method for the preparation of linear poly-p-xylylenes. J. Polym. Sci. A-1 1966, 4, 3027–3039",
        "Specialty Coating Systems PDS 2010 user manual",
    ],
    notes="Parylene-C CVD is the canonical conformal coating for microfluidic chips requiring biocompatibility, chemical resistance, or electrical insulation. Standard component of EWOD chip fabrication (as dielectric layer) and many implantable / wearable microfluidic devices. The pyrolysis-of-dimer chemistry is what enables true conformal coating including inside enclosed channels — distinguishes parylene from spin-coated dielectrics.",
)

add(
    id="microcontact-printing-protein-pattern",
    canonical_name="Microcontact printing for protein and SAM patterning on chip surfaces",
    aliases=["µCP protein patterning", "microcontact printing baseline"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="surface-modification",
    substrate_material="glass / silicon / gold-coated substrate",
    output_artifact="Patterned protein, antibody, or SAM monolayer in arbitrary 2D geometry on chip surface, with sub-µm feature resolution.",
    steps=[
        {"order": 1, "action": "Cast PDMS stamp from SU-8 master", "parameters": "10:1 PDMS poured over SU-8 master; degas 30 min; cure 60 min @ 65 °C; cut into stamp blocks ~1 cm × 1 cm", "duration": "1.5 hr", "notes": "Stamp feature heights typically 1 µm to 50 µm"},
        {"order": 2, "action": "Ink stamp", "parameters": "drop ~50 µL ink solution (protein + buffer, or alkanethiol in ethanol) on stamp surface; let adsorb 30 s; dry under N2", "duration": "5 min", "notes": "Ink loading determines transferred amount; over-loading causes feature blurring"},
        {"order": 3, "action": "Place stamp on substrate", "parameters": "gentle contact between stamp features and clean substrate surface; conformal contact for 1–60 s", "duration": "5 min", "notes": "Self-conforming PDMS-substrate contact transfers ink in feature pattern only"},
        {"order": 4, "action": "Remove stamp", "parameters": "lift stamp cleanly; substrate now bears patterned ink corresponding to stamp features", "duration": "1 min", "notes": ""},
        {"order": 5, "action": "Backfill (optional)", "parameters": "for proteins on hydrophobic surfaces: backfill non-patterned regions with BSA or PEG to prevent non-specific binding", "duration": "30 min", "notes": "Critical for biological assays where non-pattern adsorption matters"},
        {"order": 6, "action": "Rinse and use", "parameters": "rinse with buffer; substrate ready for cell or assay deployment", "duration": "5 min", "notes": ""},
    ],
    critical_parameters=[
        {"parameter": "Stamp feature size", "target": ">1 µm typical", "tolerance": "limited by SU-8 master and PDMS resolution", "failure_at_off_spec": "sub-µm features blur due to ink diffusion in PDMS"},
        {"parameter": "Ink concentration", "target": "0.01–0.1 mg/mL protein typical", "tolerance": "1× to 10×", "failure_at_off_spec": "low: incomplete pattern transfer; high: feature blurring"},
        {"parameter": "Contact pressure", "target": "gentle hand pressure", "tolerance": "no specific spec", "failure_at_off_spec": "excessive pressure causes feature collapse and over-printing"},
        {"parameter": "Substrate cleanliness", "target": "freshly cleaned", "tolerance": "<24 hr after cleaning", "failure_at_off_spec": "contaminated surface gives non-uniform pattern transfer"},
    ],
    equipment_required=[
        {"instrument_class": "PDMS soft-lithography setup", "optional_model": "see pdms-su8-soft-lithography-baseline", "notes": "for stamp casting"},
        {"instrument_class": "tweezers and inspection microscope", "optional_model": "any", "notes": "for stamp handling and pattern QC"},
    ],
    materials_required=[
        {"material": "PDMS stamp (see soft-lithography recipe)", "vendor": "internal", "part_number_optional": None},
        {"material": "ink solution (protein, antibody, alkanethiol per use)", "vendor": "various", "part_number_optional": None},
        {"material": "substrate (gold-coated, glass, or silicon)", "vendor": "any", "part_number_optional": None},
    ],
    validated_outcome="Reproduces patterns 1 µm to 1 mm in arbitrary 2D geometry with single-protein-monolayer resolution. Used widely in cell-patterning, biosensor arrays, and surface-chemistry research.",
    failure_modes=[
        {"mode": "Stamp adhesion to substrate", "diagnostic_signature": "stamp does not release cleanly", "corrective_action": "verify PDMS cure was complete; reduce contact pressure"},
        {"mode": "Pattern blurring at edges", "diagnostic_signature": "fuzzy boundaries between patterned and non-patterned regions", "corrective_action": "reduce ink concentration; shorter contact time; better PDMS post-cure"},
        {"mode": "Incomplete pattern transfer", "diagnostic_signature": "only some stamp features transferred", "corrective_action": "verify uniform stamp-substrate contact; clean substrate; longer contact time"},
    ],
    related_corpus_entries=["kumar-whitesides-1993-microcontact-printing", "xia-whitesides-1998-soft-lithography-review", "ulman-1996-self-assembled-monolayers"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline"],
    publication_citation="Kumar & Whitesides 1993 Appl. Phys. Lett. 63, 2002–2004",
    sources=[
        "Kumar, A.; Whitesides, G. M. Appl. Phys. Lett. 1993, 63, 2002–2004",
        "Xia, Y.; Whitesides, G. M. Annu. Rev. Mater. Sci. 1998, 28, 153–184",
    ],
    notes="Microcontact printing (µCP) is the canonical method for patterning biomolecules on chip surfaces. Directly extends PDMS soft-lithography from channel fabrication to surface patterning. Widely used in single-cell capture, biosensor arrays, and patterned co-culture systems.",
)


with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new recipes to {OUT}")
