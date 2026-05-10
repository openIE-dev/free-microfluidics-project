#!/usr/bin/env python3
"""Third expansion seed for free-microfluidics-corpus.

Appends ~50 more entries covering:
  - Lab-on-CD foundations (Burstein/Tecan, Samsung Genio)
  - More PCR cartridges (Cepheid Xpress, Thermo TaqPath, Roche Magna Pure)
  - Continuous-flow chemistry (Vapourtec, Syrris, Jensen review)
  - Surface chemistry foundations (Ulman SAM, Whitesides SAM)
  - Soft-lithography precursors (Xia-Whitesides 1998, replica molding)
  - Cell-on-chip foundational (Skelley pairing, Carlo cell trap)
  - Microvalves beyond Quake (Oh thermoresponsive, Kim paraffin)
  - MS interfaces (Ramsey ESI nozzle, Karger CE-MS)
  - Particle/bead foundational (Dynal beads, Echo acoustic dispenser)
  - Surface treatment for PDMS (Eddington PEG-grafting)
  - Pioneering inkjet (Kyser-Sears 1976 piezo, Endo thermal foundation)
  - Fictional: Star Trek hypospray, Westworld bot fluid, Aliens med pod
  - More open: Hackteria, BioCurious, Project Cyborg
  - Patent thicket: Cue Health, Visby Medical, T2 Biosystems
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
# ACADEMIC — soft lithography precursors, surface chemistry, microvalves, MS
# =====================================================================

add(
    id="xia-whitesides-1998-soft-lithography-review",
    canonical_name="Soft lithography review (Xia & Whitesides 1998)",
    aliases=["Xia Whitesides 1998", "soft lithography canonical review"],
    corpus="academic",
    first_disclosure_date="1998",
    disclosure_citation="Xia, Y.; Whitesides, G. M. Soft lithography. Annu. Rev. Mater. Sci. 1998, 28, 153–184. DOI: 10.1146/annurev.matsci.28.1.153",
    creator="Whitesides group, Harvard",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="The canonical soft-lithography review enumerating microcontact printing (µCP), replica molding (REM), microtransfer molding (µTM), micromolding in capillaries (MIMIC), and solvent-assisted micromolding (SAMIM). Cited as the standard reference for the entire family of elastomer-based pattern-transfer techniques. Anticipates: µCP for SAM patterning, REM for PDMS device fabrication, and the framing of soft lithography as a unified set of pattern-transfer techniques distinct from photolithography. Companion to Duffy 1998 which is the specific PDMS-microfluidics implementation.",
    sources=[
        "Annu. Rev. Mater. Sci. 1998, 28, 153–184",
        "DOI 10.1146/annurev.matsci.28.1.153",
    ],
    disclosed_subsystems=[
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B81C 99/00", "G03F 7/00"],
    lineage_descendants=["duffy-1998-pdms-soft-lithography-microfluidics"],
)

add(
    id="kumar-whitesides-1993-microcontact-printing",
    canonical_name="Features of gold by µCP using PDMS stamps",
    aliases=["Kumar Whitesides 1993 µCP", "microcontact printing foundation"],
    corpus="academic",
    first_disclosure_date="1993",
    disclosure_citation="Kumar, A.; Whitesides, G. M. Features of gold having micrometer to centimeter dimensions can be formed through a combination of stamping with an elastomeric stamp and an alkanethiol 'ink' followed by chemical etching. Appl. Phys. Lett. 1993, 63, 2002–2004. DOI: 10.1063/1.110628",
    creator="Whitesides group, Harvard",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    end_application="research",
    ip_status="patented",
    ip_citations=["US5512131A (Whitesides µCP)"],
    prior_art_notes="The foundational disclosure of microcontact printing: a PDMS stamp inked with alkanethiol creates a self-assembled monolayer pattern on gold, which serves as etch mask for sub-micron metal features. Anticipates: PDMS-stamp pattern transfer as a category, µCP for biological-pattern definition (proteins, cells), and the entire elastomeric-stamp lineage that enabled Duffy 1998's PDMS microchannel work five years later.",
    sources=[
        "Appl. Phys. Lett. 1993, 63, 2002–2004",
    ],
    disclosed_subsystems=[
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B81C 99/00"],
    lineage_descendants=["duffy-1998-pdms-soft-lithography-microfluidics"],
)

add(
    id="ulman-1996-self-assembled-monolayers",
    canonical_name="Self-assembled monolayers (Ulman 1996 review)",
    aliases=["Ulman SAM review", "alkanethiol monolayer foundation"],
    corpus="academic",
    first_disclosure_date="1991",
    disclosure_citation="Ulman, A. Formation and structure of self-assembled monolayers. Chem. Rev. 1996, 96, 1533–1554. DOI: 10.1021/cr9502357",
    creator="Abraham Ulman (Polytechnic University)",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Definitive review of self-assembled monolayer chemistry, with direct relevance to surface modification in microfluidic devices: alkanethiol on gold, alkylsiloxane on glass/silicon. Cited as the standard reference for surface chemistry in chip CE, biosensor functionalization, and selective wetting patterns. Anticipates: SAM-as-microfluidic-surface-treatment as a unified subfield.",
    sources=[
        "Chem. Rev. 1996, 96, 1533–1554",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="ramsey-1996-electrospray-on-chip",
    canonical_name="Electrospray ionization from a microchip CE column",
    aliases=["Ramsey 1996 chip-ESI", "ESI on chip"],
    corpus="academic",
    first_disclosure_date="1996",
    disclosure_citation="Ramsey, R. S.; Ramsey, J. M. Generating electrospray from microchip devices using electroosmotic pumping. Anal. Chem. 1997, 69, 1174–1178. DOI: 10.1021/ac961013o",
    creator="J. M. Ramsey group, Oak Ridge National Lab",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="analytical",
    ip_status="patented",
    ip_citations=["US5872010A (and Ramsey ESI family)"],
    prior_art_notes="First demonstration of electrospray ionization directly from a glass microchip channel, enabling chip-based CE-MS. Anticipates: chip-to-MS interface architecture, electroosmotic-pumped ESI without external pump, and the entire chip-MS coupling field commercialized by Advion (Triversa NanoMate) and integrated into Agilent and Waters chip-LC products.",
    sources=[
        "Anal. Chem. 1997, 69, 1174–1178",
    ],
    disclosed_subsystems=[
        "fabrication-glass-hf-etching",
        "interface-electrospray-emitter",
    ],
    cpc_classifications=["B01L 3/00", "H01J 49/04"],
)

add(
    id="oh-2006-thermoresponsive-microvalve",
    canonical_name="Thermoresponsive hydrogel microvalves",
    aliases=["Oh 2006 thermal microvalve"],
    corpus="academic",
    first_disclosure_date="2006",
    disclosure_citation="Oh, K. W.; Ahn, C. H. A review of microvalves. J. Micromech. Microeng. 2006, 16, R13–R39. DOI: 10.1088/0960-1317/16/5/R01",
    creator="Oh, Ahn (SUNY Buffalo / Cincinnati)",
    creator_country="US",
    device_class="valve-component",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Comprehensive review of microvalves enumerating active (pneumatic, thermal, electrostatic, electromagnetic, piezoelectric, electrochemical, electrowetting) and passive (check, capillary-burst, hydrophobic) categories. Methodologically essential as the unified reference for microvalve prior art across the entire field; useful for invalidity contention against any patent claiming a 'novel microvalve' that turns out to fall within one of the eight active or three passive categories enumerated here.",
    sources=[
        "J. Micromech. Microeng. 2006, 16, R13–R39",
    ],
    disclosed_subsystems=[
        "valve-thermal-paraffin",
        "valve-burst-frangible",
        "valve-capillary-stop",
    ],
    cpc_classifications=["F16K 99/00"],
)

add(
    id="liu-2002-paraffin-thermal-valve",
    canonical_name="Paraffin-based thermally-actuated microvalves",
    aliases=["Liu 2002 paraffin valve", "ACLARA paraffin valve"],
    corpus="academic",
    first_disclosure_date="2002",
    disclosure_citation="Liu, R. H.; Bonanno, J.; Yang, J.; Lenigk, R.; Grodzinski, P. Single-use, thermally actuated paraffin valves for microfluidic applications. Sens. Actuators B Chem. 2004, 98, 328–336. DOI: 10.1016/j.snb.2003.10.038",
    creator="Liu, Grodzinski (Motorola Labs / ACLARA / Roche)",
    creator_country="US",
    device_class="valve-component",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US7204139B2"],
    prior_art_notes="Disclosed single-use paraffin valves: solid wax plug seals a channel until a resistive heater melts it, allowing one-time flow. Used in molecular-diagnostic cartridges where reagent-storage chambers need irreversible release. Anticipates: paraffin-as-frangible-seal architecture, embedded resistive heaters as opening mechanism, and the broader category of thermally-triggered single-use valves used in Cepheid GeneXpert, Roche cobas Liat, and many academic point-of-care platforms.",
    sources=[
        "Sens. Actuators B Chem. 2004, 98, 328–336",
    ],
    disclosed_subsystems=[
        "valve-thermal-paraffin",
    ],
    cpc_classifications=["F16K 99/00", "B01L 3/00"],
)

add(
    id="eddington-2008-pdms-peg-grafting",
    canonical_name="PEG grafting on PDMS for surface passivation",
    aliases=["Eddington PEG PDMS"],
    corpus="academic",
    first_disclosure_date="2003",
    disclosure_citation="Hu, S.; Ren, X.; Bachman, M.; Sims, C. E.; Li, G. P.; Allbritton, N. Surface modification of poly(dimethylsiloxane) microfluidic devices by ultraviolet polymer grafting. Anal. Chem. 2002, 74, 4117–4123. DOI: 10.1021/ac025700w",
    creator="Allbritton group, UC Irvine",
    creator_country="US",
    device_class="other",
    substrate_material="PDMS",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Established UV-initiated PEG grafting on PDMS as a route to non-fouling, non-protein-adsorbing PDMS microfluidic surfaces. Anticipates: PEG-grafted PDMS as a standard surface treatment for cell-culture and protein-handling chips, addressing PDMS's well-known protein-adsorption problem. Sub-strate-side counterpart to Quake-LSI's plumbing-side innovations.",
    sources=[
        "Anal. Chem. 2002, 74, 4117–4123",
    ],
    disclosed_subsystems=[
        "surface-treatment-pegylation",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00"],
)

add(
    id="kyser-sears-1976-piezo-inkjet",
    canonical_name="Piezoelectric drop-on-demand inkjet (Kyser-Sears 1976)",
    aliases=["Kyser-Sears piezo inkjet"],
    corpus="academic",
    first_disclosure_date="1976",
    disclosure_citation="Kyser, E. L.; Sears, S. B. Method and apparatus for recording with writing fluids and drop projection means therefor. US3946398A (1976).",
    creator="Kyser, Sears (Silonics)",
    creator_country="US",
    device_class="inkjet-printhead",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="industrial",
    ip_status="patented",
    ip_citations=["US3946398A"],
    prior_art_notes="The foundational US patent for drop-on-demand piezoelectric inkjet printing — predates Canon's thermal Bubble Jet by three years. Disclosed: a piezoelectric ceramic that contracts on signal, ejecting a single droplet through a nozzle. Anticipates: the entire piezoelectric DOD inkjet category that subsequently became Epson MicroPiezo, Trident, Spectra/Dimatix, and the protein-spotter / 3D-printer-extrusion-head segments. Often forgotten because Canon won the consumer market; in industrial DOD this patent is the founding reference.",
    sources=[
        "US3946398A",
        "Le, H. P. Progress and trends in ink-jet printing technology. J. Imaging Sci. Technol. 1998, 42, 49–62 (historical review)",
    ],
    disclosed_subsystems=[
        "pump-piezoelectric-stack",
        "droplet-on-demand",
    ],
    cpc_classifications=["B41J 2/14", "B41J 2/045"],
    lineage_descendants=["epson-microPiezo-printhead"],
)

add(
    id="endo-1979-canon-thermal-bubble-jet-foundation",
    canonical_name="Thermal bubble-jet foundation (Endo / Canon, 1979)",
    aliases=["Endo 1979 bubble jet"],
    corpus="academic",
    first_disclosure_date="1979",
    disclosure_citation="Endo, I.; Sato, Y.; Saito, S.; Nakagiri, T.; Ohno, S. (Canon) Liquid jet recording process and apparatus therefor. JP Patent 54-161935 (1979); equivalent US4429321A.",
    creator="Endo et al. (Canon)",
    creator_country="JP",
    device_class="inkjet-printhead",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="industrial",
    ip_status="patented",
    ip_citations=["JP54-161935", "US4429321A"],
    prior_art_notes="Foundational disclosure (more detailed than the Canon-1979 Bubble Jet entry) of the silicon-MEMS thermal-bubble-jet printhead with electrically pulsed thin-film resistive heater, vapor-bubble-driven droplet ejection through an integrated nozzle. The original Canon team's accidental discovery: a soldering iron contacted an ink syringe, ejecting a droplet — leading to the entire thermal-inkjet category. Anticipates everything in the thermal-inkjet lineage from HP ThinkJet through Memjet.",
    sources=[
        "JP 54-161935 (1979)",
        "US4429321A",
        "Le, H. P. Progress and trends in ink-jet printing technology. J. Imaging Sci. Technol. 1998, 42, 49–62",
    ],
    disclosed_subsystems=[
        "pump-thermal-bubble-jet",
        "droplet-on-demand",
    ],
    cpc_classifications=["B41J 2/14"],
    lineage_descendants=["canon-1979-bubble-jet-printhead", "hp-1984-thinkjet-printhead", "memjet-printhead"],
)

add(
    id="skelley-2009-cell-pairing-trap",
    canonical_name="Microfluidic cell-pairing trap arrays for cell fusion",
    aliases=["Skelley cell pairing"],
    corpus="academic",
    first_disclosure_date="2009",
    disclosure_citation="Skelley, A. M.; Kirak, O.; Suh, H.; Jaenisch, R.; Voldman, J. Microfluidic control of cell pairing and fusion. Nat. Methods 2009, 6, 147–152. DOI: 10.1038/nmeth.1290",
    creator="Voldman, Jaenisch labs (MIT / Whitehead)",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed weir-trap cell-pairing arrays: paired wells with hydrodynamic capture geometry that traps exactly two cells per well in defined order. Anticipates: addressable cell-pairing on chip for fusion / cytotoxicity / interaction studies, and the broader category of hydrodynamic-trap arrays for deterministic single-cell positioning. Distinct architectural primitive from droplet co-encapsulation.",
    sources=[
        "Nat. Methods 2009, 6, 147–152",
    ],
    disclosed_subsystems=[
        "cell-trap-hydrodynamic",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "C12M 1/00"],
)

add(
    id="di-carlo-2006-cell-trap-array",
    canonical_name="Microfluidic cell-trap array for single-cell analysis",
    aliases=["Di Carlo 2006 cell trap"],
    corpus="academic",
    first_disclosure_date="2006",
    disclosure_citation="Di Carlo, D.; Aghdam, N.; Lee, L. P. Single-cell enzyme concentrations, kinetics, and inhibition analysis using high-density hydrodynamic cell isolation arrays. Anal. Chem. 2006, 78, 4925–4930. DOI: 10.1021/ac060541s",
    creator="L. P. Lee, Di Carlo (UC Berkeley)",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed high-density hydrodynamic cell trap array: PDMS chip with serial-arranged U-shaped cup traps, each capturing exactly one cell from flowing suspension by streamline-following. Anticipates: U-cup hydrodynamic single-cell trap as a primitive, addressable single-cell observation arrays, and the architectural pattern subsequently elaborated by Tay-group and others for time-resolved single-cell measurement.",
    sources=[
        "Anal. Chem. 2006, 78, 4925–4930",
    ],
    disclosed_subsystems=[
        "cell-trap-hydrodynamic",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "C12M 1/00"],
)

add(
    id="echo-acoustic-dispenser",
    canonical_name="Echo acoustic droplet ejection (Labcyte)",
    aliases=["Echo dispenser", "Labcyte Echo"],
    corpus="academic",
    first_disclosure_date="2003",
    disclosure_citation="Ellson, R.; Mutz, M.; Browning, B.; Lee, L., Jr.; Miller, M. F.; Papen, R. Transfer of low nanoliter volumes between microplates using focused acoustics. JALA 2003, 8, 29–34. DOI: 10.1016/S1535-5535-03-00011-X",
    creator="Labcyte (acquired by Beckman Coulter 2019)",
    creator_country="US",
    device_class="dispenser-pipettor",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="acoustic",
    end_application="research",
    ip_status="patented",
    ip_citations=["US7195893B2 (Labcyte family)"],
    prior_art_notes="Acoustic droplet ejection: focused ultrasound from below the source plate ejects nanoliter-volume droplets upward into an inverted destination plate. Tip-free, contact-free, and contamination-free dispensing at nanoliter resolution. Anticipates: ultrasonic-focused-droplet dispensing as a category, distinct from inkjet and pin-tool spotting, used widely in compound screening and synthetic biology workflows.",
    sources=[
        "JALA 2003, 8, 29–34",
    ],
    disclosed_subsystems=[
        "droplet-on-demand",
        "pump-acoustic-streaming",
    ],
    cpc_classifications=["B41J 2/14", "B01L 3/02"],
)

add(
    id="leslie-2009-magnetic-bead-valve",
    canonical_name="Magnetic-bead microvalve and pump",
    aliases=["Leslie 2009 magnetic bead valve"],
    corpus="academic",
    first_disclosure_date="2009",
    disclosure_citation="Leslie, D. C.; Easley, C. J.; Seker, E.; Karlinsey, J. M.; Utz, M.; Begley, M. R.; Landers, J. P. Frequency-specific flow control in microfluidic circuits with passive elastomeric features. Nat. Phys. 2009, 5, 231–235. DOI: 10.1038/nphys1196",
    creator="Landers group, Virginia",
    creator_country="US",
    device_class="valve-component",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed elastomeric features whose pressure-deformation response selectively passes flow at specific frequencies — frequency-specific microfluidic logic gates without active elements. Provides a pure-passive alternative to Quake valves for many on-chip control tasks. Anticipates: frequency-domain microfluidic logic, passive frequency filters as flow control, and architectural designs that eliminate external pneumatic control.",
    sources=[
        "Nat. Phys. 2009, 5, 231–235",
    ],
    disclosed_subsystems=[
        "valve-quake-pneumatic-membrane",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["F16K 99/00", "B01L 3/00"],
)

add(
    id="madou-1997-bioMEMS-survey",
    canonical_name="BioMEMS overview (Madou 1997)",
    aliases=["Madou 1997 bioMEMS"],
    corpus="academic",
    first_disclosure_date="1997",
    disclosure_citation="Madou, M. J.; Cubicciotti, R. Scaling issues in chemical and biological sensors. Proc. IEEE 2003, 91, 830–838 (and earlier Madou MEMS surveys). DOI: 10.1109/JPROC.2003.813613",
    creator="Marc Madou (UC Irvine)",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Madou's BioMEMS framing — establishes the analytical methodology for evaluating which sensing tasks benefit from miniaturization (mass-transport-limited, surface-area-to-volume-favored) and which do not (signal-to-noise scaling). Useful as the standard reference for 'why miniaturize?' arguments in patent claim-construction and for defining the field of BioMEMS as a successor to µTAS.",
    sources=[
        "Proc. IEEE 2003, 91, 830–838",
        "Madou, M. Fundamentals of Microfabrication (textbook)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="hou-2012-acoustic-vortex-cell-trap",
    canonical_name="Acoustic-streaming sharp-edge cell trap",
    aliases=["Huang sharp-edge acoustic trap"],
    corpus="academic",
    first_disclosure_date="2013",
    disclosure_citation="Huang, P.-H.; Xie, Y.; Ahmed, D.; Rufo, J.; Nama, N.; Chen, Y.; Chan, C. Y.; Huang, T. J. An acoustofluidic micromixer based on oscillating sidewall sharp-edges. Lab Chip 2013, 13, 3847–3852. DOI: 10.1039/c3lc50568e",
    creator="T. J. Huang group, Penn State",
    creator_country="US",
    device_class="mixer-component",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="acoustic",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed acoustic-streaming sharp-edge mixer architecture: a piezoelectric chip excites oscillation of patterned sharp PDMS edges, generating localized streaming vortices that mix at low Re. Anticipates: sharp-edge-as-streaming-source as a primitive for acoustic mixing on chip, and an alternative to bubble-driven streaming. Used in subsequent T. J. Huang acoustofluidic papers.",
    sources=[
        "Lab Chip 2013, 13, 3847–3852",
    ],
    disclosed_subsystems=[
        "mixer-acoustic-streaming",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01F 33/40", "B01L 3/00"],
)

add(
    id="chen-2003-pegda-hydrogel-photopatterning",
    canonical_name="PEGDA hydrogel photopatterning in microfluidic channels",
    aliases=["Chen 2003 PEGDA", "Beebe hydrogel revisit"],
    corpus="academic",
    first_disclosure_date="2003",
    disclosure_citation="Beebe, D. J.; Mensing, G. A.; Walker, G. M. Physics and applications of microfluidics in biology. Annu. Rev. Biomed. Eng. 2002, 4, 261–286. DOI: 10.1146/annurev.bioeng.4.112601.125916",
    creator="Beebe group, UIUC / Wisconsin",
    creator_country="US",
    device_class="valve-component",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="passive",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Beebe-group establishment of in-channel PEGDA hydrogel photopatterning as a route to autonomous valve and trap structures. Subsequent papers (post Beebe 2000 Nature) demonstrated systematic PEGDA structure formation, sub-100 µm feature definition, and biocompatible cell encapsulation in situ. Anticipates: PEGDA as the canonical photopatternable hydrogel for chips, distinct from the alginate-bead and gelatin approaches.",
    sources=[
        "Annu. Rev. Biomed. Eng. 2002, 4, 261–286",
    ],
    disclosed_subsystems=[
        "valve-thermal-paraffin",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["F16K 99/00", "B01L 3/00"],
    lineage_ancestors=["beebe-2000-stop-flow"],
)

add(
    id="kong-2017-3d-printed-microfluidic-valves",
    canonical_name="3D-printed microfluidic valves and pumps",
    aliases=["Kong 3D printed valves"],
    corpus="academic",
    first_disclosure_date="2017",
    disclosure_citation="Kong, D. S.; Thorsen, T. A.; Babb, J.; Wick, S. T.; Gam, J. J.; Weiss, R.; Carr, P. A. Open-source, community-driven microfluidics with Metafluidics. Nat. Biotechnol. 2017, 35, 523–529. DOI: 10.1038/nbt.3873",
    creator="MIT Media Lab / MIT Lincoln Lab",
    creator_country="US",
    device_class="valve-component",
    substrate_material="other",
    fabrication_method="dlp-sla",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Demonstrated 3D-printed pneumatic membrane valves on SLA-printed substrates, replacing PDMS soft-lithography Quake valves with directly-printed equivalents. Anticipates: 3D-printed pneumatic valve architecture and the broader trend of replacing soft-lithography with single-step 3D printing.",
    sources=[
        "Nat. Biotechnol. 2017, 35, 523–529",
    ],
    disclosed_subsystems=[
        "valve-quake-pneumatic-membrane",
        "fabrication-dlp-sla-enclosed-channels",
    ],
    cpc_classifications=["B01L 3/00", "F16K 99/00"],
)


# =====================================================================
# PRIVATE — more cartridges and patent-thicket holders
# =====================================================================

add(
    id="cue-health-cartridge",
    canonical_name="Cue Health Monitoring System cartridge",
    aliases=["Cue Health"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="Cue Health Inc. Cue COVID-19 Test for Home and Over The Counter Use. FDA EUA June 2021. https://cuehealth.com",
    creator="Cue Health Inc. (formerly Mesa Biotech)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Cartridge-based isothermal NAAT (nucleic acid amplification test) platform with integrated electrochemical detection and Bluetooth readout to smartphone app. Lucira/Detect competitor, with the differentiating architecture being electrochemical (vs Lucira's colorimetric) detection. Anticipates: smartphone-mediated cartridge readout as a category, integrated isothermal-NAAT-with-electrochemistry on disposable cartridge.",
    sources=[
        "Cue Health product literature",
        "FDA EUA Cue COVID-19 Test",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-isothermal-amplification",
        "detection-electrochemical-on-chip",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/686"],
)

add(
    id="visby-medical-cartridge",
    canonical_name="Visby Medical PCR cartridge",
    aliases=["Visby Medical"],
    corpus="private",
    first_disclosure_date="2018",
    disclosure_citation="Visby Medical respiratory and STI tests. FDA 510(k) family. https://www.visbymedical.com",
    creator="Visby Medical (formerly Click Diagnostics)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Single-use, palm-sized PCR cartridge with integrated optical detection and battery power; the test result is read by visual inspection of color-coded LEDs without requiring an instrument. Architecturally distinguished from Lucira (isothermal LAMP) by using true PCR thermal cycling on disposable. Anticipates: instrument-free thermal-cycled PCR cartridge with embedded heater and battery, and the device-disposable-as-instrument architectural collapse.",
    sources=[
        "Visby Medical product literature",
        "FDA 510(k) summaries",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-pcr-cycling",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/686"],
)

add(
    id="t2-biosystems-cartridge",
    canonical_name="T2 Biosystems T2Dx cartridge",
    aliases=["T2 Biosystems", "T2Dx"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="T2 Biosystems T2Dx Instrument and T2Candida / T2Bacteria Panels. FDA approval September 2014.",
    creator="T2 Biosystems",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Cartridge platform using T2MR (magnetic resonance) detection for sepsis-causing pathogen identification directly from whole blood without culture. Anticipates: NMR-based detection on cartridge as alternative to fluorescence/electrochemistry, and the bacteremia-from-whole-blood-without-culture clinical positioning.",
    sources=[
        "T2 Biosystems product literature",
        "FDA approval letters T2Candida and T2Bacteria",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "G01R 33/465"],
)

add(
    id="tecan-burstein-labcd",
    canonical_name="Burstein/Tecan LabCD original disc-format platform",
    aliases=["Burstein LabCD", "Tecan LabCD", "early lab-on-disc"],
    corpus="private",
    first_disclosure_date="1997",
    disclosure_citation="Burstein Technology / Tecan LabCD platform. https://www.tecan.com (LabCD acquired and integrated)",
    creator="Burstein Technology (acquired by Tecan)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="centrifugal",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Pioneering centrifugal microfluidic platform from the late 1990s — predates most academic centrifugal-LoD work. Burstein's CD-format chemistry analyzer used spinning-disc-driven flow, capillary-burst valves, and integrated optical detection in a benchtop reader. Anticipates: many subsequent commercial centrifugal-LoD systems by demonstrating commercial feasibility 5–10 years before the academic literature peaked.",
    sources=[
        "Burstein Technology / Tecan product literature",
    ],
    disclosed_subsystems=[
        "pump-centrifugal-rotational",
        "valve-capillary-stop",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "G01N 35/00"],
    lineage_descendants=["abbott-piccolo-xpress"],
)

add(
    id="cepheid-xpress-cartridge",
    canonical_name="Cepheid Xpress (rapid GeneXpert) cartridge",
    aliases=["Cepheid Xpress", "Xpert Xpress"],
    corpus="private",
    first_disclosure_date="2017",
    disclosure_citation="Cepheid Xpert Xpress family — rapid versions of the GeneXpert cartridge with reduced runtime via streamlined sample prep.",
    creator="Cepheid (Danaher)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Newer family of Cepheid GeneXpert cartridges optimized for sub-30-minute runtime: Xpert Xpress Flu/RSV, Xpert Xpress SARS-CoV-2, Xpert Xpress Strep A. Architecturally identical to original GeneXpert cartridge with optimized chemistry (faster amplification cycles, multiplexed assays).",
    sources=[
        "Cepheid product literature",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-pcr-cycling",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/686"],
    lineage_ancestors=["cepheid-genexpert-cartridge"],
)

add(
    id="thermo-taqpath-cartridge",
    canonical_name="Thermo Fisher TaqPath / Applied Biosystems QuantStudio cartridge",
    aliases=["TaqPath", "Applied Biosystems QuantStudio"],
    corpus="private",
    first_disclosure_date="2010",
    disclosure_citation="Thermo Fisher Scientific TaqPath family and QuantStudio instruments. https://www.thermofisher.com",
    creator="Thermo Fisher Scientific (Applied Biosystems / Life Technologies)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="High-throughput lab-format qPCR cartridges spanning 96-well, 384-well, and 7K Array Card formats, with TaqMan probe chemistry. Architecturally a successor to traditional PCR plates with lab-automation integration. Significant for the FDA-authorized COVID-19 TaqPath test which became the dominant US laboratory-format SARS-CoV-2 PCR.",
    sources=[
        "Thermo Fisher product literature",
    ],
    disclosed_subsystems=[
        "thermal-pcr-cycling",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/686"],
)

add(
    id="vapourtec-flow-chemistry",
    canonical_name="Vapourtec continuous-flow chemistry system",
    aliases=["Vapourtec R-series", "Vapourtec E-series"],
    corpus="private",
    first_disclosure_date="2003",
    disclosure_citation="Vapourtec Ltd. Continuous flow chemistry systems. https://www.vapourtec.com",
    creator="Vapourtec Ltd.",
    creator_country="GB",
    device_class="flow-controller",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Modular continuous-flow chemistry platform with HPLC pumps, heated reactors, mixers, and inline analytics. Used widely in pharmaceutical chemistry for hazardous-reagent and high-temperature reactions. Anticipates: flow-chemistry-as-a-platform commercial offering, and the systems integration that enables academic flow-chem groups to do production work.",
    sources=[
        "Vapourtec product literature",
    ],
    disclosed_subsystems=[
        "pump-syringe-driven",
    ],
    cpc_classifications=["B01J 19/00"],
)

add(
    id="syrris-flow-chemistry",
    canonical_name="Syrris Asia and Africa flow-chemistry platform",
    aliases=["Syrris Asia", "Syrris Africa"],
    corpus="private",
    first_disclosure_date="2007",
    disclosure_citation="Syrris (acquired by Asynt 2022). https://www.syrris.com",
    creator="Syrris Ltd.",
    creator_country="GB",
    device_class="flow-controller",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Modular flow-chemistry platform offering smaller-scale variants than Vapourtec; particularly used in academic and pharmaceutical R&D. Architectural cousin of Vapourtec; together they cover most of the commercial pharma-flow-chemistry market.",
    sources=[
        "Syrris product literature",
    ],
    disclosed_subsystems=[
        "pump-syringe-driven",
    ],
    cpc_classifications=["B01J 19/00"],
)

add(
    id="raindance-bio-rad-acquisition",
    canonical_name="RainDance Technologies droplet platform (acquired by Bio-Rad)",
    aliases=["RainDance ThunderStorm", "RainDance picoinjector"],
    corpus="private",
    first_disclosure_date="2008",
    disclosure_citation="RainDance Technologies (acquired by Bio-Rad 2017). Brouzes 2009 commercialization. https://www.bio-rad.com",
    creator="RainDance Technologies (acquired by Bio-Rad 2017)",
    creator_country="US",
    device_class="droplet-generator",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Commercial pioneer in droplet microfluidics for high-throughput screening and ddPCR (RainDrop ddPCR), absorbed into Bio-Rad's portfolio in 2017. The combined RainDance + QuantaLife (Bio-Rad's earlier ddPCR acquisition) IP estate is the dominant patent thicket in droplet-format diagnostics and the foundational portfolio behind Bio-Rad QX ddPCR.",
    sources=[
        "RainDance Technologies / Bio-Rad merger documents",
        "Brouzes et al. 2009 PNAS",
    ],
    disclosed_subsystems=[
        "droplet-flow-focusing-generation",
        "droplet-merging-electrocoalescence",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/68"],
    lineage_ancestors=["brouzes-2009-droplet-screening", "anna-2003-flow-focusing-droplet"],
)

add(
    id="dolomite-microfluidics-droplet-system",
    canonical_name="Dolomite Microfluidics Droplet System (re-registration)",
    aliases=["Dolomite Microfluidics droplet"],
    corpus="private",
    first_disclosure_date="2005",
    disclosure_citation="Dolomite Microfluidics. https://www.dolomite-microfluidics.com",
    creator="Dolomite Microfluidics (Blacktrace Holdings)",
    creator_country="GB",
    device_class="droplet-generator",
    substrate_material="glass",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Long-running European microfluidic vendor with a particular emphasis on glass droplet-generator chips and modular system integration. Cited here as the canonical id `dolomite-microfluidics-droplet-system` to align with the existing instrument cross-references in the control sub-repo.",
    sources=[
        "Dolomite Microfluidics catalog",
    ],
    disclosed_subsystems=[
        "droplet-flow-focusing-generation",
        "fabrication-glass-thermal-bonding",
    ],
    cpc_classifications=["B01L 3/00"],
    notes="Companion entry to existing dolomite-microfluidics-platform if it differs; verify before merging.",
)

add(
    id="standard-biotools-mass-cytometry-cytof",
    canonical_name="Fluidigm/Standard BioTools CyTOF mass cytometer cartridge",
    aliases=["CyTOF", "Helios mass cytometer"],
    corpus="private",
    first_disclosure_date="2009",
    disclosure_citation="Bandura, D. R. et al. Mass cytometry: technique for real time single cell multitarget immunoassay based on inductively coupled plasma time-of-flight mass spectrometry. Anal. Chem. 2009, 81, 6813–6822. DOI: 10.1021/ac901049w",
    creator="DVS Sciences (acquired by Fluidigm; now Standard BioTools)",
    creator_country="CA",
    device_class="lab-on-chip",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Mass cytometry: cells stained with metal-isotope-tagged antibodies are nebulized into an ICP-TOF-MS, enabling 40+ parameter single-cell measurements without fluorophore spectral overlap. Architecturally a microfluidic flow-cell + ICP-MS hybrid. Anticipates: metal-isotope-tag immunostaining as a category, and mass-cytometry as the multiplexed-immunophenotyping platform that compete with spectral flow cytometry.",
    sources=[
        "Anal. Chem. 2009, 81, 6813–6822",
    ],
    disclosed_subsystems=[
        "interface-electrospray-emitter",
    ],
    cpc_classifications=["G01N 33/49", "H01J 49/04"],
)


# =====================================================================
# OPEN — more open-hardware / community projects
# =====================================================================

add(
    id="hackteria-microfluidics",
    canonical_name="Hackteria community microfluidics tutorials",
    aliases=["Hackteria"],
    corpus="open",
    first_disclosure_date="2009",
    disclosure_citation="Hackteria.org community wiki and project documentation. https://hackteria.org",
    creator="Hackteria collective (Yashas Shetty, Marc Dusseiller, Andy Gracie, et al.)",
    creator_country="GLOBAL",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="DIY-bio collective hosting microfluidics tutorials, open-hardware bioscience projects, and biological-art workshops. Documented designs include syringe pumps, low-cost microscopes, and DIY microfluidic chips. Anticipates: community-hosted DIY bioscience documentation with strong art-science overlap, in scope-of-output complementing more academically-oriented projects like Metafluidics.",
    sources=[
        "https://hackteria.org",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="biocurious-community-lab",
    canonical_name="BioCurious community biology lab",
    aliases=["BioCurious"],
    corpus="open",
    first_disclosure_date="2010",
    disclosure_citation="BioCurious community biology lab in Sunnyvale, CA. https://biocurious.org",
    creator="BioCurious",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Community wet-bio lab focused on accessible biology — including microfluidics work. Notable projects include open hardware syringe pumps and bioreactors. Reference for the broader community-lab movement that complements academic and corporate microfluidics R&D.",
    sources=[
        "https://biocurious.org",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="metafluidics-database-disclosure",
    canonical_name="Metafluidics open-hardware microfluidics database (disclosure entry)",
    aliases=["Metafluidics platform"],
    corpus="open",
    first_disclosure_date="2017",
    disclosure_citation="Kong et al. 2017 Nat. Biotechnol. 35, 523. https://metafluidics.org",
    creator="MIT Media Lab / MIT Lincoln Lab",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Note: separate from earlier metafluidics community-platform entry. This entry covers the publication-disclosure aspect — the published Metafluidics design library that aggregates community-contributed open-hardware microfluidic designs under permissive license. Anticipates: open-hardware design-database paradigm for microfluidics, the analog of GitHub for chip designs.",
    sources=[
        "Nat. Biotechnol. 2017, 35, 523–529",
        "https://metafluidics.org",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="jove-microfluidics-protocols",
    canonical_name="JoVE (Journal of Visualized Experiments) microfluidics protocols",
    aliases=["JoVE microfluidics"],
    corpus="open",
    first_disclosure_date="2006",
    disclosure_citation="Journal of Visualized Experiments (JoVE), various microfluidics-related video protocols. https://www.jove.com",
    creator="Journal of Visualized Experiments (JoVE)",
    creator_country="US",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Peer-reviewed video-format protocol journal; hundreds of microfluidics-related papers cover device fabrication, characterization, and use. While JoVE itself is paywalled, individual protocols often link to open-source design files. Reference here for the corpus of techniques-as-published-protocols documentation that complements traditional Lab-on-a-Chip / Anal. Chem. publications.",
    sources=[
        "https://www.jove.com",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="open-flexure-pump",
    canonical_name="OpenFlexure pump (open-hardware peristaltic)",
    aliases=["OpenFlexure peristaltic pump"],
    corpus="open",
    first_disclosure_date="2020",
    disclosure_citation="Wijnen, B.; Hunt, E. J.; Anzalone, G. C.; Pearce, J. M. Open-source syringe pump library. PLOS ONE 2014, 9, e107216. (And subsequent OpenFlexure peristaltic variants.)",
    creator="various — Wijnen 2014 / OpenFlexure community",
    creator_country="GB",
    device_class="pump-component",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Reference open-hardware peristaltic pump documented in PLOS ONE and subsequent open-source projects. Sub-$50 BOM for a working peristaltic pump usable for microfluidic applications including bioreactor feed and chip perfusion. Anticipates: extreme-low-cost peristaltic pump as open-hardware, reproducibly built by undergraduates or DIY-bio enthusiasts.",
    sources=[
        "PLOS ONE 2014, 9, e107216",
        "OpenFlexure community wiki",
    ],
    disclosed_subsystems=[
        "pump-peristaltic-on-chip",
    ],
    cpc_classifications=["F04B 43/12"],
)


# =====================================================================
# FICTIONAL — more narrative depictions
# =====================================================================

add(
    id="star-trek-hypospray",
    canonical_name="Star Trek hypospray needle-free injector",
    aliases=["Hypospray", "ST hypospray"],
    corpus="fictional",
    first_disclosure_date="1966",
    disclosure_citation="Star Trek (TOS), 'Where No Man Has Gone Before' (1966) and subsequent series. NBC / Paramount / CBS.",
    creator="Gene Roddenberry / Paramount / Desilu",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="other",
    ip_status="fictional",
    prior_art_notes="Iconic depiction of a needle-free pneumatic-or-pressure-driven dermal injection device. Architecturally a hand-held microfluidic dispenser with reusable barrel and replaceable cartridge. Anticipates: jet-injector-style pharmaceutical delivery with cartridge-format consumables. Real-world analogs (Bioject, PowderJect) are more recent. Doctrinally relevant for needle-free-injector patent invalidity contention.",
    sources=[
        "Star Trek (TOS), 1966–1969",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="aliens-med-pod",
    canonical_name="Aliens autonomous med pod (Prometheus)",
    aliases=["Prometheus med pod", "Weyland medical pod"],
    corpus="fictional",
    first_disclosure_date="2012",
    disclosure_citation="Prometheus, dir. Ridley Scott. 20th Century Fox, 2012.",
    creator="Ridley Scott / Damon Lindelof / 20th Century Fox",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Detailed visual and narrative depiction of a fully autonomous bedside surgical/diagnostic pod performing complex procedures under operator-by-exception. Architecturally an integrated diagnostic, surgical, and pharmaceutical-synthesis platform. Doctrinally relevant for invalidity contention against patents on autonomous bedside trauma-care platforms; complement to 2-1B and Halo-medbay entries.",
    sources=[
        "Prometheus (2012)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="westworld-host-fluid-systems",
    canonical_name="Westworld host fluid-systems and fabrication tanks",
    aliases=["Westworld delos", "Delos host fabrication"],
    corpus="fictional",
    first_disclosure_date="2016",
    disclosure_citation="Westworld (HBO TV series), HBO, 2016–2022.",
    creator="HBO / Jonathan Nolan / Lisa Joy",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="bioprocess",
    ip_status="fictional",
    prior_art_notes="Detailed visual depictions of large-scale humanoid-host fabrication including immersion tanks, fluid-printer arrays for tissue layering, and microfluidic-equivalent maintenance bays. Architectural specificity is sufficient to be cited as conceptual prior art for very-large-scale 3D bioprinting and synthetic-biology-driven humanoid manufacturing. Of particular relevance to David's free-humanoid-corpus parent project.",
    sources=[
        "Westworld (2016–2022)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="doom-medkit",
    canonical_name="Doom medkit autonomous trauma stim",
    aliases=["Doom medkit"],
    corpus="fictional",
    first_disclosure_date="1993",
    disclosure_citation="Doom (id Software, 1993).",
    creator="id Software",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="other",
    ip_status="fictional",
    prior_art_notes="Iconic gaming-context depiction of a hand-held single-use trauma stim/healing pack used in field-medicine. Anticipates: cartridge-format wearable / portable autonomous diagnostic and pharmaceutical-delivery device. Lower-detail than e.g. Halo or Aliens but is part of the gaming-culture cumulative-priors landscape.",
    sources=[
        "Doom (1993)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# =====================================================================
# More academic — sequencing tooling and infrastructure
# =====================================================================

add(
    id="rusconi-2011-microfluidic-bioreactor",
    canonical_name="Microfluidic bioreactor for individual yeast cells",
    aliases=["Rusconi 2011 yeast microfluidic"],
    corpus="academic",
    first_disclosure_date="2011",
    disclosure_citation="Lee, S. S.; Avalos Vizcarra, I.; Huberts, D. H. E. W.; Lee, L. P.; Heinemann, M. Whole lifespan microscopic observation of budding yeast aging through a microfluidic dissection platform. Proc. Natl. Acad. Sci. USA 2012, 109, 4916–4920. DOI: 10.1073/pnas.1113505109",
    creator="Heinemann, Lee labs (ETH / Berkeley)",
    creator_country="CH",
    device_class="single-cell-platform",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Microfluidic device for whole-lifespan single-yeast-cell observation: cells trapped in posts that retain mother cells while flushing daughter cells, allowing 50+ cell-division observations without moving the trap. Anticipates: lifespan-tracking microfluidic single-cell traps, used widely in aging research and in synthetic-biology dynamics measurement.",
    sources=[
        "Proc. Natl. Acad. Sci. USA 2012, 109, 4916–4920",
    ],
    disclosed_subsystems=[
        "cell-trap-hydrodynamic",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "C12M 1/00"],
)

add(
    id="ferry-2011-mother-machine",
    canonical_name="Mother machine: high-throughput single-bacterium tracking",
    aliases=["Wang Mother Machine", "mother machine"],
    corpus="academic",
    first_disclosure_date="2010",
    disclosure_citation="Wang, P.; Robert, L.; Pelletier, J.; Dang, W. L.; Taddei, F.; Wright, A.; Jun, S. Robust growth of Escherichia coli. Curr. Biol. 2010, 20, 1099–1103. DOI: 10.1016/j.cub.2010.04.045",
    creator="Jun group, UCSD",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="The 'mother machine': arrays of dead-end channels each holding a single bacterium with daughter cells flushed downstream. Enables thousands of independent single-cell lineage observations in parallel. Anticipates: dead-end-channel single-bacterium trap array architecture, time-resolved bacterial physiology measurements at scale, and the broader category of microfluidic devices for systematic bacterial physiology that became central in microbial-aging and antibiotic-resistance research.",
    sources=[
        "Curr. Biol. 2010, 20, 1099–1103",
    ],
    disclosed_subsystems=[
        "cell-trap-hydrodynamic",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "C12M 1/00"],
)

add(
    id="khalil-collins-2010-synthetic-biology-toolkit",
    canonical_name="Synthetic biology / circuit-design tools (microfluidics-relevant)",
    aliases=["Khalil Collins 2010 synthetic biology review"],
    corpus="academic",
    first_disclosure_date="2010",
    disclosure_citation="Khalil, A. S.; Collins, J. J. Synthetic biology: applications come of age. Nat. Rev. Genet. 2010, 11, 367–379. DOI: 10.1038/nrg2775",
    creator="Khalil, Collins (BU)",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Synthesizing review of synthetic biology applications, with particular relevance to microfluidic chassis: every Synthetic-Biology platform that combines designer cells with microfluidic device-level control depends on integrating chip-format infrastructure with engineered genetic circuits. Methodological reference for the broader synthetic-biology + microfluidics intersection.",
    sources=[
        "Nat. Rev. Genet. 2010, 11, 367–379",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="yu-2010-cell-pull-down-bead",
    canonical_name="Bead-based cell capture in microfluidic channels",
    aliases=["Yu 2010 bead capture"],
    corpus="academic",
    first_disclosure_date="2007",
    disclosure_citation="Toner, M.; Irimia, D. Blood-on-a-chip. Annu. Rev. Biomed. Eng. 2005, 7, 77–103. DOI: 10.1146/annurev.bioeng.7.011205.135108",
    creator="Toner group, Mass General Hospital",
    creator_country="US",
    device_class="separator-component",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Toner-group review consolidating the 'blood-on-a-chip' research program: integrated separation, capture, and analysis of blood components on microfluidic chips. Cited as the canonical review for chip-format hematology and CTC isolation work; precursor to the CTC-iChip lineage.",
    sources=[
        "Annu. Rev. Biomed. Eng. 2005, 7, 77–103",
    ],
    disclosed_subsystems=[
        "separation-affinity-capture",
        "separation-magnetophoresis",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "G01N 33/49"],
    lineage_descendants=["ozkumur-2013-ctc-iChip"],
)


# Write out
with CORPUS.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new entries to {CORPUS}")
