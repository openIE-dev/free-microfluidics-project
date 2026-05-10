#!/usr/bin/env python3
"""Fifth expansion of fabrication recipes: femtosecond laser glass, EWOD cartridge fab."""
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
    id="femtosecond-laser-direct-write-glass",
    canonical_name="Femtosecond laser direct-write 3D microchannels in glass",
    aliases=["fs laser glass", "FLDW glass microfluidics"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="other",
    substrate_material="fused silica or photo-sensitive glass (Foturan)",
    output_artifact="3D internal microchannel network in glass with channel diameter 5 µm to 100 µm at arbitrary 3D paths through the substrate volume.",
    steps=[
        {"order": 1, "action": "Design 3D channel network", "parameters": "CAD model with channels routed in 3D through substrate volume; minimum bend radius >5× channel diameter for clean wet etch", "duration": "1 hr", "notes": "3D-internal channels are the architectural advantage of FLDW vs planar lithography"},
        {"order": 2, "action": "Mount substrate in fs laser system", "parameters": "Foturan or fused silica wafer mounted on XYZ stage; objective lens NA 0.4–0.8 typical", "duration": "20 min", "notes": "Higher NA gives smaller voxel but limits depth of field"},
        {"order": 3, "action": "Femtosecond laser exposure", "parameters": "ti:sapphire laser ~800 nm, 80–120 fs pulses, 100 nJ/pulse, 1 MHz rep rate; scan pattern at ~1 mm/s following CAD path", "duration": "30 min to 8 hr depending on volume", "notes": "Fs laser causes nonlinear absorption only at focal voxel, enabling true 3D modification of bulk glass"},
        {"order": 4, "action": "Optional thermal treatment (Foturan only)", "parameters": "for Foturan: 500–600 °C 1 hr to crystallize laser-modified regions; not required for direct fs ablation in fused silica", "duration": "2 hr", "notes": "Thermal crystallization makes Foturan modified regions 50× more soluble in HF"},
        {"order": 5, "action": "Wet etch", "parameters": "HF or KOH etch dissolves modified regions, leaving open channels: HF for fused silica or post-thermal Foturan; KOH for some photo-glasses", "duration": "1–6 hr", "notes": "Etch selectivity 50–100:1 between modified and unmodified glass"},
        {"order": 6, "action": "Drill access ports", "parameters": "diamond drill or laser-machined surface ports", "duration": "30 min", "notes": "Connect 3D internal network to external tubing"},
        {"order": 7, "action": "Connect tubing", "parameters": "epoxy tubing into ports", "duration": "30 min", "notes": ""},
    ],
    critical_parameters=[
        {"parameter": "Pulse energy", "target": "100 nJ for typical fused silica", "tolerance": "±20%", "failure_at_off_spec": "low: incomplete modification; high: catastrophic damage"},
        {"parameter": "Scan velocity", "target": "1 mm/s", "tolerance": "±25%", "failure_at_off_spec": "fast: discontinuous modification; slow: excessive heating, cracking"},
        {"parameter": "Etch selectivity", "target": "50:1 modified:unmodified", "tolerance": "tool-dependent", "failure_at_off_spec": "low selectivity: channels expand outside intended geometry"},
    ],
    equipment_required=[
        {"instrument_class": "femtosecond laser system", "optional_model": "Light Conversion Pharos / Spectra-Physics Spirit", "notes": "$200k–$500k commercial; rare outside specialized labs"},
        {"instrument_class": "XYZ stage with sub-µm precision", "optional_model": "Aerotech ABL series", "notes": "needed for 3D path control"},
        {"instrument_class": "HF wet etch bench", "optional_model": None, "notes": "see glass-hf-etching-baseline for safety requirements"},
    ],
    materials_required=[
        {"material": "fused silica wafer or Foturan glass", "vendor": "Schott / Heraeus / Schott Lighting", "part_number_optional": "Foturan II or Lithosil"},
        {"material": "buffered HF", "vendor": "any", "part_number_optional": "ACS grade"},
    ],
    validated_outcome="Reproduces 50 µm diameter 3D internal channels with arbitrary path geometry. Limited by tool availability and write time (>1 hr per chip for complex networks).",
    failure_modes=[
        {"mode": "Cracks at high-stress regions", "diagnostic_signature": "linear cracks in finished chip", "corrective_action": "reduce pulse energy; slow scan; allow thermal relaxation between passes"},
        {"mode": "Incomplete etching of modified regions", "diagnostic_signature": "channels partially blocked", "corrective_action": "longer etch; verify thermal treatment (Foturan); higher pulse density"},
        {"mode": "Over-etch widening", "diagnostic_signature": "channels wider than designed", "corrective_action": "reduce etch time; verify fresh HF concentration; characterize selectivity on sacrificial sample"},
    ],
    related_corpus_entries=["spackova-2022-nanofluidic-scattering-microscopy", "harrison-1992-cap-electrophoresis-on-chip"],
    related_fab_recipes=["glass-hf-etching-baseline", "two-photon-polymerization-nanoscribe-baseline"],
    publication_citation="Marcinkevicius et al. 2001 Opt. Lett. 26, 277–279 (FLDW in Foturan)",
    sources=[
        "Marcinkevicius, A.; Juodkazis, S.; Watanabe, M.; Miwa, M.; Matsuo, S.; Misawa, H.; Nishii, J. Femtosecond laser-assisted three-dimensional microfabrication in silica. Opt. Lett. 2001, 26, 277–279",
        "Sugioka, K.; Cheng, Y. Ultrafast lasers — reliable tools for advanced materials processing. Light Sci. Appl. 2014, 3, e149",
    ],
    notes="Femtosecond laser direct write is the only fabrication method capable of true 3D internal channel networks in glass — neither photolithography nor wet etching can produce buried 3D structures. Capital-intensive and slow; rare outside specialized labs. Best for demonstrators, sub-mm-scale 3D-routing chips, and applications requiring chemical resistance + 3D architecture (which precludes PDMS).",
)

add(
    id="ewod-cartridge-fabrication-baseline",
    canonical_name="EWOD digital microfluidics cartridge fabrication",
    aliases=["EWOD cartridge fab", "DMF chip fabrication"],
    contributor="Free Microfluidics Project (community-curated baseline)",
    contributor_country="US",
    recipe_class="electrode-integration",
    substrate_material="ITO-coated glass + dielectric layer + hydrophobic top layer",
    output_artifact="EWOD digital microfluidic chip with 80–256 individually addressable electrodes for droplet manipulation by electrowetting.",
    steps=[
        {"order": 1, "action": "Pattern ITO electrode array", "parameters": "ITO-coated glass slide; spin photoresist; UV expose through electrode-array mask; develop; HCl etch ITO; strip resist; result is patterned ITO electrode array", "duration": "1 hr", "notes": "Electrode pitch typically 700 µm to 2 mm; minimum gap 25 µm between electrodes"},
        {"order": 2, "action": "Deposit dielectric layer", "parameters": "PECVD SiO2 or sputtered Ta2O5 ~500 nm thickness; alternatively spin-coat parylene C ~1 µm via vacuum CVD", "duration": "2 hr", "notes": "Dielectric must withstand operating voltage (~50–300 V) without breakdown; defects cause shorts"},
        {"order": 3, "action": "Deposit hydrophobic top coat", "parameters": "spin-coat fluoropolymer (Cytop, Teflon AF, or similar) at 1–3% in fluoroether solvent; bake 180 °C 1 hr", "duration": "1.5 hr", "notes": "Hydrophobic surface maintains droplet-on-electrode contact angle ~120°"},
        {"order": 4, "action": "Prepare top plate", "parameters": "ITO-coated glass slide with ground electrode + same hydrophobic coating", "duration": "1 hr", "notes": "Top plate is the common-ground electrode for the droplet"},
        {"order": 5, "action": "Assemble chip", "parameters": "place spacers (250 µm to 1 mm thick) between bottom and top plates; clip together; load oil and aqueous droplets between plates", "duration": "30 min", "notes": "Spacer thickness sets chamber height; dictates droplet volume"},
        {"order": 6, "action": "Connect to driver electronics", "parameters": "spring-loaded contact array against bottom-plate ITO electrode pads; ground connection to top-plate ITO", "duration": "30 min", "notes": "see open-ewod-driver-dropbot-derivative for HV driver electronics"},
        {"order": 7, "action": "Test droplet motion", "parameters": "load aqueous droplets; apply test pattern at ~50–150 V; verify droplet motion across electrodes", "duration": "30 min", "notes": "Operating voltage depends on dielectric thickness and chemistry"},
    ],
    critical_parameters=[
        {"parameter": "Dielectric thickness", "target": "500 nm to 2 µm", "tolerance": "±20%", "failure_at_off_spec": "thinner: dielectric breakdown shorts; thicker: requires higher operating voltage"},
        {"parameter": "Hydrophobic coating thickness", "target": "50–200 nm", "tolerance": "±50%", "failure_at_off_spec": "too thin: pinhole defects degrade hydrophobicity; too thick: slows droplet response"},
        {"parameter": "Electrode-pair gap", "target": "25–50 µm", "tolerance": "±10 µm", "failure_at_off_spec": "wide gap: weak field across droplet edge, droplet does not move; narrow gap: shorts between electrodes"},
        {"parameter": "Operating voltage", "target": "50–150 V AC at 1 kHz", "tolerance": "depends on dielectric", "failure_at_off_spec": "low: insufficient electrowetting force; high: dielectric breakdown"},
    ],
    equipment_required=[
        {"instrument_class": "spin coater", "optional_model": None, "notes": "for dielectric and hydrophobic coatings"},
        {"instrument_class": "UV mask aligner", "optional_model": None, "notes": "for ITO patterning"},
        {"instrument_class": "PECVD or sputter system", "optional_model": "Oxford PECVD / AJA sputter", "notes": "for dielectric deposition"},
        {"instrument_class": "parylene CVD coater (alternative dielectric)", "optional_model": "Specialty Coating Systems PDS 2010", "notes": "alternative to PECVD"},
        {"instrument_class": "EWOD HV driver", "optional_model": "DropBot or open-ewod-driver-dropbot-derivative", "notes": "see control sub-repo"},
    ],
    materials_required=[
        {"material": "ITO-coated glass slides", "vendor": "Sigma-Aldrich / Delta Technologies", "part_number_optional": "20 Ω/sq ITO on 1.1 mm glass"},
        {"material": "AZ 4620 photoresist", "vendor": "MicroChemicals", "part_number_optional": None},
        {"material": "Cytop fluoropolymer", "vendor": "AGC Chemicals", "part_number_optional": "CTL-816AP"},
        {"material": "fluoroether solvent (Novec 7100)", "vendor": "3M", "part_number_optional": "Novec 7100"},
        {"material": "spacers (PSA tape or PMMA)", "vendor": "any", "part_number_optional": "250 µm to 1 mm"},
    ],
    validated_outcome="Reproduces 80-electrode EWOD chip with 1.5 mm × 1.5 mm electrode pitch; droplet motion at 70–120 V AC; >100 hr operating lifetime before dielectric degradation.",
    failure_modes=[
        {"mode": "Dielectric breakdown", "diagnostic_signature": "shorts between droplet and electrode; droplet electrolyzes", "corrective_action": "thicker dielectric; lower operating voltage; verify defect-free deposition"},
        {"mode": "Droplet pinning", "diagnostic_signature": "droplet does not move on electrode activation", "corrective_action": "verify hydrophobic coating intact; increase voltage; add surfactant trace to droplet"},
        {"mode": "Bio-fouling", "diagnostic_signature": "droplet performance degrades over time with biological samples", "corrective_action": "use silicone oil filler instead of air; PEG-graft surfaces; consider single-use cartridges"},
    ],
    related_corpus_entries=["pollack-2000-electrowetting-droplet", "cho-2003-creating-transporting-cutting-merging", "advanced-liquid-logic-illumina-dmf", "dropbot-open-source-dmf"],
    related_fab_recipes=[],
    publication_citation="Pollack 2000 Appl. Phys. Lett. 77, 1725 (foundational EWOD)",
    sources=[
        "Pollack, M. G.; Fair, R. B.; Shenderov, A. D. Appl. Phys. Lett. 2000, 77, 1725–1726",
        "Cho, S. K.; Moon, H.; Kim, C.-J. J. Microelectromech. Syst. 2003, 12, 70–80",
        "AGC Cytop datasheet",
    ],
    notes="EWOD cartridge fabrication is the most demanding planar microfluidic fab process: requires patterned electrodes, defect-free dielectric, and uniform hydrophobic coating, all of which must withstand operating voltage. The DropBot project (Wheeler lab) demonstrated complete open-hardware fabrication and driver electronics, providing the canonical reference design for academic EWOD work.",
)


with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new recipes to {OUT}")
