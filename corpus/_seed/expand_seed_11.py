#!/usr/bin/env python3
"""Eleventh expansion seed for free-microfluidics-corpus.

~30 more entries:
  - Manz-Ciba-Geigy 1989-1992 patent estate (foundational µTAS patents)
  - Asian academic groups (Tsinghua, Peking U, POSTECH, NUS)
  - More recent CRISPR-on-chip variants (Pasteur, Mammoth)
  - Open hardware automation (Opentrons variants, Pumpy successors)
  - More fictional (more 2025+ depictions)
  - Environmental microbiome cartridges
  - More 1990s-era foundational (more Manz, Harrison, Ramsey work)
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
# Manz-Ciba-Geigy foundational patent estate
# =====================================================================

add(
    id="manz-1992-ciba-geigy-mu-tas-patent-original",
    canonical_name="Manz / Ciba-Geigy original µTAS patent (1990 priority)",
    aliases=["Manz Ciba-Geigy patent", "EP0497077A1"],
    corpus="academic",
    first_disclosure_date="1990",
    disclosure_citation="Manz, A. et al. EP0497077A1 / WO9217767A1: Process for separating substances by capillary electrophoresis on chip. Priority date 1991, filed 1992 by Ciba-Geigy AG.",
    creator="Andreas Manz, Hans-Michael Widmer (Ciba-Geigy AG, Basel)",
    creator_country="CH",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="analytical",
    ip_status="patented",
    ip_citations=["EP0497077A1", "WO9217767A1", "US5180480A"],
    prior_art_notes="The seminal Ciba-Geigy patent estate filed by Manz and Widmer covering chip-format capillary electrophoresis with electroosmotic pumping. The 1990 priority date predates the Manz 1990 academic paper publication, making this patent family the dominant foundational IP for chip CE. Ciba-Geigy (later Novartis) held this patent estate through expiry in 2010-2012, generating significant licensing revenue from chip-CE-based instruments. Doctrinally critical: any patent asserting novelty for chip-format electrokinetic separation must address this prior art chain.",
    sources=[
        "EP0497077A1",
        "WO9217767A1",
        "US5180480A",
    ],
    disclosed_subsystems=[
        "fabrication-glass-hf-etching",
        "separation-capillary-electrophoresis",
        "pump-electroosmotic",
    ],
    cpc_classifications=["G01N 27/447", "B01L 3/00"],
    notes="The patent precedes the Manz 1990 academic paper by months, meaning the patent priority date (not the journal publication) is the legally effective prior-art date for chip CE. Ciba-Geigy / Novartis aggressively enforced this estate against early commercial chip-CE entrants.",
)

add(
    id="manz-1993-on-chip-injection-patent",
    canonical_name="On-chip electrokinetic injection patent (Manz / Ciba-Geigy 1993)",
    aliases=["Manz electrokinetic injection patent"],
    corpus="academic",
    first_disclosure_date="1993",
    disclosure_citation="Manz, A. et al. EP0653206 / US5500071: Method of injecting samples in chip-format CE using electrokinetic gating. Filed 1993, granted 1996.",
    creator="Manz / Widmer (Ciba-Geigy AG)",
    creator_country="CH",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="analytical",
    ip_status="patented",
    ip_citations=["EP0653206", "US5500071"],
    prior_art_notes="Companion to the foundational Ciba-Geigy patent: covers electrokinetic gated injection (cross-tee + voltage-switching) as the dominant method for sample plug definition in chip CE. This injection scheme is the de facto standard for all academic and commercial chip-CE platforms; the patent's expiration in ~2014 freed downstream developers to use the injection scheme without licensing.",
    sources=[
        "EP0653206",
        "US5500071",
    ],
    disclosed_subsystems=[
        "separation-capillary-electrophoresis",
        "pump-electroosmotic",
    ],
    cpc_classifications=["G01N 27/447", "B01L 3/00"],
    lineage_ancestors=["manz-1992-ciba-geigy-mu-tas-patent-original"],
)

add(
    id="caliper-acla-chip-1999",
    canonical_name="Caliper LabChip / ACLA chip technology (acquired by Ciba-Geigy lineage)",
    aliases=["Caliper LabChip", "Caliper ACLA"],
    corpus="private",
    first_disclosure_date="1996",
    disclosure_citation="Caliper Life Sciences (formerly Caliper Technologies) LabChip platform; acquired by PerkinElmer 2011. https://www.perkinelmer.com",
    creator="Caliper Technologies → Caliper Life Sciences → PerkinElmer",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="analytical",
    ip_status="patented",
    ip_citations=["US5571410A (Caliper / Parce family)"],
    prior_art_notes="Foundational commercial implementation of glass chip CE for protein and nucleic acid separation. The Caliper LabChip platform was the dominant academic-research chip CE platform 2000-2010 before being eclipsed by capillary instruments. Caliper held a substantial patent estate covering chip-format separations, integrated multi-channel architectures, and droplet manipulation. Acquired by PerkinElmer 2011; underlies many commercial DNA / RNA / protein gel-equivalent chip products.",
    sources=[
        "Caliper Life Sciences / PerkinElmer product literature",
        "Various Parce / Caliper patents",
    ],
    disclosed_subsystems=[
        "fabrication-glass-hf-etching",
        "separation-capillary-electrophoresis",
        "pump-electroosmotic",
    ],
    cpc_classifications=["G01N 27/447", "B01L 3/00"],
    lineage_ancestors=["manz-1992-ciba-geigy-mu-tas-patent-original"],
)


# =====================================================================
# Asian academic groups
# =====================================================================

add(
    id="tsinghua-microfluidics-program",
    canonical_name="Tsinghua University microfluidics program",
    aliases=["Tsinghua microfluidics", "Lin Bingcheng group"],
    corpus="academic",
    first_disclosure_date="2000",
    disclosure_citation="Various Tsinghua University publications 2000-onward, primarily from Lin Bingcheng group and Bao group on microfluidic chips for proteomics and clinical diagnostics.",
    creator="Lin Bingcheng group, Tsinghua University",
    creator_country="CN",
    device_class="other",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Composite reference for the Tsinghua University microfluidics research program — among the largest microfluidics academic research programs in China. Cumulative disclosures cover chip-format proteomics, clinical diagnostic cartridges, single-cell analysis, and droplet microfluidics. Significant patent estate filed primarily in CN with selective international filings; under-cited in US prior-art databases.",
    sources=[
        "Various Tsinghua University publications",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="peking-u-microfluidics-cao",
    canonical_name="Peking University microfluidic biotechnology (Cao group)",
    aliases=["Peking U microfluidics", "Cao group Peking"],
    corpus="academic",
    first_disclosure_date="2005",
    disclosure_citation="Various Peking University publications 2005-onward on microfluidic biotechnology and POC diagnostics.",
    creator="Cao / Huang groups, Peking University",
    creator_country="CN",
    device_class="other",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Composite reference for the Peking University microfluidics research program with focus on POC molecular diagnostics, single-cell analysis, and CRISPR cartridge development. Cumulative disclosures include early-stage versions of architectures later commercialized by Chinese diagnostic companies.",
    sources=[
        "Various Peking University publications",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="postech-microfluidics-suh",
    canonical_name="POSTECH microfluidic platforms (Kahp-Yang Suh / Korean lineage)",
    aliases=["POSTECH microfluidics", "Suh group Korea"],
    corpus="academic",
    first_disclosure_date="2002",
    disclosure_citation="Various Pohang University of Science and Technology publications. Suh group worked on capillary force lithography and microfluidic surface patterning prior to Suh's joining Seoul National University.",
    creator="Kahp-Yang Suh / Korean microfluidics lineage",
    creator_country="KR",
    device_class="other",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Composite reference for the Korean microfluidics research lineage anchored at POSTECH and Seoul National University. Notable contributions include capillary force lithography for soft-microfluidic patterning and significant work on PDMS-based organ-on-chip designs. Cumulative Korean academic patent filings under-cite in US prior-art databases.",
    sources=[
        "Various POSTECH / SNU publications",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="nus-microfluidics-lim",
    canonical_name="NUS microfluidic platforms (Lim group, Chen group)",
    aliases=["NUS microfluidics", "Singapore microfluidics"],
    corpus="academic",
    first_disclosure_date="2008",
    disclosure_citation="Various NUS / NTU Singapore publications on microfluidic CTC isolation and cell-mechanics platforms.",
    creator="Chwee Teck Lim group / various, National University of Singapore",
    creator_country="SG",
    device_class="other",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Composite reference for the Singapore microfluidics ecosystem anchored at NUS and NTU. Lim group at NUS produced significant work on inertial CTC isolation that was commercialized through Clearbridge BioMedics (acquired by Biolidics 2018). Singapore-based academic-to-commercial pipeline is among the more productive in Asia for microfluidic technology transfer.",
    sources=[
        "Various NUS / NTU publications",
        "Clearbridge BioMedics / Biolidics product literature",
    ],
    disclosed_subsystems=[
        "separation-inertial-focusing",
    ],
    cpc_classifications=["B01L 3/00"],
    lineage_ancestors=["di-carlo-2007-inertial-microfluidics"],
)

add(
    id="bgi-mgi-cartridge-extensions",
    canonical_name="BGI / MGI cartridge product family extensions",
    aliases=["BGI cartridge family", "MGI sequencing platforms"],
    corpus="private",
    first_disclosure_date="2017",
    disclosure_citation="BGI MGI subsidiary product family. https://en.mgi-tech.com",
    creator="BGI / MGI Tech",
    creator_country="CN",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="MGI Tech is BGI's sequencing-instrument subsidiary; cumulative MGI cartridge product family (DNBSEQ-T7, DNBSEQ-G400, etc.) extends the original Complete Genomics DNB technology with multiple instrument configurations. Together with native Chinese semiconductor manufacturing, MGI is positioned to compete with Illumina globally. Cumulative cartridge architectural disclosures from this family expand the broader sequencing-cartridge prior art.",
    sources=[
        "MGI Tech product literature",
    ],
    disclosed_subsystems=[
        "fabrication-silicon-drie",
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["C12Q 1/68"],
    lineage_ancestors=["bgi-mgi-dnbseq-flowcell"],
)


# =====================================================================
# Recent CRISPR cartridge variants
# =====================================================================

add(
    id="mammoth-detectr-boost-cartridge",
    canonical_name="Mammoth Biosciences DETECTR BOOST cartridge",
    aliases=["DETECTR BOOST", "Mammoth cartridge"],
    corpus="private",
    first_disclosure_date="2022",
    disclosure_citation="Mammoth Biosciences DETECTR BOOST. https://mammoth.bio",
    creator="Mammoth Biosciences",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Commercial DETECTR-platform CRISPR cartridge: integrated sample-prep, RPA amplification, Cas12a-based detection in single-use cartridge format. Anticipates: high-throughput automated CRISPR diagnostic cartridges as a commercial product category. Companion to academic disclosures (Chen 2018 DETECTR foundational, Myhrvold 2018 SHINE) by establishing instrument-format CRISPR-cartridge architecture.",
    sources=[
        "Mammoth Biosciences product literature",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-isothermal-amplification",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/68"],
    lineage_ancestors=["chen-doudna-2018-detectr"],
)

add(
    id="sherlock-biosciences-inspectr",
    canonical_name="Sherlock Biosciences INSPECTR cartridge",
    aliases=["INSPECTR", "Sherlock cartridge"],
    corpus="private",
    first_disclosure_date="2023",
    disclosure_citation="Sherlock Biosciences INSPECTR product family. https://sherlock.bio",
    creator="Sherlock Biosciences",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Commercial SHERLOCK-platform CRISPR cartridge: SHERLOCK Cas13-based detection in single-use cartridge with smartphone or instrument readout. Direct architectural cousin of Mammoth DETECTR BOOST but with Cas13 enzyme and different sample-prep chemistry. Reference for the broader CRISPR-cartridge product category alongside the academic foundational disclosures.",
    sources=[
        "Sherlock Biosciences product literature",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-isothermal-amplification",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/68"],
    lineage_ancestors=["gootenberg-zhang-2017-sherlock", "myhrvold-zhang-2018-shine-crispr-on-paper"],
)

add(
    id="pasteur-crispr-cartridge-academic",
    canonical_name="Institut Pasteur CRISPR cartridge work (academic)",
    aliases=["Pasteur CRISPR cartridge"],
    corpus="academic",
    first_disclosure_date="2020",
    disclosure_citation="Various Institut Pasteur publications 2020-2024 on CRISPR-cartridge POC diagnostic development.",
    creator="Various Pasteur lineage groups",
    creator_country="FR",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Composite reference for European CRISPR-cartridge academic work centered at Institut Pasteur, complementing US (Sherlock, Mammoth, Broad) and academic-to-commercial pipelines. The Pasteur lineage is particularly strong in tropical disease applications (Plasmodium, dengue, chikungunya) where CRISPR cartridge architectures have specific advantages.",
    sources=[
        "Various Pasteur publications",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-isothermal-amplification",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/68"],
    lineage_ancestors=["gootenberg-zhang-2017-sherlock"],
)


# =====================================================================
# Open hardware automation
# =====================================================================

add(
    id="opentrons-ot-2-liquid-handler",
    canonical_name="Opentrons OT-2 open-source liquid handler",
    aliases=["Opentrons OT-2", "OT-2"],
    corpus="open",
    first_disclosure_date="2018",
    disclosure_citation="Opentrons Labworks OT-2 / Flex liquid handler. https://opentrons.com",
    creator="Opentrons Labworks Inc.",
    creator_country="US",
    device_class="dispenser-pipettor",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="The dominant open-source liquid handler — sub-$5k benchtop instrument with Python API and open-source documentation, deployed at academic labs worldwide. While the OT-2 is microfluidic-adjacent rather than directly microfluidic (handling µL- to mL-volumes rather than nanoliter on-chip volumes), it serves as the integration platform for many microfluidic workflows: OT-2 dispenses samples into chips, fills reservoirs, and runs sample-prep protocols upstream of microfluidic measurement.",
    sources=[
        "Opentrons OT-2 product literature",
        "https://opentrons.com",
    ],
    disclosed_subsystems=[
        "droplet-on-demand",
    ],
    cpc_classifications=["B01L 3/02"],
)

add(
    id="opentrons-flex-liquid-handler",
    canonical_name="Opentrons Flex liquid handler (2023 successor)",
    aliases=["Opentrons Flex"],
    corpus="open",
    first_disclosure_date="2023",
    disclosure_citation="Opentrons Labworks Flex liquid handler. https://opentrons.com/flex",
    creator="Opentrons Labworks Inc.",
    creator_country="US",
    device_class="dispenser-pipettor",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Direct successor to OT-2 with ~$25k pricing and added capabilities including HEPA enclosure, 96-channel pipettor, gripper for plate movement. Open-source software (Python protocol API) preserved from OT-2; competes with Hamilton Microlab and Tecan Freedom EVO at much lower price point.",
    sources=[
        "Opentrons Flex product literature",
    ],
    disclosed_subsystems=[
        "droplet-on-demand",
    ],
    cpc_classifications=["B01L 3/02"],
    lineage_ancestors=["opentrons-ot-2-liquid-handler"],
)

add(
    id="open-pid-controller-microfluidics",
    canonical_name="Open PID controllers for microfluidic flow / pressure / temperature",
    aliases=["open PID microfluidics"],
    corpus="open",
    first_disclosure_date="2020",
    disclosure_citation="Various community projects implementing open-source PID controllers for microfluidic experimental control. Representative: simple-pid Python library, BeagleBone-based controllers.",
    creator="Various community contributors",
    creator_country="GLOBAL",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Reference for the broader open-source PID controller ecosystem applied to microfluidic flow control, pressure regulation, and temperature stabilization. Significant in lowering the barrier for academic groups to implement closed-loop control on custom-built instruments without specialized control-systems engineering expertise.",
    sources=[
        "Various github repositories",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="open-microfluidic-edge-edu-kits",
    canonical_name="Educational microfluidic kits for K-12 and undergraduate teaching",
    aliases=["microfluidic education kits", "BIOMED Hub microfluidic education"],
    corpus="open",
    first_disclosure_date="2018",
    disclosure_citation="Various — Hands-on microfluidics education kits from BIOMED Hub, NSFRET-funded projects, and academic teaching laboratories.",
    creator="Various academic and educational projects",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Reference for the broader microfluidic-education ecosystem: cost-reduced demonstration kits for K-12 and undergraduate teaching, including paper-microfluidic exercises, CD-format centrifugal LoD demonstrations, and PDMS soft-lithography teaching kits. Significant in establishing prior-art chains for educational and demonstration-scale microfluidic systems that often appear in undergraduate textbooks before commercial product literature.",
    sources=[
        "Various educational program materials",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# =====================================================================
# More academic — environmental microbiome
# =====================================================================

add(
    id="environmental-microbiome-cartridge-2024",
    canonical_name="Environmental microbiome sample-to-sequencing cartridges (2024 academic)",
    aliases=["environmental microbiome cartridge"],
    corpus="academic",
    first_disclosure_date="2024",
    disclosure_citation="Various 2024-2026 publications on environmental microbiome sample-to-sequencing integrated cartridges.",
    creator="Various groups",
    creator_country="GLOBAL",
    device_class="point-of-care-cartridge",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Composite reference for emerging sample-to-sequencing microbiome cartridges: lyse-extract-amplify-sequence in integrated disposable cartridges for soil, water, and air microbiome surveillance. The combination of long-read sequencing (Oxford Nanopore MinION) with cartridge-format sample prep enables true field-deployable microbiome analysis.",
    sources=[
        "Various 2024-2026 publications",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-pcr-cycling",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/68"],
    lineage_ancestors=["bridle-2014-soil-microfluidic-extraction", "oxford-nanopore-minion"],
)

add(
    id="zhang-2023-organ-on-chip-cancer-immunotherapy",
    canonical_name="Cancer-immunotherapy organ-on-chip (2023-2026 academic)",
    aliases=["cancer-immunotherapy organ-on-chip"],
    corpus="academic",
    first_disclosure_date="2023",
    disclosure_citation="Various 2023-2026 publications on cancer-immunotherapy organ-on-chip platforms. Representative: tumor-on-chip with CAR-T co-culture for response prediction.",
    creator="Various groups",
    creator_country="GLOBAL",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Composite reference for the 2023-onward wave of cancer-immunotherapy organ-on-chip work: patient-derived tumor organoids in microfluidic chambers with autologous immune-cell perfusion, used for personalized response prediction. Architectural successor to body-on-chip multi-tissue platforms (Wikswo 2013) by incorporating immune-cell trafficking specifically.",
    sources=[
        "Various 2023-2026 publications",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-organ-on-chip-vasculature",
    ],
    cpc_classifications=["C12M 1/00"],
    lineage_ancestors=["organoid-on-chip-clevers-2020", "wikswo-2013-multi-organ-chip"],
)

add(
    id="microfluidic-electroporation-cell-therapy",
    canonical_name="Microfluidic electroporation for cell therapy manufacturing",
    aliases=["microfluidic electroporation"],
    corpus="academic",
    first_disclosure_date="2018",
    disclosure_citation="Various publications on microfluidic mechanical and electrical-poration for non-viral gene delivery to cells. Representative: SQZ Biotechnologies cell-squeeze platform; Kwong et al. 2014 Nano Lett. for nanoneedle approach.",
    creator="Various — Sharei (SQZ), Kwong, Melosh labs",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="other",
    ip_status="patented",
    ip_citations=["US10696944B2 (SQZ Biotech family)"],
    prior_art_notes="Microfluidic constriction-based mechanical poration: cells passing through narrow constriction transiently form membrane pores, allowing delivery of macromolecules without electrical field. Architectural alternative to electroporation for non-viral cell engineering. Underlies SQZ Biotechnologies (acquired 2024) and several academic spinout efforts.",
    sources=[
        "Various publications including Sharei et al. 2013 PNAS",
        "SQZ Biotechnologies patent family",
    ],
    disclosed_subsystems=[
        "cell-encapsulation-droplet",
    ],
    cpc_classifications=["C12N 13/00", "C12N 15/89"],
)


# =====================================================================
# More fictional
# =====================================================================

add(
    id="fallout-tv-vault-medbay-2024",
    canonical_name="Fallout (Amazon) Vault medbay depictions (2024)",
    aliases=["Fallout Amazon medbay"],
    corpus="fictional",
    first_disclosure_date="2024",
    disclosure_citation="Fallout (Amazon Prime Video, 2024–). Based on Bethesda video game franchise.",
    creator="Bethesda / Amazon Studios",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Detailed depictions of post-apocalyptic Vault medical infrastructure including microfluidic-equivalent diagnostic devices and sample-handling stations. Cumulative TV/gaming-cultural-reference data point for fictional retro-futuristic microfluidic-equivalent depictions.",
    sources=[
        "Fallout (Amazon Prime Video, 2024)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="dune-2-stillsuit-fluid-recycling",
    canonical_name="Dune Part Two stillsuit body-fluid recycling (2024)",
    aliases=["Dune stillsuit", "Dune 2024"],
    corpus="fictional",
    first_disclosure_date="2024",
    disclosure_citation="Dune: Part Two (2024), Warner Bros. Based on Frank Herbert's 1965 novel.",
    creator="Denis Villeneuve / Warner Bros / Frank Herbert source",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="other",
    ip_status="fictional",
    prior_art_notes="Iconic fictional body-fluid recycling system: full-body suit collects perspiration, urine, and breath moisture, processes through reclamation system, returns drinkable water. Architecturally a wearable microfluidic-equivalent fluid-processing system. The 2024 film adaptation includes detailed visual depictions of stillsuit interior plumbing and processing modules. Cumulative SF-cultural-reference data point spanning 1965 novel through 2024 film.",
    sources=[
        "Dune: Part Two (2024)",
        "Herbert, F. Dune (1965)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="cyberpunk-edgerunners-ripperdoc",
    canonical_name="Cyberpunk Edgerunners ripperdoc body-mod fluid handling",
    aliases=["Cyberpunk Edgerunners", "Edgerunners ripperdoc"],
    corpus="fictional",
    first_disclosure_date="2022",
    disclosure_citation="Cyberpunk Edgerunners (Studio Trigger / Netflix, 2022). Set in CD Projekt's Cyberpunk 2077 game universe.",
    creator="Studio Trigger / CD Projekt / Netflix",
    creator_country="JP",
    device_class="fictional-laboratory",
    end_application="other",
    ip_status="fictional",
    prior_art_notes="Anime expansion of Cyberpunk 2077 universe with detailed depictions of ripperdoc surgical / body-modification stations including microfluidic-equivalent cyberware-installation fluid systems. Cumulative anime/gaming-cultural-reference data point for fictional cyberware-installation microfluidic-equivalent depictions.",
    sources=[
        "Cyberpunk Edgerunners (2022)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# =====================================================================
# More private cartridges
# =====================================================================

add(
    id="bd-veritor-rapid-test",
    canonical_name="BD Veritor rapid test platform",
    aliases=["BD Veritor", "BD Veritor Plus"],
    corpus="private",
    first_disclosure_date="2011",
    disclosure_citation="Becton Dickinson BD Veritor System. https://www.bd.com",
    creator="Becton Dickinson",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="BD Veritor cartridge family covers respiratory infection rapid antigen tests with companion benchtop reader. The cartridge format is a standard lateral-flow strip in a BD-proprietary cassette housing. The dominant POC influenza/RSV/COVID antigen test platform in U.S. clinical labs and emergency departments.",
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
    id="quidel-sofia-2",
    canonical_name="Quidel Sofia 2 fluorescent immunoassay analyzer",
    aliases=["Quidel Sofia 2", "Sofia 2 SARS"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="QuidelOrtho Sofia 2 Fluorescent Immunoassay Analyzer. https://www.quidelortho.com",
    creator="Quidel / QuidelOrtho",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Cartridge-based fluorescent lateral-flow immunoassay platform: standard LFA strip with fluorescent (rather than colorimetric) labels and benchtop fluorescence reader. Architectural cousin of BD Veritor with fluorescent rather than visible-light readout, offering improved sensitivity. Major POC respiratory infection test platform.",
    sources=[
        "QuidelOrtho product literature",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
    ],
    cpc_classifications=["G01N 33/543"],
)


# Write out
with CORPUS.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new entries to {CORPUS}")
