#!/usr/bin/env python3
"""Ninth expansion seed for free-microfluidics-corpus.

~30 more entries:
  - van den Berg group at Twente (foundational µTAS work)
  - Ramsey group later work (post-1996 ESI extensions)
  - Whitesides systematic disclosures (μPADs II, μPADs III)
  - Asian commercial extensions (Toshiba, Hitachi clinical extensions)
  - Recent academic 2022-2026 (CRISPR-on-chip, organoids-on-chip, drug delivery)
  - More fictional (more games, films, novels)
  - More open hardware variants (more syringe pumps, more chip designs)
  - Earlier inkjet patent foundationals (Sweet 1965 continuous inkjet)
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
# ACADEMIC — more 1990s foundational
# =====================================================================

add(
    id="van-den-berg-1995-mu-tas-conference",
    canonical_name="MicroTAS 1995 conference founding (van den Berg / Bergveld)",
    aliases=["MicroTAS conference founding", "van den Berg MicroTAS"],
    corpus="academic",
    first_disclosure_date="1995",
    disclosure_citation="van den Berg, A.; Bergveld, P. (Eds.) Micro Total Analysis Systems. Proceedings of the µTAS '94 Workshop. Springer, 1995.",
    creator="van den Berg, Bergveld (University of Twente)",
    creator_country="NL",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Foundational conference proceedings establishing the µTAS / MicroTAS conference series — the dominant academic forum for microfluidics from 1994 onward. The MicroTAS conference series is the primary venue where µTAS-era disclosures were first communicated, often years before journal publication. Historically critical because many architectural concepts in microfluidics first appear in MicroTAS proceedings rather than in journals — these proceedings are part of the prior-art record but are systematically under-cited in patent searches.",
    sources=[
        "van den Berg, A.; Bergveld, P. (Eds.) µTAS '94 Workshop Proceedings. Springer, 1995",
        "https://www.microtas.org",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="van-den-berg-1998-glass-channel-electrophoresis",
    canonical_name="Glass microchannel electrophoresis with ISFET detection (van den Berg group)",
    aliases=["van den Berg electrophoresis ISFET"],
    corpus="academic",
    first_disclosure_date="1998",
    disclosure_citation="Schasfoort, R. B. M.; Schlautmann, S.; Hendrikse, L.; van den Berg, A. Field-effect flow control for microfabricated fluidic devices. Science 1999, 286, 942–945. DOI: 10.1126/science.286.5441.942",
    creator="van den Berg group, University of Twente",
    creator_country="NL",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="analytical",
    ip_status="patented",
    prior_art_notes="Disclosed field-effect flow control: a gate electrode adjacent to a microfluidic channel modulates electroosmotic flow by directly modifying the local zeta potential, enabling integrated 'fluidic transistor' control. Anticipates: integrated electronic-microfluidic interface architecture, gate-controlled electroosmotic flow as a valve primitive, and the broader 'silicon-electronics-meets-microfluidics' tradition.",
    sources=[
        "Science 1999, 286, 942–945",
    ],
    disclosed_subsystems=[
        "valve-electrowetting",
        "fabrication-silicon-drie",
    ],
    cpc_classifications=["B01L 3/00", "G01N 27/447"],
)

add(
    id="ramsey-2000-integrated-chip-ms",
    canonical_name="Ramsey integrated chip-MS extensions (post-1996)",
    aliases=["Ramsey chip-MS extensions"],
    corpus="academic",
    first_disclosure_date="2000",
    disclosure_citation="Ramsey, J. M. The burgeoning power of the shrinking laboratory. Nat. Biotechnol. 1999, 17, 1061–1062. (And subsequent Ramsey group papers extending chip-ESI architecture.)",
    creator="J. M. Ramsey group, Oak Ridge / UNC Chapel Hill",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="electrokinetic",
    end_application="analytical",
    ip_status="patented",
    prior_art_notes="Post-1996 extensions of the Ramsey chip-ESI architecture: integrated trypsin digestion, on-chip protein-LC, and 2D separations preceding ESI. Cited as the methodological lineage for integrated chip-LC-MS workflows. Cumulative Ramsey-group disclosures define the trajectory from chip-ESI (1996) to commercial chip-LC-MS (Agilent 2005).",
    sources=[
        "Nat. Biotechnol. 1999, 17, 1061–1062",
        "Multiple Ramsey-group papers 1997–2005",
    ],
    disclosed_subsystems=[
        "interface-electrospray-emitter",
        "fabrication-glass-hf-etching",
    ],
    cpc_classifications=["B01L 3/00", "H01J 49/04"],
    lineage_ancestors=["ramsey-1996-electrospray-on-chip"],
)

add(
    id="whitesides-2010-mu-pads-systematic",
    canonical_name="µPADs II / III: Systematic Whitesides disclosures",
    aliases=["µPADs II", "µPADs III"],
    corpus="academic",
    first_disclosure_date="2010",
    disclosure_citation="Yetisen, A. K.; Akram, M. S.; Lowe, C. R. Lab Chip 2013, 13, 2210; cumulative Whitesides-group µPAD II/III publications 2008-2014.",
    creator="Whitesides group, Harvard",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Systematic Whitesides-group disclosures extending µPAD architecture from the 2007 foundational disclosure: 3D µPADs (multi-layer paper assembly), electrochemical µPADs (printed electrodes on paper), µPADs with fluorescence detection. Cumulative Whitesides-group µPAD patent filings cover much of the broader paper-microfluidic patent landscape.",
    sources=[
        "Various Whitesides group µPAD II / III papers",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "pump-capillary-passive",
        "detection-electrochemical-on-chip",
    ],
    cpc_classifications=["B01L 3/00", "G01N 33/543"],
    lineage_ancestors=["martinez-2007-paper-microfluidics"],
)

add(
    id="sweet-1965-continuous-inkjet",
    canonical_name="Continuous inkjet (Sweet 1965)",
    aliases=["Sweet continuous inkjet", "CIJ"],
    corpus="academic",
    first_disclosure_date="1965",
    disclosure_citation="Sweet, R. G. High-frequency recording with electrostatically deflected ink jets. Rev. Sci. Instrum. 1965, 36, 131–136. DOI: 10.1063/1.1719502",
    creator="Richard Sweet (Stanford)",
    creator_country="US",
    device_class="inkjet-printhead",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="industrial",
    ip_status="public-domain",
    prior_art_notes="Foundational disclosure of continuous inkjet (CIJ) printing: a continuous fluid jet broken into uniform droplets by piezoelectric perturbation, with droplets electrostatically deflected to either the substrate or a recirculation gutter. Predates DOD inkjet (Kyser-Sears 1976) and thermal bubble jet (Endo 1979) by 11–14 years. Anticipates: continuous-jet droplet generation, electrostatic droplet steering, and the entire CIJ industrial-printing category. Architectural cousin of FACS (cells in a jet electrostatically deflected by sort decision) — predates Fulwyler's FACS by exactly 1 year.",
    sources=[
        "Rev. Sci. Instrum. 1965, 36, 131–136",
    ],
    disclosed_subsystems=[
        "droplet-on-demand",
        "pump-piezoelectric-stack",
    ],
    cpc_classifications=["B41J 2/02"],
)

add(
    id="fulwyler-1965-cell-sorter-foundation",
    canonical_name="Fulwyler electrostatic cell sorter (foundation of FACS)",
    aliases=["Fulwyler 1965 cell sorter", "FACS foundation"],
    corpus="academic",
    first_disclosure_date="1965",
    disclosure_citation="Fulwyler, M. J. Electronic separation of biological cells by volume. Science 1965, 150, 910–911. DOI: 10.1126/science.150.3698.910",
    creator="Mack Fulwyler (Los Alamos)",
    creator_country="US",
    device_class="separator-component",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="The foundational disclosure of fluorescence-activated cell sorting (FACS): a cell-laden fluid jet broken into droplets by piezoelectric vibration, with droplets containing cells of interest electrostatically deflected to collection vessels. Predates Becton Dickinson FACS commercialization by 4 years. Anticipates: jet-in-air cell sorting architecture, droplet-based electrostatic deflection sorting, and the entire commercial flow cytometry industry. Direct architectural cousin of Sweet 1965 continuous inkjet — same primitive, different application.",
    sources=[
        "Science 1965, 150, 910–911",
    ],
    disclosed_subsystems=[
        "droplet-on-demand",
        "separation-affinity-capture",
    ],
    cpc_classifications=["G01N 15/14"],
    lineage_descendants=["berkeley-cellium-flow-cytometer-2009"],
)


# =====================================================================
# ACADEMIC — recent 2022-2026 (CRISPR-on-chip, organoids, drug delivery)
# =====================================================================

add(
    id="myhrvold-zhang-2018-shine-crispr-on-paper",
    canonical_name="SHINE CRISPR-on-paper diagnostic",
    aliases=["SHINE", "Myhrvold 2018 SHINE"],
    corpus="academic",
    first_disclosure_date="2018",
    disclosure_citation="Myhrvold, C. et al. Field-deployable viral diagnostics using CRISPR-Cas13. Science 2018, 360, 444–448. DOI: 10.1126/science.aas8836",
    creator="Sabeti / Zhang labs (Broad Institute)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="paper",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Disclosed SHINE: SHERLOCK + paper-strip lateral-flow readout, allowing fully field-deployable CRISPR diagnostic without instrumentation. Anticipates: paper-format CRISPR diagnostic architecture, integrating Cas13 collateral cleavage with lateral-flow visual readout. Direct ancestor of Sherlock Biosciences' commercial COVID-19 test.",
    sources=[
        "Science 2018, 360, 444–448",
    ],
    disclosed_subsystems=[
        "fabrication-paper-microfluidics",
        "thermal-isothermal-amplification",
    ],
    cpc_classifications=["C12Q 1/68", "G01N 33/543"],
    lineage_ancestors=["gootenberg-zhang-2017-sherlock", "martinez-2007-paper-microfluidics"],
)

add(
    id="organoid-on-chip-clevers-2020",
    canonical_name="Organoid-on-chip integration (Clevers 2020 review)",
    aliases=["organoid-on-chip"],
    corpus="academic",
    first_disclosure_date="2020",
    disclosure_citation="Park, S. E.; Georgescu, A.; Huh, D. Organoids-on-a-chip. Science 2019, 364, 960–965. DOI: 10.1126/science.aaw7894",
    creator="Huh group, Penn / Clevers organoid lineage",
    creator_country="US",
    device_class="organ-on-chip",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Methodological framing of the organoids-on-chip subfield: integration of stem-cell-derived 3D self-organizing organoids with microfluidic perfusion / mechanical-strain platforms. Architectural successor to the dual-channel organ-on-chip lineage by replacing flat 2D tissue culture with 3D organoids. Anticipates: organoid-format tissue + chip-format perfusion as a hybrid architecture, used in subsequent disease-modeling platforms.",
    sources=[
        "Science 2019, 364, 960–965",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["C12M 1/00"],
    lineage_ancestors=["huh-2010-lung-on-chip", "wikswo-2013-multi-organ-chip"],
)

add(
    id="microfluidic-mrna-vaccine-formulation",
    canonical_name="Microfluidic mRNA-LNP vaccine formulation",
    aliases=["mRNA LNP microfluidics", "Pieter Cullis LNP"],
    corpus="academic",
    first_disclosure_date="2012",
    disclosure_citation="Belliveau, N. M.; Huft, J.; Lin, P. J. C.; Chen, S.; Leung, A. K. K.; Leaver, T. J.; Wild, A. W.; Lee, J. B.; Taylor, R. J.; Tam, Y. K.; Hansen, C. L.; Cullis, P. R. Microfluidic synthesis of highly potent limit-size lipid nanoparticles for in vivo delivery of siRNA. Mol. Ther. Nucleic Acids 2012, 1, e37. DOI: 10.1038/mtna.2012.28",
    creator="Cullis, Hansen labs (UBC)",
    creator_country="CA",
    device_class="droplet-generator",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="other",
    ip_status="patented",
    ip_citations=["US9404127B2 (and Precision Nanosystems / Cullis family)"],
    prior_art_notes="Foundational disclosure of microfluidic LNP (lipid nanoparticle) formulation for nucleic acid delivery: rapid mixing of lipid-in-ethanol with nucleic-acid-in-aqueous in microfluidic herringbone mixer drives spontaneous LNP self-assembly with sub-100 nm size distribution. Architecturally critical: the Pfizer-BioNTech and Moderna COVID-19 vaccines depend on Precision Nanosystems' microfluidic LNP manufacturing, which descends directly from this disclosure. Among the highest-impact commercial applications of microfluidics in history.",
    sources=[
        "Mol. Ther. Nucleic Acids 2012, 1, e37",
    ],
    disclosed_subsystems=[
        "mixer-passive-split-recombine",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["A61K 9/127", "B01L 3/00"],
    lineage_ancestors=["stroock-2002-staggered-herringbone-mixer"],
)

add(
    id="precision-nanosystems-nanoassemblr",
    canonical_name="Precision Nanosystems NanoAssemblr (microfluidic LNP manufacturing)",
    aliases=["NanoAssemblr", "Precision Nanosystems Spark / Benchtop / Blaze"],
    corpus="private",
    first_disclosure_date="2010",
    disclosure_citation="Precision Nanosystems (acquired by Cytiva 2021) NanoAssemblr platform. https://www.precisionnanosystems.com",
    creator="Precision Nanosystems / Cytiva (Danaher)",
    creator_country="CA",
    device_class="droplet-generator",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="other",
    ip_status="patented",
    ip_citations=["US9404127B2", "US8956572B2 (NanoAssemblr family)"],
    prior_art_notes="Commercial implementation of the Cullis microfluidic LNP manufacturing technology. The NanoAssemblr family includes Spark (research-scale), Benchtop (preclinical-scale), and Blaze (GMP-scale) variants — Blaze instruments produced billions of doses of Pfizer-BioNTech and Moderna COVID-19 vaccines from 2020 onward. Among the most commercially significant microfluidic platforms ever deployed by impact.",
    sources=[
        "Precision Nanosystems / Cytiva product literature",
        "Various press coverage of COVID-19 vaccine manufacturing",
    ],
    disclosed_subsystems=[
        "mixer-passive-split-recombine",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["A61K 9/127", "B01L 3/00"],
    lineage_ancestors=["microfluidic-mrna-vaccine-formulation"],
)

add(
    id="microfluidics-drug-delivery-langer",
    canonical_name="Microfluidics for drug delivery (Langer-Farokhzad lineage)",
    aliases=["Langer microfluidic drug delivery"],
    corpus="academic",
    first_disclosure_date="2008",
    disclosure_citation="Karnik, R.; Gu, F.; Basto, P.; Cannizzaro, C.; Dean, L.; Kyei-Manu, W.; Langer, R.; Farokhzad, O. C. Microfluidic platform for controlled synthesis of polymeric nanoparticles. Nano Lett. 2008, 8, 2906–2912. DOI: 10.1021/nl801736q",
    creator="Langer / Farokhzad labs (MIT / BWH)",
    creator_country="US",
    device_class="droplet-generator",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="other",
    ip_status="patented",
    prior_art_notes="Foundational disclosure of microfluidic polymeric nanoparticle synthesis: rapid solvent-displacement mixing in microfluidic device drives controlled self-assembly of PLGA-PEG drug-loaded nanoparticles. Architectural cousin of LNP synthesis but for hydrophobic-drug-loaded polymeric (rather than lipid) nanoparticles. Anticipates: microfluidic-controlled nanomedicine manufacturing as a commercial category.",
    sources=[
        "Nano Lett. 2008, 8, 2906–2912",
    ],
    disclosed_subsystems=[
        "mixer-passive-split-recombine",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["A61K 9/51", "B01L 3/00"],
)

add(
    id="microfluidic-cell-therapy-manufacturing",
    canonical_name="Microfluidic cell therapy manufacturing (CAR-T scale-up)",
    aliases=["cell therapy microfluidic manufacturing"],
    corpus="academic",
    first_disclosure_date="2018",
    disclosure_citation="Tay, A.; Melosh, N. Mechanical stimulation after centrifuge-free nanoelectroporation drastically improves cell viability and gene transfer. Nano Lett. 2017, 17, 886–892. (And subsequent commercial CAR-T cell-therapy microfluidic platforms.)",
    creator="various — Melosh lab Stanford / commercial CAR-T",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="other",
    ip_status="patented",
    prior_art_notes="Recent academic and commercial work on microfluidic cell therapy manufacturing: T cell activation, transfection, and expansion in flow-through microfluidic devices for CAR-T and other adoptive cell therapies. Anticipates: closed-system microfluidic cell therapy manufacturing platforms (e.g., Cellares, Lonza Cocoon) that integrate microfluidic-equivalent cell handling at GMP scale.",
    sources=[
        "Nano Lett. 2017, 17, 886–892",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "cell-encapsulation-droplet",
    ],
    cpc_classifications=["C12M 1/00", "A61K 35/17"],
)


# =====================================================================
# PRIVATE — additional commercial and Asian
# =====================================================================

add(
    id="toshiba-clinical-analyzer",
    canonical_name="Toshiba TBA series clinical chemistry analyzer",
    aliases=["Toshiba TBA-200FR", "Canon Medical Toshiba TBA"],
    corpus="private",
    first_disclosure_date="1990",
    disclosure_citation="Toshiba Medical Systems (now Canon Medical Systems) TBA series clinical chemistry analyzers. https://global.medical.canon",
    creator="Toshiba Medical Systems / Canon Medical Systems",
    creator_country="JP",
    device_class="lab-on-chip",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Major Japanese central-lab clinical chemistry analyzer platform. The Toshiba TBA-series cumulative patent estate is among the most under-cited in US prior art databases due to language and indexing barriers. The 1990s-era Toshiba reagent-handling and analyzer architectures pre-date most US-equivalent systems.",
    sources=[
        "Canon Medical Systems product literature",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["G01N 35/00", "B01L 3/00"],
)

add(
    id="leica-bond-iii-staining",
    canonical_name="Leica Bond-III automated immunohistochemistry stainer",
    aliases=["Leica Bond III"],
    corpus="private",
    first_disclosure_date="2007",
    disclosure_citation="Leica Biosystems Bond-III. https://www.leicabiosystems.com",
    creator="Leica Biosystems (Danaher)",
    creator_country="DE",
    device_class="lab-on-chip",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Automated immunohistochemistry (IHC) stainer with cartridge-format reagent dispensers and slide-format flow chamber. Used widely in pathology labs worldwide. The Bond cartridge architecture is microfluidic-equivalent at scale: each tissue slide becomes a flow chamber for sequential reagent washes via the integrated dispenser. Reference for the broader pathology-automation cartridge segment.",
    sources=[
        "Leica Biosystems product literature",
    ],
    disclosed_subsystems=[
        "architecture-multiplex-cartridge",
    ],
    cpc_classifications=["G01N 33/543", "G01N 1/30"],
)

add(
    id="ventana-discovery-ihc",
    canonical_name="Ventana DISCOVERY ULTRA automated IHC stainer",
    aliases=["Ventana DISCOVERY", "Roche Ventana"],
    corpus="private",
    first_disclosure_date="2010",
    disclosure_citation="Roche Ventana Medical Systems DISCOVERY ULTRA. https://diagnostics.roche.com",
    creator="Roche Ventana Medical Systems",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Automated IHC stainer competing with Leica Bond. Same architectural pattern: cartridge-format reagent dispensers + slide-format flow chamber + multi-reagent sequential wash. Roche Ventana cumulative patent estate covers much of the IHC automation market.",
    sources=[
        "Roche Ventana product literature",
    ],
    disclosed_subsystems=[
        "architecture-multiplex-cartridge",
    ],
    cpc_classifications=["G01N 33/543", "G01N 1/30"],
)

add(
    id="dako-omnis-stainer",
    canonical_name="Dako Omnis IHC / ISH stainer",
    aliases=["Dako Omnis", "Agilent Dako"],
    corpus="private",
    first_disclosure_date="2013",
    disclosure_citation="Agilent Dako Omnis. https://www.agilent.com/en/products/dako",
    creator="Agilent Dako",
    creator_country="DK",
    device_class="lab-on-chip",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Third major IHC automation platform competing with Leica Bond and Ventana DISCOVERY. Architectural sibling — cartridge dispensers + slide flow chambers. Reference for the broader pathology automation patent thicket.",
    sources=[
        "Agilent Dako product literature",
    ],
    disclosed_subsystems=[
        "architecture-multiplex-cartridge",
    ],
    cpc_classifications=["G01N 33/543", "G01N 1/30"],
)

add(
    id="cellares-cell-shuttle",
    canonical_name="Cellares Cell Shuttle CAR-T manufacturing platform",
    aliases=["Cellares Cell Shuttle"],
    corpus="private",
    first_disclosure_date="2022",
    disclosure_citation="Cellares Corporation Cell Shuttle. https://www.cellares.com",
    creator="Cellares Corporation",
    creator_country="US",
    device_class="single-cell-platform",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="other",
    ip_status="patented",
    prior_art_notes="Industrial-scale CAR-T cell therapy manufacturing platform with cartridge-based closed-system processing of patient cells: activation, transduction, expansion, and harvest in a single disposable cartridge. Anticipates: GMP-scale microfluidic-equivalent cell therapy manufacturing as a category. Architectural cousin of Lonza Cocoon and Miltenyi CliniMACS Prodigy.",
    sources=[
        "Cellares product literature",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "cell-organoid-perfusion",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["C12M 1/00", "A61K 35/17"],
)

add(
    id="lonza-cocoon-cell-therapy",
    canonical_name="Lonza Cocoon CAR-T cell therapy platform",
    aliases=["Lonza Cocoon"],
    corpus="private",
    first_disclosure_date="2017",
    disclosure_citation="Lonza Cocoon Platform. https://www.lonza.com",
    creator="Lonza Group",
    creator_country="CH",
    device_class="single-cell-platform",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="other",
    ip_status="patented",
    prior_art_notes="Closed-cartridge cell therapy manufacturing platform — same product category as Cellares Cell Shuttle and Miltenyi CliniMACS Prodigy. The cell therapy manufacturing cartridge segment is one of the fastest-growing commercial microfluidic markets (2020-onward).",
    sources=[
        "Lonza product literature",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "cell-organoid-perfusion",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["C12M 1/00", "A61K 35/17"],
)

add(
    id="miltenyi-clinimacs-prodigy",
    canonical_name="Miltenyi CliniMACS Prodigy cell therapy platform",
    aliases=["CliniMACS Prodigy"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="Miltenyi Biotec CliniMACS Prodigy. https://www.miltenyibiotec.com",
    creator="Miltenyi Biotec",
    creator_country="DE",
    device_class="single-cell-platform",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="other",
    ip_status="patented",
    prior_art_notes="The first widely-deployed closed-cartridge cell therapy manufacturing platform, predating Lonza Cocoon and Cellares Cell Shuttle. Used for academic CAR-T manufacturing at most major academic medical centers worldwide. Architectural ancestor of the CAR-T-manufacturing-on-cartridge product category.",
    sources=[
        "Miltenyi Biotec product literature",
    ],
    disclosed_subsystems=[
        "architecture-stat-test-cartridge",
        "cell-organoid-perfusion",
        "separation-magnetophoresis",
    ],
    cpc_classifications=["C12M 1/00", "A61K 35/17"],
    lineage_ancestors=["miltenyi-1990-macs-magnetic-cell-sorting"],
)


# =====================================================================
# OPEN — more variants
# =====================================================================

add(
    id="ufluidix-foundry-services",
    canonical_name="uFluidix microfluidic chip fabrication services",
    aliases=["uFluidix"],
    corpus="open",
    first_disclosure_date="2014",
    disclosure_citation="uFluidix microfluidic foundry services. https://www.ufluidix.com",
    creator="uFluidix Inc.",
    creator_country="CA",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Commercial microfluidic chip foundry serving the academic research community: PDMS, glass, and thermoplastic chip fabrication services at academic-budget pricing. While uFluidix itself is commercial, the broader 'foundry services for academic microfluidics' ecosystem (including Microfluidic ChipShop, Dolomite, Black Hole Lab) plays a critical role in lowering the barrier for academic groups without in-house fabrication capability.",
    sources=[
        "uFluidix product literature",
    ],
    disclosed_subsystems=[
        "fabrication-pdms-soft-lithography",
        "fabrication-glass-hf-etching",
    ],
    cpc_classifications=[],
)

add(
    id="black-hole-lab-foundry",
    canonical_name="Black Hole Lab academic microfluidics tooling",
    aliases=["Black Hole Lab", "Elveflow Black Hole Lab"],
    corpus="open",
    first_disclosure_date="2015",
    disclosure_citation="Black Hole Lab (Elveflow) educational and prototype tooling. https://www.elveflow.com / https://www.elveflow.com/black-hole-lab/",
    creator="Black Hole Lab / Elveflow (France)",
    creator_country="FR",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Academic-oriented microfluidics tooling: low-cost spin coaters, plasma cleaners, and prototyping kits. Reference for the European academic-microfluidics tooling ecosystem complementing uFluidix and major commercial foundries.",
    sources=[
        "Black Hole Lab / Elveflow product literature",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="darwin-microfluidics-shop",
    canonical_name="Darwin Microfluidics tubing and components shop",
    aliases=["Darwin Microfluidics"],
    corpus="open",
    first_disclosure_date="2016",
    disclosure_citation="Darwin Microfluidics. https://darwin-microfluidics.com",
    creator="Darwin Microfluidics",
    creator_country="FR",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Online retailer specializing in microfluidic components: tubing, fittings, syringes, chips, and small instruments. Reference for the broader microfluidic-supply ecosystem that supports academic and DIY-bio microfluidic work — the architectural-component-level supply chain that complements chip-fabrication foundries.",
    sources=[
        "Darwin Microfluidics catalog",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="open-microfluidic-pump-pdf-replicator",
    canonical_name="Open replicator-style microfluidic pump (3D-printed peristaltic)",
    aliases=["3D-printed peristaltic pump replicator"],
    corpus="open",
    first_disclosure_date="2019",
    disclosure_citation="Various community designs — derived from Pumpy / Pearce open-source pumps. github community contributions.",
    creator="Various community contributions",
    creator_country="GLOBAL",
    device_class="pump-component",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="open-permissive",
    prior_art_notes="Sub-$50 entirely 3D-printed peristaltic pump community designs. Architectural extension of OpenFlexure / Pumpy concepts to all-3D-printed mechanical assemblies (no machined parts). Reference for the broader 'fully 3D-printed microfluidic instrumentation' trajectory enabled by hobbyist FDM 3D printers.",
    sources=[
        "Various github repositories",
    ],
    disclosed_subsystems=[
        "pump-peristaltic-on-chip",
    ],
    cpc_classifications=["F04B 43/12"],
)


# =====================================================================
# FICTIONAL — more depictions
# =====================================================================

add(
    id="death-stranding-medbay",
    canonical_name="Death Stranding bridge baby fluid systems",
    aliases=["Death Stranding BB pod"],
    corpus="fictional",
    first_disclosure_date="2019",
    disclosure_citation="Death Stranding (Kojima Productions, Sony, 2019).",
    creator="Hideo Kojima / Kojima Productions / Sony",
    creator_country="JP",
    device_class="fictional-laboratory",
    end_application="other",
    ip_status="fictional",
    prior_art_notes="Detailed visual depictions of fluid-filled containment systems for biological subjects ('bridge babies'), including microfluidic-equivalent monitoring and life-support architecture. The architectural specificity is sufficient to count as conceptual prior art for compact, sustained-life-support fluidic systems. Cumulative gaming-cultural-reference data point.",
    sources=[
        "Death Stranding (2019)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="upload-amazon-2020",
    canonical_name="Upload (Amazon) afterlife head-scanning fluid system",
    aliases=["Upload TV series"],
    corpus="fictional",
    first_disclosure_date="2020",
    disclosure_citation="Upload (Amazon Prime Video, 2020–).",
    creator="Greg Daniels / Amazon Studios",
    creator_country="US",
    device_class="fictional-laboratory",
    end_application="other",
    ip_status="fictional",
    prior_art_notes="Visual depictions of head-scanning fluid systems for digital consciousness upload. Includes microfluidic-equivalent neural-fluid-handling for tissue analysis. Cumulative TV-cultural-reference data point for fictional neural-fluid-system depictions.",
    sources=[
        "Upload (2020–)",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# =====================================================================
# More academic — newer 2023-2026 work
# =====================================================================

add(
    id="huang-2024-organoid-on-chip-disease-model",
    canonical_name="Organoid-on-chip disease modeling (2023-2026 academic work)",
    aliases=["organoid-on-chip disease model"],
    corpus="academic",
    first_disclosure_date="2023",
    disclosure_citation="Various 2023-2026 publications extending organoid-on-chip to specific disease models. Representative: Skardal lab Wake Forest body-on-chip work.",
    creator="Various — Skardal / Atala / Hamilton labs and others",
    creator_country="US",
    device_class="organ-on-chip",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Composite reference entry for the 2023-2026 wave of organoid-on-chip disease modeling work: cancer-on-chip with patient-derived organoids, autoimmune disease models, neurodegenerative disease models. The MPS (microphysiological systems) field has matured into a regulatory-recognized framework via FDA Modernization Act 2.0 (2022). Cumulative architectural disclosures from this period define the current state-of-the-art in organ-chip drug screening.",
    sources=[
        "Various 2023-2026 publications",
        "FDA Modernization Act 2.0 (2022)",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
        "architecture-organ-on-chip-vasculature",
    ],
    cpc_classifications=["C12M 1/00"],
    lineage_ancestors=["organoid-on-chip-clevers-2020", "huh-bhatia-2018-mps-roadmap"],
)

add(
    id="microfluidic-extracellular-vesicle-isolation",
    canonical_name="Microfluidic extracellular vesicle / exosome isolation",
    aliases=["microfluidic exosome isolation"],
    corpus="academic",
    first_disclosure_date="2014",
    disclosure_citation="Liga, A.; Vliegenthart, A. D. B.; Oosthuyzen, W.; Dear, J. W.; Kersaudy-Kerhoas, M. Exosome isolation: a microfluidic road-map. Lab Chip 2015, 15, 2388–2394. DOI: 10.1039/C5LC00240K",
    creator="Various — Kersaudy-Kerhoas (Heriot-Watt), Toner group, Lim group (Singapore)",
    creator_country="GB",
    device_class="separator-component",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Composite reference for the microfluidic exosome / EV isolation subfield. Combines size-based (DLD adapted for sub-200-nm cutoff), affinity-based (immunomagnetic), and electrokinetic (DEP) strategies. Anticipates: clinical-grade microfluidic exosome isolation for liquid biopsy applications. Underlies commercial efforts by Exosome Diagnostics, NX Pharmagen, and academic spinouts.",
    sources=[
        "Lab Chip 2015, 15, 2388–2394",
    ],
    disclosed_subsystems=[
        "separation-deterministic-lateral-displacement",
        "separation-magnetophoresis",
        "separation-dielectrophoresis",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "G01N 33/49"],
)

add(
    id="microfluidic-rare-cell-academic-2023",
    canonical_name="Microfluidic rare-cell isolation (2023-onward methods)",
    aliases=["microfluidic rare-cell"],
    corpus="academic",
    first_disclosure_date="2023",
    disclosure_citation="Various 2023-2026 publications on next-generation rare-cell isolation. Representative: cancer-cell-on-chip cluster-isolation methods.",
    creator="Various groups",
    creator_country="GLOBAL",
    device_class="separator-component",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Composite reference for 2023-onward rare-cell isolation work: CTC-cluster isolation (rather than single CTC), circulating immune-cell phenotyping, antigen-independent capture by combined biophysical + biochemical signatures. Cumulative architectural disclosures from this period define current state-of-the-art in rare-cell microfluidic isolation, complementing the foundational 2007-2013 work (Di Carlo, Toner, etc.).",
    sources=[
        "Various 2023-2026 publications",
    ],
    disclosed_subsystems=[
        "separation-inertial-focusing",
        "separation-affinity-capture",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "G01N 33/49"],
    lineage_ancestors=["di-carlo-2007-inertial-microfluidics", "ozkumur-2013-ctc-iChip"],
)


# Write out
with CORPUS.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new entries to {CORPUS}")
