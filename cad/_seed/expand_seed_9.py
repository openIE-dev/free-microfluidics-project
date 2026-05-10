#!/usr/bin/env python3
"""Ninth expansion of CAD designs."""
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
    id="lsi-valve-chip-256-multiplex",
    canonical_name="Large-scale-integration (LSI) Quake-valve chip (256-valve multiplex)",
    aliases=["LSI 256 chip", "Thorsen 2002-style chip"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="lab-on-chip",
    substrate_material="PDMS",
    fabrication_path="Two SU-8 masters per Thorsen 2002 architecture: control layer (rounded SPR-220 25 µm) and flow layer (SU-8 50 µm); push-up Quake valves; 256 valves arranged in 8-bit binary multiplex addressing 256 chambers",
    channel_geometry="256 reaction chambers (5 nL each) addressed by 16 row-control + 16 column-control valves arranged in 8-bit binary multiplex (saving 240 valve lines vs direct addressing). Each chamber has independently programmable contents via combinatorial valve actuation. Chip footprint 75 mm × 50 mm.",
    chip_footprint_mm=75,
    cad_files=[
        "designs/lsi-valve-chip-256-multiplex/control_layer.dxf",
        "designs/lsi-valve-chip-256-multiplex/flow_layer.dxf",
        "designs/lsi-valve-chip-256-multiplex/design.gds",
    ],
    cad_format="mixed",
    mask_count=2,
    related_corpus_entries=["thorsen-2002-microfluidic-large-scale-integration", "unger-2000-quake-monolithic-membrane-valve", "fluidigm-biomark-system"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "su8-master-baseline"],
    sources=["Thorsen et al. 2002 Science 298, 580 (LSI microfluidics)"],
    publication_citation="Thorsen et al. 2002",
    validated_performance=None,
    notes="Stub entry. The canonical large-scale-integration Quake-valve chip — direct architectural ancestor of the Fluidigm BioMark high-throughput PCR platform. Pairs with the open-multiplexed-valve-controller-256 instrument for end-to-end open-hardware LSI microfluidic capability.",
    disclosed_subsystems=[
        "valve-quake-pneumatic-membrane",
        "fabrication-pdms-soft-lithography",
        "fabrication-multilayer-lamination",
        "architecture-multiplex-cartridge",
    ],
)

add(
    id="dielectrophoresis-cell-sorter-chip",
    canonical_name="Dielectrophoresis cell sorter chip (Pohl-DEP architecture)",
    aliases=["DEP cell sorter chip", "iDEP chip"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="separator-component",
    substrate_material="glass",
    fabrication_path="Glass substrate; sputtered + lithographically patterned ITO or Pt electrodes 100 nm thickness; PDMS channel layer plasma-bonded on top with electrode contacts exposed at chip edges",
    channel_geometry="200 µm × 50 µm flow channel with 5 pairs of opposing-electrode arrays (each 50 µm × 200 µm) along channel length. Cell suspension flows through, with AC field at multiple frequencies applied to electrode pairs to selectively trap or deflect cells based on dielectric properties. Side outlet for trapped cell collection.",
    chip_footprint_mm=50,
    cad_files=[
        "designs/dielectrophoresis-cell-sorter-chip/electrode_layer.dxf",
        "designs/dielectrophoresis-cell-sorter-chip/channel_layer.dxf",
        "designs/dielectrophoresis-cell-sorter-chip/design.gds",
    ],
    cad_format="mixed",
    mask_count=2,
    related_corpus_entries=["pohl-1958-dielectrophoresis", "gascoyne-2011-dielectrophoresis-review", "apostream-cancer-isolation"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "ewod-cartridge-fabrication-baseline"],
    sources=["Pohl 1958 (DEP foundation); Gascoyne 2011 review"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. The canonical DEP cell sorter chip architecture: opposing-electrode arrays for AC-field-driven cell separation. Pairs with open-dielectrophoresis-driver instrument. Distinct from inertial-microfluidic and acoustic-microfluidic separators by enabling type-specific separation based on dielectric properties (cell membrane, cytoplasm conductivity) rather than size.",
    disclosed_subsystems=[
        "separation-dielectrophoresis",
        "fabrication-glass-photolithography",
        "fabrication-pdms-soft-lithography",
    ],
)

add(
    id="bluetooth-poc-cartridge-reference",
    canonical_name="Bluetooth POC cartridge reference (Cue/Lucira-class)",
    aliases=["BLE POC cartridge"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_path="Injection-molded PMMA or COC cartridge body; PSA-laminated cover; integrated electrochemical or fluorescent detection chamber; spring-loaded contact pads on cartridge bottom for instrument interface",
    channel_geometry="Sample-application port (200 µL) → mixing chamber with lyophilized reagents → metering chamber → detection chamber (50 µL) with embedded electrodes (electrochemical) or excitation/emission window (fluorescent). Cartridge dimensions 80 mm × 30 mm × 8 mm, designed to mate with open-bluetooth-wearable-poc-reader instrument.",
    chip_footprint_mm=80,
    cad_files=[
        "designs/bluetooth-poc-cartridge-reference/cartridge_body.dxf",
        "designs/bluetooth-poc-cartridge-reference/cover.dxf",
        "designs/bluetooth-poc-cartridge-reference/design.gds",
    ],
    cad_format="mixed",
    mask_count=2,
    related_corpus_entries=["cue-health-cartridge", "lucira-home-covid-test", "epoc-blood-gas-analyzer", "visby-medical-cartridge"],
    related_fab_recipes=["thermoplastic-hot-embossing-coc-baseline", "psa-lamination-microfluidics-baseline"],
    sources=["Various FDA EUA documents for Cue Health and Lucira COVID-19 tests"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. Reference architecture for Bluetooth-connected POC cartridges in the Cue Health / Lucira / Visby Medical product category. Pairs with open-bluetooth-wearable-poc-reader instrument for academic POC cartridge development.",
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "fabrication-thermoplastic-injection-molding",
        "fabrication-multilayer-lamination",
    ],
)

add(
    id="agricultural-microbiome-cartridge",
    canonical_name="Agricultural microbiome sample-to-sequencing cartridge",
    aliases=["soil microbiome cartridge"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_path="Injection-molded PMMA cartridge with integrated bead-beating sample-prep chamber, PCR amplification chamber, and Oxford Nanopore-compatible sequencing prep chamber",
    channel_geometry="Sample input (5 mL soil + buffer slurry) → bead-beating lysis chamber (2 mL with embedded beads) → silica column extraction (200 µL) → PCR amplification chamber (50 µL with embedded heater) → library prep chamber → output to MinION flow cell. Cartridge total dimensions 100 mm × 60 mm × 15 mm.",
    chip_footprint_mm=100,
    cad_files=[
        "designs/agricultural-microbiome-cartridge/cartridge_body.dxf",
        "designs/agricultural-microbiome-cartridge/heater_layer.dxf",
        "designs/agricultural-microbiome-cartridge/design.gds",
    ],
    cad_format="mixed",
    mask_count=2,
    related_corpus_entries=["bridle-2014-soil-microfluidic-extraction", "environmental-microbiome-cartridge-2024", "oxford-nanopore-minion"],
    related_fab_recipes=["thermoplastic-hot-embossing-coc-baseline", "psa-lamination-microfluidics-baseline"],
    sources=["Various 2024-2026 publications on field-deployable microbiome cartridges"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. Reference architecture for field-deployable soil/water microbiome cartridges combining mechanical lysis (bead-beating), nucleic-acid extraction, PCR amplification, and Oxford Nanopore sequencing prep. Direct architectural ancestor of emerging commercial soil-microbiome diagnostic platforms (Trace Genomics, Indigo Ag soil testing).",
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-pcr-cycling",
        "fabrication-thermoplastic-injection-molding",
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
