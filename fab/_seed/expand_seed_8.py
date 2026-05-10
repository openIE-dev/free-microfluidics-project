#!/usr/bin/env python3
"""Eighth expansion of fabrication recipes."""
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
    id="sacrificial-mold-3d-print-elastomer",
    canonical_name="3D-printed sacrificial molding for cast-elastomer microfluidics",
    aliases=["sacrificial mold microfluidics", "PVA dissolvable mold"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="pdms-soft-lithography",
    substrate_material="PDMS or silicone rubber + dissolvable PVA / sugar / wax sacrificial mold",
    output_artifact="3D-shape elastomer microfluidic chip with arbitrary internal channel geometry that cannot be produced by planar photolithography (e.g. true 3D vasculature networks, helical channels, internal chambers with overhangs).",
    steps=[
        {"order": 1, "action": "Design 3D channel geometry", "parameters": "CAD model of channel network as a positive (the channel volume itself becomes the sacrificial mold)", "duration": "1 hr", "notes": "Constraints: minimum 200 µm features for FDM-printed PVA; minimum 50 µm for SLA-printed water-soluble resin"},
        {"order": 2, "action": "3D-print sacrificial mold", "parameters": "FDM with PVA filament (water-dissolvable) at 200 °C, OR SLA with water-soluble resin (e.g. Formlabs water-washable WW), OR machined isomalt sugar mold", "duration": "2–8 hr", "notes": "Surface finish translates directly to channel wall finish — FDM gives ~50 µm layer marks, SLA gives sub-10 µm"},
        {"order": 3, "action": "Position mold in casting form", "parameters": "place sacrificial mold in casting box; suspend mold using thin support strands or pins that will leave access ports", "duration": "20 min", "notes": "Suspension geometry determines port locations; leave room for connector inserts"},
        {"order": 4, "action": "Pour PDMS or silicone around mold", "parameters": "10:1 PDMS or RTV-2 silicone poured around mold; degas 30 min in vacuum chamber", "duration": "1 hr", "notes": "Vacuum degas removes air bubbles trapped against mold features"},
        {"order": 5, "action": "Cure elastomer", "parameters": "60 °C 4 hr for PDMS; RT 24 hr for RTV-2 silicone", "duration": "4–24 hr", "notes": "Curing temperature must be below sacrificial mold's deformation point: PVA softens above 60 °C, sugar above 100 °C"},
        {"order": 6, "action": "Dissolve sacrificial mold", "parameters": "for PVA: warm water 50 °C 4–24 hr; for sugar: warm water 30 min; for wax: heat above melting point (60–80 °C) and flush", "duration": "1–24 hr", "notes": "Long dissolution time for complex 3D networks; agitate or use mild flow during dissolution"},
        {"order": 7, "action": "Flush and verify channels", "parameters": "flush channels with water; verify geometry by injecting dye and imaging via X-ray CT or sectioning", "duration": "1 hr", "notes": ""},
        {"order": 8, "action": "Connect tubing", "parameters": "epoxy tubing into ports left by mold suspension geometry", "duration": "30 min", "notes": ""},
    ],
    critical_parameters=[
        {"parameter": "Sacrificial mold material", "target": "PVA / water-soluble resin / isomalt / wax", "tolerance": "any dissolvable", "failure_at_off_spec": "non-dissolvable mold cannot be removed; partially-dissolvable leaves residue inside channels"},
        {"parameter": "Casting cure temperature", "target": "below mold softening point", "tolerance": "<50 °C for PVA, <80 °C for sugar", "failure_at_off_spec": "high cure T deforms mold and channel geometry"},
        {"parameter": "Dissolution completeness", "target": "100% mold removal", "tolerance": "verify by injection / imaging", "failure_at_off_spec": "residual mold blocks channels and contaminates samples"},
        {"parameter": "Surface finish", "target": "limited by 3D-printer resolution", "tolerance": "FDM: ~50 µm, SLA: ~10 µm, machined: ~5 µm", "failure_at_off_spec": "rough channel walls cause turbulence and unwanted mixing"},
    ],
    equipment_required=[
        {"instrument_class": "FDM 3D printer with PVA capability", "optional_model": "Prusa MK4 with multi-material upgrade / any dual-extruder", "notes": "for PVA sacrificial molds"},
        {"instrument_class": "SLA 3D printer with water-soluble resin (alternative)", "optional_model": "Formlabs Form 3+", "notes": "for higher-resolution sacrificial molds"},
        {"instrument_class": "vacuum degassing chamber", "optional_model": None, "notes": ""},
        {"instrument_class": "warm water bath", "optional_model": None, "notes": "for PVA dissolution"},
    ],
    materials_required=[
        {"material": "PVA filament (FDM)", "vendor": "MatterHackers / eSun", "part_number_optional": "PVA 1.75 mm"},
        {"material": "water-washable SLA resin (alternative)", "vendor": "Formlabs / Anycubic", "part_number_optional": "Formlabs WW or Anycubic water-washable"},
        {"material": "Sylgard 184 PDMS (10:1)", "vendor": "Dow", "part_number_optional": None},
        {"material": "alternative: Smooth-On Mold Star RTV silicone", "vendor": "Smooth-On", "part_number_optional": "Mold Star 30"},
    ],
    validated_outcome="Reproduces 3D channel networks with feature size limited by 3D-printer resolution (50–200 µm typical for FDM, 10 µm for SLA). Suitable for organ-vasculature mimicry, helical mixers, and 3D channel topologies impossible with planar photolithography.",
    failure_modes=[
        {"mode": "Mold breaks during PDMS pour", "diagnostic_signature": "channel network distorted in finished chip", "corrective_action": "stiffen mold geometry; cure PDMS at lower temperature; degas more slowly to avoid pressure transients"},
        {"mode": "Incomplete mold dissolution", "diagnostic_signature": "channels show partial blockage", "corrective_action": "longer dissolution; warmer water; mild flow during dissolution; sectioning may be needed for complex networks"},
        {"mode": "Surface finish too rough for application", "diagnostic_signature": "unwanted turbulence or particle trapping in channels", "corrective_action": "switch to higher-resolution sacrificial mold (SLA vs FDM); chemical polish PVA mold before casting"},
    ],
    related_corpus_entries=["miller-bhatia-2012-vasculature-on-chip", "kolesky-lewis-2014-3d-bioprinted-vasculature", "two-photon-polymerization-nanoscribe-baseline"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline"],
    publication_citation="Miller, J. S. et al. Rapid casting of patterned vascular networks for perfusable engineered three-dimensional tissues. Nat. Mater. 2012, 11, 768–774. DOI: 10.1038/nmat3357",
    sources=[
        "Miller, J. S. et al. Nat. Mater. 2012, 11, 768–774",
        "Kolesky, D. B. et al. Adv. Mater. 2014, 26, 3124–3130",
    ],
    notes="Sacrificial molding extends elastomer microfluidic fabrication into 3D channel topologies otherwise impossible with planar photolithography. The Miller-Bhatia 2012 demonstration of 3D-printed sugar networks for tissue engineering is the canonical reference. Particularly important for organ-on-chip vascular networks, helical mixers, and multi-layer 3D circuit topologies.",
)


with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new recipes to {OUT}")
