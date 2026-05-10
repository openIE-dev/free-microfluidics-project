#!/usr/bin/env python3
"""Sixth expansion of control instruments."""
import json
from pathlib import Path

OUT = Path(__file__).parent / "instruments.jsonl"
ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("last_updated", "2026-05-09")
    ENTRIES.append(kw)


add(
    id="open-smartphone-microscope-adapter",
    canonical_name="Open smartphone-microscope adapter for chip imaging",
    aliases=["smartphone microscope adapter"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware/software MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Phone-clip microscope adapter providing 10×–100× imaging of microfluidic chips through smartphone camera. Includes LED illumination, objective lens mount, and chip holder. Direct open-source replacement for commercial smartphone-microscope kits in the $100–$500 range.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-smartphone-microscope-adapter/hardware/", "format": "3D-printable mechanical CAD; OnShape parametric model (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-smartphone-microscope-adapter/firmware/", "language": "iOS/Android image-acquisition apps", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "achromatic doublet lens 4× / 10× / 40×", "vendor": "Edmund / Thorlabs / Aliexpress", "part_number": "AC127-019 (4×)", "quantity": 1, "unit_cost_usd": 30.00},
        {"part": "alternative: ball lens (lensless / cheap)", "vendor": "Aliexpress / Edmund", "part_number": "1 mm sapphire ball", "quantity": 1, "unit_cost_usd": 5.00},
        {"part": "white LED with diffuser", "vendor": "any", "part_number": "5050 SMD LED + diffuser", "quantity": 1, "unit_cost_usd": 3.00},
        {"part": "AAA battery holder + switch", "vendor": "any", "part_number": "2× AAA holder", "quantity": 1, "unit_cost_usd": 3.00},
        {"part": "3D-printed phone clip + lens housing + chip stage", "vendor": "self-printed", "part_number": "PETG 100 g", "quantity": 1, "unit_cost_usd": 5.00},
        {"part": "magnet attachment for chip holder", "vendor": "any", "part_number": "neodymium 6 mm × 2 mm", "quantity": 4, "unit_cost_usd": 4.00},
    ],
    build_difficulty="hobbyist",
    estimated_cost_usd=50,
    validated_performance=None,
    related_corpus_entries=["ozcan-2010-smartphone-microscopy", "kanakasabapathy-shafiee-2017-cellphone-fertility", "openflexure-microscope"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Ozcan group / UCLA smartphone microscopy publications",
        "OpenFlexure community design contributions",
    ],
    notes="Stub entry. Architectural target: smartphone-microscope adapter at sub-$50 BOM. Suitable for paper-microfluidic colorimetric assay readout, chip-imaging educational use, and field-deployable microfluidic POC inspection. Not a substitute for full microscopy; aims for 10–100× imaging of chip-scale features sufficient for most diagnostic readouts.",
    draft=True,
)

add(
    id="open-mppc-photon-counter",
    canonical_name="Open multi-pixel photon counter (MPPC / SiPM) for low-light chip detection",
    aliases=["open SiPM detector", "open photon counter"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Single-channel photon-counting detector using silicon photomultiplier (MPPC/SiPM) for low-light fluorescence and chemiluminescence detection on chip. Counts individual photons, suitable for very-low-concentration sample detection. Direct open-source alternative to PMT-based photon counters at fraction of cost.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-mppc-photon-counter/hardware/", "format": "KiCad project + 3D-printed light-tight housing (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-mppc-photon-counter/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 microcontroller", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "Hamamatsu MPPC module", "vendor": "Hamamatsu", "part_number": "S13360-3050CS", "quantity": 1, "unit_cost_usd": 100.00},
        {"part": "high-speed comparator", "vendor": "TI", "part_number": "TLV3501", "quantity": 1, "unit_cost_usd": 4.00},
        {"part": "fast counter / FPGA shim", "vendor": "any", "part_number": "iCE40-LP1K", "quantity": 1, "unit_cost_usd": 12.00},
        {"part": "high-voltage bias supply for MPPC", "vendor": "discrete + boost converter", "part_number": "MAX1771-class boost", "quantity": 1, "unit_cost_usd": 8.00},
        {"part": "3D-printed light-tight housing", "vendor": "self-printed", "part_number": "PETG, blackened interior", "quantity": 1, "unit_cost_usd": 10.00},
        {"part": "fiber optic + chip coupling", "vendor": "Thorlabs", "part_number": "200 µm core fiber + SMA905", "quantity": 1, "unit_cost_usd": 50.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 40.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=250,
    validated_performance=None,
    related_corpus_entries=["rissin-2010-quanterix-simoa", "todd-singulex-erenna-2006", "open-fluorescence-detector-pmt"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Hamamatsu S13360 MPPC datasheet",
    ],
    notes="Stub entry. Architectural target: single-photon counter at sub-$300 BOM. SiPM detectors offer photon-counting capability at much lower cost than PMTs (~$10k vs $100), with the trade-off of higher dark count rate and slightly worse single-photon resolution. Suitable for chemiluminescence detection (PCR, ELISA), low-fluorophore detection, and any application where photon-counting (rather than current-mode) sensitivity is required.",
    draft=True,
)

add(
    id="open-isothermal-amp-controller",
    canonical_name="Open isothermal amplification controller (LAMP / RPA / NEAR cartridge driver)",
    aliases=["open LAMP controller", "open isothermal NAAT controller"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="thermal-cycler",
    purpose="Single-temperature isothermal amplification controller driving 16 reaction wells at constant 37–65 °C with integrated fluorescence or colorimetric readout. Direct open-source replacement for $1k–$3k commercial isothermal amplification readers. Suitable for LAMP, RPA, NEAR, and other isothermal NAAT chemistries.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-isothermal-amp-controller/hardware/", "format": "KiCad project + machined heat block (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-isothermal-amp-controller/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 microcontroller", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "MAX31865 RTD amplifier", "vendor": "Adafruit", "part_number": "MAX31865", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "PT100 RTD sensor", "vendor": "any", "part_number": "PT100 class A", "quantity": 1, "unit_cost_usd": 8.00},
        {"part": "TEC1-12706 Peltier (or resistive heater)", "vendor": "any", "part_number": "TEC1-12706", "quantity": 1, "unit_cost_usd": 10.00},
        {"part": "VNH5019 H-bridge", "vendor": "Pololu", "part_number": "VNH5019", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "machined aluminum heat block (16-well 0.2 mL)", "vendor": "machined", "part_number": "16-well custom", "quantity": 1, "unit_cost_usd": 50.00},
        {"part": "RGB LED + photodiode array (16-well fluorescence)", "vendor": "Adafruit / Hamamatsu", "part_number": "S1133 + 470 nm LED", "quantity": 16, "unit_cost_usd": 80.00},
        {"part": "12V 5A PSU", "vendor": "any", "part_number": "12V/5A", "quantity": 1, "unit_cost_usd": 20.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 50.00},
    ],
    build_difficulty="intermediate",
    estimated_cost_usd=300,
    validated_performance=None,
    related_corpus_entries=["notomi-2000-loop-mediated-isothermal", "rolando-recombinase-polymerase-amplification", "lucira-home-covid-test", "cue-health-cartridge"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Notomi et al. 2000 Nucleic Acids Res. 28, e63 (LAMP)",
        "Piepenburg et al. 2006 PLOS Biol. 4, e204 (RPA)",
    ],
    notes="Stub entry. Architectural target: isothermal NAAT cartridge reader at sub-$300 BOM. The single-temperature requirement greatly simplifies the controller compared to PCR thermal cyclers. Suitable for academic research on isothermal-NAAT cartridges, agricultural-pathogen detection, and field-deployable molecular diagnostics where PCR thermal cycling is impractical.",
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
