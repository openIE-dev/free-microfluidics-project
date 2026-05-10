#!/usr/bin/env python3
"""Fourth expansion of control instruments: flow sensor, spectrometer, lock-in, vacuum source."""
import json
from pathlib import Path

OUT = Path(__file__).parent / "instruments.jsonl"
ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("last_updated", "2026-05-09")
    ENTRIES.append(kw)


add(
    id="open-thermal-mass-flow-sensor",
    canonical_name="Open thermal mass flow sensor (Sensirion-class)",
    aliases=["open flow sensor"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="In-line thermal mass flow sensor for liquid microfluidic applications. Measures flow rates 1 µL/min to 50 mL/min via temperature-difference detection across a heated central element. Suitable as feedback sensor for closed-loop syringe-pump or pressure-controller systems.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-thermal-mass-flow-sensor/hardware/", "format": "KiCad project + 3D-printed flow-cell housing (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-thermal-mass-flow-sensor/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 microcontroller", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "Sensirion SLF3S-1300F flow sensor (commercial baseline)", "vendor": "Sensirion", "part_number": "SLF3S-1300F", "quantity": 1, "unit_cost_usd": 250.00},
        {"part": "alternative: thermistor pairs + heater wire (DIY thermal flow sensor)", "vendor": "any", "part_number": "10kΩ NTC + Kanthal heater", "quantity": 1, "unit_cost_usd": 5.00},
        {"part": "MAX31865 RTD amplifier (for DIY route)", "vendor": "Adafruit", "part_number": "MAX31865", "quantity": 2, "unit_cost_usd": 30.00},
        {"part": "3D-printed flow-cell housing", "vendor": "self-printed", "part_number": "PETG", "quantity": 1, "unit_cost_usd": 5.00},
        {"part": "1/16 inch tubing fittings", "vendor": "IDEX", "part_number": "P-201X", "quantity": 2, "unit_cost_usd": 12.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 30.00},
        {"part": "USB cable + power", "vendor": "any", "part_number": "USB-C", "quantity": 1, "unit_cost_usd": 5.00},
    ],
    build_difficulty="intermediate",
    estimated_cost_usd=350,
    validated_performance=None,
    related_corpus_entries=["dual-channel-pressure-controller-stm32", "elveflow-ob1-pressure-controller"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Sensirion SLF3S-1300F datasheet",
        "Lammerink et al. 1993 Sens. Actuators A 37–38, 45–50 (thermal flow-sensor foundation)",
    ],
    notes="Stub entry. Architectural target: in-line liquid flow sensor at sub-$350 BOM. Two configurations: (1) wrapper around Sensirion SLF3S-class commercial sensor for proven accuracy; (2) DIY thermistor-pair design for ~$50 BOM at reduced accuracy. Both useful as feedback sensors for closed-loop pumping.",
    draft=True,
)

add(
    id="open-uv-vis-spectrometer-cmos",
    canonical_name="Open UV-Vis spectrometer (CMOS-based, transmission)",
    aliases=["open spectrometer"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Open-source visible spectrometer (400–700 nm) using a CMOS line sensor and reflective grating. Suitable for in-line absorbance / transmission measurements on microfluidic chips, e.g., enzyme kinetics, protein quantification, dye assays. Direct open-source replacement for commercial benchtop spectrometers in the $2k–$10k range.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-uv-vis-spectrometer-cmos/hardware/", "format": "KiCad project + 3D-printed optical mount (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-uv-vis-spectrometer-cmos/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 microcontroller", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "TCD1304 linear CCD", "vendor": "Toshiba", "part_number": "TCD1304", "quantity": 1, "unit_cost_usd": 25.00},
        {"part": "alternative: Hamamatsu C12880MA mini-spectrometer", "vendor": "Hamamatsu", "part_number": "C12880MA", "quantity": 1, "unit_cost_usd": 220.00},
        {"part": "halogen broadband source", "vendor": "any", "part_number": "12V 20W halogen", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "blazed reflective grating", "vendor": "Thorlabs / Edmund", "part_number": "GR50-1850 (1800 lines/mm)", "quantity": 1, "unit_cost_usd": 60.00},
        {"part": "fiber-coupled flow cell, 1 cm path length", "vendor": "self-fabricated", "part_number": "PETG + 200 µm core fiber", "quantity": 1, "unit_cost_usd": 40.00},
        {"part": "3D-printed optical bench", "vendor": "self-printed", "part_number": "PETG, blackened interior", "quantity": 1, "unit_cost_usd": 25.00},
        {"part": "12V 2A PSU", "vendor": "any", "part_number": "12V/2A", "quantity": 1, "unit_cost_usd": 12.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 40.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=400,
    validated_performance=None,
    related_corpus_entries=["abbott-piccolo-xpress"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Hamamatsu C12880MA datasheet",
        "Toshiba TCD1304 datasheet",
        "Public Lab DIY spectrometer projects (https://publiclab.org/wiki/spectrometer)",
    ],
    notes="Stub entry. Architectural target: visible-range spectrometer at sub-$400 BOM, replacing $2k–$10k commercial instruments. Two configurations: (1) Hamamatsu C12880MA pre-aligned mini-spectrometer for ease of build; (2) DIY grating + linear CCD for educational and ultra-low-cost work. Useful for inline absorbance measurement on microfluidic chips.",
    draft=True,
)

add(
    id="open-lock-in-amplifier",
    canonical_name="Open lock-in amplifier (general-purpose for chip detection)",
    aliases=["open lock-in"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Two-channel digital lock-in amplifier for detecting weak periodic signals from PMT, photodiode, or electrochemical sensors. Reference frequency 100 Hz to 100 kHz, output bandwidth 0.1 Hz to 100 Hz. Direct open-source replacement for commercial lock-in amplifiers in the $5k–$15k range.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-lock-in-amplifier/hardware/", "format": "KiCad project (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-lock-in-amplifier/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32H743 microcontroller (high-perf)", "vendor": "ST/Mouser", "part_number": "STM32H743VIT6", "quantity": 1, "unit_cost_usd": 18.00},
        {"part": "ADS1675 or AD7768 high-resolution ADC", "vendor": "TI/AD", "part_number": "AD7768-1", "quantity": 2, "unit_cost_usd": 40.00},
        {"part": "AD9833 DDS function generator (for reference)", "vendor": "AD", "part_number": "AD9833", "quantity": 1, "unit_cost_usd": 12.00},
        {"part": "OPA192 chopper-stabilized op-amps", "vendor": "TI", "part_number": "OPA192", "quantity": 4, "unit_cost_usd": 8.00},
        {"part": "USB-C interface + isolator", "vendor": "Adafruit", "part_number": "ISO7041", "quantity": 1, "unit_cost_usd": 30.00},
        {"part": "BNC connectors", "vendor": "any", "part_number": "PCB-mount BNC", "quantity": 4, "unit_cost_usd": 12.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "4-layer, careful grounding", "quantity": 1, "unit_cost_usd": 80.00},
        {"part": "shielded enclosure", "vendor": "Hammond", "part_number": "die-cast aluminum", "quantity": 1, "unit_cost_usd": 30.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=350,
    validated_performance=None,
    related_corpus_entries=["open-fluorescence-detector-pmt"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation="various — Stanford Research Systems SR830 reference",
    sources=[
        "Stanford Research Systems SR830 reference",
        "ZurichInstruments MFLI documentation (commercial benchmark)",
    ],
    notes="Stub entry. Architectural target: digital dual-channel lock-in amplifier at sub-$400 BOM, replacing $5k–$15k commercial lock-ins. Useful for any microfluidic application with weak periodic signal: chopped-LED fluorescence, modulated-photodiode detection, AC-impedance electrochemistry. The grounding and shielding requirements are the dominant build challenge.",
    draft=True,
)

add(
    id="open-multi-channel-vacuum-source",
    canonical_name="Open multi-channel vacuum/pressure source (4-channel, ±1 bar)",
    aliases=["open vacuum source"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="pressure-controller",
    purpose="4-channel programmable bipolar pressure source providing ±1 bar (positive or negative) per channel for pneumatic chip control. Suitable for driving Quake-style valve-bank chips, organ-on-chip vacuum-driven mechanical strain, and pressure-driven flow with integrated vacuum capability for priming.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-multi-channel-vacuum-source/hardware/", "format": "KiCad + manifold mechanical CAD (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-multi-channel-vacuum-source/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 microcontroller", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "miniature diaphragm pumps (vacuum + pressure)", "vendor": "Parker / KNF", "part_number": "KNF UNMP", "quantity": 2, "unit_cost_usd": 200.00},
        {"part": "3-way solenoid valves (channel routing)", "vendor": "any", "part_number": "miniature 3-way 12V", "quantity": 4, "unit_cost_usd": 60.00},
        {"part": "pressure sensors (±1 bar bidirectional)", "vendor": "Honeywell", "part_number": "HSCDRRD001PD2A3", "quantity": 4, "unit_cost_usd": 160.00},
        {"part": "PWM driver MOSFETs", "vendor": "any", "part_number": "IRLZ44N", "quantity": 8, "unit_cost_usd": 16.00},
        {"part": "manifold block (machined aluminum)", "vendor": "machined", "part_number": "4-channel custom", "quantity": 1, "unit_cost_usd": 120.00},
        {"part": "tubing and fittings", "vendor": "IDEX", "part_number": "1/16 inch", "quantity": 1, "unit_cost_usd": 30.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 50.00},
        {"part": "12V 2A PSU", "vendor": "any", "part_number": "12V/2A", "quantity": 1, "unit_cost_usd": 12.00},
    ],
    build_difficulty="intermediate",
    estimated_cost_usd=700,
    validated_performance=None,
    related_corpus_entries=["unger-2000-quake-monolithic-membrane-valve", "huh-2010-lung-on-chip", "open-pneumatic-valve-bank-controller"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Honeywell HSCDRRD001PD2A3 datasheet",
        "KNF UNMP miniature pump datasheet",
    ],
    notes="Stub entry. Architectural target: bipolar pressure source at sub-$700 BOM, replacing $3k–$8k commercial systems (Elveflow OB1, Fluigent MFCS). Vacuum capability is the differentiator from positive-only pressure controllers and is essential for priming chips and for vacuum-driven organ-on-chip mechanical actuation.",
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
