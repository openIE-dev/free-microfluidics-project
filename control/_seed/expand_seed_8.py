#!/usr/bin/env python3
"""Eighth expansion of control instruments."""
import json
from pathlib import Path

OUT = Path(__file__).parent / "instruments.jsonl"
ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("last_updated", "2026-05-09")
    ENTRIES.append(kw)


add(
    id="open-saw-microfluidic-driver",
    canonical_name="Open SAW (surface acoustic wave) microfluidic driver",
    aliases=["open SAW driver"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="High-frequency RF driver for surface acoustic wave (SAW) microfluidic chips: 100–500 MHz signal generation at up to +30 dBm output, suitable for driving lithium niobate IDT (interdigital transducer) electrodes for SAW-based droplet manipulation, cell sorting, and acoustofluidic mixing. Direct open-source replacement for $5k–$15k commercial RF signal generators + amplifiers.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-saw-microfluidic-driver/hardware/", "format": "KiCad project + 3D-printed enclosure (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-saw-microfluidic-driver/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32G474 microcontroller", "vendor": "ST/Mouser", "part_number": "STM32G474RE", "quantity": 1, "unit_cost_usd": 9.00},
        {"part": "AD9959 quad DDS up to 500 MHz", "vendor": "Analog Devices", "part_number": "AD9959", "quantity": 1, "unit_cost_usd": 50.00},
        {"part": "RF amplifier 0–500 MHz, +30 dBm output", "vendor": "Mini-Circuits", "part_number": "ZHL-1-2W-S+", "quantity": 1, "unit_cost_usd": 250.00},
        {"part": "SMA RF connectors", "vendor": "any", "part_number": "PCB SMA jack", "quantity": 4, "unit_cost_usd": 12.00},
        {"part": "directional coupler for power monitoring", "vendor": "Mini-Circuits", "part_number": "ADC-10-1-75+", "quantity": 1, "unit_cost_usd": 35.00},
        {"part": "log-detector RF power sensor", "vendor": "Analog Devices", "part_number": "AD8307", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "12V 3A PSU + RF-shielded enclosure", "vendor": "Hammond", "part_number": "die-cast aluminum 1590B", "quantity": 1, "unit_cost_usd": 50.00},
        {"part": "custom RF PCB (4-layer with controlled impedance)", "vendor": "JLCPCB", "part_number": "4-layer 50 Ω microstrip", "quantity": 1, "unit_cost_usd": 80.00},
        {"part": "USB-C interface", "vendor": "any", "part_number": "USB-C connector", "quantity": 1, "unit_cost_usd": 5.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=600,
    validated_performance=None,
    related_corpus_entries=["franke-2009-acoustic-cell-sorting-saw", "laurell-2007-acoustophoresis", "shi-friend-2009-saw-droplet"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Analog Devices AD9959 datasheet",
        "Mini-Circuits ZHL-1-2W-S+ datasheet",
    ],
    notes="Stub entry. Architectural target: 4-channel SAW driver at sub-$700 BOM. SAW microfluidics requires precise RF signal generation in the 100–500 MHz range with sufficient power to drive piezoelectric IDTs, which most general-purpose RF function generators don't provide cost-effectively. The 4-channel architecture supports independent control of multiple IDTs for advanced acoustofluidic operations (e.g., 2D droplet manipulation, traveling-wave acoustophoresis).",
    draft=True,
)

add(
    id="open-lateral-flow-reader",
    canonical_name="Open lateral-flow assay reader (multi-strip, smartphone-or-instrument)",
    aliases=["open LFA reader"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Quantitative lateral-flow assay reader: optical reflectance imaging of LFA test/control lines with computational analysis (line position detection, intensity normalization, multiplex deconvolution). Compatible with most commercial LFA cartridge formats. Direct open-source replacement for commercial LFA readers in the $500–$3000 range.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-lateral-flow-reader/hardware/", "format": "3D-printed body + LED + camera + Pi or smartphone (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-lateral-flow-reader/firmware/", "language": "Rust + Python image processing", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "Raspberry Pi 5 (or Pi 4)", "vendor": "Raspberry Pi", "part_number": "RPi5 4GB", "quantity": 1, "unit_cost_usd": 65.00},
        {"part": "Pi camera module (HQ or Camera v3)", "vendor": "Raspberry Pi", "part_number": "Camera Module 3", "quantity": 1, "unit_cost_usd": 30.00},
        {"part": "white LED illumination ring", "vendor": "any", "part_number": "12-LED ring", "quantity": 1, "unit_cost_usd": 10.00},
        {"part": "LED driver (constant-current)", "vendor": "any", "part_number": "AL8806", "quantity": 1, "unit_cost_usd": 5.00},
        {"part": "3D-printed reader enclosure with cartridge slot", "vendor": "self-printed", "part_number": "PETG, blackened interior", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "5V 3A PSU + USB-C", "vendor": "any", "part_number": "5V/3A USB-C", "quantity": 1, "unit_cost_usd": 12.00},
        {"part": "custom carrier PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 30.00},
    ],
    build_difficulty="hobbyist",
    estimated_cost_usd=180,
    validated_performance=None,
    related_corpus_entries=["orasure-quickflex-cartridge", "chembio-dpp", "abingdon-health-pbm-2-lfa-reader"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Various academic publications on quantitative LFA imaging",
    ],
    notes="Stub entry. Architectural target: quantitative LFA reader at sub-$200 BOM. The dominant commercial LFA reader vendors (Abingdon Health, Detekt Biomedical, Cellmic) charge $500–$3000 for proprietary readers — open-source equivalents enable academic and low-resource-setting LFA quantification at a small fraction of cost. The image-analysis software is the primary IP; hardware is straightforward.",
    draft=True,
)

add(
    id="open-water-quality-cartridge-reader",
    canonical_name="Open environmental water-quality cartridge reader",
    aliases=["open water quality reader"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Field-deployable water-quality cartridge reader: integrated incubator (35 °C ± 0.5 °C for coliform / E. coli enzyme assays), fluorescence/colorimetric optical readout, and battery operation for off-grid sampling. Compatible with IDEXX Colilert-class enzyme-substrate cartridges and similar formats.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-water-quality-cartridge-reader/hardware/", "format": "KiCad + 3D-printed insulated incubator (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-water-quality-cartridge-reader/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 microcontroller", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "PT100 RTD + MAX31865 amplifier", "vendor": "Adafruit", "part_number": "MAX31865 + PT100", "quantity": 1, "unit_cost_usd": 22.00},
        {"part": "resistive heater + insulation", "vendor": "any", "part_number": "Kapton-flex heater 12V/30W", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "365 nm UV LED for fluorescence excitation", "vendor": "Nichia / LED Engin", "part_number": "365 nm 3W", "quantity": 1, "unit_cost_usd": 25.00},
        {"part": "white LED + photodiode array for colorimetric", "vendor": "any", "part_number": "TSL2591 + LEDs", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "GU10-MPN counting lens + filter", "vendor": "Edmund / Thorlabs", "part_number": "510 nm long-pass filter", "quantity": 1, "unit_cost_usd": 40.00},
        {"part": "Li-ion battery pack 12 V / 5 Ah", "vendor": "any", "part_number": "12V Li-ion 5Ah", "quantity": 1, "unit_cost_usd": 35.00},
        {"part": "3D-printed insulated enclosure", "vendor": "self-printed", "part_number": "PETG + foam insulation", "quantity": 1, "unit_cost_usd": 25.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 50.00},
    ],
    build_difficulty="intermediate",
    estimated_cost_usd=300,
    validated_performance=None,
    related_corpus_entries=["idexx-colilert-water", "neogen-atlas-pathogen", "bridle-2014-soil-microfluidic-extraction"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "IDEXX Colilert / Quanti-Tray product literature",
    ],
    notes="Stub entry. Architectural target: field-deployable water-quality cartridge reader at sub-$300 BOM, replacing $1k–$5k benchtop incubators + readers. Suitable for citizen-science water monitoring, low-resource public health surveillance, and off-grid environmental sampling.",
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
