#!/usr/bin/env python3
"""Expansion of control instruments."""
import json
from pathlib import Path

OUT = Path(__file__).parent / "instruments.jsonl"
ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("last_updated", "2026-05-09")
    ENTRIES.append(kw)


add(
    id="open-syringe-pump-stm32-poseidon-derivative",
    canonical_name="Open syringe pump (STM32 + NEMA17, Poseidon-derivative)",
    aliases=["open syringe pump"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="syringe-pump",
    purpose="Single-channel programmable syringe pump driving 1 mL to 60 mL syringes at flow rates 0.1 µL/min to 10 mL/min. Direct open-source replacement for Harvard Apparatus / NE-1000 class syringe pumps in the $1k–$3k range.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-syringe-pump-stm32-poseidon-derivative/hardware/", "format": "KiCad project + 3D-printable mechanical CAD (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-syringe-pump-stm32-poseidon-derivative/firmware/", "language": "Rust embassy / alternatively Arduino-C++", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 Black Pill", "vendor": "WeAct / Aliexpress", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "NEMA 17 stepper motor", "vendor": "any", "part_number": "17HS19-2004S1", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "DRV8825 stepper driver", "vendor": "Pololu", "part_number": "2982", "quantity": 1, "unit_cost_usd": 8.00},
        {"part": "8 mm leadscrew + nut", "vendor": "any", "part_number": "200 mm length", "quantity": 1, "unit_cost_usd": 12.00},
        {"part": "linear rails + carriage", "vendor": "any", "part_number": "MGN9 200 mm", "quantity": 2, "unit_cost_usd": 30.00},
        {"part": "3D-printed structural parts", "vendor": "self-printed", "part_number": "PLA or PETG 200 g", "quantity": 1, "unit_cost_usd": 10.00},
        {"part": "12V power supply 3A", "vendor": "any", "part_number": "12V/3A barrel", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "OLED display 0.96 inch", "vendor": "any", "part_number": "SSD1306 I2C", "quantity": 1, "unit_cost_usd": 5.00},
        {"part": "rotary encoder + push button", "vendor": "any", "part_number": "EC11", "quantity": 1, "unit_cost_usd": 3.00},
    ],
    build_difficulty="hobbyist",
    estimated_cost_usd=120,
    validated_performance=None,
    related_corpus_entries=["poseidon-syringe-pump"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Booeshaghi et al. 2019 HardwareX (Poseidon)",
        "STM32 reference manual",
        "Pololu DRV8825 datasheet",
    ],
    notes="Stub entry. Hardware and firmware directories contain placeholder structure pending community contribution. Architectural target: open-source equivalent of Harvard Apparatus PHD class (~$3k commercial) at ~$120 BOM.",
    draft=True,
)

add(
    id="open-thermal-cycler-peltier-stm32",
    canonical_name="Open thermal cycler (Peltier + STM32, OpenPCR-derivative)",
    aliases=["open thermal cycler"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CERN-OHL-P; firmware MIT; docs CC0-1.0.",
    instrument_class="thermal-cycler",
    purpose="Programmable PCR thermal cycler for 16 × 0.2 mL tubes. Supports denaturation/anneal/extension cycling at 95/55/72 °C with ±0.5 °C uniformity. Direct open-source equivalent of OpenPCR / chai miniPCR.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-thermal-cycler-peltier-stm32/hardware/", "format": "KiCad project + aluminum heat-spreader machining (placeholder)", "license": "CERN-OHL-P"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-thermal-cycler-peltier-stm32/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 Black Pill", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "TEC1-12706 Peltier", "vendor": "any", "part_number": "TEC1-12706", "quantity": 2, "unit_cost_usd": 20.00},
        {"part": "MAX31865 RTD amplifier", "vendor": "Adafruit / Sparkfun", "part_number": "PT100 amp", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "PT100 RTD probe", "vendor": "any", "part_number": "1/8 inch class B", "quantity": 1, "unit_cost_usd": 8.00},
        {"part": "H-bridge for Peltier", "vendor": "Pololu", "part_number": "VNH5019 dual", "quantity": 1, "unit_cost_usd": 30.00},
        {"part": "aluminum heat-spreader block", "vendor": "machined", "part_number": "16-well 0.2 mL", "quantity": 1, "unit_cost_usd": 50.00},
        {"part": "heat sink + fan", "vendor": "any", "part_number": "120 mm", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "12V 10A power supply", "vendor": "any", "part_number": "12V/10A", "quantity": 1, "unit_cost_usd": 25.00},
    ],
    build_difficulty="intermediate",
    estimated_cost_usd=200,
    validated_performance=None,
    related_corpus_entries=["openpcr-thermal-cycler"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "OpenPCR project documentation",
        "STM32 reference manual",
        "TEC1-12706 datasheet",
    ],
    notes="Stub entry. Architectural target: open-source equivalent of bench thermal cyclers (~$3k–$8k commercial) at ~$200 BOM. Limited to 16-tube format; expansion to 96-well requires substantial mechanical redesign.",
    draft=True,
)

add(
    id="open-ewod-driver-dropbot-derivative",
    canonical_name="Open EWOD driver board (DropBot-derivative)",
    aliases=["open EWOD driver"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CERN-OHL-P; firmware MIT; docs CC0-1.0.",
    instrument_class="ewod-driver",
    purpose="EWOD (digital microfluidics) driver board with 80 individually addressable electrode channels at up to 300 V AC. Direct open-source replacement for commercial EWOD drivers in the $5k–$15k range. Compatible with DropBot software ecosystem.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-ewod-driver-dropbot-derivative/hardware/", "format": "KiCad project (placeholder)", "license": "CERN-OHL-P"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-ewod-driver-dropbot-derivative/firmware/", "language": "Rust embassy / Arduino-C++", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 Black Pill", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "high-voltage AC source", "vendor": "various", "part_number": "300V AC sine 1 kHz", "quantity": 1, "unit_cost_usd": 200.00},
        {"part": "HV switch matrix (HV507)", "vendor": "Microchip", "part_number": "HV507", "quantity": 3, "unit_cost_usd": 18.00},
        {"part": "FPC connector for chip", "vendor": "Hirose", "part_number": "FH12-80S", "quantity": 1, "unit_cost_usd": 8.00},
        {"part": "custom PCB", "vendor": "JLCPCB / OSHPark", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 50.00},
        {"part": "USB isolator", "vendor": "Adafruit", "part_number": "ISO7041", "quantity": 1, "unit_cost_usd": 30.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=400,
    validated_performance=None,
    related_corpus_entries=["dropbot-open-source-dmf", "pollack-2000-electrowetting-droplet"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation="Fobel, Fobel, Wheeler 2013 Appl. Phys. Lett. 102, 193513",
    sources=[
        "DropBot project repository",
        "HV507 datasheet",
        "Fobel et al. 2013",
    ],
    notes="Stub entry. Architectural target: production-grade alternative to DropBot's existing reference design at sub-$500 BOM. The most demanding instrument in the catalog because of the high-voltage AC switching and the safety considerations that follow.",
    draft=True,
)

add(
    id="open-pneumatic-valve-bank-controller",
    canonical_name="Open pneumatic valve bank controller (24-channel)",
    aliases=["open valve bank"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CERN-OHL-P; firmware MIT; docs CC0-1.0.",
    instrument_class="valve-bank-controller",
    purpose="24-channel pneumatic valve bank with individually addressable solenoid valves driving Quake-style pneumatic membrane valves on PDMS chips. Replaces commercial Fluigent / Elveflow valve banks in the $3k–$8k range.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-pneumatic-valve-bank-controller/hardware/", "format": "KiCad project + manifold mechanical CAD (placeholder)", "license": "CERN-OHL-P"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-pneumatic-valve-bank-controller/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 Black Pill", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "miniature solenoid valves 3-way", "vendor": "Lee Company / SMC", "part_number": "LHDA1233415H or equivalent", "quantity": 24, "unit_cost_usd": 35.00},
        {"part": "MIC2981 high-side driver array", "vendor": "Microchip", "part_number": "MIC2981/2", "quantity": 3, "unit_cost_usd": 5.00},
        {"part": "manifold block (machined aluminum)", "vendor": "machined", "part_number": "24-port custom", "quantity": 1, "unit_cost_usd": 200.00},
        {"part": "PTFE tubing 1/16 inch ID", "vendor": "any", "part_number": "1 m", "quantity": 1, "unit_cost_usd": 20.00},
        {"part": "compressed-air input regulator", "vendor": "SMC / Festo", "part_number": "0–6 bar", "quantity": 1, "unit_cost_usd": 80.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 60.00},
        {"part": "12V 5A power supply", "vendor": "any", "part_number": "12V/5A", "quantity": 1, "unit_cost_usd": 20.00},
    ],
    build_difficulty="intermediate",
    estimated_cost_usd=1200,
    validated_performance=None,
    related_corpus_entries=["unger-2000-quake-monolithic-membrane-valve", "thorsen-2002-microfluidic-large-scale-integration", "fluidigm-dynamic-array-ifc"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Lee Company solenoid valve datasheet",
        "Unger et al. 2000 Science 288, 113–116",
        "Wheeler group pneumatic-driver references",
    ],
    notes="Stub entry. Architectural target: production-grade open valve bank for driving Quake-style chips. Most expensive instrument in the catalog because of solenoid valve count; the MEMS-valve-on-board route (silicon-microfabricated solenoids) could substantially reduce cost in a future revision.",
    draft=True,
)

with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new instruments to {OUT}")
