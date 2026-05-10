#!/usr/bin/env python3
"""Eighth expansion seed for free-microfluidics-corpus.

~30 more entries:
  - Agricultural / environmental (water quality, soil DNA, food pathogen)
  - Synthetic biology toolkits (Echo dispenser variants, Gilson PB)
  - Smartphone-based POC + ML-driven imaging analysis
  - Pediatric / neonatal cartridges (Sebia hemoglobinopathy, capillary-blood)
  - More open-hardware community (Hackuarium, La Paillasse, Genspace)
  - More academic 2020s (LFA+ML, on-chip CRISPR variants)
  - More fictional (Snow Crash bioluminescent, Star Wars droid maintenance)
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
# ACADEMIC — environmental, agricultural, smartphone-POC
# =====================================================================

add(
    id="bridle-2014-soil-microfluidic-extraction",
    canonical_name="Microfluidic soil DNA extraction and pathogen detection",
    aliases=["Bridle soil microfluidics"],
    corpus="academic",
    first_disclosure_date="2014",
    disclosure_citation="Bridle, H.; Miller, B.; Desmulliez, M. P. Y. Application of microfluidics in waterborne pathogen monitoring: a review. Water Res. 2014, 55, 256–271. DOI: 10.1016/j.watres.2014.01.061",
    creator="Bridle group, Heriot-Watt",
    creator_country="GB",
    device_class="point-of-care-cartridge",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="public-domain",
    prior_art_notes="Foundational review establishing microfluidic waterborne pathogen detection as a coherent subfield: integration of sample-prep (filtration, concentration), nucleic-acid extraction, isothermal amplification, and integrated detection on portable cartridges. Anticipates: water-quality cartridge architecture for field deployment, distinct from clinical POC cartridges by emphasizing large-volume sample concentration upstream of small-volume analytical chamber. Underlies subsequent commercial efforts by ALS Limited, IDEXX Colilert systems, and academic agricultural-water-quality startups.",
    sources=[
        "Water Res. 2014, 55, 256–271",
    ],
    disclosed_subsystems=[
        "separation-affinity-capture",
        "thermal-isothermal-amplification",
    ],
    cpc_classifications=["G01N 33/18", "C12Q 1/68"],
)

add(
    id="ozcan-2010-smartphone-microscopy",
    canonical_name="Smartphone-based microscopy and microfluidic imaging (Ozcan 2010)",
    aliases=["Ozcan lensless microscopy", "smartphone microfluidic imaging"],
    corpus="academic",
    first_disclosure_date="2010",
    disclosure_citation="Tseng, D.; Mudanyali, O.; Oztoprak, C.; Isikman, S. O.; Sencan, I.; Yaglidere, O.; Ozcan, A. Lensfree microscopy on a cellphone. Lab Chip 2010, 10, 1787–1792. DOI: 10.1039/C003477B",
    creator="Ozcan group, UCLA",
    creator_country="US",
    device_class="other",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US9007433B2 (and Ozcan/UCLA family)"],
    prior_art_notes="Foundational disclosure of smartphone-based lensless holographic microscopy for chip imaging: a sample on a microfluidic chip is illuminated by an LED placed atop a smartphone camera, producing a holographic shadow that is computationally reconstructed into an image. Anticipates: smartphone-as-microscope architecture for field-deployable microfluidic diagnostics, lensless computational imaging on chip, and the entire smartphone-based POC imaging subfield. Underlies dozens of subsequent academic and commercial efforts (Cellscope, Nuralogix, Ozcan-spinout commercial products).",
    sources=[
        "Lab Chip 2010, 10, 1787–1792",
    ],
    disclosed_subsystems=[
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["G02B 21/00", "B01L 3/00"],
)

add(
    id="contreras-naranjo-2017-smartphone-microfluidic-review",
    canonical_name="Smartphone-based POC diagnostics review",
    aliases=["smartphone POC review"],
    corpus="academic",
    first_disclosure_date="2017",
    disclosure_citation="Contreras-Naranjo, J. C.; Wei, Q.; Ozcan, A. Mobile phone-based microscopy, sensing, and diagnostics. IEEE J. Sel. Top. Quantum Electron. 2016, 22, 7100414. DOI: 10.1109/JSTQE.2015.2478657",
    creator="Ozcan group, UCLA",
    creator_country="US",
    device_class="other",
    end_application="diagnostic",
    ip_status="public-domain",
    prior_art_notes="Comprehensive review of smartphone-based microfluidic POC diagnostics. Cited as the standard methodological reference for the subfield. Methodological — establishes the framework that any 'smartphone + microfluidic' patent must be evaluated against.",
    sources=[
        "IEEE J. Sel. Top. Quantum Electron. 2016, 22, 7100414",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="ballard-ozcan-2020-machine-learning-imaging",
    canonical_name="Deep learning for microfluidic imaging diagnostics (Ballard/Ozcan 2020)",
    aliases=["ML microfluidic imaging"],
    corpus="academic",
    first_disclosure_date="2020",
    disclosure_citation="Ballard, Z. S.; Brown, C.; Madni, A. M.; Ozcan, A. Machine learning and computation-enabled intelligent sensor design. Nat. Mach. Intell. 2021, 3, 556–565. DOI: 10.1038/s42256-021-00360-9",
    creator="Ozcan group, UCLA",
    creator_country="US",
    device_class="other",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Methodological framing of deep-learning-augmented microfluidic and POC sensors: ML for image enhancement, multiplexed assay readout, anomaly detection, and computational reconstruction of holographic data. Anticipates: ML-enabled POC microfluidic assays as a category, distinct from non-ML approaches by orders-of-magnitude improvement in sensitivity and specificity. Sets methodological framework for any 'AI-enhanced microfluidic diagnostic' patent claim.",
    sources=[
        "Nat. Mach. Intell. 2021, 3, 556–565",
    ],
    disclosed_subsystems=[
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["G06N 3/04", "G01N 33/543"],
)

add(
    id="zhang-cunningham-2014-smartphone-photonic-detection",
    canonical_name="Smartphone-based photonic-crystal biosensor",
    aliases=["Cunningham smartphone biosensor"],
    corpus="academic",
    first_disclosure_date="2013",
    disclosure_citation="Gallegos, D.; Long, K. D.; Yu, H.; Clark, P. P.; Lin, Y.; George, S.; Nath, P.; Cunningham, B. T. Label-free biodetection using a smartphone. Lab Chip 2013, 13, 2124–2132. DOI: 10.1039/C3LC40991K",
    creator="Cunningham group, UIUC",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Disclosed smartphone-based label-free biosensor: photonic-crystal resonant reflectance read by smartphone camera through diffraction-grating-based spectrometer attachment. Anticipates: photonic-crystal biosensor + smartphone optical readout, distinct architectural family from camera-based imaging POC tests.",
    sources=[
        "Lab Chip 2013, 13, 2124–2132",
    ],
    disclosed_subsystems=[
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["G01N 21/55", "B01L 3/00"],
)

add(
    id="kanakasabapathy-shafiee-2017-cellphone-fertility",
    canonical_name="Smartphone-based semen analysis (Kanakasabapathy 2017)",
    aliases=["smartphone semen analysis"],
    corpus="academic",
    first_disclosure_date="2017",
    disclosure_citation="Kanakasabapathy, M. K. et al. An automated smartphone-based diagnostic assay for point-of-care semen analysis. Sci. Transl. Med. 2017, 9, eaai7863. DOI: 10.1126/scitranslmed.aai7863",
    creator="Shafiee group, Harvard",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Disclosed smartphone-based semen analyzer: disposable microfluidic cartridge holds a semen sample under a low-magnification smartphone-attached lens, with computer-vision-based motility analysis on-device. Anticipates: at-home reproductive health POC microfluidic platform; commercialized by YO Sperm Test and competitors. Reference data point for the broader 'consumer-microfluidic-diagnostic at home' category.",
    sources=[
        "Sci. Transl. Med. 2017, 9, eaai7863",
    ],
    disclosed_subsystems=[
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["G01N 33/487", "B01L 3/00"],
)

add(
    id="psaltis-2014-color-changing-paper-microfluidic",
    canonical_name="Color-changing diagnostic paper microfluidics (multiple groups)",
    aliases=["paper-microfluidic colorimetric assays"],
    corpus="academic",
    first_disclosure_date="2010",
    disclosure_citation="Yetisen, A. K.; Akram, M. S.; Lowe, C. R. Paper-based microfluidic point-of-care diagnostic devices. Lab Chip 2013, 13, 2210–2251. DOI: 10.1039/C3LC50169H",
    creator="Yetisen, Lowe (Cambridge)",
    creator_country="GB",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="public-domain",
    prior_art_notes="Comprehensive review of paper-based microfluidic POC diagnostics: wax printing, hydrophobic patterning, multi-zone reagent staging, smartphone-camera readout. Cited as the standard reference for the entire paper-microfluidic POC subfield post-2010. Methodological complement to Whitesides foundational work and the Carrilho 2009 wax-printing recipe.",
    sources=[
        "Lab Chip 2013, 13, 2210–2251",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
    ],
    cpc_classifications=["B01L 3/00"],
    lineage_ancestors=["martinez-2007-paper-microfluidics", "franssila-2010-paper-fluidic-pcl"],
)


# =====================================================================
# Synthetic biology toolkits and instrument variants
# =====================================================================

add(
    id="echo-650-acoustic-dispenser-2009",
    canonical_name="Echo 650 high-throughput acoustic dispenser (Labcyte/Beckman)",
    aliases=["Echo 650"],
    corpus="private",
    first_disclosure_date="2009",
    disclosure_citation="Labcyte (now Beckman Coulter) Echo 525, 550, 650 product family. https://www.beckman.com/liquid-handlers/echo-650",
    creator="Labcyte / Beckman Coulter",
    creator_country="US",
    device_class="dispenser-pipettor",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="acoustic",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Higher-throughput sibling of the original Echo acoustic droplet ejection platform. Echo 650 supports 1536-well plates and DMSO/aqueous/glycerol fluid classes with 25 nL droplet volumes. Architectural extension of the Echo product line — same focused-acoustic-ejection mechanism but with throughput and fluid-class extensions.",
    sources=[
        "Beckman Coulter Echo 650 product literature",
    ],
    disclosed_subsystems=[
        "droplet-on-demand",
        "pump-acoustic-streaming",
    ],
    cpc_classifications=["B41J 2/14", "B01L 3/02"],
    lineage_ancestors=["echo-acoustic-dispenser"],
)

add(
    id="biotek-multiflo-flx-dispenser",
    canonical_name="BioTek MultiFlo FX dispenser",
    aliases=["MultiFlo FX", "BioTek MultiFlo"],
    corpus="private",
    first_disclosure_date="2010",
    disclosure_citation="Agilent Technologies BioTek MultiFlo FX. https://www.agilent.com",
    creator="BioTek (acquired by Agilent 2019)",
    creator_country="US",
    device_class="dispenser-pipettor",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Microplate dispenser/washer with peristaltic-pump-based reagent dispensing into 96/384/1536-well plates. Reference for the broader 'plate-format dispenser' product category that competes with Echo acoustic dispensing on cost and fluid compatibility (more inclusive of viscous fluids that Echo handles poorly).",
    sources=[
        "Agilent BioTek product literature",
    ],
    disclosed_subsystems=[
        "pump-peristaltic-on-chip",
    ],
    cpc_classifications=["B01L 3/02"],
)

add(
    id="formulatrix-rock-imager-microreactor",
    canonical_name="Formulatrix Rock Imager / Mantis nanodispenser",
    aliases=["Formulatrix Rock Imager", "Mantis dispenser"],
    corpus="private",
    first_disclosure_date="2008",
    disclosure_citation="Formulatrix Mantis liquid handler and Rock Imager. https://formulatrix.com",
    creator="Formulatrix Inc.",
    creator_country="US",
    device_class="dispenser-pipettor",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Microvolume dispenser optimized for protein crystallography and structural biology workflows: nanoliter-scale dispensing with 100+ tip channels for parallel screening. Architectural cousin of Mosquito (TTP Labtech) in this product category. Reference for the structural-biology-focused microfluidic dispenser segment.",
    sources=[
        "Formulatrix product literature",
    ],
    disclosed_subsystems=[
        "droplet-on-demand",
    ],
    cpc_classifications=["B01L 3/02"],
)

add(
    id="ttp-mosquito-nanoliter-dispenser",
    canonical_name="SPT Labtech Mosquito nanoliter pipettor",
    aliases=["Mosquito X1", "Mosquito HV"],
    corpus="private",
    first_disclosure_date="2003",
    disclosure_citation="SPT Labtech (formerly TTP Labtech) Mosquito product family. https://www.sptlabtech.com",
    creator="SPT Labtech / TTP Labtech",
    creator_country="GB",
    device_class="dispenser-pipettor",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disposable-tip nanoliter pipettor specifically designed for protein crystallography screening. The disposable-tip architecture eliminates cross-contamination concerns for low-volume dispensing of viscous and biological samples. Reference for the high-end nanodispenser segment.",
    sources=[
        "SPT Labtech product literature",
    ],
    disclosed_subsystems=[
        "droplet-on-demand",
    ],
    cpc_classifications=["B01L 3/02"],
)

add(
    id="ginkgo-bioworks-foundry",
    canonical_name="Ginkgo Bioworks synthetic biology foundry (microfluidic-equivalent strain engineering)",
    aliases=["Ginkgo foundry"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="Ginkgo Bioworks foundry platform. https://www.ginkgobioworks.com",
    creator="Ginkgo Bioworks",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="trade-secret",
    prior_art_notes="Industrial-scale synthetic biology automation platform integrating Echo dispensers, custom microfluidic cell-culture chips, and high-throughput screening robotics. While Ginkgo's specific architectures are proprietary, the integrated-foundry architectural pattern (combining commercial microfluidic instruments with custom integration software) is part of the broader synthetic-biology-automation prior art.",
    sources=[
        "Ginkgo Bioworks product literature",
        "various reverse-engineered descriptions in trade press",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["C12N 1/00"],
)


# =====================================================================
# More commercial cartridges, including pediatric/neonatal
# =====================================================================

add(
    id="sebia-capillarys-3",
    canonical_name="Sebia Capillarys hemoglobinopathy CE analyzer",
    aliases=["Sebia Capillarys", "Capillarys 3"],
    corpus="private",
    first_disclosure_date="2005",
    disclosure_citation="Sebia Capillarys product family. https://www.sebia.com",
    creator="Sebia (France)",
    creator_country="FR",
    device_class="lab-on-chip",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="electrokinetic",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Commercial multi-capillary CE analyzer for hemoglobinopathy screening (sickle cell, beta-thalassemia, etc.) widely used in newborn screening programs. Architectural cousin of academic CE chips at clinical-deployment scale. Reference for the hemoglobinopathy-screening cartridge product segment, particularly relevant for global low-and-middle-income-country newborn screening efforts.",
    sources=[
        "Sebia product literature",
    ],
    disclosed_subsystems=[
        "separation-capillary-electrophoresis",
    ],
    cpc_classifications=["G01N 27/447", "B01L 3/00"],
)

add(
    id="masimo-rad57-pulse-co-oximetry",
    canonical_name="Masimo Rad-57 pulse CO-oximetry sensor",
    aliases=["Masimo Rad-57"],
    corpus="private",
    first_disclosure_date="2005",
    disclosure_citation="Masimo Corporation Rad-57 Pulse CO-Oximeter. https://www.masimo.com",
    creator="Masimo Corporation",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Reusable optical sensor for pulse CO-oximetry: not microfluidic in the strict sense, but the sensor cuvette geometry and the broader pulse-oximetry product family include microfluidic-equivalent design considerations for sample (here, finger-tissue) interface. Reference for the broader 'wearable-sensor-without-fluidics' adjacent category.",
    sources=[
        "Masimo Rad-57 product literature",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["A61B 5/1455"],
    notes="Adjacent to microfluidics — pulse oximetry is a transcutaneous optical measurement rather than microfluidic, but the broader Masimo cartridge portfolio (e.g., RD SET, blood lab cartridges) includes proper microfluidic devices.",
)

add(
    id="trinity-biotech-premier-hba1c",
    canonical_name="Trinity Biotech Premier Hb9210 HbA1c analyzer cartridge",
    aliases=["Premier Hb9210"],
    corpus="private",
    first_disclosure_date="2009",
    disclosure_citation="Trinity Biotech Premier Hb9210. https://www.trinitybiotech.com",
    creator="Trinity Biotech (now Bio-Rad after 2024 acquisition)",
    creator_country="IE",
    device_class="lab-on-chip",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="HPLC-based hemoglobin A1c (HbA1c) analyzer with integrated microfluidic-equivalent column and sample handling. The HbA1c-by-HPLC product category is a major clinical lab segment for diabetes monitoring; Trinity Biotech, Bio-Rad Variant, and Tosoh G7/G8/G11 all compete in this space. Reference for the broader HbA1c cartridge market.",
    sources=[
        "Trinity Biotech product literature",
    ],
    disclosed_subsystems=[
        "separation-capillary-electrophoresis",
    ],
    cpc_classifications=["G01N 30/02", "B01L 3/00"],
)

add(
    id="i-stat-cartridge-cg8plus",
    canonical_name="i-STAT cartridge family (CHEM8+, CG8+, etc.)",
    aliases=["i-STAT CHEM8+", "i-STAT CG8+", "Abbott i-STAT cartridge"],
    corpus="private",
    first_disclosure_date="1992",
    disclosure_citation="i-STAT Corporation (acquired by Abbott 2003). i-STAT 1 system and cartridge family. FDA approval mid-1990s.",
    creator="i-STAT Corporation (Abbott Point of Care)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US5096669A (and i-STAT family)"],
    prior_art_notes="Foundational disclosure of integrated-blood-gas-and-chemistry POC cartridge: a single-use cartridge with sample-handling chamber, calibrant pouch, electrochemical sensor array, and reagent reservoirs in injection-molded thermoplastic. The i-STAT cartridge is among the longest-running and highest-volume POC cartridges in clinical use (1990s onward). Anticipates: integrated-biochemistry-cartridge architecture combining electrolyte, blood gas, and metabolite measurements in a single bedside device.",
    sources=[
        "i-STAT / Abbott Point of Care product literature",
        "US5096669A",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "fabrication-thermoplastic-injection-molding",
        "detection-electrochemical-on-chip",
        "pump-capillary-passive",
    ],
    cpc_classifications=["G01N 33/49", "B01L 3/00"],
    notes="Among the most architecturally important commercial POC cartridges — predates the µTAS-era academic POC research program by ~10 years and operationally proves the integrated-cartridge architectural pattern at clinical scale.",
)

add(
    id="epoc-blood-gas-analyzer",
    canonical_name="Siemens epoc Blood Analysis System cartridge",
    aliases=["epoc Blood Analyzer"],
    corpus="private",
    first_disclosure_date="2006",
    disclosure_citation="Siemens Healthineers epoc system. https://www.siemens-healthineers.com",
    creator="Epocal (acquired by Siemens / now part of Siemens Healthineers)",
    creator_country="CA",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="POC blood gas / chemistry / hematology cartridge with disposable test card and Bluetooth-connected reader. Architectural cousin of i-STAT in the same product category. Smaller cartridge form factor and Bluetooth-rather-than-direct-instrument architecture are differentiators.",
    sources=[
        "Siemens Healthineers product literature",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "fabrication-thermoplastic-injection-molding",
        "detection-electrochemical-on-chip",
    ],
    cpc_classifications=["G01N 33/49"],
    lineage_ancestors=["i-stat-cartridge-cg8plus"],
)

add(
    id="instrumentation-laboratory-gem-premier",
    canonical_name="Werfen GEM Premier 5000 blood gas cartridge",
    aliases=["GEM Premier", "Werfen GEM"],
    corpus="private",
    first_disclosure_date="2002",
    disclosure_citation="Werfen Instrumentation Laboratory GEM Premier system. https://www.werfen.com",
    creator="Instrumentation Laboratory (Werfen)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Cartridge-based blood gas analyzer with extended on-cartridge calibration and quality control. The GEM Premier cartridge contains all reagents, calibrants, and waste reservoirs sufficient for several hundred patient samples before replacement. Architectural cousin of i-STAT and Siemens epoc but at higher per-cartridge throughput. Reference for the multi-sample-cartridge POC blood gas segment.",
    sources=[
        "Werfen / Instrumentation Laboratory product literature",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "fabrication-thermoplastic-injection-molding",
        "detection-electrochemical-on-chip",
    ],
    cpc_classifications=["G01N 33/49"],
    lineage_ancestors=["i-stat-cartridge-cg8plus"],
)


# =====================================================================
# Open hardware — community labs and biology spaces
# =====================================================================

add(
    id="hackuarium-community-lab",
    canonical_name="Hackuarium community DIY-bio lab",
    aliases=["Hackuarium"],
    corpus="open",
    first_disclosure_date="2014",
    disclosure_citation="Hackuarium community biology space, Lausanne. https://www.hackuarium.ch",
    creator="Hackuarium collective",
    creator_country="CH",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Swiss community DIY-bio lab focused on accessible microfluidic and microbiology projects. Documented projects include open syringe pumps, fluorescent microscopy hacks, and microfluidic chip prototyping. Reference for the European DIY-bio community-lab ecosystem complementing US-based Hackteria and BioCurious.",
    sources=[
        "https://www.hackuarium.ch",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="genspace-community-lab",
    canonical_name="Genspace NYC community biology lab",
    aliases=["Genspace"],
    corpus="open",
    first_disclosure_date="2010",
    disclosure_citation="Genspace community biology lab, Brooklyn NY. https://www.genspace.org",
    creator="Genspace",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="The first community biology lab in the US (founded 2010 in Brooklyn). Hosts microfluidic project teaching and serves as community-lab-format reference. Together with BioCurious (Sunnyvale), Counter Culture Labs (Oakland), and Hackuarium (Lausanne), defines the global community-lab ecosystem for amateur biology with microfluidic adjacencies.",
    sources=[
        "https://www.genspace.org",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="la-paillasse-community-lab",
    canonical_name="La Paillasse Paris community biology lab",
    aliases=["La Paillasse"],
    corpus="open",
    first_disclosure_date="2011",
    disclosure_citation="La Paillasse community biology lab, Paris. (closed 2018 but historical reference; community continues via DIY-bio-Paris)",
    creator="La Paillasse collective",
    creator_country="FR",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="French community biology lab founded 2011, prominent during 2011–2018. Hosted microfluidic-related DIY projects and served as the European-side anchor for community-lab DIY-bio efforts. Closed in 2018 but historically significant reference for the European community-lab ecosystem.",
    sources=[
        "Various press coverage 2011–2018",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="counter-culture-labs",
    canonical_name="Counter Culture Labs community biology lab Oakland",
    aliases=["Counter Culture Labs"],
    corpus="open",
    first_disclosure_date="2013",
    disclosure_citation="Counter Culture Labs community biology space, Oakland. https://www.counterculturelabs.org",
    creator="Counter Culture Labs",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Bay-Area community biology lab — together with Genspace (NYC), BioCurious (Sunnyvale), and Hackuarium (Lausanne) defines the broader community-lab DIY-bio ecosystem within which microfluidic open-hardware projects are developed and taught.",
    sources=[
        "https://www.counterculturelabs.org",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# =====================================================================
# More academic — environmental, agricultural
# =====================================================================

add(
    id="cady-2003-agricultural-pathogen-cartridge",
    canonical_name="Field-deployable agricultural pathogen detection cartridges (Cady 2003 lineage)",
    aliases=["agricultural POC cartridge"],
    corpus="academic",
    first_disclosure_date="2005",
    disclosure_citation="Cady, N. C. et al. Real-time PCR detection of Listeria monocytogenes using an integrated microfluidic platform. Sens. Actuators B Chem. 2005, 107, 332–341. DOI: 10.1016/j.snb.2004.10.022",
    creator="Various — Cady (Cornell) / Lampe lineage",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Foundational disclosure of agricultural / food-pathogen detection on integrated microfluidic platform: Listeria monocytogenes detection from food matrix by integrated lyse-extract-amplify-detect cartridge. Anticipates: agricultural-context integrated-PCR-cartridge architecture, distinct from clinical cartridges by emphasizing food-matrix sample-prep upstream. Underlies subsequent commercial efforts by Neogen, 3M Petrifilm, and academic agricultural-pathogen-cartridge programs.",
    sources=[
        "Sens. Actuators B Chem. 2005, 107, 332–341",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-pcr-cycling",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/686"],
)

add(
    id="quake-2003-microfluidic-protein-crystallization",
    canonical_name="Microfluidic protein crystallization in nanoliter chambers",
    aliases=["microfluidic crystallography"],
    corpus="academic",
    first_disclosure_date="2002",
    disclosure_citation="Hansen, C. L.; Skordalakes, E.; Berger, J. M.; Quake, S. R. A robust and scalable microfluidic metering method that allows protein crystal growth by free interface diffusion. Proc. Natl. Acad. Sci. USA 2002, 99, 16531–16536. DOI: 10.1073/pnas.262485199",
    creator="Quake group, Caltech",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US7195670B2 (and Fluidigm family)"],
    prior_art_notes="Disclosed PDMS-Quake-valve-based protein crystallization screening: hundreds of nanoliter-scale crystallization chambers in parallel using free-interface diffusion as the supersaturation mechanism. Architectural ancestor of Fluidigm Topaz protein crystallization chip — and of the broader nanoliter-screen / structural-biology automation that competes with Mosquito / Formulatrix dispensers.",
    sources=[
        "Proc. Natl. Acad. Sci. USA 2002, 99, 16531–16536",
    ],
    disclosed_subsystems=[
        "valve-quake-pneumatic-membrane",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["C30B 7/00", "B01L 3/00"],
    lineage_ancestors=["unger-2000-quake-monolithic-membrane-valve"],
)


# =====================================================================
# More fictional
# =====================================================================

add(
    id="for-all-mankind-jamestown-medbay",
    canonical_name="For All Mankind Jamestown lunar medbay",
    aliases=["Jamestown medbay", "FAM lunar medical"],
    corpus="fictional",
    first_disclosure_date="2019",
    disclosure_citation="For All Mankind (Apple TV+, 2019–).",
    creator="Ronald D. Moore / Apple TV",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Detailed depictions of NASA-aesthetic lunar / Mars medbay automation including microfluidic-equivalent on-cartridge diagnostics in low-resource extraplanetary settings. Architecturally specific enough to count as conceptual prior art for compact, autonomous, sustained-mission diagnostic microfluidic platforms. Cumulative fictional-prior-art data point.",
    sources=[
        "For All Mankind (2019–)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="severance-medical-floor-procedures",
    canonical_name="Severance medical procedures and 'wellness' depictions",
    aliases=["Severance medical procedures"],
    corpus="fictional",
    first_disclosure_date="2022",
    disclosure_citation="Severance (Apple TV+, 2022–).",
    creator="Dan Erickson / Ben Stiller / Apple TV",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Visual depictions of unconventional bedside procedure rooms with custom diagnostic equipment. Architecturally specific enough to count as a fictional-prior-art reference for unconventional bedside-equipment configurations. Cumulative cultural-priors data point.",
    sources=[
        "Severance (2022–)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# Write out
with CORPUS.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new entries to {CORPUS}")
