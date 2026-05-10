#!/usr/bin/env python3
"""Third expansion of control instruments: ESI HV, multi-channel peristaltic, OD sensor."""
import json
from pathlib import Path

OUT = Path(__file__).parent / "instruments.jsonl"
ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("last_updated", "2026-05-09")
    ENTRIES.append(kw)


add(
    id="open-esi-hv-controller",
    canonical_name="Open electrospray HV controller (chip-MS interface)",
    aliases=["open ESI controller"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CERN-OHL-P; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Single-channel high-voltage source (0–5 kV DC) with current sensing for driving electrospray emitters in chip-MS interfaces. Replaces commercial benchtop HV power supplies in the $2k–$8k range. Includes safety interlocks and integrated current monitoring for tip-degradation detection.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-esi-hv-controller/hardware/", "format": "KiCad project + 3D-printed safety enclosure (placeholder)", "license": "CERN-OHL-P"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-esi-hv-controller/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 Black Pill", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "EMCO Q-series HV power supply module", "vendor": "XP Power / EMCO", "part_number": "Q50-5", "quantity": 1, "unit_cost_usd": 280.00},
        {"part": "12-bit DAC for HV control", "vendor": "TI", "part_number": "MCP4725", "quantity": 1, "unit_cost_usd": 4.00},
        {"part": "current-sense amplifier (low-side, 1 nA-class)", "vendor": "TI", "part_number": "INA138 + nA-class transimpedance", "quantity": 1, "unit_cost_usd": 8.00},
        {"part": "interlock switches (door, ground)", "vendor": "any", "part_number": "magnetic + mechanical", "quantity": 3, "unit_cost_usd": 12.00},
        {"part": "USB isolator", "vendor": "Adafruit", "part_number": "ISO7041", "quantity": 1, "unit_cost_usd": 30.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run; HV creepage requirements", "quantity": 1, "unit_cost_usd": 60.00},
        {"part": "HV-rated enclosure + grounded shielding", "vendor": "any", "part_number": "machined aluminum or printed PETG with shield", "quantity": 1, "unit_cost_usd": 50.00},
        {"part": "12V 1A PSU", "vendor": "any", "part_number": "12V/1A", "quantity": 1, "unit_cost_usd": 12.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=500,
    validated_performance=None,
    related_corpus_entries=["ramsey-1996-electrospray-on-chip", "advion-triversa-nanomate"],
    related_fab_recipes=["glass-capillary-pulling-baseline"],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "EMCO Q50-5 datasheet",
        "TI INA138 datasheet",
    ],
    notes="Stub entry. Architectural target: HV controller for chip-ESI workflows at sub-$500 BOM, replacing $3k–$8k commercial benchtop supplies. SAFETY CRITICAL: this instrument generates lethal voltages and must include interlocks, ground-fault detection, and operator-side controls; do not deploy without trained electrical engineering review of the design.",
    draft=True,
)

add(
    id="open-multi-channel-peristaltic-pump",
    canonical_name="Open multi-channel peristaltic pump (8-channel)",
    aliases=["open peristaltic pump multi-channel"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="syringe-pump",
    purpose="8-channel peristaltic pump driving 0.1 mL/min to 50 mL/min per channel through 1/16 inch silicone tubing. Direct open-source replacement for commercial multi-channel peristaltic pumps in the $2k–$5k range. Suitable for parallel bioreactor feed, multi-organ-chip perfusion, and combinatorial flow-chemistry work.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-multi-channel-peristaltic-pump/hardware/", "format": "KiCad project + 3D-printable rotor/stator (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-multi-channel-peristaltic-pump/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 Black Pill", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "TMC2209 stepper drivers", "vendor": "Trinamic", "part_number": "TMC2209", "quantity": 8, "unit_cost_usd": 64.00},
        {"part": "NEMA 11 stepper motors", "vendor": "any", "part_number": "11HS18-0674S", "quantity": 8, "unit_cost_usd": 160.00},
        {"part": "3D-printed rotor with 3 rollers each", "vendor": "self-printed", "part_number": "PETG 100 g per channel", "quantity": 8, "unit_cost_usd": 16.00},
        {"part": "608ZZ bearings (rollers)", "vendor": "any", "part_number": "608ZZ", "quantity": 24, "unit_cost_usd": 24.00},
        {"part": "silicone tubing 1/16 inch ID", "vendor": "Cole-Parmer / Saint-Gobain", "part_number": "Tygon B-44-3", "quantity": 1, "unit_cost_usd": 30.00},
        {"part": "machined aluminum stators", "vendor": "machined", "part_number": "8-channel custom", "quantity": 1, "unit_cost_usd": 80.00},
        {"part": "12V 5A PSU", "vendor": "any", "part_number": "12V/5A", "quantity": 1, "unit_cost_usd": 25.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 50.00},
        {"part": "OLED display + encoder", "vendor": "any", "part_number": "SSD1306 + EC11", "quantity": 1, "unit_cost_usd": 12.00},
    ],
    build_difficulty="intermediate",
    estimated_cost_usd=500,
    validated_performance=None,
    related_corpus_entries=["chibio-bioreactor", "evolver-klavins", "open-flexure-pump"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Trinamic TMC2209 datasheet",
        "Saint-Gobain Tygon B-44-3 datasheet",
        "OpenFlexure peristaltic pump community design",
    ],
    notes="Stub entry. Architectural target: 8-channel peristaltic pump at sub-$500 BOM, replacing $2k–$5k commercial multi-channel pumps. The rotor/stator mechanical design is the most important fabrication detail; 3D-printed PETG with off-the-shelf bearings is sufficient for >100 hr continuous operation before tubing replacement.",
    draft=True,
)

add(
    id="open-od-turbidity-sensor",
    canonical_name="Open OD/turbidity sensor for in-line cell-density measurement",
    aliases=["open OD sensor"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="In-line OD600 / turbidity sensor for continuous cell-density monitoring in microfluidic bioreactor or chemostat applications. Single LED-photodiode pair with 600 nm excitation and lock-in detection for noise rejection. Direct open-source equivalent of in-line OD probes in the $1k–$3k range.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-od-turbidity-sensor/hardware/", "format": "KiCad project + 3D-printed flow-cell housing (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-od-turbidity-sensor/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 Black Pill", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "600 nm LED", "vendor": "Cree", "part_number": "C503B-RAN", "quantity": 1, "unit_cost_usd": 1.00},
        {"part": "photodiode (Si)", "vendor": "Hamamatsu / Vishay", "part_number": "S1133", "quantity": 1, "unit_cost_usd": 8.00},
        {"part": "transimpedance amplifier", "vendor": "TI", "part_number": "OPA192", "quantity": 1, "unit_cost_usd": 4.00},
        {"part": "16-bit ADC", "vendor": "TI", "part_number": "ADS1115", "quantity": 1, "unit_cost_usd": 12.00},
        {"part": "3D-printed flow cell with 1 cm path length", "vendor": "self-printed", "part_number": "PETG", "quantity": 1, "unit_cost_usd": 5.00},
        {"part": "clear glass / acrylic windows", "vendor": "any", "part_number": "10 mm cover slides", "quantity": 2, "unit_cost_usd": 4.00},
        {"part": "tubing fittings 1/16 inch", "vendor": "IDEX", "part_number": "P-200X / P-201X", "quantity": 2, "unit_cost_usd": 12.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 30.00},
    ],
    build_difficulty="hobbyist",
    estimated_cost_usd=120,
    validated_performance=None,
    related_corpus_entries=["chibio-bioreactor", "evolver-klavins"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Hamamatsu S1133 photodiode datasheet",
        "TI ADS1115 datasheet",
    ],
    notes="Stub entry. Architectural target: in-line OD sensor at sub-$150 BOM, replacing $1k–$3k commercial probes. Lock-in detection (LED modulated at ~1 kHz, ADC sampled in phase) substantially improves SNR over direct DC measurement. Suitable for bioreactor cell density 0.1–4.0 OD600 range.",
    draft=True,
)


with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new instruments to {OUT}")

# Stub directories
for e in ENTRIES:
    base = Path(__file__).parent / "instruments" / e["id"]
    for sub in ["hardware", "firmware", "docs"]:
        d = base / sub
        d.mkdir(parents=True, exist_ok=True)
        (d / ".gitkeep").touch()
