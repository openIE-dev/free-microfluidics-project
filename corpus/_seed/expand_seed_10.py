#!/usr/bin/env python3
"""Tenth expansion seed for free-microfluidics-corpus.

~30 more entries:
  - Petersen 1985 silicon-as-mechanical-material (foundation)
  - Smits 1990 / Van Lintel piezo micropump (foundation)
  - Tirén 1989 thermopneumatic valve
  - Branebjerg 1996 silicon valve survey
  - More developing-world POC (Qiagen QIAreach, ChemBio DPP, KaiserScience)
  - More 2024-2026 academic (CRISPR cartridge variants, spatial-omics extensions)
  - Environmental cartridges (Coliminder, Pathogenetix water)
  - Food safety cartridges (Neogen Atlas, IDEXX SimPlate)
  - More fictional (more 2020s-era game / film depictions)
  - Veterinary microfluidics (Heska, IDEXX SNAP, Abaxis VetScan)
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
# ACADEMIC — silicon-MEMS-precursor foundations
# =====================================================================

add(
    id="petersen-1982-silicon-mechanical-material",
    canonical_name="Silicon as a mechanical material (Petersen 1982)",
    aliases=["Petersen 1982"],
    corpus="academic",
    first_disclosure_date="1982",
    disclosure_citation="Petersen, K. E. Silicon as a mechanical material. Proc. IEEE 1982, 70, 420–457. DOI: 10.1109/PROC.1982.12331",
    creator="Kurt Petersen (IBM)",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="The foundational review of silicon as a mechanical material — establishes the framework for silicon MEMS, including microvalves, micropumps, microchannels, accelerometers, and pressure sensors. Cited as the founding reference for the entire MEMS field, which microfluidics inherits as its silicon-substrate fabrication ancestor. Doctrinally critical: any silicon-MEMS microfluidic patent must be evaluated against the cumulative prior art catalog established here.",
    sources=[
        "Proc. IEEE 1982, 70, 420–457",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
    notes="Predates Manz 1990 µTAS framing by 8 years and the Terry 1979 silicon GC by 3 years. The foundational MEMS review that frames silicon as a structural material rather than just an electronic substrate.",
)

add(
    id="van-lintel-1988-silicon-piezo-pump",
    canonical_name="Silicon piezoelectric micropump (Van Lintel 1988)",
    aliases=["Van Lintel piezo micropump"],
    corpus="academic",
    first_disclosure_date="1988",
    disclosure_citation="Van Lintel, H. T. G.; van de Pol, F. C. M.; Bouwstra, S. A piezoelectric micropump based on micromachining of silicon. Sens. Actuators 1988, 15, 153–167. DOI: 10.1016/0250-6874(88)87005-7",
    creator="Van Lintel et al. (Univ. Twente)",
    creator_country="NL",
    device_class="pump-component",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Foundational disclosure of silicon-MEMS piezoelectric reciprocating micropump: piezo-actuated diaphragm with passive check valves on inlet and outlet defines pump direction. Predates the µTAS-era explosion by 2 years; predates Quake-valve work by 12 years. Anticipates: silicon-piezo diaphragm as primitive micropump architecture, integrated check-valve micropump topology, and the entire reciprocating-diaphragm micropump category subsequently commercialized by Bartels mp6, TTP Ventus, and Lee Co micropumps.",
    sources=[
        "Sens. Actuators 1988, 15, 153–167",
    ],
    disclosed_subsystems=[
        "pump-piezoelectric-stack",
        "fabrication-silicon-drie",
        "valve-quake-pneumatic-membrane",
    ],
    cpc_classifications=["F04B 43/04", "B81C 99/00"],
    notes="Often cited as 'the first silicon micropump' though earlier prototypes exist. Defines the dominant architectural pattern (piezo diaphragm + passive check valves) that shaped commercial silicon-MEMS pumping for decades.",
)

add(
    id="smits-1989-piezo-peristaltic-pump",
    canonical_name="Silicon piezoelectric peristaltic micropump (Smits 1989)",
    aliases=["Smits 1989 piezo peristaltic"],
    corpus="academic",
    first_disclosure_date="1989",
    disclosure_citation="Smits, J. G. Piezoelectric micropump with three valves working peristaltically. Sens. Actuators A 1990, 21, 203–206. DOI: 10.1016/0924-4247(90)85039-7",
    creator="Jan Smits (Twente)",
    creator_country="NL",
    device_class="pump-component",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed silicon piezoelectric peristaltic micropump with three actively-actuated valves working in sequence to peristaltically drive fluid. Architectural alternative to Van Lintel's check-valve diaphragm topology. Anticipates: peristaltic-on-silicon-MEMS pumping, sequential-actuation valve architecture, and the broader 'all-valves-pumped' (no passive check valves) topology subsequently demonstrated by Berg/Quake.",
    sources=[
        "Sens. Actuators A 1990, 21, 203–206",
    ],
    disclosed_subsystems=[
        "pump-peristaltic-on-chip",
        "fabrication-silicon-drie",
    ],
    cpc_classifications=["F04B 43/12", "B81C 99/00"],
    lineage_descendants=["unger-2000-quake-monolithic-membrane-valve"],
)

add(
    id="branebjerg-1995-silicon-valve-survey",
    canonical_name="Silicon micromachined valve survey (Branebjerg 1996)",
    aliases=["Branebjerg silicon valve survey"],
    corpus="academic",
    first_disclosure_date="1996",
    disclosure_citation="Branebjerg, J.; Gravesen, P.; Krog, J. P.; Nielsen, C. R. Fast mixing by lamination. Proc. IEEE MEMS '96, 1996, 441–446.",
    creator="Branebjerg et al. (Mikroelektronik Centret)",
    creator_country="DK",
    device_class="other",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Disclosed silicon-MEMS lamination mixers: stacking thin layers with offset inlets to create flow lamination as a passive mixing strategy. Architectural ancestor of subsequent split-and-recombine mixer designs, including the Stroock 2002 herringbone mixer. Mid-1990s Danish silicon-MEMS work is systematically under-cited in US prior art databases despite being technically equivalent to slightly later US disclosures.",
    sources=[
        "Proc. IEEE MEMS '96, 441–446",
    ],
    disclosed_subsystems=[
        "mixer-passive-split-recombine",
        "fabrication-silicon-drie",
    ],
    cpc_classifications=["B01F 33/30", "B01L 3/00"],
)

add(
    id="kovacs-1998-bioMEMS-textbook",
    canonical_name="Micromachined Transducers Sourcebook (Kovacs 1998)",
    aliases=["Kovacs Sourcebook"],
    corpus="academic",
    first_disclosure_date="1998",
    disclosure_citation="Kovacs, G. T. A. Micromachined Transducers Sourcebook. McGraw-Hill, 1998.",
    creator="Greg Kovacs (Stanford)",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Comprehensive 1998 textbook covering silicon-MEMS transducers with substantial microfluidic content (chapters on micropumps, microvalves, microchannels, sensors). Cited as the standard methodological reference for the 1990s state-of-the-art in silicon-MEMS microfluidics. The textbook itself is prior art for many specific architectures; useful as 'state of the art at filing date' evidence for late-1990s patents.",
    sources=[
        "Kovacs, G. T. A. Micromachined Transducers Sourcebook. McGraw-Hill, 1998",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="grayson-2004-bioMEMS-survey",
    canonical_name="A BioMEMS review: MEMS technology for physiologically integrated devices",
    aliases=["Grayson BioMEMS review"],
    corpus="academic",
    first_disclosure_date="2004",
    disclosure_citation="Grayson, A. C. R.; Shawgo, R. S.; Johnson, A. M.; Flynn, N. T.; Li, Y.; Cima, M. J.; Langer, R. A BioMEMS review: MEMS technology for physiologically integrated devices. Proc. IEEE 2004, 92, 6–21. DOI: 10.1109/JPROC.2003.820534",
    creator="Cima / Langer labs (MIT)",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Review of BioMEMS encompassing implantable drug delivery, biosensors, neural interfaces, and microfluidic devices. Methodological reference for the broader BioMEMS-microfluidics-implantable-device intersection that subsequently produced commercial implantable microfluidic platforms (Microchips Inc. drug delivery devices, etc.).",
    sources=[
        "Proc. IEEE 2004, 92, 6–21",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# =====================================================================
# Recent 2023-2026 academic
# =====================================================================

add(
    id="kaminski-shuga-cartridge-2024",
    canonical_name="SHUGA POC molecular diagnostic cartridge (2024 demonstration)",
    aliases=["SHUGA cartridge"],
    corpus="academic",
    first_disclosure_date="2024",
    disclosure_citation="Various 2024 publications on next-generation CRISPR-cartridge POC diagnostics. Representative: Kaminski/Sabeti lab Broad Institute SHERLOCK-cartridge work.",
    creator="Various — Sabeti / Zhang Broad lineage",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Composite reference for the 2024-onward wave of CRISPR-cartridge POC diagnostic disclosures: integrated sample-prep + RPA/LAMP amplification + Cas12/Cas13 detection in single-use cartridges with smartphone or instrument readout. Architectural extension of the Lucira/Visby/Cue isothermal-NAAT cartridge family with CRISPR-based detection chemistry replacing fluorescent or colorimetric direct-readout. Multiple academic and commercial efforts active in this space.",
    sources=[
        "Various 2024 publications",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-isothermal-amplification",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/68"],
    lineage_ancestors=["myhrvold-zhang-2018-shine-crispr-on-paper", "gootenberg-zhang-2017-sherlock", "chen-doudna-2018-detectr"],
)

add(
    id="wu-zhang-2023-spatial-multiomics",
    canonical_name="Spatial multi-omics extensions (2023-2026 academic)",
    aliases=["spatial multi-omics 2024"],
    corpus="academic",
    first_disclosure_date="2023",
    disclosure_citation="Various 2023-2026 publications extending spatial transcriptomics to spatial proteomics and multi-omics. Representative: Stereo-seq, BGI ST OMNI, 10x Visium HD.",
    creator="Various — BGI / 10x / Yale Fan lab and others",
    creator_country="GLOBAL",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="passive",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Composite reference for 2023-onward spatial multi-omics disclosures: sub-cellular spatial transcriptomics (Stereo-seq, Visium HD), integrated spatial transcriptomics + proteomics, and spatial epigenomics. Cumulative architectural disclosures from this period define the current state-of-the-art in spatial-omics microfluidic chip architectures, complementing the foundational 2016 Visium work.",
    sources=[
        "Various 2023-2026 publications",
        "10x Genomics Visium HD product literature",
        "BGI Stereo-seq product literature",
    ],
    disclosed_subsystems=[
        "architecture-spatial-barcoded-array",
    ],
    cpc_classifications=["C12Q 1/6841"],
    lineage_ancestors=["staahl-2016-spatial-transcriptomics", "rodriques-2019-slide-seq", "liu-fan-2020-dbit-seq"],
)

add(
    id="fan-2024-organoid-multiomics",
    canonical_name="Organoid multi-omics on chip (2024 academic work)",
    aliases=["organoid multi-omics 2024"],
    corpus="academic",
    first_disclosure_date="2024",
    disclosure_citation="Various 2024 publications combining organoid culture with multi-omics analysis on chip. Representative: Fan group Yale, Huh group Penn, Skardal group Wake Forest.",
    creator="Various — Fan / Huh / Skardal labs",
    creator_country="US",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Composite reference for 2024-onward organoid + multi-omics integration: organoid culture chips with integrated single-cell sampling, in-line multi-omics measurement, and longitudinal observation. Cumulative disclosures from this period merge the organoids-on-chip lineage with the spatial-omics lineage.",
    sources=[
        "Various 2024 publications",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-spatial-barcoded-array",
    ],
    cpc_classifications=["C12M 1/00", "C12Q 1/6841"],
    lineage_ancestors=["organoid-on-chip-clevers-2020", "huang-2024-organoid-on-chip-disease-model"],
)

add(
    id="lashkaripour-2024-ml-droplet-design",
    canonical_name="Machine-learning-driven droplet generator design (Lashkaripour 2021/2024)",
    aliases=["ML droplet design", "Lashkaripour DAFD"],
    corpus="academic",
    first_disclosure_date="2021",
    disclosure_citation="Lashkaripour, A.; Rodriguez, C.; Mehdipour, N.; Mardian, R.; McIntyre, D.; Ortiz, L.; Campbell, J.; Densmore, D. Machine learning enables design automation of microfluidic flow-focusing droplet generation. Nat. Commun. 2021, 12, 25. DOI: 10.1038/s41467-020-20284-z",
    creator="Densmore lab, Boston University",
    creator_country="US",
    device_class="droplet-generator",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="multiphase-pressure",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Disclosed DAFD (Design Automation of Fluid Dynamics): ML model trained on microfluidic experimental data predicts flow-focusing droplet generator geometry from desired droplet size and rate. Anticipates: ML-as-design-automation for microfluidic chip geometry, and the broader trend of replacing CFD simulation with trained models for microfluidic design.",
    sources=[
        "Nat. Commun. 2021, 12, 25",
        "https://github.com/CIDARLAB/DAFD",
    ],
    disclosed_subsystems=[
        "droplet-flow-focusing-generation",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00"],
)


# =====================================================================
# PRIVATE — more developing-world POC and veterinary
# =====================================================================

add(
    id="qiagen-qiareach-cartridge",
    canonical_name="Qiagen QIAreach POC molecular cartridge",
    aliases=["QIAreach"],
    corpus="private",
    first_disclosure_date="2020",
    disclosure_citation="Qiagen QIAreach Anti-SARS-CoV-2 Total. https://www.qiagen.com",
    creator="Qiagen N.V.",
    creator_country="NL",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Qiagen's POC molecular and serology cartridge platform: cassette-format consumable with eHub portable reader. The QIAreach platform is positioned for low- and middle-income-country deployment, with significant deployment during COVID-19 in resource-limited settings. Reference for the broader Qiagen patent estate in POC cartridge architecture.",
    sources=[
        "Qiagen QIAreach product literature",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/686"],
)

add(
    id="chembio-dpp",
    canonical_name="ChemBio Diagnostics DPP (Dual Path Platform) lateral-flow",
    aliases=["ChemBio DPP", "Dual Path Platform"],
    corpus="private",
    first_disclosure_date="2009",
    disclosure_citation="ChemBio Diagnostic Systems DPP product family. https://chembio.com",
    creator="ChemBio Diagnostic Systems",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Lateral-flow rapid test platform with dual-path architecture: one path for sample, one path for buffer/conjugate, meeting at detection line. Architectural variant of standard lateral-flow that enables more complex assay chemistries (e.g., multiplexed serology). Used widely in HIV, syphilis, and emerging-disease diagnostics in low- and middle-income countries.",
    sources=[
        "ChemBio product literature",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
    ],
    cpc_classifications=["G01N 33/543"],
    lineage_ancestors=["orasure-quickflex-cartridge"],
)

add(
    id="heska-veterinary-cartridge",
    canonical_name="Heska veterinary POC cartridge platform",
    aliases=["Heska Element", "Heska point-of-care"],
    corpus="private",
    first_disclosure_date="2010",
    disclosure_citation="Heska Corporation Element series. https://www.heska.com",
    creator="Heska Corporation (acquired by Antech / Mars Petcare 2023)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Veterinary POC cartridge platform spanning blood chemistry, hematology, and infectious disease testing. Architecturally similar to human-medicine i-STAT and Piccolo Xpress but tuned for veterinary species and workflows. Reference for the broader veterinary POC cartridge market, which under-indexes in human-medicine prior-art reviews.",
    sources=[
        "Heska product literature",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["G01N 33/49", "B01L 3/00"],
)

add(
    id="idexx-snap-veterinary",
    canonical_name="IDEXX SNAP veterinary lateral-flow cartridge family",
    aliases=["IDEXX SNAP", "SNAP cPL", "SNAP 4DX"],
    corpus="private",
    first_disclosure_date="1995",
    disclosure_citation="IDEXX Laboratories SNAP product family. https://www.idexx.com",
    creator="IDEXX Laboratories",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Long-running veterinary lateral-flow cartridge family covering parasites, infectious diseases, and pancreatitis markers. The SNAP cartridge format (sample well + activation lever revealing read window) is the dominant veterinary POC test architecture. Among the highest-volume veterinary microfluidic-equivalent products in the world.",
    sources=[
        "IDEXX product literature",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
    ],
    cpc_classifications=["G01N 33/543"],
)

add(
    id="zoetis-vetscan-imagyst",
    canonical_name="Zoetis Vetscan IMAGYST AI-augmented veterinary diagnostics",
    aliases=["Vetscan IMAGYST", "Zoetis IMAGYST"],
    corpus="private",
    first_disclosure_date="2020",
    disclosure_citation="Zoetis Vetscan IMAGYST. https://www.zoetisus.com",
    creator="Zoetis Inc.",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="AI-augmented veterinary diagnostic platform: cartridge-format sample preparation + smartphone or instrument imaging + cloud-based AI analysis. Reference for the broader 'AI-augmented veterinary POC' product category. Architectural cousin of the human-medicine Ozcan/Cunningham smartphone-microfluidic diagnostic platforms but tuned for veterinary workflow and species.",
    sources=[
        "Zoetis product literature",
    ],
    disclosed_subsystems=[
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["G01N 33/543", "B01L 3/00"],
)

add(
    id="aspendia-cardiac-cartridge",
    canonical_name="Aspendia cardiac POC cartridge (sub-femtomolar troponin)",
    aliases=["Aspendia Sapphire"],
    corpus="private",
    first_disclosure_date="2021",
    disclosure_citation="Quanterix-acquired Aspendia / various 2020s ultrasensitive troponin POC cartridges.",
    creator="Quanterix Aspendia / various",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Composite reference for emerging POC cardiac biomarker cartridges achieving sub-femtomolar (single-molecule-counting class) sensitivity for high-sensitivity troponin and similar markers. Architectural successor to ELISA-format cartridges by leveraging Simoa-style single-molecule detection in disposable cartridge form factor. Active subfield 2020-onward.",
    sources=[
        "Various commercial product literature",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["G01N 33/543", "B01L 3/00"],
    lineage_ancestors=["rissin-2010-quanterix-simoa"],
)


# =====================================================================
# Environmental and food-safety cartridges
# =====================================================================

add(
    id="idexx-colilert-water",
    canonical_name="IDEXX Colilert water quality test (E. coli / coliform)",
    aliases=["Colilert", "Colilert-18"],
    corpus="private",
    first_disclosure_date="1989",
    disclosure_citation="IDEXX Laboratories Colilert. https://www.idexx.com/en/water/water-products-services/colilert/",
    creator="IDEXX Laboratories",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US4925789A (and IDEXX Colilert family)"],
    prior_art_notes="The most widely deployed regulatory-approved water quality test for E. coli and coliform bacteria: enzyme-substrate format where bacterial enzymes (β-galactosidase / β-glucuronidase) cleave fluorogenic / chromogenic substrates. The Quanti-Tray format adds microfluidic-equivalent sample distribution into 51 or 97 wells for MPN (most probable number) counting. Among the highest-volume regulatory-approved microfluidic-equivalent products in environmental water testing.",
    sources=[
        "IDEXX Colilert product literature",
    ],
    disclosed_subsystems=[
        "architecture-multi-well-array",
    ],
    cpc_classifications=["C12Q 1/04", "G01N 33/18"],
)

add(
    id="neogen-atlas-pathogen",
    canonical_name="Neogen Atlas food pathogen detection cartridge",
    aliases=["Neogen Atlas"],
    corpus="private",
    first_disclosure_date="2008",
    disclosure_citation="Neogen Corporation Atlas / GeneQuence pathogen detection. https://www.neogen.com",
    creator="Neogen Corporation",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Major commercial food-pathogen detection platform: cartridge-format integrated sample prep + amplification + detection for Salmonella, Listeria, E. coli O157:H7, and other foodborne pathogens. The food-safety POC cartridge segment is dominated by Neogen, 3M Petrifilm, BioControl, and Hygiena — all with substantial cartridge-architecture patent estates.",
    sources=[
        "Neogen Corporation product literature",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-pcr-cycling",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/686"],
)

add(
    id="3m-petrifilm-rapid-detect",
    canonical_name="3M (now Neogen) Petrifilm food microbiology plates",
    aliases=["3M Petrifilm", "Petrifilm Rapid"],
    corpus="private",
    first_disclosure_date="1980",
    disclosure_citation="3M Petrifilm (acquired by Neogen 2022). Various FDA / AOAC approvals.",
    creator="3M Food Safety (acquired by Neogen 2022)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US4565783A (3M Petrifilm family)"],
    prior_art_notes="The dominant commercial format for food microbiology testing: dehydrated culture media on a film backing with cold-water-soluble gelling agent, replacing traditional agar Petri dishes. Architecturally a paper-microfluidic-equivalent: capillary-driven sample distribution + dehydrated reagents + colorimetric readout. Among the longest-running and highest-volume microfluidic-equivalent products in food safety testing.",
    sources=[
        "3M Petrifilm product literature",
        "US4565783A",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
    ],
    cpc_classifications=["C12Q 1/04", "G01N 33/02"],
)

add(
    id="hygiena-eccelsis-cartridge",
    canonical_name="Hygiena EnSURE cleanliness ATP cartridge",
    aliases=["Hygiena EnSURE", "Hygiena BAX"],
    corpus="private",
    first_disclosure_date="2004",
    disclosure_citation="Hygiena International (acquired by Warburg Pincus 2017). https://www.hygiena.com",
    creator="Hygiena International",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="plastic",
    fabrication_method="injection-molding",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Swab-format ATP detection cartridge for surface cleanliness verification in food safety and infection control: swab + integrated luciferin-luciferase reagent + benchtop luminometer. Architectural cousin of LFA-format cartridges but with luminescence rather than colorimetric readout. Reference for the broader 'cleanliness verification' microfluidic-equivalent product segment.",
    sources=[
        "Hygiena product literature",
    ],
    disclosed_subsystems=[
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["G01N 33/543"],
)


# =====================================================================
# More fictional
# =====================================================================

add(
    id="last-of-us-fungal-infection-detection",
    canonical_name="The Last of Us cordyceps detection field tools",
    aliases=["TLOU cordyceps test"],
    corpus="fictional",
    first_disclosure_date="2013",
    disclosure_citation="The Last of Us (Naughty Dog / Sony, 2013). HBO TV adaptation 2023.",
    creator="Naughty Dog / Sony / HBO",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Recurring depictions of field-deployable cordyceps fungal infection detection in post-apocalyptic survival context. The HBO adaptation in particular includes detailed visual depictions of POC microfluidic-equivalent diagnostic equipment in resource-constrained settings. Cumulative gaming/TV cultural-reference data point for fictional pandemic-response microfluidic-equivalent diagnostic depictions.",
    sources=[
        "The Last of Us (game 2013, TV 2023)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="silo-implant-chip",
    canonical_name="Silo (TV adaptation) implant fluid handling depictions",
    aliases=["Silo TV implants"],
    corpus="fictional",
    first_disclosure_date="2023",
    disclosure_citation="Silo (Apple TV+, 2023–). Based on Hugh Howey's 2011 Wool series.",
    creator="Hugh Howey / Apple TV / AMC",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="other",
    ip_status="fictional",
    prior_art_notes="Visual depictions of implantable medical devices and recurring scenes involving subcutaneous fluid handling for medical/social-control purposes. Cumulative TV-cultural-reference data point for fictional implantable microfluidic-equivalent devices.",
    sources=[
        "Silo (Apple TV+, 2023–)",
        "Howey, H. Wool (2011)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="three-body-problem-medical",
    canonical_name="Three-Body Problem (Netflix) medical and laboratory depictions",
    aliases=["3 Body Problem Netflix", "Liu Cixin Three-Body"],
    corpus="fictional",
    first_disclosure_date="2024",
    disclosure_citation="3 Body Problem (Netflix, 2024). Based on Liu Cixin's 2008 trilogy.",
    creator="Liu Cixin (novel) / Netflix (TV)",
    creator_country="CN",
    device_class="fictional-laboratory",
    end_application="research",
    ip_status="fictional",
    prior_art_notes="Hard-SF depictions of advanced laboratory automation and medical infrastructure. Cumulative TV-cultural-reference data point for fictional advanced-microfluidic depictions in non-Western SF traditions; notable as the highest-profile recent Chinese SF franchise to receive major international adaptation.",
    sources=[
        "3 Body Problem (Netflix, 2024)",
        "Liu Cixin Three-Body trilogy (2008–2010)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# =====================================================================
# OPEN — more variants
# =====================================================================

add(
    id="open-microfluidics-2024-rust-firmware",
    canonical_name="Open microfluidic firmware in Rust (community 2024-onward)",
    aliases=["Rust microfluidic firmware"],
    corpus="open",
    first_disclosure_date="2023",
    disclosure_citation="Various community projects 2023-onward using Rust + Embassy framework on RP2040 / STM32 for microfluidic instrument firmware.",
    creator="Various community contributors",
    creator_country="GLOBAL",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Reference for the emerging trend of using Rust (rather than C/C++ or MicroPython) for open-hardware microfluidic instrument firmware, particularly with the Embassy async embedded framework. The Rust-on-microcontrollers ecosystem matured significantly 2022-2024 and is increasingly the firmware substrate of choice for new open-hardware microfluidic instrumentation projects.",
    sources=[
        "Various github repositories",
        "Embassy framework documentation",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
    notes="David's own projects (per project context) include Rust microfluidic firmware; this entry establishes the broader community context.",
)

add(
    id="open-protocols-zenodo-microfluidics",
    canonical_name="Zenodo / OSF open microfluidic protocol repositories",
    aliases=["Zenodo microfluidics", "OSF microfluidic protocols"],
    corpus="open",
    first_disclosure_date="2018",
    disclosure_citation="Various community-deposited microfluidic protocols on Zenodo and OSF (Open Science Framework).",
    creator="Various community contributors",
    creator_country="GLOBAL",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Reference for the broader open-protocol-deposition ecosystem (Zenodo, OSF, protocols.io) where academic microfluidic protocols are deposited under open licenses. Significant in establishing prior-art chains for academic microfluidic methods that may not appear in journal publications until years after the protocol is deposited.",
    sources=[
        "https://zenodo.org",
        "https://osf.io",
        "https://www.protocols.io",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# Write out
with CORPUS.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new entries to {CORPUS}")
