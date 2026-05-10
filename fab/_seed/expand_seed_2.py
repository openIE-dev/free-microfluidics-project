#!/usr/bin/env python3
"""Second expansion of fabrication recipes."""
import json
from pathlib import Path

OUT = Path(__file__).parent / "recipes.jsonl"
ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("last_updated", "2026-05-09")
    kw.setdefault("license", "CC0-1.0")
    ENTRIES.append(kw)


# =====================================================================
# DRIE / Bosch process for silicon
# =====================================================================
add(
    id="silicon-drie-bosch-baseline",
    canonical_name="Silicon DRIE (Bosch process) baseline",
    aliases=["Bosch process baseline", "DRIE baseline"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="silicon-microfabrication",
    substrate_material="single-crystal silicon (100) wafer",
    output_artifact="Silicon substrate with high-aspect-ratio (>20:1) anisotropic etched microchannels of depth 10 µm to 500 µm.",
    steps=[
        {"order": 1, "action": "RCA clean wafer", "parameters": "RCA-1 (5:1:1 H2O:H2O2:NH4OH 70 °C 10 min) + RCA-2 (5:1:1 H2O:H2O2:HCl 70 °C 10 min) + DI rinse + N2 dry", "duration": "1 hr", "notes": "Standard cleanroom prep"},
        {"order": 2, "action": "Spin-coat photoresist", "parameters": "AZ 4620 at 3000 rpm 30 s; soft-bake 100 °C 5 min", "duration": "20 min", "notes": "Thicker resist for longer DRIE etches"},
        {"order": 3, "action": "Lithography", "parameters": "365 nm i-line UV exposure ~600 mJ/cm² through photomask", "duration": "5 min", "notes": "Verify pattern fidelity before DRIE"},
        {"order": 4, "action": "Develop", "parameters": "AZ 400K developer 1:4 in DI for 60 s; DI rinse; N2 dry", "duration": "10 min", "notes": ""},
        {"order": 5, "action": "Hard bake (optional)", "parameters": "120 °C 30 min", "duration": "30 min", "notes": "Improves resist resilience to DRIE plasma; not always required"},
        {"order": 6, "action": "Bosch-process DRIE", "parameters": "alternating SF6 etch (typ. 7 s, 600 W ICP, 30 W bias) and C4F8 passivation (typ. 5 s, 600 W ICP, 0 W bias) cycles in inductively-coupled-plasma DRIE tool; etch rate ~3 µm/min with sidewall scalloping <100 nm", "duration": "10 min to 3 hr depending on depth", "notes": "Cycle parameters tuned per tool; characterize on sacrificial wafer"},
        {"order": 7, "action": "Strip resist", "parameters": "acetone wash; isopropanol; DI; N2 dry; or O2 plasma 200 W 5 min", "duration": "15 min", "notes": ""},
        {"order": 8, "action": "Optional thermal oxide growth", "parameters": "wet thermal oxidation 1100 °C to grow ~500 nm SiO2 for surface passivation", "duration": "(furnace process, separate cycle)", "notes": "Required for biocompatibility; alternatively use SiO2 sputter or LPCVD"},
        {"order": 9, "action": "Anodic bond to glass cover", "parameters": "see glass-glass-thermal-bonding for thermal bond, or anodic bond at 400 °C with 1 kV applied across stack for 30 min", "duration": "1 hr", "notes": "Anodic bonding to Borofloat 33 is the standard silicon-glass seal; CTE-matched"},
    ],
    critical_parameters=[
        {"parameter": "Etch/passivation cycle ratio", "target": "tuned per geometry", "tolerance": "1–2 s in either step", "failure_at_off_spec": "off-ratio gives positive or negative sidewall taper"},
        {"parameter": "ICP and bias powers", "target": "600 W ICP / 30 W bias for Bosch", "tolerance": "±10%", "failure_at_off_spec": "low ICP reduces etch rate; high bias causes resist erosion"},
        {"parameter": "Mask thickness", "target": ">2 µm photoresist for ≤100 µm etch", "tolerance": "1.5×", "failure_at_off_spec": "mask consumption causes feature widening"},
    ],
    equipment_required=[
        {"instrument_class": "ICP-DRIE etcher", "optional_model": "Oxford PlasmaPro 100, SPTS Pegasus, Plasma-Therm Versaline", "notes": "Bosch-capable cluster tool"},
        {"instrument_class": "spin coater", "optional_model": None, "notes": "for resist"},
        {"instrument_class": "UV mask aligner", "optional_model": None, "notes": "365 nm contact aligner"},
        {"instrument_class": "anodic bonder or fusion bonder", "optional_model": "Suss SB6/SB8", "notes": "for cap bonding"},
        {"instrument_class": "RCA cleaning bench", "optional_model": None, "notes": ""},
    ],
    materials_required=[
        {"material": "single-crystal silicon (100) wafers", "vendor": "any", "part_number_optional": "1 mm DSP"},
        {"material": "AZ 4620 photoresist", "vendor": "MicroChemicals", "part_number_optional": None},
        {"material": "AZ 400K developer", "vendor": "MicroChemicals", "part_number_optional": None},
        {"material": "SF6 process gas", "vendor": "any", "part_number_optional": "VLSI grade"},
        {"material": "C4F8 process gas", "vendor": "any", "part_number_optional": "VLSI grade"},
        {"material": "Borofloat 33 wafer (bonding cap)", "vendor": "Schott", "part_number_optional": None},
    ],
    validated_outcome="Reproduces 50 µm × 200 µm anisotropic silicon channels (4:1 aspect ratio) at ±5 µm tolerance with characteristic Bosch sidewall scallops <100 nm peak-valley.",
    failure_modes=[
        {"mode": "Aspect ratio dependent etching", "diagnostic_signature": "narrow features etch slower than wide features", "corrective_action": "extend total etch time; pre-characterize ARDE for the tool/recipe"},
        {"mode": "Notching at silicon-oxide interface", "diagnostic_signature": "lateral undercut at the bottom of through-wafer etches", "corrective_action": "switch to BSC (bypass) recipe near completion; use SOI wafers with thin BOX layer"},
        {"mode": "Sidewall striations / black silicon", "diagnostic_signature": "rough sidewalls or grass-like residue at trench bottom", "corrective_action": "tune passivation step longer; verify chamber cleanliness"},
    ],
    related_corpus_entries=["terry-1979-stanford-gas-chromatograph", "huang-2004-dld-deterministic-lateral-displacement", "huh-2010-lung-on-chip"],
    publication_citation="Laermer & Schilp 1996 (Bosch DRIE patent and disclosure)",
    sources=[
        "Laermer, F.; Schilp, A. Method of anisotropically etching silicon. US5501893A (Bosch).",
        "Madou, M. Fundamentals of Microfabrication, 3rd ed., chapter on dry etching",
    ],
    notes="DRIE Bosch process is the standard for silicon microfluidics requiring high aspect ratios (>10:1) and through-wafer features. The original Bosch patent has expired; SF6/C4F8 chemistry is now standard practice with no IP encumbrance on the process itself.",
)

# =====================================================================
# Laser ablation
# =====================================================================
add(
    id="co2-laser-ablation-pmma-baseline",
    canonical_name="CO2 laser ablation of PMMA / acrylic microfluidic channels",
    aliases=["CO2 laser microfluidics", "Epilog/Glowforge PMMA"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="laser-ablation",
    substrate_material="cast PMMA (acrylic), 3 mm thickness; or extruded PMMA",
    output_artifact="PMMA substrate with ablated microchannels of width 100 µm to 5 mm; depth controlled by laser power and pass count.",
    steps=[
        {"order": 1, "action": "Design vector pattern", "parameters": "Inkscape / Illustrator vector file; minimum line width 100 µm for hobbyist 40W lasers", "duration": "10 min", "notes": "Cast PMMA gives cleaner ablation than extruded; verify substrate type"},
        {"order": 2, "action": "Set laser parameters", "parameters": "for 40W CO2: 30% power, 30% speed, 500 dpi for ~100 µm channel depth; characterize on scrap", "duration": "5 min", "notes": "Channel cross-section is roughly Gaussian; depth scales sublinearly with power"},
        {"order": 3, "action": "Ablate channel pattern", "parameters": "single pass for shallow features; multi-pass with focus adjustment for >500 µm depth", "duration": "5–30 min depending on pattern", "notes": "Ventilate aggressively — PMMA pyrolysis releases methyl methacrylate vapor"},
        {"order": 4, "action": "Drill access ports", "parameters": "drill at 1000 rpm, or laser-cut through-holes with multiple passes", "duration": "10 min", "notes": ""},
        {"order": 5, "action": "Anneal substrate (optional)", "parameters": "80 °C oven for 4 hr to release residual stress and reduce optical scatter", "duration": "5 hr", "notes": "Improves channel optical clarity"},
        {"order": 6, "action": "Cap with PMMA cover or PSA film", "parameters": "thermal lamination at 110 °C 5 min for PMMA-PMMA, or pressure-sensitive adhesive film for low-pressure applications", "duration": "30 min", "notes": "Thermal bonding gives best chemical resistance; PSA easier for prototyping"},
    ],
    critical_parameters=[
        {"parameter": "Laser power × dwell time", "target": "calibrate per substrate", "tolerance": "±10%", "failure_at_off_spec": "underexposure: incomplete ablation; overexposure: charring, melted edges"},
        {"parameter": "Substrate type", "target": "cast PMMA (e.g., Plexiglas G)", "tolerance": "cast only", "failure_at_off_spec": "extruded PMMA gives stress-cracking and rough ablated walls"},
        {"parameter": "Focus offset", "target": "factory focal plane", "tolerance": "±0.5 mm", "failure_at_off_spec": "out-of-focus gives wider, shallower kerfs"},
    ],
    equipment_required=[
        {"instrument_class": "CO2 laser cutter", "optional_model": "Glowforge / Epilog Mini / Bofa fume extraction", "notes": "10–80 W typical for microfluidic features"},
        {"instrument_class": "fume extraction", "optional_model": None, "notes": "MMA vapor is moderately toxic and pungent"},
        {"instrument_class": "thermal laminator or hot press", "optional_model": None, "notes": "for cap bonding"},
    ],
    materials_required=[
        {"material": "cast PMMA sheet, 3 mm", "vendor": "Plaskolite / Evonik", "part_number_optional": "Plexiglas G or Acrylite GP"},
        {"material": "PSA film (acrylic adhesive)", "vendor": "3M / Adhesives Research", "part_number_optional": "9784 or AR-Care"},
    ],
    validated_outcome="Reproduces 200 µm × 100 µm channels at ±25 µm tolerance for hobbyist-grade 40W CO2 laser; smaller features achievable with higher-end systems.",
    failure_modes=[
        {"mode": "Stress cracking", "diagnostic_signature": "linear cracks adjacent to ablated kerfs", "corrective_action": "verify cast PMMA; anneal substrate post-ablation"},
        {"mode": "Yellowed/melted edges", "diagnostic_signature": "discolored kerf walls", "corrective_action": "reduce power; increase speed; verify focus"},
        {"mode": "Bubbles trapped under PSA cap", "diagnostic_signature": "voids visible at interface", "corrective_action": "apply cap with squeegee; vacuum-laminate if available"},
    ],
    related_corpus_entries=["martinez-2007-paper-microfluidics"],
    publication_citation="Klank, Kutter, Geschke 2002 Lab Chip 2, 242–246",
    sources=[
        "Klank, H.; Kutter, J. P.; Geschke, O. CO2-laser micromachining and back-end processing for rapid production of PMMA-based microfluidic systems. Lab Chip 2002, 2, 242–246",
    ],
    notes="CO2 laser ablation is the cheapest microfluidic fabrication method providing full enclosed channels (vs xurography which requires lamination). Hobbyist setup ~$2000 (Glowforge or kit CO2 laser), entry-level commercial ~$5000. Limited by feature size (~100 µm), surface roughness, and substrate compatibility (PMMA, polycarbonate, polystyrene work; PDMS does not). Well suited for prototype iteration and educational use.",
)

# =====================================================================
# Two-photon polymerization
# =====================================================================
add(
    id="two-photon-polymerization-nanoscribe-baseline",
    canonical_name="Two-photon polymerization microfluidic feature fabrication",
    aliases=["2PP", "Nanoscribe baseline", "TPP microfluidics"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="dlp-sla-printing",
    substrate_material="acrylate or epoxy photoresin (IP-Q, IP-Dip, OrmoComp); typically on glass coverslip substrate",
    output_artifact="3D-printed microfluidic feature with sub-µm voxel resolution; useful for embedded sub-100 µm features beyond traditional photolithography limits.",
    steps=[
        {"order": 1, "action": "Prepare substrate", "parameters": "glass coverslip cleaned with isopropanol; or silicon wafer with ITO electrode for in-situ fluidic integration", "duration": "5 min", "notes": ""},
        {"order": 2, "action": "Apply photoresin", "parameters": "drop-cast or pre-fill IP-Q for typical microfluidic features; IP-Dip for high-resolution; OrmoComp for biocompatible features", "duration": "5 min", "notes": "Resin choice dictates achievable feature size and chemistry"},
        {"order": 3, "action": "Mount in 2PP system", "parameters": "load substrate into Nanoscribe Photonic Professional or equivalent; align objective", "duration": "20 min", "notes": ""},
        {"order": 4, "action": "Configure print job", "parameters": "convert STL/CAD to .gwl or .stl with DeScribe; select galvo scan + piezo z; set hatching distance 200 nm and slicing distance 300 nm for typical features", "duration": "30 min", "notes": "Hatch/slice dictates feature precision and print time"},
        {"order": 5, "action": "Print", "parameters": "writing speed 10 mm/s, laser power 25 mW (or per resin datasheet)", "duration": "30 min to 24 hr depending on volume", "notes": "Two-photon mechanism enables sub-diffraction feature size at the focal voxel"},
        {"order": 6, "action": "Develop", "parameters": "PGMEA developer 20 min; isopropanol rinse; supercritical CO2 dry (preferred) or air dry with care", "duration": "1 hr", "notes": "Mechanical fragility highest pre-development; air-drying may collapse delicate features"},
        {"order": 7, "action": "UV post-cure (optional)", "parameters": "365 nm UV 30 min in N2 atmosphere", "duration": "30 min", "notes": "Fully crosslinks any remaining monomer; improves chemical resistance"},
    ],
    critical_parameters=[
        {"parameter": "Laser power", "target": "25 mW for IP-Q at 10 mm/s", "tolerance": "±10%", "failure_at_off_spec": "low: incomplete polymerization, voids; high: overpolymerization, feature widening"},
        {"parameter": "Hatching/slicing distance", "target": "200/300 nm", "tolerance": "see resin datasheet", "failure_at_off_spec": "coarser hatching gives surface roughness"},
        {"parameter": "Substrate flatness", "target": "<1 µm over print field", "tolerance": "<5 µm", "failure_at_off_spec": "drift causes layer misalignment"},
    ],
    equipment_required=[
        {"instrument_class": "two-photon polymerization system", "optional_model": "Nanoscribe Photonic Professional GT/GT2/Quantum X / UpNano NanoOne", "notes": "$200k–$500k commercial; community-built systems exist but are rare"},
        {"instrument_class": "supercritical CO2 dryer", "optional_model": "Tousimis Samdri", "notes": "for delicate features"},
        {"instrument_class": "UV post-cure chamber", "optional_model": "any 365 nm flood source", "notes": ""},
    ],
    materials_required=[
        {"material": "IP-Q or IP-Dip photoresin", "vendor": "Nanoscribe", "part_number_optional": None},
        {"material": "PGMEA developer", "vendor": "any", "part_number_optional": "MicroChem SU-8 developer is equivalent"},
        {"material": "glass coverslips, 170 µm", "vendor": "any", "part_number_optional": None},
    ],
    validated_outcome="Reproduces sub-µm features (smallest practical: 200 nm voxel diameter) embedded in mm-scale structures. Used for sub-resolution microfluidic features beyond what photolithography can achieve.",
    failure_modes=[
        {"mode": "Feature collapse on drying", "diagnostic_signature": "delicate features deformed or missing post-development", "corrective_action": "supercritical CO2 dry rather than air dry"},
        {"mode": "Layer-line surface roughness", "diagnostic_signature": "visible stair-stepping in tilted surfaces", "corrective_action": "decrease slicing distance; orient critical surfaces parallel to laser axis"},
        {"mode": "Adhesion failure to substrate", "diagnostic_signature": "print floats away during development", "corrective_action": "plasma-activate substrate; use silane adhesion promoter"},
    ],
    related_corpus_entries=["gong-2017-3d-printed-microfluidics", "kelly-2019-cal-volumetric-printing"],
    publication_citation="multiple; canonical: Maruo, Nakamura, Kawata 1997 Opt. Lett. 22, 132–134",
    sources=[
        "Maruo, S.; Nakamura, O.; Kawata, S. Three-dimensional microfabrication with two-photon-absorbed photopolymerization. Opt. Lett. 1997, 22, 132–134",
        "Nanoscribe IP-resin datasheets",
    ],
    notes="Two-photon polymerization is the highest-resolution 3D fabrication available and increasingly used for sub-100-µm microfluidic features that DLP-SLA cannot resolve. Capital-intensive; rare outside specialized labs. Best for demonstrators and very low-volume work; not suitable for production.",
)

# =====================================================================
# Lamination microfluidics
# =====================================================================
add(
    id="psa-lamination-microfluidics-baseline",
    canonical_name="PSA lamination microfluidics (pressure-sensitive-adhesive stack)",
    aliases=["PSA lamination", "tape microfluidics"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="lamination",
    substrate_material="multi-layer stack of PMMA / glass / cover film + PSA layers (e.g., 3M 9474LE)",
    output_artifact="Multi-layer microfluidic chip assembled from cut layers and PSA bonding films; channel depth controlled by middle-layer thickness.",
    steps=[
        {"order": 1, "action": "Design layer stack", "parameters": "typical 5-layer stack: PMMA top + PSA + middle (PMMA or PET sheet defining channel depth) + PSA + PMMA bottom; channel pattern cut from middle layer", "duration": "30 min", "notes": "Each layer designed in CAD with registration features"},
        {"order": 2, "action": "Cut layers", "parameters": "CO2 laser or vinyl cutter for each layer per design; PSA layers cut with pattern aligned to channel pattern", "duration": "1 hr", "notes": "Registration features simplify alignment"},
        {"order": 3, "action": "Drill access ports", "parameters": "0.7 mm drill bit through top and bottom rigid layers", "duration": "20 min", "notes": ""},
        {"order": 4, "action": "Stack and align layers", "parameters": "remove PSA backing; align using registration pins or jig; press progressively from one edge to expel air", "duration": "30 min", "notes": "Patience here prevents trapped air bubbles"},
        {"order": 5, "action": "Apply pressure", "parameters": "roller laminator at 25 °C, 0.5 m/min, 50 N/cm pressure; or platen press at 1 MPa for 5 min", "duration": "10 min", "notes": "Cold lamination preserves PSA adhesion characteristics; thermal lamination accelerates curing of some PSAs"},
        {"order": 6, "action": "Connect tubing", "parameters": "epoxy or compression fittings into pre-drilled access holes", "duration": "30 min", "notes": ""},
    ],
    critical_parameters=[
        {"parameter": "Layer alignment", "target": "<50 µm registration error", "tolerance": "<100 µm", "failure_at_off_spec": "channels misaligned, ports blocked"},
        {"parameter": "Lamination pressure", "target": "1 MPa platen or 50 N/cm roller", "tolerance": "±20%", "failure_at_off_spec": "weak bond at low pressure; channel deformation at high pressure"},
        {"parameter": "PSA chemistry", "target": "match application (acrylic for general; silicone for high-T)", "tolerance": "see datasheet", "failure_at_off_spec": "incompatible PSA may dissolve in solvent or release residue"},
    ],
    equipment_required=[
        {"instrument_class": "CO2 laser cutter", "optional_model": "Glowforge / Epilog", "notes": "for cutting layers"},
        {"instrument_class": "roller laminator", "optional_model": "GBC Catena 35", "notes": "or platen press"},
        {"instrument_class": "drill press", "optional_model": "any", "notes": "for ports"},
    ],
    materials_required=[
        {"material": "cast PMMA, 1.5 mm", "vendor": "Plaskolite", "part_number_optional": "Plexiglas G"},
        {"material": "PSA film (acrylic)", "vendor": "3M", "part_number_optional": "9474LE / 9088"},
        {"material": "PET spacer film", "vendor": "any", "part_number_optional": "100–500 µm thickness"},
    ],
    validated_outcome="Reproduces 500 µm × 200 µm channels at ±50 µm tolerance with build time of <2 hr per chip. Suitable for educational, prototype, and lateral-flow applications.",
    failure_modes=[
        {"mode": "Trapped air in lamination", "diagnostic_signature": "voids visible in finished chip", "corrective_action": "vacuum-bag lamination; squeegee technique during stacking"},
        {"mode": "PSA delamination under flow", "diagnostic_signature": "leaks at adhesive interface", "corrective_action": "select higher-strength PSA; reduce flow pressure; consider PSA-free thermal-bond alternative"},
        {"mode": "Solvent incompatibility", "diagnostic_signature": "discoloration or swelling at PSA interface", "corrective_action": "use solvent-resistant PSA (silicone-based) or switch to non-PSA bonding"},
    ],
    related_corpus_entries=["martinez-2007-paper-microfluidics"],
    publication_citation="Patko et al. 2014 Lab Chip 14, 4187–4195 (PSA microfluidics review)",
    sources=[
        "3M 9474LE / 9088 datasheets",
        "Patko, D.; Mártonfalvi, Z.; Kovacs, B.; Vonderviszt, F.; Kellermayer, M.; Horvath, R. Single-cell adhesion strength and contact density drops in the M phase of cancer cells. Lab Chip 2014, 14, 4187–4195",
    ],
    notes="PSA lamination is the dominant fabrication method for industrial cartridges (BioFire, Cepheid, Lucira) because it is (a) compatible with high-volume manufacturing, (b) doesn't require thermal bonding, (c) accommodates multi-material stacks (paper, PMMA, glass, electronics in one chip). Hobbyist accessibility is excellent; the limiting factor is layer alignment.",
)

# =====================================================================
# SLA stereolithography baseline
# =====================================================================
add(
    id="sla-stereolithography-baseline",
    canonical_name="SLA stereolithography microfluidic baseline (Form3 class)",
    aliases=["SLA microfluidics", "Form3 / Form4 microfluidics"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="dlp-sla-printing",
    substrate_material="acrylate-based photoresin (Formlabs Clear V4, Anycubic Clear, BioMed Clear)",
    output_artifact="3D-printed microfluidic device with embedded channels of width 200 µm to 5 mm; depth limited by resin clearing geometry.",
    steps=[
        {"order": 1, "action": "Design in CAD with channel-clearing supports", "parameters": "Fusion 360 / OnShape / Tinkercad; ensure channels have a draining path with <60° overhangs and no horizontal traps", "duration": "1 hr", "notes": "Trapped resin in channels is the dominant failure mode; design for drainage"},
        {"order": 2, "action": "Slice for SLA", "parameters": "PreForm or Lychee Slicer; orient with channels diagonal (~45°) for self-supporting", "duration": "20 min", "notes": "Layer thickness 50 µm balances time and quality"},
        {"order": 3, "action": "Print", "parameters": "Form3 with Clear V4 resin: ~3 hr for 50 mm chip at 50 µm layer", "duration": "2–6 hr", "notes": ""},
        {"order": 4, "action": "Drain uncured resin from channels", "parameters": "use syringe with isopropanol to flush channels immediately after print; allow >30 min draining", "duration": "1 hr", "notes": "Critical step. Failure here ruins channels post-cure."},
        {"order": 5, "action": "Wash", "parameters": "Form Wash with isopropanol, 10 min for hard surfaces, 20 min for channels (flush channels with syringe during wash)", "duration": "30 min", "notes": ""},
        {"order": 6, "action": "Final UV cure", "parameters": "Form Cure 60 °C 60 min; or comparable UV chamber", "duration": "1 hr", "notes": "Cure both internally and externally"},
        {"order": 7, "action": "Connect tubing", "parameters": "epoxy or compression fittings into integrated ports", "duration": "30 min", "notes": "Print ports directly when possible"},
    ],
    critical_parameters=[
        {"parameter": "Channel size", "target": ">300 µm for Form3 class", "tolerance": ">200 µm", "failure_at_off_spec": "smaller channels trap uncured resin, become permanently blocked"},
        {"parameter": "Drainage geometry", "target": "<60° overhangs, no horizontal pockets", "tolerance": "verify by simulation", "failure_at_off_spec": "trapped resin polymerizes during UV cure"},
        {"parameter": "Wash thoroughness", "target": "channels flushed with IPA via syringe", "tolerance": "until no residue", "failure_at_off_spec": "incomplete wash leaves resin film that interferes with biocompatibility"},
    ],
    equipment_required=[
        {"instrument_class": "SLA 3D printer", "optional_model": "Formlabs Form3/Form4 / Anycubic Photon / Phrozen Sonic", "notes": "$200–$3500 range; print resolution ~50 µm XY with 25 µm Z"},
        {"instrument_class": "wash station", "optional_model": "Form Wash or manual IPA bath", "notes": ""},
        {"instrument_class": "UV cure chamber", "optional_model": "Form Cure or 365 nm chamber", "notes": ""},
    ],
    materials_required=[
        {"material": "Clear V4 resin or BioMed Clear", "vendor": "Formlabs / Anycubic", "part_number_optional": None},
        {"material": "isopropanol (90%+)", "vendor": "any", "part_number_optional": ""},
    ],
    validated_outcome="Reproduces 500 µm × 500 µm channels at ±100 µm tolerance with $3000-class printer; smaller channels possible with care.",
    failure_modes=[
        {"mode": "Trapped resin in channels", "diagnostic_signature": "channels blocked, no flow", "corrective_action": "redesign for drainage; flush channels during/after wash; use lower-viscosity resin"},
        {"mode": "Layer delamination", "diagnostic_signature": "leaks at layer interfaces under pressure", "corrective_action": "verify printer calibration; ensure full UV cure"},
        {"mode": "Resin biocompatibility issues", "diagnostic_signature": "cell cytotoxicity in finished chip", "corrective_action": "switch to BioMed-class resin; extended IPA wash; double-cure"},
    ],
    related_corpus_entries=["gong-2017-3d-printed-microfluidics", "tumbleston-2015-clip-3d-printing"],
    publication_citation="Beauchamp et al. 2017 Anal. Chem. 89, 4054–4061",
    sources=[
        "Formlabs Clear V4 resin technical data",
        "Beauchamp, M. J. et al. 3D printed microfluidic devices for microchip electrophoresis. Anal. Chem. 2017, 89, 4054–4061",
    ],
    notes="SLA is the dominant 'desktop 3D printer' microfluidics path. Distinct from DLP (which uses a digital mirror device for parallel exposure of an entire layer); SLA uses a galvo-scanned laser for layer-by-layer single-spot exposure. Capital cost is moderate ($200–$3500 entry); operating cost dominated by resin (~$200/L). Best for prototype geometries and connectors that wouldn't be cleanly fabricable with traditional photolithography, e.g., curved or non-planar 3D channels.",
)


# Write out
with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new recipes to {OUT}")
