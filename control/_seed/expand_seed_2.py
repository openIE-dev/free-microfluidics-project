#!/usr/bin/env python3
"""Second expansion of control instruments."""
import json
from pathlib import Path

OUT = Path(__file__).parent / "instruments.jsonl"
ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("last_updated", "2026-05-09")
    ENTRIES.append(kw)


add(
    id="open-potentiostat-dstat-derivative",
    canonical_name="Open potentiostat (DStat-class)",
    aliases=["DStat", "Rodeostat"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CERN-OHL-P; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Open electrochemistry potentiostat for on-chip electrochemical detection. Supports cyclic voltammetry, chronoamperometry, square-wave voltammetry, and EIS at sub-nA current resolution. Direct open-source replacement for instruments in the $5k–$15k commercial range.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-potentiostat-dstat-derivative/hardware/", "format": "KiCad project (placeholder)", "license": "CERN-OHL-P"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-potentiostat-dstat-derivative/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32G474 microcontroller", "vendor": "ST/Mouser", "part_number": "STM32G474RE", "quantity": 1, "unit_cost_usd": 9.00},
        {"part": "ADS1256 ADC", "vendor": "TI", "part_number": "ADS1256", "quantity": 1, "unit_cost_usd": 18.00},
        {"part": "DAC8550 16-bit DAC", "vendor": "TI", "part_number": "DAC8550", "quantity": 1, "unit_cost_usd": 12.00},
        {"part": "OPA192 chopper-stabilized op-amp", "vendor": "TI", "part_number": "OPA192", "quantity": 4, "unit_cost_usd": 8.00},
        {"part": "RG177BS instrumentation amp", "vendor": "AD", "part_number": "AD8421", "quantity": 1, "unit_cost_usd": 12.00},
        {"part": "USB isolator", "vendor": "Adafruit", "part_number": "ISO7041", "quantity": 1, "unit_cost_usd": 30.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 60.00},
        {"part": "BNC connectors for electrodes", "vendor": "any", "part_number": "BNC PCB-mount", "quantity": 4, "unit_cost_usd": 12.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=300,
    validated_performance=None,
    related_corpus_entries=["genmark-eplex-cartridge", "rothberg-2011-ion-torrent"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation="Dryden, Wheeler 2015 PLOS ONE 10, e0140349 (DStat reference)",
    sources=[
        "Dryden, M. D. M.; Wheeler, A. R. DStat: a versatile, open-source potentiostat for electroanalysis and integration. PLOS ONE 2015, 10, e0140349",
        "https://github.com/IorodeoLLC/rodeostat",
    ],
    notes="Stub entry. Architectural target: production-grade potentiostat at sub-$300 BOM. Particularly relevant for on-chip electrochemical sensing (Ion Torrent, GenMark eSensor, glucose biosensors) where commercial instruments are overkill for prototype development.",
    draft=True,
)

add(
    id="open-fluorescence-detector-pmt",
    canonical_name="Open fluorescence detector (PMT-amplifier + LED excitation)",
    aliases=["open fluorescence detector", "PMT amplifier"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CERN-OHL-P; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Single-channel fluorescence detector with LED excitation, optical filter set, photomultiplier tube, transimpedance amplifier, and ADC. Suitable for on-chip droplet detection, real-time PCR fluorescence monitoring, and capillary electrophoresis fluorescence detection.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-fluorescence-detector-pmt/hardware/", "format": "KiCad project + 3D-printed optical mount (placeholder)", "license": "CERN-OHL-P"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-fluorescence-detector-pmt/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 microcontroller", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "Hamamatsu PMT module", "vendor": "Hamamatsu", "part_number": "H10720-110", "quantity": 1, "unit_cost_usd": 350.00},
        {"part": "transimpedance amplifier (LF356)", "vendor": "TI", "part_number": "LF356", "quantity": 1, "unit_cost_usd": 4.00},
        {"part": "LED 470 nm + driver", "vendor": "Cree / Thorlabs", "part_number": "M470L4", "quantity": 1, "unit_cost_usd": 80.00},
        {"part": "excitation filter (480/30)", "vendor": "Chroma / Semrock", "part_number": "ET480/30x", "quantity": 1, "unit_cost_usd": 60.00},
        {"part": "emission filter (535/40)", "vendor": "Chroma", "part_number": "ET535/40m", "quantity": 1, "unit_cost_usd": 60.00},
        {"part": "dichroic mirror", "vendor": "Chroma", "part_number": "T505lpxr", "quantity": 1, "unit_cost_usd": 50.00},
        {"part": "achromatic doublet lens 25 mm", "vendor": "Thorlabs", "part_number": "AC254-040", "quantity": 2, "unit_cost_usd": 80.00},
        {"part": "3D-printed mechanical housing", "vendor": "self-printed", "part_number": "PETG", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "12V power supply", "vendor": "any", "part_number": "12V/2A", "quantity": 1, "unit_cost_usd": 12.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=750,
    validated_performance=None,
    related_corpus_entries=["macosko-2015-drop-seq", "bio-rad-qx-ddpcr-system"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Hamamatsu H10720 datasheet",
        "Thorlabs cage-system documentation",
    ],
    notes="Stub entry. Architectural target: GFP-class fluorescence detector at sub-$1000 BOM, replacing $5k–$10k commercial instruments. PMT + filter set are the dominant cost; CMOS-camera-based alternative would reduce cost ~3× at the expense of single-photon sensitivity.",
    draft=True,
)

add(
    id="open-imaging-stage-xyz",
    canonical_name="Open imaging XYZ stage for chip imaging",
    aliases=["open imaging stage"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CERN-OHL-P; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Three-axis motorized stage for systematic imaging of microfluidic chips with travel range 50 × 50 × 25 mm and step resolution 1 µm. Enables tiled bright-field / fluorescence imaging of chip arrays without manual position adjustment.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-imaging-stage-xyz/hardware/", "format": "KiCad + 3D-printable + machined parts (placeholder)", "license": "CERN-OHL-P"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-imaging-stage-xyz/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 microcontroller", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "TMC2209 stepper drivers", "vendor": "Trinamic", "part_number": "TMC2209", "quantity": 3, "unit_cost_usd": 24.00},
        {"part": "NEMA 11 stepper motors", "vendor": "any", "part_number": "11HS18-0674S", "quantity": 3, "unit_cost_usd": 60.00},
        {"part": "linear rails + carriages 50 mm", "vendor": "any", "part_number": "MGN9 50mm", "quantity": 6, "unit_cost_usd": 75.00},
        {"part": "8 mm leadscrews + nuts", "vendor": "any", "part_number": "200 mm", "quantity": 3, "unit_cost_usd": 36.00},
        {"part": "3D-printed structural parts", "vendor": "self-printed", "part_number": "PETG 300 g", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "limit switches", "vendor": "any", "part_number": "mechanical", "quantity": 6, "unit_cost_usd": 8.00},
        {"part": "12V 5A PSU", "vendor": "any", "part_number": "12V/5A", "quantity": 1, "unit_cost_usd": 20.00},
    ],
    build_difficulty="intermediate",
    estimated_cost_usd=250,
    validated_performance=None,
    related_corpus_entries=["openflexure-microscope", "squid-microscope"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Sharkey et al. 2016 Rev. Sci. Instrum. 87, 025104 (OpenFlexure stage)",
        "Trinamic TMC2209 datasheet",
    ],
    notes="Stub entry. Architectural target: open-source XYZ stage for chip imaging at sub-$250 BOM. Designed for rigid coupling to a SmartPhone or USB camera; suitable as base for OpenFlexure-style microscopes or as positioning system for chip-imaging robots.",
    draft=True,
)

add(
    id="open-temperature-controller-pid",
    canonical_name="Open generic temperature controller (PID, Peltier or resistive)",
    aliases=["open temperature controller"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CERN-OHL-P; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Generic temperature controller for microfluidic applications: PID control of Peltier or resistive heater elements with 0.1 °C resolution and ±0.5 °C accuracy at setpoint. 4 channels independent. Suitable for on-chip incubation, PCR, organ-on-chip, and cell culture.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-temperature-controller-pid/hardware/", "format": "KiCad project (placeholder)", "license": "CERN-OHL-P"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-temperature-controller-pid/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 microcontroller", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "MAX31865 RTD amplifier", "vendor": "Adafruit", "part_number": "MAX31865", "quantity": 4, "unit_cost_usd": 60.00},
        {"part": "PT100 RTD sensors", "vendor": "any", "part_number": "1/8 inch class A", "quantity": 4, "unit_cost_usd": 32.00},
        {"part": "VNH5019 H-bridge", "vendor": "Pololu", "part_number": "VNH5019", "quantity": 4, "unit_cost_usd": 60.00},
        {"part": "Peltier modules TEC1-12706", "vendor": "any", "part_number": "TEC1-12706", "quantity": 4, "unit_cost_usd": 40.00},
        {"part": "12V 10A PSU", "vendor": "any", "part_number": "12V/10A", "quantity": 1, "unit_cost_usd": 25.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 50.00},
        {"part": "OLED display + encoder", "vendor": "any", "part_number": "SSD1306 + EC11", "quantity": 1, "unit_cost_usd": 12.00},
    ],
    build_difficulty="intermediate",
    estimated_cost_usd=300,
    validated_performance=None,
    related_corpus_entries=["openpcr-thermal-cycler", "huh-2010-lung-on-chip"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "MAX31865 datasheet",
        "Pololu VNH5019 datasheet",
    ],
    notes="Stub entry. Architectural target: 4-channel PID temperature controller at sub-$300 BOM, replacing single-channel commercial controllers in the $500–$2000 range. Useful as a generic substrate for any microfluidic application with thermal regulation needs.",
    draft=True,
)

add(
    id="open-pressure-regulator-proportional",
    canonical_name="Open proportional pressure regulator",
    aliases=["open pressure regulator"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CERN-OHL-P; firmware MIT; docs CC0-1.0.",
    instrument_class="pressure-controller",
    purpose="2-channel proportional pressure regulator providing closed-loop pressure control 0–3 bar with ±5 mbar accuracy. Drives compressed-air or compressed-N2 supply through proportional solenoid valves to deliver controlled pressure to fluidic reservoirs.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-pressure-regulator-proportional/hardware/", "format": "KiCad + manifold mechanical CAD (placeholder)", "license": "CERN-OHL-P"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-pressure-regulator-proportional/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 microcontroller", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "proportional solenoid valves", "vendor": "ASCO/Festo/SMC", "part_number": "ASCO 202G02 or equivalent", "quantity": 2, "unit_cost_usd": 200.00},
        {"part": "pressure sensors 0-3 bar", "vendor": "Honeywell", "part_number": "HSCMRRD030PA2A3", "quantity": 2, "unit_cost_usd": 80.00},
        {"part": "PWM driver MOSFETs", "vendor": "any", "part_number": "IRLZ44N", "quantity": 2, "unit_cost_usd": 4.00},
        {"part": "manifold block (machined aluminum)", "vendor": "machined", "part_number": "2-channel custom", "quantity": 1, "unit_cost_usd": 80.00},
        {"part": "compressed-air filter regulator (input)", "vendor": "SMC", "part_number": "AC30-03DG", "quantity": 1, "unit_cost_usd": 60.00},
        {"part": "PTFE/PEEK tubing 1/16 OD", "vendor": "IDEX", "part_number": "1/16 OD", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 40.00},
        {"part": "12V 2A PSU", "vendor": "any", "part_number": "12V/2A", "quantity": 1, "unit_cost_usd": 12.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=600,
    validated_performance=None,
    related_corpus_entries=["elveflow-ob1-pressure-controller", "dolomite-microfluidics-platform"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "ASCO 202G02 proportional valve datasheet",
        "Honeywell HSCMRRD030PA2A3 datasheet",
    ],
    notes="Stub entry. Architectural target: 2-channel proportional pressure controller at sub-$600 BOM. The dual-channel-pressure-controller-stm32 entry is the higher-precision close-loop version of this; this entry is the simpler proportional-valve-driven baseline.",
    draft=True,
)


with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new instruments to {OUT}")

# Create stub directories
import os
for e in ENTRIES:
    base = Path(__file__).parent / "instruments" / e["id"]
    for sub in ["hardware", "firmware", "docs"]:
        d = base / sub
        d.mkdir(parents=True, exist_ok=True)
        (d / ".gitkeep").touch()
