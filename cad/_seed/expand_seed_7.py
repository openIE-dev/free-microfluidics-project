#!/usr/bin/env python3
"""Seventh expansion of CAD designs."""
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
    id="herringbone-mixer-reference-mrna-lnp",
    canonical_name="Staggered herringbone mixer chip for mRNA-LNP synthesis",
    aliases=["herringbone LNP chip", "Stroock SHM chip"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="mixer-component",
    substrate_material="PDMS",
    fabrication_path="Two SU-8 masters per herringbone-mixer-fabrication-baseline; 50 µm channel base + 25 µm herringbone grooves; PDMS replica plasma-bonded to glass",
    channel_geometry="Y-junction inlet for two streams (aqueous + ethanol/lipid) at 200 µm × 75 µm cross-section, merging into 200 µm × 100 µm main flow channel with 25 µm-deep staggered herringbone grooves at 45°. Mixer length 30 mm with 6-cycle alternating herringbone groups. Single outlet for collected LNP product.",
    chip_footprint_mm=50,
    cad_files=[
        "designs/herringbone-mixer-reference-mrna-lnp/channel_layer.dxf",
        "designs/herringbone-mixer-reference-mrna-lnp/herringbone_layer.dxf",
        "designs/herringbone-mixer-reference-mrna-lnp/design.gds",
    ],
    cad_format="mixed",
    mask_count=2,
    related_corpus_entries=["stroock-2002-staggered-herringbone-mixer", "microfluidic-mrna-vaccine-formulation", "precision-nanosystems-nanoassemblr"],
    related_fab_recipes=["herringbone-mixer-fabrication-baseline", "pdms-su8-soft-lithography-baseline", "su8-master-baseline"],
    sources=["Stroock et al. 2002 Science 295, 647; Belliveau et al. 2012 Mol. Ther. Nucleic Acids 1, e37"],
    publication_citation="Stroock et al. 2002",
    validated_performance=None,
    notes="Stub entry. Reference design specifically tuned for mRNA-LNP synthesis at academic-research scale (ml-per-hour throughput). Direct architectural ancestor of Precision Nanosystems NanoAssemblr Spark / Benchtop chips, which achieve 90+% mRNA encapsulation at sub-100 nm LNP size.",
    disclosed_subsystems=[
        "mixer-passive-split-recombine",
        "fabrication-pdms-soft-lithography",
        "fabrication-multilayer-lamination",
    ],
)

add(
    id="organoid-on-chip-well-array",
    canonical_name="Organoid-on-chip well array (96-format)",
    aliases=["organoid well chip"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_path="SU-8 master with 1 mm-deep wells and 200 µm-deep perfusion channels; PDMS cast and bonded to glass; ANSI/SLAS 96-well plate footprint with each well containing perfused organoid chamber",
    channel_geometry="ANSI/SLAS 1-2004 96-well plate footprint (127.76 × 85.48 mm) with 96 organoid wells at 9 mm pitch. Each well: 4 mm × 4 mm × 1 mm chamber for organoid culture, with two side-channel perfusion ports for media supply and waste removal. Shared perfusion bus connects all 96 wells in parallel.",
    chip_footprint_mm=128,
    cad_files=[
        "designs/organoid-on-chip-well-array/channel_layer.dxf",
        "designs/organoid-on-chip-well-array/well_layer.dxf",
        "designs/organoid-on-chip-well-array/design.gds",
    ],
    cad_format="mixed",
    mask_count=2,
    related_corpus_entries=["organoid-on-chip-clevers-2020", "huh-2010-lung-on-chip", "huh-bhatia-2018-mps-roadmap", "huang-2024-organoid-on-chip-disease-model"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "su8-master-baseline", "oxygen-plasma-pdms-glass-bonding"],
    sources=["Park et al. 2019 Science 364, 960 (organoids-on-chip); Huh-Bhatia 2020 NIH MPS framework"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. Plate-format organoid-on-chip architecture compatible with high-throughput screening workflows: each of 96 wells contains a perfused organoid chamber, with shared media-supply bus enabling simultaneous perfusion of all wells. Architectural alternative to dual-channel organ-chip (Huh 2010 lung-on-chip lineage) by emphasizing throughput over cell-cell-interface modeling.",
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-organ-on-chip-vasculature",
        "architecture-multi-well-array",
        "fabrication-pdms-soft-lithography",
    ],
)

add(
    id="exosome-separation-dld-chip",
    canonical_name="Exosome separation DLD chip (sub-200 nm cutoff)",
    aliases=["exosome DLD chip"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="separator-component",
    substrate_material="silicon",
    fabrication_path="DRIE-etched silicon with sub-200 nm hexagonal post array; bonded to Borofloat 33 cap via anodic bonding; sub-100 nm post gap requires e-beam lithography for mask fabrication",
    channel_geometry="Hexagonal post array with 500 nm post diameter, 100 nm gap, 1/20 row shift fraction over 20 mm length. Cutoff diameter ~80 nm (within exosome size range, 30–150 nm). Sample inlet, buffer-sheath inlet, and four size-fractionated outlets for size-based exosome enrichment from biological fluids.",
    chip_footprint_mm=50,
    cad_files=[
        "designs/exosome-separation-dld-chip/silicon_layer.dxf",
        "designs/exosome-separation-dld-chip/glass_cap.dxf",
        "designs/exosome-separation-dld-chip/design.gds",
    ],
    cad_format="mixed",
    mask_count=2,
    related_corpus_entries=["microfluidic-extracellular-vesicle-isolation", "huang-2004-dld-deterministic-lateral-displacement", "ozkumur-2013-ctc-iChip"],
    related_fab_recipes=["silicon-drie-bosch-baseline", "silicon-glass-anodic-bonding-baseline", "glass-hf-etching-baseline"],
    sources=["Liga et al. 2015 Lab Chip 15, 2388 (microfluidic exosome isolation)"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. The challenging variant of DLD: scaled to sub-200 nm post gap for exosome (rather than cell or platelet) size range. Requires e-beam lithography for mask fabrication and DRIE for high-aspect-ratio etching of sub-100 nm features. Suitable as IP-clear reference for academic exosome-isolation work.",
    disclosed_subsystems=[
        "separation-deterministic-lateral-displacement",
        "fabrication-silicon-drie",
        "fabrication-glass-anodic-bonding",
    ],
)

add(
    id="ihc-slide-flow-chamber",
    canonical_name="IHC / pathology slide flow chamber reference",
    aliases=["pathology slide chamber"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="organ-on-chip",
    substrate_material="thermoplastic",
    fabrication_path="Injection-molded PMMA or COC body with PSA-laminated cover; 1.5 mm × 25 mm × 75 mm flow chamber sized to standard pathology slide; reservoir wells for reagent dispensing",
    channel_geometry="25 mm × 75 mm × 200 µm flow chamber sized to a standard pathology slide footprint (3 inch × 1 inch). Reagent inlet port + 4 reagent wells along chamber periphery for sequential reagent introduction. Shared waste outlet at chamber exit.",
    chip_footprint_mm=75,
    cad_files=[
        "designs/ihc-slide-flow-chamber/cartridge_body.dxf",
        "designs/ihc-slide-flow-chamber/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["leica-bond-iii-staining", "ventana-discovery-ihc", "dako-omnis-stainer", "goldman-2014-codex-akoya"],
    related_fab_recipes=["thermoplastic-hot-embossing-coc-baseline", "psa-lamination-microfluidics-baseline"],
    sources=["Various IHC automation product literature"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. Standardized flow-chamber-on-pathology-slide architecture compatible with Leica Bond / Ventana DISCOVERY / Dako Omnis-style automated IHC workflows. The pathology-slide footprint (3 inch × 1 inch) is the most common architectural standard in the field; this design provides a chip-format flow chamber compatible with that standard for academic IHC method development.",
    disclosed_subsystems=[
        "architecture-multiplex-cartridge",
        "fabrication-thermoplastic-injection-molding",
    ],
)


# Stub directories
for e in ENTRIES:
    d = Path(__file__).parent / "designs" / e["id"]
    d.mkdir(parents=True, exist_ok=True)
    for fname in e["cad_files"]:
        (Path(__file__).parent / fname).touch()

with OUT.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new designs to {OUT}")
