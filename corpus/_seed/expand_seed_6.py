#!/usr/bin/env python3
"""Sixth expansion seed for free-microfluidics-corpus.

~35 more entries:
  - More 1990s µTAS foundations (Jacobson 1994b, Harrison 1993, Effenhauser variants)
  - Body-on-chip variants (gut-on-chip Kim 2012, kidney Jang, BBB Booth, liver Bhushan)
  - Mass spec interfaces (Karger CE-MS, sheath-flow ESI, IonOptix microneedle)
  - More international patent thicket (Sysmex, Roche Mannheim, Beckman Coulter, Hitachi)
  - Microfluidic synthesis (Jensen DARPA OMNI, Ley flow chemistry)
  - Wearable POC (Abbott CGM Libre detail, Dexcom G7, sensor-on-skin)
  - More open hardware (Public Lab, FlexiLab, Backyard Brains)
  - More fictional (Star Trek replicator, BSG medbay, Westworld bioprinter detail)
  - Fluidic-mechanics theory updates (Stone droplet review, Anna review)
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
# ACADEMIC — more µTAS foundations and body-on-chip
# =====================================================================

add(
    id="harrison-1993-electroosmotic-cycling",
    canonical_name="Electroosmotic injection / pumping on chip CE",
    aliases=["Harrison 1993 electroosmotic"],
    corpus="academic",
    first_disclosure_date="1993",
    disclosure_citation="Harrison, D. J.; Fluri, K.; Seiler, K.; Fan, Z.; Effenhauser, C. S.; Manz, A. Micromachining a miniaturized capillary electrophoresis-based chemical analysis system on a chip. Science 1993, 261, 895–897. DOI: 10.1126/science.261.5123.895",
    creator="Harrison group, Alberta",
    creator_country="CA",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="analytical",
    ip_status="public-domain",
    prior_art_notes="Companion to Harrison 1992 / Manz 1990 establishing electroosmotic pumping on glass CE chips. Demonstrated reproducible voltage-controlled fluid handling on-chip without mechanical pumps — pure electrokinetic transport with sub-nanoliter sample plug definition. Anticipates: voltage-as-pump for chip CE, programmable electrokinetic flow control, and the electroosmotic pumping paradigm that became the de facto fluid-handling method for chip CE before pressure-driven systems took over.",
    sources=[
        "Science 1993, 261, 895–897",
    ],
    disclosed_subsystems=[
        "fabrication-glass-hf-etching",
        "separation-capillary-electrophoresis",
        "pump-electroosmotic",
    ],
    cpc_classifications=["B01L 3/00", "G01N 27/447"],
    lineage_ancestors=["harrison-1992-cap-electrophoresis-on-chip"],
)

add(
    id="kim-ingber-2012-gut-on-chip",
    canonical_name="Gut-on-chip with peristalsis-mimicking mechanical strain",
    aliases=["gut-on-chip", "Kim Ingber 2012 gut chip"],
    corpus="academic",
    first_disclosure_date="2012",
    disclosure_citation="Kim, H. J.; Huh, D.; Hamilton, G.; Ingber, D. E. Human gut-on-a-chip inhabited by microbial flora that experiences intestinal peristalsis-like motions and flow. Lab Chip 2012, 12, 2165–2174. DOI: 10.1039/c2lc40074j",
    creator="Ingber group, Wyss Institute / Harvard",
    creator_country="US",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US9725687B2 (Wyss organ-chip family)"],
    prior_art_notes="Disclosed gut-on-chip: dual-channel PDMS architecture similar to lung-on-chip but with peristalsis-mimicking mechanical strain via vacuum-driven side channels, supporting Caco-2 villi formation and microbial co-culture. Anticipates: peristaltic-strain organ-chip architecture, microbial-mammalian co-culture on chip, and the gut-microbiome organ-chip subfield.",
    sources=[
        "Lab Chip 2012, 12, 2165–2174",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-organ-on-chip-vasculature",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["C12M 1/00", "B01L 3/00"],
    lineage_ancestors=["huh-2010-lung-on-chip"],
)

add(
    id="jang-suh-2013-kidney-on-chip",
    canonical_name="Kidney proximal tubule-on-chip",
    aliases=["kidney-on-chip", "Jang Suh 2013"],
    corpus="academic",
    first_disclosure_date="2013",
    disclosure_citation="Jang, K.-J.; Mehr, A. P.; Hamilton, G. A.; McPartlin, L. A.; Chung, S.; Suh, K.-Y.; Ingber, D. E. Human kidney proximal tubule-on-a-chip for drug transport and nephrotoxicity assessment. Integr. Biol. 2013, 5, 1119–1129. DOI: 10.1039/c3ib40049b",
    creator="Suh / Ingber labs (Wyss Institute)",
    creator_country="US",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed kidney proximal tubule-on-chip: dual-channel PDMS with porous membrane and unidirectional shear flow mimicking tubular fluid mechanics, used for nephrotoxicity drug screening. Anticipates: tubule-shear-stress organ-chip architecture, and the FDA-relevant nephrotoxicity drug-screening application that became part of the NIH MPS / FDA Modernization Act 2.0 framework.",
    sources=[
        "Integr. Biol. 2013, 5, 1119–1129",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-organ-on-chip-vasculature",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["C12M 1/00", "B01L 3/00"],
    lineage_ancestors=["huh-2010-lung-on-chip"],
)

add(
    id="booth-kim-2012-bbb-on-chip",
    canonical_name="Blood-brain barrier-on-chip",
    aliases=["BBB-on-chip", "Booth Kim 2012"],
    corpus="academic",
    first_disclosure_date="2012",
    disclosure_citation="Booth, R.; Kim, H. Characterization of a microfluidic in vitro model of the blood-brain barrier (µBBB). Lab Chip 2012, 12, 1784–1792. DOI: 10.1039/c2lc40094d",
    creator="Kim group, Vanderbilt",
    creator_country="US",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Disclosed in vitro blood-brain barrier on chip: porous-membrane-separated dual-channel device with brain endothelial cells on luminal side and astrocytes on abluminal side, with TEER (trans-endothelial electrical resistance) measurement. Anticipates: TEER-integrated BBB-on-chip architecture, dual-cell-type co-culture organ-chip with electrical readout, and the BBB drug-permeability screening application.",
    sources=[
        "Lab Chip 2012, 12, 1784–1792",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-organ-on-chip-vasculature",
        "detection-electrochemical-on-chip",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["C12M 1/00", "B01L 3/00"],
)

add(
    id="bhushan-2013-liver-on-chip",
    canonical_name="Liver hepatocyte sandwich-culture on chip",
    aliases=["liver-on-chip", "Bhushan 2013"],
    corpus="academic",
    first_disclosure_date="2013",
    disclosure_citation="Bhushan, A.; Senutovitch, N.; Bale, S. S.; McCarty, W. J.; Hegde, M.; Jindal, R.; Golberg, I.; Berk Usta, O.; Yarmush, M. L.; Vernetti, L.; Gough, A.; Bakan, A.; Shun, T. Y.; Biasio, R.; Taylor, D. L. Towards a three-dimensional microfluidic liver platform for predicting drug efficacy and toxicity in humans. Stem Cell Res. Ther. 2013, 4, S16. DOI: 10.1186/scrt377",
    creator="Yarmush, Taylor labs (MGH / Pittsburgh)",
    creator_country="US",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed 3D liver-on-chip: hepatocyte sandwich-culture in microfluidic perfusion device for hepatotoxicity drug screening. Architecturally an organ-chip variant emphasizing 3D tissue rather than dual-channel architecture. Anticipates: 3D-cultured-hepatocyte microfluidic platform, and the drug-induced-liver-injury (DILI) screening application that drove much of the early commercial organ-chip market.",
    sources=[
        "Stem Cell Res. Ther. 2013, 4, S16",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["C12M 1/00", "B01L 3/00"],
)

add(
    id="ronaghi-1996-pyrosequencing",
    canonical_name="Pyrosequencing (Ronaghi 1996)",
    aliases=["pyrosequencing", "454 sequencing precursor"],
    corpus="academic",
    first_disclosure_date="1996",
    disclosure_citation="Ronaghi, M.; Karamohamed, S.; Pettersson, B.; Uhlén, M.; Nyrén, P. Real-time DNA sequencing using detection of pyrophosphate release. Anal. Biochem. 1996, 242, 84–89. DOI: 10.1006/abio.1996.0432",
    creator="Nyrén, Ronaghi (Royal Institute of Technology / KTH)",
    creator_country="SE",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="patented",
    ip_citations=["EP0791058B1"],
    prior_art_notes="Disclosed pyrosequencing: real-time sequencing-by-synthesis using pyrophosphate-coupled luciferase chemiluminescence. Architectural ancestor of 454 Life Sciences (acquired by Roche) commercial sequencer, which used PicoTiterPlate microwell-array architecture. Indirect lineage to ion-torrent and other microwell-array-based NGS platforms.",
    sources=[
        "Anal. Biochem. 1996, 242, 84–89",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["C12Q 1/68"],
    lineage_descendants=["rothberg-2011-ion-torrent"],
)

add(
    id="margulies-2005-454-picotiterplate",
    canonical_name="454 Life Sciences PicoTiterPlate sequencing",
    aliases=["454 sequencing", "PicoTiterPlate", "Margulies 2005"],
    corpus="academic",
    first_disclosure_date="2005",
    disclosure_citation="Margulies, M. et al. Genome sequencing in microfabricated high-density picolitre reactors. Nature 2005, 437, 376–380. DOI: 10.1038/nature03959",
    creator="454 Life Sciences (acquired by Roche 2007)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="other",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US7264929B2 (and 454 family)"],
    prior_art_notes="Disclosed PicoTiterPlate: a fiber-optic faceplate etched into ~1.6M picoliter wells, each loaded with a single template-loaded bead for emulsion-PCR-amplified pyrosequencing. The first commercial massively parallel sequencing platform (2005); discontinued 2016. Architectural ancestor of every microwell-array-based NGS platform that followed (Ion Torrent, BGI, Singular Genomics).",
    sources=[
        "Nature 2005, 437, 376–380",
    ],
    disclosed_subsystems=[
        "fabrication-glass-thermal-bonding",
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["C12Q 1/68"],
    lineage_ancestors=["ronaghi-1996-pyrosequencing"],
    lineage_descendants=["rothberg-2011-ion-torrent"],
)

add(
    id="anna-mayer-2005-droplet-fluidics-review",
    canonical_name="Microfluidic emulsion droplets in research and applications",
    aliases=["Anna Mayer review"],
    corpus="academic",
    first_disclosure_date="2005",
    disclosure_citation="Anna, S. L. Droplets and bubbles in microfluidic devices. Annu. Rev. Fluid Mech. 2016, 48, 285–309. DOI: 10.1146/annurev-fluid-122414-034425",
    creator="Anna group, Carnegie Mellon",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Comprehensive review of droplet microfluidics from a fluid-mechanics-rooted perspective. Cited as the standard reference for theoretical foundations of droplet generation, breakup, coalescence, and emulsion stability. Methodological complement to Squires-Quake 2005 single-phase review.",
    sources=[
        "Annu. Rev. Fluid Mech. 2016, 48, 285–309",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="seemann-2012-droplet-review",
    canonical_name="Droplet-based microfluidics review (Seemann 2012)",
    aliases=["Seemann droplet review"],
    corpus="academic",
    first_disclosure_date="2012",
    disclosure_citation="Seemann, R.; Brinkmann, M.; Pfohl, T.; Herminghaus, S. Droplet based microfluidics. Rep. Prog. Phys. 2012, 75, 016601. DOI: 10.1088/0034-4885/75/1/016601",
    creator="Seemann group, MPI",
    creator_country="DE",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Long-form droplet microfluidics review with strong emphasis on physical chemistry and dynamics. Methodological reference for the theoretical underpinnings of T-junction, flow-focusing, and step-emulsification droplet generation. Cited as the standard reference for the physics of droplet manipulation.",
    sources=[
        "Rep. Prog. Phys. 2012, 75, 016601",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="dittrich-manz-2006-utas-review",
    canonical_name="Lab-on-a-chip: microfluidics in drug discovery",
    aliases=["Dittrich Manz 2006 drug discovery"],
    corpus="academic",
    first_disclosure_date="2006",
    disclosure_citation="Dittrich, P. S.; Manz, A. Lab-on-a-chip: microfluidics in drug discovery. Nat. Rev. Drug Discovery 2006, 5, 210–218. DOI: 10.1038/nrd1985",
    creator="Manz group, ISAS / Imperial College",
    creator_country="DE",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Manz-group framing review of microfluidics in pharmaceutical discovery applications, including HTS, ADME-Tox screening, single-cell pharmacology, and microreactor synthesis. Cited as the standard reference for pharmaceutical applications of µTAS and informs much of the patent landscape in pharmaceutical-discovery microfluidics.",
    sources=[
        "Nat. Rev. Drug Discovery 2006, 5, 210–218",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="ley-2013-flow-chemistry-pharma-review",
    canonical_name="Continuous flow chemistry review (Ley 2013)",
    aliases=["Ley flow chemistry review"],
    corpus="academic",
    first_disclosure_date="2013",
    disclosure_citation="Ley, S. V.; Fitzpatrick, D. E.; Ingham, R. J.; Myers, R. M. Organic synthesis: march of the machines. Angew. Chem. Int. Ed. 2015, 54, 3449–3464. DOI: 10.1002/anie.201410744",
    creator="Ley group, Cambridge",
    creator_country="GB",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Ley-group review of automation and continuous flow chemistry in organic synthesis. The canonical reference for the integration of continuous-flow microfluidic reactors with automated reagent dispensing, real-time analytics, and machine learning for process optimization. Companion to Reizman 2015 self-optimizing flow chemistry.",
    sources=[
        "Angew. Chem. Int. Ed. 2015, 54, 3449–3464",
    ],
    disclosed_subsystems=[
        "architecture-process-analytical-technology",
    ],
    cpc_classifications=["B01J 19/00"],
)

add(
    id="kapur-2013-cellsearch-ctc-system",
    canonical_name="CellSearch CTC isolation system",
    aliases=["CellSearch", "Veridex CellSearch"],
    corpus="academic",
    first_disclosure_date="2003",
    disclosure_citation="Allard, W. J. et al. Tumor cells circulate in the peripheral blood of all major carcinomas but not in healthy subjects or patients with nonmalignant diseases. Clin. Cancer Res. 2004, 10, 6897–6904. DOI: 10.1158/1078-0432.CCR-04-0378",
    creator="Veridex / Immunicon (now Menarini Silicon Biosystems)",
    creator_country="US",
    device_class="separator-component",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US6790366B2 (and Immunicon family)"],
    prior_art_notes="The first FDA-cleared CTC isolation platform (2004): immunomagnetic capture using EpCAM-coated ferrofluid in a magnetic-field-array carousel. Architecturally not strictly microfluidic, but established the clinical-CTC-isolation product category and is the comparator for every subsequent microfluidic CTC platform (CTC-iChip, Vortex, ApoStream).",
    sources=[
        "Clin. Cancer Res. 2004, 10, 6897–6904",
    ],
    disclosed_subsystems=[
        "separation-magnetophoresis",
        "separation-affinity-capture",
    ],
    cpc_classifications=["G01N 33/49", "B01L 3/00"],
)


# =====================================================================
# PRIVATE — more cartridges and patent thicket holders
# =====================================================================

add(
    id="sysmex-cbc-cartridge",
    canonical_name="Sysmex hematology analyzer flow cell",
    aliases=["Sysmex XN-series", "Sysmex CBC analyzer"],
    corpus="private",
    first_disclosure_date="1968",
    disclosure_citation="Sysmex Corporation hematology analyzer family (XN-1000, XN-2000, etc.). https://www.sysmex.com",
    creator="Sysmex Corporation (Kobe, Japan)",
    creator_country="JP",
    device_class="lab-on-chip",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Microfluidic flow-cell architecture for clinical hematology counting (CBC differential): Coulter-impedance counting + flow cytometry + reagent mixing on integrated cartridge. Sysmex is the dominant global hematology analyzer vendor with a long history of flow-cell innovation predating the µTAS era. The flow-cell architectures used in modern Sysmex XN-series instruments are direct descendants of 1970s-era Coulter Counter and Technicon SMA designs but at substantially smaller scale.",
    sources=[
        "Sysmex product literature",
    ],
    disclosed_subsystems=[
        "detection-fluorescence-on-chip",
        "detection-electrochemical-on-chip",
    ],
    cpc_classifications=["G01N 15/12", "G01N 15/14"],
)

add(
    id="roche-cobas-c-cartridge",
    canonical_name="Roche cobas c clinical chemistry analyzer cartridge",
    aliases=["cobas c", "Roche cobas chemistry"],
    corpus="private",
    first_disclosure_date="2007",
    disclosure_citation="Roche Diagnostics cobas c platform (c 311, c 501, c 6000, c 8000). https://diagnostics.roche.com",
    creator="Roche Diagnostics (Mannheim)",
    creator_country="DE",
    device_class="lab-on-chip",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Reagent-cartridge format for high-volume clinical chemistry (200+ assays / hour). Each reagent cartridge integrates microfluidic delivery channels for reagent metering. Architecturally a high-volume implementation of microfluidic reagent dispensing in central lab automation context. Reference for the broader 'central-lab-automation' microfluidic patent thicket distinct from POC cartridges.",
    sources=[
        "Roche Diagnostics product literature",
    ],
    disclosed_subsystems=[
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["G01N 35/00", "B01L 3/00"],
)

add(
    id="beckman-coulter-au-flow-cell",
    canonical_name="Beckman Coulter AU/DxC clinical chemistry analyzer",
    aliases=["Beckman AU", "DxC"],
    corpus="private",
    first_disclosure_date="2003",
    disclosure_citation="Beckman Coulter AU/DxC analyzer family. https://www.beckmancoulter.com",
    creator="Beckman Coulter (Danaher)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Major central-lab clinical chemistry analyzer platform. Cousin of Roche cobas c series in product positioning. The Beckman Coulter portfolio (acquired by Danaher 2011) includes diverse microfluidic-equivalent analytical cartridges from the 1990s onward — the cumulative patent estate is among the largest in the central-lab clinical chemistry space.",
    sources=[
        "Beckman Coulter product literature",
    ],
    disclosed_subsystems=[
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["G01N 35/00", "B01L 3/00"],
)

add(
    id="hitachi-7080-clinical-chemistry",
    canonical_name="Hitachi 7080/7180/7600 clinical chemistry analyzer",
    aliases=["Hitachi 7080", "Hitachi clinical chemistry"],
    corpus="private",
    first_disclosure_date="1995",
    disclosure_citation="Hitachi High-Tech Corporation clinical chemistry analyzers (7080/7180/7600). https://www.hitachi-hightech.com",
    creator="Hitachi High-Tech Corporation",
    creator_country="JP",
    device_class="lab-on-chip",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Long-running Japanese central-lab clinical chemistry analyzer platform. Hitachi's cumulative patent estate in this space is among the most under-cited in US prior art databases due to language and indexing barriers. The 1990s-era Hitachi 7000-series analyzer designs include reagent-handling and flow-cell architectures that pre-date most US disclosures.",
    sources=[
        "Hitachi High-Tech product literature",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["G01N 35/00", "B01L 3/00"],
)

add(
    id="abbott-architect-i2000",
    canonical_name="Abbott ARCHITECT i2000/i2000SR immunoassay analyzer cartridge",
    aliases=["Abbott ARCHITECT", "i2000"],
    corpus="private",
    first_disclosure_date="2003",
    disclosure_citation="Abbott Laboratories ARCHITECT immunoassay family. https://www.abbottdiagnostics.com",
    creator="Abbott Laboratories",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Major central-lab immunoassay platform with reagent-cartridge format and integrated chemiluminescent magnetic microparticle (CMIA) detection. The reagent cartridges include microfluidic-equivalent delivery and metering channels. Among the largest patent estates in central-lab immunoassay automation.",
    sources=[
        "Abbott Diagnostics product literature",
    ],
    disclosed_subsystems=[
        "fabrication-thermoplastic-injection-molding",
        "separation-magnetophoresis",
    ],
    cpc_classifications=["G01N 33/543", "B01L 3/00"],
)

add(
    id="dexcom-g7-cgm",
    canonical_name="Dexcom G7 continuous glucose monitor sensor",
    aliases=["Dexcom G7", "Dexcom CGM"],
    corpus="private",
    first_disclosure_date="2022",
    disclosure_citation="Dexcom G7 Continuous Glucose Monitoring System. https://www.dexcom.com",
    creator="Dexcom Inc.",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Skin-mounted continuous glucose monitor with subcutaneous enzymatic glucose sensor wire and integrated wireless transmitter. Architecturally a wearable microfluidic-equivalent biosensor: the sensor wire performs enzymatic glucose oxidation at sub-mm scale with electrochemical detection. The Dexcom and Abbott Libre CGM cartridges are the highest-volume wearable biosensors deployed globally (~10s of millions of units annually).",
    sources=[
        "Dexcom G7 product literature",
        "FDA approval documents",
    ],
    disclosed_subsystems=[
        "detection-electrochemical-on-chip",
    ],
    cpc_classifications=["A61B 5/145"],
    lineage_ancestors=["abbott-freestyle-libre"],
)

add(
    id="fluidigm-helios-mass-cytometry",
    canonical_name="Fluidigm Helios mass cytometer (CyTOF re-registration with extended scope)",
    aliases=["Helios mass cytometer"],
    corpus="private",
    first_disclosure_date="2015",
    disclosure_citation="Fluidigm Corporation Helios mass cytometer (now Standard BioTools). https://www.standardbio.com",
    creator="Fluidigm / Standard BioTools",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Companion entry to standard-biotools-mass-cytometry-cytof; Helios is the second-generation commercial CyTOF platform with improved acquisition rates. Architecturally microfluidic flow-cell + ICP-TOF-MS hybrid system supporting 40+ parameter single-cell measurements without optical-spectrum overlap concerns.",
    sources=[
        "Standard BioTools / Fluidigm product literature",
    ],
    disclosed_subsystems=[
        "interface-electrospray-emitter",
    ],
    cpc_classifications=["G01N 33/49", "H01J 49/04"],
    lineage_ancestors=["standard-biotools-mass-cytometry-cytof"],
)

add(
    id="biorad-nanocoulter-bead-counter",
    canonical_name="Bio-Rad TC20 / TC10 automated cell counter",
    aliases=["Bio-Rad TC20", "Bio-Rad cell counter"],
    corpus="private",
    first_disclosure_date="2010",
    disclosure_citation="Bio-Rad Laboratories TC20/TC10 Automated Cell Counter. https://www.bio-rad.com",
    creator="Bio-Rad Laboratories",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="passive",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Cell-counting cartridge format: a slide-format disposable with 10 µL sample chamber that the instrument images and counts via brightfield image analysis. Architecturally a low-cost alternative to flow cytometric cell counting for routine cell culture work. Reference for the broader 'cell-counting cartridge' product category that competes with hemocytometers.",
    sources=[
        "Bio-Rad TC20 product literature",
    ],
    disclosed_subsystems=[
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "G01N 15/14"],
)


# =====================================================================
# OPEN
# =====================================================================

add(
    id="public-lab-spectrometer",
    canonical_name="Public Lab DIY spectrometer",
    aliases=["Public Lab spectrometer", "PublicLab Foldable Mini-Spectrometer"],
    corpus="open",
    first_disclosure_date="2010",
    disclosure_citation="Public Lab community DIY spectrometer wiki. https://publiclab.org/wiki/spectrometer",
    creator="Public Lab community",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Long-running open-hardware spectrometer project including paper, foldable, and 3D-printed designs at sub-$50 BOM. Education-oriented; widely used in citizen-science environmental monitoring. Reference for the open-hardware optical-spectroscopy ecosystem complementing commercial mini-spectrometer modules.",
    sources=[
        "Public Lab spectrometer wiki",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["G01J 3/02"],
)

add(
    id="backyard-brains-spikerbox",
    canonical_name="Backyard Brains SpikerBox open neuroscience hardware",
    aliases=["SpikerBox", "Backyard Brains"],
    corpus="open",
    first_disclosure_date="2011",
    disclosure_citation="Backyard Brains SpikerBox electrophysiology kit. https://backyardbrains.com",
    creator="Backyard Brains",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Open-source neuroscience and electrophysiology hardware with extensive education focus. The SpikerBox amplifier is microfluidic-relevant by analogy: similar architectural pattern of low-cost open hardware bringing professional research equipment into education, hobbyist, and DIY-bio settings. Reference data point for the broader open-hardware-in-life-sciences movement.",
    sources=[
        "Backyard Brains catalog",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="open-source-toolkit-for-microfluidics",
    canonical_name="Open-source toolkits for microfluidics design and simulation",
    aliases=["microfluidic CAD toolkits", "DAFD"],
    corpus="open",
    first_disclosure_date="2018",
    disclosure_citation="Various — DAFD (Design Automation of Fluid Dynamics), 3DµF, ParchMint. See e.g. Lashkaripour et al. 2021 Nat. Commun. 12, 25.",
    creator="Various — Densmore lab BU, MIT 3DµF, others",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Open-source design-automation tools for microfluidic chips including DAFD (parametric flow-focusing droplet generator design), 3DµF (parametric microfluidic CAD library), and ParchMint (microfluidic netlist standard for chip design exchange). Reference for the broader 'EDA-for-microfluidics' movement that aims to bring electronic-design-automation principles to microfluidic chip design.",
    sources=[
        "Lashkaripour, A. et al. Machine learning enables design automation of microfluidic flow-focusing droplet generation. Nat. Commun. 2021, 12, 25",
        "https://github.com/CIDARLAB/3DuF",
        "https://github.com/Cidarlab/ParchMint",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="bento-bio-engineer",
    canonical_name="Bento Bioworks Bento Lab portable PCR + electrophoresis",
    aliases=["Bento Lab"],
    corpus="open",
    first_disclosure_date="2016",
    disclosure_citation="Bento Bioworks Bento Lab. https://www.bento.bio",
    creator="Bento Bioworks Ltd.",
    creator_country="GB",
    device_class="point-of-care-cartridge",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Portable laboratory in a briefcase combining centrifuge, PCR thermal cycler, and gel electrophoresis with open-source documentation. Sub-$2k consumer price point. Reference for the broader 'lab-in-a-box' movement bringing molecular biology infrastructure to citizen scientists, classrooms, and field-deployed contexts.",
    sources=[
        "Bento Bioworks product literature",
    ],
    disclosed_subsystems=[
        "thermal-pcr-cycling",
    ],
    cpc_classifications=["B01L 7/00", "G01N 27/447"],
)


# =====================================================================
# FICTIONAL
# =====================================================================

add(
    id="star-trek-replicator",
    canonical_name="Star Trek molecular replicator",
    aliases=["replicator", "Federation replicator"],
    corpus="fictional",
    first_disclosure_date="1987",
    disclosure_citation="Star Trek: The Next Generation, 'Encounter at Farpoint' (1987) and subsequent franchise.",
    creator="Paramount / Roddenberry estate",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="bioprocess",
    ip_status="fictional",
    prior_art_notes="Iconic narrative depiction of a synthesis device producing arbitrary molecular and macroscale objects from energy + raw materials. Microfluidic-relevant in the limit case: at high enough automation and integration, microfluidic-equivalent on-demand synthesis approaches replicator-like functionality. Cited as conceptual prior art for 'on-demand bedside pharmaceutical synthesis' platforms (Adamo 2016 and successors).",
    sources=[
        "Star Trek: The Next Generation (1987–1994) and subsequent franchise",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="bsg-medbay-cylons",
    canonical_name="Battlestar Galactica medbay (Galactica + Cylon variants)",
    aliases=["BSG medbay", "Caprica medical"],
    corpus="fictional",
    first_disclosure_date="2003",
    disclosure_citation="Battlestar Galactica (re-imagined series), Sci Fi Channel / Universal, 2003–2009.",
    creator="Ronald D. Moore / Universal Television",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Series-spanning depictions of military-grade medbay automation including diagnostic, surgical, and Cylon-detection biological-analysis equipment. The 'Cylon detection test' subplot involves what is depicted as a cell-level biological assay — architecturally microfluidic-equivalent. Cumulative depictions add to fictional-prior-art landscape for autonomous bedside diagnostic systems.",
    sources=[
        "Battlestar Galactica (2003–2009)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="expanse-protomolecule-vat",
    canonical_name="The Expanse protomolecule containment / analysis vat",
    aliases=["Expanse protomolecule", "Phoebe lab"],
    corpus="fictional",
    first_disclosure_date="2015",
    disclosure_citation="The Expanse (TV series), Syfy / Amazon Prime Video, 2015–2022. Source novels Corey 2011–.",
    creator="Daniel Abraham / Ty Franck (James S.A. Corey) / Alcon TV",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="research",
    ip_status="fictional",
    prior_art_notes="Detailed visual and narrative depictions of high-containment microbiological / synthetic-biology research facilities including microfluidic-equivalent infrastructure. The Phoebe and Eros station sequences include observation of biological systems at sub-mm scale through what are depicted as microscopy + microfluidic chambers. Reference data point for hard-SF depictions of microfluidic biology.",
    sources=[
        "The Expanse (2015–2022)",
        "Corey, J. S. A. Leviathan Wakes (2011) and subsequent novels",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="alita-battle-angel-cyborg-medbay",
    canonical_name="Alita Battle Angel cyborg-body diagnostic and assembly",
    aliases=["Alita medical", "Iron City Doc Ido clinic"],
    corpus="fictional",
    first_disclosure_date="2019",
    disclosure_citation="Alita: Battle Angel (2019), 20th Century Fox; based on Yukito Kishiro's Gunnm manga (1990–1995).",
    creator="James Cameron / Robert Rodriguez / Yukito Kishiro source",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Detailed visual depictions of cyborg-body diagnostic and assembly equipment including microfluidic-equivalent synthetic-blood and tissue-fluid handling systems. Architectural specificity comparable to Westworld host fabrication and Cyberpunk 2077 ripperdoc settings. Cumulative fictional prior art for cyborg-body fluid-systems depictions.",
    sources=[
        "Alita: Battle Angel (2019)",
        "Kishiro, Y. Gunnm (1990–1995)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# Write out
with CORPUS.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new entries to {CORPUS}")
