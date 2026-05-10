#!/usr/bin/env python3
"""Expansion of CAD designs."""
import json
from pathlib import Path

OUT = Path(__file__).parent / "designs.jsonl"
ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("last_updated", "2026-05-09")
    kw.setdefault("license", "CC0-1.0")
    kw.setdefault("draft", True)
    ENTRIES.append(kw)


add(
    id="pdms-t-junction-droplet-100um",
    canonical_name="100 µm T-junction droplet generator (reference design)",
    aliases=["T-junction reference"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="droplet-generator",
    substrate_material="PDMS",
    fabrication_path="SU-8 2050 master, 100 µm; PDMS 10:1 cured 60 min @ 65 °C; plasma bond to glass slide",
    channel_geometry="100 µm × 100 µm continuous-phase channel intersected at 90° by 50 µm dispersed-phase channel; collection serpentine",
    chip_footprint_mm=75,
    cad_files=[
        "designs/pdms-t-junction-droplet-100um/design.dxf",
        "designs/pdms-t-junction-droplet-100um/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["thorsen-2002-droplet-microfluidics-flow-focusing"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline"],
    sources=["Thorsen et al. 2001 PRL 86, 4163–4166 (T-junction reference)"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. The canonical T-junction architecture; complementary to the flow-focusing entry.",
    disclosed_subsystems=[
        "droplet-t-junction-generation",
        "fabrication-pdms-soft-lithography",
        "fabrication-su8-photoresist",
    ],
)

add(
    id="pdms-christmas-tree-gradient-generator",
    canonical_name="Christmas-tree concentration gradient generator",
    aliases=["Christmas tree gradient"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="mixer-component",
    substrate_material="PDMS",
    fabrication_path="SU-8 2050 master, 50 µm; PDMS 10:1 cured 60 min @ 65 °C; plasma bond to glass slide",
    channel_geometry="2-input branched mixer cascade producing 8 parallel output channels with linear concentration gradient; 200 µm × 50 µm channels with serpentine mixing sections at each junction",
    chip_footprint_mm=75,
    cad_files=[
        "designs/pdms-christmas-tree-gradient-generator/design.dxf",
        "designs/pdms-christmas-tree-gradient-generator/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["dertinger-2001-christmas-tree-gradient"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline"],
    sources=["Dertinger et al. 2001 Anal. Chem. 73, 1240–1246"],
    publication_citation="Dertinger et al. 2001",
    validated_performance=None,
    notes="Stub entry. The standard chemotaxis-assay gradient generator. 8-output canonical version; 16- and 32-output variants are common forks.",
    disclosed_subsystems=[
        "mixer-passive-split-recombine",
        "fabrication-pdms-soft-lithography",
    ],
)

add(
    id="glass-capillary-electrophoresis-cross-injector",
    canonical_name="Glass CE chip with cross-injector (Harrison reference)",
    aliases=["CE-on-chip reference"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_path="HF-etched Borofloat 33 bottom (50 µm × 50 µm channels) + drilled Borofloat top; thermal fusion bond at 620 °C",
    channel_geometry="cross-injector geometry with 60 mm separation channel and 5 mm short-arm injection cross; 4 reservoir wells",
    chip_footprint_mm=75,
    cad_files=[
        "designs/glass-capillary-electrophoresis-cross-injector/design.dxf",
        "designs/glass-capillary-electrophoresis-cross-injector/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["harrison-1992-cap-electrophoresis-on-chip"],
    related_fab_recipes=["glass-hf-etching-baseline", "glass-glass-thermal-bonding-baseline"],
    sources=["Harrison et al. 1992 Anal. Chem. 64, 1926–1932"],
    publication_citation="Harrison et al. 1992",
    validated_performance=None,
    notes="Stub entry. The canonical CE-on-chip geometry that established the field. Glass substrate gives chemical resistance and high-voltage stability that PDMS cannot match.",
    disclosed_subsystems=[
        "fabrication-glass-hf-etching",
        "fabrication-glass-thermal-bonding",
        "separation-capillary-electrophoresis",
        "material-borofloat-glass",
    ],
)

# Create stub directories
for e in ENTRIES:
    d = Path(__file__).parent / "designs" / e["id"]
    d.mkdir(parents=True, exist_ok=True)
    for fname in ["design.dxf", "design.gds"]:
        (d / fname).touch()

with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new designs to {OUT}")
