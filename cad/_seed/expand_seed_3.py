#!/usr/bin/env python3
"""Third expansion of CAD designs: Quake valve test, mother machine, fluidic logic, ESI emitter."""
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
    id="quake-valve-test-pattern",
    canonical_name="Quake valve test pattern (push-up, 100 µm membrane)",
    aliases=["Quake valve test", "MLSI test pattern"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="valve-component",
    substrate_material="PDMS",
    fabrication_path="Two SU-8 masters: control layer 25 µm tall on rounded photoresist (reflow-rounded SPR-220), flow layer 50 µm rectangular SU-8; bilayer PDMS (5:1 control / 20:1 flow) with thermal bond at 80 °C 1 hr, plasma bond to glass slide",
    channel_geometry="Push-up Quake valve test: 100 µm × 100 µm flow channel (50 µm tall) crossed at 90° by 100 µm × 25 µm rounded control channel. Valve closes when control pressurized to 30 psi. Test pattern includes 8 valves in parallel for closure-pressure characterization.",
    chip_footprint_mm=75,
    cad_files=[
        "designs/quake-valve-test-pattern/control_layer.dxf",
        "designs/quake-valve-test-pattern/flow_layer.dxf",
        "designs/quake-valve-test-pattern/design.gds",
    ],
    cad_format="mixed",
    mask_count=2,
    related_corpus_entries=["unger-2000-quake-monolithic-membrane-valve", "thorsen-2002-microfluidic-large-scale-integration"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "su8-master-baseline"],
    sources=["Unger et al. 2000 Science 288, 113–116"],
    publication_citation="Unger et al. 2000",
    validated_performance=None,
    notes="Stub entry. The canonical Quake-valve test pattern: validates valve closure pressure, response time, and reliability across multiple valves on the same chip. Push-up geometry (control channel below flow channel) is the dominant variant; push-down is the alternative. Rounded control-channel cross-section (achieved by reflowing positive photoresist before SU-8 deposition) is essential for full valve closure.",
    disclosed_subsystems=[
        "valve-quake-pneumatic-membrane",
        "fabrication-pdms-soft-lithography",
        "fabrication-multilayer-lamination",
    ],
)

add(
    id="mother-machine-bacterial-trap-array",
    canonical_name="Mother machine bacterial trap array (Wang/Jun 2010 reference)",
    aliases=["mother machine reference"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="single-cell-platform",
    substrate_material="PDMS",
    fabrication_path="SU-8 master with two-step photolithography: 1.2 µm tall trenches (SU-8 2002 spin coated to ~1.2 µm) + 25 µm tall main flow channel (SU-8 2025); PDMS 10:1 cured 60 min @ 65 °C; plasma bond to glass slide",
    channel_geometry="Main flow channel 100 µm × 25 µm with arrays of perpendicular dead-end trenches 1.2 µm wide × 25 µm long × 1.0 µm tall — sized to hold a single bacterial cell (typ. E. coli 1 µm × 2 µm) at the closed end while excluding subsequent daughter cells via flow",
    chip_footprint_mm=75,
    cad_files=[
        "designs/mother-machine-bacterial-trap-array/trench_layer.dxf",
        "designs/mother-machine-bacterial-trap-array/flow_layer.dxf",
        "designs/mother-machine-bacterial-trap-array/design.gds",
    ],
    cad_format="mixed",
    mask_count=2,
    related_corpus_entries=["ferry-2011-mother-machine"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "su8-master-baseline"],
    sources=["Wang et al. 2010 Curr. Biol. 20, 1099 (mother machine)"],
    publication_citation="Wang et al. 2010",
    validated_performance=None,
    notes="Stub entry. The canonical mother-machine architecture: hundreds of dead-end trenches, each capturing a single bacterium, allowing thousands of independent single-cell lineages to be tracked in parallel under continuous-perfusion nutrient supply. The two-step photolithography (different SU-8 thicknesses for trenches vs main channel) is the key fabrication challenge.",
    disclosed_subsystems=[
        "cell-trap-hydrodynamic",
        "fabrication-pdms-soft-lithography",
        "fabrication-su8-photoresist",
    ],
)

add(
    id="fluidic-not-gate-bubble-logic",
    canonical_name="Fluidic NOT gate (bubble-logic primitive)",
    aliases=["bubble logic NOT gate"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="other",
    substrate_material="PDMS",
    fabrication_path="SU-8 master, 50 µm; PDMS 10:1 cured 60 min @ 65 °C; plasma bond to glass slide",
    channel_geometry="T-junction with asymmetric channel widths (100 µm and 50 µm branches) following Prakash 2007 design: bubble-bias through narrow branch implements logical inversion. Typical implementations include AND/OR/NOT/SR-latch primitives in cascade.",
    chip_footprint_mm=75,
    cad_files=[
        "designs/fluidic-not-gate-bubble-logic/design.dxf",
        "designs/fluidic-not-gate-bubble-logic/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["prakash-2007-bubble-logic", "weaver-2010-microfluidic-large-scale-integration", "goldstein-mueller-1968-fluidic-amplifier"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline"],
    sources=["Prakash & Gershenfeld 2007 Science 315, 832"],
    publication_citation="Prakash & Gershenfeld 2007",
    validated_performance=None,
    notes="Stub entry. The simplest fluidic-logic primitive: an asymmetric T-junction in two-phase flow. Combined with reservoir delay lines and AND/OR primitives, supports Turing-complete fluidic computation as demonstrated by Prakash & Gershenfeld 2007. Architectural cousin of the 1960s Stanford / HDL fluidic-amplifier work at much smaller scale.",
    disclosed_subsystems=[
        "fabrication-pdms-soft-lithography",
    ],
)

add(
    id="esi-emitter-glass-chip",
    canonical_name="Glass chip with integrated ESI emitter (Ramsey reference)",
    aliases=["chip-ESI reference"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_path="HF-etched Borofloat 33 (10 µm × 50 µm separation channel) + drilled top piece; thermal fusion bond at 620 °C; emitter pulled by glass-capillary puller and bonded externally with epoxy",
    channel_geometry="Separation channel 60 mm × 50 µm × 10 µm with cross-injector at upstream end; downstream emitter outlet fed into pulled-glass ESI tip (5 µm OD) bonded in alignment slot",
    chip_footprint_mm=75,
    cad_files=[
        "designs/esi-emitter-glass-chip/design.dxf",
        "designs/esi-emitter-glass-chip/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["ramsey-1996-electrospray-on-chip", "advion-triversa-nanomate", "harrison-1992-cap-electrophoresis-on-chip"],
    related_fab_recipes=["glass-hf-etching-baseline", "glass-glass-thermal-bonding-baseline", "glass-capillary-pulling-baseline"],
    sources=["Ramsey & Ramsey 1997 Anal. Chem. 69, 1174"],
    publication_citation="Ramsey & Ramsey 1997",
    validated_performance=None,
    notes="Stub entry. The canonical chip-ESI architecture: glass CE chip with integrated electrospray emitter. The pulled-glass tip is the dominant emitter style in academic chip-MS work; commercial systems (Advion NanoMate) use silicon-MEMS nozzle arrays. Both architectures coexist in the prior art.",
    disclosed_subsystems=[
        "fabrication-glass-hf-etching",
        "fabrication-glass-thermal-bonding",
        "separation-capillary-electrophoresis",
        "interface-electrospray-emitter",
        "material-borofloat-glass",
    ],
)


# Create stub directories
for e in ENTRIES:
    d = Path(__file__).parent / "designs" / e["id"]
    d.mkdir(parents=True, exist_ok=True)
    for fname in e["cad_files"]:
        (Path(__file__).parent / fname).touch()

with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new designs to {OUT}")
