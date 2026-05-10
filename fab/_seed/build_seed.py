#!/usr/bin/env python3
"""Generate seed fabrication recipes."""
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
    id="pdms-su8-soft-lithography-baseline",
    canonical_name="Baseline SU-8 + PDMS soft lithography",
    aliases=["PDMS soft litho baseline", "Whitesides baseline"],
    contributor="Free Microfluidics Project (community-curated baseline recipe)",
    contributor_country="US",
    recipe_class="pdms-soft-lithography",
    substrate_material="PDMS on SU-8 master on silicon wafer",
    output_artifact="PDMS chip with replicated channels, plasma-bonded to glass slide; channels 50 µm to 200 µm wide.",
    steps=[
        {"order": 1, "action": "Clean 4-inch silicon wafer", "parameters": "piranha 4:1 H2SO4:H2O2 for 10 min, DI rinse, N2 dry; 200 °C dehydration bake 10 min", "duration": "30 min", "notes": "Substitute O2 plasma if piranha unavailable"},
        {"order": 2, "action": "Spin coat SU-8 2050", "parameters": "static dispense ~3 mL, ramp 100 rpm/s to 500 rpm hold 10 s, ramp 300 rpm/s to 1500 rpm hold 30 s for 50 µm thickness", "duration": "1 min", "notes": "Adjust spin speed per Kayaku datasheet for target thickness"},
        {"order": 3, "action": "Soft bake", "parameters": "65 °C 5 min, ramp to 95 °C, hold 15 min for 50 µm; cool to room temp slowly on hot plate", "duration": "30 min", "notes": "Slow cooldown reduces edge-bead crack risk"},
        {"order": 4, "action": "UV expose through chrome mask", "parameters": "365 nm i-line, dose 250 mJ/cm² for 50 µm SU-8 2050; vacuum-contact alignment", "duration": "1–2 min", "notes": "Dose scales with thickness; consult Kayaku Y2 chart"},
        {"order": 5, "action": "Post-exposure bake", "parameters": "65 °C 1 min then 95 °C 5 min; slow cooldown", "duration": "10 min", "notes": "Critical for crosslinking; do not skip"},
        {"order": 6, "action": "Develop", "parameters": "SU-8 developer (PGMEA) immersion with mild agitation 6 min for 50 µm, IPA rinse 30 s, N2 dry", "duration": "10 min", "notes": "Check under microscope; under-development leaves residue"},
        {"order": 7, "action": "Hard bake (optional)", "parameters": "150 °C 10 min for adhesion improvement", "duration": "20 min", "notes": "Skip if features <20 µm wide to avoid distortion"},
        {"order": 8, "action": "Silanize master", "parameters": "vapor-phase trichloro(perfluorooctyl)silane in vacuum desiccator, 1 hr", "duration": "1 hr", "notes": "Critical for clean PDMS release; failure causes master destruction on first peel"},
        {"order": 9, "action": "Mix and degas PDMS", "parameters": "Sylgard 184 base:cure 10:1 by mass, 5 min mix, 30 min vacuum desiccator", "duration": "45 min", "notes": "Variability in mix ratio is largest yield killer"},
        {"order": 10, "action": "Pour and cure PDMS", "parameters": "pour onto silanized master, cure 65 °C 60 min", "duration": "1 hr", "notes": "Higher temperature shortens cure but stresses master"},
        {"order": 11, "action": "Peel and dice", "parameters": "scalpel cut PDMS at chip outline, peel slowly from master, punch inlet/outlet ports with 0.75 mm biopsy punch", "duration": "30 min", "notes": "Use ethanol to lubricate punch"},
        {"order": 12, "action": "Plasma bond to glass", "parameters": "30 s O2 plasma at ~30 W on PDMS and glass slide; immediately press together; bake 80 °C 30 min", "duration": "1 hr", "notes": "Bonding window is ~60 s after plasma; longer waits weaken bond"},
    ],
    critical_parameters=[
        {"parameter": "SU-8 spin speed", "target": "1500 rpm for 50 µm", "tolerance": "±50 rpm", "failure_at_off_spec": "thickness deviates linearly with spin; affects channel depth"},
        {"parameter": "Soft-bake temperature", "target": "95 °C peak", "tolerance": "±2 °C", "failure_at_off_spec": "incomplete solvent removal causes wrinkling and edge bead"},
        {"parameter": "UV dose", "target": "250 mJ/cm² for 50 µm 2050", "tolerance": "±10%", "failure_at_off_spec": "underexposure causes T-topping; overexposure widens features"},
        {"parameter": "PDMS mix ratio", "target": "10:1 base:curing", "tolerance": "±0.1 in ratio", "failure_at_off_spec": "off-spec ratios produce sticky or brittle PDMS; compromises bonding"},
        {"parameter": "Plasma exposure window", "target": "<60 s post-plasma to contact", "tolerance": "<90 s", "failure_at_off_spec": "weak bond, leaks under pressure"},
    ],
    equipment_required=[
        {"instrument_class": "spin coater", "optional_model": "Laurell WS-650Mz", "notes": "any spin coater with programmable ramp"},
        {"instrument_class": "hot plate", "optional_model": None, "notes": "two minimum, programmable preferred"},
        {"instrument_class": "UV mask aligner", "optional_model": "OAI 200 / Suss MJB4 / 365 nm LED with collimator", "notes": "DIY UV LED + photomask works for >50 µm features"},
        {"instrument_class": "vacuum desiccator", "optional_model": None, "notes": "for PDMS degas and silanization"},
        {"instrument_class": "plasma cleaner", "optional_model": "Harrick PDC-32G", "notes": "tabletop O2 plasma sufficient"},
        {"instrument_class": "biopsy punch", "optional_model": "0.75 mm Miltex", "notes": "size to match tubing OD"},
    ],
    materials_required=[
        {"material": "SU-8 2050", "vendor": "Kayaku Advanced Materials", "part_number_optional": "Y111072"},
        {"material": "SU-8 developer (PGMEA)", "vendor": "Kayaku", "part_number_optional": None},
        {"material": "Sylgard 184 PDMS", "vendor": "Dow Corning", "part_number_optional": "Sylgard 184"},
        {"material": "trichloro(perfluorooctyl)silane", "vendor": "Sigma-Aldrich", "part_number_optional": "448931"},
        {"material": "4-inch silicon wafers", "vendor": "any", "part_number_optional": "100 mm prime"},
        {"material": "1 mm soda-lime or borofloat slides", "vendor": "Schott / VWR", "part_number_optional": None},
    ],
    validated_outcome="Reproduces 50 µm channels at 75 mm × 25 mm chip footprint with bond strengths >300 kPa burst pressure (typical) when fresh-plasma-bonded.",
    failure_modes=[
        {"mode": "PDMS won't release from master", "diagnostic_signature": "tearing on peel, master destruction", "corrective_action": "re-silanize; verify silane vapor was fresh"},
        {"mode": "Channels collapse on bonding", "diagnostic_signature": "channels deform under microscope", "corrective_action": "increase aspect ratio (deeper or narrower channels), reduce plasma duration"},
        {"mode": "Bond fails under flow", "diagnostic_signature": "leakage under pressure", "corrective_action": "reduce wait time between plasma and contact; verify clean glass surface"},
        {"mode": "SU-8 features lift off wafer", "diagnostic_signature": "small features missing after develop", "corrective_action": "improve adhesion: O2 plasma pre-treat, dehydration bake, or HMDS prime"},
    ],
    related_cad_designs=["pdms-flow-focusing-droplet-junction-50um", "pdms-staggered-herringbone-mixer-reference"],
    related_corpus_entries=["duffy-1998-pdms-soft-lithography-microfluidics"],
    publication_citation="Duffy et al. 1998, Anal. Chem. 70, 4974–4984. DOI 10.1021/ac980656z",
    sources=[
        "Kayaku SU-8 2000 series datasheet",
        "Dow Sylgard 184 datasheet",
        "Whitesides group PDMS protocols (multiple)",
        "Duffy et al. 1998",
    ],
    notes="Baseline recipe. Most groups develop their own variant; this version is intentionally conservative. Patent considerations: PDMS soft lithography itself is unpatented (and would be unenforceable as prior art predates 1998). Specific applications may be patented (e.g., Quake valve architecture); flag downstream.",
)

add(
    id="dlp-sla-enclosed-channels-pegda-baseline",
    canonical_name="Baseline DLP-SLA enclosed-channel print (PEGDA)",
    aliases=["DLP enclosed channels baseline"],
    contributor="Free Microfluidics Project (placeholder; Nordin group recipe family is the reference)",
    contributor_country="US",
    recipe_class="dlp-sla-enclosed-channels",
    substrate_material="PEGDA-based photopolymer",
    output_artifact="3D-printed device with fully enclosed microfluidic channels, no post-print sealing required.",
    steps=[
        {"order": 1, "action": "Prepare resin", "parameters": "PEGDA-258 with 1 wt% phenylbis(2,4,6-trimethylbenzoyl)phosphine oxide (Irgacure 819 / TPO-L) photoinitiator + 1 wt% avobenzone UV absorber for ~25 µm penetration depth", "duration": "30 min", "notes": "Absorber concentration tunes Z-resolution; recipe target is 25 µm penetration"},
        {"order": 2, "action": "Calibrate printer", "parameters": "verify pixel pitch, expose calibration squares, measure Z-step accuracy with profilometer", "duration": "1 hr", "notes": "Critical: Z-step must equal optical penetration depth, not arbitrary smaller layer"},
        {"order": 3, "action": "Slice geometry", "parameters": "layer thickness = 25 µm matching penetration depth; build orientation chosen so channels run perpendicular to print axis", "duration": "10 min", "notes": "Channels parallel to print axis fail to enclose"},
        {"order": 4, "action": "Print", "parameters": "exposure 4 s/layer at 405 nm, ~2 mW/cm² intensity at build plane", "duration": "30 min for typical chip", "notes": "Adjust exposure with absorber concentration; characterize by test channel widths"},
        {"order": 5, "action": "Drain channels", "parameters": "flush channels with isopropanol via syringe immediately after print, before post-cure", "duration": "10 min", "notes": "Uncured resin trapped in channels will solidify on post-cure and clog"},
        {"order": 6, "action": "Post-cure", "parameters": "405 nm flood, 5 min on each side", "duration": "15 min", "notes": "Insufficient post-cure leaves device tacky and reduces strength"},
        {"order": 7, "action": "Surface treatment (optional)", "parameters": "rinse with PEG200 then DI water for hydrophilic channels; otherwise proceed to use", "duration": "30 min", "notes": "Untreated PEGDA-258 channels are mildly hydrophobic"},
    ],
    critical_parameters=[
        {"parameter": "UV absorber concentration", "target": "1 wt% avobenzone (depth tuning)", "tolerance": "±0.1 wt%", "failure_at_off_spec": "deeper penetration over-cures into channel; shallower fails to enclose"},
        {"parameter": "Layer thickness vs penetration depth", "target": "Z-step = penetration depth", "tolerance": "±1 µm", "failure_at_off_spec": "Z-step < penetration: channels under-cure; Z-step > penetration: layers don't bond"},
        {"parameter": "Exposure dose per layer", "target": "8 mJ/cm²", "tolerance": "±10%", "failure_at_off_spec": "underexposure: weak layer-to-layer bond; overexposure: feature growth into channel"},
        {"parameter": "Post-print drain timing", "target": "<5 min after print", "tolerance": "<15 min", "failure_at_off_spec": "delayed drain causes resin gelling in channels"},
    ],
    equipment_required=[
        {"instrument_class": "DLP-SLA printer", "optional_model": "Asiga Pro 4K / Phrozen Sonic Mini / custom", "notes": "must support custom resin and exposure-per-layer control"},
        {"instrument_class": "405 nm flood post-cure unit", "optional_model": "Asiga Flash / DIY UV chamber", "notes": "any post-cure with ≥10 mW/cm² at 405 nm"},
        {"instrument_class": "syringe / pressure source", "optional_model": None, "notes": "for channel drain"},
    ],
    materials_required=[
        {"material": "PEGDA-258", "vendor": "Sigma-Aldrich", "part_number_optional": "475629"},
        {"material": "TPO-L (Irgacure 819)", "vendor": "Sigma-Aldrich", "part_number_optional": None},
        {"material": "avobenzone (UV absorber)", "vendor": "Sigma-Aldrich", "part_number_optional": None},
        {"material": "isopropanol (drain solvent)", "vendor": "any", "part_number_optional": None},
    ],
    validated_outcome="Targeted reproduction of Gong et al. 2017 / Nordin group baseline: 50–100 µm enclosed channels reliably, 18–25 µm channels with careful tuning. Multi-resolution sub-2-µm channels (Miner 2026) require custom multi-wavelength engine, not in scope of this baseline.",
    failure_modes=[
        {"mode": "Channels clogged after print", "diagnostic_signature": "no flow on injection", "corrective_action": "improve drain procedure; reduce post-cure flood time"},
        {"mode": "Channels collapsed", "diagnostic_signature": "channels visible but no flow", "corrective_action": "reduce exposure dose; verify Z-step matches penetration depth"},
        {"mode": "Layer delamination", "diagnostic_signature": "device splits along build axis under load", "corrective_action": "increase exposure dose by 10%; verify post-cure"},
    ],
    related_cad_designs=[],
    related_corpus_entries=["gong-2017-3d-printed-18x20-microfluidic-channels", "miner-2026-multi-resolution-3d-printing-microfluidics"],
    publication_citation="Gong et al. 2017, Lab Chip 17, 2899–2909. DOI 10.1039/C7LC00644F",
    sources=[
        "Gong, Bickham, Woolley, Nordin 2017 Lab Chip",
        "Nordin group BYU SOPs (publicly described)",
        "PEGDA-258 datasheet",
    ],
    notes="Baseline recipe captures the enclosed-channel DLP-SLA approach; specific high-resolution variants require multi-wavelength engines (see Miner 2026). The recipe-as-text is unencumbered; specific resin formulations may carry patent claims (check Nordin group's BYU TTO portfolio for formulations claimed in published work).",
    draft=True,  # marked draft because the contributor field is a placeholder
)

with OUT.open("w") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  wrote {len(ENTRIES)} recipes to {OUT}")
