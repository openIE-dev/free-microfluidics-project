#!/usr/bin/env python3
"""Fifth expansion of CAD designs."""
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
    id="gut-on-chip-dual-channel-reference",
    canonical_name="Gut-on-chip dual-channel reference (Kim 2012 architecture)",
    aliases=["gut-on-chip reference"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_path="Two SU-8 masters; PDMS-PDMS bond with O2 plasma; PDMS porous membrane (10 µm pore) sandwiched between layers; vacuum side-channels for cyclic peristalsis-mimicking strain at 0.15 Hz",
    channel_geometry="Two parallel 1 mm × 150 µm channels separated by porous PDMS membrane. Top channel: gut epithelial side (Caco-2 + microbiome). Bottom channel: vascular side. Side vacuum channels apply 10% cyclic strain at 0.15 Hz to mimic intestinal peristalsis.",
    chip_footprint_mm=75,
    cad_files=[
        "designs/gut-on-chip-dual-channel-reference/top_channel.dxf",
        "designs/gut-on-chip-dual-channel-reference/bottom_channel.dxf",
        "designs/gut-on-chip-dual-channel-reference/membrane_outline.dxf",
        "designs/gut-on-chip-dual-channel-reference/design.gds",
    ],
    cad_format="mixed",
    mask_count=2,
    related_corpus_entries=["kim-ingber-2012-gut-on-chip", "huh-2010-lung-on-chip", "ingber-emulate-organ-chip"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "su8-master-baseline", "oxygen-plasma-pdms-glass-bonding"],
    sources=["Kim et al. 2012 Lab Chip 12, 2165–2174"],
    publication_citation="Kim et al. 2012",
    validated_performance=None,
    notes="Stub entry. Direct architectural cousin of lung-on-chip but with peristalsis-mimicking strain frequency (0.15 Hz vs 0.5 Hz for lung breathing). Critical for studying gut-microbiome interactions and intestinal pharmacology.",
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-organ-on-chip-vasculature",
        "fabrication-pdms-soft-lithography",
        "fabrication-multilayer-lamination",
    ],
)

add(
    id="bbb-on-chip-teer-reference",
    canonical_name="Blood-brain barrier-on-chip with TEER electrodes (Booth 2012 architecture)",
    aliases=["BBB-on-chip reference"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_path="Two SU-8 masters; PDMS-PDMS bond; polycarbonate track-etched membrane (0.4 µm pore) between layers; integrated TEER electrodes (gold or Ag/AgCl) on top and bottom channels for trans-endothelial resistance measurement",
    channel_geometry="Two parallel 0.5 mm × 200 µm channels separated by polycarbonate track-etched membrane (0.4 µm pore). Top channel: blood/luminal side (brain endothelial cells). Bottom channel: brain/abluminal side (astrocytes). 4 TEER electrodes (2 per channel) at 5 mm spacing for impedance measurement.",
    chip_footprint_mm=75,
    cad_files=[
        "designs/bbb-on-chip-teer-reference/top_channel.dxf",
        "designs/bbb-on-chip-teer-reference/bottom_channel.dxf",
        "designs/bbb-on-chip-teer-reference/electrode_layer.dxf",
        "designs/bbb-on-chip-teer-reference/design.gds",
    ],
    cad_format="mixed",
    mask_count=3,
    related_corpus_entries=["booth-kim-2012-bbb-on-chip", "huh-2010-lung-on-chip"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "su8-master-baseline", "oxygen-plasma-pdms-glass-bonding"],
    sources=["Booth & Kim 2012 Lab Chip 12, 1784–1792"],
    publication_citation="Booth & Kim 2012",
    validated_performance=None,
    notes="Stub entry. The BBB variant of organ-on-chip adds integrated TEER electrodes for non-destructive measurement of barrier integrity — critical for drug-permeability screening. The 0.4 µm pore membrane (vs 10 µm for lung/gut) reflects the much tighter native BBB.",
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-organ-on-chip-vasculature",
        "detection-electrochemical-on-chip",
        "fabrication-pdms-soft-lithography",
        "fabrication-multilayer-lamination",
    ],
)

add(
    id="ewod-electrode-array-reference-80",
    canonical_name="EWOD electrode array reference (80-electrode, 1.5 mm pitch)",
    aliases=["EWOD reference 80", "DropBot-style chip"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="digital-microfluidics",
    substrate_material="glass",
    fabrication_path="ITO-coated glass slide; lithographic ITO patterning; PECVD SiO2 dielectric (500 nm); spin-coat Cytop hydrophobic top layer; assembled with ITO-coated glass top plate via 250 µm spacers",
    channel_geometry="80 individually addressable square electrodes at 1.5 mm × 1.5 mm pitch arranged in 8 × 10 array; reservoir electrodes (3 mm × 3 mm) at four corners; gap between electrodes 50 µm; total active area 12 mm × 15 mm. Top plate is unpatterned ITO common ground.",
    chip_footprint_mm=75,
    cad_files=[
        "designs/ewod-electrode-array-reference-80/electrode_layer.dxf",
        "designs/ewod-electrode-array-reference-80/contact_pads.dxf",
        "designs/ewod-electrode-array-reference-80/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["pollack-2000-electrowetting-droplet", "cho-2003-creating-transporting-cutting-merging", "dropbot-open-source-dmf", "advanced-liquid-logic-illumina-dmf"],
    related_fab_recipes=["ewod-cartridge-fabrication-baseline"],
    sources=["Pollack 2000 Appl. Phys. Lett. 77, 1725 (foundational EWOD); Wheeler/DropBot reference chip designs"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. The canonical 80-electrode EWOD chip layout: enough electrodes for nontrivial droplet routing while remaining compatible with standard FPC connectors and the open-ewod-driver-dropbot-derivative driver electronics. Larger 256- and 1024-electrode variants exist but require custom interconnect layouts.",
    disclosed_subsystems=[
        "dmf-electrowetting-on-dielectric",
        "dmf-addressable-electrode-array",
    ],
)

add(
    id="coulter-counter-constriction-chip",
    canonical_name="Coulter counter constriction chip (impedance cell counting)",
    aliases=["impedance counter chip"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="separator-component",
    substrate_material="PDMS",
    fabrication_path="SU-8 master, 30 µm; PDMS 10:1 cured 60 min @ 65 °C; plasma bond to glass slide with patterned platinum electrodes; alternative: thermoplastic substrate with embedded electrodes for production",
    channel_geometry="Funnel-shaped flow channel narrowing to 30 µm × 30 µm × 100 µm constriction with two flanking platinum electrodes spanning the constriction; entrance channel widens to 200 µm; exit channel widens to 500 µm for downstream collection. Cells passing through constriction modulate impedance between electrodes.",
    chip_footprint_mm=25,
    cad_files=[
        "designs/coulter-counter-constriction-chip/channel_layer.dxf",
        "designs/coulter-counter-constriction-chip/electrode_layer.dxf",
        "designs/coulter-counter-constriction-chip/design.gds",
    ],
    cad_format="mixed",
    mask_count=2,
    related_corpus_entries=["sysmex-cbc-cartridge", "biorad-nanocoulter-bead-counter"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "su8-master-baseline", "oxygen-plasma-pdms-glass-bonding"],
    sources=["Coulter US2656508 (1953); Sun & Morgan 2010 (impedance cytometry review)"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. The microfluidic implementation of the classical Coulter counter principle: a constriction sized to allow only one cell at a time generates per-cell impedance pulses. Pairs with the open-coulter-counter electronics design. Useful for blood cell counting, particle size distribution, and as front-end to many cell-sorting workflows.",
    disclosed_subsystems=[
        "detection-electrochemical-on-chip",
        "fabrication-pdms-soft-lithography",
    ],
)


# Stub directories
for e in ENTRIES:
    d = Path(__file__).parent / "designs" / e["id"]
    d.mkdir(parents=True, exist_ok=True)
    for fname in e["cad_files"]:
        (Path(__file__).parent / fname).touch()

with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new designs to {OUT}")
