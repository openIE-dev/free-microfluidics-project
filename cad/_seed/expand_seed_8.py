#!/usr/bin/env python3
"""Eighth expansion of CAD designs."""
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
    id="saw-droplet-manipulation-chip",
    canonical_name="SAW droplet manipulation chip on lithium niobate",
    aliases=["SAW droplet chip", "Friend SAW"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="droplet-generator",
    substrate_material="LiNbO3 (lithium niobate piezoelectric substrate)",
    fabrication_path="Lithium niobate Y-cut wafer; lift-off-patterned aluminum interdigital transducers (IDTs) with 100 µm pitch (~50 MHz operation); hydrophobic top coating (Cytop or similar) on droplet manipulation region",
    channel_geometry="Lithium niobate substrate (10 mm × 10 mm × 0.5 mm) with two opposing IDT pairs at edges (each IDT ~2 mm × 5 mm with 50 µm finger pitch). Open hydrophobic surface in center for droplet manipulation. Each IDT pair generates SAW propagating across hydrophobic surface; droplets respond to SAW radiation pressure.",
    chip_footprint_mm=10,
    cad_files=[
        "designs/saw-droplet-manipulation-chip/idt_pattern.dxf",
        "designs/saw-droplet-manipulation-chip/lift_off_mask.dxf",
        "designs/saw-droplet-manipulation-chip/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["franke-2009-acoustic-cell-sorting-saw", "shi-friend-2009-saw-droplet", "ding-huang-2013-saw-tweezers"],
    related_fab_recipes=[],
    sources=["Friend & Yeo 2011 Rev. Mod. Phys. 83, 647 (microscale acoustofluidics review)"],
    publication_citation="Friend & Yeo 2011",
    validated_performance=None,
    notes="Stub entry. The canonical SAW microfluidic chip architecture: piezoelectric lithium niobate substrate + lithographically patterned IDTs + hydrophobic surface for open-droplet manipulation. Compatible with the open-saw-microfluidic-driver instrument. Suitable for acoustic droplet manipulation, single-cell sorting, and acoustofluidic mixing applications.",
    disclosed_subsystems=[
        "separation-acoustophoresis",
        "droplet-on-demand",
        "fabrication-glass-photolithography",
    ],
)

add(
    id="vasculature-on-chip-3d-bioprinted",
    canonical_name="3D-bioprinted vasculature-on-chip reference (Miller-Bhatia architecture)",
    aliases=["vasculature-on-chip"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="organ-on-chip",
    substrate_material="hydrogel (GelMA / collagen + PDMS substrate)",
    fabrication_path="3D-printed sugar/PVA sacrificial mold per sacrificial-mold-3d-print-elastomer recipe; cast hydrogel around mold; dissolve sacrificial mold to leave perfusable vasculature network in hydrogel",
    channel_geometry="3D branching vasculature network with main channels 500 µm diameter branching into capillary-mimicking 100 µm channels. Total perfused volume ~5 mL within 25 mm × 25 mm × 5 mm hydrogel block. Inlet/outlet ports for media perfusion through vasculature; surrounding hydrogel can be loaded with cells before casting.",
    chip_footprint_mm=25,
    cad_files=[
        "designs/vasculature-on-chip-3d-bioprinted/sacrificial_mold.stl",
        "designs/vasculature-on-chip-3d-bioprinted/casting_form.stl",
    ],
    cad_format="mixed",
    mask_count=0,
    related_corpus_entries=["organoid-on-chip-clevers-2020", "huang-2024-organoid-on-chip-disease-model", "fan-2024-organoid-multiomics"],
    related_fab_recipes=["sacrificial-mold-3d-print-elastomer", "pdms-su8-soft-lithography-baseline"],
    sources=["Miller, J. S. et al. Nat. Mater. 2012, 11, 768–774 (rapid casting of vasculature)"],
    publication_citation="Miller et al. 2012",
    validated_performance=None,
    notes="Stub entry. The canonical 3D-bioprinted-vasculature reference architecture: a sacrificial 3D-printed sugar/PVA mold defines a branching vasculature network in cast hydrogel, then dissolves to leave perfusable channels. Distinct from planar dual-channel organ-on-chip (lung-on-chip, gut-on-chip) by enabling true 3D vasculature topology rather than 2D surface contact. Critical for thick-tissue / organoid models where simple 2D surface perfusion is insufficient.",
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-organ-on-chip-vasculature",
    ],
)

add(
    id="3d-printed-reservoir-manifold",
    canonical_name="3D-printed reservoir manifold for academic chip mounting",
    aliases=["chip mount manifold"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="other",
    substrate_material="thermoplastic",
    fabrication_path="FDM or SLA 3D-printed PETG / Nylon / SLA resin; integrated tubing-fitting threads (1/4-28 UNF or M6); pneumatic-source-to-chip coupling",
    channel_geometry="Manifold body 50 mm × 50 mm × 20 mm with integrated reservoir wells (5 mL each), Luer-lock chip docking interface, and pneumatic input ports. Three reservoir wells for typical droplet-microfluidics applications (cells / beads / oil). Compatible with standard 1/16 inch PEEK tubing and disposable syringe interfaces.",
    chip_footprint_mm=50,
    cad_files=[
        "designs/3d-printed-reservoir-manifold/manifold.stl",
        "designs/3d-printed-reservoir-manifold/chip_dock.stl",
    ],
    cad_format="STL",
    mask_count=0,
    related_corpus_entries=["open-droplet-generator-controller", "open-mrna-lnp-synthesizer-controller"],
    related_fab_recipes=[],
    sources=["Various community-deposited reservoir manifold designs"],
    publication_citation=None,
    validated_performance=None,
    notes="Stub entry. The 'forgotten interface' between control instruments (pumps, pressure sources) and microfluidic chips: most academic groups build ad-hoc manifolds for each new chip. A standardized 3D-printable reservoir manifold reduces setup time and improves reproducibility. Direct architectural cousin of commercial chip-mount platforms (Elveflow, Fluigent) at a fraction of cost.",
    disclosed_subsystems=[],
)

add(
    id="lateral-flow-strip-cartridge-reference",
    canonical_name="Lateral-flow strip cartridge reference (multiplexed serology)",
    aliases=["LFA strip reference", "multiplexed serology cartridge"],
    designer="Free Microfluidics Project (placeholder pending community deposit)",
    designer_country="US",
    license="CC0-1.0",
    license_notes="Stub design pending community contribution.",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_path="Nitrocellulose membrane on backing card; antibody-conjugated gold nanoparticle conjugate pad; sample pad; absorbent pad; injection-molded plastic housing",
    channel_geometry="Standard 60 mm × 4 mm lateral-flow strip in injection-molded housing with sample well (3 mm diameter), antibody-spotted test lines (3 lines for multiplexed assay) at 1 mm spacing, and control line. Capillary flow drives sample through antibody zones with detection by visual or smartphone-camera readout.",
    chip_footprint_mm=75,
    cad_files=[
        "designs/lateral-flow-strip-cartridge-reference/strip_pattern.dxf",
        "designs/lateral-flow-strip-cartridge-reference/cassette_body.dxf",
        "designs/lateral-flow-strip-cartridge-reference/design.gds",
    ],
    cad_format="mixed",
    mask_count=1,
    related_corpus_entries=["orasure-quickflex-cartridge", "chembio-dpp", "qiagen-qiareach-cartridge", "psaltis-2014-color-changing-paper-microfluidic"],
    related_fab_recipes=["paper-microfluidics-wax-printing-baseline"],
    sources=["Yetisen et al. 2013 Lab Chip 13, 2210 (paper microfluidic POC review)"],
    publication_citation="Yetisen et al. 2013",
    validated_performance=None,
    notes="Stub entry. The canonical lateral-flow strip cartridge architecture: 4-pad design (sample / conjugate / nitrocellulose / absorbent) in injection-molded housing. The most produced microfluidic-equivalent product format in the world (billions of LFA strips per year). Useful as IP-clear reference architecture for academic LFA development and as parent reference for many commercial LFA cartridge variants.",
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
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
