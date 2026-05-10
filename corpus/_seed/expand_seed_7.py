#!/usr/bin/env python3
"""Seventh expansion: mass-spec-on-chip, more international cartridges, more academic."""
import json
from pathlib import Path

CORPUS = Path(__file__).parent / "corpus.jsonl"
ENTRIES = []


def add(**kw):
    kw.setdefault("schema_version", 2)
    kw.setdefault("last_updated", "2026-05-09")
    ENTRIES.append(kw)


# =====================================================================
# Mass spec-on-chip
# =====================================================================

add(
    id="figeys-1997-microfabricated-esi",
    canonical_name="Microfabricated ESI emitter (Figeys 1997)",
    aliases=["Figeys 1997 µESI"],
    corpus="academic",
    first_disclosure_date="1997",
    disclosure_citation="Figeys, D.; Aebersold, R. Nanoflow solvent gradient delivery from a microfabricated device for protein identifications by electrospray ionization mass spectrometry. Anal. Chem. 1998, 70, 3721–3727. DOI: 10.1021/ac980312w",
    creator="Aebersold group, University of Washington",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="analytical",
    ip_status="patented",
    prior_art_notes="Disclosed silicon-microfabricated nanoflow ESI emitter for nano-LC-MS protein identification. Architectural complement to Ramsey 1996 chip-ESI from a different research lineage. Anticipates: silicon-MEMS ESI emitter integrated with nano-LC for proteomics applications, the architectural family that became the Advion NanoMate, Agilent HPLC-Chip, and Waters Xevo G2-XS chip-coupling platforms.",
    sources=[
        "Anal. Chem. 1998, 70, 3721–3727",
    ],
    disclosed_subsystems=[
        "interface-electrospray-emitter",
        "fabrication-silicon-drie",
    ],
    cpc_classifications=["B01L 3/00", "H01J 49/04"],
    lineage_descendants=["advion-triversa-nanomate"],
)

add(
    id="agilent-hplc-chip",
    canonical_name="Agilent HPLC-Chip / MS Chip Cube",
    aliases=["HPLC-Chip", "Agilent Chip Cube"],
    corpus="private",
    first_disclosure_date="2005",
    disclosure_citation="Agilent Technologies HPLC-Chip / MS system. https://www.agilent.com",
    creator="Agilent Technologies",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="analytical",
    ip_status="patented",
    prior_art_notes="Polyimide-substrate microfluidic HPLC-MS chip integrating sample enrichment column, analytical separation column, and ESI nozzle on a single disposable chip. Direct architectural descendant of Ramsey 1996 / Figeys 1997 academic disclosures. Among the earliest commercial chip-LC-MS platforms; subsequently displaced for many applications by capillary nano-LC but retains use in dedicated chip-LC workflows.",
    sources=[
        "Agilent Technologies product literature",
    ],
    disclosed_subsystems=[
        "interface-electrospray-emitter",
        "separation-affinity-capture",
    ],
    cpc_classifications=["B01L 3/00", "H01J 49/04"],
    lineage_ancestors=["ramsey-1996-electrospray-on-chip", "figeys-1997-microfabricated-esi"],
)

add(
    id="waters-iongenius-chip",
    canonical_name="Waters ionKey/MS chip",
    aliases=["ionKey", "ionKey/MS"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="Waters Corporation ionKey/MS system. https://www.waters.com",
    creator="Waters Corporation",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="analytical",
    ip_status="patented",
    prior_art_notes="Ceramic-substrate microfluidic LC-MS chip with integrated separation column and ESI emitter. Architectural cousin of Agilent HPLC-Chip with different substrate (ceramic vs polyimide) and different vendor positioning. Reference for the broader chip-LC-MS commercial ecosystem.",
    sources=[
        "Waters Corporation product literature",
    ],
    disclosed_subsystems=[
        "interface-electrospray-emitter",
        "separation-affinity-capture",
    ],
    cpc_classifications=["B01L 3/00", "H01J 49/04"],
    lineage_ancestors=["agilent-hplc-chip"],
)


# =====================================================================
# More international cartridges
# =====================================================================

add(
    id="autobio-rapid-test",
    canonical_name="Autobio Diagnostics rapid test cartridge family",
    aliases=["Autobio rapid test"],
    corpus="private",
    first_disclosure_date="2010",
    disclosure_citation="Autobio Diagnostics Co. https://www.autobio.com.cn",
    creator="Autobio Diagnostics",
    creator_country="CN",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Major Chinese rapid-test manufacturer with broad cartridge portfolio across infectious disease, drugs of abuse, and pregnancy testing. Significant global market presence in low- and middle-income countries. Reference for the Chinese rapid-test patent landscape that under-indexes in US prior-art databases.",
    sources=[
        "Autobio Diagnostics product literature",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
    ],
    cpc_classifications=["G01N 33/543"],
)

add(
    id="lifescan-glucose-test-strip",
    canonical_name="LifeScan / OneTouch glucose test strip",
    aliases=["OneTouch test strip", "LifeScan strip"],
    corpus="private",
    first_disclosure_date="1981",
    disclosure_citation="LifeScan Inc. (Johnson & Johnson) OneTouch product family. Original 1981 disclosure by Newman.",
    creator="LifeScan Inc. (Johnson & Johnson)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US4929545A (and Newman / LifeScan family)"],
    prior_art_notes="Foundational disposable glucose test strip with capillary-fill sample chamber, glucose oxidase enzyme layer, and electrochemical detection electrodes. The highest-cumulative-volume microfluidic-equivalent product in history (>10B units shipped since 1980s). Architectural ancestor of every modern blood-glucose test strip and many other electrochemical-detection POC strips.",
    sources=[
        "Newman et al. US4929545A",
        "LifeScan OneTouch product history",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
        "detection-electrochemical-on-chip",
    ],
    cpc_classifications=["G01N 33/487"],
)

add(
    id="abaxis-vetscan-vs2",
    canonical_name="Abaxis VetScan VS2 veterinary clinical chemistry analyzer",
    aliases=["VetScan VS2", "Abaxis veterinary"],
    corpus="private",
    first_disclosure_date="1995",
    disclosure_citation="Abaxis (acquired by Zoetis 2018) VetScan VS2 system; same disc-format as Piccolo Xpress for veterinary use.",
    creator="Abaxis (Zoetis)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="centrifugal",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Veterinary-market sibling product of the Piccolo Xpress: same centrifugal microfluidic disc architecture but with veterinary chemistry panels. Reference for the broader veterinary diagnostic cartridge market, which under-indexes in human-medicine prior-art reviews despite using the same architectural primitives.",
    sources=[
        "Abaxis VetScan product literature",
    ],
    disclosed_subsystems=[
        "pump-centrifugal-rotational",
        "valve-capillary-stop",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "G01N 35/00"],
    lineage_ancestors=["abbott-piccolo-xpress"],
)


# =====================================================================
# More foundational academic
# =====================================================================

add(
    id="nelson-polymerase-chain-reaction-1985",
    canonical_name="PCR (Mullis 1985)",
    aliases=["Mullis PCR", "polymerase chain reaction"],
    corpus="academic",
    first_disclosure_date="1985",
    disclosure_citation="Saiki, R. K.; Scharf, S.; Faloona, F.; Mullis, K. B.; Horn, G. T.; Erlich, H. A.; Arnheim, N. Enzymatic amplification of beta-globin genomic sequences and restriction site analysis for diagnosis of sickle cell anemia. Science 1985, 230, 1350–1354. DOI: 10.1126/science.2999980",
    creator="Mullis, Saiki et al. (Cetus Corporation)",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US4683202A (Mullis), US4683195A (Mullis et al.)"],
    prior_art_notes="The foundational disclosure of polymerase chain reaction (PCR). Not microfluidic itself, but the entire molecular-diagnostic-cartridge category exists because PCR enables exponential amplification of nucleic acids — without PCR, none of the BioFire / Cepheid / Lucira / Visby Medical / Cue Health cartridges would be possible. The Mullis patents have expired but the architectural pattern of 'cartridge-format PCR' depends on this foundational disclosure. Doctrinally critical for any prior-art chain leading to a molecular-diagnostic cartridge claim.",
    sources=[
        "Science 1985, 230, 1350–1354",
        "US4683202A (Mullis 1987 issue)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["C12Q 1/68"],
    notes="Not microfluidic itself; included because every cartridge molecular-diagnostic claim requires PCR and the corpus would be incomplete without the foundational reference.",
)

add(
    id="wittwer-1997-rapid-cycler",
    canonical_name="LightCycler real-time rapid PCR (Wittwer 1997)",
    aliases=["LightCycler", "Wittwer real-time PCR"],
    corpus="academic",
    first_disclosure_date="1997",
    disclosure_citation="Wittwer, C. T.; Herrmann, M. G.; Moss, A. A.; Rasmussen, R. P. Continuous fluorescence monitoring of rapid cycle DNA amplification. BioTechniques 1997, 22, 130–138. DOI: 10.2144/97221bi01",
    creator="Wittwer group, University of Utah / Idaho Technology / Roche",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US6174670B1 (Wittwer real-time PCR family)"],
    prior_art_notes="Disclosed rapid-cycle real-time PCR with continuous fluorescence monitoring during thermal cycling, in glass capillary tubes for fast heat transfer. Architectural ancestor of every real-time PCR cartridge: the framing that PCR + real-time fluorescence reading enables quantitative analysis from a single closed reaction. The Wittwer-Idaho-Technology lineage produced the LightCycler (acquired by Roche 1997) and via the BioFire spinout (2003) the FilmArray cartridge. One of the most consequential academic-to-commercial transitions in molecular diagnostics.",
    sources=[
        "BioTechniques 1997, 22, 130–138",
        "US6174670B1",
    ],
    disclosed_subsystems=[
        "thermal-pcr-cycling",
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["C12Q 1/686"],
    lineage_descendants=["biofire-filmarray-multiplex-pcr-cartridge"],
)

add(
    id="zhang-jin-2011-cas9-discovery",
    canonical_name="CRISPR-Cas9 mechanism (Jinek 2012; Cong/Mali 2013) — context for CRISPR diagnostics",
    aliases=["CRISPR-Cas9 foundational"],
    corpus="academic",
    first_disclosure_date="2012",
    disclosure_citation="Jinek, M.; Chylinski, K.; Fonfara, I.; Hauer, M.; Doudna, J. A.; Charpentier, E. A programmable dual-RNA-guided DNA endonuclease in adaptive bacterial immunity. Science 2012, 337, 816–821. DOI: 10.1126/science.1225829",
    creator="Doudna, Charpentier (UC Berkeley / Vienna)",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="patented",
    ip_citations=["US10266850B2 (Doudna/Charpentier family)", "US8697359B1 (Zhang/Broad family)"],
    prior_art_notes="Foundational disclosure of CRISPR-Cas9 as a programmable nuclease. Not microfluidic itself, but enables an entire generation of diagnostic platforms based on CRISPR detection (Cas12a/Cas13 cartridges from Mammoth Biosciences, Sherlock Biosciences, etc.). Doctrinally critical for any CRISPR-diagnostic cartridge prior-art chain.",
    sources=[
        "Science 2012, 337, 816–821",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["C12N 9/22"],
    notes="Not microfluidic itself; included because CRISPR-diagnostic cartridges (Mammoth DETECTR, Sherlock SHERLOCK) are an emerging cartridge category that requires this foundational reference.",
)

add(
    id="gootenberg-zhang-2017-sherlock",
    canonical_name="SHERLOCK CRISPR-Cas13 nucleic acid detection",
    aliases=["SHERLOCK", "Cas13 detection"],
    corpus="academic",
    first_disclosure_date="2017",
    disclosure_citation="Gootenberg, J. S. et al. Nucleic acid detection with CRISPR-Cas13a/C2c2. Science 2017, 356, 438–442. DOI: 10.1126/science.aam9321",
    creator="Zhang group, Broad Institute / Sherlock Biosciences",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US10266887B2 (Sherlock family)"],
    prior_art_notes="Disclosed SHERLOCK: CRISPR-Cas13a-based nucleic acid detection at attomolar sensitivity by combining isothermal amplification with collateral-cleavage-activated reporter. Anticipates: CRISPR-cleavage-as-detection on cartridge format, and the Sherlock Biosciences commercial diagnostic platform. Architectural cousin of Mammoth's DETECTR (Cas12a) approach.",
    sources=[
        "Science 2017, 356, 438–442",
    ],
    disclosed_subsystems=[
        "thermal-isothermal-amplification",
    ],
    cpc_classifications=["C12Q 1/68"],
    lineage_ancestors=["zhang-jin-2011-cas9-discovery", "notomi-2000-loop-mediated-isothermal"],
)

add(
    id="chen-doudna-2018-detectr",
    canonical_name="DETECTR CRISPR-Cas12a nucleic acid detection",
    aliases=["DETECTR", "Cas12a detection"],
    corpus="academic",
    first_disclosure_date="2018",
    disclosure_citation="Chen, J. S.; Ma, E.; Harrington, L. B.; Da Costa, M.; Tian, X.; Palefsky, J. M.; Doudna, J. A. CRISPR-Cas12a target binding unleashes indiscriminate single-stranded DNase activity. Science 2018, 360, 436–439. DOI: 10.1126/science.aar6245",
    creator="Doudna group, UC Berkeley / Mammoth Biosciences",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US11236391B2 (Mammoth family)"],
    prior_art_notes="Disclosed DETECTR: CRISPR-Cas12a-based nucleic acid detection via collateral cleavage of single-stranded DNA reporter. Architectural cousin of SHERLOCK (Cas13 vs Cas12 enzyme). Anticipates: Mammoth Biosciences commercial diagnostic platform; foundational for CRISPR-cartridge IP positions distinct from Sherlock Biosciences.",
    sources=[
        "Science 2018, 360, 436–439",
    ],
    disclosed_subsystems=[
        "thermal-isothermal-amplification",
    ],
    cpc_classifications=["C12Q 1/68"],
    lineage_ancestors=["zhang-jin-2011-cas9-discovery"],
)


# =====================================================================
# More open hardware / microfluidic-design tools
# =====================================================================

add(
    id="microfluidic-cad-software-clewinwin-cleWin",
    canonical_name="CleWin / KLayout microfluidic mask layout tools",
    aliases=["CleWin", "KLayout for microfluidics"],
    corpus="open",
    first_disclosure_date="2003",
    disclosure_citation="WieWeb CleWin layout editor and KLayout open-source GDS layout editor. https://klayout.de",
    creator="WieWeb / KLayout community",
    creator_country="OTHER",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Mask-layout editors widely used for microfluidic chip design. KLayout in particular is open-source and widely adopted in academic microfluidics for GDS-format mask design. Reference for the open-source EDA-for-microfluidics tooling ecosystem; companion to ParchMint / 3DµF / DAFD entries.",
    sources=[
        "https://klayout.de",
        "WieWeb CleWin product literature",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="open-flexure-microfluidics-fork",
    canonical_name="OpenFlexure microfluidics-friendly XYZ stage variant",
    aliases=["OpenFlexure µFluidic"],
    corpus="open",
    first_disclosure_date="2020",
    disclosure_citation="OpenFlexure Microscope project — community variants for chip-imaging. https://openflexure.org",
    creator="OpenFlexure community",
    creator_country="GB",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="OpenFlexure community-contributed variants specifically targeting microfluidic chip imaging applications: chip-mount adapters, integrated tubing routing, and incubator-compatible variants. Reference for community-driven adaptation of open-hardware microscope platforms to microfluidic-specific needs.",
    sources=[
        "https://openflexure.org",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
    lineage_ancestors=["openflexure-microscope"],
)


# =====================================================================
# More fictional
# =====================================================================

add(
    id="rick-and-morty-portal-fluid",
    canonical_name="Rick and Morty portal fluid synthesis",
    aliases=["Rick and Morty portal fluid"],
    corpus="fictional",
    first_disclosure_date="2013",
    disclosure_citation="Rick and Morty (Adult Swim, 2013–).",
    creator="Justin Roiland / Dan Harmon / Adult Swim",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="research",
    ip_status="fictional",
    prior_art_notes="Recurring depictions of garage-scale chemistry and biological synthesis, including microfluidic-equivalent fluid handling for synthesis of arbitrary chemicals. The architectural commitment is to a 'mad-scientist personal laboratory' aesthetic that includes recognizable microfluidic-equivalent components. Cumulative cultural reference data point.",
    sources=[
        "Rick and Morty (2013–)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="black-mirror-blockchain-implant",
    canonical_name="Black Mirror neural-fluid implant depictions",
    aliases=["Black Mirror neural fluid"],
    corpus="fictional",
    first_disclosure_date="2016",
    disclosure_citation="Black Mirror (Channel 4 / Netflix, 2011–). Various episodes depicting neural-fluid implants.",
    creator="Charlie Brooker / House of Tomorrow / Netflix",
    creator_country="GB",
    device_class="fictional-laboratory",
    end_application="other",
    ip_status="fictional",
    prior_art_notes="Multiple episodes depict implantable neural fluid handling, blood / cerebrospinal-fluid sampling, and synthetic-life-support systems. Architectural specificity is sufficient to count as conceptual prior art for various wearable / implantable microfluidic devices. Distinct from the Profusa / Dexcom-class continuous biosensor lineage by emphasizing more invasive applications.",
    sources=[
        "Black Mirror episodes (selected)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# =====================================================================
# More academic — newer single-cell / spatial methods
# =====================================================================

add(
    id="rodriques-2019-slide-seq",
    canonical_name="Slide-seq spatial transcriptomics on bead arrays",
    aliases=["Slide-seq", "Rodriques 2019"],
    corpus="academic",
    first_disclosure_date="2019",
    disclosure_citation="Rodriques, S. G. et al. Slide-seq: a scalable technology for measuring genome-wide expression at high spatial resolution. Science 2019, 363, 1463–1467. DOI: 10.1126/science.aaw1219",
    creator="Macosko lab, Broad Institute",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed Slide-seq: 10 µm-resolution spatial transcriptomics by transferring tissue sections onto rubber-pucks coated with barcoded oligo beads with known spatial coordinates. Architectural alternative to 10x Visium (which uses lithographically-patterned spots). Anticipates: random-bead-array spatial transcriptomics, sub-cellular-resolution spatial-omics on chip-format substrates.",
    sources=[
        "Science 2019, 363, 1463–1467",
    ],
    disclosed_subsystems=[
        "architecture-spatial-barcoded-array",
    ],
    cpc_classifications=["C12Q 1/6841"],
    lineage_ancestors=["staahl-2016-spatial-transcriptomics"],
)

add(
    id="liu-fan-2020-dbit-seq",
    canonical_name="DBiT-seq spatial multi-omics on chip",
    aliases=["DBiT-seq"],
    corpus="academic",
    first_disclosure_date="2020",
    disclosure_citation="Liu, Y. et al. High-spatial-resolution multi-omics sequencing via deterministic barcoding in tissue. Cell 2020, 183, 1665–1681.e18. DOI: 10.1016/j.cell.2020.10.026",
    creator="R. Fan group, Yale",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed DBiT-seq: deterministic-barcoding-in-tissue using two orthogonal sets of barcoded reagent flows through PDMS microfluidic channels pressed onto tissue, defining a 50 × 50 grid of 50 µm × 50 µm spatial barcodes. Anticipates: PDMS-microchannel-defined spatial barcoding architecture as alternative to spotted-array (Visium) and random-bead (Slide-seq) approaches.",
    sources=[
        "Cell 2020, 183, 1665–1681.e18",
    ],
    disclosed_subsystems=[
        "architecture-spatial-barcoded-array",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["C12Q 1/6841"],
    lineage_ancestors=["staahl-2016-spatial-transcriptomics"],
)

add(
    id="berkeley-cellium-flow-cytometer-2009",
    canonical_name="Microfluidic flow cytometer architectures (academic)",
    aliases=["chip flow cytometer"],
    corpus="academic",
    first_disclosure_date="2002",
    disclosure_citation="Fu, A. Y.; Spence, C.; Scherer, A.; Arnold, F. H.; Quake, S. R. A microfabricated fluorescence-activated cell sorter. Nat. Biotechnol. 1999, 17, 1109–1111. DOI: 10.1038/15095",
    creator="Quake group, Caltech",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="The first microfabricated FACS — fluorescence-activated cell sorter on chip. Demonstrated cell sorting at modest throughput (~10 cells/s) with optical interrogation and pneumatic actuation in PDMS. Anticipates: chip-FACS architecture, microfluidic flow cytometry, and the entire chip-based flow cytometry subfield subsequently expanded by Sony SP6800, BD Cytopeia, On-chip Sort, and others.",
    sources=[
        "Nat. Biotechnol. 1999, 17, 1109–1111",
    ],
    disclosed_subsystems=[
        "valve-quake-pneumatic-membrane",
        "detection-fluorescence-on-chip",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["G01N 15/14", "B01L 3/00"],
    lineage_ancestors=["unger-2000-quake-monolithic-membrane-valve"],
)


# Write out
with CORPUS.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new entries to {CORPUS}")
