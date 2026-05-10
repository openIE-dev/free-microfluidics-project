#!/usr/bin/env python3
"""Fifth expansion of control instruments."""
import json
from pathlib import Path

OUT = Path(__file__).parent / "instruments.jsonl"
ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("last_updated", "2026-05-09")
    ENTRIES.append(kw)


add(
    id="open-coulter-counter",
    canonical_name="Open Coulter counter (electrical impedance cell counter)",
    aliases=["open Coulter", "DIY Coulter counter"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Open-source electrical impedance counter ('Coulter counter'): cells passing through a microfluidic constriction modulate impedance between two electrodes, generating a count + size measurement per cell. Suitable for cell counting, blood differential analysis, and particle-size distribution. Replaces commercial bench Coulter counters in the $5k–$30k range.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-coulter-counter/hardware/", "format": "KiCad project + microfluidic chip flow cell (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-coulter-counter/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32G474 microcontroller", "vendor": "ST/Mouser", "part_number": "STM32G474RE", "quantity": 1, "unit_cost_usd": 9.00},
        {"part": "AD9833 DDS function generator", "vendor": "AD", "part_number": "AD9833", "quantity": 1, "unit_cost_usd": 12.00},
        {"part": "lock-in amplifier IC (or discrete via OPA192 + ADC)", "vendor": "TI/AD", "part_number": "AD630 or discrete", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "instrumentation amplifier", "vendor": "AD", "part_number": "AD8421", "quantity": 1, "unit_cost_usd": 12.00},
        {"part": "16-bit ADC", "vendor": "TI", "part_number": "ADS8688", "quantity": 1, "unit_cost_usd": 25.00},
        {"part": "Pt or Au electrode pair (or DIY platinum wire)", "vendor": "Sigma / Goodfellow", "part_number": "Pt wire 100 µm", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "microfluidic chip with constriction (PDMS or thermoplastic)", "vendor": "self-fab", "part_number": "30 µm × 30 µm × 100 µm constriction", "quantity": 1, "unit_cost_usd": 5.00},
        {"part": "syringe pump (open syringe pump entry recommended)", "vendor": "self-built", "part_number": "see open-syringe-pump entry", "quantity": 1, "unit_cost_usd": 120.00},
        {"part": "custom PCB with shielded analog front-end", "vendor": "JLCPCB", "part_number": "4-layer", "quantity": 1, "unit_cost_usd": 60.00},
        {"part": "USB-C interface", "vendor": "any", "part_number": "USB-C connector", "quantity": 1, "unit_cost_usd": 5.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=400,
    validated_performance=None,
    related_corpus_entries=["sysmex-cbc-cartridge", "biorad-nanocoulter-bead-counter"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline"],
    related_cad_designs=[],
    publication_citation="Coulter 1953 patent US2656508 (foundational); Sun & Morgan 2010 review",
    sources=[
        "Coulter, W. H. Means for counting particles suspended in a fluid. US2656508, 1953",
        "Sun, T.; Morgan, H. Single-cell microfluidic impedance cytometry: a review. Microfluid. Nanofluidics 2010, 8, 423–443",
    ],
    notes="Stub entry. Architectural target: open Coulter counter at sub-$400 BOM. Combines microfluidic constriction (the chip), pumping (separate open syringe pump entry), and electronics. Useful for cell counting, blood cell differential, and any particle-size-distribution measurement up to ~10 µm. Higher-frequency multi-frequency variants enable some discrimination of cell type beyond just size.",
    draft=True,
)

add(
    id="open-droplet-generator-controller",
    canonical_name="Open droplet generator pressure controller (for ddPCR / droplet single-cell)",
    aliases=["open droplet controller", "DIY ddPCR controller"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="pressure-controller",
    purpose="Three-channel pressure controller specifically configured for droplet microfluidic chip operation: independent control of cell suspension, bead suspension, and oil pressure inputs at sub-mbar precision over 0–500 mbar range. Suitable for Drop-seq, inDrops-style single-cell encapsulation and ddPCR-style droplet generation.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-droplet-generator-controller/hardware/", "format": "KiCad project + manifold + reservoir mounting (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-droplet-generator-controller/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 microcontroller", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "proportional pressure regulators", "vendor": "SMC / Festo", "part_number": "ITV-0021-3BL or equivalent", "quantity": 3, "unit_cost_usd": 600.00},
        {"part": "Honeywell pressure sensors 0–500 mbar", "vendor": "Honeywell", "part_number": "HSCMRRD500MD2A3", "quantity": 3, "unit_cost_usd": 240.00},
        {"part": "12-bit DAC for setpoint", "vendor": "TI", "part_number": "MCP4728", "quantity": 1, "unit_cost_usd": 5.00},
        {"part": "machined aluminum reservoir mount", "vendor": "machined", "part_number": "3-port custom; chip-pneumatic interface", "quantity": 1, "unit_cost_usd": 100.00},
        {"part": "pneumatic input filter regulator", "vendor": "SMC", "part_number": "AC30-03DG", "quantity": 1, "unit_cost_usd": 60.00},
        {"part": "PEEK tubing 1/16 OD + fittings", "vendor": "IDEX", "part_number": "1/16 OD", "quantity": 1, "unit_cost_usd": 30.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 50.00},
        {"part": "12V 2A PSU", "vendor": "any", "part_number": "12V/2A", "quantity": 1, "unit_cost_usd": 12.00},
    ],
    build_difficulty="professional",
    estimated_cost_usd=1200,
    validated_performance=None,
    related_corpus_entries=["macosko-2015-drop-seq", "klein-2015-indrops", "10x-genomics-chromium-controller", "bio-rad-qx-ddpcr-system"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline"],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "SMC ITV proportional regulator datasheet",
        "Honeywell HSCMRRD500MD2A3 datasheet",
    ],
    notes="Stub entry. Architectural target: dedicated droplet-generator controller at sub-$1200 BOM, replacing commercial Elveflow OB1 / Fluigent MFCS in the $5k–$10k range. The three-channel architecture matches the typical Drop-seq chip layout (cells / beads / oil). For finer pressure control, replace proportional regulators with closed-loop feedback servovalves at additional cost.",
    draft=True,
)

add(
    id="open-microscope-incubator",
    canonical_name="Open stage-top incubator for chip microscopy",
    aliases=["open stage incubator"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="mixed",
    license_notes="Hardware CC0-1.0; firmware MIT; docs CC0-1.0.",
    instrument_class="other",
    purpose="Stage-top incubator for live-cell microscopy on microfluidic chips: maintains 37 °C ± 0.1 °C, 5% CO2, and 95% humidity over a stage-mounted chip. Direct open-source replacement for commercial stage-top incubators in the $5k–$15k range.",
    hardware_artifacts=[
        {"path_or_url": "instruments/open-microscope-incubator/hardware/", "format": "KiCad + 3D-printed enclosure (placeholder)", "license": "CC0-1.0"},
    ],
    firmware_artifacts=[
        {"path_or_url": "instruments/open-microscope-incubator/firmware/", "language": "Rust embassy", "license": "MIT"},
    ],
    bill_of_materials=[
        {"part": "STM32F411 microcontroller", "vendor": "WeAct", "part_number": "STM32F411CEU6", "quantity": 1, "unit_cost_usd": 6.00},
        {"part": "PT100 RTD + MAX31865 amplifier", "vendor": "Adafruit", "part_number": "MAX31865 + PT100", "quantity": 2, "unit_cost_usd": 30.00},
        {"part": "CO2 sensor (NDIR)", "vendor": "Sensirion / SCD30", "part_number": "SCD30", "quantity": 1, "unit_cost_usd": 60.00},
        {"part": "humidity sensor", "vendor": "Sensirion", "part_number": "SHT31", "quantity": 1, "unit_cost_usd": 12.00},
        {"part": "transparent ITO heater on glass", "vendor": "any", "part_number": "ITO-coated glass + heater", "quantity": 1, "unit_cost_usd": 30.00},
        {"part": "miniature CO2 valve + premixed CO2 cylinder", "vendor": "industrial gas", "part_number": "5% CO2 in air premix", "quantity": 1, "unit_cost_usd": 100.00},
        {"part": "miniature humidifier (peltier or piezo)", "vendor": "any", "part_number": "ultrasonic humidifier", "quantity": 1, "unit_cost_usd": 25.00},
        {"part": "3D-printed enclosure (transparent for imaging)", "vendor": "self-printed", "part_number": "PETG + acrylic windows", "quantity": 1, "unit_cost_usd": 30.00},
        {"part": "12V 3A PSU", "vendor": "any", "part_number": "12V/3A", "quantity": 1, "unit_cost_usd": 15.00},
        {"part": "custom PCB", "vendor": "JLCPCB", "part_number": "1-off run", "quantity": 1, "unit_cost_usd": 50.00},
    ],
    build_difficulty="intermediate",
    estimated_cost_usd=400,
    validated_performance=None,
    related_corpus_entries=["huh-2010-lung-on-chip", "kim-ingber-2012-gut-on-chip", "ingber-emulate-organ-chip"],
    related_fab_recipes=[],
    related_cad_designs=[],
    publication_citation=None,
    sources=[
        "Sensirion SCD30 datasheet",
        "Adafruit MAX31865 product page",
    ],
    notes="Stub entry. Architectural target: stage-top live-cell-imaging incubator at sub-$400 BOM. Critical for any organ-on-chip or live-cell microfluidics work that requires extended (hours-to-days) imaging on a microscope stage. The transparent ITO heater on glass is the key component allowing imaging through the heated stage without thermal-gradient artifacts.",
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
