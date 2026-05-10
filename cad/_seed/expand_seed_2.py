#!/usr/bin/env python3
"""Second expansion of CAD designs."""
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
    id="dld-deterministic-lateral-displacement-array",
    canonical_name="DLD (deterministic lateral displacement) reference array, 5 µm cutoff",
    aliases=["DLD reference"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="separator-component",
    substrate_material="PDMS",
    fabrication_path="SU-8 2025 master, 25 µm; PDMS 10:1 cured 60 min @ 65 °C; plasma bond to glass slide",
    channel_geometry="Hexagonal post array with 10 µm post diameter, 6 µm gap, 1/10 row shift fraction over 50 mm length; cutoff diameter ~5 µm; 8-row design giving 4× lateral displacement of large particles",
    chip_footprint_mm=75,
    cad_files=[
        "designs/dld-deterministic-lateral-displacement-array/design.dxf",
        "designs/dld-deterministic-lateral-displacement-array/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["huang-2004-dld-deterministic-lateral-displacement", "ozkumur-2013-ctc-iChip"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline"],
    sources=["Huang et al. 2004 Science 304, 987 (DLD foundation)"],
    publication_citation="Huang et al. 2004",
    validated_performance=None,
    notes="Stub entry. The canonical DLD architecture for size-based label-free particle separation. Cutoff diameter scales with post gap and row-shift fraction; the parameters above give ~5 µm cutoff suitable for blood-cell-from-platelet separation.",
    disclosed_subsystems=[
        "separation-deterministic-lateral-displacement",
        "fabrication-pdms-soft-lithography",
        "fabrication-su8-photoresist",
    ],
)

add(
    id="inertial-spiral-cell-focuser",
    canonical_name="Inertial spiral cell focuser reference",
    aliases=["spiral inertial reference"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="separator-component",
    substrate_material="PDMS",
    fabrication_path="SU-8 2050 master, 100 µm; PDMS 10:1 cured 60 min @ 65 °C; plasma bond to glass slide",
    channel_geometry="Archimedean spiral with 8 turns, 100 µm × 100 µm channel cross-section, inner radius 5 mm, outer radius 25 mm; sample inlet plus single sheath inlet; 4-bifurcation outlet for size-based collection",
    chip_footprint_mm=75,
    cad_files=[
        "designs/inertial-spiral-cell-focuser/design.dxf",
        "designs/inertial-spiral-cell-focuser/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["di-carlo-2007-inertial-microfluidics", "ozkumur-2013-ctc-iChip"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline"],
    sources=["Di Carlo et al. 2007 PNAS 104, 18892 (inertial focusing foundation)"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. The canonical spiral inertial geometry that combines Dean drag (transverse motion in curving channels at moderate Re) with shear-gradient lift to focus particles into a single streamline. Used in commercial CTC-iChip and Vortex Biosciences platforms.",
    disclosed_subsystems=[
        "separation-inertial-focusing",
        "fabrication-pdms-soft-lithography",
        "fabrication-su8-photoresist",
    ],
)

add(
    id="standardized-port-footprint-mini-luer-12",
    canonical_name="Standardized 12-port mini-Luer footprint reference (microfluidic ChipShop compat)",
    aliases=["mini-Luer reference"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="other",
    substrate_material="hybrid",
    fabrication_path="any (substrate-agnostic; fixture for connector standardization)",
    channel_geometry="12-port mini-Luer connector array on a 25 × 75 mm chip footprint at 6.3 mm pitch; matches microfluidic ChipShop standard",
    chip_footprint_mm=75,
    cad_files=[
        "designs/standardized-port-footprint-mini-luer-12/design.dxf",
        "designs/standardized-port-footprint-mini-luer-12/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["microfluidic-chipshop-fluidic-chips"],
    related_fab_recipes=[],
    sources=["microfluidic ChipShop product catalog"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. Standardized port-footprint reference for microfluidic chip-to-world connectors using the mini-Luer thread (ISO 80369-7 derived). Adopting this footprint allows chips to use commodity connectors and tubing kits already manufactured for the microfluidic ChipShop ecosystem.",
    disclosed_subsystems=[
        "interface-fluidic-edge-connector",
    ],
)

add(
    id="96-well-plate-format-chip-outline",
    canonical_name="96-well-plate-format chip outline (SBS / ANSI standard)",
    aliases=["SBS plate footprint chip"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="other",
    substrate_material="hybrid",
    fabrication_path="any (substrate-agnostic; fixture for plate-format compatibility)",
    channel_geometry="ANSI/SLAS 1-2004 96-well plate footprint (127.76 × 85.48 mm) with optional integration of 96 wells at 9 mm pitch starting at A1=14.38, 11.24 mm; chip body machined to match plate dimensions for handling by liquid-handling robots",
    chip_footprint_mm=128,
    cad_files=[
        "designs/96-well-plate-format-chip-outline/design.dxf",
        "designs/96-well-plate-format-chip-outline/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["fluidigm-dynamic-array-ifc", "opentrons-ot2"],
    related_fab_recipes=[],
    sources=["ANSI/SLAS 1-2004 microplate dimensions standard"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. Canonical reference outline for chips that need to be handled by 96-well-plate-compatible automation (Opentrons, Tecan, Hamilton). The footprint allows chips to slot into existing plate-format infrastructure including liquid handlers, plate readers, and shaker decks.",
    disclosed_subsystems=[
        "architecture-multi-well-array",
    ],
)

add(
    id="droplet-picoinjector-side-channel",
    canonical_name="Droplet picoinjector with side-channel reagent delivery",
    aliases=["picoinjector reference"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="droplet-generator",
    substrate_material="PDMS",
    fabrication_path="SU-8 2025 master, 25 µm; PDMS 10:1 cured 60 min @ 65 °C; plasma bond to glass slide",
    channel_geometry="50 µm × 25 µm pre-formed droplet channel intersected by 10 µm × 25 µm reagent injection orifice with electrocoalescence electrodes; downstream serpentine for mixing",
    chip_footprint_mm=75,
    cad_files=[
        "designs/droplet-picoinjector-side-channel/design.dxf",
        "designs/droplet-picoinjector-side-channel/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["ttp-mirus", "brouzes-2009-droplet-screening"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline"],
    sources=["Abate et al. 2010 PNAS 107, 19163"],
    publication_citation="Abate et al. 2010",
    validated_performance=None,
    notes="Stub entry. Canonical picoinjector geometry: pre-formed droplets pass an injection orifice where applied AC voltage destabilizes the droplet-oil interface, drawing reagent into the droplet. Operates at >10 kHz droplet rates.",
    disclosed_subsystems=[
        "droplet-merging-electrocoalescence",
        "fabrication-pdms-soft-lithography",
        "fabrication-su8-photoresist",
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
