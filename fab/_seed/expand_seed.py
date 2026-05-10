#!/usr/bin/env python3
"""Expansion of fabrication recipes."""
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
# Glass HF etching baseline
# =====================================================================

add(
    id="glass-hf-etching-baseline",
    canonical_name="Baseline glass channel HF etching",
    aliases=["glass HF etch", "borofloat etch baseline"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="glass-photolithography",
    substrate_material="Borofloat 33 borosilicate glass",
    output_artifact="Glass substrate with isotropically etched microchannels of depth 10 µm to 200 µm.",
    steps=[
        {"order": 1, "action": "Clean glass substrate", "parameters": "piranha 4:1 H2SO4:H2O2 for 10 min, DI rinse, N2 dry; alternatively: detergent wash + IPA + N2", "duration": "30 min", "notes": "Critical for adhesion of subsequent metal mask"},
        {"order": 2, "action": "Sputter or evaporate Cr/Au etch mask", "parameters": "10 nm Cr adhesion layer + 100 nm Au; or 200 nm of polysilicon as alternative", "duration": "1 hr", "notes": "Au is the canonical HF mask; polysilicon works for shorter etches and is cleaner"},
        {"order": 3, "action": "Spin coat positive photoresist", "parameters": "AZ 4620 or equivalent at 3000 rpm for 30 s, soft-bake 100 °C 5 min", "duration": "20 min", "notes": "Thicker resist gives better HF resistance"},
        {"order": 4, "action": "UV expose through chrome mask", "parameters": "365 nm i-line, dose per resist datasheet (typ. 600 mJ/cm² for AZ 4620)", "duration": "1–2 min", "notes": "Underexposure is preferable to overexposure for HF mask robustness"},
        {"order": 5, "action": "Develop photoresist", "parameters": "AZ 400K developer 1:4 in DI, 60 s with agitation, DI rinse", "duration": "10 min", "notes": "Inspect under microscope before proceeding"},
        {"order": 6, "action": "Etch Au layer", "parameters": "KI/I2 gold etchant, 30–60 s with agitation, DI rinse", "duration": "5 min", "notes": "Time depends on Au thickness; over-etch is acceptable"},
        {"order": 7, "action": "Etch Cr adhesion layer", "parameters": "Cr etchant (Cyantek CR-7 or similar), 30 s, DI rinse", "duration": "5 min", "notes": "Failure here causes mask undercutting in HF"},
        {"order": 8, "action": "Etch glass with HF", "parameters": "buffered HF (BHF) 6:1 NH4F:HF for slow etch, or 49% HF for fast etch; etch rate ~1.4 µm/min in BHF, ~7 µm/min in 49% HF", "duration": "3–60 min depending on target depth", "notes": "EXTREME HAZARD — HF burns are insidious and can be fatal. Use full-face shield, double-glove with neoprene, work behind splash shield in dedicated HF-rated hood, keep calcium gluconate gel within reach. Train before attempting."},
        {"order": 9, "action": "Stop etch", "parameters": "remove from HF, immediately quench in DI water bath ≥10 L, then transfer to fresh DI rinse, N2 dry", "duration": "10 min", "notes": "Residual HF on substrate continues etching; thorough quench is critical"},
        {"order": 10, "action": "Strip etch mask", "parameters": "Au strip in KI/I2, then Cr strip in CR-7, then resist strip in acetone/IPA", "duration": "30 min", "notes": ""},
    ],
    critical_parameters=[
        {"parameter": "HF concentration", "target": "BHF 6:1 for controllable rate", "tolerance": "as supplied", "failure_at_off_spec": "concentrated HF gives faster but less uniform etch; risk of mask undercutting"},
        {"parameter": "Etch time", "target": "set to target depth using measured rate", "tolerance": "±10%", "failure_at_off_spec": "depth deviates linearly; characterize rate on a sacrificial wafer"},
        {"parameter": "Etch mask integrity", "target": "no pinholes in Cr/Au stack", "tolerance": "<1 pinhole/cm²", "failure_at_off_spec": "pinholes cause spurious channels in random locations"},
        {"parameter": "Quench timing", "target": "<10 s from etch removal to quench", "tolerance": "<30 s", "failure_at_off_spec": "delayed quench produces position-dependent over-etch"},
    ],
    equipment_required=[
        {"instrument_class": "spin coater", "optional_model": None, "notes": "for photoresist"},
        {"instrument_class": "UV mask aligner", "optional_model": None, "notes": "365 nm, contact or proximity"},
        {"instrument_class": "metal deposition system", "optional_model": "sputter coater or e-beam evaporator", "notes": "for Cr/Au mask"},
        {"instrument_class": "HF-rated wet bench", "optional_model": None, "notes": "PVC or polypropylene vessels only; dedicated HF tools"},
        {"instrument_class": "PPE: full face shield, neoprene gloves, lab coat, splash shield", "optional_model": None, "notes": "non-negotiable; calcium gluconate gel must be within arm's reach"},
        {"instrument_class": "profilometer", "optional_model": "Dektak / KLA Tencor", "notes": "for etch-rate characterization"},
    ],
    materials_required=[
        {"material": "Borofloat 33 wafers or slides", "vendor": "Schott / University Wafer", "part_number_optional": "1 mm thickness standard"},
        {"material": "AZ 4620 positive photoresist", "vendor": "MicroChemicals / EMD", "part_number_optional": None},
        {"material": "AZ 400K developer", "vendor": "MicroChemicals", "part_number_optional": None},
        {"material": "Cr/Au sputter targets", "vendor": "Kurt J. Lesker / ACI Alloys", "part_number_optional": None},
        {"material": "buffered HF (6:1)", "vendor": "Honeywell / Sigma", "part_number_optional": "ACS or VLSI grade"},
        {"material": "Au etchant (KI/I2)", "vendor": "Sigma-Aldrich", "part_number_optional": None},
        {"material": "Cr etchant CR-7", "vendor": "Cyantek / Transene", "part_number_optional": None},
        {"material": "calcium gluconate 2.5% gel", "vendor": "first-aid supply", "part_number_optional": None},
    ],
    validated_outcome="Reproduces 50 µm × 100 µm isotropic glass channels at ±5 µm tolerance with 1.4 µm/min BHF etch rate.",
    failure_modes=[
        {"mode": "Mask undercutting", "diagnostic_signature": "channels wider than designed by >2× target depth", "corrective_action": "verify Cr adhesion; consider polysilicon mask for deeper etches"},
        {"mode": "Pinholes in mask", "diagnostic_signature": "random small pits in glass surface", "corrective_action": "improve metal deposition; thicker Au layer; pre-wet substrate before HF"},
        {"mode": "Resist lift-off in HF", "diagnostic_signature": "complete mask failure, full-surface etch", "corrective_action": "thicker resist; longer hard bake; alternative mask material"},
        {"mode": "Operator HF exposure", "diagnostic_signature": "(emergency)", "corrective_action": "apply calcium gluconate gel immediately; transport to ER; HF burns can be life-threatening even when small in area"},
    ],
    related_corpus_entries=["harrison-1992-cap-electrophoresis-on-chip", "spackova-2022-nanofluidic-scattering-microscopy"],
    publication_citation="multiple; canonical reference is Manz/Harrison group's 1990s glass-chip work",
    sources=[
        "MicroChemicals AZ 4620 datasheet",
        "Schott Borofloat 33 datasheet",
        "Madou, M. Fundamentals of Microfabrication, 3rd ed., chapter on wet etching",
    ],
    notes="Glass HF etching is the canonical fabrication path for capillary electrophoresis chips and remains the gold standard for chemically-resistant glass microfluidics. Patent considerations: the recipe itself is unencumbered; specific applications may carry IP.",
)

# =====================================================================
# Glass-glass thermal bonding
# =====================================================================

add(
    id="glass-glass-thermal-bonding-baseline",
    canonical_name="Baseline glass-glass thermal fusion bonding",
    aliases=["fusion bonding", "thermal glass bonding"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="glass-bonding",
    substrate_material="Borofloat 33 borosilicate glass (etched bottom + drilled top)",
    output_artifact="Sealed glass microfluidic chip with through-thickness fluidic ports.",
    steps=[
        {"order": 1, "action": "Drill access ports in top piece", "parameters": "0.7 mm diamond burr at 5000 rpm with water flood; through-holes aligned to channel termini", "duration": "30 min", "notes": "Drill before bonding; chips with bonded ports require expensive laser drilling"},
        {"order": 2, "action": "Clean both glass pieces", "parameters": "RCA-1 (5:1:1 H2O:H2O2:NH4OH) at 70 °C for 10 min, DI rinse, then RCA-2 (5:1:1 H2O:H2O2:HCl) at 70 °C for 10 min, DI rinse, N2 dry; alternatively: piranha + DI", "duration": "1 hr", "notes": "Bond strength is dominated by surface cleanliness; abbreviated cleans give weak bonds"},
        {"order": 3, "action": "Activate surfaces (optional)", "parameters": "O2 plasma 100 W 60 s, or NH4OH:H2O2:H2O 1:1:5 dip 30 s", "duration": "5 min", "notes": "Activation lowers required bond temperature; recommended for thin substrates"},
        {"order": 4, "action": "Pre-bond contact", "parameters": "place pieces channel-side together; press lightly; observe interference fringes (Newton's rings) — bond will follow fringe pattern; gently push fringes outward to expel air", "duration": "10 min", "notes": "Patience here saves bonding-step failures; air-trapped regions will not bond"},
        {"order": 5, "action": "Furnace anneal / bond", "parameters": "ramp to 600–650 °C at 5 °C/min, hold 4 hr, ramp down at 2 °C/min; place 200 g weight on chip stack to maintain contact", "duration": "16 hr (overnight)", "notes": "Borofloat 33 bonds reliably at 620 °C; soda-lime at 580 °C; quartz at 1100 °C"},
        {"order": 6, "action": "Inspect bond quality", "parameters": "view through chip under crossed polarizers; uniform color = uniform bond; rainbow fringes = trapped air; opaque regions = failed bond", "duration": "10 min", "notes": ""},
    ],
    critical_parameters=[
        {"parameter": "Surface cleanliness", "target": "<1 particle >0.5 µm per cm² before contact", "tolerance": "essentially zero", "failure_at_off_spec": "particles produce non-bonded voids that can propagate during anneal"},
        {"parameter": "Bond temperature", "target": "620 °C for Borofloat", "tolerance": "±10 °C", "failure_at_off_spec": "low T: weak bond; high T: glass deformation, channel collapse"},
        {"parameter": "Hold time", "target": "4 hr at peak temp", "tolerance": "≥3 hr", "failure_at_off_spec": "shorter holds give incomplete fusion bonding"},
        {"parameter": "Cooling rate", "target": "2 °C/min from peak", "tolerance": "≤5 °C/min", "failure_at_off_spec": "fast cooling induces thermal stress and chip cracking"},
    ],
    equipment_required=[
        {"instrument_class": "diamond drill press or CNC", "optional_model": None, "notes": "for port drilling"},
        {"instrument_class": "RCA cleaning bench", "optional_model": None, "notes": "or piranha bench as alternative"},
        {"instrument_class": "high-temperature programmable furnace", "optional_model": "Carbolite, MTI, Thermolyne", "notes": "must support ≥700 °C, programmable ramp"},
        {"instrument_class": "weight stack", "optional_model": None, "notes": "200–500 g of high-temp-resistant material (graphite plates, refractory weights)"},
        {"instrument_class": "polarizing inspection setup", "optional_model": None, "notes": "for bond quality QC"},
    ],
    materials_required=[
        {"material": "Borofloat 33 wafers (etched bottom and drilled top)", "vendor": "Schott / University Wafer", "part_number_optional": None},
        {"material": "RCA cleaning chemistries (NH4OH, HCl, H2O2)", "vendor": "any", "part_number_optional": "VLSI grade"},
        {"material": "graphite or quartz spacers", "vendor": "any", "part_number_optional": "for weight distribution"},
    ],
    validated_outcome="Bond strength typically >25 MPa shear (limited by glass strength rather than bond strength) when cleanly executed.",
    failure_modes=[
        {"mode": "Channel collapse", "diagnostic_signature": "channels visible but flow blocked or reduced cross-section", "corrective_action": "lower bond temperature; Borofloat 33 specifically tolerates 620 °C without channel deformation, but high-aspect channels may need 600 °C and longer hold"},
        {"mode": "Trapped air voids", "diagnostic_signature": "rainbow fringes in finished chip", "corrective_action": "improve pre-bond contact technique; cleaner surfaces; vacuum-bonding alternative"},
        {"mode": "Cracking on cooldown", "diagnostic_signature": "linear cracks in cooled chip", "corrective_action": "slower cool-down ramp; verify CTE match between two pieces"},
    ],
    related_corpus_entries=["harrison-1992-cap-electrophoresis-on-chip", "spackova-2022-nanofluidic-scattering-microscopy"],
    related_cad_designs=[],
    publication_citation="multiple; canonical reference is Madou, Fundamentals of Microfabrication, 3rd ed.",
    sources=[
        "Madou, M. Fundamentals of Microfabrication, 3rd ed.",
        "Schott Borofloat 33 datasheet",
        "Iliescu et al. 2008 Sens. Actuators A 143, 154–161",
    ],
    notes="Glass-glass thermal fusion bonding produces the most robust microfluidic seals available — solvent-resistant, biocompatible, optically clear. Limited by furnace access and bonding cycle time (~16 hr per batch). Patent considerations: thermal fusion bonding itself is unpatentable as a process.",
)

# =====================================================================
# Hot embossing thermoplastic
# =====================================================================

add(
    id="thermoplastic-hot-embossing-coc-baseline",
    canonical_name="Baseline hot embossing of cyclic-olefin copolymer",
    aliases=["COC hot embossing baseline"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="thermoplastic-hot-embossing",
    substrate_material="cyclic-olefin copolymer (COC, Topas 5013 or Zeonor 1060R)",
    output_artifact="Embossed COC substrate with replicated microchannels of depth 5 µm to 100 µm.",
    steps=[
        {"order": 1, "action": "Prepare master tool", "parameters": "electroplate Ni shim from SU-8 or silicon master; alternatively use silicon or photoetched stainless steel directly", "duration": "(separate process; 1 day)", "notes": "Tool determines yield; one good Ni shim produces 1000+ chips"},
        {"order": 2, "action": "Pre-treat COC substrate", "parameters": "dehydration bake 100 °C 15 min", "duration": "30 min", "notes": "Removes adsorbed moisture; critical for void-free embossing"},
        {"order": 3, "action": "Heat tool stack to embossing temperature", "parameters": "Topas 5013: 150–170 °C; Zeonor 1060R: 130–150 °C; ramp 5 °C/min", "duration": "30 min", "notes": "Temperature must exceed Tg by 30–50 °C for adequate flow"},
        {"order": 4, "action": "Apply embossing pressure", "parameters": "1–10 MPa for 60–300 s; specific pressure depends on feature aspect ratio", "duration": "5 min", "notes": "Higher aspect ratios need higher pressure and longer hold"},
        {"order": 5, "action": "Cool under pressure", "parameters": "cool to <Tg minus 30 °C while maintaining pressure; typically to 90 °C for Topas at 5 °C/min", "duration": "20 min", "notes": "Pressure release before cooling causes feature relaxation"},
        {"order": 6, "action": "Demold", "parameters": "release pressure; demold by gentle peel or controlled lift-off", "duration": "5 min", "notes": "Sharp ridges or square corners may cause sticking; consider draft angles in tool design"},
        {"order": 7, "action": "Drill access ports", "parameters": "0.7 mm carbide drill bit at 3000 rpm; or laser drill for smaller diameters", "duration": "20 min", "notes": ""},
        {"order": 8, "action": "Bond cover layer", "parameters": "thermal lamination of COC film at 110 °C, 1 MPa, 5 min; or solvent bonding with cyclohexane vapor exposure", "duration": "30 min", "notes": "Bond temperature must not exceed Tg minus 20 °C for the embossed substrate"},
    ],
    critical_parameters=[
        {"parameter": "Embossing temperature", "target": "Tg + 40 °C", "tolerance": "±5 °C", "failure_at_off_spec": "low T: incomplete fill; high T: residue on tool, flash"},
        {"parameter": "Embossing pressure", "target": "5 MPa for AR<2; 10 MPa for AR<5", "tolerance": "±10%", "failure_at_off_spec": "underpressure: incomplete fill"},
        {"parameter": "Hold time", "target": "120 s", "tolerance": "±30 s", "failure_at_off_spec": "shorter holds leave residual stress that relaxes on cooling"},
        {"parameter": "Demolding temperature", "target": "<Tg minus 30 °C", "tolerance": "<Tg minus 20 °C", "failure_at_off_spec": "warm demold causes feature distortion"},
    ],
    equipment_required=[
        {"instrument_class": "hot embossing press or hot plate + manual press", "optional_model": "Jenoptik HEX 03 / Specac platen press", "notes": "must support programmable T+P with cooling capability"},
        {"instrument_class": "vacuum chamber (optional)", "optional_model": None, "notes": "for void-free embossing of complex geometries"},
        {"instrument_class": "laminator or thermal bonder", "optional_model": "GBC laminator or industrial heat press", "notes": "for cover bonding"},
    ],
    materials_required=[
        {"material": "Topas 5013 COC pellets or sheets", "vendor": "TOPAS Advanced Polymers", "part_number_optional": "5013L-10"},
        {"material": "Zeonor 1060R COC", "vendor": "Zeon Specialty Materials", "part_number_optional": "1060R"},
        {"material": "Nickel shim or silicon master", "vendor": "internal fabrication", "part_number_optional": None},
        {"material": "thermal bonding film (COC)", "vendor": "TOPAS / 3M", "part_number_optional": None},
    ],
    validated_outcome="Reproduces 50 µm × 50 µm channels at ±5 µm tolerance and 100+ chip yield per shim with optical-quality surface finish.",
    failure_modes=[
        {"mode": "Incomplete feature fill", "diagnostic_signature": "channels shallow or missing in regions", "corrective_action": "increase T or P; degas substrate longer"},
        {"mode": "Bubble inclusion", "diagnostic_signature": "voids in molded part", "corrective_action": "vacuum embossing, or longer dehydration bake"},
        {"mode": "Demold sticking", "diagnostic_signature": "tool features broken / substrate damaged on demold", "corrective_action": "lower demold temperature; add draft angle to tool; apply release agent"},
        {"mode": "Cover bond failure", "diagnostic_signature": "leaks at cover interface", "corrective_action": "increase bond T (within Tg constraints); plasma activate before bonding"},
    ],
    related_corpus_entries=["biofire-filmarray-multiplex-pcr-cartridge", "cepheid-genexpert-cartridge", "10x-genomics-chromium-controller"],
    publication_citation="canonical references: Becker & Gärtner 2008 Anal. Bioanal. Chem. 390, 89–111",
    sources=[
        "TOPAS 5013L datasheet",
        "Zeonor 1060R datasheet",
        "Becker, H.; Gärtner, C. Polymer microfabrication technologies for microfluidic systems. Anal. Bioanal. Chem. 2008, 390, 89–111",
    ],
    notes="Hot embossing dominates academic-prototype thermoplastic microfluidics because it bridges the gap between PDMS (too low-volume for production) and injection molding (too high-tooling-cost for prototypes). Suitable for runs of 10–10,000 chips per shim.",
)

# =====================================================================
# Xurography (vinyl cutting + lamination)
# =====================================================================

add(
    id="xurography-vinyl-microfluidics-baseline",
    canonical_name="Baseline xurography microfluidics (vinyl cutting + lamination)",
    aliases=["xurography baseline", "vinyl-cut microfluidics"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="xurography",
    substrate_material="self-adhesive vinyl + glass slides or PMMA",
    output_artifact="Sub-$1 microfluidic chip with channels 100 µm to 5 mm wide and depth ~50–250 µm (defined by vinyl thickness).",
    steps=[
        {"order": 1, "action": "Design channel geometry", "parameters": "vector design in Inkscape / Illustrator; minimum feature 200 µm for hobby cutters, 50 µm for high-end (Graphtec)", "duration": "10 min", "notes": "Negative space (channel) is what is removed from vinyl"},
        {"order": 2, "action": "Cut vinyl", "parameters": "Cricut / Silhouette / Graphtec craft cutter, blade depth set per vinyl thickness", "duration": "5 min", "notes": "Multiple passes for cleaner edges in thick vinyl"},
        {"order": 3, "action": "Weed the channels", "parameters": "manually peel away the channel-region vinyl using a weeding tool, leaving only non-channel vinyl", "duration": "15 min", "notes": "Patience required for fine features"},
        {"order": 4, "action": "Transfer-tape vinyl onto substrate", "parameters": "apply transfer tape to vinyl surface, peel from backing, align to glass slide or PMMA, press, peel off transfer tape", "duration": "10 min", "notes": "Glass slide or PMMA must be clean (IPA wipe)"},
        {"order": 5, "action": "Apply cover layer", "parameters": "second vinyl layer, glass slide, or PSA-coated film as cover; press firmly to seal", "duration": "5 min", "notes": "PSA delamination is the main failure mode at higher pressures"},
        {"order": 6, "action": "Connect tubing", "parameters": "epoxy or hot-glue tubing into pre-cut access holes", "duration": "30 min", "notes": "Allow epoxy to cure fully before flow"},
    ],
    critical_parameters=[
        {"parameter": "Vinyl thickness", "target": "100 µm or 250 µm (defines channel depth)", "tolerance": "±10 µm", "failure_at_off_spec": "thickness sets channel depth; tolerance affects flow uniformity"},
        {"parameter": "Cutter blade depth", "target": "set so blade penetrates vinyl but not backing", "tolerance": "fine adjustment", "failure_at_off_spec": "too deep: cuts backing, weeding fails; too shallow: incomplete cuts"},
        {"parameter": "Substrate cleanliness", "target": "particle-free, oil-free", "tolerance": "wipe with IPA", "failure_at_off_spec": "contamination causes adhesion failure and channel leaks"},
    ],
    equipment_required=[
        {"instrument_class": "craft vinyl cutter", "optional_model": "Cricut Maker / Silhouette Cameo / Graphtec CE7000", "notes": "even hobbyist cutters work for >200 µm features; Graphtec needed for 50–100 µm"},
        {"instrument_class": "weeding tools", "optional_model": "any", "notes": "tweezers and pick tools"},
    ],
    materials_required=[
        {"material": "self-adhesive vinyl (100 µm or 250 µm)", "vendor": "Oracal / Avery", "part_number_optional": "Oracal 651 (100 µm)"},
        {"material": "transfer tape", "vendor": "any vinyl supplier", "part_number_optional": None},
        {"material": "glass microscope slides or PMMA sheet", "vendor": "any", "part_number_optional": None},
        {"material": "tubing and 5-min epoxy", "vendor": "any", "part_number_optional": None},
    ],
    validated_outcome="Sub-$1 chips with 200 µm-wide × 100 µm-deep channels suitable for educational demonstrations, lateral flow prototypes, and rapid concept iteration.",
    failure_modes=[
        {"mode": "PSA delamination under flow", "diagnostic_signature": "leaks at vinyl-substrate interface", "corrective_action": "use double-sided tape underlay; reduce flow pressure; switch to rigid bonded substrate"},
        {"mode": "Channel blockage at narrow features", "diagnostic_signature": "no flow at thin channels", "corrective_action": "increase minimum feature size; use higher-end cutter; reduce cutter blade speed"},
    ],
    related_corpus_entries=["martinez-2007-paper-microfluidics"],
    publication_citation="Bartholomeusz, Buser, Andrade 2005 J. MEMS 14, 1364. DOI 10.1109/JMEMS.2005.859087",
    sources=[
        "Bartholomeusz, D. A.; Buser, R. W.; Andrade, J. D. Xurography: rapid prototyping of microstructures using a cutting plotter. J. Microelectromech. Syst. 2005, 14, 1364–1374",
        "Martinez et al. 2007 (paper microfluidics, related architecture)",
    ],
    notes="Xurography is the cheapest microfluidic fabrication path with a tooling cost under $300 for a hobbyist setup. Limited by feature size (~200 µm typical), bond strength under pressure, and chemical compatibility (vinyl is incompatible with many organic solvents). Best for educational, prototype, and lateral-flow applications.",
)

# =====================================================================
# Plasma surface modification
# =====================================================================

add(
    id="oxygen-plasma-pdms-glass-bonding",
    canonical_name="Oxygen plasma activation for PDMS-glass irreversible bonding",
    aliases=["O2 plasma bonding", "PDMS plasma bonding"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="surface-modification",
    substrate_material="PDMS + glass slide",
    output_artifact="Irreversibly bonded PDMS-glass chip with bond strength >300 kPa.",
    steps=[
        {"order": 1, "action": "Clean PDMS chip", "parameters": "tape clean (apply and remove Scotch tape several times), or wash IPA + DI + N2 dry", "duration": "5 min", "notes": "Removes PDMS dust from cutting/punching"},
        {"order": 2, "action": "Clean glass slide", "parameters": "IPA wipe + N2 dry, or RCA-1 if higher cleanliness needed", "duration": "5 min", "notes": ""},
        {"order": 3, "action": "Plasma chamber setup", "parameters": "place PDMS (channel side up) and glass slide in plasma chamber; pump to <100 mTorr; bleed in O2 to 200–500 mTorr", "duration": "5 min", "notes": "Pressure regulation matters for reproducibility"},
        {"order": 4, "action": "Apply plasma", "parameters": "30 W RF, 30 s; or 100 W, 15 s for higher-throughput plasma cleaners", "duration": "1 min", "notes": "Over-plasma causes brittle surface layer; under-plasma gives weak bond"},
        {"order": 5, "action": "Vent and immediate contact", "parameters": "vent chamber; remove parts; place in contact within 60 s", "duration": "1 min", "notes": "Bonding window closes rapidly as activated surface returns to hydrophobic state"},
        {"order": 6, "action": "Optional bond enhancement", "parameters": "bake 80 °C for 30 min after contact", "duration": "30 min", "notes": "Improves bond strength; useful for high-pressure applications"},
    ],
    critical_parameters=[
        {"parameter": "Plasma power × time", "target": "30 W × 30 s = 900 W·s", "tolerance": "±20%", "failure_at_off_spec": "too low: weak bond; too high: brittle surface, crack initiation"},
        {"parameter": "Time between plasma and contact", "target": "<60 s", "tolerance": "<90 s", "failure_at_off_spec": "weak bond, partial delamination under flow"},
        {"parameter": "Surface contact pressure", "target": "gentle hand pressure", "tolerance": "no specific spec", "failure_at_off_spec": "channel collapse if excessive; trapped voids if insufficient"},
    ],
    equipment_required=[
        {"instrument_class": "plasma cleaner", "optional_model": "Harrick PDC-32G / Diener Femto / homemade vacuum + RF", "notes": "tabletop O2 plasma sufficient"},
        {"instrument_class": "O2 supply", "optional_model": "compressed gas cylinder", "notes": "research-grade O2"},
    ],
    materials_required=[
        {"material": "PDMS chip (Sylgard 184 base)", "vendor": "Dow", "part_number_optional": None},
        {"material": "glass slides (1 mm Borofloat or soda-lime)", "vendor": "any", "part_number_optional": None},
    ],
    validated_outcome="Bond strength >300 kPa burst pressure when freshly plasma-bonded; >500 kPa after 80 °C 30 min bake.",
    failure_modes=[
        {"mode": "Hydrophobic recovery before contact", "diagnostic_signature": "weak bond, peelable", "corrective_action": "reduce time between plasma and contact; verify plasma is operating"},
        {"mode": "Channel collapse on contact", "diagnostic_signature": "channels deformed in finished chip", "corrective_action": "reduce contact pressure; verify channel aspect ratio is >0.1"},
        {"mode": "Brittle surface cracking", "diagnostic_signature": "fine cracks in PDMS surface visible under microscope", "corrective_action": "reduce plasma power × time"},
    ],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline"],
    related_corpus_entries=["duffy-1998-pdms-soft-lithography-microfluidics"],
    sources=[
        "Duffy et al. 1998 Anal. Chem. 70, 4974–4984",
        "Bhattacharya et al. 2005 J. Microelectromech. Syst. 14, 590–597",
    ],
    notes="Fastest and most reliable PDMS-glass bonding method when properly executed. Most common failure is operator delay between plasma and contact.",
)

with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new recipes to {OUT}")
