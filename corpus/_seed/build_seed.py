#!/usr/bin/env python3
"""Generate the seed corpus for free-microfluidics-corpus.

Each entry below is intended to be commons-grade or explicitly draft.
The script writes a single corpus.jsonl ready to be validated.
"""
import json
from pathlib import Path

OUT = Path(__file__).parent / "corpus.jsonl"

ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 2)
    kw.setdefault("last_updated", "2026-05-09")
    ENTRIES.append(kw)


# =====================================================================
# ACADEMIC — foundational and recent
# =====================================================================

add(
    id="manz-1990-mu-tas-concept",
    canonical_name="Miniaturized total chemical analysis system (µ-TAS)",
    aliases=["µTAS", "miniaturised total analysis systems"],
    corpus="academic",
    first_disclosure_date="1990",
    disclosure_citation="Manz, A.; Graber, N.; Widmer, H. M. Miniaturized total chemical analysis systems: a novel concept for chemical sensing. Sens. Actuators B 1990, 1, 244–248. DOI: 10.1016/0925-4005(90)80209-I",
    creator="Andreas Manz, Nico Graber, Michael Widmer",
    creator_country="CH",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="analytical",
    ip_status="public-domain",
    notable_capabilities=[
        "concept of integrated sample preparation, separation, and detection on a chip",
        "originated the µTAS / lab-on-chip terminology",
    ],
    prior_art_notes="The seminal disclosure of integrated total chemical analysis on a single miniaturized substrate. Anticipates the entire concept of multi-step assay integration on a chip — sample prep, reagent addition, separation, and detection in one device. Any patent claim asserting novelty over 'integrated chemical analysis on a microscale chip' as a generic concept must contend with this 1990 paper.",
    sources=[
        "Sens. Actuators B 1990, 1, 244–248",
        "DOI 10.1016/0925-4005(90)80209-I",
    ],
    disclosed_subsystems=[
        "fabrication-silicon-koh-etching",
    ],
    cpc_classifications=["B01L 3/00"],
    notes="Definitional. Cited by essentially every subsequent µTAS / lab-on-chip paper. Together with Harrison et al. 1993 establishes the field.",
)

add(
    id="harrison-1992-cap-electrophoresis-on-chip",
    canonical_name="Capillary electrophoresis on a microchip",
    aliases=["Harrison 1992", "CE-on-chip"],
    corpus="academic",
    first_disclosure_date="1992",
    disclosure_citation="Harrison, D. J.; Manz, A.; Fan, Z.; Lüdi, H.; Widmer, H. M. Capillary electrophoresis and sample injection systems integrated on a planar glass chip. Anal. Chem. 1992, 64, 1926–1932. DOI: 10.1021/ac00041a030",
    creator="D. Jed Harrison, Andreas Manz et al.",
    creator_country="CA",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    channel_geometry="HF-etched glass capillary network",
    flow_regime="electrokinetic",
    end_application="analytical",
    ip_status="public-domain",
    prior_art_notes="First demonstration of capillary electrophoresis with sample injection integrated on a planar glass chip. Anticipates: integrated electrokinetic separation, T-injector geometry for plug formation, glass-glass thermal bonding for chip sealing, and on-chip electrochemical or fluorescence detection coupled to electrophoretic separation. Patent claims asserting novelty over CE-on-chip as a category run into this disclosure.",
    sources=[
        "Anal. Chem. 1992, 64, 1926–1932",
        "DOI 10.1021/ac00041a030",
    ],
    disclosed_subsystems=[
        "fabrication-glass-hf-etching",
        "fabrication-glass-thermal-bonding",
        "separation-capillary-electrophoresis",
        "material-borofloat-glass",
    ],
    cpc_classifications=["G01N 27/447"],
    lineage_ancestors=["manz-1990-mu-tas-concept"],
)

add(
    id="duffy-1998-pdms-soft-lithography-microfluidics",
    canonical_name="Rapid prototyping of microfluidic systems in PDMS",
    aliases=["Duffy 1998", "PDMS soft lithography for microfluidics"],
    corpus="academic",
    first_disclosure_date="1998",
    disclosure_citation="Duffy, D. C.; McDonald, J. C.; Schueller, O. J. A.; Whitesides, G. M. Rapid prototyping of microfluidic systems in poly(dimethylsiloxane). Anal. Chem. 1998, 70, 4974–4984. DOI: 10.1021/ac980656z",
    creator="Whitesides group, Harvard",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    channel_geometry="SU-8 master with PDMS replica, channel widths 10 µm to 1 mm",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="The paper that turned PDMS soft lithography into the default microfluidics fabrication method for the next 25+ years. Anticipates: SU-8 master mold + PDMS replica casting, oxygen-plasma bonding of PDMS to glass or PDMS, hydrophilic surface treatment by plasma oxidation, and rapid-prototyping iteration of channel designs. Any patent claiming novelty over 'PDMS replica molding from a photoresist master with plasma bonding to substrate' must address this disclosure.",
    sources=[
        "Anal. Chem. 1998, 70, 4974–4984",
        "DOI 10.1021/ac980656z",
    ],
    disclosed_subsystems=[
        "fabrication-pdms-soft-lithography",
        "fabrication-pdms-replica-molding",
        "fabrication-su8-photoresist",
        "surface-pdms-plasma-bonding",
        "material-pdms-base",
    ],
    cpc_classifications=["B01L 3/00", "B81C 1/00"],
    lineage_ancestors=["manz-1990-mu-tas-concept"],
)

add(
    id="unger-2000-quake-monolithic-membrane-valve",
    canonical_name="Quake monolithic pneumatic membrane valve and pump",
    aliases=["Quake valve", "MSL valve", "multilayer soft lithography valve"],
    corpus="academic",
    first_disclosure_date="2000",
    disclosure_citation="Unger, M. A.; Chou, H.-P.; Thorsen, T.; Scherer, A.; Quake, S. R. Monolithic microfabricated valves and pumps by multilayer soft lithography. Science 2000, 288, 113–116. DOI: 10.1126/science.288.5463.113",
    creator="Stephen Quake group, Caltech",
    creator_country="US",
    device_class="valve-component",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    channel_geometry="two-layer PDMS, control channel above flow channel separated by thin elastomer membrane",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US6929030B2", "US7144616B1", "WO2001001025A2 (and family)"],
    prior_art_notes="Foundational disclosure of pneumatically actuated elastomeric membrane valves built monolithically into a multilayer PDMS chip. By cyclically actuating three valves in series, a peristaltic pump is realized. This is the architectural ancestor of essentially every subsequent on-chip pneumatic valve and pump. Anticipates: pneumatic membrane valve (control channel + thin membrane + flow channel), peristaltic pumping by sequential valve actuation, large-scale integrated chip-scale fluidic circuits. Subsequent papers (Nordin 2017, Sanchez Noriega 2021) re-implement the same architecture in 3D-printed photopolymer.",
    sources=[
        "Science 2000, 288, 113–116",
        "DOI 10.1126/science.288.5463.113",
    ],
    disclosed_subsystems=[
        "valve-quake-pneumatic-membrane",
        "pump-membrane-pneumatic",
        "pump-peristaltic-on-chip",
        "fabrication-pdms-soft-lithography",
        "fabrication-multilayer-lamination",
    ],
    cpc_classifications=["F16K 99/00", "B01L 3/00"],
    lineage_ancestors=["duffy-1998-pdms-soft-lithography-microfluidics"],
)

add(
    id="thorsen-2002-droplet-microfluidics-flow-focusing",
    canonical_name="Dynamic pattern formation in a vesicle-generating microfluidic device",
    aliases=["Thorsen 2002 droplet generation"],
    corpus="academic",
    first_disclosure_date="2001",
    disclosure_citation="Thorsen, T.; Roberts, R. W.; Arnold, F. H.; Quake, S. R. Dynamic pattern formation in a vesicle-generating microfluidic device. Phys. Rev. Lett. 2001, 86, 4163–4166. DOI: 10.1103/PhysRevLett.86.4163",
    creator="Thorsen, Quake et al., Caltech",
    creator_country="US",
    device_class="droplet-generator",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="One of the earliest demonstrations of monodisperse aqueous droplet generation in oil within a microfluidic geometry. Anticipates: T-junction droplet formation, controlled droplet size as a function of flow rate ratio, monodisperse emulsion as a microfluidic primitive. The lineage from here runs through Anna 2003 (flow focusing) into the entire droplet-microfluidics field including ddPCR, single-cell RNA-seq, and barcoded bead workflows.",
    sources=[
        "Phys. Rev. Lett. 2001, 86, 4163–4166",
        "DOI 10.1103/PhysRevLett.86.4163",
    ],
    disclosed_subsystems=[
        "droplet-t-junction-generation",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01F 23/00", "B01L 3/00"],
    lineage_ancestors=["duffy-1998-pdms-soft-lithography-microfluidics"],
)

add(
    id="anna-2003-flow-focusing-droplet",
    canonical_name="Flow-focusing droplet generation in microfluidic devices",
    aliases=["Anna flow focusing"],
    corpus="academic",
    first_disclosure_date="2003",
    disclosure_citation="Anna, S. L.; Bontoux, N.; Stone, H. A. Formation of dispersions using 'flow focusing' in microchannels. Appl. Phys. Lett. 2003, 82, 364–366. DOI: 10.1063/1.1537519",
    creator="Anna, Bontoux, Stone (Harvard)",
    creator_country="US",
    device_class="droplet-generator",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Established flow-focusing droplet generation as a parallel architecture to the T-junction. Disclosed: a continuous-phase fluid focuses a dispersed-phase stream through a constriction, forming droplets at controllable rates and sizes. This geometry underlies most modern droplet platforms (10x Genomics-style microfluidic chips, Bio-Rad ddPCR generators, etc.).",
    sources=[
        "Appl. Phys. Lett. 2003, 82, 364–366",
        "DOI 10.1063/1.1537519",
    ],
    disclosed_subsystems=[
        "droplet-flow-focusing-generation",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01F 23/00"],
    lineage_ancestors=["thorsen-2002-droplet-microfluidics-flow-focusing"],
)

add(
    id="stroock-2002-staggered-herringbone-mixer",
    canonical_name="Chaotic mixer for microchannels (staggered herringbone)",
    aliases=["staggered herringbone mixer", "SHM"],
    corpus="academic",
    first_disclosure_date="2002",
    disclosure_citation="Stroock, A. D.; Dertinger, S. K. W.; Ajdari, A.; Mezic, I.; Stone, H. A.; Whitesides, G. M. Chaotic mixer for microchannels. Science 2002, 295, 647–651. DOI: 10.1126/science.1066238",
    creator="Stroock, Whitesides et al., Harvard",
    creator_country="US",
    device_class="mixer-component",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="The canonical disclosure of passive chaotic mixing in microchannels via patterned grooves on the channel floor. Anticipates: staggered herringbone topology, the principle of using transverse flow patterns to fold fluid layers and shorten diffusion paths in laminar regimes. Any patent claiming novelty over 'patterned floor structures producing transverse flow for mixing' must contend with this disclosure.",
    sources=[
        "Science 2002, 295, 647–651",
        "DOI 10.1126/science.1066238",
    ],
    disclosed_subsystems=[
        "mixer-passive-staggered-herringbone",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01F 33/30"],
)

add(
    id="huang-2004-dld-deterministic-lateral-displacement",
    canonical_name="Deterministic lateral displacement particle separation",
    aliases=["DLD", "Huang 2004"],
    corpus="academic",
    first_disclosure_date="2004",
    disclosure_citation="Huang, L. R.; Cox, E. C.; Austin, R. H.; Sturm, J. C. Continuous particle separation through deterministic lateral displacement. Science 2004, 304, 987–990. DOI: 10.1126/science.1094567",
    creator="Huang, Sturm, Austin, Cox (Princeton)",
    creator_country="US",
    device_class="separator-component",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="analytical",
    ip_status="patented",
    ip_citations=["US7150812B2"],
    prior_art_notes="Disclosed deterministic lateral displacement: a periodic pillar array shifts particles above a critical size laterally with each row, while smaller particles pass through. Anticipates the entire DLD field including blood cell separation, CTC capture, and exosome isolation. Subsequent commercial implementations (e.g., GPB Scientific) build directly on this geometry.",
    sources=[
        "Science 2004, 304, 987–990",
        "DOI 10.1126/science.1094567",
    ],
    disclosed_subsystems=[
        "separation-deterministic-lateral-displacement",
        "fabrication-silicon-drie",
    ],
    cpc_classifications=["B03B 5/00", "B01L 3/00"],
)

add(
    id="martinez-2007-paper-microfluidics",
    canonical_name="Paper-based microfluidic devices for distributed point-of-care diagnostics",
    aliases=["Martinez 2007 µPAD", "paper microfluidics"],
    corpus="academic",
    first_disclosure_date="2007",
    disclosure_citation="Martinez, A. W.; Phillips, S. T.; Butte, M. J.; Whitesides, G. M. Patterned paper as a platform for inexpensive, low-volume, portable bioassays. Angew. Chem. Int. Ed. 2007, 46, 1318–1320. DOI: 10.1002/anie.200603817",
    creator="Whitesides group, Harvard",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="photolithography",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US20100285578A1"],
    prior_art_notes="The paper that established paper-based microfluidic analytical devices (µPADs) as a category. Anticipates: hydrophobic patterning of cellulose paper to define fluid channels, capillary-driven flow without external pumps, multiplex colorimetric assays on a single paper substrate. The entire low-resource diagnostic paper-fluidics field descends from this disclosure.",
    sources=[
        "Angew. Chem. Int. Ed. 2007, 46, 1318–1320",
        "DOI 10.1002/anie.200603817",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
        "material-paper-cellulose",
    ],
    cpc_classifications=["B01L 3/00", "G01N 33/52"],
)

add(
    id="huh-2010-lung-on-chip",
    canonical_name="Lung-on-a-chip",
    aliases=["Huh 2010 lung on chip", "Wyss lung-on-chip"],
    corpus="academic",
    first_disclosure_date="2010",
    disclosure_citation="Huh, D.; Matthews, B. D.; Mammoto, A.; Montoya-Zavala, M.; Hsin, H. Y.; Ingber, D. E. Reconstituting organ-level lung functions on a chip. Science 2010, 328, 1662–1668. DOI: 10.1126/science.1188302",
    creator="Donald Ingber group, Wyss Institute",
    creator_country="US",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    channel_geometry="two parallel PDMS channels separated by a thin porous membrane with cyclic pneumatic stretch",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US8647861B2", "WO2010009307A2"],
    prior_art_notes="The foundational organ-on-chip disclosure: lung alveolar-capillary interface reconstituted on a microfluidic chip with cyclic mechanical stretch. Anticipates: dual-channel architecture with intervening porous membrane, mechanical actuation of cell-bearing membranes via pneumatic chambers, perfused human cell co-culture with epithelial-endothelial interfaces. Spawned the Emulate Inc. commercial platform and the entire organ-on-chip field.",
    sources=[
        "Science 2010, 328, 1662–1668",
        "DOI 10.1126/science.1188302",
    ],
    disclosed_subsystems=[
        "fabrication-pdms-soft-lithography",
        "architecture-organ-on-chip-vasculature",
        "valve-quake-pneumatic-membrane",
        "cell-organoid-perfusion",
    ],
    cpc_classifications=["C12M 1/00", "C12M 3/00"],
    lineage_ancestors=[
        "duffy-1998-pdms-soft-lithography-microfluidics",
        "unger-2000-quake-monolithic-membrane-valve",
    ],
)

add(
    id="macosko-2015-drop-seq",
    canonical_name="Drop-seq single-cell RNA sequencing",
    aliases=["Drop-seq"],
    corpus="academic",
    first_disclosure_date="2015",
    disclosure_citation="Macosko, E. Z. et al. Highly parallel genome-wide expression profiling of individual cells using nanoliter droplets. Cell 2015, 161, 1202–1214. DOI: 10.1016/j.cell.2015.05.002",
    creator="Macosko, McCarroll lab, Broad Institute",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Anticipates: co-encapsulation of single cells with barcoded beads in droplets via flow-focusing, lysis-on-bead chemistry, downstream pooled sequencing with barcode demultiplexing. Together with InDrops (Klein et al. 2015), this is the technical foundation of the modern single-cell genomics ecosystem, including the commercial 10x Genomics Chromium platform.",
    sources=[
        "Cell 2015, 161, 1202–1214",
        "DOI 10.1016/j.cell.2015.05.002",
    ],
    disclosed_subsystems=[
        "droplet-flow-focusing-generation",
        "cell-encapsulation-droplet",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["C12Q 1/68"],
    lineage_ancestors=["anna-2003-flow-focusing-droplet"],
)

add(
    id="gong-2017-3d-printed-18x20-microfluidic-channels",
    canonical_name="Custom 3D printer and resin for 18×20 µm microfluidic flow channels",
    aliases=["Gong 2017", "Nordin 18x20 channels"],
    corpus="academic",
    first_disclosure_date="2017",
    disclosure_citation="Gong, H.; Bickham, B. P.; Woolley, A. T.; Nordin, G. P. Custom 3D printer and resin for 18 µm × 20 µm microfluidic flow channels. Lab Chip 2017, 17, 2899–2909. DOI: 10.1039/C7LC00644F",
    creator="Nordin / Woolley group, BYU",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="other",
    fabrication_method="dlp-sla",
    channel_geometry="18 µm × 20 µm fully enclosed channels in PEGDA-based resin via custom DLP-SLA printer",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Established that DLP-SLA 3D printing can produce sub-25-µm enclosed microfluidic channels using a custom printer with custom UV-absorber resin formulation. Anticipates: dual-cycle resin with photoinitiator + UV absorber to localize photopolymerization, layer thickness selected from optical penetration depth (not arbitrary), and enclosed channel formation via timed exposures. The direct ancestor of the Nordin 2026 multi-resolution work.",
    sources=[
        "Lab Chip 2017, 17, 2899–2909",
        "DOI 10.1039/C7LC00644F",
    ],
    disclosed_subsystems=[
        "fabrication-dlp-sla-enclosed-channels",
        "material-pegda-photoresin",
    ],
    cpc_classifications=["B33Y 10/00", "B01L 3/00"],
)

add(
    id="spackova-2022-nanofluidic-scattering-microscopy",
    canonical_name="Nanofluidic scattering microscopy (NSM)",
    aliases=["Špačková 2022 NSM"],
    corpus="academic",
    first_disclosure_date="2022",
    disclosure_citation="Špačková, B. et al. Label-free nanofluidic scattering microscopy of size and mass of single diffusing molecules and nanoparticles. Nat. Methods 2022, 19, 751–758. DOI: 10.1038/s41592-022-01491-6",
    creator="Langhammer group, Chalmers",
    creator_country="SE",
    device_class="nanofluidic-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    channel_geometry="100–200 nm wide × 200 nm deep nanochannels in thermal SiO2, bonded with Borofloat 33 lid",
    flow_regime="pressure-driven",
    sample_volume="600 attoliter per imaged channel section",
    end_application="analytical",
    ip_status="public-domain",
    prior_art_notes="Established label-free single-molecule mass and size measurement via scattering from individual molecules in nanofluidic channels. Anticipates: Si/SiO2 nanochannel arrays with co-linear sample/reference channels for differential scattering measurement, Borofloat-glass optical window thermally bonded to silicon for inverted-microscope access. Direct ancestor of NSS (Altenburger 2025) and the Langhammer 2026 chip-holder work.",
    sources=[
        "Nat. Methods 2022, 19, 751–758",
        "DOI 10.1038/s41592-022-01491-6",
    ],
    disclosed_subsystems=[
        "detection-nanofluidic-scattering-spectroscopy",
        "detection-label-free-imaging",
        "fabrication-glass-thermal-bonding",
        "interface-optical-window-borofloat",
        "material-borofloat-glass",
    ],
    cpc_classifications=["G01N 21/64"],
)

add(
    id="miner-2026-multi-resolution-3d-printing-microfluidics",
    canonical_name="Multi-resolution DLP-SLA for 2 µm microfluidic channels",
    aliases=["Miner 2026", "Nordin 2026 multi-resolution"],
    corpus="academic",
    first_disclosure_date="2026-02-27",
    disclosure_citation="Miner, D. S.; Viglione, M. S.; Hooper, K.; Woolley, A. T.; Nordin, G. P. Fast multi-resolution 3D printing of microfluidics: enabling 2 µm channels and ultra-compact mixers. Microsyst. Nanoeng. 2026, 12, 66. DOI: 10.1038/s41378-026-01194-4",
    creator="Nordin / Woolley group, BYU",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="other",
    fabrication_method="dlp-sla",
    channel_geometry="1.9 × 2.0 µm enclosed channels via dual optical engine (0.75 µm and 15 µm pixel pitches), 17 nL on-chip mixer",
    flow_regime="pressure-driven",
    sample_volume="17 nL printed mixer volume; ~2 nL interior",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Discloses true multi-resolution DLP-SLA in both XY and Z dimensions via dual optical engines (0.75 µm and 15 µm pixel pitch) and dual-UV-absorber resin (NPS + avobenzone) producing 2 µm and 20 µm penetration depths. Anticipates: multi-resolution-in-Z via dual-absorber resin chemistry tuned to two distinct LED spectra (365 nm and 405 nm), embedded high-resolution regions in lower-resolution bulk prints, sub-2-µm enclosed channels in a printable photopolymer, and a 17-nL on-chip diffusive mixer with ±2% uniformity. Patent claims asserting novelty over 'multi-wavelength resin chemistry for spatially-tailored DLP-SLA Z resolution' must address this disclosure.",
    sources=[
        "Microsyst. Nanoeng. 2026, 12, 66",
        "DOI 10.1038/s41378-026-01194-4",
    ],
    disclosed_subsystems=[
        "fabrication-dlp-sla-enclosed-channels",
        "fabrication-multi-resolution-3d-printing",
        "mixer-passive-interleaved-streams",
        "valve-quake-pneumatic-membrane",
        "pump-membrane-pneumatic",
        "material-pegda-photoresin",
    ],
    cpc_classifications=["B33Y 10/00", "B33Y 70/00", "B01L 3/00"],
    lineage_ancestors=[
        "gong-2017-3d-printed-18x20-microfluidic-channels",
        "unger-2000-quake-monolithic-membrane-valve",
    ],
)

add(
    id="altenburger-2026-temperature-controlled-chip-holder",
    canonical_name="Temperature-controlled chip holder with integrated electrodes for NSS",
    aliases=["Langhammer 2026 chip holder"],
    corpus="academic",
    first_disclosure_date="2026-01-19",
    disclosure_citation="Altenburger, B.; Fritzsche, J.; Langhammer, C. A temperature-controlled chip holder with integrated electrodes for nanofluidic scattering spectroscopy on highly integrated nanofluidic systems. Microsyst. Nanoeng. 2026, 12, 32. DOI: 10.1038/s41378-025-01125-9",
    creator="Langhammer group, Chalmers",
    creator_country="SE",
    device_class="chip-holder",
    substrate_material="hybrid",
    fabrication_method="other",
    channel_geometry="acrylic channel plate with 12 Luer-Lock cannulated fluidic connection points; aluminum heat bridge with four Peltier elements",
    flow_regime="pressure-driven",
    chip_footprint_mm=10,
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Discloses a multifunctional fluidic chip holder integrating: 12 Luer-Lock fluidic ports with O-ring sealing against a 1 cm² Si/SiO2 chip, four series-wired Peltier elements thermally bridged to the chip via an aluminum heat bridge with passive air-gap insulation, electrodes inserted through Luer-T couplings for application of electric fields across the same connection points used for fluid, and an optically transparent acrylic channel plate. Operating range 12 °C to 112 °C with characterized hysteresis curves. Anticipates: combined fluid/electrode insertion through a single Luer-T port, off-chip Peltier-on-frame architecture instead of on-chip resistive heating, and the architectural pattern of treating the holder as the multi-modal periphery of a small chip.",
    sources=[
        "Microsyst. Nanoeng. 2026, 12, 32",
        "DOI 10.1038/s41378-025-01125-9",
    ],
    disclosed_subsystems=[
        "thermal-on-chip-peltier",
        "interface-luer-lock-port",
        "interface-o-ring-seal",
        "interface-electrode-integration",
        "interface-pressure-manifold",
        "interface-optical-window-borofloat",
        "detection-nanofluidic-scattering-spectroscopy",
    ],
    cpc_classifications=["B01L 3/00", "B01L 9/00"],
    lineage_ancestors=["spackova-2022-nanofluidic-scattering-microscopy"],
)

add(
    id="wang-2026-dish-volumetric-3d-printing",
    canonical_name="DISH: digital incoherent synthesis of holographic light fields",
    aliases=["DISH", "Wang 2026 volumetric printing"],
    corpus="academic",
    first_disclosure_date="2026-02-11",
    disclosure_citation="Wang, X.; Ma, Y.; Niu, Y.; Xiong, B.; Zhang, A.; Zhang, G.; Chen, Y.; Wei, W.; Fang, L.; Wu, J.; Dai, Q. Sub-second volumetric 3D printing by synthesis of holographic light fields. Nature 2026. DOI: 10.1038/s41586-026-10114-5",
    creator="Dai / Wu / Fang group, Tsinghua",
    creator_country="CN",
    device_class="printer-tooling",
    substrate_material="other",
    fabrication_method="dlp-sla",
    channel_geometry="0.6 s mm-scale objects, 19 µm uniform resolution across 1 cm depth, 12 µm finest positive feature",
    flow_regime="pressure-driven",
    throughput="333 mm³/s; 1.25×10^8 voxels/s; 0.6 s per millimetre-scale object",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Discloses sub-second volumetric 3D printing by holographically synthesized multi-angle DMD projections through a high-speed rotating periscope (10 rotations/s) instead of rotating the sample. Anticipates: rotating-periscope-rather-than-rotating-sample architecture for tomographic volumetric printing, holographic optimization of binary DMD patterns against a wave-optics propagation model with refraction at the air-resin interface, adaptive-optics calibration via two orthogonal cameras as wavefront sensors, integration of volumetric printing with a flow channel for continuous mass production of arbitrary 3D microparticles in low-viscosity resins (4.7 cP), and the use of incoherent synthesis of binary holograms to generate high-contrast 3D dose distributions across depth ranges 25× the objective's depth of field.",
    sources=[
        "Nature 2026; DOI 10.1038/s41586-026-10114-5",
        "Code: https://github.com/sugar10w/DISH",
        "Zenodo: 10.5281/zenodo.17905914",
    ],
    disclosed_subsystems=[
        "fabrication-volumetric-3d-printing",
        "architecture-mass-production-volumetric-print",
        "material-pegda-photoresin",
    ],
    cpc_classifications=["B33Y 10/00", "B33Y 30/00", "B29C 64/124"],
)

add(
    id="zhang-2026-aesop-acoustic-electric-poration",
    canonical_name="AESOP: acoustic-electric shear orbiting poration",
    aliases=["AESOP", "Lee 2026 sequential delivery"],
    corpus="academic",
    first_disclosure_date="2026-04-09",
    disclosure_citation="Zhang, M.; Taravatfard, A. Z.; Aghaamoo, M.; Lee, A. P. Sequential intracellular delivery of genetic coding molecules using an acoustic electric microfluidic platform. Lab Chip 2026, advance article. DOI: 10.1039/D5LC00941C",
    creator="Abraham P. Lee group, UC Irvine",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="acoustic",
    sample_volume="hundreds of thousands of cells per chip",
    end_application="bioprocess",
    ip_status="patented",
    ip_citations=["status to be verified; check Lee group / UCI portfolio"],
    prior_art_notes="Discloses an acoustic-electric microfluidic platform for sequential intracellular transfection without external pumping. Anticipates: arrays of acoustic microstreaming vortices generated by oscillating air-liquid interfaces (trapped bubbles driven by piezoactuation) for cell trapping, simultaneous use of the same acoustic field for sequential reagent exchange, combined mechanical shear + electric field poration as a single transfection step, and 7× efficiency gain over co-transfection for plasmid DNA + Cas9 RNP delivery. Single physical mechanism (acoustic streaming) collapses three subsystems (cell trap, fluid handler, transfection actuator).",
    sources=[
        "Lab Chip 2026, advance article",
        "DOI 10.1039/D5LC00941C",
    ],
    disclosed_subsystems=[
        "cell-trap-acoustic-streaming-vortex",
        "cell-poration-electric",
        "cell-poration-mechanical-shear",
        "pump-acoustic-streaming",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["C12N 13/00", "C12M 35/00"],
)

# =====================================================================
# PRIVATE — patent-thicket holders, commercial cartridges
# =====================================================================

add(
    id="lee-company-disc-pump-piezoelectric",
    canonical_name="Lee Company / TTP Ventus Disc Pump",
    aliases=["TTP Ventus Disc Pump", "Lee Disc Pump"],
    corpus="private",
    first_disclosure_date="2009",
    disclosure_citation="TTP Ventus disc pump technology, originally disclosed via TTP plc / Cambridge UK; commercialized; acquired by The Lee Company. See https://www.theleeco.com/disc-pumps/ and product datasheets.",
    creator="TTP Ventus (TTP plc spinout); now The Lee Company",
    creator_country="GB",
    device_class="pump-component",
    substrate_material="other",
    fabrication_method="other",
    channel_geometry="29 mm form factor pneumatic micropump; piezoelectrically actuated cavity",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=[
        "GB2467966A (and family)",
        "US8678787B2",
        "US9777724B2",
    ],
    prior_art_notes="Discloses a small-form-factor piezoelectrically driven disc pump generating pressure or vacuum with pulsation-free output and infinite turndown ratio. Standard 'air-over-liquid' actuation pattern: pump moves gas, gas indirectly displaces liquid in tubing or chip. Anticipates: 29-mm-class piezoelectric pneumatic micropumps for diagnostics, infinite-turndown pneumatic actuation, and the air-over-liquid architectural pattern as a substitute for direct liquid pumping in microfluidic instrument design.",
    sources=[
        "https://www.theleeco.com/disc-pumps/",
        "TTP Ventus product literature",
        "GB2467966A patent family",
    ],
    disclosed_subsystems=[
        "pump-piezoelectric-disc",
        "pump-pressure-controlled-air-over-liquid",
    ],
    cpc_classifications=["F04B 43/04", "F04B 17/00"],
)

add(
    id="lee-fixed-volume-dispense-pump",
    canonical_name="Lee fixed-volume solenoid dispense pump",
    aliases=["Lee Co fixed-volume pump"],
    corpus="private",
    first_disclosure_date="2007",
    disclosure_citation="Lee Company fixed volume dispense pump product line. https://www.theleeco.com/industries/diagnostics/products/pumps/ and product datasheets.",
    creator="The Lee Company",
    creator_country="US",
    device_class="pump-component",
    substrate_material="other",
    fabrication_method="other",
    channel_geometry="solenoid-driven positive displacement, 25–50 µL per stroke",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["various Lee Company patents"],
    prior_art_notes="Discloses a chemically inert solenoid-driven positive-displacement pump with integrated check valves, energize-to-aspirate / de-energize-to-dispense control. Anticipates: single-electrical-input deterministic-volume dispensing in IVD instruments, anti-siphon housing geometry with diaphragm seal, and the broader category of solenoid-driven discrete-volume pumps for clinical diagnostics.",
    sources=[
        "https://www.theleeco.com/industries/diagnostics/products/pumps/",
        "Lee Company product handbooks",
    ],
    disclosed_subsystems=[
        "pump-solenoid-displacement",
        "valve-check",
    ],
    cpc_classifications=["F04B 17/04", "B01L 3/02"],
)

add(
    id="biofire-filmarray-multiplex-pcr-cartridge",
    canonical_name="BioFire FilmArray multiplex PCR cartridge",
    aliases=["FilmArray", "BioFire pouch"],
    corpus="private",
    first_disclosure_date="2008",
    disclosure_citation="Idaho Technology Inc. (now BioFire Diagnostics, BioMérieux). FilmArray system. FDA 510(k) clearances K103175 (2011) and subsequent panels.",
    creator="BioFire Diagnostics (Idaho Technology origin); BioMérieux subsidiary",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    channel_geometry="pouch-format multilayer thermoplastic with blister-pack reagent storage; integrated nested PCR + multiplex array detection",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=[
        "US8895295B2",
        "US9528144B2",
        "FDA 510(k) K103175 and subsequent",
    ],
    prior_art_notes="Discloses a single-use disposable cartridge integrating sample preparation, nucleic acid extraction, multiplex nested PCR, and array-based detection in a closed pouch format. Anticipates: blister-pack on-cartridge reagent storage, foil-piercing actuation, multilayer thermoplastic lamination as a fabrication path for point-of-care molecular diagnostics, integrated thermal cycling within a sealed pouch, and the architectural pattern of 'sample-in / answer-out' multiplex IVD cartridges. The dominant commercial implementation in syndromic panel testing.",
    sources=[
        "BioFire / BioMérieux product literature",
        "Poritz et al. 2011 PLoS ONE 6(10):e26047",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "architecture-multiplex-cartridge",
        "interface-blister-pack-reagent-storage",
        "interface-foil-pierce-actuation",
        "fabrication-multilayer-lamination",
        "fabrication-thermoplastic-injection-molding",
        "thermal-pcr-cycling",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/686"],
)

add(
    id="cepheid-genexpert-cartridge",
    canonical_name="Cepheid GeneXpert cartridge",
    aliases=["GeneXpert", "Cepheid cartridge"],
    corpus="private",
    first_disclosure_date="2004",
    disclosure_citation="Cepheid GeneXpert system; FDA 510(k) K043510 (2004) and subsequent assay clearances.",
    creator="Cepheid (Danaher subsidiary)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    channel_geometry="rotary valve cartridge with multiple reagent chambers, integrated reaction tube for real-time PCR",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=[
        "US6818185B1",
        "US7081226B1",
        "US7780336B2",
    ],
    prior_art_notes="Discloses a disposable cartridge with a rotary valve sequencing reagents through a sample preparation pathway into an optical reaction tube for real-time PCR. Anticipates: rotary-valve / multi-port selector architecture for multi-reagent cartridges, optically interrogated reaction chamber within a closed disposable, and the GeneXpert-style sample-prep + amplification + detection integration that underlies most Cepheid POC products including the Xpert MTB/RIF tuberculosis test.",
    sources=[
        "Cepheid product literature",
        "Helb et al. 2010 J. Clin. Microbiol. 48, 229–237",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "valve-rotary-multiport",
        "thermal-pcr-cycling",
        "fabrication-thermoplastic-injection-molding",
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/686"],
)

add(
    id="abbott-id-now-isothermal-cartridge",
    canonical_name="Abbott ID NOW isothermal amplification cartridge",
    aliases=["ID NOW", "Alere i", "Abbott Alere"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="Alere i / Abbott ID NOW. FDA 510(k) and EUA clearances. https://www.globalpointofcare.abbott/en/product-details/id-now.html",
    creator="Alere Inc.; now Abbott Diagnostics",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US8945881B2", "various Alere/Abbott patents"],
    prior_art_notes="Discloses a small-format isothermal nucleic acid amplification cartridge for ~15-minute molecular diagnostics, eliminating thermal cycling hardware. Anticipates: nicking-enzyme-amplification-reaction (NEAR) chemistry on a disposable cartridge, isothermal POC molecular testing for influenza/strep/SARS-CoV-2, and the architectural pattern of substituting fast isothermal chemistry for cartridge-level thermal cycling complexity.",
    sources=[
        "Abbott ID NOW product literature",
        "Nie et al. 2014 J. Clin. Microbiol. 52, 3339–3344",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-isothermal-amplification",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/686"],
)

add(
    id="canon-bubble-jet-printhead",
    canonical_name="Canon thermal Bubble Jet inkjet printhead",
    aliases=["Bubble Jet", "Canon BJ"],
    corpus="private",
    first_disclosure_date="1979",
    disclosure_citation="Endo, I.; Sato, Y.; Saito, S.; Nakagiri, T.; Ohno, S. Liquid jet recording process and apparatus therefor. JP S54-59936A (1979); subsequent US patents include US4723129 (1988).",
    creator="Canon Inc., Endo et al.",
    creator_country="JP",
    device_class="inkjet-printhead",
    substrate_material="silicon",
    fabrication_method="photolithography",
    channel_geometry="microchannel array with thin-film resistor heaters at nozzle exits; vapor-bubble ejection",
    flow_regime="pressure-driven",
    end_application="industrial",
    ip_status="patented",
    ip_citations=["US4723129", "JP S54-59936A"],
    prior_art_notes="Foundational disclosure of thermal bubble-jet inkjet printheads — almost certainly the highest-volume microfluidic device ever produced. Anticipates: integrated silicon-based microfluidic channels with embedded thin-film resistive heaters, on-demand vapor-bubble droplet ejection from microscale orifices, and the entire thermal-inkjet category of consumer printers. Microfluidics' largest commercial deployment by orders of magnitude predates the academic field's emergence.",
    sources=[
        "Canon Bubble Jet history; Endo et al. patent family",
        "US4723129",
    ],
    disclosed_subsystems=[
        "pump-thermal-bubble-jet",
        "droplet-on-demand",
        "fabrication-silicon-koh-etching",
    ],
    cpc_classifications=["B41J 2/14"],
    notes="Often forgotten in 'microfluidics' surveys because it predates the µTAS framing. Manz 1990 was new terminology; Canon and HP had been shipping silicon microfluidics for over a decade by then.",
)

add(
    id="hp-thinkjet-thermal-inkjet",
    canonical_name="HP ThinkJet thermal inkjet printhead",
    aliases=["HP ThinkJet", "HP 2225"],
    corpus="private",
    first_disclosure_date="1984",
    disclosure_citation="Hewlett-Packard ThinkJet (HP 2225), launched 1984; thermal-inkjet patent family includes US4490728 (Vaught & Hackleman, 1984).",
    creator="Hewlett-Packard, John Vaught et al.",
    creator_country="US",
    device_class="inkjet-printhead",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="industrial",
    ip_status="patented",
    ip_citations=["US4490728"],
    prior_art_notes="HP's parallel disclosure of thermal-inkjet printing, launched commercially in the ThinkJet (HP 2225) in 1984. Independent of Canon's bubble-jet line; together they establish thermal-inkjet as a category. Anticipates: thermally pulsed liquid ejection from silicon-microfabricated chambers, replaceable printhead cartridges, and the consumable-cartridge business model that mass-microfluidics enabled.",
    sources=[
        "US4490728",
        "HP ThinkJet product history",
    ],
    disclosed_subsystems=[
        "pump-thermal-bubble-jet",
        "droplet-on-demand",
    ],
    cpc_classifications=["B41J 2/14"],
)

add(
    id="10x-genomics-chromium-controller",
    canonical_name="10x Genomics Chromium controller and Next GEM chip",
    aliases=["Chromium", "10x Next GEM"],
    corpus="private",
    first_disclosure_date="2016",
    disclosure_citation="10x Genomics Chromium platform; product literature and Zheng et al. 2017 Nat. Commun. 8, 14049. DOI: 10.1038/ncomms14049",
    creator="10x Genomics",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=[
        "US9694361B2",
        "US10301677B2",
        "US10626458B2 (and large family)",
    ],
    prior_art_notes="Commercial single-cell encapsulation platform: Chromium controller drives flow-focusing geometry on a disposable Next GEM chip, co-encapsulating cells with barcoded gel beads in droplets for downstream sequencing. Anticipates: high-throughput parallel droplet generation in a disposable thermoplastic cartridge driven by an instrument-side pneumatic pressure source, the gel-bead-in-droplet architecture for barcoded single-cell genomics, and the integration of microfluidic droplet generation with a turnkey commercial instrument workflow. Encumbered by an aggressive patent thicket; corpus entry exists to enable invalidity analysis.",
    sources=[
        "10x Genomics product literature",
        "Zheng et al. 2017 Nat. Commun. 8, 14049",
    ],
    disclosed_subsystems=[
        "droplet-flow-focusing-generation",
        "cell-encapsulation-droplet",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/68"],
    lineage_ancestors=[
        "anna-2003-flow-focusing-droplet",
        "macosko-2015-drop-seq",
    ],
)

add(
    id="bio-rad-qx-ddpcr-system",
    canonical_name="Bio-Rad QX Droplet Digital PCR system",
    aliases=["QX200", "Bio-Rad ddPCR"],
    corpus="private",
    first_disclosure_date="2011",
    disclosure_citation="Bio-Rad Laboratories QX100/QX200 ddPCR systems. Hindson et al. 2011 Anal. Chem. 83, 8604–8610. DOI: 10.1021/ac202028g",
    creator="Bio-Rad / QuantaLife",
    creator_country="US",
    device_class="droplet-generator",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US8709762B2", "US9534216B2", "various Bio-Rad/RainDance patents"],
    prior_art_notes="Discloses an integrated commercial workflow for droplet digital PCR: cartridge-based generation of ~20,000 monodisperse droplets per sample, off-chip thermal cycling, and droplet-by-droplet fluorescence readout. Anticipates: the digital-PCR workflow as a discrete commercial category, integration of injection-molded droplet-generation cartridges with an instrument-side flow controller, and a sample-to-answer ddPCR system architecture.",
    sources=[
        "Bio-Rad product literature",
        "Hindson et al. 2011 Anal. Chem. 83, 8604–8610",
    ],
    disclosed_subsystems=[
        "droplet-flow-focusing-generation",
        "thermal-droplet-pcr-cycling",
        "detection-fluorescence-on-chip",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["C12Q 1/686", "B01L 3/00"],
    lineage_ancestors=["anna-2003-flow-focusing-droplet"],
)

add(
    id="elveflow-ob1-pressure-controller",
    canonical_name="Elveflow OB1 pressure controller",
    aliases=["OB1", "Elveflow OB1 MK4"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="Elveflow OB1 product datasheet. https://www.elveflow.com/microfluidic-products/microfluidics-flow-control-systems/ob1-pressure-controller/",
    creator="Elvesys / Elveflow",
    creator_country="FR",
    device_class="flow-controller",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="trade-secret",
    prior_art_notes="Commercial multi-channel pressure controller for microfluidics, providing precise gas-pressure regulation (mbar resolution) to drive air-over-liquid flow in chips. Anticipates: instrument-side pressure regulation as a substitute for syringe pumping, integrated PID feedback on multiple independent reservoirs, and the architectural pattern of decoupling instrument pressure delivery from chip-side fluidics.",
    sources=[
        "Elveflow OB1 datasheet and user manual",
    ],
    disclosed_subsystems=[
        "pump-pressure-controlled-air-over-liquid",
        "interface-pressure-manifold",
    ],
    cpc_classifications=["G05D 16/00"],
)

add(
    id="dolomite-microfluidics-droplet-system",
    canonical_name="Dolomite Microfluidics droplet generation system",
    aliases=["Dolomite Droplet System"],
    corpus="private",
    first_disclosure_date="2009",
    disclosure_citation="Dolomite Microfluidics droplet system; product literature. https://www.dolomite-microfluidics.com",
    creator="Dolomite Microfluidics (Blacktrace Holdings)",
    creator_country="GB",
    device_class="droplet-generator",
    substrate_material="glass",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Glass-based commercial droplet generation chips and instruments aimed at research and bioprocess users. Anticipates: glass droplet-junction chips as commodity components, integration with Mitos pressure pumps, and the modular off-the-shelf microfluidics product category as opposed to bespoke PDMS chips.",
    sources=[
        "Dolomite Microfluidics product literature",
    ],
    disclosed_subsystems=[
        "droplet-t-junction-generation",
        "droplet-flow-focusing-generation",
        "fabrication-glass-thermal-bonding",
    ],
    cpc_classifications=["B01L 3/00"],
)

add(
    id="emulate-organ-on-chip-platform",
    canonical_name="Emulate Inc. Organ-Chip platform",
    aliases=["Emulate", "Bio-Kit", "Zoë"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="Emulate Inc. (Wyss spinout) Organ-Chip platform; product literature. https://www.emulatebio.com",
    creator="Emulate Inc. (Donald Ingber / Wyss spinout)",
    creator_country="US",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US8647861B2 (parent Wyss IP)", "various Emulate filings"],
    prior_art_notes="Commercial organ-on-chip platform deriving from the Huh 2010 lung-on-chip disclosure. The Zoë instrument provides perfusion and stretch actuation to standard 'Bio-Kit' organ chips. Anticipates: standardized commercial organ-chip cartridge with paired perfusion + cyclic-stretch instrument, and the organ-chip-as-a-product category.",
    sources=[
        "Emulate product literature and white papers",
    ],
    disclosed_subsystems=[
        "fabrication-pdms-soft-lithography",
        "architecture-organ-on-chip-vasculature",
        "valve-quake-pneumatic-membrane",
        "cell-organoid-perfusion",
    ],
    cpc_classifications=["C12M 1/00", "C12M 3/00"],
    lineage_ancestors=["huh-2010-lung-on-chip"],
)

add(
    id="abbott-freestyle-libre-cgm",
    canonical_name="Abbott FreeStyle Libre continuous glucose monitor",
    aliases=["FreeStyle Libre", "Libre 2", "Libre 3"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="Abbott FreeStyle Libre system; FDA approval 2017 (US); product literature. https://www.freestyle.abbott",
    creator="Abbott Diabetes Care",
    creator_country="US",
    device_class="point-of-care-cartridge",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US8073519B2", "US8512244B2", "various Abbott patents"],
    prior_art_notes="Wearable interstitial-fluid glucose sensor with a microscale filament inserted subcutaneously. Microfluidic only in a degenerate sense (single capillary-driven fluid path through a filament-supported enzyme/electrode structure), but representative of mass-deployed body-worn microfluidics. Anticipates: subcutaneous filament microsensor architecture, NFC-coupled disposable sensor + reader instrument decomposition, and the product category of disposable biosensors with multi-week wear.",
    sources=[
        "Abbott FreeStyle Libre product literature",
    ],
    disclosed_subsystems=[
        "detection-electrochemical-on-chip",
        "pump-capillary-passive",
    ],
    cpc_classifications=["A61B 5/145", "G01N 27/26"],
)

# =====================================================================
# OPEN — open-hardware microfluidics
# =====================================================================

add(
    id="metafluidics-platform",
    canonical_name="Metafluidics open microfluidics design repository",
    aliases=["Metafluidics"],
    corpus="open",
    first_disclosure_date="2018",
    disclosure_citation="Kong, D. S. et al. Open-source, community-driven microfluidics with Metafluidics. Nat. Biotechnol. 2017, 35, 523–529. DOI: 10.1038/nbt.3873; metafluidics.org repository",
    creator="MIT Lincoln Lab / Metafluidics community",
    creator_country="US",
    device_class="other",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="mixed",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Established a community-curated open-source repository of microfluidic device designs, fabrication recipes, and characterization data. Anticipates: open-source clearinghouse model for microfluidic chip designs (analogous to Addgene for plasmids); design files released under permissive licenses; community-shared characterization data alongside CAD.",
    sources=[
        "Nat. Biotechnol. 2017, 35, 523–529",
        "metafluidics.org",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="dropbot-open-source-dmf",
    canonical_name="DropBot open-source digital microfluidics platform",
    aliases=["DropBot", "DMF Toolkit"],
    corpus="open",
    first_disclosure_date="2013",
    disclosure_citation="Fobel, R.; Fobel, C.; Wheeler, A. R. DropBot: an open-source digital microfluidics control system with precise control of electrostatic driving force and instantaneous drop velocity measurement. Appl. Phys. Lett. 2013, 102, 193513. DOI: 10.1063/1.4807118",
    creator="Wheeler group, University of Toronto",
    creator_country="CA",
    device_class="digital-microfluidics",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="digital-droplet",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Disclosed an open-source DMF (digital microfluidics) control system with software, electronics, and reference EWOD chip designs released under permissive license. Anticipates: open-source EWOD instrument architecture, real-time droplet velocity feedback as a control primitive, and Python-based DMF protocol scripting.",
    sources=[
        "Appl. Phys. Lett. 2013, 102, 193513",
        "https://github.com/sci-bots/dropbot",
    ],
    disclosed_subsystems=[
        "dmf-electrowetting-on-dielectric",
        "dmf-addressable-electrode-array",
    ],
    cpc_classifications=["B01L 3/00"],
)

add(
    id="sparkfun-microfluidic-bricks",
    canonical_name="SparkFun / Pumping Lemma open microfluidic 'brick' connectors",
    aliases=["microfluidic bricks"],
    corpus="open",
    first_disclosure_date="2017",
    disclosure_citation="Pumping Lemma microfluidic bricks open-source connector system; community release. Various Hackaday and instructable disclosures from 2017 onward.",
    creator="Pumping Lemma / open community",
    creator_country="US",
    device_class="consumable-bulk",
    substrate_material="thermoplastic",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Disclosed standardized modular interlocking microfluidic 'brick' connectors enabling rapid prototyping of fluidic networks from reusable parts. Anticipates: modular microfluidic interconnect standard for rapid hobbyist / educational fluidic-network prototyping.",
    sources=[
        "Pumping Lemma community releases",
    ],
    disclosed_subsystems=[
        "interface-fluidic-edge-connector",
    ],
    cpc_classifications=["F16L 37/00"],
    draft=True,
    notes="Draft — primary citation needs cleanup; representative of a class of open-hardware microfluidic-connector projects.",
)

# =====================================================================
# FICTIONAL — narrative depictions of lab-on-chip-equivalents
# =====================================================================

add(
    id="star-trek-tricorder-medical",
    canonical_name="Star Trek medical tricorder",
    aliases=["medical tricorder", "Tricorder"],
    corpus="fictional",
    first_disclosure_date="1966",
    disclosure_citation="Star Trek (original series), 1966–1969, NBC. Medical tricorder appears across the series as Dr. McCoy's diagnostic instrument.",
    creator="Gene Roddenberry; Desilu / NBC",
    creator_country="US",
    device_class="fictional-laboratory",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Long-running narrative depiction of a handheld diagnostic instrument performing rapid multiplexed measurements on a single patient sample. Cited (notably during the X-Prize Tricorder competition framing) as the conceptual ancestor of handheld point-of-care diagnostic devices. As 102 prior art for 'handheld portable multiplex medical diagnostic instrument as a category', Star Trek's depiction predates every commercial implementation by decades.",
    sources=[
        "Star Trek (TOS) 1966–1969",
        "Memory Alpha: Tricorder",
        "Qualcomm Tricorder X-Prize history",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
    ],
    cpc_classifications=[],
    notes="Fictional but doctrinally relevant: §102 prior art does not require enablement of every claim element, and depicting a category in advance of its commercial implementation has been cited successfully in invalidity proceedings (cf. Vornado v. Hunter Fan).",
)

add(
    id="andromeda-strain-isolation-chamber",
    canonical_name="The Andromeda Strain isolation/analysis lab",
    aliases=["Wildfire lab", "Andromeda Strain lab"],
    corpus="fictional",
    first_disclosure_date="1969",
    disclosure_citation="Crichton, M. The Andromeda Strain. Knopf, New York, 1969.",
    creator="Michael Crichton",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="analytical",
    ip_status="fictional",
    prior_art_notes="Narrative description of a fully-automated multilevel containment laboratory performing sequential automated analyses on a single sample under sterile conditions. The depiction predates µTAS (Manz 1990) by 21 years. Doctrinally relevant for invalidity contention against patents claiming 'integrated automated multi-step pathogen analysis' as a generic category.",
    sources=[
        "Crichton, M. The Andromeda Strain. 1969.",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="gattaca-instant-genome-readout",
    canonical_name="Gattaca instant genome / blood readout console",
    aliases=["Gattaca DNA reader"],
    corpus="fictional",
    first_disclosure_date="1997",
    disclosure_citation="Gattaca (film), Andrew Niccol, Columbia Pictures, 1997.",
    creator="Andrew Niccol; Columbia Pictures",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Narrative depiction of routine push-button blood/saliva genetic readout devices as ubiquitous workplace fixtures. Predates rapid POC molecular testing commercial availability by ~20 years. Cited as conceptual prior art for 'consumer-grade ubiquitous push-button genetic identity verification' device category.",
    sources=[
        "Gattaca (1997)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="theranos-promised-cartridge",
    canonical_name="Theranos Edison / miniLab cartridge (claimed)",
    aliases=["Theranos cartridge", "Edison", "miniLab"],
    corpus="private",
    first_disclosure_date="2003",
    disclosure_citation="Theranos Inc. patent filings beginning 2003 (US7635594B2 and family); SEC v. Theranos litigation record.",
    creator="Theranos Inc.",
    creator_country="US",
    device_class="point-of-care-cartridge",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US7635594B2", "US8088593B2", "various Theranos filings"],
    prior_art_notes="Patent filings disclosed an asserted single-cartridge multi-test blood diagnostic platform from finger-stick volumes. The filings stand as 102/103 art regardless of whether the company successfully reduced to practice; many subsequent POC-blood patents must contend with these filings as anticipating prior art for 'finger-stick-volume multi-assay cartridge as architecture.' Inclusion in this corpus is not an endorsement of the product's claimed performance.",
    sources=[
        "US7635594B2 and Theranos patent family",
        "Carreyrou, J. Bad Blood. 2018.",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "architecture-multiplex-cartridge",
    ],
    cpc_classifications=["B01L 3/00", "G01N 33/48"],
    notes="Included for completeness — the patent filings are real prior art whether or not the device worked.",
)


# =====================================================================
# Write out
# =====================================================================
with OUT.open("w") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  wrote {len(ENTRIES)} entries to {OUT}")
