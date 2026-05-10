#!/usr/bin/env python3
"""Seventh expansion of control instruments."""
import json
from pathlib import Path

OUT = Path(__file__).parent / "instruments.jsonl"
ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("last_updated", "2026-05-09")
    ENTRIES.append(kw)


add(
    id="open-mrna-lnp-synthesizer-controller",
    canonical_name="Open mRNA-LNP synthesizer flow controller",
    aliases=["open LNP synthesizer", "open NanoAssemblr"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="syringe-pump",
    purpose="Two-channel high-precision syringe pump controller specifically tuned for mRNA-LNP synthesis: independent mass-flow-controlled aqueous and ethanol-lipid channels into a herringbone mixer chip, with flow-rate ratio control (typ. 3:1 aqueous:ethanol). Direct open-source equivalent of Precision Nanosystems Spark research-scale instrument in the $50k commercial range.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-mrna-lnp-synthesizer-controller/hardware/", "format": "KiCad project + machined syringe holder + chip mount (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-mrna-lnp-synthesizer-controller/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 microcontroller", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "high-resolution stepper motors (precision lead-screw drive)", "vendor": "any", "part_number": "NEMA 17 high-resolution + planetary gear", "quantity": 2, "unit_cost_usd": 80.00},
        {"part": "Trinamic TMC2209 stepper drivers", "vendor": "Trinamic", "part_number": "TMC2209", "quantity": 2, "unit_cost_usd": 16.00},
        {"part": "BD glass syringes (10 mL) + holders", "vendor": "BD / Hamilton", "part_number": "10 mL gas-tight glass", "quantity": 2, "unit_cost_usd": 60.00},
        {"part": "machined aluminum syringe drives", "vendor": "machined", "part_number": "high-precision lead-screw assembly", "quantity": 2, "unit_cost_usd": 200.00},
        {"part": "herringbone mixer chip (PDMS or thermoplastic)", "vendor": "self-fab or vendor", "part_number": "see herringbone-mixer-fabrication-baseline", "quantity": 1, "unit_cost_usd": 20.00},
        {"part": "1/16 inch PEEK tubing + fittings", "vendor": "IDEX", "part_number": "1/16 OD PEEK", "quantity": 1, "unit_cost_usd": 30.00},
        {"part": "12V 5A PSU", "vendor": "any", "part_number": "12V/5A", "quantity": 1, "unit_cost_usd": 20.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 50.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=600,
    validated_performance=None,
    related_corpus_entries=["microfluidic-mrna-vaccine-formulation", "precision-nanosystems-nanoassemblr", "stroock-2002-staggered-herringbone-mixer"],
    related_fab_recipes=["herringbone-mixer-fabrication-baseline", "pdms-su8-soft-lithography-baseline"],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Belliveau et al. 2012 Mol. Ther. Nucleic Acids 1, e37 (Cullis LNP synthesis)",
    ],
    notes="Stub entry. Architectural target: research-scale mRNA-LNP synthesizer at sub-$1000 BOM. The Precision Nanosystems Spark sells for ~$50k; this design replicates the core flow-control functionality at academic budget. Critical for academic mRNA vaccine research that doesn't require GMP-scale Precision Nanosystems Blaze instruments.",
    draft=True,
)

add(
    id="open-cell-therapy-process-monitor",
    canonical_name="Open cell therapy process monitor (cell-counting + viability)",
    aliases=["open CAR-T monitor"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="In-line cell-counting and viability monitor for cell therapy manufacturing: combines impedance counting (Coulter) with optical viability assessment (calcein AM / propidium iodide ratiometric fluorescence) for closed-loop monitoring of CAR-T or other cell therapy bioreactor cultures.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-cell-therapy-process-monitor/hardware/", "format": "KiCad + integrated chip mount (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-cell-therapy-process-monitor/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32G474 microcontroller", "vendor": "ST/Mouser", "part_number": "STM32G474RE", "quantity": 1, "unit_cost_usd": 9.00},
        {"part": "impedance counter front-end (see open-coulter-counter)", "vendor": "internal", "part_number": "see open-coulter-counter entry", "quantity": 1, "unit_cost_usd": 100.00},
        {"part": "fluorescence detector (PMT or SiPM)", "vendor": "Hamamatsu", "part_number": "S13360 SiPM or H10720 PMT", "quantity": 2, "unit_cost_usd": 200.00},
        {"part": "LED excitation 470 nm + 545 nm", "vendor": "Cree", "part_number": "C503B + 545 nm LED", "quantity": 2, "unit_cost_usd": 30.00},
        {"part": "filter set (FITC + Texas Red)", "vendor": "Chroma", "part_number": "ET-FITC + ET-TexasRed", "quantity": 1, "unit_cost_usd": 250.00},
        {"part": "microfluidic flow cell (impedance + fluorescence)", "vendor": "self-fab", "part_number": "PDMS + Pt electrodes", "quantity": 1, "unit_cost_usd": 30.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "4-layer", "quantity": 1, "unit_cost_usd": 60.00},
        {"part": "12V 2A PSU + USB", "vendor": "any", "part_number": "12V/2A", "quantity": 1, "unit_cost_usd": 15.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=800,
    validated_performance=None,
    related_corpus_entries=["microfluidic-cell-therapy-manufacturing", "cellares-cell-shuttle", "lonza-cocoon-cell-therapy", "miltenyi-clinimacs-prodigy"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Sun & Morgan 2010 (impedance cytometry review)",
    ],
    notes="Stub entry. Architectural target: cell therapy process monitor at sub-$1000 BOM. Combines impedance counting and ratiometric viability fluorescence in a single in-line probe suitable for closed-system cell therapy bioreactor monitoring. Enables academic CAR-T research without commercial Cellares / Lonza / Miltenyi process equipment.",
    draft=True,
)

add(
    id="open-organoid-on-chip-perfusion-controller",
    canonical_name="Open organoid-on-chip perfusion controller",
    aliases=["open organoid perfusion"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="pressure-controller",
    purpose="Multi-channel low-pressure perfusion controller specifically tuned for organoid-on-chip applications: 8 independent channels at 0–50 mbar with sub-µL/min flow control, integrated waste handling, and CO2/O2 gas exchange line. Direct open-source equivalent of Emulate / TissUse organ-chip culture systems.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-organoid-on-chip-perfusion-controller/hardware/", "format": "KiCad + manifold + chip-holder mechanical CAD (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-organoid-on-chip-perfusion-controller/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 microcontroller", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "low-pressure proportional regulators 0–100 mbar", "vendor": "Festo / SMC", "part_number": "VEAA 0-100mbar", "quantity": 8, "unit_cost_usd": 1200.00},
        {"part": "Honeywell low-range pressure sensors 0–100 mbar", "vendor": "Honeywell", "part_number": "HSCMRRD100MD2A3", "quantity": 8, "unit_cost_usd": 320.00},
        {"part": "machined aluminum manifold + chip holders", "vendor": "machined", "part_number": "8-channel custom + chip dock", "quantity": 1, "unit_cost_usd": 250.00},
        {"part": "tubing and fittings (cell-culture-grade)", "vendor": "IDEX / Cole-Parmer", "part_number": "PEEK + biocompatible silicone", "quantity": 1, "unit_cost_usd": 80.00},
        {"part": "stage-top incubator interface (CO2 + temperature)", "vendor": "see open-microscope-incubator entry", "part_number": "internal", "quantity": 1, "unit_cost_usd": 400.00},
        {"part": "12V 3A PSU", "vendor": "any", "part_number": "12V/3A", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 60.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=2500,
    validated_performance=None,
    related_corpus_entries=["organoid-on-chip-clevers-2020", "emulate-organ-on-chip-platform", "ingber-emulate-organ-chip", "huh-2010-lung-on-chip"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Festo VEAA datasheet",
        "Honeywell HSCMRRD100MD2A3 datasheet",
    ],
    notes="Stub entry. Architectural target: 8-channel organ-chip perfusion controller at sub-$3000 BOM. Replaces commercial Emulate Zoë system (~$80k) and TissUse / Mimetas systems for organ-on-chip experiments. The low-pressure (sub-50-mbar) operation requirement is demanding — most pressure controllers are designed for 0–1 bar range and do not give precise sub-mbar resolution at the low end of organ-chip flow rates.",
    draft=True,
)


with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new instruments to {OUT}")

for e in ENTRIES:
    base = Path(__file__).parent / "instruments" / e["id"]
    for sub in ["hardware", "firmware", "docs"]:
        d = base / sub
        d.mkdir(parents=True, exist_ok=True)
        (d / ".gitkeep").touch()
