#!/usr/bin/env python3
"""Third expansion of fabrication recipes: glass capillary pulling, SU-8 baseline."""
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
    id="su8-master-baseline",
    canonical_name="SU-8 master fabrication baseline (for PDMS replication)",
    aliases=["SU-8 master", "SU-8 photoresist baseline"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="silicon-surface-micromachining",
    substrate_material="silicon wafer with patterned SU-8 negative photoresist",
    output_artifact="Silicon wafer with raised SU-8 features defining channel master pattern, suitable for casting PDMS replicas (reusable >100 times if handled carefully).",
    steps=[
        {"order": 1, "action": "Clean silicon wafer", "parameters": "acetone + IPA + DI rinse + N2 dry; or piranha clean for highest reliability", "duration": "10 min", "notes": "Clean wafer is essential for SU-8 adhesion"},
        {"order": 2, "action": "Dehydration bake", "parameters": "200 °C 5 min on hotplate", "duration": "10 min", "notes": "Drives off adsorbed moisture; critical for SU-8 adhesion"},
        {"order": 3, "action": "Spin-coat SU-8", "parameters": "SU-8 2050 at 3000 rpm 30 s for ~50 µm thickness; SU-8 2025 at 3000 rpm for ~25 µm; consult MicroChem datasheet for thickness vs spin curve", "duration": "5 min", "notes": "Thickness sets channel depth in final PDMS chip"},
        {"order": 4, "action": "Soft bake", "parameters": "65 °C 2 min, ramp to 95 °C, hold 5 min for 50 µm SU-8 (extend for thicker layers per datasheet)", "duration": "15 min", "notes": "Two-step bake reduces edge bead and improves resolution"},
        {"order": 5, "action": "UV exposure through photomask", "parameters": "365 nm i-line, dose ~150 mJ/cm² for 50 µm SU-8 (datasheet); use long-pass filter to block <350 nm wavelengths that cause T-topping", "duration": "1–2 min", "notes": "Underexposure gives weak crosslinking; overexposure gives blown-out features"},
        {"order": 6, "action": "Post-exposure bake (PEB)", "parameters": "65 °C 1 min, ramp to 95 °C, hold 5 min", "duration": "15 min", "notes": "Critical for crosslinking; skipping causes feature loss"},
        {"order": 7, "action": "Develop", "parameters": "PGMEA developer (SU-8 developer / mr-Dev 600) with agitation, 5–10 min for 50 µm features; IPA rinse; DI rinse; N2 dry", "duration": "20 min", "notes": "Inspect under microscope before proceeding; develop longer if residue persists"},
        {"order": 8, "action": "Hard bake (optional)", "parameters": "180 °C 30 min", "duration": "1 hr", "notes": "Improves chemical resistance and feature durability for repeated PDMS casting"},
        {"order": 9, "action": "Silane treatment (for PDMS release)", "parameters": "vapor-phase trichloro(1H,1H,2H,2H-perfluorooctyl)silane in vacuum desiccator overnight", "duration": "12 hr", "notes": "Prevents PDMS adhesion to master; reapply every ~50 castings"},
    ],
    critical_parameters=[
        {"parameter": "SU-8 thickness", "target": "set by spin speed per datasheet", "tolerance": "±5%", "failure_at_off_spec": "thickness sets channel depth; non-uniform thickness gives variable channel depth across chip"},
        {"parameter": "Soft bake / PEB temperatures", "target": "two-step ramped bake", "tolerance": "±2 °C", "failure_at_off_spec": "under-baked: weak adhesion; over-baked: thermal stress, cracks"},
        {"parameter": "UV exposure dose", "target": "150 mJ/cm² for 50 µm", "tolerance": "±10%", "failure_at_off_spec": "under-exposed: features dissolve; over-exposed: features widened by reflection"},
        {"parameter": "Develop time", "target": "5–10 min for 50 µm SU-8", "tolerance": "until clean", "failure_at_off_spec": "incomplete develop: residue at feature bases blocks PDMS replication"},
    ],
    equipment_required=[
        {"instrument_class": "spin coater", "optional_model": None, "notes": ""},
        {"instrument_class": "UV mask aligner", "optional_model": "Suss MA6, OAI 200, EVG 620 (cleanroom) or homemade UV LED contact aligner", "notes": "365 nm with i-line filter"},
        {"instrument_class": "hotplates", "optional_model": "Torrey Pines HS40A or equivalent", "notes": "two needed for two-stage bake"},
        {"instrument_class": "vacuum desiccator", "optional_model": None, "notes": "for silane treatment"},
    ],
    materials_required=[
        {"material": "silicon wafers (4 inch, single-side polished)", "vendor": "any", "part_number_optional": "525 µm SSP"},
        {"material": "SU-8 2050 photoresist", "vendor": "MicroChem / Kayaku", "part_number_optional": "SU-8 2050"},
        {"material": "PGMEA SU-8 developer", "vendor": "MicroChem / Kayaku", "part_number_optional": "SU-8 developer or mr-Dev 600"},
        {"material": "perfluorooctylsilane (silane release agent)", "vendor": "Sigma-Aldrich", "part_number_optional": "448931"},
    ],
    validated_outcome="Reproduces 50 µm × N µm SU-8 features at ±5 µm dimensional tolerance; master typically supports 100+ PDMS castings before requiring re-silanization or replacement.",
    failure_modes=[
        {"mode": "Feature delamination", "diagnostic_signature": "SU-8 features peel off during develop or first PDMS casting", "corrective_action": "verify wafer cleanliness; longer dehydration bake; check soft-bake temperature"},
        {"mode": "Cracked SU-8 features", "diagnostic_signature": "linear cracks in tall features", "corrective_action": "slower temperature ramps in soft bake and PEB; consider lower-stress SU-8 variants (SU-8 3000 series)"},
        {"mode": "Feature widening", "diagnostic_signature": "features wider than designed by >5 µm", "corrective_action": "reduce UV exposure dose; verify mask contact pressure; use anti-reflective coating on wafer"},
    ],
    related_corpus_entries=["duffy-1998-pdms-soft-lithography-microfluidics", "xia-whitesides-1998-soft-lithography-review"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline"],
    publication_citation="MicroChem / Kayaku SU-8 datasheets",
    sources=[
        "MicroChem SU-8 2000 series datasheet",
        "del Campo, A.; Greiner, C. SU-8: a photoresist for high-aspect-ratio and 3D submicron lithography. J. Micromech. Microeng. 2007, 17, R81–R95",
    ],
    notes="SU-8 master fabrication is the bottleneck step in PDMS soft lithography (the PDMS step itself is straightforward). Most academic labs outsource master fabrication to a cleanroom; this recipe documents the standard process for those building in-house capability. SU-8 2050 covers the most common 50 µm channel depth; the 2000 and 3000 series datasheets cover 1 µm to 500 µm range.",
)

add(
    id="glass-capillary-pulling-baseline",
    canonical_name="Glass capillary pulling for ESI emitter / patch pipette / DNA injection",
    aliases=["fused silica capillary pulling", "ESI tip pulling"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="other",
    substrate_material="borosilicate or fused-silica capillary tubing (typ. 1 mm OD, 0.5 mm ID)",
    output_artifact="Pulled capillary tip with sub-micrometer to ~10 µm orifice diameter, suitable as ESI emitter, patch pipette, or microinjection needle.",
    steps=[
        {"order": 1, "action": "Cut capillary to length", "parameters": "score with diamond pen; snap; typical lengths 75 mm to 150 mm", "duration": "5 min", "notes": "Cleaner break gives better starting condition"},
        {"order": 2, "action": "Mount in puller", "parameters": "load capillary into puller jaws; center heating filament on capillary midpoint", "duration": "5 min", "notes": "Sutter P-97 / P-1000 or equivalent"},
        {"order": 3, "action": "Set pull program", "parameters": "single-stage pull for ESI emitters: HEAT 525, PULL 50, VEL 50, TIME 250 (Sutter P-97 unit values; calibrate per puller / box-filament combination)", "duration": "5 min", "notes": "Multi-stage programs give finer tip control"},
        {"order": 4, "action": "Execute pull", "parameters": "filament heats capillary above softening point (~820 °C for borosilicate); spring-loaded jaws separate, drawing capillary to a fine taper that breaks at the focused heating point", "duration": "30 s", "notes": "Each puller gives slightly different geometry; characterize with sample pulls"},
        {"order": 5, "action": "Inspect tip under microscope", "parameters": "10× to 40× magnification; measure tip OD against reticle", "duration": "5 min", "notes": "Reject tips outside target range"},
        {"order": 6, "action": "Optional fire-polishing", "parameters": "platinum/iridium heating element + microscope; touch heater briefly to tip to round edges", "duration": "10 min", "notes": "For patch pipettes, smooths tip for cell sealing; not needed for ESI"},
        {"order": 7, "action": "Optional bevel grinding", "parameters": "rotating diamond grinding wheel for angled tip", "duration": "10 min", "notes": "For some patch-clamp and microinjection applications"},
    ],
    critical_parameters=[
        {"parameter": "Filament temperature (HEAT)", "target": "depends on filament/box; calibrate", "tolerance": "±10 units (Sutter)", "failure_at_off_spec": "too cold: thick neck, blunt tip; too hot: brittle, snaps unevenly"},
        {"parameter": "Pull velocity (VEL)", "target": "set per program", "tolerance": "±10%", "failure_at_off_spec": "affects tip cone angle and final OD"},
        {"parameter": "Time-out (TIME)", "target": "set per program", "tolerance": "±10%", "failure_at_off_spec": "affects whether tip is fully pulled or breaks early"},
        {"parameter": "Capillary cleanliness", "target": "particle-free", "tolerance": "wipe with IPA before mounting", "failure_at_off_spec": "contamination causes asymmetric pulls"},
    ],
    equipment_required=[
        {"instrument_class": "micropipette puller", "optional_model": "Sutter P-97 / P-1000 / P-2000 (laser); Narishige PC-100", "notes": "$8k–$25k commercial; community pullers exist for narrow applications"},
        {"instrument_class": "microscope", "optional_model": "any 10–40× stereo or compound", "notes": "for tip inspection"},
        {"instrument_class": "microforge (optional)", "optional_model": "Narishige MF-900", "notes": "for fire-polishing patch pipettes"},
    ],
    materials_required=[
        {"material": "borosilicate capillary tubing", "vendor": "Sutter Instrument / WPI / Drummond", "part_number_optional": "BF150-86-10 (1.5 mm OD, 0.86 mm ID)"},
        {"material": "fused silica capillary (for ESI)", "vendor": "Polymicro / IDEX / Molex", "part_number_optional": "TSP100170 (100 µm ID, 170 µm OD)"},
    ],
    validated_outcome="Reproduces 1–10 µm tip OD at ±20% with experienced operator; tip-to-tip variation in commercial pullers typically ±10%.",
    failure_modes=[
        {"mode": "Asymmetric tips", "diagnostic_signature": "tip pulled toward one side", "corrective_action": "verify capillary alignment; clean filament; rotate filament position"},
        {"mode": "Blocked tips", "diagnostic_signature": "no flow through pulled tip", "corrective_action": "verify capillary inner diameter pre-pull; pulled too fine — adjust pull program"},
        {"mode": "Brittle tips that snap on contact", "diagnostic_signature": "tip breaks during chip integration", "corrective_action": "lower HEAT setting; consider laser puller (Sutter P-2000) for fused silica"},
    ],
    related_corpus_entries=["ramsey-1996-electrospray-on-chip", "advion-triversa-nanomate"],
    related_fab_recipes=[],
    publication_citation="Sutter Instrument P-97/P-1000 manuals; Narishige PC-100 manual",
    sources=[
        "Sutter Instrument Pipette Cookbook (P-97/P-1000)",
        "Narishige PC-100 manual",
        "Polymicro Technologies fused silica tubing data sheet",
    ],
    notes="Glass capillary pulling is the canonical fabrication path for chip-to-MS interfaces (electrospray emitters), patch-clamp electrodes, intracellular microinjection, and many specialized microfluidic interfaces. Classified under 'other' recipe class because it's neither photolithography nor 3D-printing nor any of the planar substrate methods; the equipment is dedicated and the technique stands apart.",
)


with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new recipes to {OUT}")
