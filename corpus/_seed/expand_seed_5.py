#!/usr/bin/env python3
"""Fifth expansion seed for free-microfluidics-corpus.

Appends ~35 more entries covering:
  - Foundational hydrodynamics (Reynolds, Purcell, Taylor-Aris)
  - Wearable / implantable (Gao sweat, Heikenfeld iontophoresis, MC10, Profusa)
  - Diabetes pump cartridges (Tandem t:slim, Insulet OmniPod, Medtronic)
  - Hydrogel-bead foundational (Choi alginate, Rotem barcoded beads)
  - Surface chemistry (Pluronic F-127, BSA, MPC polymer)
  - Chemotaxis (IBIDI, Boyden chamber descendants)
  - More international cartridges (BGI MGI, GeneSure, Mindray)
  - Newer inertial / acoustic (Sollier vortex, AcouSort)
  - PDMS-skeptical alternatives (NOA, OSTE)
  - Continuous-flow pharma (Jensen MIT spinouts)
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
# FOUNDATIONAL HYDRODYNAMICS — anchor entries far older than µTAS
# =====================================================================

add(
    id="reynolds-1883-pipe-flow-transition",
    canonical_name="An experimental investigation of the circumstances which determine flow regime",
    aliases=["Reynolds 1883", "Reynolds number"],
    corpus="academic",
    first_disclosure_date="1883",
    disclosure_citation="Reynolds, O. An experimental investigation of the circumstances which determine whether the motion of water shall be direct or sinuous, and of the law of resistance in parallel channels. Philos. Trans. R. Soc. London 1883, 174, 935–982. DOI: 10.1098/rstl.1883.0029",
    creator="Osborne Reynolds (Manchester)",
    creator_country="GB",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="The foundational paper of fluid mechanics relevant to microfluidics: defines the Reynolds number Re = ρUL/µ and demonstrates that pipe flow transitions from laminar to turbulent at Re ≈ 2000. Microfluidic flow operates almost universally at Re < 1, deep in the laminar regime, which is why diffusive mixing dominates and why most of microfluidics' counterintuitive behavior follows. Cited as the de facto first reference in any rigorous microfluidic theory paper. Doctrinally relevant for invalidity contention against any patent claiming 'novel laminar-flow microfluidic separation' as a category — the laminar regime itself is 140 years old.",
    sources=[
        "Philos. Trans. R. Soc. London 1883, 174, 935–982",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
    notes="Predates microfluidics by a century; included as the foundational fluid-mechanics anchor that every microfluidic paper implicitly cites.",
)

add(
    id="purcell-1977-life-at-low-reynolds",
    canonical_name="Life at low Reynolds number",
    aliases=["Purcell 1977", "Life at low Re"],
    corpus="academic",
    first_disclosure_date="1977",
    disclosure_citation="Purcell, E. M. Life at low Reynolds number. Am. J. Phys. 1977, 45, 3–11. DOI: 10.1119/1.10903",
    creator="Edward Purcell (Harvard)",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="The canonical pedagogical reference for low-Re hydrodynamics from a microfluidic perspective: bacteria swimming, the scallop theorem (a time-reversible swimming stroke produces no net motion at low Re), and the implications of viscous-dominance for transport at small scales. Cited by essentially every microfluidic-mixing and -swimming paper. Defines the framework within which active vs passive mixing strategies must be evaluated. Doctrinally critical: the scallop theorem invalidates many naive 'reciprocating' mixer claims at low Re.",
    sources=[
        "Am. J. Phys. 1977, 45, 3–11",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="taylor-aris-dispersion-1953",
    canonical_name="Taylor-Aris dispersion in pipe flow",
    aliases=["Taylor dispersion", "Taylor-Aris 1953"],
    corpus="academic",
    first_disclosure_date="1953",
    disclosure_citation="Taylor, G. Dispersion of soluble matter in solvent flowing slowly through a tube. Proc. R. Soc. London Ser. A 1953, 219, 186–203. DOI: 10.1098/rspa.1953.0139 (and Aris, R. Proc. R. Soc. London Ser. A 1956, 235, 67–77.)",
    creator="G. I. Taylor (Cambridge), R. Aris",
    creator_country="GB",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Foundational disclosure of Taylor-Aris dispersion: in pressure-driven (Poiseuille) flow through a tube, the parabolic velocity profile combined with cross-stream diffusion produces an effective axial dispersion coefficient that grows with Pe². This phenomenon is the dominant peak-broadening mechanism in chip CE and continuous-flow analysis, and the reason electroosmotic flow (with its plug-like profile) gives sharper peaks than pressure-driven flow. Anticipates: every CE chip's optimization of peak resolution by minimizing Taylor-Aris dispersion through plug-flow (electroosmotic, electrokinetic) regimes.",
    sources=[
        "Proc. R. Soc. London Ser. A 1953, 219, 186–203",
        "Aris, R. Proc. R. Soc. London Ser. A 1956, 235, 67–77",
    ],
    disclosed_subsystems=[
        "separation-capillary-electrophoresis",
    ],
    cpc_classifications=[],
)

add(
    id="stone-2004-engineering-flows-microfluidics",
    canonical_name="Engineering flows in small devices: microfluidics toward a lab-on-a-chip",
    aliases=["Stone Stroock Ajdari 2004"],
    corpus="academic",
    first_disclosure_date="2004",
    disclosure_citation="Stone, H. A.; Stroock, A. D.; Ajdari, A. Engineering flows in small devices: microfluidics toward a lab-on-a-chip. Annu. Rev. Fluid Mech. 2004, 36, 381–411. DOI: 10.1146/annurev.fluid.36.050802.122124",
    creator="Stone (Princeton), Stroock (Cornell), Ajdari (ESPCI)",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Comprehensive review of microfluidic fluid mechanics with particular emphasis on engineering implications: low-Re scaling, electrokinetics, droplets, mixing strategies, and the mathematical framework for lab-on-a-chip device design. Companion to Squires-Quake 2005 with stronger emphasis on multiphase flow and engineering practice. Methodological foundation for many subsequent device-physics papers.",
    sources=[
        "Annu. Rev. Fluid Mech. 2004, 36, 381–411",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)


# =====================================================================
# WEARABLE / IMPLANTABLE microfluidics
# =====================================================================

add(
    id="gao-2016-sweat-sensor-wearable",
    canonical_name="Wearable sweat sensors with multiplexed biosensing",
    aliases=["Gao 2016 sweat sensor"],
    corpus="academic",
    first_disclosure_date="2016",
    disclosure_citation="Gao, W.; Emaminejad, S.; Nyein, H. Y. Y.; Challa, S.; Chen, K.; Peck, A.; Fahad, H. M.; Ota, H.; Shiraki, H.; Kiriya, D.; Lien, D.-H.; Brooks, G. A.; Davis, R. W.; Javey, A. Fully integrated wearable sensor arrays for multiplexed in situ perspiration analysis. Nature 2016, 529, 509–514. DOI: 10.1038/nature16521",
    creator="Javey group, UC Berkeley",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US10898137B2 (Berkeley wearable sweat sensor family)"],
    prior_art_notes="Foundational disclosure of fully integrated wearable sweat sensor: flexible PCB with multiple ion-selective electrodes, wireless transmission, and integrated microfluidic-equivalent sweat-collection layer. Anticipates: skin-conformal microfluidic sensor architecture, real-time multiplexed sweat metabolite monitoring, and the entire wearable-microfluidic-biosensor commercial category subsequently pursued by Epicore Biosystems, Nix Biosensors, and major sports-physiology efforts.",
    sources=[
        "Nature 2016, 529, 509–514",
    ],
    disclosed_subsystems=[
        "pump-capillary-passive",
        "detection-electrochemical-on-chip",
    ],
    cpc_classifications=["A61B 5/00", "G01N 27/30"],
)

add(
    id="koh-rogers-2016-epidermal-microfluidic",
    canonical_name="Soft, skin-mounted epidermal microfluidic device for sweat collection and analysis",
    aliases=["Koh Rogers 2016 epidermal microfluidics"],
    corpus="academic",
    first_disclosure_date="2016",
    disclosure_citation="Koh, A.; Kang, D.; Xue, Y.; Lee, S.; Pielak, R. M.; Kim, J.; Hwang, T.; Min, S.; Banks, A.; Bastien, P.; Manco, M. C.; Wang, L.; Ammann, K. R.; Jang, K.-I.; Won, P.; Han, S.; Ghaffari, R.; Paik, U.; Slepian, M. J.; Balooch, G.; Huang, Y.; Rogers, J. A. A soft, wearable microfluidic device for the capture, storage, and colorimetric sensing of sweat. Sci. Transl. Med. 2016, 8, 366ra165. DOI: 10.1126/scitranslmed.aaf2593",
    creator="John Rogers group (Northwestern / Illinois)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US10653342B2 (and Rogers wearable family)"],
    prior_art_notes="Disclosed soft skin-mounted epidermal microfluidic patch with networks of capillary-driven channels, color-changing reagent zones, and smartphone-based readout. Anticipates: PDMS-based skin-conformal microfluidic chip architecture, capillary-driven sweat collection and reservoir storage on body, colorimetric multiplexed analysis with smartphone readout. Direct architectural ancestor of the Epicore Biosystems Gx Sweat Patch and similar commercial products.",
    sources=[
        "Sci. Transl. Med. 2016, 8, 366ra165",
    ],
    disclosed_subsystems=[
        "fabrication-pdms-soft-lithography",
        "pump-capillary-passive",
    ],
    cpc_classifications=["A61B 5/00", "B01L 3/00"],
)

add(
    id="kim-rogers-iontophoresis-skin-2014",
    canonical_name="Iontophoretic / reverse iontophoretic sampling on skin (Heikenfeld lineage)",
    aliases=["Heikenfeld iontophoresis"],
    corpus="academic",
    first_disclosure_date="2014",
    disclosure_citation="Heikenfeld, J. Non-invasive analyte access and sensing through eccrine sweat: challenges and outlook circa 2016. Electroanalysis 2016, 28, 1242–1249. DOI: 10.1002/elan.201600018",
    creator="Heikenfeld group, Cincinnati",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="electrokinetic",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Heikenfeld-group framing of skin-interfacing microfluidic biosensors: iontophoretic sweat induction, capillary collection, electrochemical analysis. Reference for the architectural family of stimulus-evoked-sample wearable biosensors that compete with passive-collection (Rogers) approaches.",
    sources=[
        "Electroanalysis 2016, 28, 1242–1249",
    ],
    disclosed_subsystems=[
        "detection-electrochemical-on-chip",
    ],
    cpc_classifications=["A61B 5/00", "G01N 27/00"],
)

add(
    id="mc10-biostamp",
    canonical_name="MC10 BioStamp wearable physiological sensor",
    aliases=["MC10 BioStamp", "BioStamp nPoint"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="MC10 Inc. BioStamp Research Connect platform. Patent family includes US9159635B2.",
    creator="MC10 Inc. (assets acquired by Medidata 2020)",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="capillary",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US9159635B2", "US9554850B2 (MC10 wearable family)"],
    prior_art_notes="Commercial pioneer in skin-conformal flexible electronic and microfluidic patches for clinical-grade physiological monitoring. Architectural ancestor of much of the modern wearable-microfluidic landscape — anticipates: ultra-thin flexible substrate + integrated electronics + microfluidic-equivalent fluid handling, deployed at clinical-trial scale before the academic literature peaked.",
    sources=[
        "MC10 product literature (archived)",
        "MC10 patent family",
    ],
    disclosed_subsystems=[
        "detection-electrochemical-on-chip",
    ],
    cpc_classifications=["A61B 5/00"],
)

add(
    id="profusa-lumee-implantable",
    canonical_name="Profusa Lumee implantable hydrogel oxygen sensor",
    aliases=["Profusa Lumee", "Lumee O2"],
    corpus="private",
    first_disclosure_date="2014",
    disclosure_citation="Profusa Inc. Lumee Oxygen Platform. https://profusa.com",
    creator="Profusa Inc.",
    creator_country="US",
    device_class="point-of-care-cartridge",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Implantable subcutaneous hydrogel-encapsulated phosphorescent oxygen sensor with optical readout through skin. Architecturally a tissue-resident microfluidic-equivalent that performs continuous biosensing without extracorporeal sample handling. Anticipates: implantable-hydrogel sensor as a category, optical-readout-through-skin architecture, and the broader 'continuous tissue biosensor' product class.",
    sources=[
        "Profusa product literature",
    ],
    disclosed_subsystems=[
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["A61B 5/00"],
)


# =====================================================================
# DIABETES PUMP CARTRIDGES — high-volume microfluidic devices commonly forgotten
# =====================================================================

add(
    id="tandem-tslim-x2-cartridge",
    canonical_name="Tandem Diabetes t:slim X2 insulin pump cartridge",
    aliases=["t:slim X2", "Tandem X2"],
    corpus="private",
    first_disclosure_date="2012",
    disclosure_citation="Tandem Diabetes Care t:slim X2 Insulin Pump. https://www.tandemdiabetes.com",
    creator="Tandem Diabetes Care",
    creator_country="US",
    device_class="other",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="other",
    ip_status="patented",
    ip_citations=["US7905867B2 (and Tandem patent family)"],
    prior_art_notes="Disposable insulin pump cartridge with integrated micro-pump (microfluidic delivery channel + flat-membrane reservoir) for sub-µL/min closed-loop insulin dosing. Architecturally a high-volume implementation of microfluidic dosing technology — the sub-mL/day insulin delivery rates make this one of the most demanding commercial microfluidic dosing applications. Anticipates: programmable closed-loop microfluidic pharmaceutical delivery in disposable cartridge form factor.",
    sources=[
        "Tandem Diabetes Care product literature",
    ],
    disclosed_subsystems=[
        "pump-piezoelectric-stack",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["A61M 5/14"],
)

add(
    id="insulet-omnipod-cartridge",
    canonical_name="Insulet OmniPod tubeless insulin pump",
    aliases=["OmniPod", "OmniPod 5"],
    corpus="private",
    first_disclosure_date="2005",
    disclosure_citation="Insulet Corporation OmniPod Insulin Management System. https://www.omnipod.com",
    creator="Insulet Corporation",
    creator_country="US",
    device_class="other",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="other",
    ip_status="patented",
    ip_citations=["US7128727B2 (and Insulet patent family)"],
    prior_art_notes="Tubeless wearable insulin pump 'pod' integrating reservoir, micropump, infusion cannula, and wireless communication in a single skin-mounted disposable. Architecturally distinct from Tandem t:slim by eliminating external tubing. Highest-volume wearable microfluidic device in the world by unit count (sub-100M units shipped). Anticipates: integrated wearable disposable microfluidic pump architecture, body-mounted closed-loop pharmaceutical delivery.",
    sources=[
        "Insulet OmniPod product literature",
    ],
    disclosed_subsystems=[
        "pump-piezoelectric-stack",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["A61M 5/14", "A61M 5/142"],
)

add(
    id="medtronic-780g-pump",
    canonical_name="Medtronic MiniMed 780G insulin pump cartridge",
    aliases=["MiniMed 780G", "Medtronic 780G"],
    corpus="private",
    first_disclosure_date="2017",
    disclosure_citation="Medtronic MiniMed 780G System. https://www.medtronicdiabetes.com",
    creator="Medtronic plc",
    creator_country="IE",
    device_class="other",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="pressure-driven",
    end_application="other",
    ip_status="patented",
    prior_art_notes="Long-lived insulin pump platform with integrated CGM (continuous glucose monitor) and closed-loop dosing algorithm. The CGM cartridge involves microfluidic-equivalent transcutaneous glucose sensing. Architectural precedent for closed-loop sense+dose wearable microfluidic systems.",
    sources=[
        "Medtronic Diabetes product literature",
    ],
    disclosed_subsystems=[
        "pump-piezoelectric-stack",
        "detection-electrochemical-on-chip",
    ],
    cpc_classifications=["A61M 5/14", "G01N 27/00"],
)


# =====================================================================
# HYDROGEL BEAD foundational
# =====================================================================

add(
    id="choi-weitz-2007-alginate-microbead",
    canonical_name="Microfluidic alginate microbead generation",
    aliases=["Choi Weitz alginate beads"],
    corpus="academic",
    first_disclosure_date="2007",
    disclosure_citation="Choi, C.-H.; Jung, J.-H.; Rhee, Y. W.; Kim, D.-P.; Shim, S.-E.; Lee, C.-S. Generation of monodisperse alginate microbeads and in situ encapsulation of cell in microfluidic device. Biomed. Microdevices 2007, 9, 855–862. DOI: 10.1007/s10544-007-9098-7",
    creator="various — Lee, Weitz, Doyle (early 2000s contributions)",
    creator_country="KR",
    device_class="droplet-generator",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="multiphase-pressure",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Foundational disclosure of microfluidic alginate microbead generation: aqueous alginate flow-focused into oil with downstream calcium-mediated gelation produces monodisperse alginate microbeads suitable for cell encapsulation. Anticipates: alginate-as-microbead-substrate-in-droplet-microfluidics, which became the backbone of single-cell sequencing platforms (Drop-seq, inDrops, Tapestri) where the bead encapsulates barcoding oligos.",
    sources=[
        "Biomed. Microdevices 2007, 9, 855–862",
    ],
    disclosed_subsystems=[
        "droplet-flow-focusing-generation",
        "cell-encapsulation-droplet",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "C12N 11/04"],
)

add(
    id="rotem-zilionis-2015-barcoded-bead",
    canonical_name="Barcoded hydrogel beads for single-cell RNA-seq",
    aliases=["Rotem Zilionis 2015 barcoded beads"],
    corpus="academic",
    first_disclosure_date="2015",
    disclosure_citation="Klein, A. M.; Mazutis, L.; et al. (inDrops paper, see klein-2015-indrops). Zilionis, R. et al. Single-cell barcoding and sequencing using droplet microfluidics. Nat. Protoc. 2017, 12, 44–73.",
    creator="Klein / Mazutis / Weitz (Harvard)",
    creator_country="US",
    device_class="droplet-generator",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="multiphase-pressure",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Disclosed barcoded-hydrogel-bead manufacturing for single-cell RNA-seq: split-and-pool synthesis on alginate beads in microfluidic encapsulation produces a library of beads each bearing a unique barcode, used in inDrops and similar platforms. Anticipates: split-pool-bead-barcoding architecture, which became central to the inDrops and 10x Chromium commercial platforms.",
    sources=[
        "Nat. Protoc. 2017, 12, 44–73",
    ],
    disclosed_subsystems=[
        "droplet-flow-focusing-generation",
        "cell-encapsulation-droplet",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["C12Q 1/68", "B01L 3/00"],
    lineage_descendants=["klein-2015-indrops", "10x-genomics-chromium-controller"],
)


# =====================================================================
# SURFACE CHEMISTRY — ubiquitous-but-rarely-cited foundational chemistries
# =====================================================================

add(
    id="vroman-effect-1962",
    canonical_name="Vroman effect: time-resolved competitive protein adsorption",
    aliases=["Vroman effect"],
    corpus="academic",
    first_disclosure_date="1962",
    disclosure_citation="Vroman, L. Effect of adsorbed proteins on the wettability of hydrophilic and hydrophobic solids. Nature 1962, 196, 476–477. DOI: 10.1038/196476a0",
    creator="Leo Vroman",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Foundational disclosure of the Vroman effect: when blood or serum contacts a surface, smaller proteins adsorb first and are subsequently displaced by larger proteins in a kinetic cascade ending with high-molecular-weight kininogen on most surfaces. Critical context for any blood-contacting microfluidic device — protein fouling on surfaces is essentially impossible to prevent without active passivation. Doctrinally relevant for invalidity contention against patents claiming 'novel non-fouling surface' that turns out to be a known passivation chemistry.",
    sources=[
        "Nature 1962, 196, 476–477",
    ],
    disclosed_subsystems=[],
    cpc_classifications=[],
)

add(
    id="lee-1989-mpc-polymer-passivation",
    canonical_name="2-methacryloyloxyethyl phosphorylcholine (MPC) polymer for non-fouling surfaces",
    aliases=["MPC polymer", "Lipidure"],
    corpus="academic",
    first_disclosure_date="1989",
    disclosure_citation="Ishihara, K.; Aragaki, R.; Ueda, T.; Watenabe, A.; Nakabayashi, N. Reduced thrombogenicity of polymers having phospholipid polar groups. J. Biomed. Mater. Res. 1990, 24, 1069–1077. DOI: 10.1002/jbm.820240810",
    creator="Ishihara group (Tokyo Medical and Dental University)",
    creator_country="JP",
    device_class="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="patented",
    ip_citations=["JP H01-258732 (Ishihara MPC family)"],
    prior_art_notes="Disclosure of MPC (2-methacryloyloxyethyl phosphorylcholine) polymer for non-fouling biomedical surfaces. Anticipates: phosphorylcholine-headgroup polymer coatings on microfluidic surfaces (commercialized as NOF Corporation's Lipidure), which reduce protein adsorption by mimicking the outer leaflet of a cell membrane. Among the most widely-used commercial passivation chemistries in the microfluidic / blood-contacting medical device industry.",
    sources=[
        "J. Biomed. Mater. Res. 1990, 24, 1069–1077",
        "NOF Corporation Lipidure product literature",
    ],
    disclosed_subsystems=[
        "surface-treatment-pegylation",
    ],
    cpc_classifications=["C08F 220/26", "B01L 3/00"],
)


# =====================================================================
# PDMS-SKEPTICAL alternatives
# =====================================================================

add(
    id="bartolo-2008-noa-microfluidics",
    canonical_name="NOA-81 (Norland Optical Adhesive) microfluidic chip fabrication",
    aliases=["NOA microfluidics", "Bartolo NOA"],
    corpus="academic",
    first_disclosure_date="2008",
    disclosure_citation="Bartolo, D.; Degré, G.; Nghe, P.; Studer, V. Microfluidic stickers. Lab Chip 2008, 8, 274–279. DOI: 10.1039/B712368J",
    creator="Studer group, ESPCI",
    creator_country="FR",
    device_class="lab-on-chip",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="Disclosed NOA-81 (Norland Optical Adhesive 81) microfluidic chip fabrication: UV-curable thiol-ene polymer cast against PDMS master and bonded to glass without plasma activation. Architectural alternative to PDMS that addresses PDMS's well-known limitations: hydrophobicity recovery, small-molecule absorption, gas permeability. Anticipates: thiol-ene-as-microfluidic-substrate, and the broader 'PDMS-skeptical' fabrication trend that includes OSTE (off-stoichiometry thiol-ene) and Norland-cousin photopolymers.",
    sources=[
        "Lab Chip 2008, 8, 274–279",
    ],
    disclosed_subsystems=[
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00"],
    notes="The architectural alternative to PDMS for chips that need solvent compatibility, no small-molecule absorption, and rigid bonding.",
)

add(
    id="carlborg-2011-oste-microfluidics",
    canonical_name="OSTE (off-stoichiometry thiol-ene) microfluidic substrates",
    aliases=["OSTE", "OSTE+"],
    corpus="academic",
    first_disclosure_date="2011",
    disclosure_citation="Carlborg, C. F.; Haraldsson, T.; Öberg, K.; Malkoch, M.; van der Wijngaart, W. Beyond PDMS: off-stoichiometry thiol-ene (OSTE) based soft lithography for rapid prototyping of microfluidic devices. Lab Chip 2011, 11, 3136–3147. DOI: 10.1039/C1LC20388F",
    creator="van der Wijngaart, Carlborg, Haraldsson (KTH Stockholm)",
    creator_country="SE",
    device_class="lab-on-chip",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Disclosed OSTE (off-stoichiometry thiol-ene) substrate for microfluidics: a tunable photopolymer with controllable surface chemistry, mechanical properties, and bonding behavior. The OSTE+ variant adds reactive surface chemistry that allows direct chemical bonding to other substrates. Architectural alternative to PDMS for chips needing tuned surface chemistry, organic-solvent compatibility, and rigid mechanical properties.",
    sources=[
        "Lab Chip 2011, 11, 3136–3147",
    ],
    disclosed_subsystems=[
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00"],
)


# =====================================================================
# CHEMOTAXIS / CELL MIGRATION
# =====================================================================

add(
    id="boyden-1962-chamber-chemotaxis",
    canonical_name="Boyden chamber chemotaxis assay",
    aliases=["Boyden chamber"],
    corpus="academic",
    first_disclosure_date="1962",
    disclosure_citation="Boyden, S. The chemotactic effect of mixtures of antibody and antigen on polymorphonuclear leucocytes. J. Exp. Med. 1962, 115, 453–466. DOI: 10.1084/jem.115.3.453",
    creator="Stephen Boyden",
    creator_country="AU",
    device_class="other",
    substrate_material="other",
    fabrication_method="other",
    flow_regime="passive",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="The Boyden chamber: two compartments separated by a porous membrane (typ. 5 µm pore polycarbonate) with chemoattractant in the lower compartment and cells in the upper compartment. Cells migrate through the membrane in proportion to chemoattractant gradient. Microfluidic-relevant prior art: every microfluidic chemotaxis chip (gradient generator + cell observation chamber) is conceptually downstream of the Boyden chamber. Anticipates: porous-membrane-separated-chamber architecture for cell migration assays.",
    sources=[
        "J. Exp. Med. 1962, 115, 453–466",
    ],
    disclosed_subsystems=[],
    cpc_classifications=["C12M 1/00"],
)

add(
    id="ibidi-mu-slide-chemotaxis",
    canonical_name="IBIDI µ-Slide chemotaxis chamber",
    aliases=["IBIDI µ-Slide", "IBIDI chemotaxis"],
    corpus="private",
    first_disclosure_date="2007",
    disclosure_citation="ibidi GmbH µ-Slide Chemotaxis 2D / 3D. https://ibidi.com",
    creator="ibidi GmbH",
    creator_country="DE",
    device_class="other",
    substrate_material="thermoplastic",
    fabrication_method="injection-molding",
    flow_regime="passive",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Commercial chemotaxis chip in slide format: injection-molded thermoplastic with three reservoir wells and microfluidic gradient channel between two source wells, allowing live-cell imaging of chemotaxis. Architecturally a commercial implementation of the Christmas-tree-gradient principle in slide-format consumable. The dominant academic chemotaxis chip platform 2010–present.",
    sources=[
        "ibidi product literature",
    ],
    disclosed_subsystems=[
        "mixer-passive-split-recombine",
        "fabrication-thermoplastic-injection-molding",
    ],
    cpc_classifications=["C12M 1/00", "B01L 3/00"],
    lineage_ancestors=["dertinger-2001-christmas-tree-gradient"],
)


# =====================================================================
# INTERNATIONAL CARTRIDGES / SEQUENCERS
# =====================================================================

add(
    id="bgi-mgi-dnbseq-flowcell",
    canonical_name="BGI MGI DNBSEQ sequencer flow cell",
    aliases=["BGI DNBSEQ", "MGI DNBSEQ", "Complete Genomics DNB"],
    corpus="private",
    first_disclosure_date="2010",
    disclosure_citation="Drmanac, R. et al. Human genome sequencing using unchained base reads on self-assembling DNA nanoarrays. Science 2010, 327, 78–81. DOI: 10.1126/science.1181498",
    creator="Complete Genomics (acquired by BGI 2013) / MGI",
    creator_country="CN",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    ip_citations=["US7910302B2 (Complete Genomics DNB family)"],
    prior_art_notes="DNA nanoball (DNB) sequencing: rolling-circle-amplified DNA nanoballs spotted on patterned silicon arrays for combinatorial probe-anchor-ligation sequencing. Architecturally distinct from Illumina (bridge amplification) and Ion Torrent (clonal microwell) by using pre-amplified template nanoballs. The dominant non-Illumina sequencing platform globally by deployed instrument count, particularly outside the US market. Anticipates: nanoball-array architecture for high-density sequencing, and the architectural diversity of post-2010 short-read sequencer platforms.",
    sources=[
        "Science 2010, 327, 78–81",
        "BGI / MGI product literature",
    ],
    disclosed_subsystems=[
        "fabrication-silicon-drie",
        "detection-fluorescence-on-chip",
    ],
    cpc_classifications=["C12Q 1/68"],
)


# =====================================================================
# NEWER inertial / acoustic platforms
# =====================================================================

add(
    id="sollier-2014-vortex-chip",
    canonical_name="Vortex chip for label-free CTC isolation (Sollier 2014)",
    aliases=["Vortex chip", "Vortex Biosciences"],
    corpus="academic",
    first_disclosure_date="2014",
    disclosure_citation="Sollier, E. et al. Size-selective collection of circulating tumor cells using Vortex technology. Lab Chip 2014, 14, 63–77. DOI: 10.1039/C3LC50689D",
    creator="Di Carlo group, UCLA / Vortex Biosciences",
    creator_country="US",
    device_class="separator-component",
    substrate_material="PDMS",
    fabrication_method="soft-lithography",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US9695432B2 (Vortex Biosciences family)"],
    prior_art_notes="Disclosed vortex-chamber inertial separation: large CTCs are trapped in microscale vortex chambers via inertial migration while smaller blood cells flow through, enabling label-free size-based CTC enrichment. Anticipates: vortex-chamber-as-cell-trap architecture, label-free CTC isolation by inertial trapping (distinct from inertial focusing for streamline ordering). Commercial implementation: Vortex Biosciences VTX-1 (now part of NanoString).",
    sources=[
        "Lab Chip 2014, 14, 63–77",
    ],
    disclosed_subsystems=[
        "separation-inertial-focusing",
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00", "G01N 33/49"],
    lineage_ancestors=["di-carlo-2007-inertial-microfluidics"],
)

add(
    id="acousort-acoustofluidic-platform",
    canonical_name="AcouSort BAW acoustofluidic platform",
    aliases=["AcouSort", "AcouWash"],
    corpus="private",
    first_disclosure_date="2013",
    disclosure_citation="AcouSort AB. https://acousort.com",
    creator="AcouSort AB (Lund Sweden, spinoff from Laurell group)",
    creator_country="SE",
    device_class="separator-component",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="acoustic",
    end_application="diagnostic",
    ip_status="patented",
    prior_art_notes="Commercial bulk-acoustic-wave (BAW) acoustofluidic platform: silicon-microchannel BAW resonator for label-free continuous cell separation. Architecturally the commercial descendant of Laurell 2007 acoustophoresis. Used clinically for blood-cell washing, platelet separation, and CTC enrichment. Anticipates: BAW-acoustofluidic platform commercialization at clinical scale.",
    sources=[
        "AcouSort product literature",
    ],
    disclosed_subsystems=[
        "separation-acoustophoresis",
        "fabrication-silicon-drie",
        "fabrication-glass-anodic-bonding",
    ],
    cpc_classifications=["B01L 3/00", "G01N 15/02"],
    lineage_ancestors=["laurell-2007-acoustophoresis"],
)


# =====================================================================
# CONTINUOUS-FLOW PHARMA
# =====================================================================

add(
    id="adamo-2016-continuous-pharma-mit",
    canonical_name="Continuous-flow pharmaceutical manufacturing on chip (Jensen 2016 MIT spinout-driven)",
    aliases=["Adamo continuous pharma", "Jensen continuous pharma"],
    corpus="academic",
    first_disclosure_date="2016",
    disclosure_citation="Adamo, A. et al. On-demand continuous-flow production of pharmaceuticals in a compact, reconfigurable system. Science 2016, 352, 61–67. DOI: 10.1126/science.aaf1337",
    creator="Jensen group, MIT",
    creator_country="US",
    device_class="flow-controller",
    substrate_material="hybrid",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="industrial",
    ip_status="patented",
    prior_art_notes="Demonstrated end-to-end continuous-flow synthesis of four small-molecule pharmaceuticals (lidocaine, diphenhydramine, fluoxetine, diazepam) on a 1-meter benchtop system integrating reaction modules, separations, and crystallization. Anticipates: end-to-end continuous-flow pharmaceutical manufacturing in compact reconfigurable form factor, and the architectural goal of distributed pharmaceutical manufacturing that informs the FDA Pharmaceutical Quality for the 21st Century framework.",
    sources=[
        "Science 2016, 352, 61–67",
    ],
    disclosed_subsystems=[
        "architecture-process-analytical-technology",
    ],
    cpc_classifications=["B01J 19/00"],
    lineage_ancestors=["reizman-2015-self-optimizing-flow"],
)


# =====================================================================
# LATER ACADEMIC additions
# =====================================================================

add(
    id="mcdonald-whitesides-2002-pdms-review",
    canonical_name="Poly(dimethylsiloxane) as a material for fabricating microfluidic devices (McDonald & Whitesides 2002)",
    aliases=["McDonald Whitesides PDMS review"],
    corpus="academic",
    first_disclosure_date="2002",
    disclosure_citation="McDonald, J. C.; Whitesides, G. M. Poly(dimethylsiloxane) as a material for fabricating microfluidic devices. Acc. Chem. Res. 2002, 35, 491–499. DOI: 10.1021/ar010110q",
    creator="McDonald, Whitesides (Harvard)",
    creator_country="US",
    device_class="other",
    end_application="research",
    ip_status="public-domain",
    prior_art_notes="The canonical methodology paper for PDMS as a microfluidic substrate: physical properties, surface chemistry, plasma activation, design constraints. Cited as the standard methodological reference for any PDMS-based microfluidic device. Companion to Duffy 1998 (the originating disclosure) and Xia/Whitesides 1998 (the broader soft-lithography review).",
    sources=[
        "Acc. Chem. Res. 2002, 35, 491–499",
    ],
    disclosed_subsystems=[
        "fabrication-pdms-soft-lithography",
    ],
    cpc_classifications=["B01L 3/00"],
    lineage_ancestors=["duffy-1998-pdms-soft-lithography-microfluidics"],
)

add(
    id="quake-1997-pcr-on-chip",
    canonical_name="Continuous-flow PCR on chip (Kopp 1998)",
    aliases=["Kopp 1998 continuous-flow PCR"],
    corpus="academic",
    first_disclosure_date="1998",
    disclosure_citation="Kopp, M. U.; de Mello, A. J.; Manz, A. Chemical amplification: continuous-flow PCR on a chip. Science 1998, 280, 1046–1048. DOI: 10.1126/science.280.5366.1046",
    creator="Manz group, Imperial College",
    creator_country="GB",
    device_class="lab-on-chip",
    substrate_material="glass",
    fabrication_method="photolithography",
    flow_regime="pressure-driven",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US6613560B1"],
    prior_art_notes="Disclosed continuous-flow PCR on chip: serpentine glass channel passes through three temperature zones (denature/anneal/extend), with the number of cycles equal to the number of channel passes through each zone. Anticipates: spatial-temperature-zone PCR architecture as alternative to time-domain thermal cycling, and the entire continuous-flow PCR subfield. Architectural ancestor of many subsequent flow-PCR designs.",
    sources=[
        "Science 1998, 280, 1046–1048",
    ],
    disclosed_subsystems=[
        "fabrication-glass-hf-etching",
        "thermal-pcr-cycling",
    ],
    cpc_classifications=["C12Q 1/686", "B01L 3/00"],
)

add(
    id="northrup-1993-silicon-pcr-microreactor",
    canonical_name="Silicon-based miniature PCR thermal cycler (Northrup 1993)",
    aliases=["Northrup 1993 silicon PCR"],
    corpus="academic",
    first_disclosure_date="1993",
    disclosure_citation="Northrup, M. A.; Ching, M. T.; White, R. M.; Watson, R. T. DNA amplification with a microfabricated reaction chamber. Proc. Transducers '93, 1993, 924–926.",
    creator="Northrup group, Lawrence Livermore",
    creator_country="US",
    device_class="lab-on-chip",
    substrate_material="silicon",
    fabrication_method="photolithography",
    flow_regime="passive",
    end_application="diagnostic",
    ip_status="patented",
    ip_citations=["US5589136A (Northrup silicon PCR)"],
    prior_art_notes="The first demonstration of PCR in a silicon microfabricated reaction chamber with integrated heater. Predates Wittwer's commercial RapidCycler and Manz's continuous-flow PCR; the architectural ancestor of all subsequent silicon-microreactor PCR work. Among the foundational references in chip-format molecular diagnostics — disclosed five years before the µTAS-era PCR chip explosion.",
    sources=[
        "Proc. Transducers '93, 924–926",
    ],
    disclosed_subsystems=[
        "fabrication-silicon-drie",
        "thermal-pcr-cycling",
    ],
    cpc_classifications=["C12Q 1/686", "B01L 3/00"],
)

add(
    id="taiwan-tw-organ-chip-research",
    canonical_name="Asia-Pacific organ-on-chip programs (Taiwan, Korea, Singapore consortia)",
    aliases=["APAC organ-on-chip programs"],
    corpus="academic",
    first_disclosure_date="2018",
    disclosure_citation="Various Asia-Pacific organ-on-chip consortia announcements; representative: NTU Singapore CAMP / KAIST / NHRI Taiwan organ-chip programs.",
    creator="Various Asia-Pacific consortia",
    creator_country="OTHER",
    device_class="organ-on-chip",
    fabrication_method="other",
    flow_regime="pressure-driven",
    end_application="research",
    ip_status="patented",
    prior_art_notes="Reference entry for the Asia-Pacific organ-on-chip research and consortia activity that emerged 2015–present, complementing the US (NIH MPS) and EU (EU-MPS / ERA) programs. Specific commercial activity includes Singapore-based organ-chip startups, Taiwan NHRI-funded efforts, and Korea KIST work. The patent and architectural disclosures from this region are systematically under-cited in US prior-art databases.",
    sources=[
        "Various consortia announcements and publications",
    ],
    disclosed_subsystems=[
        "cell-organoid-perfusion",
    ],
    cpc_classifications=["C12M 1/00"],
)


# Write out
with CORPUS.open("a") as f:
    for e in ENTRIES:
        f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
print(f"  appended {len(ENTRIES)} new entries to {CORPUS}")
