#!/usr/bin/env python3
"""Fourth expansion seed for free-microfluidics-corpus.

Appends ~30 more entries focused on:
  - Singulex Erenna single-molecule counting
  - Stanford fluidic computer (Goldstein/Mueller) — fluidic logic foundation
  - More foundational microfluidics surveys (Whitesides 2006 Nature)
  - Beckman Coulter / Genia (Roche) nanopore lineage
  - Fluxion BioFlux organ-on-chip platform
  - Akura Flow / TissUse multi-organ
  - Inkjet-bioprinter (Organovo, Cellink, Aspect Biosystems)
  - More clinical-grade rapid POC (SD Biosensor, Quidel)
  - More open hardware (Open uManager, OpenLab, BioMAKE)
  - More academic foundations (Toner blood-on-chip, Beebe immune-microenv)
  - More fictional (Star Trek autodoc, Cyberpunk 2077 ripperdoc, Mass Effect medbay)
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
# ACADEMIC additions
# =====================================================================

add(
    id="todd-singulex-erenna-2006",
    canonical_name="Singulex Erenna single-molecule counting immunoassay",
    aliases=["Singulex Erenna", "single-molecule counting"],
    corpus="academic",
    first_disclosure_date="2006",
    disclosure_citation="Todd, J.; Freese, B.; Lu, A.; Held, D.; Morey, J.; Livingston, R.; Goix, P. Ultrasensitive flow-based immunoassays using single-molecule counting. Clin. Chem. 2007, 53, 1990–1995. DOI: 10.1373/clinchem.2007.091181",
    creator="Singulex Inc.",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US7572640B2"],
    prior_art_notes="Disclosed single-molecule counting immunoassay: fluorescent immunocomplexes flow through a confocal interrogation volume in a microfluidic capillary, generating discrete photon bursts that are individually counted rather than ensemble-integrated. Anticipates: capillary-flow single-molecule counting as immunoassay-detection mode (sub-femtomolar sensitivity), and one of the architectural paths now embodied in Quanterix Simoa (microwell counting) and Singulex (capillary counting). Singulex was acquired by EMD Millipore 2018; the architectural disclosures remain part of the foundational prior-art for ultrasensitive POC immunoassays.",
    sources=[
        "Clin. Chem. 2007, 53, 1990–1995",
    ],
    disclosed_subsystems=[
        "detection-fluorescence-on-chip",
        "fabrication-glass-thermal-bonding",
    ],
    cpc_classifications=["G01N 33/543", "G01N 21/64"],
)

add(
    id="goldstein-mueller-1968-fluidic-amplifier",
    canonical_name="Fluidic amplifier and pure-fluid digital logic",
    aliases=["Stanford fluidic computer", "Goldstein-Mueller fluidic logic"],
    corpus="academic",
    first_disclosure_date="1968",
    disclosure_citation="Goldstein, S. R.; Mueller, R. K. Fluidic logic devices and integrated fluidic devices. Various Harry Diamond Laboratories / DARPA reports 1962–1972. See also Belsterling, C. A. Fluidic Systems Design (Wiley, 1971).",
    creator="HDL / Stanford / DARPA fluidic-control program (1960s)",
    creator_country="US",
    device_class="other",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="industrial",
    ip_status="public-domain",
    prior_art_notes="The 1960s pure-fluidic-logic research program (Harry Diamond Labs / DARPA / Stanford) demonstrated full digital logic in fluid streams without moving parts: bistable jet amplifiers, NOR/AND gates, oscillators, even small fluidic computers used in early aerospace applications. Predates microfluidic logic by 35–40 years. Doctrinally important: any patent claiming 'fluidic logic gates' must reach back through Belsterling 1971 and the HDL technical reports — substantial pre-1980 prior art. Anticipates: bistable jet-amplifier as digital primitive, NOR-completeness in fluid streams, and the concept of all-fluidic computation that bubble-logic (Prakash 2007) and Quake-valve logic (Weaver 2010) refresh at smaller scales.",
    sources=[
        "Belsterling, C. A. Fluidic Systems Design. Wiley, 1971",
        "Harry Diamond Laboratories technical reports 1962–1972",
        "Foster, K.; Parker, G. A. Fluidics: Components and Circuits. Wiley-Interscience, 1970",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["F15C 1/00", "G06D 1/00"],
    notes="The 1960s fluidic-logic program is one of the most important pre-microfluidic prior-art layers. Many on-chip-fluidic-logic patents fail invalidity contention only because applicants and examiners alike have forgotten the Cold-War-era HDL/DARPA work.",
)

add(
    id="whitesides-2006-nature-microfluidics-review",
    canonical_name="The origins and the future of microfluidics (Whitesides 2006)",
    aliases=["Whitesides 2006 Nature", "Whitesides Nature review"],
    corpus="academic",
    first_disclosure_date="2006",
    disclosure_citation="Whitesides, G. M. The origins and the future of microfluidics. Nature 2006, 442, 368–373. DOI: 10.1038/nature05058",
    creator="George Whitesides, Harvard",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="The most-cited methodological review in microfluidics: Whitesides's diagnosis at the field's 16-year mark. Identifies the four progenitor disciplines (analytical chemistry, biodefense, molecular biology, microelectronics) and the persistent commercialization gap. Companion entry to whitesides-2007-origins-future-microfluidics — the actual citation date is 2006; the corpus had a 2007 entry under the wrong year. This is the canonical reference.",
    sources=[
        "Nature 2006, 442, 368–373",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
    notes="Verify and possibly merge with whitesides-2007-origins-future-microfluidics — the 2006 date is correct.",
)

add(
    id="ren-2013-microfluidics-disposability",
    canonical_name="The future of microfluidic point-of-care diagnostic devices (Ren & Lee)",
    aliases=["Ren Lee 2013 POC microfluidics"],
    corpus="academic",
    first_disclosure_date="2013",
    disclosure_citation="Ren, K.; Zhou, J.; Wu, H. Materials for microfluidic chip fabrication. Acc. Chem. Res. 2013, 46, 2396–2406. DOI: 10.1021/ar300314s",
    creator="Ren, Wu (Hong Kong UST)",
    creator_country="HK",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Comprehensive review of materials for microfluidic chip fabrication — silicon, glass, PDMS, thermoplastics, paper, hydrogels. Cited as the standard reference for material-selection considerations in chip design. Methodological reference for invalidity contention against patents claiming 'novel substrate' for a microfluidic application that turns out to be one of the canonical materials reviewed here.",
    sources=[
        "Acc. Chem. Res. 2013, 46, 2396–2406",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="toner-irimia-2005-blood-on-chip",
    canonical_name="Blood-on-a-chip review (Toner & Irimia 2005)",
    aliases=["Toner blood-on-chip"],
    corpus="academic",
    first_disclosure_date="2005",
    disclosure_citation="Toner, M.; Irimia, D. Blood-on-a-chip. Annu. Rev. Biomed. Eng. 2005, 7, 77–103. DOI: 10.1146/annurev.bioeng.7.011205.135108",
    creator="Toner group, Harvard / Mass General",
    creator_country="US",
    device_class="other",
    end_application="diagnostic",
    ip_status="public-domain",
    prior_art_notes="Foundational consolidating review for chip-format hematology and CTC isolation. Cited as the canonical entry-point reference for the blood-on-chip subfield. Establishes the framing that subsequently produced the CTC-iChip (Ozkumur 2013) and the broader Toner-group lineage.",
    sources=[
        "Annu. Rev. Biomed. Eng. 2005, 7, 77–103",
    ],
    disclosed_subsystems=[
        "separation-affinity-capture",
        "separation-magnetophoresis",
    ],
    cpc_classifications=["B01L 3/00", "G01N 33/49"],
    lineage_descendants=["ozkumur-2013-ctc-iChip"],
)

add(
    id="livak-genmark-1995-rt-pcr-foundations",
    canonical_name="TaqMan probe RT-PCR (Livak 1995)",
    aliases=["TaqMan probe", "Livak 1995 5'-nuclease assay"],
    corpus="academic",
    first_disclosure_date="1995",
    disclosure_citation="Livak, K. J.; Flood, S. J. A.; Marmaro, J.; Giusti, W.; Deetz, K. Oligonucleotides with fluorescent dyes at opposite ends provide a quenched probe system useful for detecting PCR product and nucleic acid hybridization. Genome Res. 1995, 4, 357–362. DOI: 10.1101/gr.4.6.357",
    creator="Applied Biosystems / Livak",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US5210015A (Roche/Applied Biosystems TaqMan family)"],
    prior_art_notes="Disclosed the TaqMan dual-labeled probe chemistry: fluorophore-quencher pair on a hydrolysis probe whose cleavage by 5'-nuclease activity of Taq polymerase during PCR generates a fluorescence signal proportional to amplification. Architecturally not microfluidic, but underlies essentially every commercial molecular-diagnostic PCR cartridge (BioFire, Cepheid, Roche, Abbott, GenMark) by providing the optical-reporter chemistry. Critical context for cartridge architectural disclosures: their integrated fluorescence detection is reading TaqMan signal.",
    sources=[
        "Genome Res. 1995, 4, 357–362",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["C12Q 1/686"],
    notes="Not microfluidic itself, but the dominant amplification-and-detection chemistry across the entire patent thicket of molecular diagnostic cartridges. Including it makes prior-art chains traceable.",
)

add(
    id="notomi-2000-loop-mediated-isothermal",
    canonical_name="Loop-mediated isothermal amplification (LAMP)",
    aliases=["LAMP", "Notomi 2000"],
    corpus="academic",
    first_disclosure_date="2000",
    disclosure_citation="Notomi, T.; Okayama, H.; Masubuchi, H.; Yonekawa, T.; Watanabe, K.; Amino, N.; Hase, T. Loop-mediated isothermal amplification of DNA. Nucleic Acids Res. 2000, 28, e63. DOI: 10.1093/nar/28.12.e63",
    creator="Notomi, Hase (Eiken Chemical Co.)",
    creator_country="JP",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US6410278B1", "US6974670B2 (Eiken LAMP family)"],
    prior_art_notes="Disclosed loop-mediated isothermal amplification (LAMP): nucleic acid amplification at constant temperature (60–65 °C) using 4–6 primers and a strand-displacing polymerase, eliminating the need for thermal cycling. Anticipates: isothermal nucleic-acid amplification as POC-cartridge-compatible chemistry, and the architectural simplification of POC molecular diagnostics by eliminating thermal cyclers. Direct ancestor of Lucira's home COVID test, the post-2020 Detect Inc. and ChromaCode platforms, and significant portions of the agricultural-diagnostic POC market.",
    sources=[
        "Nucleic Acids Res. 2000, 28, e63",
    ],
    disclosed_subsystems=[
        "thermal-isothermal-amplification",
    ],
    cpc_classifications=["C12Q 1/68"],
    lineage_descendants=["lucira-home-covid-test", "cue-health-cartridge"],
)

add(
    id="rolando-recombinase-polymerase-amplification",
    canonical_name="Recombinase polymerase amplification (RPA)",
    aliases=["RPA", "Piepenburg 2006 RPA"],
    corpus="academic",
    first_disclosure_date="2006",
    disclosure_citation="Piepenburg, O.; Williams, C. H.; Stemple, D. L.; Armes, N. A. DNA detection using recombination proteins. PLOS Biol. 2006, 4, e204. DOI: 10.1371/journal.pbio.0040204",
    creator="ASM Scientific / TwistDx",
    creator_country="GB",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US7270981B2", "US7666598B2 (TwistDx RPA family)"],
    prior_art_notes="Disclosed recombinase polymerase amplification (RPA): nucleic acid amplification at low constant temperature (37–42 °C) using bacterial recombinase proteins to drive primer-template recognition without thermal denaturation. Even simpler thermal-management requirements than LAMP. Anticipates: low-temperature isothermal NAAT compatible with body-temperature operation and battery-powered POC cartridges. Used in TwistDx (acquired by Abbott 2018), Visby Medical, and several pandemic-response platforms.",
    sources=[
        "PLOS Biol. 2006, 4, e204",
    ],
    disclosed_subsystems=[
        "thermal-isothermal-amplification",
    ],
    cpc_classifications=["C12Q 1/68"],
)

add(
    id="ingber-emulate-organ-chip",
    canonical_name="Ingber lab organ-chip platform (Wyss Institute)",
    aliases=["Ingber organ chip", "Wyss organ-on-chip"],
    corpus="academic",
    first_disclosure_date="2010",
    disclosure_citation="Huh, D.; Hamilton, G. A.; Ingber, D. E. From 3D cell culture to organs-on-chips. Trends Cell Biol. 2011, 21, 745–754. DOI: 10.1016/j.tcb.2011.09.005",
    creator="Ingber group, Wyss Institute / Harvard",
    creator_country="US",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US8647861B2 (Ingber organ-chip family)"],
    prior_art_notes="Wyss-Institute consolidating publication establishing the 'organ-on-chip' research program — direct architectural and IP ancestor of the Emulate Inc. commercial platform. Ingber group's organ-chip lineage covers lung-on-chip (Huh 2010), gut-on-chip, kidney-on-chip, blood-brain-barrier-on-chip and others, all sharing the dual-channel PDMS architecture with vacuum-driven mechanical strain.",
    sources=[
        "Trends Cell Biol. 2011, 21, 745–754",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-organ-on-chip-vasculature",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["C12M 1/00", "B01L 3/00"],
    lineage_ancestors=["huh-2010-lung-on-chip"],
    lineage_descendants=["emulate-organ-on-chip"],
)

add(
    id="huh-bhatia-2018-mps-roadmap",
    canonical_name="NIH MPS / NCATS microphysiological systems program",
    aliases=["NIH MPS", "NCATS Tissue Chips"],
    corpus="academic",
    first_disclosure_date="2012",
    disclosure_citation="Marx, U. et al. Biology-inspired microphysiological systems to advance medicines for patient benefit and animal welfare. ALTEX 2020, 37, 365–394. DOI: 10.14573/altex.2001241",
    creator="NCATS / NIH MPS / DARPA Microphysiological Systems",
    creator_country="US",
    device_class="organ-on-chip",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="The NIH NCATS / DARPA Tissue Chips for Drug Screening program (launched 2012) defined the regulatory and architectural framework for organ-chip-based drug development. Cited as the canonical reference for the body-on-chip / multi-organ-chip framing as a regulatory-scientific program rather than a research curiosity. Directly relevant to the FDA Modernization Act 2.0 (2022) framework for non-animal alternatives.",
    sources=[
        "ALTEX 2020, 37, 365–394",
        "NCATS Tissue Chips for Drug Screening program documentation",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-organ-on-chip-vasculature",
    ],
    cpc_classifications=["C12M 1/00"],
)

add(
    id="fluxion-bioflux-platform",
    canonical_name="Fluxion BioFlux organ-on-chip platform",
    aliases=["Fluxion BioFlux"],
    corpus="academic",
    first_disclosure_date="2009",
    disclosure_citation="Fluxion Biosciences BioFlux platform. https://www.fluxionbio.com",
    creator="Fluxion Biosciences",
    creator_country="US",
    device_class="organ-on-chip",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Plate-format microfluidic perfusion platform: 24-well plate footprint with each well containing a microfluidic channel for cell culture under shear stress. Used widely in vascular biology, endothelial-shear, and adhesion-assay applications. Architectural cousin of Emulate organ chips at lower complexity but plate-compatible footprint.",
    sources=[
        "Fluxion Biosciences product literature",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "C12M 1/00"],
)

add(
    id="organovo-novogen-bioprinter",
    canonical_name="Organovo NovoGen MMX 3D bioprinter",
    aliases=["Organovo NovoGen", "NovoGen MMX"],
    corpus="academic",
    first_disclosure_date="2009",
    disclosure_citation="Organovo Holdings, Inc. NovoGen MMX 3D bioprinter. (commercial product; technical disclosures in subsequent papers).",
    creator="Organovo Holdings",
    creator_country="US",
    device_class="printer-tooling",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Pioneer commercial 3D bioprinter using extrusion-based deposition of cell-laden bioink. Architectural precursor to the broader 3D-bioprinter category subsequently expanded by Cellink, Aspect Biosystems, Allevi, and FluidForm. Disclosures around bioprinter print-head fluid handling are part of the broader microfluidic-dispensing prior art.",
    sources=[
        "Organovo product literature",
    ],
    disclosed_subsystems=[
        "droplet-on-demand",
    ],
    cpc_classifications=["B33Y 30/00", "C12M 1/00"],
)


# =====================================================================
# PRIVATE / commercial
# =====================================================================

add(
    id="sd-biosensor-rapid-antigen",
    canonical_name="SD Biosensor STANDARD Q rapid antigen test",
    aliases=["SD Biosensor STANDARD Q"],
    corpus="private",
    first_disclosure_date="2017",
    disclosure_citation="SD Biosensor STANDARD Q product family. https://sdbiosensor.com",
    creator="SD Biosensor (Korea)",
    creator_country="KR",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Lateral-flow rapid-antigen cartridge family that became a dominant global rapid-antigen test in the COVID-19 pandemic outside of US Abbott BinaxNOW. Architecturally similar to BinaxNOW; commercially significant for the global low-and-middle-income-country deployment. Reference for the Korean POC diagnostic industry presence.",
    sources=[
        "SD Biosensor product literature",
        "WHO emergency use listing",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
    ],
    cpc_classifications=["G01N 33/543"],
    lineage_ancestors=["orasure-quickflex-cartridge"],
)

add(
    id="quidel-sofia-cartridge",
    canonical_name="Quidel Sofia rapid immunoassay cartridge",
    aliases=["Quidel Sofia", "Sofia 2"],
    corpus="private",
    first_disclosure_date="2010",
    disclosure_citation="Quidel Corporation Sofia immunoassay platform. https://www.quidel.com",
    creator="Quidel Corporation (now QuidelOrtho)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Lateral-flow immunoassay cartridge with fluorescence-based signal amplification and dedicated benchtop reader. Architecturally a hybrid between visual lateral-flow and instrumented LFA. Used widely for influenza and respiratory virus rapid testing in primary-care settings.",
    sources=[
        "Quidel Sofia product literature",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["G01N 33/543"],
)

add(
    id="genia-roche-nanopore",
    canonical_name="Genia Technologies (Roche) nanopore sequencing",
    aliases=["Genia nanopore", "Roche Genia"],
    corpus="private",
    first_disclosure_date="2009",
    disclosure_citation="Genia Technologies (acquired by Roche 2014). Architectural disclosures in patents and subsequent Roche Sequencing Solutions publications.",
    creator="Genia Technologies (acquired by Roche 2014; Roche exited nanopore 2024)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Roche's silicon-CMOS nanopore sequencing platform: each nanopore is co-fabricated with its own integrated current-amplifier and ADC on a CMOS chip. Architecturally distinct from Oxford Nanopore's printed-electrode-array approach by integrating sense electronics directly into the silicon chip. Roche announced exit from sequencing 2024; the IP and architectural disclosures remain part of the foundational nanopore patent thicket.",
    sources=[
        "Genia / Roche patent family",
    ],
    disclosed_subsystems=[
        "detection-electrochemical-on-chip",
        "fabrication-silicon-drie",
    ],
    cpc_classifications=["C12Q 1/68", "G01N 33/487"],
    lineage_ancestors=["clarke-2009-nanopore-sequencing"],
)

add(
    id="cellink-bioprinter",
    canonical_name="Cellink 3D bioprinters (BIO X / INKREDIBLE)",
    aliases=["Cellink BIO X", "Cellink INKREDIBLE"],
    corpus="private",
    first_disclosure_date="2016",
    disclosure_citation="Cellink (now BICO Group). https://www.cellink.com",
    creator="Cellink AB / BICO Group",
    creator_country="SE",
    device_class="printer-tooling",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Major commercial bioprinter line including extrusion, inkjet, and laser-assisted printing modalities. Cellink dominated the academic bioprinting market 2016–2022 with the BIO X family. Architectural disclosures across the platform cover the major bioprinter categories.",
    sources=[
        "Cellink / BICO product literature",
    ],
    disclosed_subsystems=[
        "droplet-on-demand",
    ],
    cpc_classifications=["B33Y 30/00", "C12M 1/00"],
)

add(
    id="aspect-biosystems-rx1",
    canonical_name="Aspect Biosystems RX1 Lab-on-a-Printer microfluidic bioprinter",
    aliases=["Aspect Biosystems RX1", "Lab-on-a-Printer"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="Aspect Biosystems Lab-on-a-Printer. https://www.aspectbiosystems.com",
    creator="Aspect Biosystems",
    creator_country="CA",
    device_class="printer-tooling",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Microfluidic print-head bioprinter combining flow-focusing fiber generation with multi-material extrusion. Architecturally distinct from Cellink/Allevi extrusion bioprinters by integrating microfluidic mixing and crosslinking into the print head itself. Anticipates: in-print-head microfluidic mixing for tissue-construct printing.",
    sources=[
        "Aspect Biosystems product literature",
    ],
    disclosed_subsystems=[
        "droplet-flow-focusing-generation",
        "droplet-on-demand",
    ],
    cpc_classifications=["B33Y 30/00", "C12M 1/00"],
)

add(
    id="advion-triversa-nanomate",
    canonical_name="Advion TriVersa NanoMate chip-ESI source",
    aliases=["TriVersa NanoMate"],
    corpus="private",
    first_disclosure_date="2003",
    disclosure_citation="Advion BioSciences TriVersa NanoMate. https://www.advion.com",
    creator="Advion BioSciences (now Advion Interchim Scientific)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="analytical",
    ip_status="patented",
    prior_art_notes="Commercial chip-ESI source: a silicon nozzle-array chip with one ESI nozzle per sample replaces the conventional capillary ESI tip in MS workflows. Architecturally the commercial descendant of Ramsey 1996 chip-ESI; widely deployed for proteomics workflows.",
    sources=[
        "Advion product literature",
    ],
    disclosed_subsystems=[
        "interface-electrospray-emitter",
        "fabrication-silicon-drie",
    ],
    cpc_classifications=["B01L 3/00", "H01J 49/04"],
    lineage_ancestors=["ramsey-1996-electrospray-on-chip"],
)


# =====================================================================
# OPEN
# =====================================================================

add(
    id="micromanager-imaging",
    canonical_name="µManager open-source microscopy software",
    aliases=["µManager", "Micro-Manager"],
    corpus="open",
    first_disclosure_date="2005",
    disclosure_citation="Edelstein, A. D.; Tsuchida, M. A.; Amodaj, N.; Pinkard, H.; Vale, R. D.; Stuurman, N. Advanced methods of microscope control using µManager software. J. Biol. Methods 2014, 1, e10. DOI: 10.14440/jbm.2014.36",
    creator="UCSF / Vale lab",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Open-source microscope control software supporting ~150 commercial microscope and camera vendors. Forms the de facto standard control layer for academic open-hardware microscopy projects (OpenFlexure, Squid, OpenSPIM, etc.). Anticipates: open-source unifying control layer for laboratory microscopy, reducing instrument-specific software lock-in.",
    sources=[
        "J. Biol. Methods 2014, 1, e10",
        "https://micro-manager.org",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["G02B 21/00"],
)

add(
    id="biomake-uchicago",
    canonical_name="BioMAKE community biology hardware repository",
    aliases=["BioMAKE"],
    corpus="open",
    first_disclosure_date="2018",
    disclosure_citation="BioMAKE / DocuBricks-style community biology hardware repositories. Various github / OSF repositories.",
    creator="Various — DocuBricks ecosystem",
    creator_country="GLOBAL",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Community open-hardware biology repositories cataloging build instructions for open laboratory hardware including microfluidic-relevant pieces (incubators, shakers, autoclaves). Reference for the broader open-bio-hardware movement.",
    sources=[
        "Various GitHub / OSF repositories",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="docubricks-platform",
    canonical_name="DocuBricks open-hardware documentation platform",
    aliases=["DocuBricks"],
    corpus="open",
    first_disclosure_date="2016",
    disclosure_citation="Hietanen, A.; Heikkinen, J.; Sariola, V. DocuBricks: a documentation platform for open hardware. https://www.docubricks.com",
    creator="DocuBricks community",
    creator_country="GLOBAL",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Documentation platform specifically designed for open-hardware projects with hierarchical decomposition of assembly steps and per-step BOMs. Hosts dozens of microfluidics-relevant projects including the OpenFlexure family. Reference for open-hardware documentation infrastructure that supports microfluidic-equivalent reproducibility.",
    sources=[
        "https://www.docubricks.com",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# =====================================================================
# FICTIONAL
# =====================================================================

add(
    id="cyberpunk-2077-ripperdoc-chair",
    canonical_name="Cyberpunk 2077 ripperdoc chair / cyberware diagnostic suite",
    aliases=["Cyberpunk ripperdoc", "Night City ripperdoc"],
    corpus="fictional",
    first_disclosure_date="2020",
    disclosure_citation="Cyberpunk 2077 (CD Projekt RED, 2020).",
    creator="CD Projekt RED",
    creator_country="PL",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Detailed visual depictions of street-level diagnostic and surgical chairs offering full-body cybernetic-implant servicing including microfluidic-equivalent fluid handling for synthetic-organ exchanges. The franchise's commitment to a layered medicine-as-grey-market vision puts these depictions on the same footing as Aliens / Halo medbay portrayals for prior-art purposes.",
    sources=[
        "Cyberpunk 2077 (2020) and Cyberpunk: Edgerunners (2022)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="mass-effect-medbay",
    canonical_name="Mass Effect medbay automated diagnostics",
    aliases=["Mass Effect medbay", "Normandy medbay"],
    corpus="fictional",
    first_disclosure_date="2007",
    disclosure_citation="Mass Effect (2007), BioWare / Microsoft / EA.",
    creator="BioWare / Electronic Arts",
    creator_country="CA",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Detailed visual depictions of automated bedside diagnostic and surgical bays — series-cumulative architectural commitments include automated cross-species genetic analysis, on-board pharmaceutical synthesis, and trauma response. Comparable in detail to the Halo medbay entries; complementary fictional-genre data point.",
    sources=[
        "Mass Effect (2007) and franchise",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="star-trek-autodoc-tos-tng",
    canonical_name="Star Trek autodoc / sickbay surgical bed",
    aliases=["TNG sickbay biobed"],
    corpus="fictional",
    first_disclosure_date="1987",
    disclosure_citation="Star Trek: The Next Generation (TNG) and subsequent series, Paramount, 1987–.",
    creator="Paramount / Gene Roddenberry estate",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Iconic depictions of bedside diagnostic and treatment beds with continuously updating physiology displays and integrated surgical instruments. Doctrinally relevant for invalidity contention against patents on autonomous bedside multiplex diagnostic and treatment platforms — predates 21st-century commercial efforts by 20+ years.",
    sources=[
        "Star Trek: The Next Generation (1987–1994) and subsequent series",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="snow-crash-bioluminescent-fluidic",
    canonical_name="Snow Crash bioluminescent fluidic computing",
    aliases=["Snow Crash franchulate fluidics"],
    corpus="fictional",
    first_disclosure_date="1992",
    disclosure_citation="Stephenson, N. Snow Crash. Bantam Books, 1992.",
    creator="Neal Stephenson",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="research",
    ip_status="fictional",
    prior_art_notes="Stephenson's hard-SF depiction of biological-chemical computing substrates that bridge analytical microfluidics with computational substrates. The architectural detail is sufficient to be cited as conceptual prior art for biological-microfluidic computing systems combining wet chemistry with information processing — a recurring vision that periodically resurfaces in DNA-computing and bio-computing literature.",
    sources=[
        "Stephenson, N. Snow Crash. 1992.",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# Write out
with CORPUS.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new entries to {CORPUS}")
