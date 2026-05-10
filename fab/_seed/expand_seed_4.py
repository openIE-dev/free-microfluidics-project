#!/usr/bin/env python3
"""Fourth expansion of fabrication recipes: wax printing, anodic bonding, NOA microfluidics."""
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
    id="paper-microfluidics-wax-printing-baseline",
    canonical_name="Wax-printed paper microfluidics baseline",
    aliases=["wax printing paper microfluidics", "Carrilho wax printing"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="paper-microfluidics-patterning",
    substrate_material="cellulose chromatography paper (Whatman No. 1) or filter paper",
    output_artifact="Paper-based microfluidic device with hydrophobic wax barriers defining capillary channels for sample application, reagent zones, and detection lines.",
    steps=[
        {"order": 1, "action": "Design pattern", "parameters": "Inkscape / Illustrator vector pattern; minimum channel width 1 mm for hobbyist printers, ~500 µm for ColorQube-class wax printers; black/dark color in print = wax-coated regions = hydrophobic barriers", "duration": "20 min", "notes": "White/uncolored regions remain hydrophilic chromatography paper"},
        {"order": 2, "action": "Print wax pattern", "parameters": "Xerox ColorQube 8570/8870 (legacy) or Xerox Phaser 8560/8580; if no wax printer available, alternative: print toner pattern via standard laser printer and reflow", "duration": "5 min", "notes": "Wax printers are increasingly hard to source new; secondary market offers options"},
        {"order": 3, "action": "Reflow wax through paper", "parameters": "hotplate or oven at 120–150 °C for 60–120 s; the wax melts and wicks through paper thickness, creating through-thickness hydrophobic barriers", "duration": "5 min", "notes": "Insufficient reflow leaves channels permeable through paper depth; excessive reflow widens barriers"},
        {"order": 4, "action": "Cool to room temperature", "parameters": "ambient cooling on flat surface", "duration": "5 min", "notes": "Quench cooling can warp paper"},
        {"order": 5, "action": "Test by applying water", "parameters": "drop water at sample-application point; verify capillary flow through hydrophilic channels and confinement at wax barriers", "duration": "2 min", "notes": "Failed barriers leak; rerun reflow if needed"},
        {"order": 6, "action": "Apply reagents", "parameters": "drop colorimetric or fluorometric reagents at designated zones; allow to dry before sealing/use", "duration": "30 min", "notes": "Reagent dry-down preserves shelf life; air-dry or vacuum-dry"},
        {"order": 7, "action": "Optional lamination", "parameters": "thermal lamination with overhead-projector lamination film at 80 °C for handling robustness", "duration": "10 min", "notes": "Improves handling but reduces optical clarity; can be skipped for prototypes"},
    ],
    critical_parameters=[
        {"parameter": "Wax reflow temperature", "target": "120 °C for paraffin-wax printers; 150 °C for higher-melt wax", "tolerance": "±10 °C", "failure_at_off_spec": "low T: incomplete through-paper barrier; high T: channel widening, paper scorching"},
        {"parameter": "Reflow time", "target": "60–120 s", "tolerance": "60–180 s", "failure_at_off_spec": "shorter: incomplete barrier formation"},
        {"parameter": "Pattern resolution", "target": "≥500 µm minimum feature", "tolerance": "≥1 mm for hobbyist setups", "failure_at_off_spec": "finer features lose definition during reflow due to wax wicking"},
    ],
    equipment_required=[
        {"instrument_class": "wax printer", "optional_model": "Xerox ColorQube 8570/8870 (best); Xerox Phaser 8560/8580", "notes": "Discontinued products; secondary market source"},
        {"instrument_class": "hotplate or oven", "optional_model": "any 120–150 °C", "notes": "for reflow"},
        {"instrument_class": "thermal laminator (optional)", "optional_model": "any consumer laminator", "notes": "for protective overlay"},
    ],
    materials_required=[
        {"material": "Whatman No. 1 chromatography paper", "vendor": "Cytiva / Sigma", "part_number_optional": "1001-110 (110 mm circles)"},
        {"material": "wax printer ink", "vendor": "Xerox", "part_number_optional": "ColorStix 8570 / 8870"},
        {"material": "lamination film (optional)", "vendor": "any office supply", "part_number_optional": "75 µm or 125 µm hot-laminate"},
    ],
    validated_outcome="Reproduces 1 mm × 50 mm hydrophilic channels at ±100 µm tolerance, sub-$0.10 cost per device, with capillary-driven sample transport at 1–10 mm/s.",
    failure_modes=[
        {"mode": "Channels leak across barriers", "diagnostic_signature": "color migrates outside intended path", "corrective_action": "longer reflow time; verify barrier widths in design (>500 µm); use thicker paper"},
        {"mode": "Channels do not wet", "diagnostic_signature": "water beads up at sample inlet, no flow", "corrective_action": "verify paper is absorbent (not pre-treated); check for inadvertent wax coverage; add surfactant trace to sample"},
        {"mode": "Reagent zones bleed during storage", "diagnostic_signature": "color spread before use", "corrective_action": "ensure reagent dry-down; consider vacuum drying; reduce reagent volume per zone"},
    ],
    related_corpus_entries=["martinez-2007-paper-microfluidics", "franssila-2010-paper-fluidic-pcl", "orasure-quickflex-cartridge"],
    related_fab_recipes=[],
    publication_citation="Carrilho, Martinez, Whitesides 2009 (canonical reference)",
    sources=[
        "Carrilho, E.; Martinez, A. W.; Whitesides, G. M. Anal. Chem. 2009, 81, 7091–7095",
        "Lu, Y.; Shi, W.; Jiang, L.; Qin, J.; Lin, B. Rapid prototyping of paper-based microfluidics with wax for low-cost, portable bioassay. Electrophoresis 2009, 30, 1497–1500",
    ],
    notes="Wax printing is the dominant fabrication method for academic paper microfluidics. The discontinuation of the Xerox ColorQube line creates a long-term supply problem; alternative methods (toner-based pattern transfer, screen printing of wax, laser-cut hydrophobic stickers, photolithographic SU-8 patterning of paper) have emerged but none has matched wax printing's combination of speed, resolution, and cost. A research-grade migration path is needed before wax printers fully exit the market.",
)

add(
    id="silicon-glass-anodic-bonding-baseline",
    canonical_name="Silicon-glass anodic bonding baseline",
    aliases=["anodic bonding", "silicon-Pyrex bonding"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="glass-bonding",
    substrate_material="silicon (etched bottom with sealed channels) + Borofloat 33 glass cap (drilled access ports)",
    output_artifact="Silicon-glass bonded microfluidic chip with chemically-resistant sealed channels and through-glass fluidic ports.",
    steps=[
        {"order": 1, "action": "Drill access ports in glass cap", "parameters": "0.7 mm or 1.0 mm diamond drill at 5000 rpm with water flood; through-holes aligned to silicon channel termini", "duration": "30 min", "notes": "Drill before bonding; bonded glass is much harder to drill cleanly"},
        {"order": 2, "action": "RCA clean both substrates", "parameters": "RCA-1 (5:1:1 H2O:H2O2:NH4OH 70 °C 10 min) + DI rinse + RCA-2 (5:1:1 H2O:H2O2:HCl 70 °C 10 min) + DI rinse + N2 dry", "duration": "1 hr", "notes": "Surface cleanliness dominates bond yield"},
        {"order": 3, "action": "Pre-bond contact", "parameters": "place glass on top of silicon, channel side facing glass; press lightly; observe Newton's-ring-like fringes", "duration": "10 min", "notes": "Pre-bond is tighter than thermal-fusion case because oxide-glass affinity is high"},
        {"order": 4, "action": "Mount in anodic bonder", "parameters": "place stack on heated chuck; top electrode pressed against glass top surface; bottom electrode contacting silicon", "duration": "10 min", "notes": "Suss SB6 / Karl Suss / EVG anodic bonder typical"},
        {"order": 5, "action": "Heat and apply voltage", "parameters": "ramp to 400 °C at 5 °C/min; apply +1000 V on silicon side (glass at ground); hold 10–30 min until current drops to <1% of peak (indicating bond completion)", "duration": "1 hr", "notes": "Voltage is unipolar — silicon positive, glass negative; reversed polarity will not bond"},
        {"order": 6, "action": "Cool under voltage", "parameters": "ramp down to <100 °C at 2 °C/min while maintaining voltage; then remove voltage", "duration": "30 min", "notes": "Cooling under voltage prevents bond reversal at oxide interface"},
        {"order": 7, "action": "Inspect bond quality", "parameters": "view through glass under crossed polarizers; uniform color = uniform bond; rainbow fringes = trapped air", "duration": "10 min", "notes": ""},
    ],
    critical_parameters=[
        {"parameter": "Bond temperature", "target": "400 °C for Borofloat 33 / silicon", "tolerance": "±20 °C", "failure_at_off_spec": "below 350 °C: insufficient ion mobility for bond; above 450 °C: glass flow / channel deformation"},
        {"parameter": "Bond voltage", "target": "+1000 V", "tolerance": "±200 V", "failure_at_off_spec": "lower V: incomplete bond; higher V: dielectric breakdown of glass"},
        {"parameter": "Surface cleanliness", "target": "particle-free", "tolerance": "very strict", "failure_at_off_spec": "particles produce non-bonded voids that propagate"},
        {"parameter": "CTE match", "target": "Borofloat 33 with silicon (CTE-matched)", "tolerance": "±0.5 ppm/°C", "failure_at_off_spec": "CTE mismatch causes thermal stress and chip cracking on cooling"},
    ],
    equipment_required=[
        {"instrument_class": "anodic bonder", "optional_model": "Suss SB6/SB8 / EVG 510 / Karl Suss SB6e", "notes": "$50k–$300k commercial; community DIY versions exist for specific geometries"},
        {"instrument_class": "diamond drill press", "optional_model": "any", "notes": "for glass port drilling"},
        {"instrument_class": "RCA cleaning bench", "optional_model": None, "notes": ""},
        {"instrument_class": "polarizing inspection setup", "optional_model": "any cross-polarizer", "notes": ""},
    ],
    materials_required=[
        {"material": "silicon wafer (etched)", "vendor": "any (substrate-agnostic; see DRIE recipe)", "part_number_optional": None},
        {"material": "Borofloat 33 glass cap (drilled)", "vendor": "Schott", "part_number_optional": None},
        {"material": "RCA cleaning chemistries", "vendor": "any", "part_number_optional": "VLSI grade"},
    ],
    validated_outcome="Bond strength typically >25 MPa shear (limited by glass strength) when cleanly executed; the canonical seal for chemically-resistant silicon-microfluidic devices.",
    failure_modes=[
        {"mode": "Trapped air voids", "diagnostic_signature": "rainbow fringes in finished chip", "corrective_action": "improve pre-bond contact; cleaner surfaces; vacuum-bonding tool"},
        {"mode": "Cracking on cooldown", "diagnostic_signature": "linear cracks in cooled chip", "corrective_action": "slower cool-down; verify CTE match between silicon and glass (Borofloat 33 specifically chosen for this)"},
        {"mode": "Bond does not initiate", "diagnostic_signature": "current does not flow when voltage applied", "corrective_action": "verify voltage polarity (silicon must be positive); verify backside electrical contact; ensure surfaces are clean and in contact"},
    ],
    related_corpus_entries=["terry-1979-stanford-gas-chromatograph", "huang-2004-dld-deterministic-lateral-displacement", "acousort-acoustofluidic-platform"],
    related_fab_recipes=["silicon-drie-bosch-baseline", "glass-hf-etching-baseline"],
    publication_citation="Wallis & Pomerantz 1969 (anodic bonding original disclosure)",
    sources=[
        "Wallis, G.; Pomerantz, D. I. Field assisted glass-metal sealing. J. Appl. Phys. 1969, 40, 3946–3949",
        "Madou, M. Fundamentals of Microfabrication, 3rd ed., chapter on bonding",
    ],
    notes="Anodic bonding is the canonical seal for silicon-microfluidic devices when chemical resistance and high-pressure operation are required. The CTE match between silicon and Borofloat 33 (~3.3 ppm/°C) is what makes the chip survive thermal cycling without cracking; substrate selection is non-negotiable.",
)

add(
    id="noa-soft-lithography-baseline",
    canonical_name="Norland Optical Adhesive (NOA-81) microfluidic chip baseline",
    aliases=["NOA-81 microfluidics", "NOA microfluidic stickers"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="pdms-soft-lithography",
    substrate_material="NOA-81 (Norland Optical Adhesive 81) UV-curable thiol-ene polymer + glass slide cover",
    output_artifact="Rigid thiol-ene microfluidic chip with channel features 5 µm to 200 µm, organic-solvent-resistant, no small-molecule absorption (PDMS alternative).",
    steps=[
        {"order": 1, "action": "Prepare PDMS master", "parameters": "cast 10:1 PDMS against SU-8 master per pdms-su8-soft-lithography-baseline; cure 60 min @ 65 °C", "duration": "1.5 hr", "notes": "PDMS is the working master here; SU-8 is the original photolithographic master"},
        {"order": 2, "action": "Drop NOA-81 onto glass slide", "parameters": "dispense 0.5–1 mL NOA-81 onto cleaned glass slide", "duration": "5 min", "notes": "NOA-81 is a single-component thiol-ene UV-curable adhesive"},
        {"order": 3, "action": "Press PDMS master onto NOA-81", "parameters": "lower PDMS master features-down onto NOA-81 droplet; press to spread NOA-81 evenly to ~100 µm thickness; expel air bubbles", "duration": "10 min", "notes": "Optional spacer (e.g., adhesive tape strips) sets uniform NOA thickness"},
        {"order": 4, "action": "UV cure", "parameters": "365 nm UV at 4 mW/cm² for 30 s through glass slide (curing through glass; PDMS is UV-transparent)", "duration": "5 min", "notes": "Short cure preserves PDMS mold; longer post-cure improves bond and rigidity"},
        {"order": 5, "action": "Peel off PDMS master", "parameters": "carefully separate PDMS from cured NOA-81 chip", "duration": "5 min", "notes": "NOA features should remain on glass slide as the channel layer"},
        {"order": 6, "action": "Apply cover", "parameters": "drop additional NOA-81 onto pre-drilled glass top-cap; press onto NOA channel layer; UV cure 30 s through glass", "duration": "15 min", "notes": "NOA-NOA bonding produces a rigid sealed chip"},
        {"order": 7, "action": "Final post-cure", "parameters": "365 nm UV 5 min total dose", "duration": "5 min", "notes": "Improves chemical resistance and removes residual reactivity"},
        {"order": 8, "action": "Connect tubing", "parameters": "epoxy or compression fittings into glass top ports", "duration": "30 min", "notes": ""},
    ],
    critical_parameters=[
        {"parameter": "NOA-81 thickness", "target": "~100 µm (matched to channel feature height)", "tolerance": "±20 µm", "failure_at_off_spec": "too thin: fragile chip; too thick: features not fully replicated"},
        {"parameter": "UV dose", "target": "120 mJ/cm² (4 mW/cm² × 30 s)", "tolerance": "±30%", "failure_at_off_spec": "low dose: incomplete cure, sticky surfaces; high dose: brittle, yellowing"},
        {"parameter": "PDMS master release", "target": "clean separation", "tolerance": "no broken features", "failure_at_off_spec": "stuck features indicate insufficient cure or poor master quality"},
    ],
    equipment_required=[
        {"instrument_class": "UV lamp", "optional_model": "365 nm, 4–10 mW/cm² flood source", "notes": ""},
        {"instrument_class": "PDMS soft-lithography setup", "optional_model": "see pdms-su8-soft-lithography-baseline", "notes": "for master casting"},
    ],
    materials_required=[
        {"material": "Norland Optical Adhesive 81 (NOA-81)", "vendor": "Norland Products", "part_number_optional": "NOA-81"},
        {"material": "PDMS Sylgard 184", "vendor": "Dow", "part_number_optional": None},
        {"material": "glass microscope slides", "vendor": "any", "part_number_optional": None},
        {"material": "SU-8 master (see SU-8 master baseline)", "vendor": "internal", "part_number_optional": None},
    ],
    validated_outcome="Reproduces 50 µm × 50 µm channels at ±5 µm tolerance with no measurable small-molecule absorption (vs PDMS where small-molecule loss is the dominant chip artifact); chemical compatibility extends to most organic solvents that destroy PDMS.",
    failure_modes=[
        {"mode": "Sticky surfaces after cure", "diagnostic_signature": "channel surface tacky to touch", "corrective_action": "extend UV cure time; verify lamp output (4–10 mW/cm² target)"},
        {"mode": "Master sticks to NOA", "diagnostic_signature": "PDMS master is destroyed during demold", "corrective_action": "verify NOA does not penetrate into PDMS pores (degas PDMS thoroughly); silane-treat PDMS as anti-stick layer"},
        {"mode": "Yellowing over time", "diagnostic_signature": "chip turns yellow under storage", "corrective_action": "store in dark / nitrogen environment; reduce UV exposure dose"},
    ],
    related_corpus_entries=["bartolo-2008-noa-microfluidics", "carlborg-2011-oste-microfluidics", "duffy-1998-pdms-soft-lithography-microfluidics"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "su8-master-baseline"],
    publication_citation="Bartolo et al. 2008 Lab Chip 8, 274 (NOA microfluidic stickers)",
    sources=[
        "Bartolo, D. et al. Microfluidic stickers. Lab Chip 2008, 8, 274–279",
        "Norland Products NOA-81 datasheet",
    ],
    notes="NOA-81 chip fabrication addresses PDMS's two main limitations: small-molecule absorption (PDMS absorbs hydrophobic molecules into the bulk material) and organic-solvent incompatibility. The trade-off is reduced gas permeability (which is sometimes a feature, sometimes a liability for cell culture) and rigidity (which precludes Quake-valve-style elastomeric features). For analytical chemistry on chip and most organic-solvent applications, NOA is the better choice; for cell culture and Quake valves, PDMS remains preferable.",
)


with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new recipes to {OUT}")
