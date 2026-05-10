#!/usr/bin/env python3
"""Ninth expansion of control instruments."""
import json
from pathlib import Path

OUT = Path(__file__).parent / "instruments.jsonl"
ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("last_updated", "2026-05-09")
    ENTRIES.append(kw)


add(
    id="open-multiplexed-valve-controller-256",
    canonical_name="Open multiplexed pneumatic valve controller (256-channel)",
    aliases=["open valve controller 256"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="pressure-controller",
    purpose="High-channel-count pneumatic valve controller for large-scale-integration (LSI) microfluidic chips: 256 independently addressable solenoid valves controlling Quake-style pneumatic membrane valves on PDMS chips. Direct open-source replacement for $20k–$50k commercial Fluidigm BioMark / Wago-Ladewig systems.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-multiplexed-valve-controller-256/hardware/", "format": "KiCad project + machined manifold + chip dock (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-multiplexed-valve-controller-256/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32H743 microcontroller (high-perf for 256-ch updates)", "vendor": "ST/Mouser", "part_number": "STM32H743VIT6", "quantity": 1, "unit_cost_usd": 18.00},
        {"part": "Festo MHE2 / SMC SX10 mini solenoid valves (24V, 8 mm)", "vendor": "Festo / SMC", "part_number": "MHE2-MS1H", "quantity": 256, "unit_cost_usd": 5120.00},
        {"part": "16-channel I/O expanders", "vendor": "Microchip", "part_number": "MCP23S17", "quantity": 16, "unit_cost_usd": 32.00},
        {"part": "MOSFET valve drivers", "vendor": "any", "part_number": "ULN2803A 8-ch Darlington array", "quantity": 32, "unit_cost_usd": 64.00},
        {"part": "machined aluminum 256-port manifold", "vendor": "machined", "part_number": "256-port custom", "quantity": 1, "unit_cost_usd": 800.00},
        {"part": "1/16 inch pneumatic tubing + multi-port fittings", "vendor": "IDEX / SMC", "part_number": "1/16 OD pneumatic", "quantity": 1, "unit_cost_usd": 200.00},
        {"part": "compressor (oil-free, 30 psi capable)", "vendor": "any", "part_number": "Werther Sil-Air 50 or equivalent", "quantity": 1, "unit_cost_usd": 400.00},
        {"part": "24V 10A PSU + 5V regulators", "vendor": "any", "part_number": "24V/10A", "quantity": 1, "unit_cost_usd": 60.00},
        {"part": "custom backplane PCB", "vendor": "JLCPCB", "part_number": "8-layer with thermal management", "quantity": 1, "unit_cost_usd": 200.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=7000,
    validated_performance=None,
    related_corpus_entries=["unger-2000-quake-monolithic-membrane-valve", "thorsen-2002-microfluidic-large-scale-integration", "fluidigm-biomark-system"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline"],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Festo MHE2 mini solenoid datasheet",
    ],
    notes="Stub entry. Architectural target: 256-channel pneumatic valve controller at sub-$8000 BOM, replacing $30k+ commercial systems. The valve count itself dominates BOM cost — solenoid valves at $20 each × 256 = $5120 floor. Critical for academic groups working with Quake-valve LSI chips (Thorsen 2002 lineage); without this scale of valve control, only smaller chips (Beebe 2007 'self-propulsion' types) are accessible.",
    draft=True,
)

add(
    id="open-dielectrophoresis-driver",
    canonical_name="Open dielectrophoresis (DEP) driver",
    aliases=["open DEP driver"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Multi-frequency AC signal source for dielectrophoresis (DEP) cell sorting and trapping: 1 kHz to 100 MHz at 0–20 Vpp, with independent control of frequency, amplitude, and phase across 4 electrode pairs. Suitable for academic DEP-based cell separation, exosome isolation, and nanoparticle manipulation.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-dielectrophoresis-driver/hardware/", "format": "KiCad project + 3D-printed chip mount (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-dielectrophoresis-driver/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32G474 microcontroller", "vendor": "ST/Mouser", "part_number": "STM32G474RE", "quantity": 1, "unit_cost_usd": 9.00},
        {"part": "AD9959 quad DDS up to 100 MHz", "vendor": "Analog Devices", "part_number": "AD9959", "quantity": 1, "unit_cost_usd": 50.00},
        {"part": "high-voltage op-amps (±15V output, 100 MHz BW)", "vendor": "Analog Devices", "part_number": "ADA4870", "quantity": 4, "unit_cost_usd": 80.00},
        {"part": "transformer-coupled output stage", "vendor": "Mini-Circuits", "part_number": "ADTT1-1", "quantity": 4, "unit_cost_usd": 60.00},
        {"part": "3D-printed chip mount with spring-loaded contacts", "vendor": "self-printed", "part_number": "PETG", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "amplitude monitor (rectifier + ADC)", "vendor": "discrete", "part_number": "Schottky + AD8307", "quantity": 4, "unit_cost_usd": 40.00},
        {"part": "BNC + SMA connectors", "vendor": "any", "part_number": "PCB SMA + BNC", "quantity": 8, "unit_cost_usd": 24.00},
        {"part": "custom RF PCB (4-layer)", "vendor": "JLCPCB", "part_number": "4-layer 50 Ω", "quantity": 1, "unit_cost_usd": 80.00},
        {"part": "12V 2A PSU + ±15V supplies", "vendor": "any", "part_number": "dual-rail", "quantity": 1, "unit_cost_usd": 30.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=500,
    validated_performance=None,
    related_corpus_entries=["pohl-1958-dielectrophoresis", "gascoyne-2011-dielectrophoresis-review", "apostream-cancer-isolation"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Analog Devices AD9959 datasheet",
        "Pohl 1958 dielectrophoresis foundation",
    ],
    notes="Stub entry. Architectural target: 4-channel DEP driver at sub-$500 BOM. The wide frequency range (1 kHz to 100 MHz) is characteristic of DEP — different cell types respond to different frequencies, so multi-frequency capability enables sequential separation. Most commercial DEP instruments (e.g., Apocell ApoStream) are dedicated single-application systems; an open multi-frequency driver enables custom DEP applications.",
    draft=True,
)

add(
    id="open-bluetooth-wearable-poc-reader",
    canonical_name="Open Bluetooth wearable POC reader (smartphone-companion)",
    aliases=["open BLE POC reader"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Bluetooth-LE wearable POC reader: small battery-powered cartridge interface that performs local sample-handling, optical or electrochemical readout, and BLE transmission to a smartphone for analysis. Architectural cousin of Siemens epoc, Cue Health Reader, and Lucira COVID test cartridges.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-bluetooth-wearable-poc-reader/hardware/", "format": "KiCad project + 3D-printed wearable enclosure (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-bluetooth-wearable-poc-reader/firmware/", "language": "Rust embassy + smartphone companion app", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "Nordic nRF52840 (BLE + microcontroller)", "vendor": "Nordic Semiconductor", "part_number": "nRF52840", "quantity": 1, "unit_cost_usd": 18.00},
        {"part": "TSL2591 light-to-digital converter (colorimetric readout)", "vendor": "ams", "part_number": "TSL2591", "quantity": 1, "unit_cost_usd": 8.00},
        {"part": "RGB LEDs for excitation", "vendor": "any", "part_number": "white + 470nm", "quantity": 2, "unit_cost_usd": 5.00},
        {"part": "thermistor + RTD + heater (for isothermal amplification)", "vendor": "any", "part_number": "PT100 + Kapton heater", "quantity": 1, "unit_cost_usd": 25.00},
        {"part": "Li-poly battery 1000 mAh + charger", "vendor": "Adafruit", "part_number": "MCP73831 + 1000 mAh", "quantity": 1, "unit_cost_usd": 25.00},
        {"part": "single-use cartridge interface (spring-loaded contacts)", "vendor": "any", "part_number": "10-pin spring contacts", "quantity": 1, "unit_cost_usd": 8.00},
        {"part": "3D-printed enclosure", "vendor": "self-printed", "part_number": "PETG", "quantity": 1, "unit_cost_usd": 8.00},
        {"part": "custom PCB (2-layer, compact)", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 30.00},
    ],
    build_difficulty="intermediate",
    estimated_cost_usd=130,
    validated_performance=None,
    related_corpus_entries=["epoc-blood-gas-analyzer", "cue-health-cartridge", "lucira-home-covid-test", "abingdon-health-pbm-2-lfa-reader"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Nordic Semiconductor nRF52840 datasheet",
    ],
    notes="Stub entry. Architectural target: Bluetooth-connected wearable POC reader at sub-$150 BOM. Direct architectural cousin of Cue Health and Lucira commercial readers but at a fraction of cost. Suitable for academic groups developing custom POC cartridges who need a low-cost reader-instrument substrate.",
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
