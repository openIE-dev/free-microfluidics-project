#!/usr/bin/env python3
"""Second expansion seed for free-microfluidics-corpus.

Appends ~50 more entries covering:
  - DEP / dielectrophoresis lineage (Pohl 1951, Gascoyne, Voldman)
  - magnetic cell sorting (Miltenyi MACS)
  - more µTAS-era foundations (Manz/Widmer 1990, Effenhauser, Jacobson)
  - optofluidics (Psaltis, Whitesides, ARROW waveguides)
  - body-on-chip / multi-organ (Wikswo)
  - digital PCR (Vogelstein-Kinzler 1999)
  - sequencing (Illumina flow cell, Ion Torrent, ONT MinION, PacBio SMRT)
  - biotech cartridges (Quanterix Simoa, Akoya, NanoString, Visium)
  - POC diagnostics (BinaxNOW, BD Veritor, SD Biosensor)
  - more fictional (Wildfire, Six Million Dollar Man, Ghost in the Shell)
  - more open hardware (Chi.Bio, eVOLVER, Squid, OpenSPIM)
  - fluidic logic (Stanford fluidic computer, microfluidic logic)
  - more patent-thicket (Element Biosciences, Singular Genomics, Quantum-Si)
"""
import json
from pathlib import Path

CORPUS = Path(__file__).parent / "corpus.jsonl"
ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 2)
    kw.setdefault("last_updated", "2026-05-09")
    ENTRIES.append(kw)


# =====================================================================
# ACADEMIC — foundational additions
# =====================================================================

add(
    id="manz-widmer-1990-utas-framing",
    canonical_name="Miniaturized total chemical analysis systems: a novel concept for chemical sensing",
    aliases=["µTAS framing paper", "Manz-Widmer 1990"],
    corpus="academic",
    first_disclosure_date="1990",
    disclosure_citation="Manz, A.; Graber, N.; Widmer, H. M. Miniaturized total chemical analysis systems: a novel concept for chemical sensing. Sens. Actuators B Chem. 1990, 1, 244–248. DOI: 10.1016/0925-4005(90)80209-I",
    creator="Manz, Graber, Widmer (Ciba-Geigy)",
    creator_country="CH",
    device_class="other",
    end_application="analytical",
    ip_status="public-domain",
    prior_art_notes="The framing paper that named the field 'micro total analysis systems' (µTAS). Companion to the Manz CE-on-chip 1990 disclosure but distinct: this paper articulates the conceptual program of integrating sample-prep, separation, and detection on a single chip. Anticipates: the integrated-analytical-system framing that subsequently structured a generation of microfluidics research and gave the field its first international conference series (MicroTAS). Cited as the ur-reference for 'lab-on-a-chip' as a research program.",
    sources=[
        "Sens. Actuators B Chem. 1990, 1, 244–248",
        "DOI 10.1016/0925-4005(90)80209-I",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["B01L 3/00"],
)

add(
    id="effenhauser-1993-glass-microchip-electrophoresis",
    canonical_name="High-speed separation of antisense oligonucleotides on a micromachined capillary electrophoresis device",
    aliases=["Effenhauser 1993"],
    corpus="academic",
    first_disclosure_date="1993",
    disclosure_citation="Effenhauser, C. S.; Manz, A.; Widmer, H. M. Glass chips used as micro-reactors for chemical synthesis and electrophoresis. Anal. Chem. 1993, 65, 2637–2642. DOI: 10.1021/ac00067a015",
    creator="Manz group, Ciba-Geigy / Hewlett-Packard",
    creator_country="CH",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="analytical",
    ip_status="public-domain",
    prior_art_notes="Demonstrated practical high-speed separation of oligonucleotides on a glass micromachined CE chip. With Harrison 1992 establishes glass chip CE as a working analytical technique rather than a curiosity. Anticipates: glass-CE as the workhorse architecture for the first commercial chip electrophoresis systems (Agilent 2100 Bioanalyzer, Caliper LabChip).",
    sources=[
        "Anal. Chem. 1993, 65, 2637–2642",
        "DOI 10.1021/ac00067a015",
    ],
    disclosed_subsystems=[
        "separation-capillary-electrophoresis",
        "fabrication-glass-hf-etching",
    ],
    cpc_classifications=["B01L 3/00", "G01N 27/447"],
    lineage_ancestors=["harrison-1992-cap-electrophoresis-on-chip", "manz-1990-microchip-cap-electrophoresis"],
)

add(
    id="jacobson-1994-pinched-injection",
    canonical_name="Pinched injection on glass CE microchips",
    aliases=["Jacobson 1994 pinched injection"],
    corpus="academic",
    first_disclosure_date="1994",
    disclosure_citation="Jacobson, S. C.; Hergenroder, R.; Koutny, L. B.; Warmack, R. J.; Ramsey, J. M. Effects of injection schemes and column geometry on the performance of microchip electrophoresis devices. Anal. Chem. 1994, 66, 1107–1113. DOI: 10.1021/ac00079a028",
    creator="J. M. Ramsey group, Oak Ridge National Lab",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="analytical",
    ip_status="public-domain",
    prior_art_notes="Disclosed pinched-injection geometry for chip CE: a four-port crossed-channel layout with simultaneously pulled sample-and-buffer arms generates a precisely defined sub-nanoliter sample plug. Anticipates: pinched-injection cross geometry as the standard chip-CE injection primitive, used in essentially every subsequent commercial CE chip. Among Ramsey's most-cited microfluidics papers.",
    sources=[
        "Anal. Chem. 1994, 66, 1107–1113",
        "DOI 10.1021/ac00079a028",
    ],
    disclosed_subsystems=[
        "separation-capillary-electrophoresis",
        "fabrication-glass-hf-etching",
    ],
    cpc_classifications=["B01L 3/00", "G01N 27/447"],
    lineage_ancestors=["harrison-1992-cap-electrophoresis-on-chip"],
)

add(
    id="pohl-1951-dielectrophoresis-foundation",
    canonical_name="The motion and precipitation of suspensoids in divergent electric fields (dielectrophoresis foundation)",
    aliases=["Pohl 1951 DEP", "Pohl dielectrophoresis"],
    corpus="academic",
    first_disclosure_date="1951",
    disclosure_citation="Pohl, H. A. The motion and precipitation of suspensoids in divergent electric fields. J. Appl. Phys. 1951, 22, 869–871. DOI: 10.1063/1.1700065",
    creator="H. A. Pohl",
    creator_country="US",
    device_class="other",
    flow_regime="electrokinetic",
    end_application="analytical",
    ip_status="public-domain",
    prior_art_notes="Foundational disclosure of dielectrophoresis (DEP): the motion of polarizable particles in non-uniform electric fields, distinct from electrophoresis (which moves charged particles in uniform fields). Predates microfluidics by 40 years. Anticipates: the entire DEP-on-chip subfield (Gascoyne, Voldman, Pethig). Critical because much later DEP-on-chip disclosure can be reduced in scope by reaching back to Pohl for the foundational physics.",
    sources=[
        "J. Appl. Phys. 1951, 22, 869–871",
        "Pohl, H. A. Dielectrophoresis. Cambridge UP 1978 (book-length treatment)",
    ],
    disclosed_subsystems=[
        "separation-dielectrophoresis",
    ],
    cpc_classifications=["G01N 27/447"],
)

add(
    id="gascoyne-2002-dep-cancer-cells",
    canonical_name="Dielectrophoresis-based separation of human cancer cells from blood",
    aliases=["Gascoyne DEP", "Gascoyne 2002"],
    corpus="academic",
    first_disclosure_date="2002",
    disclosure_citation="Gascoyne, P. R. C.; Vykoukal, J. Particle separation by dielectrophoresis. Electrophoresis 2002, 23, 1973–1983. DOI: 10.1002/1522-2683(200207)23:13<1973::AID-ELPS1973>3.0.CO;2-1",
    creator="Gascoyne group, MD Anderson",
    creator_country="US",
    device_class="separator-component",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US7081189B2 (Gascoyne DEP family)"],
    prior_art_notes="Established practical DEP-FFF (dielectrophoretic field-flow fractionation) for cell separation, particularly CTC enrichment from blood. Demonstrates positive-DEP capture of cancer cells against negative-DEP blood cells using castellated electrode arrays. Anticipates: castellated-electrode-array DEP architecture, DEP-FFF as a continuous-flow separation method, and the commercial DEPArray and ApoCell platforms.",
    sources=[
        "Electrophoresis 2002, 23, 1973–1983",
    ],
    disclosed_subsystems=[
        "separation-dielectrophoresis",
        "fabrication-glass-hf-etching",
    ],
    cpc_classifications=["B01L 3/00", "G01N 15/02"],
    lineage_ancestors=["pohl-1951-dielectrophoresis-foundation"],
)

add(
    id="voldman-2002-cell-trap-dep-array",
    canonical_name="Microfabricated dielectrophoretic single-cell trap arrays",
    aliases=["Voldman 2002 DEP trap", "Voldman cage"],
    corpus="academic",
    first_disclosure_date="2002",
    disclosure_citation="Voldman, J.; Gray, M. L.; Toner, M.; Schmidt, M. A. A microfabrication-based dynamic array cytometer. Anal. Chem. 2002, 74, 3984–3990. DOI: 10.1021/ac0256235",
    creator="Voldman, Toner, Schmidt (MIT / Harvard)",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed addressable DEP cage arrays for trapping individual cells at defined positions while preserving viability and dynamic release. Anticipates: addressable-DEP-cage-array architecture for single-cell capture, dynamic single-cell release for downstream off-chip analysis, and the commercial Menarini DEPArray platform that became the dominant tool for rare-cell isolation in oncology.",
    sources=[
        "Anal. Chem. 2002, 74, 3984–3990",
    ],
    disclosed_subsystems=[
        "separation-dielectrophoresis",
        "fabrication-silicon-drie",
    ],
    cpc_classifications=["B01L 3/00"],
    lineage_ancestors=["pohl-1951-dielectrophoresis-foundation"],
)

add(
    id="miltenyi-1990-macs-magnetic-cell-sorting",
    canonical_name="Magnetic-activated cell sorting (MACS)",
    aliases=["MACS", "Miltenyi MACS"],
    corpus="academic",
    first_disclosure_date="1990",
    disclosure_citation="Miltenyi, S.; Müller, W.; Weichel, W.; Radbruch, A. High gradient magnetic cell separation with MACS. Cytometry 1990, 11, 231–238. DOI: 10.1002/cyto.990110203",
    creator="Miltenyi et al., founder of Miltenyi Biotec",
    creator_country="DE",
    device_class="separator-component",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="patented",
    ip_citations=["EP0149240A1 (and Miltenyi family)"],
    prior_art_notes="Disclosed high-gradient magnetic cell separation using ferromagnetic-bead-coated antibodies in a column packed with steel matrix in a strong external field. Industrially the foundational immunomagnetic cell separation chemistry, although the column form is non-microfluidic. Critical context for microfluidic immunomagnetic separation: every CTC-iChip and IsoFlux-style architecture is the chip-scale descendant of the MACS column.",
    sources=[
        "Cytometry 1990, 11, 231–238",
        "Miltenyi Biotec product literature",
    ],
    disclosed_subsystems=[
        "separation-magnetophoresis",
    ],
    cpc_classifications=["G01N 33/543"],
    notes="Not microfluidic itself. Included because microfluidic immunomagnetic-separation patents must be evaluated against its 35-year-old prior art.",
)

add(
    id="vogelstein-kinzler-1999-digital-pcr",
    canonical_name="Digital PCR",
    aliases=["Vogelstein 1999 digital PCR"],
    corpus="academic",
    first_disclosure_date="1999",
    disclosure_citation="Vogelstein, B.; Kinzler, K. W. Digital PCR. Proc. Natl. Acad. Sci. USA 1999, 96, 9236–9241. DOI: 10.1073/pnas.96.16.9236",
    creator="Vogelstein, Kinzler (Johns Hopkins)",
    creator_country="US",
    device_class="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US6440706B1 (and Hopkins/Bert family)"],
    prior_art_notes="Disclosed digital PCR: dilute the template such that each well contains 0 or 1 copy, run end-point PCR, and count positive wells against Poisson distribution to obtain absolute copy number without a standard curve. Originally implemented in plate format. Anticipates: the entire digital-PCR concept that subsequently was implemented in droplets (Bio-Rad QX/RainDance), microwell arrays (Fluidigm), and chip arrays (Stilla, Thermo). The Bio-Rad QX ddPCR cartridge (separate entry) descends directly from this disclosure as a droplet-format implementation.",
    sources=[
        "Proc. Natl. Acad. Sci. USA 1999, 96, 9236–9241",
    ],
    disclosed_subsystems=[
        "thermal-droplet-pcr-cycling",
    ],
    cpc_classifications=["C12Q 1/686"],
    lineage_descendants=["bio-rad-qx-ddpcr-cartridge"],
)

add(
    id="huh-2007-lung-on-chip-precursor",
    canonical_name="Acoustically detectable cellular-level lung injury model",
    aliases=["Huh 2007 acoustic lung", "Lung-on-chip precursor"],
    corpus="academic",
    first_disclosure_date="2007",
    disclosure_citation="Huh, D.; Fujioka, H.; Tung, Y.-C.; Futai, N.; Paine, R., 3rd; Grotberg, J. B.; Takayama, S. Acoustically detectable cellular-level lung injury induced by fluid mechanical stresses in microfluidic airway systems. Proc. Natl. Acad. Sci. USA 2007, 104, 18886–18891. DOI: 10.1073/pnas.0610868104",
    creator="Takayama group, Michigan",
    creator_country="US",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Direct precursor to the Huh-Ingber 2010 lung-on-chip paper; demonstrated airway-stress modeling in PDMS chips. Establishes the Takayama-group lineage that connects to Ingber's Wyss Institute lung-on-chip and ultimately Emulate's commercial platform. Important for tracing the academic-to-commercial pathway of organ-on-chip work.",
    sources=[
        "Proc. Natl. Acad. Sci. USA 2007, 104, 18886–18891",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "C12M 1/00"],
    lineage_descendants=["huh-2010-lung-on-chip"],
)

add(
    id="wikswo-2013-multi-organ-chip",
    canonical_name="Engineering multi-organ microphysiological systems (multi-organ-on-chip)",
    aliases=["Wikswo body-on-chip", "multi-organ-on-chip"],
    corpus="academic",
    first_disclosure_date="2013",
    disclosure_citation="Wikswo, J. P.; Curtis, E. L.; Eagleton, Z. E.; Evans, B. C.; Kole, A.; Hofmeister, L. H.; Matloff, W. J. Scaling and systems biology for integrating multiple organs-on-a-chip. Lab Chip 2013, 13, 3496–3511. DOI: 10.1039/c3lc50243k",
    creator="Wikswo group, Vanderbilt",
    creator_country="US",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Established the multi-organ-on-chip / body-on-chip framing: scaling rules for connecting multiple organ chips into a perfused circulation that approximates whole-body physiology. Anticipates: multi-organ chip architectures, scaling-law-based design (residence time, surface-to-volume ratio), and the framing of organ-on-chip as a drug-development platform rather than a single-tissue assay. Cornerstone reference for HESI body-on-chip programs and the FDA Modernization Act 2.0 alternatives-to-animal-testing landscape.",
    sources=[
        "Lab Chip 2013, 13, 3496–3511",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-organ-on-chip-vasculature",
    ],
    cpc_classifications=["C12M 1/00"],
    lineage_descendants=["huh-2010-lung-on-chip"],
)

add(
    id="psaltis-2006-optofluidic-review",
    canonical_name="Developing optofluidic technology through the fusion of microfluidics and optics",
    aliases=["Psaltis 2006 optofluidics"],
    corpus="academic",
    first_disclosure_date="2006",
    disclosure_citation="Psaltis, D.; Quake, S. R.; Yang, C. Developing optofluidic technology through the fusion of microfluidics and optics. Nature 2006, 442, 381–386. DOI: 10.1038/nature05060",
    creator="Psaltis (Caltech), Quake (Caltech), Yang (Caltech)",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Framing review establishing 'optofluidics' as a research program: the integration of microfluidics with optical waveguides, lasers, lenses, and resonators to make tunable photonic devices. Anticipates: liquid-core optical waveguides (ARROW), tunable microfluidic lenses, and integrated detection on-chip. Methodological review that defined the optofluidics field.",
    sources=[
        "Nature 2006, 442, 381–386",
    ],
    disclosed_subsystems=[
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["B01L 3/00", "G02B 6/00"],
)

add(
    id="schmidt-hawkins-arrow-waveguide",
    canonical_name="ARROW liquid-core optical waveguide on chip",
    aliases=["ARROW waveguide", "Schmidt-Hawkins ARROW"],
    corpus="academic",
    first_disclosure_date="2004",
    disclosure_citation="Yin, D.; Schmidt, H.; Barber, J. P.; Hawkins, A. R. Integrated ARROW waveguides with hollow cores. Opt. Express 2004, 12, 2710–2715. DOI: 10.1364/OPEX.12.002710",
    creator="Schmidt (UCSC), Hawkins (BYU)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="passive",
    end_application="analytical",
    ip_status="patented",
    prior_art_notes="Disclosed antiresonant reflecting optical waveguide (ARROW) with a hollow core that can be filled with sample fluid: a liquid-core waveguide enabling guided light through the analyte itself. Anticipates: liquid-core integrated waveguides, on-chip absorbance/fluorescence in-line analysis without external optical components, and ultra-sensitive single-molecule detection by guided-mode interaction. Foundational architecture for chip-integrated optical detection.",
    sources=[
        "Opt. Express 2004, 12, 2710–2715",
    ],
    disclosed_subsystems=[
        "detection-fluorescence-on-chip",
        "fabrication-silicon-drie",
    ],
    cpc_classifications=["G02B 6/032", "B01L 3/00"],
)

add(
    id="bentley-2008-illumina-flow-cell",
    canonical_name="Illumina Solexa sequencing flow cell",
    aliases=["Solexa flow cell", "Illumina flow cell"],
    corpus="academic",
    first_disclosure_date="2008",
    disclosure_citation="Bentley, D. R. et al. Accurate whole human genome sequencing using reversible terminator chemistry. Nature 2008, 456, 53–59. DOI: 10.1038/nature07517",
    creator="Bentley et al., Illumina / Solexa",
    creator_country="GB",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US7541444B2", "US7771973B2 (and large Illumina family)"],
    prior_art_notes="Foundational disclosure of the Illumina sequencing flow cell: a glass channel with patterned oligo lawn supporting bridge amplification, reversible-terminator sequencing chemistry, and per-channel optical scanning. Architecturally a microfluidic device, although it is rarely classified as one in microfluidics literature. Anticipates: patterned-flow-cell architecture for massively parallel single-molecule chemistry, and the entire Illumina commercial sequencing platform that dominated the genomics market 2010–2025.",
    sources=[
        "Nature 2008, 456, 53–59",
    ],
    disclosed_subsystems=[
        "fabrication-glass-thermal-bonding",
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["C12Q 1/68", "B01L 3/00"],
)

add(
    id="rothberg-2011-ion-torrent",
    canonical_name="Ion Torrent semiconductor sequencing chip",
    aliases=["Ion Torrent", "Personal Genome Machine"],
    corpus="academic",
    first_disclosure_date="2011",
    disclosure_citation="Rothberg, J. M. et al. An integrated semiconductor device enabling non-optical genome sequencing. Nature 2011, 475, 348–352. DOI: 10.1038/nature10242",
    creator="Rothberg et al., Ion Torrent / Life Technologies",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US7948015B2", "US8262900B2 (Ion Torrent family)"],
    prior_art_notes="Disclosed semiconductor sequencing: a CMOS chip with millions of pH-sensitive microwells, each with a single template-loaded bead, where polymerase-incorporation H+ release is detected by ISFET sensing. Architecturally a hybrid silicon-microfluidic-MEMS-CMOS device. Anticipates: integrated CMOS-fluidic sequencing, ISFET-array-as-sensor architecture, and the entire 'sequencing-on-a-chip' family that subsequently expanded to Roche 454, ONT MinION, PacBio, Element Biosciences AVITI, Singular Genomics G4.",
    sources=[
        "Nature 2011, 475, 348–352",
    ],
    disclosed_subsystems=[
        "detection-electrochemical-on-chip",
        "fabrication-silicon-drie",
    ],
    cpc_classifications=["C12Q 1/68", "B01L 3/00"],
)

add(
    id="clarke-2009-nanopore-sequencing",
    canonical_name="Single-molecule DNA sequencing through nanopore",
    aliases=["Clarke 2009 nanopore", "ONT MinION precursor"],
    corpus="academic",
    first_disclosure_date="2009",
    disclosure_citation="Clarke, J.; Wu, H.-C.; Jayasinghe, L.; Patel, A.; Reid, S.; Bayley, H. Continuous base identification for single-molecule nanopore DNA sequencing. Nat. Nanotechnol. 2009, 4, 265–270. DOI: 10.1038/nnano.2009.12",
    creator="Bayley group, Oxford / Oxford Nanopore Technologies",
    creator_country="GB",
    device_class="lab-on-chip",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="electrokinetic",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Foundational disclosure for nanopore-based DNA sequencing: continuous base identification by ionic-current modulation as DNA strands traverse a protein nanopore. Direct ancestor of Oxford Nanopore Technologies' MinION, GridION, and PromethION platforms. The MinION cartridge is microfluidic in the strict sense (an array of nanopore sensors in flow channels). Anticipates: nanopore-array-as-sensor microfluidic architecture, single-molecule electronic sequencing without optical detection.",
    sources=[
        "Nat. Nanotechnol. 2009, 4, 265–270",
    ],
    disclosed_subsystems=[
        "detection-electrochemical-on-chip",
    ],
    cpc_classifications=["C12Q 1/68", "G01N 33/487"],
)

add(
    id="eid-2009-pacbio-smrt",
    canonical_name="Real-time DNA sequencing from single polymerase molecules (PacBio SMRT)",
    aliases=["PacBio SMRT", "Eid 2009 SMRT"],
    corpus="academic",
    first_disclosure_date="2009",
    disclosure_citation="Eid, J. et al. Real-time DNA sequencing from single polymerase molecules. Science 2009, 323, 133–138. DOI: 10.1126/science.1162986",
    creator="Pacific Biosciences",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US7170050B2 (and PacBio ZMW family)"],
    prior_art_notes="Disclosed Single-Molecule Real-Time (SMRT) sequencing using zero-mode waveguides (ZMWs) — sub-wavelength metal apertures that confine fluorescence excitation to zeptoliter-scale volumes around individual immobilized polymerases. Anticipates: ZMW-array architecture, single-molecule fluorescence sequencing without amplification, and the long-read sequencing market commercialized by PacBio.",
    sources=[
        "Science 2009, 323, 133–138",
    ],
    disclosed_subsystems=[
        "detection-fluorescence-on-chip",
        "fabrication-silicon-drie",
    ],
    cpc_classifications=["C12Q 1/68"],
)

add(
    id="rissin-2010-quanterix-simoa",
    canonical_name="Single molecule arrays (Simoa) for ultrasensitive immunoassay",
    aliases=["Quanterix Simoa", "Rissin 2010 single molecule arrays"],
    corpus="academic",
    first_disclosure_date="2010",
    disclosure_citation="Rissin, D. M. et al. Single-molecule enzyme-linked immunosorbent assay detects serum proteins at subfemtomolar concentrations. Nat. Biotechnol. 2010, 28, 595–599. DOI: 10.1038/nbt.1641",
    creator="Walt group, Tufts / Quanterix",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US8222047B2 (and Quanterix family)"],
    prior_art_notes="Disclosed single-molecule immunoassay (Simoa): trap individual antibody-functionalized beads in femtoliter microwells, isolate by oil overlay to digitize fluorogenic-substrate signal per bead. Anticipates: femtoliter-microwell-array architecture for digital ELISA, oil-isolated chamber arrays for single-molecule chemistry, and the Quanterix HD-X / SR-X commercial platforms. Sub-femtomolar protein detection in serum.",
    sources=[
        "Nat. Biotechnol. 2010, 28, 595–599",
    ],
    disclosed_subsystems=[
        "fabrication-glass-thermal-bonding",
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["G01N 33/543", "B01L 3/00"],
)

add(
    id="goldman-2014-codex-akoya",
    canonical_name="CODEX multiplexed antibody imaging (Akoya CODEX/PhenoCycler)",
    aliases=["CODEX", "Akoya PhenoCycler"],
    corpus="academic",
    first_disclosure_date="2014",
    disclosure_citation="Goltsev, Y.; Samusik, N.; Kennedy-Darling, J.; Bhate, S.; Hale, M.; Vazquez, G.; Black, S.; Nolan, G. P. Deep profiling of mouse splenic architecture with CODEX multiplexed imaging. Cell 2018, 174, 968–981.e15. DOI: 10.1016/j.cell.2018.07.010",
    creator="Nolan group, Stanford / Akoya Biosciences",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US10995361B2 (and Akoya family)"],
    prior_art_notes="Disclosed iterative-fluidic-cycling multiplexed immunofluorescence: oligonucleotide-tagged antibodies are revealed sequentially by complementary fluorophore-coupled reporters delivered through an automated fluidic cycler atop a tissue-section flow cell. Anticipates: iterative-fluidic-multiplexing architecture for spatial proteomics, and the Akoya PhenoCycler commercial platform.",
    sources=[
        "Cell 2018, 174, 968–981.e15",
    ],
    disclosed_subsystems=[
        "architecture-multiplex-cartridge",
    ],
    cpc_classifications=["G01N 33/53"],
)

add(
    id="staahl-2016-spatial-transcriptomics",
    canonical_name="Spatial transcriptomics (Visium / Slide-seq ancestors)",
    aliases=["Ståhl 2016 spatial transcriptomics"],
    corpus="academic",
    first_disclosure_date="2016",
    disclosure_citation="Ståhl, P. L. et al. Visualization and analysis of gene expression in tissue sections by spatial transcriptomics. Science 2016, 353, 78–82. DOI: 10.1126/science.aaf2403",
    creator="Lundeberg group, Stockholm / 10x Genomics Visium",
    creator_country="SE",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="patented",
    ip_citations=["US10472669B2 (10x Genomics spatial family)"],
    prior_art_notes="Disclosed spatial transcriptomics: a glass slide patterned with spatially-barcoded oligonucleotide capture probes, on which a tissue section is mounted and permeabilized to capture mRNA at known x,y positions. Anticipates: spatial-barcode-grid architecture for transcriptomics, and the 10x Genomics Visium / Visium HD platforms which extended the resolution from 100 µm to sub-cellular scale. Microfluidic in the sense that diffusion-mediated capture is the operative transport mechanism.",
    sources=[
        "Science 2016, 353, 78–82",
    ],
    disclosed_subsystems=[
        "architecture-spatial-barcoded-array",
    ],
    cpc_classifications=["C12Q 1/6841"],
    lineage_descendants=["10x-genomics-chromium-controller"],
)

add(
    id="mathies-1995-radial-cap-array",
    canonical_name="Radial capillary-array electrophoresis chip",
    aliases=["Mathies 1995 radial array"],
    corpus="academic",
    first_disclosure_date="1995",
    disclosure_citation="Woolley, A. T.; Mathies, R. A. Ultra-high-speed DNA sequencing using capillary electrophoresis chips. Anal. Chem. 1995, 67, 3676–3680. DOI: 10.1021/ac00116a010",
    creator="R. A. Mathies group, UC Berkeley",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="analytical",
    ip_status="patented",
    prior_art_notes="Demonstrated 96-channel radial CE array on a single 100-mm glass wafer for parallel DNA sequencing reads. Anticipates: radial-channel-array architecture for parallel CE, glass-chip-as-replacement-for-slab-gel for sequencing, and the Caliper LabChip / Agilent Bioanalyzer commercial platforms. Established the wafer-scale parallelism paradigm in chip CE.",
    sources=[
        "Anal. Chem. 1995, 67, 3676–3680",
    ],
    disclosed_subsystems=[
        "separation-capillary-electrophoresis",
        "fabrication-glass-hf-etching",
    ],
    cpc_classifications=["B01L 3/00", "G01N 27/447"],
    lineage_ancestors=["harrison-1992-cap-electrophoresis-on-chip"],
)

add(
    id="terry-1979-stanford-gas-chromatograph",
    canonical_name="Miniaturized gas chromatograph on a silicon wafer (Stanford 1979)",
    aliases=["Terry 1979 GC", "Stanford miniaturized GC"],
    corpus="academic",
    first_disclosure_date="1979",
    disclosure_citation="Terry, S. C.; Jerman, J. H.; Angell, J. B. A gas chromatographic air analyzer fabricated on a silicon wafer. IEEE Trans. Electron Devices 1979, 26, 1880–1886. DOI: 10.1109/T-ED.1979.19791",
    creator="Terry, Jerman, Angell (Stanford)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="analytical",
    ip_status="public-domain",
    prior_art_notes="The first paper widely cited as a microfluidic-equivalent device: a 5-cm silicon wafer integrating a sample-injection valve, 1.5-meter spiral GC column, and a thermal conductivity detector. Predates Manz/Widmer's µTAS framing by 11 years and Manz's CE-on-chip by 11 years. Anticipates: silicon-substrate microfluidic chip as integrated analytical instrument, on-chip valves and integrated detection, and the entire silicon-microfluidic precursor literature. Often called the 'first lab-on-a-chip' although that term wasn't coined until much later.",
    sources=[
        "IEEE Trans. Electron Devices 1979, 26, 1880–1886",
    ],
    disclosed_subsystems=[
        "fabrication-silicon-drie",
        "fabrication-glass-anodic-bonding",
    ],
    cpc_classifications=["G01N 30/60", "B01L 3/00"],
)

add(
    id="reyes-2002-utas-history-review",
    canonical_name="Micro total analysis systems. 1. Introduction, theory, and technology",
    aliases=["Reyes 2002 µTAS review"],
    corpus="academic",
    first_disclosure_date="2002",
    disclosure_citation="Reyes, D. R.; Iossifidis, D.; Auroux, P.-A.; Manz, A. Micro total analysis systems. 1. Introduction, theory, and technology. Anal. Chem. 2002, 74, 2623–2636. DOI: 10.1021/ac0202435",
    creator="Manz group, Imperial College / NIST",
    creator_country="GB",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Manz-group decadal review of µTAS at its 12-year mark. Cited as a standard reference for the early-µTAS-era technology landscape. Methodological — establishes which technologies were considered state of the art in 2002 and is therefore useful as 'state of the art at filing date' evidence for any patent filed shortly after.",
    sources=[
        "Anal. Chem. 2002, 74, 2623–2636",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# =====================================================================
# PRIVATE — more cartridges, instruments, patent-thicket holders
# =====================================================================

add(
    id="abbott-binaxnow-rapid-antigen",
    canonical_name="Abbott BinaxNOW rapid antigen test cassette",
    aliases=["BinaxNOW", "Abbott rapid antigen"],
    corpus="private",
    first_disclosure_date="1996",
    disclosure_citation="Abbott BinaxNOW product family (originally Binax Inc., acquired by Inverness/Alere then Abbott). FDA EUA December 2020 for COVID-19 antigen.",
    creator="Binax Inc. → Inverness → Alere → Abbott",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Lateral-flow rapid antigen cartridge with cassette housing, swab application port, buffer well, and double-line readout. Architecturally a follow-on to OraSure-class lateral-flow cassettes; commercially the dominant US over-the-counter COVID-19 home test 2020–2023. Anticipates: integrated cassette-housing + buffer-well + swab-port form factor that defined the COVID-era rapid-antigen test category.",
    sources=[
        "Abbott BinaxNOW product literature",
        "FDA EUA",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
    ],
    cpc_classifications=["G01N 33/543"],
    lineage_ancestors=["orasure-quickflex-cartridge"],
)

add(
    id="bd-veritor-cartridge",
    canonical_name="BD Veritor System cartridge",
    aliases=["BD Veritor"],
    corpus="private",
    first_disclosure_date="2010",
    disclosure_citation="BD Veritor System product family. https://www.bd.com",
    creator="Becton, Dickinson and Company",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Lateral-flow antigen cartridge architecturally similar to BinaxNOW, with reflectance-readout instrument distinguishing positive lines below visible-detection threshold. Anticipates: instrument-read lateral-flow as a hybrid between purely visual rapid antigen tests and full molecular diagnostic instruments.",
    sources=[
        "BD Veritor product literature",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
    ],
    cpc_classifications=["G01N 33/543"],
)

add(
    id="standard-biotools-csg-fluidigm",
    canonical_name="Standard BioTools (formerly Fluidigm) C1 single-cell genomics IFC",
    aliases=["C1", "Fluidigm C1", "Standard BioTools C1"],
    corpus="private",
    first_disclosure_date="2013",
    disclosure_citation="Fluidigm Corp. C1 system (now Standard BioTools). Pollen et al. 2014 Nat. Biotechnol. 32, 1053–1058. DOI: 10.1038/nbt.2967",
    creator="Fluidigm (now Standard BioTools)",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["(Fluidigm IFC family + C1-specific extensions)"],
    prior_art_notes="Single-cell capture-and-amplify IFC: 96 chambers each receiving exactly one cell by hydrodynamic trap, then automated lysis, RT, and PCR per chamber for downstream sequencing. Architectural ancestor of all subsequent microfluidic-trap single-cell genomics, including 10x Chromium's droplet successor. Largely displaced by droplet platforms after 2015 because of cost-per-cell, but retains use in low-throughput high-fidelity work.",
    sources=[
        "Fluidigm C1 product literature",
        "Pollen et al. 2014 Nat. Biotechnol. 32, 1053–1058",
    ],
    disclosed_subsystems=[
        "valve-quake-pneumatic-membrane",
        "cell-trap-hydrodynamic",
        "fabrication-pdms-soft-lithography",
        "thermal-pcr-cycling",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/6841"],
    lineage_ancestors=["unger-2000-quake-monolithic-membrane-valve", "thorsen-2002-microfluidic-large-scale-integration"],
)

add(
    id="element-biosciences-aviti",
    canonical_name="Element Biosciences AVITI sequencer flow cell",
    aliases=["AVITI", "Element Biosciences AVITI"],
    corpus="private",
    first_disclosure_date="2022",
    disclosure_citation="Element Biosciences AVITI system. https://www.elementbiosciences.com",
    creator="Element Biosciences",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Patterned-flow-cell sequencer using avidite chemistry — a polymer-tethered fluorescent reporter for sequencing-by-synthesis distinct from Illumina's reversible terminator. Architecturally a flow cell similar to Illumina but with patent-free chemistry. Part of the post-2020 Illumina-IP-expiry wave of competing patterned-flow-cell sequencers.",
    sources=[
        "Element Biosciences product literature",
    ],
    disclosed_subsystems=[
        "fabrication-glass-thermal-bonding",
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["C12Q 1/68"],
    lineage_ancestors=["bentley-2008-illumina-flow-cell"],
)

add(
    id="singular-genomics-g4",
    canonical_name="Singular Genomics G4 sequencer flow cell",
    aliases=["G4", "Singular Genomics G4"],
    corpus="private",
    first_disclosure_date="2022",
    disclosure_citation="Singular Genomics G4 system. https://www.singulargenomics.com",
    creator="Singular Genomics",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Patterned-flow-cell sequencer with parallel-flow-cell architecture for fast turnaround. Part of the post-2020 wave of Illumina alternatives. Microfluidically very similar to AVITI and Illumina; differentiation is in chemistry and instrument throughput.",
    sources=[
        "Singular Genomics product literature",
    ],
    disclosed_subsystems=[
        "fabrication-glass-thermal-bonding",
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["C12Q 1/68"],
    lineage_ancestors=["bentley-2008-illumina-flow-cell"],
)

add(
    id="quantum-si-platinum",
    canonical_name="Quantum-Si Platinum protein sequencer",
    aliases=["Quantum-Si Platinum"],
    corpus="private",
    first_disclosure_date="2022",
    disclosure_citation="Quantum-Si Platinum system. https://www.quantum-si.com",
    creator="Quantum-Si (founded by Jonathan Rothberg)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="CMOS chip for single-molecule protein sequencing using time-domain fluorescence lifetime detection on a chip with millions of waveguide-coupled wells. Architectural cousin to PacBio ZMWs but with CMOS readout and a different chemistry (N-terminal aminopeptidase cycling). Anticipates: integrated-CMOS-photonic protein sequencing chip, time-domain detection on integrated photodetectors.",
    sources=[
        "Quantum-Si product literature",
    ],
    disclosed_subsystems=[
        "detection-fluorescence-on-chip",
        "fabrication-silicon-drie",
    ],
    cpc_classifications=["C12Q 1/68", "G01N 33/68"],
)

add(
    id="nanostring-geomx",
    canonical_name="NanoString GeoMx Digital Spatial Profiler",
    aliases=["GeoMx", "NanoString GeoMx DSP"],
    corpus="private",
    first_disclosure_date="2019",
    disclosure_citation="NanoString GeoMx Digital Spatial Profiler. Merritt et al. 2020 Nat. Biotechnol. 38, 586–599.",
    creator="NanoString Technologies (acquired by Bruker 2024)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Tissue-section spatial profiling using UV-cleavable oligo-tagged probes, micro-aspiration of cleaved barcodes from operator-defined regions of interest, and downstream readout on the NanoString nCounter platform. Anticipates: micro-aspiration-from-tissue spatial profiling architecture, distinct from the Visium spatial-barcode-grid approach.",
    sources=[
        "NanoString product literature",
    ],
    disclosed_subsystems=[
        "architecture-spatial-barcoded-array",
    ],
    cpc_classifications=["C12Q 1/6841"],
)

add(
    id="nanostring-cosmx",
    canonical_name="NanoString CosMx Spatial Molecular Imager",
    aliases=["CosMx", "NanoString CosMx SMI"],
    corpus="private",
    first_disclosure_date="2022",
    disclosure_citation="NanoString CosMx Spatial Molecular Imager. He et al. 2022 Nat. Biotechnol. 40, 1794–1806.",
    creator="NanoString Technologies (Bruker)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Iterative-fluidic-cycling single-cell spatial transcriptomics on intact tissue: encoded fluorescent probes hybridized to mRNA in tissue are revealed across multiple imaging cycles. Architecturally similar to Akoya CODEX but for transcripts rather than proteins. Anticipates: in-situ-hybridization-cycle architecture for single-cell-resolution spatial transcriptomics.",
    sources=[
        "NanoString product literature",
    ],
    disclosed_subsystems=[
        "architecture-multiplex-cartridge",
    ],
    cpc_classifications=["C12Q 1/6841"],
)

add(
    id="oxford-nanopore-minion",
    canonical_name="Oxford Nanopore MinION flow cell",
    aliases=["MinION", "ONT MinION"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="Oxford Nanopore Technologies MinION flow cell. https://nanoporetech.com",
    creator="Oxford Nanopore Technologies",
    creator_country="GB",
    device_class="lab-on-chip",
    substrate_material="hybrid",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="research",
    ip_status="patented",
    ip_citations=["US8226880B2", "US8821798B2 (and ONT family)"],
    prior_art_notes="USB-form-factor cartridge containing a microfluidic channel with an array of 512 protein nanopores, each with integrated current-sense electronics. The smallest commercially-deployed sequencing form factor. Anticipates: handheld microfluidic sequencing cartridge, USB-powered sequencing instrument, and the field-deployable sequencing application class. Direct commercial descendant of Bayley/Clarke 2009.",
    sources=[
        "Oxford Nanopore Technologies product literature",
    ],
    disclosed_subsystems=[
        "detection-electrochemical-on-chip",
    ],
    cpc_classifications=["C12Q 1/68", "G01N 33/487"],
    lineage_ancestors=["clarke-2009-nanopore-sequencing"],
)

add(
    id="menarini-deparray",
    canonical_name="Menarini Silicon Biosystems DEPArray",
    aliases=["DEPArray"],
    corpus="private",
    first_disclosure_date="2009",
    disclosure_citation="Menarini Silicon Biosystems DEPArray. https://www.siliconbiosystems.com",
    creator="Silicon Biosystems (Menarini Group)",
    creator_country="IT",
    device_class="single-cell-platform",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US7892817B2 (and Silicon Biosystems family)"],
    prior_art_notes="Commercial DEP-cage array on a CMOS chip for individual cell capture, image-based identification, and individual cell release into downstream tubes. Used clinically for circulating tumor cell isolation and for forensic mixed-DNA-sample resolution. Architecturally the commercial descendant of Voldman 2002.",
    sources=[
        "Menarini Silicon Biosystems product literature",
    ],
    disclosed_subsystems=[
        "separation-dielectrophoresis",
        "fabrication-silicon-drie",
    ],
    cpc_classifications=["B01L 3/00", "G01N 33/49"],
    lineage_ancestors=["voldman-2002-cell-trap-dep-array"],
)

add(
    id="nanofluidics-bionano-saphyr",
    canonical_name="Bionano Genomics Saphyr optical genome mapping",
    aliases=["Saphyr", "Bionano optical mapping"],
    corpus="private",
    first_disclosure_date="2017",
    disclosure_citation="Bionano Genomics Saphyr system. https://bionano.com",
    creator="Bionano Genomics",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Disclosed nanochannel-array chip that linearizes individual long DNA molecules in fluorescently-labeled form for optical genome mapping. Anticipates: nanochannel-array architecture for single-molecule DNA elongation, and label-pattern detection of long-range structural variation invisible to short-read sequencing.",
    sources=[
        "Bionano Genomics product literature",
    ],
    disclosed_subsystems=[
        "fabrication-silicon-drie",
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/68"],
)

add(
    id="abbott-piccolo-xpress",
    canonical_name="Abbott Piccolo Xpress / Abaxis disc-format clinical chemistry analyzer",
    aliases=["Piccolo Xpress", "Abaxis Piccolo"],
    corpus="private",
    first_disclosure_date="1995",
    disclosure_citation="Abbott Piccolo Xpress (originally Abaxis). https://www.abbott.com",
    creator="Abaxis (acquired by Zoetis, then Abbott)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="centrifugal",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Centrifugal microfluidic disposable disc with pre-loaded dry reagent wells and integrated optical detection in benchtop reader. Each disc runs a chemistry panel (electrolytes, liver enzymes, kidney function) on 100 µL whole blood in 12 minutes. One of the earliest successful commercial centrifugal microfluidic platforms (1995 launch), predating most academic centrifugal LoD work.",
    sources=[
        "Abbott Piccolo Xpress product literature",
    ],
    disclosed_subsystems=[
        "pump-centrifugal-rotational",
        "valve-capillary-stop",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "G01N 35/00"],
)


# =====================================================================
# OPEN — more open-hardware microfluidics
# =====================================================================

add(
    id="chibio-bioreactor",
    canonical_name="Chi.Bio open-hardware bioreactor",
    aliases=["Chi.Bio"],
    corpus="open",
    first_disclosure_date="2018",
    disclosure_citation="Steel, H.; Habgood, R.; Kelly, C.; Papachristodoulou, A. In situ characterisation and manipulation of biological systems with Chi.Bio. PLOS Biol. 2020, 18, e3000794. DOI: 10.1371/journal.pbio.3000794",
    creator="Steel et al., Oxford / Imperial",
    creator_country="GB",
    device_class="flow-controller",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Open-hardware bioreactor with integrated optical density measurement, fluorescence detection, peristaltic pumping, and feedback-controlled environment. ~$700 BOM. Anticipates: prosumer-grade closed-loop bioreactor for synthetic biology, with feedback control between sensors and actuators built into a benchtop form factor. Strong IP-clearing significance for the small-bioreactor space.",
    sources=[
        "PLOS Biol. 2020, 18, e3000794",
        "https://chi.bio",
    ],
    disclosed_subsystems=[
        "pump-peristaltic-on-chip",
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["C12M 1/00"],
)

add(
    id="evolver-klavins",
    canonical_name="eVOLVER multi-bioreactor evolution platform",
    aliases=["eVOLVER"],
    corpus="open",
    first_disclosure_date="2018",
    disclosure_citation="Wong, B. G.; Mancuso, C. P.; Kiriakov, S.; Bashor, C. J.; Khalil, A. S. Precise, automated control of conditions for high-throughput growth of yeast and bacteria with eVOLVER. Nat. Biotechnol. 2018, 36, 614–623. DOI: 10.1038/nbt.4151",
    creator="Khalil group, Boston University",
    creator_country="US",
    device_class="flow-controller",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Open-hardware 16-vessel parallel bioreactor system with per-vessel temperature, OD, stirring, and feed control. Designed for laboratory directed-evolution and high-throughput growth experiments. Anticipates: massively-parallel addressable bioreactor architecture, open-source bioreactor scaling, and the experimental-evolution use case at academic-budget price points.",
    sources=[
        "Nat. Biotechnol. 2018, 36, 614–623",
        "https://www.fynchbio.com / eVOLVER GitHub",
    ],
    disclosed_subsystems=[
        "pump-peristaltic-on-chip",
        "thermal-droplet-pcr-cycling",
    ],
    cpc_classifications=["C12M 1/00"],
)

add(
    id="squid-microscope",
    canonical_name="Squid open-hardware microscopy platform",
    aliases=["Squid", "octopi"],
    corpus="open",
    first_disclosure_date="2020",
    disclosure_citation="Hongquan Li, Deepak Krishnamurthy, et al. (Prakash Lab Stanford). https://github.com/hongquanli/octopi-research and https://squid-imaging.org",
    creator="Prakash Lab, Stanford (Hongquan Li, Deepak Krishnamurthy, et al.)",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Open-hardware microscopy platform with multi-axis stage, autofocus, multiple imaging modalities (brightfield, fluorescence, phase) and integration with microfluidic chips. Modular and reconfigurable. Anticipates: open-hardware microscopy for high-throughput cell-imaging on chip, replacing $50k-$200k commercial systems with sub-$10k builds. Important reference for any chip-imaging-based microfluidic platform.",
    sources=[
        "https://squid-imaging.org",
        "https://github.com/hongquanli/octopi-research",
    ],
    disclosed_subsystems=[
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["G02B 21/00"],
)

add(
    id="openspim-microscope",
    canonical_name="OpenSPIM light-sheet microscope",
    aliases=["OpenSPIM"],
    corpus="open",
    first_disclosure_date="2013",
    disclosure_citation="Pitrone, P. G. et al. OpenSPIM: an open-access light-sheet microscopy platform. Nat. Methods 2013, 10, 598–599. DOI: 10.1038/nmeth.2507",
    creator="Tomancak group, MPI-CBG",
    creator_country="DE",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Open-source light-sheet (selective-plane illumination) microscope with full mechanical and optical specifications, build instructions, and ImageJ plugin pipeline. Anticipates: open-hardware light-sheet microscopy as a category, with the architectural pattern of community-shared instructions for complex optical instruments.",
    sources=[
        "Nat. Methods 2013, 10, 598–599",
        "https://openspim.org",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["G02B 21/00"],
)

add(
    id="micropython-microfluidics-controller",
    canonical_name="MicroPython microfluidics controller patterns (community)",
    aliases=["MicroPython microfluidics"],
    corpus="open",
    first_disclosure_date="2017",
    disclosure_citation="Various community projects on github documenting MicroPython on RP2040/ESP32 for microfluidic control.",
    creator="Community (various authors)",
    creator_country="GLOBAL",
    device_class="flow-controller",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="The widespread use of MicroPython on RP2040 / ESP32 for microfluidic control firmware (rather than C/C++) has emerged as a community pattern that lowers the bar for biology-trained researchers to write controller firmware. Anticipates: MicroPython-on-RP2040 as a default firmware substrate for low-throughput microfluidic instrumentation.",
    sources=[
        "Various github repositories",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# =====================================================================
# FICTIONAL — more narrative depictions
# =====================================================================

add(
    id="andromeda-strain-wildfire-detail",
    canonical_name="Andromeda Strain Wildfire facility microfluidic detail",
    aliases=["Wildfire facility", "Andromeda Strain Level V"],
    corpus="fictional",
    first_disclosure_date="1969",
    disclosure_citation="Crichton, M. The Andromeda Strain. Knopf, New York, 1969.",
    creator="Michael Crichton",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="research",
    ip_status="fictional",
    prior_art_notes="Detailed narrative depiction of automated microbiological analysis pipeline including automated sample preparation, electron microscopy, biochemical screening, and genomic sequencing — all with operator-by-exception. The depiction is unusually mechanistically specific for SF and arguably anticipates the entire integrated-multi-omics workflow that became commercial 50 years later.",
    sources=[
        "Crichton, M. The Andromeda Strain. 1969.",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="six-million-dollar-man-bionic-diagnostics",
    canonical_name="Six Million Dollar Man bionic-diagnostic medical scanner",
    aliases=["Bionic medical scanner"],
    corpus="fictional",
    first_disclosure_date="1973",
    disclosure_citation="The Six Million Dollar Man (TV series) and pilot film Cyborg, ABC, 1973–1978.",
    creator="ABC Television / Martin Caidin source novel",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Narrative depiction of compact bedside diagnostic instruments performing comprehensive blood-panel and physiological-state assessment with rapid output. Anticipates: compact bedside multiplex diagnostics in a clinical-decision-support context.",
    sources=[
        "The Six Million Dollar Man (1973–1978)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="ghost-in-the-shell-cybernetic-diagnostics",
    canonical_name="Ghost in the Shell cybernetic-body diagnostic facility",
    aliases=["GitS Section 9 medical bay"],
    corpus="fictional",
    first_disclosure_date="1995",
    disclosure_citation="Ghost in the Shell (1995 anime film), dir. Mamoru Oshii. Bandai Visual / Production I.G.",
    creator="Production I.G. / Masamune Shirow source",
    creator_country="JP",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Detailed visual depiction of automated cybernetic-body diagnostic and maintenance bays. Anticipates: integrated body-scan, automated tissue-sample analysis, and human-machine-interface diagnostic workflows.",
    sources=[
        "Ghost in the Shell (1995)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="halo-cortana-medical",
    canonical_name="Halo medical bay automated diagnostics",
    aliases=["UNSC medical bay"],
    corpus="fictional",
    first_disclosure_date="2001",
    disclosure_citation="Halo: Combat Evolved (2001) and Halo franchise. Bungie / 343 Industries / Microsoft.",
    creator="Bungie / 343 Industries / Microsoft",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Narrative depiction of fully automated medical and trauma bays with integrated diagnostic, surgical, and pharmaceutical-synthesis capabilities. Cumulative architectural commitments across the Halo franchise are detailed enough to qualify as conceptual prior art for autonomous bedside trauma-care systems.",
    sources=[
        "Halo: Combat Evolved (2001) and franchise materials",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# =====================================================================
# Misc — fluidic logic, microreaction engineering
# =====================================================================

add(
    id="prakash-2007-bubble-logic",
    canonical_name="Microfluidic bubble logic",
    aliases=["Prakash bubble logic"],
    corpus="academic",
    first_disclosure_date="2007",
    disclosure_citation="Prakash, M.; Gershenfeld, N. Microfluidic bubble logic. Science 2007, 315, 832–835. DOI: 10.1126/science.1136907",
    creator="Prakash, Gershenfeld (MIT)",
    creator_country="US",
    device_class="other",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="multiphase-pressure",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Disclosed microfluidic bubble logic gates: AND/OR/NOT operations implemented purely in two-phase flow geometry, using bubbles as the binary signal. Anticipates: programmable microfluidic logic without electrical actuation, and the broader concept of fluidic-Turing-completeness on chip. Precursor of HUVAS-style bubble computers.",
    sources=[
        "Science 2007, 315, 832–835",
    ],
    disclosed_subsystems=[
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "G06D 1/00"],
)

add(
    id="weaver-2010-microfluidic-large-scale-integration",
    canonical_name="Latching microfluidic valves and digital logic",
    aliases=["Weaver microfluidic logic"],
    corpus="academic",
    first_disclosure_date="2010",
    disclosure_citation="Weaver, J. A.; Melin, J.; Stark, D.; Quake, S. R.; Horowitz, M. A. Static control logic for microfluidic devices using pressure-gain valves. Nat. Phys. 2010, 6, 218–223. DOI: 10.1038/nphys1513",
    creator="Quake / Horowitz groups, Stanford",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed pressure-gain microfluidic valves enabling combinational logic on chip — microfluidic equivalents of CMOS logic gates. Demonstrates 8-bit shift register and ring oscillator implemented in PDMS. Anticipates: microfluidic-only digital control logic without external addressing electronics, and the architectural goal of a self-contained programmable chip without electronic peripherals.",
    sources=[
        "Nat. Phys. 2010, 6, 218–223",
    ],
    disclosed_subsystems=[
        "valve-quake-pneumatic-membrane",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "G06D 1/00"],
    lineage_ancestors=["unger-2000-quake-monolithic-membrane-valve"],
)

add(
    id="mosadegh-2010-fluidic-rectifier",
    canonical_name="Fluidic rectifier and microfluidic memory",
    aliases=["Mosadegh fluidic rectifier"],
    corpus="academic",
    first_disclosure_date="2010",
    disclosure_citation="Mosadegh, B.; Kuo, C.-H.; Tung, Y.-C.; Torisawa, Y.; Bersano-Begey, T.; Tavana, H.; Takayama, S. Integrated elastomeric components for autonomous regulation of sequential and oscillatory flow switching in microfluidic devices. Nat. Phys. 2010, 6, 433–437. DOI: 10.1038/nphys1637",
    creator="Takayama group, Michigan",
    creator_country="US",
    device_class="other",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed elastomeric fluidic-rectifier and oscillator primitives implemented as monolithic-PDMS Quake-valve variants. Provides a microfluidic equivalent of the diode and the relaxation oscillator. Anticipates: monolithic elastomeric fluidic logic substrate, and autonomous-pumping microfluidic chips that operate without external pressure modulation.",
    sources=[
        "Nat. Phys. 2010, 6, 433–437",
    ],
    disclosed_subsystems=[
        "valve-quake-pneumatic-membrane",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00"],
    lineage_ancestors=["unger-2000-quake-monolithic-membrane-valve"],
)

add(
    id="kim-2017-multilayer-soft-lithography-mems",
    canonical_name="Continuous high-throughput single-cell western blotting (scWestern)",
    aliases=["scWestern", "Hughes 2014 single-cell western"],
    corpus="academic",
    first_disclosure_date="2014",
    disclosure_citation="Hughes, A. J. et al. Single-cell western blotting. Nat. Methods 2014, 11, 749–755. DOI: 10.1038/nmeth.2992",
    creator="Herr group, UC Berkeley",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="electrokinetic",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed single-cell western blotting on a polyacrylamide-gel chip with thousands of microwells, each containing one cell, where after lysis and electrophoresis the gel-bound proteins are immunoprobed in place. Anticipates: per-cell-resolution proteomics by chip-format gel electrophoresis, and the gel-as-microfluidic-substrate paradigm.",
    sources=[
        "Nat. Methods 2014, 11, 749–755",
    ],
    disclosed_subsystems=[
        "separation-capillary-electrophoresis",
    ],
    cpc_classifications=["B01L 3/00", "G01N 33/68"],
)

add(
    id="abate-2010-surfactant-survey",
    canonical_name="Krytox-PFPE surfactant for biocompatible droplet stabilization",
    aliases=["Krytox surfactant", "PFPE-PEG surfactant"],
    corpus="academic",
    first_disclosure_date="2008",
    disclosure_citation="Holtze, C.; Rowat, A. C.; Agresti, J. J.; Hutchison, J. B.; Angilè, F. E.; Schmitz, C. H. J.; Köster, S.; Duan, H.; Humphry, K. J.; Scanga, R. A.; Johnson, J. S.; Pisignano, D.; Weitz, D. A. Biocompatible surfactants for water-in-fluorocarbon emulsions. Lab Chip 2008, 8, 1632–1639. DOI: 10.1039/b806706f",
    creator="Weitz group, Harvard",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="multiphase-pressure",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed PFPE-PEG triblock surfactants in fluorocarbon oil for biocompatible water-in-oil droplet stabilization. The chemistry that made droplet-format single-cell biology possible: previous surfactants either lysed cells or destabilized droplets within hours. Anticipates: PFPE-PEG surfactant as the de facto standard for single-cell droplet workflows, used in essentially every published Drop-seq, inDrops, ddPCR, and 10x Chromium experiment.",
    sources=[
        "Lab Chip 2008, 8, 1632–1639",
    ],
    disclosed_subsystems=[
        "droplet-stabilizing-surfactant",
    ],
    cpc_classifications=["B01L 3/00"],
)

# Add the new cross-cut tags to the schema (we'll handle this via a separate update)
# For now: separation-magnetophoresis, separation-dielectrophoresis,
# architecture-spatial-barcoded-array, droplet-stabilizing-surfactant,
# thermal-microchannel-cooling-electronics, fabrication-volumetric-3d-printing,
# cell-trap-hydrodynamic, fabrication-glass-anodic-bonding


# Write out
with CORPUS.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new entries to {CORPUS}")
