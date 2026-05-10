#!/usr/bin/env python3
"""Expansion seed for free-microfluidics-corpus.

Appends roughly 50 entries to corpus.jsonl covering:
  - inertial microfluidics, acoustofluidics, EWOD/DMF, centrifugal LoD
  - more cartridges (Roche, GenMark, Lucira, OraSure)
  - more inkjet (Epson, Memjet, Xaar, MicroFab)
  - electronics cooling / two-phase microchannels
  - more fictional (Brave New World, Hitchhiker's, Foundation, Star Wars med droid)
  - more patent thicket (Fluidigm, Standard BioTools, ProteinSimple, Mission Bio)
  - 3D-printing variants (CLIP, FRESH, LCM)
  - more open hardware (OpenFlexure, OpenLH, Pumpy, Poseidon, OpenPCR)

Entries are commons-grade unless explicitly flagged draft.
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
# ACADEMIC — major missing foundational and recent papers
# =====================================================================

add(
    id="tuckerman-pease-1981-microchannel-cooling",
    canonical_name="High-performance heat sinking for VLSI (microchannel cooling)",
    aliases=["Tuckerman-Pease microchannel"],
    corpus="academic",
    first_disclosure_date="1981",
    disclosure_citation="Tuckerman, D. B.; Pease, R. F. W. High-performance heat sinking for VLSI. IEEE Electron Device Lett. 1981, 2, 126–129. DOI: 10.1109/EDL.1981.25367",
    creator="Tuckerman, Pease (Stanford)",
    creator_country="US",
    device_class="cooling-substrate",
    substrate_material="silicon",
    fabrication_method="photolithography",
    channel_geometry="50 µm wide × 300 µm deep silicon microchannels at 100 µm pitch, etched directly into VLSI substrate backside",
    flow_regime="pressure-driven",
    end_application="thermal-mgmt",
    ip_status="public-domain",
    prior_art_notes="Foundational disclosure of microchannel single-phase liquid cooling integrated directly into a silicon device backside, demonstrating 790 W/cm² heat removal — a number that defined the performance ceiling for chip cooling for the next 30 years. Anticipates: silicon-microchannel cold plates as integrated VLSI thermal solutions, parallel rectangular microchannels at sub-100-µm scale, water-as-coolant in silicon microfluidics, and the entire embedded-liquid-cooling subfield that resurfaced in the 2010s with EU/DARPA programs (ICECool) and now with on-chip AI accelerators. This paper predates the µTAS framing by a decade.",
    sources=[
        "IEEE Electron Device Lett. 1981, 2, 126–129",
        "DOI 10.1109/EDL.1981.25367",
    ],
    disclosed_subsystems=[
        "thermal-microchannel-cooling-electronics",
        "fabrication-silicon-koh-etching",
    ],
    cpc_classifications=["H01L 23/473", "F28F 3/12"],
    notes="Often forgotten in 'microfluidics' surveys because it's filed under thermal management rather than analytical chemistry. Predates Manz 1990 by nine years and Canon's bubble jet by only two. The first widely cited use of silicon microfluidics for engineering rather than chemistry.",
)

add(
    id="di-carlo-2007-inertial-microfluidics",
    canonical_name="Continuous inertial focusing, ordering, and separation of particles in microchannels",
    aliases=["Di Carlo 2007 inertial focusing"],
    corpus="academic",
    first_disclosure_date="2007",
    disclosure_citation="Di Carlo, D.; Irimia, D.; Tompkins, R. G.; Toner, M. Continuous inertial focusing, ordering, and separation of particles in microchannels. Proc. Natl. Acad. Sci. USA 2007, 104, 18892–18897. DOI: 10.1073/pnas.0704958104",
    creator="Di Carlo, Toner et al. (Harvard / Mass General)",
    creator_country="US",
    device_class="separator-component",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="analytical",
    ip_status="patented",
    ip_citations=["US8186913B2", "US8784012B2"],
    prior_art_notes="Established inertial microfluidics as a continuous-flow particle-separation regime exploiting Dean drag and shear-gradient lift in curving and straight channels at intermediate Reynolds numbers (Re~10–100). Anticipates: spiral and serpentine inertial focusing geometries, label-free CTC enrichment by inertial migration, sheath-free particle ordering, and the entire inertial-microfluidics subfield as commercialized by Vortex Biosciences, ClearCell, and the iCellate / iChip CTC platforms. Together with Sturm/Huang DLD (2004) it defines the dominant label-free continuous-separation paradigms.",
    sources=[
        "Proc. Natl. Acad. Sci. USA 2007, 104, 18892–18897",
        "DOI 10.1073/pnas.0704958104",
    ],
    disclosed_subsystems=[
        "separation-inertial-focusing",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "G01N 15/02"],
    lineage_descendants=["ozkumur-2013-ctc-iChip"],
)

add(
    id="ozkumur-2013-ctc-iChip",
    canonical_name="CTC-iChip: inertial focusing for high-throughput rare-cell isolation",
    aliases=["CTC-iChip", "Ozkumur 2013"],
    corpus="academic",
    first_disclosure_date="2013",
    disclosure_citation="Ozkumur, E.; Shah, A. M.; Ciciliano, J. C.; Emmink, B. L.; Miyamoto, D. T.; Brachtel, E.; Yu, M.; Chen, P.-i.; Morgan, B.; Trautwein, J.; Kimura, A.; Sengupta, S.; Stott, S. L.; Karabacak, N. M.; Barber, T. A.; Walsh, J. R.; Smith, K.; Spuhler, P. S.; Sullivan, J. P.; Lee, R. J.; Ting, D. T.; Luo, X.; Shaw, A. T.; Bardia, A.; Sequist, L. V.; Louis, D. N.; Maheswaran, S.; Kapur, R.; Haber, D. A.; Toner, M. Inertial focusing for tumor antigen-dependent and -independent sorting of rare circulating tumor cells. Sci. Transl. Med. 2013, 5, 179ra47. DOI: 10.1126/scitranslmed.3005616",
    creator="Toner / Maheswaran / Haber labs (Mass General)",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    throughput="10^7 cells/min",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US9090663B2 (and family)"],
    prior_art_notes="Translational descendant of Di Carlo 2007 demonstrating clinical-grade circulating tumor cell isolation by combining hydrodynamic size-based debulking, inertial focusing into a single streamline, and immunomagnetic deflection in series. Anticipates: integrated multi-modal CTC-isolation cartridge architecture, sheath-flow whole-blood debulking with leukocyte depletion, and antigen-independent rare-cell capture as a clinical workflow. Direct ancestor of multiple commercial CTC platforms.",
    sources=[
        "Sci. Transl. Med. 2013, 5, 179ra47",
        "DOI 10.1126/scitranslmed.3005616",
    ],
    disclosed_subsystems=[
        "separation-inertial-focusing",
        "separation-magnetophoresis",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "G01N 33/49"],
    lineage_ancestors=["di-carlo-2007-inertial-microfluidics", "huang-2004-dld-deterministic-lateral-displacement"],
)

add(
    id="laurell-2007-acoustophoresis",
    canonical_name="Free-flow acoustophoresis for cell separation",
    aliases=["Laurell acoustophoresis"],
    corpus="academic",
    first_disclosure_date="2007",
    disclosure_citation="Petersson, F.; Åberg, L.; Swärd-Nilsson, A.-M.; Laurell, T. Free flow acoustophoresis: microfluidic-based mode of particle and cell separation. Anal. Chem. 2007, 79, 5117–5123. DOI: 10.1021/ac070444e",
    creator="Laurell group, Lund University",
    creator_country="SE",
    device_class="separator-component",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="acoustic",
    end_application="analytical",
    ip_status="patented",
    ip_citations=["US8865003B2", "WO2007024485A2"],
    prior_art_notes="Foundational disclosure of free-flow acoustophoresis: continuous-flow particle separation in a microchannel by transverse acoustic radiation force from a half-wavelength bulk acoustic standing wave, with sample inlet and multiple outlets at distinct lateral positions. Anticipates: silicon-channel BAW resonator architecture, label-free continuous acoustic separation by particle compressibility / density contrast, and the entire bulk-acoustic-wave acoustofluidics field commercialized by AcouSort and used in dozens of academic CTC and exosome platforms.",
    sources=[
        "Anal. Chem. 2007, 79, 5117–5123",
        "DOI 10.1021/ac070444e",
    ],
    disclosed_subsystems=[
        "separation-acoustophoresis",
        "fabrication-silicon-drie",
        "fabrication-glass-anodic-bonding",
    ],
    cpc_classifications=["B01L 3/00", "G01N 15/02"],
)

add(
    id="ding-2012-saw-acoustic-tweezers",
    canonical_name="Standing surface acoustic wave (SSAW) acoustic tweezers",
    aliases=["Ding 2012 SAW tweezers", "Huang acoustic tweezers"],
    corpus="academic",
    first_disclosure_date="2012",
    disclosure_citation="Ding, X.; Lin, S.-C. S.; Kiraly, B.; Yue, H.; Li, S.; Chiang, I.-K.; Shi, J.; Benkovic, S. J.; Huang, T. J. On-chip manipulation of single microparticles, cells, and organisms using surface acoustic waves. Proc. Natl. Acad. Sci. USA 2012, 109, 11105–11109. DOI: 10.1073/pnas.1209288109",
    creator="T. J. Huang group, Penn State / Duke",
    creator_country="US",
    device_class="separator-component",
    substrate_material="hybrid",
    fabrication_method="photolithography",
    channel_geometry="PDMS channel on lithium niobate piezoelectric substrate with patterned interdigital transducers (IDTs)",
    flow_regime="acoustic",
    end_application="research",
    ip_status="patented",
    ip_citations=["US9606086B2"],
    prior_art_notes="Disclosed SSAW (standing surface acoustic wave) micromanipulation of cells and microparticles in a PDMS channel atop a lithium niobate substrate with paired IDTs. Anticipates: IDT-on-LiNbO3 SSAW architecture for sub-mm patterning of pressure nodes in solution, individually addressable cell trapping by SAW phase shifting, and the SAW microfluidics paradigm that competes with Laurell-style BAW. Underlies most subsequent SAW-based cell-separation papers.",
    sources=[
        "Proc. Natl. Acad. Sci. USA 2012, 109, 11105–11109",
        "DOI 10.1073/pnas.1209288109",
    ],
    disclosed_subsystems=[
        "separation-acoustophoresis",
        "cell-trap-acoustic-streaming-vortex",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "G01N 15/02"],
)

add(
    id="pollack-2000-electrowetting-droplet",
    canonical_name="Electrowetting-based actuation of liquid droplets for microfluidic applications",
    aliases=["Pollack 2000 EWOD"],
    corpus="academic",
    first_disclosure_date="2000",
    disclosure_citation="Pollack, M. G.; Fair, R. B.; Shenderov, A. D. Electrowetting-based actuation of liquid droplets for microfluidic applications. Appl. Phys. Lett. 2000, 77, 1725–1726. DOI: 10.1063/1.1308534",
    creator="Pollack, Fair, Shenderov (Duke)",
    creator_country="US",
    device_class="digital-microfluidics",
    substrate_material="glass",
    fabrication_method="photolithography",
    channel_geometry="planar electrode array on glass with dielectric and hydrophobic coating, paired top plate, ~700 µm electrode pitch",
    flow_regime="digital-droplet",
    end_application="research",
    ip_status="patented",
    ip_citations=["US6565727B1", "US6911132B2 (and Duke EWOD family)"],
    prior_art_notes="The foundational disclosure of electrowetting-on-dielectric (EWOD) for digital microfluidics. Demonstrated discrete water-droplet transport across an addressable electrode array under voltage control. Anticipates: addressable-electrode array DMF architecture, DC + AC EWOD actuation modes, droplet-merge / droplet-split / droplet-dispense as primitives, and the Advanced Liquid Logic / Illumina commercial DMF lineage. Together with Cho 2003 it defines the EWOD field.",
    sources=[
        "Appl. Phys. Lett. 2000, 77, 1725–1726",
        "DOI 10.1063/1.1308534",
    ],
    disclosed_subsystems=[
        "dmf-electrowetting-on-dielectric",
        "dmf-addressable-electrode-array",
        "valve-electrowetting",
    ],
    cpc_classifications=["B01L 3/00", "G02B 26/005"],
)

add(
    id="cho-2003-creating-transporting-cutting-merging",
    canonical_name="Creating, transporting, cutting, and merging liquid droplets by electrowetting-based actuation",
    aliases=["Cho 2003 EWOD"],
    corpus="academic",
    first_disclosure_date="2003",
    disclosure_citation="Cho, S. K.; Moon, H.; Kim, C.-J. Creating, transporting, cutting, and merging liquid droplets by electrowetting-based actuation for digital microfluidic circuits. J. Microelectromech. Syst. 2003, 12, 70–80. DOI: 10.1109/JMEMS.2002.807467",
    creator="C.-J. Kim group, UCLA",
    creator_country="US",
    device_class="digital-microfluidics",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="digital-droplet",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Companion foundational paper to Pollack 2000, expanding the primitive set of EWOD operations from transport to creation, cutting, and merging — i.e., the full droplet-circuit calculus. Anticipates: complete DMF instruction set (dispense, transport, split, merge), and the framing of DMF as 'digital microfluidic circuits' analogous to digital electronic circuits.",
    sources=[
        "J. Microelectromech. Syst. 2003, 12, 70–80",
        "DOI 10.1109/JMEMS.2002.807467",
    ],
    disclosed_subsystems=[
        "dmf-electrowetting-on-dielectric",
        "dmf-addressable-electrode-array",
        "droplet-merging-electrocoalescence",
        "droplet-splitting-bifurcation",
    ],
    cpc_classifications=["B01L 3/00"],
    lineage_ancestors=["pollack-2000-electrowetting-droplet"],
)

add(
    id="madou-2006-centrifugal-microfluidics",
    canonical_name="Lab-on-a-CD: centrifugal microfluidics platform",
    aliases=["LabCD", "centrifugal lab-on-disc"],
    corpus="academic",
    first_disclosure_date="2006",
    disclosure_citation="Madou, M.; Zoval, J.; Jia, G.; Kido, H.; Kim, J.; Kim, N. Lab on a CD. Annu. Rev. Biomed. Eng. 2006, 8, 601–628. DOI: 10.1146/annurev.bioeng.8.061505.095758",
    creator="Madou group, UC Irvine (and earlier Burstein/Tecan)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="centrifugal",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Comprehensive review and synthesis of centrifugal microfluidics: pumping by spin-rate-controlled centrifugal force, valving by capillary-burst pressure thresholds, mixing by Coriolis-aided shaking, and assay sequencing by sequential burst-frequency design. Anticipates: lab-on-disc architecture, capillary-burst valves with threshold rotational frequencies, pumping-as-rotation as a substitute for external pressure, and the commercial pathway commercialized by Gyros (immunoassays), Samsung (Genio), Roche (cobas Liat traces architectural lineage). Among the few papers covering an entire substantive class of microfluidic device.",
    sources=[
        "Annu. Rev. Biomed. Eng. 2006, 8, 601–628",
        "DOI 10.1146/annurev.bioeng.8.061505.095758",
    ],
    disclosed_subsystems=[
        "pump-centrifugal-rotational",
        "valve-burst-frangible",
        "valve-capillary-stop",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "G01N 35/00"],
)

add(
    id="dertinger-2001-christmas-tree-gradient",
    canonical_name="Generation of gradients having complex shapes using microfluidic networks",
    aliases=["Christmas tree gradient generator", "Dertinger 2001"],
    corpus="academic",
    first_disclosure_date="2001",
    disclosure_citation="Dertinger, S. K. W.; Chiu, D. T.; Jeon, N. L.; Whitesides, G. M. Generation of gradients having complex shapes using microfluidic networks. Anal. Chem. 2001, 73, 1240–1246. DOI: 10.1021/ac001132d",
    creator="Whitesides group, Harvard",
    creator_country="US",
    device_class="mixer-component",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Disclosed the iconic 'Christmas tree' splitting-and-recombining microfluidic network for arbitrary-shape concentration gradient generation. Anticipates: branched diffusion-mixer cascade for gradient generation, parallel-channel concentration gradient as a primitive in chemotaxis assays, and the gradient-generator microfluidic motif appearing in hundreds of subsequent cell-biology papers.",
    sources=[
        "Anal. Chem. 2001, 73, 1240–1246",
        "DOI 10.1021/ac001132d",
    ],
    disclosed_subsystems=[
        "mixer-passive-split-recombine",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01F 33/30", "B01L 3/00"],
    lineage_ancestors=["duffy-1998-pdms-soft-lithography-microfluidics"],
)

add(
    id="beebe-2000-stop-flow",
    canonical_name="Stop-flow lithography and Beebe geometry",
    aliases=["Beebe 2000 hydrogel valves"],
    corpus="academic",
    first_disclosure_date="2000",
    disclosure_citation="Beebe, D. J.; Moore, J. S.; Bauer, J. M.; Yu, Q.; Liu, R. H.; Devadoss, C.; Jo, B.-H. Functional hydrogel structures for autonomous flow control inside microfluidic channels. Nature 2000, 404, 588–590. DOI: 10.1038/35007047",
    creator="Beebe group (UIUC / Wisconsin)",
    creator_country="US",
    device_class="valve-component",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed pH-responsive hydrogel structures photopatterned in situ inside microchannels to act as autonomous valves and chemostat-like sensors. Anticipates: in-channel photopolymerized hydrogel valves, stimulus-responsive autonomous flow regulation, and the entire 'smart hydrogel' microfluidics subfield. Among the most-cited microfluidics papers and a foundational primitive distinct from Quake-style pneumatic valves.",
    sources=[
        "Nature 2000, 404, 588–590",
        "DOI 10.1038/35007047",
    ],
    disclosed_subsystems=[
        "valve-thermal-paraffin",
        "fabrication-pdms-soft-lithography",
        "fabrication-su8-photoresist",
    ],
    cpc_classifications=["F16K 99/00", "B01L 3/00"],
    notes="The valve mechanism is hydrogel-swelling rather than thermal-paraffin; tagged with the closest existing taxonomy element until a hydrogel-specific tag is added.",
)

add(
    id="squires-quake-2005-review",
    canonical_name="Microfluidics: fluid physics at the nanoliter scale",
    aliases=["Squires Quake 2005"],
    corpus="academic",
    first_disclosure_date="2005",
    disclosure_citation="Squires, T. M.; Quake, S. R. Microfluidics: fluid physics at the nanoliter scale. Rev. Mod. Phys. 2005, 77, 977–1026. DOI: 10.1103/RevModPhys.77.977",
    creator="Squires (UCSB), Quake (Caltech / Stanford)",
    creator_country="US",
    device_class="other",
    flow_regime="mixed",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="The canonical theoretical review of microfluidic fluid physics: low-Reynolds-number scaling, electrokinetic phenomena, surface tension at small scales, mixing in laminar flow, two-phase flow physics. Cited as the textbook reference in essentially every theoretical microfluidics paper since. Doesn't disclose specific devices but establishes the analytical framework that every subsequent device sits inside.",
    sources=[
        "Rev. Mod. Phys. 2005, 77, 977–1026",
        "DOI 10.1103/RevModPhys.77.977",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
    notes="No subsystem tags; this is a methods/review entry whose value is the consolidated framework, not a specific subsystem disclosure.",
)

add(
    id="whitesides-2007-origins-future-microfluidics",
    canonical_name="The origins and the future of microfluidics",
    aliases=["Whitesides 2007 Nature review"],
    corpus="academic",
    first_disclosure_date="2007",
    disclosure_citation="Whitesides, G. M. The origins and the future of microfluidics. Nature 2006, 442, 368–373. DOI: 10.1038/nature05058",
    creator="George Whitesides, Harvard",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Whitesides's history-and-prospects review identifying the four progenitor fields of microfluidics (analytical chemistry, biodefense, molecular biology, microelectronics). Cited as the standard origin-story reference. Does not disclose new devices but establishes the field's intellectual genealogy.",
    sources=[
        "Nature 2006, 442, 368–373",
        "DOI 10.1038/nature05058",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="thorsen-2002-microfluidic-large-scale-integration",
    canonical_name="Microfluidic large-scale integration",
    aliases=["MLSI", "Thorsen 2002 LSI"],
    corpus="academic",
    first_disclosure_date="2002",
    disclosure_citation="Thorsen, T.; Maerkl, S. J.; Quake, S. R. Microfluidic large-scale integration. Science 2002, 298, 580–584. DOI: 10.1126/science.1076996",
    creator="Quake group, Caltech",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    channel_geometry="3,574 valves and 1,000 individually addressable chambers in 25 mm² area; multilayer PDMS",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US7144616B1 (and Quake LSI family)"],
    prior_art_notes="Demonstrated 'microfluidic large-scale integration' — thousands of Quake valves operated as binary multiplexers to address hundreds of chambers from a few control lines. The conceptual analog of VLSI for microfluidics. Anticipates: hierarchical valve multiplexing for chamber-array addressing (n chambers from O(log n) control lines), and the architectural model that underlies Fluidigm IFCs and most chip-scale microfluidic automation. Companion to Unger 2000 valve disclosure; together they define MLSI.",
    sources=[
        "Science 2002, 298, 580–584",
        "DOI 10.1126/science.1076996",
    ],
    disclosed_subsystems=[
        "valve-quake-pneumatic-membrane",
        "fabrication-pdms-soft-lithography",
        "fabrication-multilayer-lamination",
    ],
    cpc_classifications=["B01L 3/00"],
    lineage_ancestors=["unger-2000-quake-monolithic-membrane-valve"],
)

add(
    id="brouzes-2009-droplet-screening",
    canonical_name="Droplet microfluidic technology for single-cell high-throughput screening",
    aliases=["Brouzes 2009 droplet HTS"],
    corpus="academic",
    first_disclosure_date="2009",
    disclosure_citation="Brouzes, E.; Medkova, M.; Savenelli, N.; Marran, D.; Twardowski, M.; Hutchison, J. B.; Rothberg, J. M.; Link, D. R.; Perrimon, N.; Samuels, M. L. Droplet microfluidic technology for single-cell high-throughput screening. Proc. Natl. Acad. Sci. USA 2009, 106, 14195–14200. DOI: 10.1073/pnas.0903542106",
    creator="RainDance Technologies / Perrimon lab",
    creator_country="US",
    device_class="droplet-generator",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    throughput="kHz droplet sorting throughput",
    end_application="research",
    ip_status="patented",
    ip_citations=["various RainDance patents (acquired by Bio-Rad)"],
    prior_art_notes="Established droplet microfluidics for single-cell HTS by combining flow-focusing droplet generation, on-droplet barcoding, fluorescence-activated droplet sorting (FADS), and downstream analysis. Anticipates: barcoded droplet libraries for combinatorial screening, droplet sorting at kHz rates with electrocoalescence, and the directed-evolution / single-cell-screen workflows commercialized by RainDance and absorbed into Bio-Rad's portfolio.",
    sources=[
        "Proc. Natl. Acad. Sci. USA 2009, 106, 14195–14200",
        "DOI 10.1073/pnas.0903542106",
    ],
    disclosed_subsystems=[
        "droplet-flow-focusing-generation",
        "droplet-sorting-fluorescence-activated",
        "droplet-merging-electrocoalescence",
        "architecture-droplet-library-screening",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/68"],
    lineage_ancestors=["anna-2003-flow-focusing-droplet"],
)

add(
    id="klein-2015-indrops",
    canonical_name="inDrops: droplet-based barcoding for single-cell transcriptomics",
    aliases=["inDrops"],
    corpus="academic",
    first_disclosure_date="2015",
    disclosure_citation="Klein, A. M.; Mazutis, L.; Akartuna, I.; Tallapragada, N.; Veres, A.; Li, V.; Peshkin, L.; Weitz, D. A.; Kirschner, M. W. Droplet barcoding for single-cell transcriptomics applied to embryonic stem cells. Cell 2015, 161, 1187–1201. DOI: 10.1016/j.cell.2015.04.044",
    creator="Klein, Weitz, Kirschner labs (Harvard)",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Published one week after Drop-seq; together they establish single-cell droplet RNA-seq as a category. inDrops uses hydrogel-encapsulated barcodes (rather than Drop-seq's polystyrene beads), an architectural choice subsequently inherited by 1Cell-Bio's commercial inDrops platform. Both papers anticipate: massively parallel single-cell RNA-seq via droplet co-encapsulation, but with different bead chemistries that anchor distinct patent positions.",
    sources=[
        "Cell 2015, 161, 1187–1201",
        "DOI 10.1016/j.cell.2015.04.044",
    ],
    disclosed_subsystems=[
        "droplet-flow-focusing-generation",
        "cell-encapsulation-droplet",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["C12Q 1/68", "B01L 3/00"],
    lineage_ancestors=["anna-2003-flow-focusing-droplet"],
)

add(
    id="tumbleston-2015-clip-3d-printing",
    canonical_name="CLIP: continuous liquid interface production",
    aliases=["CLIP", "Carbon CLIP"],
    corpus="academic",
    first_disclosure_date="2015",
    disclosure_citation="Tumbleston, J. R.; Shirvanyants, D.; Ermoshkin, N.; Janusziewicz, R.; Johnson, A. R.; Kelly, D.; Chen, K.; Pinschmidt, R.; Rolland, J. P.; Ermoshkin, A.; Samulski, E. T.; DeSimone, J. M. Continuous liquid interface production of 3D objects. Science 2015, 347, 1349–1352. DOI: 10.1126/science.aaa2397",
    creator="DeSimone group (UNC) / Carbon Inc.",
    creator_country="US",
    device_class="printer-tooling",
    substrate_material="other",
    fabrication_method="dlp-sla",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US9216546B2", "US10618215B2 (Carbon CLIP family)"],
    prior_art_notes="Disclosed continuous liquid interface production: an oxygen-permeable membrane creates a 'dead zone' of inhibited polymerization at the build window, enabling continuous (rather than layered) DLP-SLA printing. Anticipates: oxygen-inhibition-mediated continuous photopolymerization, dead-zone window architecture for SLA, and the Carbon Inc. commercial platform that turned SLA into a production-scale process.",
    sources=[
        "Science 2015, 347, 1349–1352",
        "DOI 10.1126/science.aaa2397",
    ],
    disclosed_subsystems=[
        "fabrication-dlp-sla-enclosed-channels",
    ],
    cpc_classifications=["B33Y 10/00", "B29C 64/124"],
)

add(
    id="kelly-2019-cal-volumetric-printing",
    canonical_name="Computed axial lithography (CAL): volumetric 3D printing",
    aliases=["CAL", "Kelly 2019 volumetric"],
    corpus="academic",
    first_disclosure_date="2019",
    disclosure_citation="Kelly, B. E.; Bhattacharya, I.; Heidari, H.; Shusteff, M.; Spadaccini, C. M.; Taylor, H. K. Volumetric additive manufacturing via tomographic reconstruction. Science 2019, 363, 1075–1079. DOI: 10.1126/science.aau7114",
    creator="Taylor group, UC Berkeley / LLNL",
    creator_country="US",
    device_class="printer-tooling",
    substrate_material="other",
    fabrication_method="dlp-sla",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["WO2018208378A1", "US20200147889A1"],
    prior_art_notes="Disclosed computed axial lithography (CAL): volumetric 3D printing by superimposing multi-angle 2D light projections on a rotating photoresin volume to deliver a polymerization-threshold dose at every voxel of the target geometry simultaneously. Anticipates: tomographic-reconstruction-based volumetric printing, sample-rotation architecture, threshold-dose accumulation as the print mechanism. Direct ancestor of DISH (Wang 2026) which inverts the rotation onto a periscope and adds holographic synthesis.",
    sources=[
        "Science 2019, 363, 1075–1079",
        "DOI 10.1126/science.aau7114",
    ],
    disclosed_subsystems=[
        "fabrication-volumetric-3d-printing",
    ],
    cpc_classifications=["B33Y 10/00", "B29C 64/124"],
    lineage_descendants=["wang-2026-dish-volumetric-3d-printing"],
)

add(
    id="hinton-2015-fresh-printing",
    canonical_name="FRESH: freeform reversible embedding of suspended hydrogels",
    aliases=["FRESH"],
    corpus="academic",
    first_disclosure_date="2015",
    disclosure_citation="Hinton, T. J.; Jallerat, Q.; Palchesko, R. N.; Park, J. H.; Grodzicki, M. S.; Shue, H.-J.; Ramadan, M. H.; Hudson, A. R.; Feinberg, A. W. Three-dimensional printing of complex biological structures by freeform reversible embedding of suspended hydrogels. Sci. Adv. 2015, 1, e1500758. DOI: 10.1126/sciadv.1500758",
    creator="Feinberg group, Carnegie Mellon",
    creator_country="US",
    device_class="printer-tooling",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed FRESH: extrusion 3D printing of soft hydrogel structures into a thixotropic gelatin support bath that holds the soft material until thermal release. Anticipates: support-bath-stabilized soft-material 3D printing, biocompatible scaffold printing for tissue engineering, and the FluidForm commercial bioprinting platform. Architecturally adjacent to organ-on-chip vasculature manufacturing.",
    sources=[
        "Sci. Adv. 2015, 1, e1500758",
        "DOI 10.1126/sciadv.1500758",
    ],
    disclosed_subsystems=[
        "architecture-organ-on-chip-vasculature",
    ],
    cpc_classifications=["B29C 64/00", "B33Y 10/00"],
)

add(
    id="reizman-2015-self-optimizing-flow",
    canonical_name="Self-optimizing continuous flow chemistry",
    aliases=["Reizman 2015"],
    corpus="academic",
    first_disclosure_date="2015",
    disclosure_citation="Reizman, B. J.; Wang, Y.-M.; Buchwald, S. L.; Jensen, K. F. Suzuki–Miyaura cross-coupling optimization enabled by automated feedback. React. Chem. Eng. 2016, 1, 658–666. DOI: 10.1039/C6RE00153J",
    creator="Jensen group, MIT / Buchwald, MIT",
    creator_country="US",
    device_class="flow-controller",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Disclosed automated feedback-controlled flow chemistry combining continuous flow microreactors, inline analytics (HPLC), and Bayesian-style optimization to autonomously identify reaction conditions. Anticipates: closed-loop autonomous reaction optimization, AI-controlled microfluidic process analytical technology (PAT), and the entire 'self-driving labs' framing that became a major area of automated discovery research.",
    sources=[
        "React. Chem. Eng. 2016, 1, 658–666",
        "DOI 10.1039/C6RE00153J",
    ],
    disclosed_subsystems=[
        "architecture-process-analytical-technology",
    ],
    cpc_classifications=["B01J 19/00"],
)

add(
    id="lab-on-chip-mehling-tay-review",
    canonical_name="Microfluidic cell culture review",
    aliases=["Mehling Tay 2014 review"],
    corpus="academic",
    first_disclosure_date="2014",
    disclosure_citation="Mehling, M.; Tay, S. Microfluidic cell culture. Curr. Opin. Biotechnol. 2014, 25, 95–102. DOI: 10.1016/j.copbio.2013.10.005",
    creator="Tay group, ETH Zurich",
    creator_country="CH",
    device_class="organ-on-chip",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Concise review of microfluidic cell culture establishing the design principles that distinguish cell-culture chips from chemistry chips: surface chemistry compatibility, perfusion timescales matching biological time constants, gas exchange, and avoiding shear-induced cell stress. Cited as a methods reference for organ-on-chip work.",
    sources=[
        "Curr. Opin. Biotechnol. 2014, 25, 95–102",
        "DOI 10.1016/j.copbio.2013.10.005",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
    ],
    cpc_classifications=["C12M 1/00"],
)

add(
    id="boom-1990-silica-magnetic-extraction",
    canonical_name="Boom guanidinium-silica nucleic acid extraction",
    aliases=["Boom method", "guanidinium silica extraction"],
    corpus="academic",
    first_disclosure_date="1990",
    disclosure_citation="Boom, R.; Sol, C. J. A.; Salimans, M. M. M.; Jansen, C. L.; van Dillen, P. M. E.; van der Noordaa, J. Rapid and simple method for purification of nucleic acids. J. Clin. Microbiol. 1990, 28, 495–503.",
    creator="Boom et al., University of Amsterdam",
    creator_country="NL",
    device_class="other",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US5234809A (Boom)"],
    prior_art_notes="Disclosed guanidinium-silica nucleic acid extraction chemistry that, while not microfluidic on its own, became the dominant on-cartridge sample-prep chemistry across virtually every commercial molecular diagnostic cartridge (BioFire, Cepheid, Abbott, Roche, GenMark). Included in the corpus because cartridge architectural disclosures cannot be evaluated without recognizing this as the standard nucleic-acid-prep chemistry they all integrate.",
    sources=[
        "J. Clin. Microbiol. 1990, 28, 495–503",
    ],
    disclosed_subsystems=[
        "separation-affinity-capture",
    ],
    cpc_classifications=["C12N 15/10"],
    notes="Not microfluidic in the strict sense, but every cartridge-format molecular diagnostic that integrates sample prep depends on this chemistry. Including it makes cartridge prior-art chains traceable.",
)

add(
    id="sackmann-2014-microfluidics-medicine-review",
    canonical_name="The present and future role of microfluidics in biomedical research",
    aliases=["Sackmann 2014 Nature review"],
    corpus="academic",
    first_disclosure_date="2014",
    disclosure_citation="Sackmann, E. K.; Fulton, A. L.; Beebe, D. J. The present and future role of microfluidics in biomedical research. Nature 2014, 507, 181–189. DOI: 10.1038/nature13118",
    creator="Beebe group, Wisconsin",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Beebe-group review surveying microfluidics-in-biomedicine adoption barriers, particularly the gap between academic demonstration and clinical implementation. Cited as the canonical reference for the 'why hasn't microfluidics taken over diagnostics yet' question. Methodological — establishes the framing rather than disclosing devices.",
    sources=[
        "Nature 2014, 507, 181–189",
        "DOI 10.1038/nature13118",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="hou-2013-acoustic-cell-trapping",
    canonical_name="Acoustic-streaming microvortex cell trap",
    aliases=["Hou 2013 acoustic vortex", "Lee group oscillating bubble trap"],
    corpus="academic",
    first_disclosure_date="2009",
    disclosure_citation="Wang, C.; Jalikop, S. V.; Hilgenfeldt, S. Size-sensitive sorting of microparticles through control of flow geometry. Appl. Phys. Lett. 2011, 99, 034101. DOI: 10.1063/1.3610940 (and earlier Lee/Hilgenfeldt work)",
    creator="Hilgenfeldt group / A. Lee group (UCI)",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="acoustic",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Established oscillating air-liquid interface as a microstreaming-vortex cell trap: a piezoactuated chip drives oscillation of trapped bubbles, which generate steady-streaming microvortices that capture cells. Direct architectural ancestor of the AESOP work (Zhang 2026) which uses the same trap mechanism for sequential transfection. Anticipates: bubble-driven steady-streaming microvortex cell trap as a primitive.",
    sources=[
        "Appl. Phys. Lett. 2011, 99, 034101",
        "DOI 10.1063/1.3610940",
    ],
    disclosed_subsystems=[
        "cell-trap-acoustic-streaming-vortex",
        "pump-acoustic-streaming",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00"],
    lineage_descendants=["zhang-2026-aesop-acoustic-electric-poration"],
)

add(
    id="franssila-2010-paper-fluidic-pcl",
    canonical_name="Wax-printed paper microfluidics for low-cost diagnostics",
    aliases=["Carrilho 2009 wax printing"],
    corpus="academic",
    first_disclosure_date="2009",
    disclosure_citation="Carrilho, E.; Martinez, A. W.; Whitesides, G. M. Understanding wax printing: a simple micropatterning process for paper-based microfluidics. Anal. Chem. 2009, 81, 7091–7095. DOI: 10.1021/ac901071p",
    creator="Whitesides group, Harvard",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="public-domain",
    prior_art_notes="Disclosed wax printing as a sub-$0.10/device fabrication path for paper microfluidics: a commodity solid-ink printer deposits wax patterns that, after melting, reflow vertically through paper to create hydrophobic barriers defining channels. Anticipates: wax-as-hydrophobic-barrier as a paper microfluidic fabrication primitive, low-cost disposable diagnostic manufacturing without specialized equipment, and the entire post-2009 paper-microfluidic literature.",
    sources=[
        "Anal. Chem. 2009, 81, 7091–7095",
        "DOI 10.1021/ac901071p",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
        "material-paper-cellulose",
    ],
    cpc_classifications=["B01L 3/00"],
    lineage_ancestors=["martinez-2007-paper-microfluidics"],
)


# =====================================================================
# PRIVATE — more cartridges, instruments, patent-thicket holders
# =====================================================================

add(
    id="roche-cobas-liat-cartridge",
    canonical_name="Roche cobas Liat point-of-care cartridge",
    aliases=["cobas Liat", "IQuum"],
    corpus="private",
    first_disclosure_date="2009",
    disclosure_citation="IQuum (later acquired by Roche) cobas Liat system. FDA 510(k) K123251 (2014) for influenza assay. https://diagnostics.roche.com/global/en/products/instruments/cobas-liat.html",
    creator="IQuum (acquired by Roche 2014)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    channel_geometry="flexible-tube format with sequential pinch-valve compartments and integrated PCR amplification segment",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US7494770B2", "US8470588B2", "(IQuum patent family)"],
    prior_art_notes="Disclosed a flexible-tube cartridge format with sequential compartments separated by external pinch valves, allowing reagent staging and PCR thermal cycling without rigid microfluidic channels. Anticipates: flex-tube-as-microfluidic-substrate, external-pinch-valve actuation as substitute for on-chip valves, and the architectural simplification of POC molecular diagnostics by eliminating injection-molded fluidic complexity.",
    sources=[
        "Roche cobas Liat product literature",
        "IQuum / Roche patent family",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-pcr-cycling",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/686"],
)

add(
    id="genmark-eplex-cartridge",
    canonical_name="GenMark ePlex cartridge",
    aliases=["ePlex", "GenMark Diagnostics ePlex"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="GenMark Diagnostics (now Roche) ePlex system. FDA 510(k) K161312 and family. https://www.genmarkdx.com/eplex/",
    creator="GenMark Diagnostics (acquired by Roche 2021)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US8425861B2", "US9075042B2 (and GenMark family)"],
    prior_art_notes="Disclosed a multiplex molecular diagnostic cartridge integrating sample prep, PCR amplification, and electrochemical detection on a printed gold electrode array (eSensor technology). Anticipates: electrochemical-array detection as alternative to optical fluorescence in syndromic POC molecular diagnostics, and the architectural pattern of integrating eSensor-style detection within a self-contained cartridge.",
    sources=[
        "GenMark / Roche product literature",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "architecture-multiplex-cartridge",
        "thermal-pcr-cycling",
        "detection-electrochemical-on-chip",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/686"],
)

add(
    id="lucira-home-covid-test",
    canonical_name="Lucira Health Check It home COVID-19 isothermal molecular test",
    aliases=["Lucira Check It", "Lucira COVID home test"],
    corpus="private",
    first_disclosure_date="2020",
    disclosure_citation="Lucira Health Check It / All-In-One COVID-19 Test Kit. FDA EUA December 2020 (first FDA-authorized at-home molecular COVID-19 test). https://www.fda.gov/media/143810/download",
    creator="Lucira Health (acquired by Pfizer 2023)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US10941394B2", "US11268130B2 (Lucira patent family)"],
    prior_art_notes="The first FDA-authorized at-home molecular COVID-19 test, demonstrating that LAMP isothermal amplification + colorimetric readout could be packaged into a fully self-contained $50-class disposable. Anticipates: complete self-contained battery-powered isothermal molecular diagnostic at consumer price points, integrated colorimetric readout without optical instrumentation, and the architectural collapse of the molecular diagnostics stack from $30k cartridge readers to single-use disposables.",
    sources=[
        "Lucira Health product literature",
        "FDA EUA letter for Lucira COVID-19 All-In-One Test Kit",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "thermal-isothermal-amplification",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/686"],
)

add(
    id="orasure-quickflex-cartridge",
    canonical_name="OraSure rapid HIV test cassette (lateral flow)",
    aliases=["OraQuick", "OraSure lateral flow"],
    corpus="private",
    first_disclosure_date="1995",
    disclosure_citation="OraSure Technologies OraQuick rapid HIV-1/2 antibody test. FDA approval 2002 (in-vitro use), 2012 (over-the-counter). https://www.orasure.com",
    creator="OraSure Technologies",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Lateral flow immunoassay cartridge — the architectural ancestor of all subsequent rapid antigen tests including pregnancy tests, COVID rapid antigen, and dozens of others. Anticipates: nitrocellulose lateral-flow membrane format, capillary-driven assay with conjugate pad and capture line, and the entire commercial point-of-care antigen-test product category.",
    sources=[
        "OraSure product literature",
        "FDA OraQuick approval letter",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
        "material-paper-cellulose",
    ],
    cpc_classifications=["G01N 33/543", "B01L 3/00"],
    notes="Lateral flow predates the µTAS framing and the academic 'paper microfluidics' work (Martinez 2007); architecturally it is the same primitive applied to immunoassay rather than analytical chemistry.",
)

add(
    id="fluidigm-dynamic-array-ifc",
    canonical_name="Fluidigm Dynamic Array Integrated Fluidic Circuit",
    aliases=["IFC", "Fluidigm BioMark", "Standard BioTools IFC"],
    corpus="private",
    first_disclosure_date="2003",
    disclosure_citation="Fluidigm Corp. (now Standard BioTools) Integrated Fluidic Circuit / Dynamic Array. https://www.standardbio.com/products/instruments-and-consumables and Fluidigm IFC patent family.",
    creator="Fluidigm Corp. (now Standard BioTools)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    channel_geometry="9,216 to 96 × 96 reaction-chamber arrays in monolithic PDMS with thousands of Quake valves",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US7144616B1 (Quake LSI)", "US7494555B2", "(Fluidigm IFC family)"],
    prior_art_notes="Commercial implementation of Quake / Thorsen MLSI (microfluidic large-scale integration) for high-throughput qPCR, single-cell qPCR, and digital PCR. Anticipates: direct architectural lineage from Unger 2000 + Thorsen 2002 to commercial multi-thousand-well qPCR arrays. The corpus exists in part because of the IP positions Fluidigm built around this architecture.",
    sources=[
        "Standard BioTools (Fluidigm) product literature",
    ],
    disclosed_subsystems=[
        "valve-quake-pneumatic-membrane",
        "fabrication-pdms-soft-lithography",
        "fabrication-multilayer-lamination",
        "thermal-pcr-cycling",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/686"],
    lineage_ancestors=["unger-2000-quake-monolithic-membrane-valve", "thorsen-2002-microfluidic-large-scale-integration"],
)

add(
    id="proteinsimple-westernblot-simple-western",
    canonical_name="Bio-Techne / ProteinSimple Simple Western (capillary western)",
    aliases=["Simple Western", "ProteinSimple WES", "Jess"],
    corpus="private",
    first_disclosure_date="2011",
    disclosure_citation="Bio-Techne ProteinSimple Simple Western platform. https://www.bio-techne.com/p/simple-western/wes",
    creator="ProteinSimple (acquired by Bio-Techne)",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="hybrid",
    fabrication_method="other",
    channel_geometry="capillary-format separation channel with UV-immobilization step and immunodetection",
    flow_regime="electrokinetic",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Capillary-format automated western blot replacement: protein separation by SDS capillary electrophoresis, UV-induced covalent immobilization to capillary wall, antibody probing, and chemiluminescence detection — all on a single instrument with disposable capillary cartridges. Anticipates: capillary-immobilization westerns, automated multi-step immunodetection on a microfluidic-equivalent capillary substrate, and the broader trend of replacing manual molecular biology bench protocols with cartridge-format automation.",
    sources=[
        "Bio-Techne ProteinSimple product literature",
    ],
    disclosed_subsystems=[
        "separation-capillary-electrophoresis",
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["G01N 27/447", "G01N 33/68"],
)

add(
    id="mission-bio-tapestri",
    canonical_name="Mission Bio Tapestri single-cell DNA sequencing",
    aliases=["Tapestri"],
    corpus="private",
    first_disclosure_date="2018",
    disclosure_citation="Mission Bio Tapestri platform. https://missionbio.com/tapestri/",
    creator="Mission Bio",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Two-step droplet workflow for single-cell DNA sequencing: cells encapsulated, lysed, and tagged in primary droplets; PCR products extracted and re-emulsified for amplicon sequencing. Anticipates: serial-emulsion architecture in single-cell genomics workflows, distinguishing Mission Bio's IP position from 10x Genomics' single-emulsion approach.",
    sources=[
        "Mission Bio Tapestri product literature",
    ],
    disclosed_subsystems=[
        "droplet-flow-focusing-generation",
        "cell-encapsulation-droplet",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["C12Q 1/68", "B01L 3/00"],
)

add(
    id="epson-microPiezo-printhead",
    canonical_name="Epson MicroPiezo printhead (piezoelectric drop-on-demand)",
    aliases=["MicroPiezo", "Epson piezo printhead"],
    corpus="private",
    first_disclosure_date="1993",
    disclosure_citation="Seiko Epson MicroPiezo printhead, originally introduced 1993 (Epson MJ-500 / Stylus Color). Patent family includes US5402162.",
    creator="Seiko Epson",
    creator_country="JP",
    device_class="inkjet-printhead",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="industrial",
    ip_status="patented",
    ip_citations=["US5402162", "US5736993"],
    prior_art_notes="Piezoelectric drop-on-demand inkjet printhead: a piezo actuator deflects a chamber wall, ejecting a droplet through a microfabricated nozzle. Architectural complement to Canon/HP thermal-bubble-jet — same droplet-on-demand outcome via a different physical mechanism. Anticipates: piezo-stack DOD printhead architecture as the dominant industrial inkjet technology (3D bioprinters, OLED displays, semiconductor-grade pattern printing), and the piezoelectric-disc pump category broadly.",
    sources=[
        "Epson MicroPiezo product literature",
        "US5402162",
    ],
    disclosed_subsystems=[
        "pump-piezoelectric-stack",
        "droplet-on-demand",
    ],
    cpc_classifications=["B41J 2/14", "B41J 2/045"],
)

add(
    id="memjet-printhead",
    canonical_name="Memjet thermal silicon-MEMS printhead",
    aliases=["Memjet"],
    corpus="private",
    first_disclosure_date="2007",
    disclosure_citation="Memjet (Silverbrook Research) printhead architecture. https://memjet.com",
    creator="Memjet (Silverbrook Research)",
    creator_country="AU",
    device_class="inkjet-printhead",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="industrial",
    ip_status="patented",
    prior_art_notes="High-density thermal-bubble-jet printhead with ~70,000 nozzles per page-wide module on a single silicon MEMS die. Anticipates: page-wide-array thermal-inkjet architecture, sub-200 µm nozzle pitch on silicon, and integrated drive electronics + nozzle-plate co-fabrication.",
    sources=[
        "Memjet product literature",
    ],
    disclosed_subsystems=[
        "pump-thermal-bubble-jet",
        "droplet-on-demand",
    ],
    cpc_classifications=["B41J 2/14"],
)

add(
    id="microfab-piezo-droplet-dispenser",
    canonical_name="MicroFab piezo droplet dispenser (industrial)",
    aliases=["MicroFab MJ-AT"],
    corpus="private",
    first_disclosure_date="1995",
    disclosure_citation="MicroFab Technologies piezo dispenser product line. https://www.microfab.com",
    creator="MicroFab Technologies",
    creator_country="US",
    device_class="dispenser-pipettor",
    substrate_material="glass",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="industrial",
    ip_status="patented",
    prior_art_notes="Industrial piezo droplet dispenser (single-droplet to MHz rates, 10 pL to 1 nL droplet volumes) used for protein arrays, microbiology spotting, electronics manufacturing, and pharmaceutical formulation. Anticipates: piezo-glass-capillary droplet generator as a discrete instrument-grade primitive (as opposed to consumer printhead arrays), and laboratory automation for low-volume liquid handling.",
    sources=[
        "MicroFab product literature",
    ],
    disclosed_subsystems=[
        "pump-piezoelectric-stack",
        "droplet-on-demand",
    ],
    cpc_classifications=["B41J 2/045", "B01L 3/02"],
)

add(
    id="advanced-liquid-logic-illumina-dmf",
    canonical_name="Advanced Liquid Logic / Illumina NeoPrep digital microfluidics",
    aliases=["NeoPrep", "ALL", "Advanced Liquid Logic"],
    corpus="private",
    first_disclosure_date="2007",
    disclosure_citation="Advanced Liquid Logic (acquired by Illumina 2013). NeoPrep system launched 2014.",
    creator="Advanced Liquid Logic (acquired by Illumina)",
    creator_country="US",
    device_class="digital-microfluidics",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="digital-droplet",
    end_application="research",
    ip_status="patented",
    ip_citations=["US7815871B2", "US8137917B2 (Pollack/Duke licensed family)"],
    prior_art_notes="Commercial implementation of EWOD digital microfluidics for nucleic acid library preparation, automating a previously manual NGS sample-prep workflow on a disposable EWOD cartridge. The platform was discontinued by Illumina in 2017 but the IP position survives. Anticipates: EWOD as commercial NGS sample-prep automation, and the disposable-cartridge form factor for DMF.",
    sources=[
        "Illumina NeoPrep product literature (archived)",
        "Pollack/Duke EWOD patent family",
    ],
    disclosed_subsystems=[
        "dmf-electrowetting-on-dielectric",
        "dmf-addressable-electrode-array",
    ],
    cpc_classifications=["B01L 3/00", "C12Q 1/68"],
    lineage_ancestors=["pollack-2000-electrowetting-droplet"],
)

add(
    id="gyros-bioaffy-cd",
    canonical_name="Gyros Bioaffy CD immunoassay platform",
    aliases=["Gyros Bioaffy", "Gyrolab"],
    corpus="private",
    first_disclosure_date="2002",
    disclosure_citation="Gyros (now Gyros Protein Technologies) Bioaffy / Gyrolab system. https://www.gyrosproteintechnologies.com",
    creator="Gyros AB (Sweden)",
    creator_country="SE",
    device_class="lab-on-chip",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="centrifugal",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Centrifugal microfluidic immunoassay platform on injection-molded CD-format substrate. Disposable CDs contain hundreds of parallel affinity-column-format immunoassays driven by spin-rate-controlled centrifugal pumping and capillary-burst valves. Anticipates: lab-on-disc immunoassay architecture, parallel column-format affinity assays under centrifugal flow, and CD-format consumable economics.",
    sources=[
        "Gyros Protein Technologies product literature",
    ],
    disclosed_subsystems=[
        "pump-centrifugal-rotational",
        "valve-capillary-stop",
        "valve-burst-frangible",
        "separation-affinity-capture",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00", "G01N 33/53"],
    lineage_ancestors=["madou-2006-centrifugal-microfluidics"],
)

add(
    id="ttp-mirus",
    canonical_name="TTP Mirus / Sphere Fluidics droplet picoinjector",
    aliases=["picoinjector"],
    corpus="private",
    first_disclosure_date="2010",
    disclosure_citation="Abate, A. R.; Hung, T.; Mary, P.; Agresti, J. J.; Weitz, D. A. High-throughput injection with microfluidics using picoinjectors. Proc. Natl. Acad. Sci. USA 2010, 107, 19163–19166. DOI: 10.1073/pnas.1006888107",
    creator="Weitz lab (Harvard); commercialized by Sphere Fluidics",
    creator_country="US",
    device_class="droplet-generator",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Microfluidic picoinjector: introduces a precise volume of reagent into pre-formed droplets at >10 kHz rates by combining electrocoalescence with a side-channel injection orifice. Anticipates: post-formation droplet reagent injection as a primitive, and the multi-step droplet workflow architectures used in commercial directed-evolution and single-cell screening platforms.",
    sources=[
        "Proc. Natl. Acad. Sci. USA 2010, 107, 19163–19166",
        "DOI 10.1073/pnas.1006888107",
    ],
    disclosed_subsystems=[
        "droplet-merging-electrocoalescence",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00"],
)

add(
    id="microfluidic-chipshop-fluidic-chips",
    canonical_name="microfluidic ChipShop standard glass and thermoplastic chips",
    aliases=["microfluidic ChipShop", "Chipshop chips"],
    corpus="private",
    first_disclosure_date="2002",
    disclosure_citation="microfluidic ChipShop GmbH product catalog. https://www.microfluidic-chipshop.com",
    creator="microfluidic ChipShop GmbH",
    creator_country="DE",
    device_class="lab-on-chip",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="trade-secret",
    prior_art_notes="Long-running European microfluidic-chip vendor offering standardized glass and thermoplastic chips and custom contract fabrication. Architecturally similar to Dolomite; significant role in the European academic and industrial market. Catalog includes droplet generators, mixers, separators, organ-on-chip mounts, and standardized formats. The catalog itself is prior art for many specific geometries.",
    sources=[
        "microfluidic ChipShop catalog",
    ],
    disclosed_subsystems=[
        "fabrication-glass-thermal-bonding",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["B01L 3/00"],
)


# =====================================================================
# OPEN — open-hardware microfluidics
# =====================================================================

add(
    id="poseidon-syringe-pump",
    canonical_name="Poseidon open-source syringe pump",
    aliases=["Poseidon"],
    corpus="open",
    first_disclosure_date="2018",
    disclosure_citation="Booeshaghi, A. S. et al. Poseidon: a 3D printed syringe pump system for low-cost microfluidics. HardwareX 2019, 6, e00074. DOI: 10.1016/j.ohx.2019.e00074",
    creator="Pachter lab, Caltech",
    creator_country="US",
    device_class="flow-controller",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="open-permissive",
    ip_citations=["MIT license; https://github.com/pachterlab/poseidon"],
    prior_art_notes="Disclosed an open-source 3D-printed syringe pump system for microfluidics, BOM under $400, with Arduino-based control firmware. Anticipates: open-hardware-instrumentation pattern for the syringe-pump category, replacing $1k–$5k commercial single-channel syringe pumps with sub-$500 community-buildable equivalents.",
    sources=[
        "HardwareX 2019, 6, e00074",
        "DOI 10.1016/j.ohx.2019.e00074",
        "https://github.com/pachterlab/poseidon",
    ],
    disclosed_subsystems=[
        "pump-syringe-driven",
    ],
    cpc_classifications=["F04B 13/00", "B01L 3/02"],
)

add(
    id="openpcr-thermal-cycler",
    canonical_name="OpenPCR open-source thermal cycler",
    aliases=["OpenPCR"],
    corpus="open",
    first_disclosure_date="2010",
    disclosure_citation="OpenPCR project, Tito Jankowski / Josh Perfetto. https://openpcr.org",
    creator="OpenPCR (Chai Biotech founders)",
    creator_country="US",
    device_class="flow-controller",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Open-source desktop thermal cycler ($600 BOM, $599 kit) with full schematics and firmware released under permissive license. Anticipates: open-hardware thermal cycler architecture, prosumer-grade molecular biology instrumentation outside institutional purchase channels, and the broader category of open-source life-science instruments. Predates Arduino-microbiology by a few years.",
    sources=[
        "OpenPCR project pages",
        "GitHub mirrors of original release",
    ],
    disclosed_subsystems=[
        "thermal-pcr-cycling",
    ],
    cpc_classifications=["C12Q 1/686", "B01L 7/00"],
)

add(
    id="openflexure-microscope",
    canonical_name="OpenFlexure Microscope",
    aliases=["OpenFlexure"],
    corpus="open",
    first_disclosure_date="2016",
    disclosure_citation="Sharkey, J. P.; Foo, D. C. W.; Kabla, A.; Baumberg, J. J.; Bowman, R. W. A one-piece 3D printed flexure translation stage for open-source microscopy. Rev. Sci. Instrum. 2016, 87, 025104. DOI: 10.1063/1.4941068",
    creator="Bowman group, Bath / Cambridge",
    creator_country="GB",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Open-source 3D-printable microscope with sub-100-nm resolution flexure stage. Anticipates: 3D-printed flexure-stage architecture for sub-µm positioning, open-hardware microscopy as a category, and the integration of microfluidic chip imaging with low-cost open instrumentation.",
    sources=[
        "Rev. Sci. Instrum. 2016, 87, 025104",
        "DOI 10.1063/1.4941068",
        "https://openflexure.org",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["G02B 21/00"],
)

add(
    id="openlh-liquid-handler",
    canonical_name="OpenLH open-source liquid handler",
    aliases=["OpenLH"],
    corpus="open",
    first_disclosure_date="2018",
    disclosure_citation="Gerber, L. C.; Calasanz-Kaiser, A.; Hyman, L.; Voitiuk, K.; Patil, U.; Riedel-Kruse, I. H. Liquid-handling Lego robots and experiments for STEM education and research. PLOS Biol. 2018, 16, e2007413. DOI: 10.1371/journal.pbio.2007413",
    creator="Riedel-Kruse group, Stanford",
    creator_country="US",
    device_class="dispenser-pipettor",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Open-source liquid-handling robot built from EV3 Lego components, demonstrating that lab automation is accessible at sub-$1000 price points. Anticipates: low-cost prosumer liquid-handling robotics, hobbyist-grade laboratory automation, and the architectural pattern of treating commercial Lego/Open-source components as legitimate scientific instruments.",
    sources=[
        "PLOS Biol. 2018, 16, e2007413",
        "DOI 10.1371/journal.pbio.2007413",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["B01L 9/00"],
)

add(
    id="opentrons-ot2",
    canonical_name="Opentrons OT-2 liquid handler",
    aliases=["OT-2", "Opentrons"],
    corpus="open",
    first_disclosure_date="2018",
    disclosure_citation="Opentrons OT-2 platform; firmware and host software open-source under Apache 2.0. https://opentrons.com and https://github.com/Opentrons/opentrons",
    creator="Opentrons Labworks",
    creator_country="US",
    device_class="dispenser-pipettor",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="open-permissive",
    ip_citations=["Apache-2.0 (firmware/software); commercial hardware sold by Opentrons"],
    prior_art_notes="Commercial-but-open laboratory automation platform combining a $5k–$10k liquid-handling robot with fully open-source firmware and Python control library. Anticipates: programmable laboratory automation at academic-budget price points, Python-as-protocol-language for biological experiments, and the hybrid open-source-software / commercial-hardware business model that has worked for laboratory automation.",
    sources=[
        "Opentrons product literature",
        "https://github.com/Opentrons/opentrons",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["B01L 9/00"],
)

add(
    id="ufluidix-pumpy",
    canonical_name="Pumpy peristaltic pump (open-hardware)",
    aliases=["Pumpy", "uFluidix Pumpy"],
    corpus="open",
    first_disclosure_date="2017",
    disclosure_citation="Pumpy peristaltic pump open-source design. https://github.com/pumpy",
    creator="Pumpy community / uFluidix",
    creator_country="CA",
    device_class="pump-component",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Open-hardware peristaltic pump design with 3D-printable mechanical parts and Arduino control firmware. Sub-$100 BOM. Anticipates: prosumer peristaltic-pump category, with Arduino + stepper motor + 3D-printed roller assembly as standard architecture.",
    sources=[
        "Pumpy GitHub repository and community documentation",
    ],
    disclosed_subsystems=[
        "pump-peristaltic-on-chip",
    ],
    cpc_classifications=["F04B 43/12"],
)

add(
    id="glia-microfluidics-low-resource",
    canonical_name="Glia Project low-resource microfluidic devices (otoscope, etc.)",
    aliases=["Glia"],
    corpus="open",
    first_disclosure_date="2015",
    disclosure_citation="Glia Project. https://glia.org and Niemeyer / Loubani publications.",
    creator="Glia Project (Tarek Loubani et al.)",
    creator_country="CA",
    device_class="point-of-care-cartridge",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="open-permissive",
    prior_art_notes="Open-source medical hardware project including diagnostic devices, otoscopes, tourniquets, and (in development) microfluidic POC tests, all designed for low-resource and humanitarian deployment. Anticipates: open-hardware paradigm for FDA-equivalent regulated medical devices, deployable in conflict zones and low-resource settings, including microfluidic diagnostics released under permissive license.",
    sources=[
        "Glia Project website and publications",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["A61B 5/00"],
)


# =====================================================================
# FICTIONAL — more narrative depictions
# =====================================================================

add(
    id="brave-new-world-bokanovsky-process",
    canonical_name="Brave New World Bokanovsky-process embryo hatchery",
    aliases=["Bokanovsky's Process", "Central London Hatchery"],
    corpus="fictional",
    first_disclosure_date="1932",
    disclosure_citation="Huxley, A. Brave New World. Chatto & Windus, London, 1932.",
    creator="Aldous Huxley",
    creator_country="GB",
    device_class="fictional-laboratory",
    end_application="bioprocess",
    ip_status="fictional",
    prior_art_notes="Detailed narrative depiction of an industrialized embryo-cultivation facility with continuous-flow conveyor processing, in vitro fertilization at scale, and parallel automation of human reproductive biology. Predates IVF by 46 years and modern bioreactor design by decades. Doctrinally relevant for invalidity contention against patents claiming 'industrial-scale automated parallel cell culture' as a generic category.",
    sources=[
        "Huxley, A. Brave New World. 1932.",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-on-chip-incubator",
    ],
    cpc_classifications=[],
)

add(
    id="hitchhikers-nutrimat-drink-machine",
    canonical_name="Hitchhiker's Nutri-Matic Drinks Synthesizer",
    aliases=["Nutri-Matic"],
    corpus="fictional",
    first_disclosure_date="1979",
    disclosure_citation="Adams, D. The Hitchhiker's Guide to the Galaxy. Pan Books, London, 1979.",
    creator="Douglas Adams",
    creator_country="GB",
    device_class="fictional-laboratory",
    flow_regime="passive",
    end_application="other",
    ip_status="fictional",
    prior_art_notes="Narrative depiction of a personalized beverage-synthesis device that performs spectroscopic analysis of the user's neurological state and generates a beverage matched to their physiological needs. Anticipates: closed-loop biochemical analysis + on-demand reagent synthesis as a consumer-grade automated chemistry platform.",
    sources=[
        "Adams, D. The Hitchhiker's Guide to the Galaxy. 1979.",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="star-wars-2-1b-medical-droid",
    corpus="fictional",
    canonical_name="Star Wars 2-1B medical droid",
    aliases=["2-1B", "Two-Onebee"],
    first_disclosure_date="1980",
    disclosure_citation="The Empire Strikes Back, dir. Irvin Kershner, Lucasfilm, 1980.",
    creator="Lucasfilm",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="diagnostic",
    ip_status="fictional",
    prior_art_notes="Narrative depiction of a free-standing autonomous medical robot performing surgical and diagnostic operations, including the prosthetic-limb fitting in Empire Strikes Back. Doctrinally relevant for invalidity contention against patents claiming 'autonomous bedside diagnostic and therapeutic robotic systems' as a category.",
    sources=[
        "The Empire Strikes Back (1980)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="seveneves-stratosphere-microfluidic-lab",
    canonical_name="Seveneves orbital microfluidic biology suite",
    aliases=["Seveneves Cradle"],
    corpus="fictional",
    first_disclosure_date="2015",
    disclosure_citation="Stephenson, N. Seveneves. William Morrow, New York, 2015.",
    creator="Neal Stephenson",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="research",
    ip_status="fictional",
    prior_art_notes="Detailed narrative depiction of microfluidic-equivalent biological research and reproductive support in the cramped volume of the Cradle/Endurance habitats post-Earth-loss. Architecturally specific enough to anticipate compact integrated microfluidic biological-support systems for space-constrained applications including spacecraft and undersea habitats.",
    sources=[
        "Stephenson, N. Seveneves. 2015.",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="diaspora-polis-physiology",
    canonical_name="Diaspora polis physiological substrate",
    aliases=["Konishi polis"],
    corpus="fictional",
    first_disclosure_date="1997",
    disclosure_citation="Egan, G. Diaspora. Orion Publishing, London, 1997.",
    creator="Greg Egan",
    creator_country="AU",
    device_class="fictional-laboratory",
    end_application="other",
    ip_status="fictional",
    prior_art_notes="Hard-SF depiction of physical-substrate microfluidic-equivalent technologies sustaining flesh bodies in pre-upload polis environments. Egan's work is typical of the genre's tendency to specify enough mechanism to function as conceptual prior art for future patent claims, particularly in the long-term life-support and synthetic-biology adjacencies.",
    sources=[
        "Egan, G. Diaspora. 1997.",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# Write out
with CORPUS.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new entries to {CORPUS}")
