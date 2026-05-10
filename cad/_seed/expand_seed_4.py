#!/usr/bin/env python3
"""Fourth expansion of CAD designs: lung-on-chip, sweat patch, centrifugal disc, Drop-seq encapsulation."""
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
    id="lung-on-chip-dual-channel-reference",
    canonical_name="Lung-on-chip dual-channel reference (Huh 2010 architecture)",
    aliases=["lung-on-chip reference"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_path="Two SU-8 masters (top: 1 mm × 100 µm channel; bottom: 1 mm × 100 µm channel) cast as separate PDMS layers; PDMS-PDMS bond with O2 plasma activation; track-etched PCM/polycarbonate membrane (10 µm pore) sandwiched between layers; vacuum side-channels for cyclic mechanical strain",
    channel_geometry="Two parallel 1 mm × 100 µm channels separated by porous PDMS or polycarbonate membrane (~10 µm thickness, 10 µm pores). Top channel: epithelial side (air-liquid interface). Bottom channel: vascular side (cell media, fluid flow). Side vacuum channels apply cyclic mechanical strain to the central tissue interface (mimicking breathing motion).",
    chip_footprint_mm=75,
    cad_files=[
        "designs/lung-on-chip-dual-channel-reference/top_channel.dxf",
        "designs/lung-on-chip-dual-channel-reference/bottom_channel.dxf",
        "designs/lung-on-chip-dual-channel-reference/membrane_outline.dxf",
        "designs/lung-on-chip-dual-channel-reference/design.gds",
    ],
    cad_format="mixed",
    mask_count=2,
    related_corpus_entries=["huh-2010-lung-on-chip", "huh-2007-lung-on-chip-precursor", "ingber-emulate-organ-chip", "emulate-organ-on-chip-platform"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "su8-master-baseline", "oxygen-plasma-pdms-glass-bonding"],
    sources=["Huh et al. 2010 Science 328, 1662 (lung-on-chip)"],
    publication_citation="Huh et al. 2010",
    validated_performance=None,
    notes="Stub entry. The canonical lung-on-chip dual-channel architecture from Huh 2010 / Wyss Institute. Subsequent organ-chip designs (gut-on-chip, kidney-on-chip, blood-brain-barrier-on-chip) inherit the same dual-channel + porous-membrane + side-vacuum-strain architecture with tissue-specific surface chemistry. The Emulate commercial chips trace direct lineage from this design.",
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-organ-on-chip-vasculature",
        "fabrication-pdms-soft-lithography",
        "fabrication-multilayer-lamination",
    ],
)

add(
    id="sweat-collection-wearable-patch",
    canonical_name="Sweat-collection epidermal microfluidic patch (Rogers 2016 architecture)",
    aliases=["sweat patch reference"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="point-of-care-cartridge",
    substrate_material="PDMS",
    fabrication_path="SU-8 master, 200 µm thick; soft 30:1 PDMS for skin-conformal flexibility; cast then bonded to PDMS bottom layer with adhesive perimeter; integrated chambers loaded with colorimetric reagents (chloride, glucose, lactate, pH)",
    channel_geometry="Spiral capillary inlet 200 µm wide collecting from sweat pores; 4 reagent reservoir chambers (2 mm diameter × 200 µm depth) connected by capillary-driven channels with integrated bypass for sweat-rate measurement; total patch footprint 30 mm diameter circular",
    chip_footprint_mm=30,
    cad_files=[
        "designs/sweat-collection-wearable-patch/design.dxf",
        "designs/sweat-collection-wearable-patch/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["koh-rogers-2016-epidermal-microfluidic", "gao-2016-sweat-sensor-wearable"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "su8-master-baseline"],
    sources=["Koh et al. 2016 Sci. Transl. Med. 8, 366ra165"],
    publication_citation="Koh et al. 2016",
    validated_performance=None,
    notes="Stub entry. The canonical Rogers-group epidermal microfluidic sweat patch architecture. Subsequent commercial implementations (Epicore Biosystems Gx Sweat Patch, Nix Biosensors hydration patch) descend directly from this design. The combination of capillary-driven sample collection and pre-loaded colorimetric reagents enables fully passive operation with smartphone-camera readout.",
    disclosed_subsystems=[
        "fabrication-pdms-soft-lithography",
        "pump-capillary-passive",
    ],
)

add(
    id="centrifugal-disc-reference-cd",
    canonical_name="Centrifugal lab-on-disc reference (CD-format)",
    aliases=["lab-on-disc reference", "CD-format chip"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="lab-on-chip",
    substrate_material="thermoplastic",
    fabrication_path="CNC-machined or hot-embossed PMMA disc; 120 mm diameter standard CD format; 4 detection-cell positions at 35 mm radius; capillary-burst valves designed at 12, 20, 30, 40 Hz spin frequencies for sequential operation",
    channel_geometry="120 mm diameter PMMA disc with 4 parallel assay paths radiating from central sample-application well at 5 mm radius. Each path: sample chamber → metering chamber → reagent chamber 1 (burst at 12 Hz) → mixing chamber → reagent chamber 2 (burst at 20 Hz) → detection cell at 35 mm radius. Channel widths 200–500 µm, depths 100–300 µm.",
    chip_footprint_mm=120,
    cad_files=[
        "designs/centrifugal-disc-reference-cd/design.dxf",
        "designs/centrifugal-disc-reference-cd/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["madou-2006-centrifugal-microfluidics", "gyros-bioaffy-cd", "abbott-piccolo-xpress", "tecan-burstein-labcd"],
    related_fab_recipes=["thermoplastic-hot-embossing-coc-baseline", "co2-laser-ablation-pmma-baseline"],
    sources=["Madou et al. 2006 Annu. Rev. Biomed. Eng. 8, 601 (centrifugal LoD review)"],
    publication_citation="Madou et al. 2006",
    validated_performance=None,
    notes="Stub entry. The canonical centrifugal lab-on-disc reference architecture: CD-format substrate, sequential capillary-burst valves at distinct spin frequencies, parallel assay paths radiating from central sample input. Architecturally similar to Gyros Bioaffy, Abaxis Piccolo, and Burstein/Tecan LabCD. Suitable as starting point for academic centrifugal-LoD work and as IP-clear reference architecture.",
    disclosed_subsystems=[
        "pump-centrifugal-rotational",
        "valve-burst-frangible",
        "valve-capillary-stop",
        "fabrication-thermoplastic-injection-molding",
    ],
)

add(
    id="drop-seq-co-encapsulation-chip",
    canonical_name="Drop-seq co-encapsulation chip (Macosko 2015 architecture)",
    aliases=["Drop-seq chip reference"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="droplet-generator",
    substrate_material="PDMS",
    fabrication_path="SU-8 master, 100 µm; PDMS 10:1 cured 60 min @ 65 °C; plasma bond to glass slide; channels rendered hydrophobic by perfluorosilane vapor treatment for stable water-in-oil emulsion",
    channel_geometry="Three input channels: cell suspension (50 µm × 100 µm), bead suspension (50 µm × 100 µm), oil with surfactant (3 × 100 µm × 100 µm). Channels co-flow into 100 µm × 100 µm flow-focusing junction with 75 µm orifice for monodisperse droplet generation. Downstream serpentine collection channel.",
    chip_footprint_mm=75,
    cad_files=[
        "designs/drop-seq-co-encapsulation-chip/design.dxf",
        "designs/drop-seq-co-encapsulation-chip/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["macosko-2015-drop-seq", "klein-2015-indrops", "anna-2003-flow-focusing-droplet", "abate-2010-surfactant-survey"],
    related_fab_recipes=["pdms-su8-soft-lithography-baseline", "su8-master-baseline"],
    sources=["Macosko et al. 2015 Cell 161, 1202–1214"],
    publication_citation="Macosko et al. 2015",
    validated_performance=None,
    notes="Stub entry. The Drop-seq co-encapsulation architecture: Poisson-limited co-loading of single cells and single barcoded beads into nanoliter droplets. Architecturally the parent of every commercial single-cell RNA-seq platform (10x Chromium, BD Rhapsody, Mission Bio Tapestri); the differences between platforms are in bead chemistry rather than chip geometry.",
    disclosed_subsystems=[
        "droplet-flow-focusing-generation",
        "cell-encapsulation-droplet",
        "fabrication-pdms-soft-lithography",
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
