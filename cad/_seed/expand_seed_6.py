#!/usr/bin/env python3
"""Sixth expansion of CAD designs."""
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
    id="paper-microfluidic-colorimetric-multiplex",
    canonical_name="Paper-microfluidic multiplex colorimetric assay reference",
    aliases=["paper µPAD multiplex"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_path="Whatman No. 1 chromatography paper; wax-printed barriers (Xerox ColorQube or equivalent); 130 °C 60 s reflow; reagent zones loaded via micropipette dispensing; air-dry 30 min; optional thermal lamination",
    channel_geometry="Central sample-application zone (8 mm circle) connecting via 2 mm-wide channels to 6 peripheral 5 mm reagent zones in radial pattern. Each peripheral zone pre-loaded with a different colorimetric reagent for simultaneous multiplex assay (e.g. glucose, protein, ketone, leukocyte esterase, nitrite, pH).",
    chip_footprint_mm=50,
    cad_files=[
        "designs/paper-microfluidic-colorimetric-multiplex/wax_pattern.dxf",
        "designs/paper-microfluidic-colorimetric-multiplex/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["martinez-2007-paper-microfluidics", "franssila-2010-paper-fluidic-pcl", "psaltis-2014-color-changing-paper-microfluidic"],
    related_fab_recipes=["paper-microfluidics-wax-printing-baseline"],
    sources=["Martinez et al. 2007 Angew. Chem. (foundational µPAD); Carrilho et al. 2009 (wax printing)"],
    publication_citation="Martinez et al. 2007",
    validated_performance=None,
    notes="Stub entry. The canonical multiplex colorimetric paper-microfluidic device — radial layout with central sample input feeding peripheral reagent zones via wax-defined channels. Sub-$0.10 manufacturing cost makes this format viable for low-resource and disposable diagnostic applications.",
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
        "material-paper-cellulose",
    ],
)

add(
    id="isothermal-lamp-cartridge-reference",
    canonical_name="Isothermal LAMP cartridge reference (Lucira-style architecture)",
    aliases=["isothermal NAAT cartridge"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_path="Injection-molded PMMA or COC body with PSA-laminated cover; integrated lyophilized reagent reservoir, sample chamber, amplification chamber, and colorimetric readout window; PSA pinch-valves between chambers",
    channel_geometry="Sample-application port (200 µL) → mixing chamber with lyophilized lysis buffer → swab-fluid metering chamber → LAMP amplification chamber (50 µL × 1 mm × 5 mm) at 65 °C with embedded resistive heater → colorimetric readout window with pH-sensitive dye. Total cartridge footprint 75 mm × 25 mm × 8 mm.",
    chip_footprint_mm=75,
    cad_files=[
        "designs/isothermal-lamp-cartridge-reference/cartridge_body.dxf",
        "designs/isothermal-lamp-cartridge-reference/heater_layer.dxf",
        "designs/isothermal-lamp-cartridge-reference/design.gds",
    ],
    cad_format="mixed",
    mask_count=2,
    related_corpus_entries=["notomi-2000-loop-mediated-isothermal", "lucira-home-covid-test", "cue-health-cartridge", "visby-medical-cartridge"],
    related_fab_recipes=["thermoplastic-hot-embossing-coc-baseline", "psa-lamination-microfluidics-baseline"],
    sources=["Notomi 2000 (LAMP); FDA EUA for Lucira COVID-19 Test"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. The canonical Lucira-class isothermal NAAT cartridge architecture — single-use, battery-powered, instrument-free POC molecular diagnostic. Architectural sibling to the Cue Health cartridge (which uses electrochemical readout) and Visby Medical cartridge (which uses true PCR). The single-temperature operation (65 °C for LAMP) greatly simplifies the heater design vs PCR cartridges.",
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-isothermal-amplification",
        "fabrication-thermoplastic-injection-molding",
        "fabrication-multilayer-lamination",
    ],
)

add(
    id="smartphone-imaging-chip-flow-cell",
    canonical_name="Smartphone-imaging chip flow cell (Ozcan-style holographic)",
    aliases=["smartphone chip imaging reference"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_path="Injection-molded PMMA disc (50 mm × 25 mm × 1 mm); 200 µm thick imaging chamber; LED-illumination from above, smartphone-camera imaging from below through transparent bottom; fittings for 1/16 inch tubing inlet and outlet",
    channel_geometry="Single 200 µm × 5 mm × 25 mm imaging chamber with sample inlet at one end and outlet at other; transparent top window for LED illumination; transparent bottom for smartphone camera capture. Designed for lensless holographic microscopy via Ozcan-style smartphone microscope adapter.",
    chip_footprint_mm=50,
    cad_files=[
        "designs/smartphone-imaging-chip-flow-cell/cartridge_body.dxf",
        "designs/smartphone-imaging-chip-flow-cell/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["ozcan-2010-smartphone-microscopy", "kanakasabapathy-shafiee-2017-cellphone-fertility", "contreras-naranjo-2017-smartphone-microfluidic-review"],
    related_fab_recipes=["co2-laser-ablation-pmma-baseline", "psa-lamination-microfluidics-baseline"],
    sources=["Ozcan group / UCLA smartphone microscopy publications"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. The canonical smartphone-imaging chip architecture — single chamber sized for direct smartphone-camera holographic imaging. Compatible with the open-smartphone-microscope-adapter instrument (separate control entry). Suitable for cell-counting, motility analysis (e.g. semen analysis), and parasitology applications.",
    disclosed_subsystems=[
        "fabrication-thermoplastic-injection-molding",
        "detection-fluorescence-on-chip",
    ],
)

add(
    id="protein-crystallization-screen-chip",
    canonical_name="Protein crystallization nanoliter screening chip (Hansen-Quake architecture)",
    aliases=["protein crystallography chip"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="lab-on-chip",
    substrate_material="PDMS",
    fabrication_path="Two SU-8 masters: control layer (rounded SPR-220 25 µm) and flow layer (SU-8 50 µm); push-up Quake valves; 144 nanoliter chambers in parallel with free-interface diffusion architecture",
    channel_geometry="144 paired chambers per chip, each pair containing protein solution (5 nL) and crystallization condition (15 nL) separated by Quake valve; opening valve allows free-interface diffusion to drive supersaturation. Chip footprint 75 mm × 25 mm.",
    chip_footprint_mm=75,
    cad_files=[
        "designs/protein-crystallization-screen-chip/control_layer.dxf",
        "designs/protein-crystallization-screen-chip/flow_layer.dxf",
        "designs/protein-crystallization-screen-chip/design.gds",
    ],
    cad_format="mixed",
    mask_count=2,
    related_corpus_entries=["quake-2003-microfluidic-protein-crystallization", "unger-2000-quake-monolithic-membrane-valve", "thorsen-2002-microfluidic-large-scale-integration"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "su8-master-baseline"],
    sources=["Hansen et al. 2002 PNAS 99, 16531 (microfluidic protein crystallization)"],
    publication_citation="Hansen et al. 2002",
    validated_performance=None,
    notes="Stub entry. The Quake-group nanoliter protein crystallization chip — directly commercialized as Fluidigm Topaz. Useful as IP-clear reference architecture for academic structural biology automation. Architectural cousin of Mosquito and Echo dispenser approaches with the difference that the Quake-valve architecture enables true free-interface diffusion (impossible with droplet-based dispensers).",
    disclosed_subsystems=[
        "valve-quake-pneumatic-membrane",
        "fabrication-pdms-soft-lithography",
        "fabrication-multilayer-lamination",
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
