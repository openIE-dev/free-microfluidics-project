---
title: architecture-process-analytical-technology
parent: Cross-cuts
layout: default
---

# Cross-cut: `architecture-process-analytical-technology`

**66 corpus entries disclose this subsystem.**

Earliest disclosure: 1995

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Mettler-Toledo InPro 6800 / 6850 Dissolved Oxygen Sensor (1995)

- **id**: `mettler-toledo-inpro-6800-do`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Mettler-Toledo Process Analytics
- **disclosure**: Mettler-Toledo InPro 6800 polarographic DO sensor product introduction mid-1990s; InPro 6850 optical successor introduced ~2010; Mettler-Toledo Process Analytics product literature; US patent US7,022,505B1 (Mettler-Toledo, optical oxygen sensor)
- **ip status**: patented
- **prior art notes**: Discloses two architectures: the InPro 6800 implements a Clark-cell polarographic DO measurement (Pt cathode, Ag/AgCl anode, electrolyte-filled chamber, PTFE gas-permeable membrane); the InPro 6850 implements a luminescence-lifetime optical DO measurement (luminophore in polymer matrix, LED excitation, photodiode detection of fluorescence-decay phase shift). Anticipates: paired polarographic and optical DO architectures with shared probe-body form factor and digital ISM interface, allowing process-development to validate either sensor type in interchangeable ports. Element-by-element: probe body + sensing element (membrane + electrolyte / optical spot) + signal-processing electronics + digital interface.

## Aldevron Plasmid Manufacturing Platform (Danaher subsidiary) (1998)

- **id**: `aldevron-plasmid-extend`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Aldevron LLC (acquired 2021 by Danaher)
- **disclosure**: Aldevron company founding 1998; Aldevron patent US10,975,374B2 (Methods for plasmid DNA manufacturing); Aldevron acquired by Danaher 2021 for $9.6B (SEC 8-K)
- **ip status**: patented
- **prior art notes**: Process disclosure (extending wave 1 generic plasmid coverage): Aldevron's GMP plasmid train comprises fed-batch E. coli fermentation → in-line continuous static-mixer alkaline lysis (microfluidic laminar mixing of cell paste with NaOH/SDS lysis buffer) → flocculation neutralization → centrifugal/depth clarification → TFF concentration → AEX (Q-Sepharose / Capto-class) → HIC polishing → final TFF + 0.2 µm sterile filtration. Anticipates: standardized GMP plasmid manufacturing chain optimized for CGT and mRNA-vaccine-template supply, where the in-line static-mixer lysis step is the microfluidic-relevant unit operation (controls shear-induced plasmid degradation by setting mixing residence time and Reynolds regime). Element-by-element: fermenter outlet + static-mixer lysis + neutralizer junction + centrifuge → bag → AEX column → HIC column → TFF → sterile fill.

## Velocys microchannel Fischer-Tropsch reactor for GTL/PTL/BTL (2001)

- **id**: `velocys-microchannel-fischer-tropsch`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Velocys Inc. (PNNL spinout, US/UK)
- **disclosure**: Tonkovich, A. L.; Perry, S.; Wang, Y.; Qiu, D.; LaPlante, T.; Rogers, W. A. 'Microchannel process technology for compact methane steam reforming' Chem. Eng. Sci. 2004, 59, 4819–4824; Velocys Inc. (formerly Oxford Catalysts Group) founding 2001 from PNNL spinout; ENVIA Energy Oklahoma City GTL plant commissioning 2017
- **ip status**: patented
- **prior art notes**: Canonical industrial deployment of microchannel chemistry to a multi-thousand-kilogram-per-day production application. Discloses (a) diffusion-bonded stainless-steel laminate microchannel reactor with alternating reaction and coolant layers — the architectural pattern that made plant-scale microchannel reactors economically viable; (b) catalyst-coated structured washcoat within sub-millimeter channels for highly exothermic Fischer-Tropsch synthesis; (c) the 'numbering-up at scale' execution of stacking thousands of identical channels in parallel inside a single reactor block; (d) commercial demonstration at ENVIA Energy Oklahoma City. Anticipates patent claims to laminated metal microchannel reactors for highly exothermic gas-to-liquids chemistry, and to catalyst-coated microchannel architecture for compact GTL plants.

## Ehrfeld Mikrotechnik BTS CYTOS College and Caterpillar microreactors (2002)

- **id**: `ehrfeld-cytos-college-caterpillar`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Ehrfeld Mikrotechnik BTS GmbH (Bayer Technology Services subsidiary)
- **disclosure**: Ehrfeld, W.; Hessel, V.; Löwe, H. Microreactors: New Technology for Modern Chemistry, Wiley-VCH, 2000, ISBN 978-3-527-29590-6; CPC Systems / Ehrfeld Mikrotechnik BTS CYTOS College brochure 2002; US patent 6,221,226; Bayer Technology Services acquisition of Ehrfeld 2009
- **ip status**: patented
- **prior art notes**: Discloses (a) the Caterpillar mixer geometry — a cascade of asymmetric ramps that repeatedly splits and laminates the flow at the sub-millimeter scale, predating most heart-shape literature in the production-microreactor context; (b) the CYTOS College modular cassette pattern of swappable mixer/residence/heat-exchanger units sharing a common manifold and electronic/pneumatic backbone, anticipating the modular cassette pattern later popularized by Vapourtec, Syrris, Future Chemistry; (c) industrial deployment by Bayer (parent company) for hazardous chemistries. Should be cited against later patent claims directed to 'cascade ramp split-recombine mixer' and 'modular cassette flow-chemistry platform with shared backbone'.

## ThalesNano H-Cube continuous-flow hydrogenation reactor (2003)

- **id**: `thalesnano-h-cube-flow-hydrogenation`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: ThalesNano Inc. (Budapest, HU)
- **disclosure**: Jones, R. V.; Godorhazy, L.; Varga, N.; Szalay, D.; Urge, L.; Darvas, F. 'Continuous-flow high pressure hydrogenation reactor for optimization and high-throughput synthesis' J. Comb. Chem. 2006, 8, 110–116; ThalesNano H-Cube launch press release 2003; H-Cube user manual rev 2 (2005); US7128883B2
- **ip status**: patented
- **prior art notes**: Canonical commercialization of (a) in-situ electrolytic hydrogen generation coupled to a heated packed-bed flow reactor — eliminating compressed H2 cylinders and enabling lab-bench hydrogenation; (b) the disposable prepacked catalyst cartridge ('CatCart') as standardized sub-component, swappable in <30 s, with 500+ pre-loaded catalyst SKUs (Pd/C, Pt/C, Raney Ni, chiral hydrogenation catalysts); (c) integrated PAT and pressure control sealed in a benchtop appliance form factor. Anticipates patent claims directed to combined-electrolyzer-and-flow-hydrogenation reactors and to disposable prepacked catalyst cartridges within continuous-flow chemistry rigs.

## Air Products microchannel hydrocarbon-to-hydrogen bench reactor (microHCBR) (2003)

- **id**: `air-products-microhcbr-hydrogen-reactor`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Air Products and Chemicals Inc. in collaboration with Pacific Northwest National Laboratory (PNNL)
- **disclosure**: Whyatt, G. A.; TeGrotenhuis, W. E.; Wegeng, R. S.; Pederson, L. R. 'Microchannel reactors for fuel processing applications. II. Compact fuel vaporization for fuel cells' AIChE Spring Meeting 2002 / DOE technical report; Air Products / PNNL CRADA 2002–2008; US7186388B2; AIChE Process Intensification Award presentation 2007
- **ip status**: patented
- **prior art notes**: The PNNL/Air Products CRADA work in 2002–2008 produced foundational US patents on microchannel steam-methane reforming for distributed hydrogen production. Discloses (a) integration of SMR + water-gas-shift catalyst beds in adjacent microchannel layers within a single diffusion-bonded laminate reactor block; (b) integrated combustion channels providing endothermic-reaction heat in cross-flow arrangement; (c) sized for distributed (refueling-station-scale) hydrogen production. Anticipates patent claims directed to integrated SMR+WGS microchannel modules for distributed hydrogen production. Pairs with Velocys (FT) and Ineratec (PtX) — same diffusion-bonded laminate platform, different chemistry.

## Endress+Hauser Memosens Digital Sensor Platform (2004)

- **id**: `endress-hauser-memosens-digital-probe`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Endress+Hauser AG
- **disclosure**: Endress+Hauser Memosens digital sensor architecture introduced 2004; Memosens 2.0 enhanced security 2017; US patent US7,368,920B2 (Endress+Hauser, inductive digital sensor connector)
- **ip status**: patented
- **prior art notes**: Discloses a digital sensor architecture with inductive (transformer-coupled) connector that eliminates wetted electrical contacts: the probe head contains a transformer half-coil and the cable contains the matching half-coil; communication and power transfer occur inductively across the boundary. Calibration data is resident in the probe, allowing the probe to be moved between transmitters or recalibrated off-line then re-installed. Anticipates: inductive-coupled digital sensor connector as alternative to galvanic connector (eliminates contact corrosion and ground-loop issues in process plants); resident-calibration probe architecture for hot-swap workflows. Closely related to Hamilton Arc; differentiated by the inductive coupler vs Hamilton's galvanic digital connector.

## optek-Danulat AF26 Absorption / Turbidity Sensor (2005)

- **id**: `optek-af26-turbidity`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: optek-Danulat GmbH
- **disclosure**: optek-Danulat GmbH AF26 product literature; sensor introduced ~2005; product datasheet rev 2018
- **ip status**: patented
- **prior art notes**: Discloses an inline turbidity / absorption sensor with sapphire windows in a stainless flow cell, NIR LED + photodiode pair across the optical path, signal proportional to cell-density-times-pathlength. Used as in-line PAT for fermentation cell-density measurement and downstream chromatography elution monitoring. Anticipates: inline sapphire-windowed turbidity probe architecture for high-temperature/high-pH-tolerant PAT; combined absorption + scattering measurement in a single flow cell. Element-by-element: stainless flow body + sapphire windows + LED source + photodiode detector + transmitter electronics.

## Avantium Flowrence high-throughput parallel microreactor system (2006)

- **id**: `avantium-flowrence-parallel-microreactor`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Avantium NV (Amsterdam, NL; spinout of Shell)
- **disclosure**: Pérez-Ramírez, J.; Abelló, S.; van der Pers, N. M. 'Memory effect of activated Mg-Al hydrotalcite' Chem. Eur. J. 2007, 13, 870–878 (uses Avantium Flowrence); Avantium press release Flowrence launch 2006; Avantium Flowrence brochure rev 2014; Lange, J.-P. (Shell, Avantium customer) 'Don't forget product recovery in catalysis research' Catal. Today 2010, 159, 23–26
- **ip status**: patented
- **prior art notes**: Discloses (a) the canonical high-throughput parallel-flow-microreactor architecture for industrial-catalyst screening — N reactors sharing a single feed manifold with passive capillary flow restrictors (eliminating per-reactor mass-flow controllers and equalizing residence time across the array); (b) automated inline-GC sampling time-multiplexed across all reactors; (c) the integrated catalyst-development workflow from early-stage screening (Flowrence) through process design (Avantium pilot rigs); (d) Shell origin: Avantium was spun out of Royal Dutch Shell in 2000 with the Flowrence platform as its first product. Anticipates patent claims directed to N-fold parallel microreactor arrays with passive flow-equalization manifolds.

## Cytiva Xcellerex XDR single-use stirred-tank bioreactor (2007)

- **id**: `cytiva-xcellerex-xdr`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Cytiva (Danaher; formerly Xcellerex)
- **disclosure**: Xcellerex Inc. XDR launch 2007 (acquired by GE Healthcare 2012, now Cytiva). Patent family: US7682067B2 (Xcellerex; priority 2005).
- **ip status**: patented
- **prior art notes**: Discloses single-use stirred-tank bioreactor architecture with rigid outer support and disposable inner bag plus impeller assembly. Anticipates: large-format single-use stirred-tank bioreactor architectures for CGT and viral-vector manufacturing; integration with single-use sensor patches and tubing harnesses for closed-system operation at 50-2000 L scale.

## Corning Advanced-Flow Reactor G1 (2007)

- **id**: `corning-advanced-flow-reactor-g1`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Corning Incorporated
- **disclosure**: Lavric, E. D.; Woehl, P. Advanced-Flow Glass Reactors for Seamless Scale-Up. Chimica Oggi - Chemistry Today 2009, 27 (3); Corning Inc. Advanced-Flow Reactors product brochure (Corning AFR G1, 2007); US patent 7,939,033 'Honeycomb microchannel reactor design'
- **ip status**: patented
- **prior art notes**: Discloses a borosilicate glass microreactor module composed of stacked etched plates with a 'heart-shaped' (HEART) mixing/heat-transfer geometry that produces repeated splitting and recombination of the reagent stream within sub-millimeter channels. Heat-transfer fluid flows in adjacent channels, enabling kW/L heat removal. Anticipates: (a) the heart/teardrop micro-mixer geometry as a manufacturable industrial micromixer with isothermal control of fast exotherms; (b) numbering-up by stacking thin glass plates rather than scale-up by enlarging channels; (c) continuous-flow production-grade reactor with all wetted parts borosilicate glass for chemical compatibility; (d) integration of heat-exchange and reaction in the same fluidic plate using counter-current cross-flow architecture. Should be cited against any later patent claiming heart/teardrop split-and-recombine mixers in stacked glass plates for continuous chemistry.

## HEL FlowCAT continuous catalysis flow reactor (2007)

- **id**: `hel-flowcat-catalysis`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: HEL Group Ltd. (Hertfordshire, UK)
- **disclosure**: HEL Group FlowCAT product brochure 2007; Mahomed, A. (HEL Group) 'FlowCAT: A modular system for continuous catalyst evaluation' Org. Process Res. Dev. 2009, 13, 1284–1290 (cited); HEL FlowCAT user manual rev 5 (2018); product datasheet https://helgroup.com/products/process-development/flowcat-continuous-flow-reactor/
- **ip status**: patented
- **prior art notes**: Discloses (a) parallel trickle-bed catalyst flow reactor system at 4–12 mm tube ID — bridge between true microchannel reactors and conventional fixed-bed catalysis; (b) integrated automation: HPLC pumps, mass flow controllers, back-pressure regulator, all under unified PLC/PC control; (c) 4-up parallel screening with shared utilities for catalyst screening campaigns. Important for prior-art coverage of parallel-flow-reactor screening rigs distinct from droplet-screening; anticipates claims to multi-reactor parallel catalyst-screening platforms with integrated PAT.

## Uniqsis FlowSyn modular flow chemistry reactor (2007)

- **id**: `uniqsis-flowsyn`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Uniqsis Ltd. (Shepreth, Cambridgeshire, UK)
- **disclosure**: Uniqsis Ltd. FlowSyn product launch 2007; Glasnov, T. N.; Kappe, C. O. 'Continuous-flow syntheses of heterocyclic targets' Adv. Synth. Catal. 2010, 352, 3089–3097 (cites FlowSyn); Uniqsis FlowSyn brochure rev 2018; product page https://www.uniqsis.com/paProduct.aspx?ID=FlowSyn
- **ip status**: patented
- **prior art notes**: Discloses an integrated benchtop flow chemistry workstation distinct from Vapourtec/Syrris by virtue of (a) integrated dual HPLC pumps + heated reactor + BPR + collection in single sealed unit (one box rather than rack of cassettes); (b) standardized swappable reactor cartridges spanning coil and chip designs; (c) compatibility with the Polar Bear (separate Cambridge Reactor Design product, distributed by Uniqsis) for cryogenic operation. Useful prior-art entry showing third independent UK commercial flow chemistry rig (alongside Vapourtec, Syrris) demonstrating the integrated-benchtop architecture.

## ThalesNano X-Cube, Phoenix Flow Reactor, Ice-Cube, and Gas Module (2008)

- **id**: `thalesnano-x-cube-phoenix-icecube-gasmodule`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: ThalesNano Inc. (Budapest, HU)
- **disclosure**: ThalesNano Phoenix Flow Reactor launch 2008 (high-T flow up to 450 °C, 200 bar); X-Cube launch 2009; Ice-Cube launch 2014; Gas Module launch 2010; Cantillo, D.; Damm, M.; Kappe, C. O. 'Continuous-flow synthesis of biaryls' J. Org. Chem. 2014, 79, 223–229 (cites X-Cube); Bartrum, H. E. et al. 'Flow-chemistry vs. batch' Tetrahedron 2013, 69, 3279
- **ip status**: patented
- **prior art notes**: Distinct from H-Cube entry. Discloses (a) Phoenix high-T/P 'novel process window' flow reactor enabling chemistry at conditions impossible in batch glass; (b) Ice-Cube integrated Peltier-cooled flow coil for cryogenic flow chemistry (sub-zero organolithium and Grignard); (c) Gas Module providing precision-dosed gaseous-reagent inlet with mass flow control plus back-pressure equilibration, enabling routine CO, H2, O2 chemistry without cylinder safety concerns; (d) the 'novel process window' framing — exploiting transient sub-millimeter heat/mass transport to access chemistry inaccessible to batch. Anticipates patent claims to integrated multi-temperature flow rigs spanning -10 to +450 °C and to gas-dosing modules for continuous flow.

## Microinnova Engineering modular continuous-flow skid (2008)

- **id**: `microinnova-engineering-modular-skid`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Microinnova Engineering GmbH (Graz, AT)
- **disclosure**: Microinnova Engineering GmbH founding 2003 (Graz, Austria); company brochure 'Continuous Process Engineering' 2008; Yaseneva, P.; Yan, Y.; Lapkin, A. 'Continuous-flow synthesis of (+)-2-methyltetrahydrofuran' Chem. Eng. Process. 2017, 122, 67–73 (cites Microinnova); product page https://www.microinnova.com
- **ip status**: patented
- **prior art notes**: Discloses the canonical 'engineering integrator' role for industrial microreactor deployments — a service+hardware vendor that takes Corning AFR or Chemtrix Plantrix plates and packages them with PLC, PAT, ATEX-rated electricals, and CIP/SIP utilities into a deployable plant skid. Anticipates patent claims directed to integrated continuous-flow chemical-process skid architectures with ATEX-zoned containment and SCADA-controlled microreactor plates.

## PowerCell Sweden microchannel fuel processor reformer (2008)

- **id**: `powercell-microchannel-fuel-cell-reformer`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: PowerCell Sweden AB (Gothenburg, SE; Volvo spinout)
- **disclosure**: PowerCell Sweden AB founding 2008 (Volvo SOFC spinout); Karlsson, P.; Lundberg, J.; Sjöstrand, M. 'Diesel-fueled SOFC APU using a microchannel reformer' SAE Technical Paper 2011-01-2271, 2011; PowerCell datasheet rev 2018; Volvo Powertrain microchannel reformer prior art DE19712114A1 1997
- **ip status**: patented
- **prior art notes**: Discloses a diffusion-bonded stainless-steel microchannel autothermal reformer with catalyst-coated reaction channels and parallel combustion channels for in-situ heating, sized for vehicle-APU SOFC integration. Anticipates patent claims directed to integrated microchannel reformer-combustor architectures for distributed hydrogen production. Pairs with Velocys (FT side) and Air Products (steam reforming) to broadly cover the microchannel-reformer prior art.

## Aber Instruments Incyte (Hamilton Incyte) Capacitance Probe (2008)

- **id**: `aber-incyte-capacitance-probe`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Aber Instruments Ltd. (UK; partnered with Hamilton Bonaduz AG for Incyte)
- **disclosure**: Aber Instruments Futura biomass monitor (predecessor) ~2000; Incyte single-use capacitance probe launched as joint Aber/Hamilton product ~2008; US patent US7,930,110B2 (Aber Instruments; biomass monitor based on dielectric spectroscopy); product literature 2010-2023
- **ip status**: patented
- **prior art notes**: Discloses an in-line dielectric-spectroscopy probe that measures capacitance across a sweep of frequencies (typically 0.3-10 MHz); the difference between low-frequency (cell-membrane-charged) and high-frequency (cell-membrane-transparent) capacitance is proportional to the viable biomass volume fraction; signal processing extracts viable-cell-density estimate in real time. The single-use Incyte variant uses a disposable insert-molded electrode head compatible with gamma-irradiation pre-sterilized bioreactors. Anticipates: in-line PAT viable-biomass measurement by multi-frequency dielectric spectroscopy (distinguishable from off-line Coulter, NucleoCounter); single-use disposable probe head as the single-use-bioreactor compatibility solution. Element-by-element: probe body + electrode tip + sweep frequency generator + impedance lock-in + biomass extraction algorithm.

## BlueSens BlueInOne Cell Off-Gas Analyzer (2008)

- **id**: `bluesens-blueinone-offgas`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: BlueSens gas sensor GmbH
- **disclosure**: BlueSens gas sensor GmbH BlueInOne product launch 2008; BlueInOne Cell datasheet rev 2018; US patent US8,691,143B2 (BlueSens, off-gas analysis)
- **ip status**: patented
- **prior art notes**: Discloses a compact off-gas analyzer combining electrochemical O2 measurement and NDIR (non-dispersive infrared) CO2 measurement in a single rack-mount unit, with sample-conditioning (gas drier, particulate filter) integrated; sample gas is drawn from bioreactor exhaust at low flow; OUR/CER calculated from inlet vs outlet partial-pressure difference. Anticipates: combined O2/CO2 off-gas analyzer in a compact form factor suitable for distributed deployment at each bioreactor (vs centralized mass spec); sample-conditioning train integration. Element-by-element: gas inlet + drier + filter + electrochemical O2 cell + NDIR CO2 cell + outlet to atmosphere + RS485/Profibus output.

## Sartorius ambr 15 microbioreactor system (2009)

- **id**: `sartorius-ambr-15`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Sartorius Stedim Biotech (formerly TAP Biosystems)
- **disclosure**: TAP Biosystems (acquired by Sartorius 2013) ambr 15 launch 2009. Bareither, R.; Pollard, D. A review of advanced small-scale parallel bioreactor technology for accelerated process development. Biotechnol. Prog. 2011, 27:2-14. doi:10.1002/btpr.522. Patent family: US8501462B2 (TAP Biosystems; priority 2007).
- **ip status**: patented
- **prior art notes**: Discloses a parallel-array microbioreactor system in which 24-48 single-use stirred-tank vessels of 10-15 mL working volume are simultaneously controlled with individual DO, pH, temperature, and gas-mix feedback, fed and sampled by a robotic pipettor. Anticipates: (a) parallel-microbioreactor process development as a category, including for CGT cell-line characterization; (b) robotic-pipettor-fed parallel small-scale stirred-tank arrays; (c) computer-vision and impedance-based monitoring of individual microbioreactor wells for AI-driven design-of-experiment process optimization.

## Sartorius BioSMB continuous multi-column chromatography (2010)

- **id**: `sartorius-biosmb-continuous-chromatography`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Sartorius / Pall (formerly Tarpon Biosystems)
- **disclosure**: Tarpon Biosystems (acquired by Pall 2015; subsequently part of Sartorius portfolio via Danaher BioPharma divestment) BioSMB launch 2010. Bisschops, M. et al. Single-use, continuous-countercurrent, multicolumn chromatography. BioProcess Int. 2009. Patent family: US8057694B2 (Tarpon Biosystems; priority 2008).
- **ip status**: patented
- **prior art notes**: Discloses a multi-column simulated-moving-bed continuous chromatography platform using a single-use disposable diaphragm-valve manifold rather than traditional metal rotary SMB valves. Anticipates: single-use disposable valve manifolds for continuous chromatography; SMB continuous Protein A capture as a CGT/mAb downstream architecture; multi-column countercurrent chromatography integrated with single-use bioprocess trains.

## Corning Advanced-Flow Reactor G3 (production-scale) (2010)

- **id**: `corning-advanced-flow-reactor-g3`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Corning Incorporated
- **disclosure**: Corning Inc. AFR G3 launch announcement (Achema 2009 / 2010 product release); Buisson, B.; Donegan, S.; Wray, D.; Parracho, A.; Gamoudi, J.; Bonny, M.; Guermeur, S. 'Slurry hydrogenation in a continuous flow reactor for pharmaceutical application' Chimica Oggi/Chemistry Today 2009, 27 (6) Suppl; Corning AFR G3 product datasheet rev 2010
- **ip status**: patented
- **prior art notes**: Production-scale numbering-up of the AFR G1 architecture: same heart-shaped channel motif, scaled to ~1 mm hydraulic diameter and ~25× footprint. Discloses (a) industrial-throughput borosilicate microreactor at multi-hundred-gram-per-minute regime; (b) modular stacking with shared heat-transfer manifolds; (c) compatibility with slurries (catalytic hydrogenation, crystallization-onset reactions) within microchannels — historically considered impossible. Anticipates patent claims directed to 'stacked plate microreactor for continuous pharmaceutical manufacturing at multi-tonne scale'. Pairs with G1 entry for full numbering-up disclosure.

## Syrris Asia and Asia 320 modular flow chemistry platform (2010)

- **id**: `syrris-asia-platform`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Syrris Ltd. (Blacktrace Holdings, now Asynt)
- **disclosure**: Syrris Ltd. Asia product launch press release, June 2010; Asia 320 launch 2017; Syrris Asia user manual rev 4 (2014); product brochure https://syrris.com/products/asia-flow-chemistry/
- **ip status**: patented
- **prior art notes**: Distinct from base Syrris-flow-chemistry entry. Discloses (a) 'pressurized-syringe' pump with sealed reservoir and electronic pressure feedback eliminating pulsation typical of HPLC pumps; (b) the FLLEX inline liquid-liquid extraction unit using a hydrophobic porous PTFE membrane to phase-separate organic and aqueous flows continuously without settling tanks; (c) Asia 320 ultra-high-pressure variant for supercritical-like flow chemistry; (d) modular architecture with shared 19-inch rack and tablet-based control software. Anticipates patent claims to pressurized-reservoir pulsation-free pumps for flow chemistry, and to inline membrane LLE within the residence-time loop of a flow reactor.

## Cambridge Reactor Design Polar Bear and Polar Bear Plus flow chemistry chiller (2010)

- **id**: `cambridge-reactor-design-polar-bear-plus`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Cambridge Reactor Design Ltd. (Cambridge, UK)
- **disclosure**: Cambridge Reactor Design Ltd. Polar Bear product launch 2010; Browne, D. L.; Wright, S.; Deadman, B. J.; Dunnage, S.; Baxendale, I. R.; Turner, R. M.; Ley, S. V. 'Continuous flow processing of slurries: evaluation of an agitated cell reactor' Rapid Commun. Mass Spectrom. 2012, 26, 1999–2006 (cites Polar Bear); CRD Polar Bear Plus datasheet 2013; product page https://cambridgereactordesign.com
- **ip status**: patented
- **prior art notes**: Discloses a self-contained thermoelectric chiller capable of -78 °C wraparound jacketing for fluoropolymer-tubing flow reactors — the practical solid-state alternative to dry-ice or liquid-nitrogen baths for cryogenic flow chemistry. Anticipates: (a) thermoelectric-stack (multi-stage Peltier) module integrated into a chiller form factor for laboratory flow chemistry; (b) the universal-fit wraparound jacket pattern that accepts any user-wound reactor coil; (c) the 'no consumables coolant' architecture (no LN2, no dry ice) for routine cryogenic flow chemistry. Anticipates patent claims to thermoelectric-stack chillers wraparound to fluoropolymer flow reactors at -78 °C.

## AMTechnology Coflore ATR oscillatory baffled flow reactor (2010)

- **id**: `amtechnology-coflore-atr`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: AM Technology Ltd. (Runcorn, UK)
- **disclosure**: AM Technology Coflore ATR launch 2010; Browne, D. L.; Deadman, B. J.; Ashe, R.; Baxendale, I. R.; Ley, S. V. 'Continuous flow processing of slurries: evaluation of an agitated cell reactor' Org. Process Res. Dev. 2011, 15, 693–697; Coflore ATR product brochure rev 2015
- **ip status**: patented
- **prior art notes**: Borderline microfluidic but included for prior-art coverage — the oscillatory-baffled-reactor (OBR) architecture provides radial-mixing decoupled from net axial flow, achieving plug-flow with relatively large (~cm) cells. Discloses (a) the agitated-cell-reactor as solid-tolerant alternative to PFR microreactors clogged by suspended solids; (b) the practical mechanical-oscillation architecture (whole-reactor reciprocation rather than baffle motion); (c) industrial deployment for crystallization, biocatalysis, and polymerization in continuous flow. Anticipates patent claims to mechanically oscillated baffled flow reactors for continuous slurry-handling chemistry.

## Charles River Laboratories Cobra Plasmid Manufacturing Platform (2010)

- **id**: `charles-river-cobra-plasmid`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Cobra Biologics (acquired 2021 by Charles River Laboratories)
- **disclosure**: Charles River Laboratories acquired Cobra Biologics 2021-02; Cobra Biologics plasmid manufacturing public disclosures 2010-2020 including Cobra ORT operator-repressor titration patent US7,943,377B2 (Cobra Biologics, ORT antibiotic-free plasmid selection)
- **ip status**: patented
- **prior art notes**: Process disclosure for GMP plasmid DNA manufacturing: high-density E. coli fermentation under ORT antibiotic-free selection → alkaline lysis (often in a continuous static-mixer lysis skid, microfluidic in laminar regime) → flocculation → tangential-flow filtration → anion-exchange chromatography → hydrophobic-interaction polishing → 0.2 µm sterile filtration → fill. The microfluidic content is the in-line static-mixer lysis architecture and the TFF skid. Anticipates: continuous in-line alkaline-lysis plasmid manufacturing using laminar-mixing static elements rather than batch lysis tanks; antibiotic-free plasmid selection (ORT) as a strain-engineering precondition for CGT-grade plasmid.

## Pall iCellis Fixed-Bed Bioreactor (Nano / 500) (2010)

- **id**: `pall-icellis-fixed-bed`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Artelis SA (acquired 2010 by Pall Corporation; Pall acquired by Danaher 2015)
- **disclosure**: Artelis (acquired 2010 by Pall) iCellis product launch 2010; US patent US8,278,101B2 (Disposable bioreactor with packed bed for cell culture, Artelis/Pall, priority 2008); EP2186881B1
- **ip status**: patented
- **prior art notes**: Discloses a single-use fixed-bed bioreactor where a non-woven PET fiber matrix provides high specific surface area (>30,000 m²/m³) for adherent cell culture; an internal magnetic impeller drives medium recirculation through the matrix providing both nutrient delivery and oxygenation; perfusion or batch operation is supported. Anticipates: PET-fiber random-packing fixed-bed bioreactor architecture for adherent cell culture (distinguishable from Univercells scale-X structured packing); single-use thermoformed vessel format for viral vector production; the Nano-to-500 scale chain that allows DOE in Nano to inform commercial 500 manufacture.

## Hamilton Arc Intelligent Sensors (pH, DO, ORP, conductivity) (2010)

- **id**: `hamilton-arc-sensors`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Hamilton Bonaduz AG
- **disclosure**: Hamilton Bonaduz AG Arc sensor platform launch 2010; Hamilton Arc View 3 product datasheet; product literature 2012-2023
- **ip status**: patented
- **prior art notes**: Discloses an intelligent-sensor architecture where the calibration data, signal conditioning electronics, and digital communication interface are all resident in the probe head, allowing the probe to be moved between transmitters without recalibration. The VisiFerm DO variant uses an optical-spot fluorescence-quenching architecture in which a luminophore is excited and the lifetime of fluorescence quenching is proportional to dissolved oxygen — supports both stainless and single-use (patch) form factors. Anticipates: digital intelligent-sensor architecture for bioprocess PAT (distinguishable from analog probes whose calibration lives in the transmitter); luminescence-lifetime DO measurement compatible with single-use bioreactor patch sensors.

## Sartorius BioPAT Process Analytical Technology Suite (2010)

- **id**: `sartorius-biopat-pat-framework`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Sartorius AG
- **disclosure**: Sartorius BioPAT product line introduced ~2010 with BioPAT MFCS SCADA; BioPAT ViaMass capacitance launched 2018; Sartorius product literature 2010-2023
- **ip status**: patented
- **prior art notes**: Discloses a vertically-integrated PAT framework where multiple in-line probes (capacitance, Raman, DO, pH) feed a unified SCADA layer (BioPAT MFCS) that supports model-based and closed-loop process control. Anticipates: the architectural pattern of treating PAT as a software-integrated suite rather than a collection of independent probes; closed-loop bioprocess control where a probe-derived state (cell density, glucose concentration) directly modulates a feed pump. Element-by-element: probe array + transmitter rack + MFCS SCADA + closed-loop controller + bioreactor actuator (feed pump, gas valve).

## Solaris Biotech Jupiter Bioreactor / Fermenter (2010)

- **id**: `solaris-jupiter-custom-bioreactor`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Solaris Biotech Solutions S.r.l. (acquired 2021 by Donaldson)
- **disclosure**: Solaris Biotech Solutions S.r.l. Jupiter bioreactor product literature ~2010; company website; acquired by Donaldson 2021
- **ip status**: trade-secret
- **prior art notes**: Discloses a customer-configurable head-plate bench bioreactor system with Solaris's Leonardo SCADA control software providing scale-down/scale-up workflow continuity from Jupiter (bench) through Tetra (pilot) to Saturn (production). Anticipates: customer-configurable head-plate architecture as a flexibility primitive (vs fixed Sartorius/Eppendorf head plates); shared SCADA across scale ladder. Trade-secret heavy; entry rests on company literature.

## Bruker MATRIX-MF In-Line FTIR PAT Spectrometer (2010)

- **id**: `bruker-matrix-mf-ftir-pat`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Bruker Optics (Germany/USA)
- **disclosure**: Bruker Optics MATRIX-MF product brochure 2010; De Beer, T. R. et al. 'In-line and real-time process monitoring of a freeze drying process using Raman and NIR spectroscopy as complementary process analytical technology (PAT) tools.' Journal of Pharmaceutical Sciences 98, 3430-3446 (2009), doi:10.1002/jps.21633
- **ip status**: patented
- **prior art notes**: Discloses the Bruker MATRIX-MF process FTIR spectrometer with rugged stainless-steel pharmaceutical-process-grade housing and multi-fiber optical interface. Anticipates: (a) ruggedized process FTIR spectrometers for in-line PAT installation in continuous-manufacturing skids; (b) multi-fiber single-spectrometer architecture for parallel multi-point process monitoring; (c) the integration template into GEA ConsiGma and similar continuous-tableting lines. Cite against later patents claiming multi-fiber single-spectrometer FTIR PAT instruments.

## Mettler-Toledo ParticleTrack G400 FBRM Probe (2010)

- **id**: `mettler-toledo-particletrack-g400-fbrm`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Mettler-Toledo AutoChem (formerly Lasentec)
- **disclosure**: Mettler-Toledo ParticleTrack G400 product brochure 2010-2014; Pearson, A. P. et al. 'Use of FBRM (focused beam reflectance measurement) to monitor particle size and shape during industrial pharmaceutical crystallization.' Crystal Growth & Design 11, 4806-4811 (2011), doi:10.1021/cg200591k
- **ip status**: patented
- **prior art notes**: Discloses the Lasentec/Mettler ParticleTrack G400 FBRM probe - the canonical in-line particle-size PAT tool for pharmaceutical crystallization. The probe rotates a focused laser beam at fixed velocity through a sapphire window in contact with the suspension; backscatter pulses time-of-flight maps to chord lengths via CLD (chord length distribution) analysis. Anticipates: (a) FBRM as an in-line particle-size measurement technique for pharmaceutical crystallization PAT; (b) sapphire-window high-pressure probe architectures for in-process particle monitoring; (c) the architectural integration of FBRM with PVM (particle vision microscope) for combined size+shape analysis; (d) automated phase-identification algorithms for nucleation/growth/agglomeration crystallization stages. Cite against later patents claiming rotating-laser FBRM probes with sapphire windows for in-line crystallization.

## BlueSens BlueInOne FERM Off-Gas Analyzer (2010)

- **id**: `bluesens-blueinone-ferm-offgas`
- **corpus**: private
- **device class**: flow-controller
- **creator**: BlueSens gas sensor GmbH (Germany)
- **disclosure**: BlueSens BlueInOne FERM product brochure (BlueSens gas sensor GmbH 2010-2014); Schaepe, S. et al. 'Bioprocess monitoring using off-gas analysis.' Engineering in Life Sciences 13, 549-558 (2013), doi:10.1002/elsc.201200103
- **ip status**: patented
- **prior art notes**: Discloses the BlueSens BlueInOne FERM off-gas analyzer combining zirconia O2 and NDIR CO2 sensors in a compact bioreactor-mounted unit. Anticipates: (a) compact dual-sensor (O2+CO2) off-gas analyzer architecture replacing rack-mount mass spectrometers for bioreactor exhaust monitoring; (b) integrated OUR/CER/RQ calculation in the analyzer firmware; (c) the same analyzer architecture scaling from shake-flask to production bioreactor. Cite against later patents claiming compact dual-sensor zirconia-NDIR off-gas analyzers with on-board OUR/CER/RQ calculation.

## GSK / CMAC Strathclyde continuous-flow API manufacturing platform (2011)

- **id**: `gsk-strathclyde-cmac-continuous-api`
- **corpus**: academic
- **device class**: lab-on-chip
- **creator**: Centre for Innovative Manufacturing in Continuous Manufacturing and Crystallisation (CMAC), University of Strathclyde, in collaboration with GSK and 7 pharma companies
- **disclosure**: Florence, A. J.; Johnston, A.; Price, S. L.; Nowell, H.; Kennedy, A. R.; Shankland, K. EPSRC Centre for Innovative Manufacturing in Continuous Manufacturing and Crystallisation (CMAC) launch, University of Strathclyde, 2011; Cole, K. P. et al. 'Kilogram-scale prexasertib monolactate monohydrate synthesis under continuous-flow CGMP conditions' Science 2017, 356, 1144–1150 (Eli Lilly + CMAC collaboration); CMAC Hub annual report 2015–2020
- **ip status**: patented
- **prior art notes**: CMAC is the principal UK academic-industrial vehicle for continuous-API process development. Discloses (a) the canonical 'continuous-from-step-1-to-API' process map for small-molecule drug substance manufacturing; (b) continuous MSMPR cascade crystallization with PAT-driven control; (c) kg-scale CGMP-grade continuous flow demonstrated in the published Lilly prexasertib paper (Science 2017); (d) the consortium model in which 7 pharma companies share IP and process methods through the CMAC framework. Anticipates many process-method claims directed to 'continuous synthesis-crystallization-isolation of [small molecule API]' that have begun to appear in pharma patent literature 2018–2024.

## Continuus Pharmaceuticals Integrated Continuous Manufacturing (ICM) platform (2012)

- **id**: `continuus-pharmaceuticals-icm`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Continuus Pharmaceuticals (MIT/Novartis CCM spinout, Woburn MA)
- **disclosure**: Mascia, S.; Heider, P. L.; Zhang, H.; Lakerveld, R.; Benyahia, B.; Barton, P. I.; Braatz, R. D.; Myerson, A. S.; Trout, B. L.; Evans, J. M. B.; Jamison, T. F.; Jensen, K. F. 'End-to-end continuous manufacturing of pharmaceuticals: integrated synthesis, purification, and final dosage formation' Angew. Chem. Int. Ed. 2013, 52, 12359–12363; Continuus Pharmaceuticals founding 2012 (MIT/Novartis spinout); FDA Emerging Technology Program ICM submission 2017
- **ip status**: patented
- **prior art notes**: Direct industrial descendant of the Novartis-MIT Center for Continuous Manufacturing (CCM, 2007–2017). Discloses (a) the first end-to-end (raw-material to tablet) continuous-pharmaceutical manufacturing line operating commercially-relevant volumes; (b) integration of continuous reaction (PFR), continuous mixed-suspension-mixed-product-removal (MSMPR) crystallizer, continuous filter-dryer, continuous tablet press; (c) PAT-driven real-time release replacing batch QA holds; (d) sub-100-m² compact-plant footprint as an architectural goal. Anticipates patent claims to end-to-end CM-pharma plants combining PFR + MSMPR + filter-dryer + tableting under unified PAT control.

## Eppendorf BioBLU Single-Use Bioreactor (0.3c / 3c / 10c / 50c) (2012)

- **id**: `eppendorf-bioblu-single-use`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Eppendorf AG (formerly New Brunswick Scientific)
- **disclosure**: Eppendorf (formerly New Brunswick Scientific) BioBLU product launch 2012; BioBLU rigid single-use vessel patent US9,243,217B2; Eppendorf product literature 2014-2023
- **ip status**: patented
- **prior art notes**: Discloses a rigid plastic single-use bioreactor vessel with insert-molded impeller shaft, sparger ring, sensor ports (optical patches for pH/DO compatible), and harvest dip tube; the rigid form preserves the stirred-tank impeller-driven mixing characteristics of glass/stainless vessels (vs flexible-bag SUB which requires wave/rocker mixing). Anticipates: rigid-plastic single-use bioreactor architecture as alternative to flexible-bag SUB for stirred-tank workflows; the scaling chain (0.3c through 50c) preserving impeller geometry and aspect ratio. Distinguishable from Sartorius BIOSTAT STR (flexible bag) and Cytiva Xcellerex XDR (flexible bag) by being a rigid molded vessel.

## HEL FlexFermentor Parallel Bioreactor System (2012)

- **id**: `hel-flexfermentor-parallel-bioreactor`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: HEL Group
- **disclosure**: HEL Group FlexFermentor product literature ~2012; HEL Group company website; sister product to HEL FlowCAT (already in corpus)
- **ip status**: trade-secret
- **prior art notes**: Process-development scale parallel bioreactor system with 4-8 independently-controlled small-volume vessels; addresses the DOE-throughput gap between single shake flask and single bench bioreactor. Anticipates: parallel small-scale bioreactor architecture for fermentation DOE (overlapping with Sartorius ambr 250 and Eppendorf DASGIP, distinguishable by glass-vessel format and HEL's WinISO control system). Trade-secret heavy on the controls; entry strength rests on product literature.

## Continuous flow chemistry review (Ley 2013) (2013)

- **id**: `ley-2013-flow-chemistry-pharma-review`
- **corpus**: academic
- **device class**: other
- **creator**: Ley group, Cambridge
- **disclosure**: Ley, S. V.; Fitzpatrick, D. E.; Ingham, R. J.; Myers, R. M. Organic synthesis: march of the machines. Angew. Chem. Int. Ed. 2015, 54, 3449–3464. DOI: 10.1002/anie.201410744
- **ip status**: public-domain
- **prior art notes**: Ley-group review of automation and continuous flow chemistry in organic synthesis. The canonical reference for the integration of continuous-flow microfluidic reactors with automated reagent dispensing, real-time analytics, and machine learning for process optimization. Companion to Reizman 2015 self-optimizing flow chemistry.

## Sartorius ambr 250 high-throughput single-use bioreactor (2013)

- **id**: `sartorius-ambr-250`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Sartorius Stedim Biotech
- **disclosure**: TAP Biosystems / Sartorius ambr 250 launch 2013. Tai, M. et al. ambr 250 use in CHO cell process development. Biotechnol. Prog. 2015, 31:1388-1395. doi:10.1002/btpr.2142. Patent family extends from US8501462B2.
- **ip status**: patented
- **prior art notes**: Mid-scale parallel-array stirred-tank microbioreactor system bridging the ambr 15 and pilot-scale bioreactors. Anticipates: scale-down models of 2000 L commercial bioreactors implemented as parallel 100-250 mL single-use vessels with matched mixing and aeration characteristics, used as the FDA-recognized scale-down qualification approach for bioprocess development. The ambr 250 HT perfusion variant additionally anticipates integration of single-use cell-retention devices (ATF/TFF) into a parallel-array small-scale platform.

## ABEC Custom Single-use Bioreactor (CSR) / Custom Stainless Steel Bioreactor (CSSB) (2013)

- **id**: `abec-cssb-custom-stainless-bioreactor`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: ABEC Inc.
- **disclosure**: ABEC Inc. CSR product launch ~2013; ABEC patent estate US9,988,605B2 (Single-use bioreactor and methods); ABEC Inc. company literature 2018-2023
- **ip status**: patented
- **prior art notes**: Discloses a custom-engineered single-use bioreactor where the stainless-steel jacket is custom-fabricated for the client's chosen impeller geometry, sensor port array, and cell-density target, and the disposable bag liner is welded to match. Microfluidic content is in the sparger/impeller flow distribution geometry, the in-line PAT sensor manifolds, and the harvest/feed port architecture. Anticipates: single-use bioreactor scaling to 6000 L (significantly above prior Sartorius/Cytiva SUB ceilings of ~2000 L); custom-engineered jacket-and-bag pairing as a manufacturing model. Element-by-element: jacket + impeller + sparger + PAT manifold + harvest line + bag liner.

## Sartorius Flexsafe RM single-use rocking bag and BIOSTAT RM (2014)

- **id**: `sartorius-flexsafe-rm`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Sartorius Stedim Biotech
- **disclosure**: Sartorius Stedim Biotech BIOSTAT RM and Flexsafe RM bag launch 2014. Sartorius Application Note SBI4029-e. Patent family: US9217131B2 (Sartorius; priority 2010).
- **ip status**: patented
- **prior art notes**: Discloses Sartorius single-use rocking bioreactor line (BIOSTAT RM) with Flexsafe polymer-film bags. Anticipates: extensible-film single-use rocking bioreactor architectures with in-bag optical DO/pH and capacitance sensors; CGT-validated extractables/leachables polymer-film formulations. Sister to the Cytiva Xuri line.

## Corning Advanced-Flow Reactor G4 (silicon-carbide) (2014)

- **id**: `corning-advanced-flow-reactor-g4-sic`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Corning Incorporated
- **disclosure**: Corning Inc. press release 'Corning Advanced-Flow G4 SiC Reactor', Achema 2015; Roberge, D. M.; Gottsponer, M.; Eyholzer, M.; Kockmann, N. 'Industrial design, scale-up, and use of microreactors' Chimica Oggi 2009, 27 (4); SiC AFR product brochure 2014–2015
- **ip status**: patented
- **prior art notes**: Discloses a sintered silicon-carbide industrial microreactor with the same heart-shape mixer motif as the borosilicate G1/G3 generations but with thermal conductivity ~300× higher than glass and chemical compatibility extended to fluorinations, nitrations, and concentrated mineral acids. Anticipates: (a) industrial SiC microreactor as practical hardware (vs research only); (b) microreactor architectures for diazomethane, fluorination, and oleum-mediated chemistries at production scale; (c) integration of high-thermal-conductivity ceramic substrates with stacked-plate heat-exchange architectures. Pairs with G3 entry to disclose the full glass-to-ceramic substrate transition for industrial flow chemistry.

## Vapourtec R-Series with UV-150 photochemical reactor and V-3 peristaltic pump (2014)

- **id**: `vapourtec-r-series-uv-150`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Vapourtec Ltd.
- **disclosure**: Vapourtec UV-150 photochemical reactor product launch 2014; Williams, J. D.; Nakano, M.; Gérardy, R.; Rincón, J. A.; García-Losada, P.; Mateos, C.; Hawkins, J. M.; Jensen, K. F.; Monbaliu, J.-C. M.; Kappe, C. O. 'Finding the perfect match: a combined computational and experimental study toward efficient and scalable photosensitized [2+2] cycloadditions in flow' Org. Process Res. Dev. 2019, 23, 78–87; Vapourtec V-3 peristaltic pump datasheet 2017
- **ip status**: patented
- **prior art notes**: Distinct from base vapourtec-flow-chemistry entry. Discloses (a) jacketed-tubing photochemical reactor architecture, with FEP tubing wound on quartz immersion well, swappable medium-pressure mercury or LED lamp; (b) integration of slurry-tolerant peristaltic V-3 pump within the same R-series electrical/communication backbone, enabling solid-handling reactions in continuous flow that historically required batch reactors; (c) the architectural pattern of plug-and-play modules sharing a USB-controlled bus. Anticipates patent claims directed to fluoropolymer-tubing photoreactors with switchable-wavelength lamp jackets, and to slurry-tolerant peristaltic pumps integrated into commercial flow chemistry rigs.

## Snapdragon Chemistry continuous-manufacturing platform (acquired by Cambrex 2021) (2014)

- **id**: `snapdragon-cambrex-continuous-manufacturing`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Snapdragon Chemistry Inc. (now Cambrex Boston)
- **disclosure**: Snapdragon Chemistry Inc. founding 2014 (Boston, MA); company acquired by Cambrex 13 May 2021 (Cambrex press release); Snapdragon FoxFire continuous-process control platform technical white paper 2019; Mo, Y.; Jensen, K. F. 'A miniature CSTR cascade for continuous flow of reactions containing solids' React. Chem. Eng. 2016, 1, 501–507 (founding-team work)
- **ip status**: patented
- **prior art notes**: Discloses (a) miniature-CSTR cascade as a slurry-tolerant alternative to plug-flow microchannel reactors, addressing the canonical PFR limitation that suspended solids clog sub-millimeter channels; (b) integration with multivariate inline PAT (FTIR/Raman/UV-Vis) for continuous-process control; (c) the CDMO business model in which a contract organization performs flow-chemistry process development, scale, and manufacturing for a pharma client end-to-end. Anticipates patent claims directed to mini-CSTR cascade reactors with integrated multimodal PAT, and to the integrated continuous-API CDMO service architecture.

## AmAr Equipments continuous-flow microreactor skid (2014)

- **id**: `amar-equipments-microreactor-skid`
- **corpus**: private
- **device class**: flow-controller
- **creator**: AmAr Equipments Pvt. Ltd.
- **disclosure**: AmAr Equipments Pvt. Ltd. (Mumbai, IN) microreactor product brochure 2014; AmAr Equipments 'Continuous Flow Reactor systems' application note rev 2018; product page https://www.amarequip.com/continuous-flow-microreactor.html
- **ip status**: unknown
- **prior art notes**: Discloses an Indian-domiciled microreactor skid integrator analogous to Microinnova in Europe. Important commons entry because (a) Indian API CDMOs (Sun Pharma, Aurobindo, Dr. Reddy's, Cipla) host a substantial fraction of the world's continuous-flow API manufacturing; (b) AmAr microreactor skids cite no patents in marketing literature, suggesting commodity/derivative design; (c) the existence of cost-engineered Indian-supplied microreactor hardware is itself prior art that limits patentability of the skid integration. Anticipates patent claims directed to standardized SS316/Hastelloy plate-and-frame microreactor skids for pharmaceutical CDMO use.

## Pfizer Portable Continuous Miniature and Modular (PCMM) plant (2014)

- **id**: `pfizer-pcmm-portable-on-demand`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Pfizer Inc., GSK, G-CON Manufacturing (consortium)
- **disclosure**: Pfizer / GSK / G-CON Manufacturing PCMM joint announcement May 2014; Reid, P. 'PCMM: A new paradigm for pharmaceutical manufacturing' Pharma. Eng. 2015, 35 (5), 38–46; G-CON PCMM technical description; FDA pre-submission meeting docs 2016
- **ip status**: patented
- **prior art notes**: Discloses the 'plant-in-a-box' architecture for continuous pharmaceutical manufacturing — a prefabricated cleanroom POD with standardized utilities and integrated continuous-OSD line, shippable as a unit and re-siteable. Anticipates patent claims directed to: (a) modular shippable GMP cleanroom POD architectures; (b) multi-pharma-vendor consortium standardization on a common POD footprint; (c) site-redeployable continuous manufacturing facilities as a capital-efficiency strategy. Important prior-art entry for the broader 'distributed manufacturing' thesis that informs On Demand Pharmaceuticals and the DARPA Make-It program.

## Touchlight Genetics doggybone DNA (dbDNA) Synthesis (2014)

- **id**: `touchlight-doggybone-dna-microfluidic`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Touchlight Genetics Ltd.
- **disclosure**: Walters et al., Nucleic Acids Res 42:e10 (2014) doi:10.1093/nar/gkt1101 (foundational dbDNA paper); EP2820164B1 priority 2012
- **ip status**: patented
- **prior art notes**: Discloses a continuous-flow microfluidic-bioprocess platform that performs phi29-mediated RCA followed by TelN protelomerase resolution to produce covalently-closed linear dsDNA without bacterial fermentation. Anticipates: chip-scale or skid-scale bioprocess architectures that combine RCA with enzymatic resolution to produce non-plasmid dsDNA therapeutics; replacement of E. coli-based plasmid manufacturing with controlled enzymatic flow processes; integration of in-line analytical sensing with sterile single-use process loops for nucleic-acid manufacturing.

## Cytiva FlexFactory for Cell Therapy (2014)

- **id**: `cytiva-flexfactory-cell-therapy`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Cytiva (formerly GE Healthcare Life Sciences)
- **disclosure**: GE Healthcare Life Sciences (now Cytiva) FlexFactory product launch 2014; Cytiva FlexFactory product literature 2020-2023; Cytiva US patents on Xcellerex bioreactor controls
- **ip status**: patented
- **prior art notes**: Process disclosure: facility-level integration of Cytiva's portfolio (Sefia + Xuri + Xcellerex + AKTA + Allegro + Chronicle SCADA) into a single CGT manufacturing line. Microfluidic content is the cumulative content of the integrated unit operations (each separately covered in the corpus); the FlexFactory disclosure adds the connectivity, sterile-weld topology, and SCADA orchestration. Anticipates: single-vendor turnkey CGT facility composed of pre-validated single-use sub-systems with a unified audit-trail control layer. Distinguishable from Lonza Cocoon (single-cassette per-patient) by being a multi-station modular facility rather than a closed-cassette device.

## Mettler-Toledo ReactIR 700 / 7000 In-Line FTIR (2014)

- **id**: `mettler-toledo-reactir-700-7000-ftir`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Mettler-Toledo AutoChem (USA/Switzerland)
- **disclosure**: Mettler-Toledo ReactIR 7000 product brochure 2014-2018; Carter, C. F. et al. 'ReactIR Flow Cell: A New Analytical Tool for Continuous Flow Chemical Processing.' Organic Process Research & Development 14, 393-404 (2010), doi:10.1021/op900305v
- **ip status**: patented
- **prior art notes**: Discloses the Mettler-Toledo ReactIR family of process FTIR spectrometers with diamond/silicon/AgX ATR flow-cell probes purpose-built for continuous-flow chemistry monitoring. Anticipates: (a) diamond-ATR flow-cell architecture for high-pressure continuous-flow FTIR; (b) silicon and silver halide alternative ATR materials for IR-window spectral-range trade-offs; (c) integrated kinetic-profiling software (iC IR) closing feedback-control loops on flow-chemistry reactors; (d) the de facto industry-standard PAT tool for academic and industrial flow-chemistry labs (Vapourtec, Syrris, Uniqsis, etc. all certify ReactIR integration). Cite against later patents claiming diamond-ATR flow-cell FTIR for continuous-flow chemistry.

## Beta Bionics iLet Bionic Pancreas (2014-06-15)

- **id**: `beta-bionics-ilet-bionic-pancreas`
- **corpus**: private
- **device class**: pump-component
- **creator**: Beta Bionics Inc.
- **disclosure**: Russell SJ et al. N Engl J Med 371(4):313-325 2014 doi:10.1056/NEJMoa1314474; FDA 510(k) K223846 May 2023
- **ip status**: patented
- **prior art notes**: Discloses an automated closed-loop insulin (or insulin+glucagon) delivery system with simplified user interface (weight-only initialization) and adaptive control. The pumping mechanism uses prefilled microliter-resolution cartridges. Anticipates: zero-input bionic-pancreas closed-loop architectures; the user-experience pattern of weight-only initialization for an autonomous pump; bi-hormonal microliter glucagon delivery alongside insulin.

## Self-optimizing continuous flow chemistry (2015)

- **id**: `reizman-2015-self-optimizing-flow`
- **corpus**: academic
- **device class**: flow-controller
- **creator**: Jensen group, MIT / Buchwald, MIT
- **disclosure**: Reizman, B. J.; Wang, Y.-M.; Buchwald, S. L.; Jensen, K. F. Suzuki–Miyaura cross-coupling optimization enabled by automated feedback. React. Chem. Eng. 2016, 1, 658–666. DOI: 10.1039/C6RE00153J
- **ip status**: public-domain
- **prior art notes**: Disclosed automated feedback-controlled flow chemistry combining continuous flow microreactors, inline analytics (HPLC), and Bayesian-style optimization to autonomously identify reaction conditions. Anticipates: closed-loop autonomous reaction optimization, AI-controlled microfluidic process analytical technology (PAT), and the entire 'self-driving labs' framing that became a major area of automated discovery research.

## Asynt fReactor multi-stage CSTR flow reactor (2015)

- **id**: `asynt-freactor`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Asynt Ltd. (Cambridge, UK), invented at Univ. Leeds Bourne group
- **disclosure**: Asynt Ltd. fReactor product launch 2015; Reay, A. J.; Hammond, J. M.; Bourne, J.; Lee, M.; Smith, M. B. 'Reactor characterization for use in active fermentation' (uses fReactor); Asynt fReactor datasheet rev 3 (2018); product page https://www.asynt.com/product/freactor/
- **ip status**: patented
- **prior art notes**: Discloses (a) a low-cost 3D-printed cascade of mini-CSTRs with magnetic stirring as an academic-affordable alternative to Snapdragon-style CSTR cascades; (b) magnetic-coupled stirring in each cell (no shaft seals) enabling closed continuous operation; (c) the design pattern of 'inexpensive 3D-printed flow chemistry hardware for academic adoption'. Anticipates patent claims to magnetically stirred mini-CSTR cascade reactors and to 3D-printed multi-cell continuous reactors for academic flow chemistry.

## Sartorius BioPAT MFCS / Biostat Bioprocess Analytics (2015)

- **id**: `sartorius-bioprocess-analytics-bionet`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Sartorius Stedim Biotech (Germany)
- **disclosure**: Sartorius BioPAT MFCS-DA product brochure 2015-2019; Glassey, J. et al. 'Process analytical technology (PAT) for biopharmaceuticals.' Biotechnology Journal 6, 369-377 (2011), doi:10.1002/biot.201000356
- **ip status**: patented
- **prior art notes**: Discloses the Sartorius BioPAT MFCS-DA bioprocess analytics platform - the unifying PAT software stack across the Sartorius bioreactor portfolio. Anticipates: (a) OPC-UA/OPC-DA standardized PAT-probe-to-DCS integration architectures for biopharmaceutical manufacturing; (b) MVDA-driven golden-batch comparison as an in-process release strategy for biologics; (c) the unified software stack pattern enabling consistent PAT integration from R&D ambr-15 through GMP STR-2000. Cite against later patents claiming OPC-UA-standardized bioprocess PAT integration with MVDA golden-batch comparison.

## Vaisala Viewpoint Humidity Monitoring for Tableting (2015)

- **id**: `vaisala-viewpoint-tableting-humidity`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Vaisala Oyj (Finland)
- **disclosure**: Vaisala Viewpoint product brochure 2015-2020; Vaisala HMP110/HMP60/HMT330 datasheet for pharmaceutical applications 2015
- **ip status**: patented
- **prior art notes**: Discloses the Vaisala Viewpoint humidity-monitoring infrastructure widely deployed in pharmaceutical tableting and continuous-manufacturing facilities. Anticipates: (a) wireless 21 CFR Part 11-compliant humidity-monitoring infrastructure for clean-rooms; (b) HMT330 in-process humidity probes for fluid-bed dryer outlet monitoring as a PAT-adjacent measurement; (c) centralized cloud-aware monitoring of pharmaceutical environmental conditions. Cite against later patents claiming 21 CFR Part 11-compliant wireless humidity monitoring for pharmaceutical environments.

## Continuous-flow pharmaceutical manufacturing on chip (Jensen 2016 MIT spinout-driven) (2016)

- **id**: `adamo-2016-continuous-pharma-mit`
- **corpus**: academic
- **device class**: flow-controller
- **creator**: Jensen group, MIT
- **disclosure**: Adamo, A. et al. On-demand continuous-flow production of pharmaceuticals in a compact, reconfigurable system. Science 2016, 352, 61–67. DOI: 10.1126/science.aaf1337
- **ip status**: patented
- **prior art notes**: Demonstrated end-to-end continuous-flow synthesis of four small-molecule pharmaceuticals (lidocaine, diphenhydramine, fluoxetine, diazepam) on a 1-meter benchtop system integrating reaction modules, separations, and crystallization. Anticipates: end-to-end continuous-flow pharmaceutical manufacturing in compact reconfigurable form factor, and the architectural goal of distributed pharmaceutical manufacturing that informs the FDA Pharmaceutical Quality for the 21st Century framework.

## Ineratec PtX microreactor for e-fuels and Power-to-Liquid (2016)

- **id**: `ineratec-ptx-microreactor`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Ineratec GmbH (KIT spinout)
- **disclosure**: Ineratec GmbH founding 2016 from Karlsruhe Institute of Technology spinout; Loewert, M.; Pfeifer, P. 'Microstructured Fischer-Tropsch reactor scale-up and opportunities for decentralized application' Chem. Ing. Tech. 2020, 92, 696–708; Ineratec product release 'P2X container' 2018; INERATEC Atmosfair pilot plant commissioning 2021 Werlte, Germany
- **ip status**: patented
- **prior art notes**: Direct descendant of Velocys's microchannel-FT architecture, but optimized for e-fuel/PtX rather than gas-to-liquids: (a) discloses containerized modular packaging of microchannel FT and methanol synthesis plus reverse-water-gas-shift (RWGS) into shipping-container-sized standardized modules suitable for distributed deployment at hydrogen production sites; (b) discloses CO2-feedstock-compatible catalyst formulations and the integrated RWGS-FT process intensification within a microchannel block; (c) commercial demonstration at Werlte, Germany. Anticipates patent claims directed to containerized microchannel e-fuel plants and to integrated RWGS-FT microchannel reactor blocks.

## Janssen / Johnson & Johnson Prezista (darunavir) continuous manufacturing line (2016)

- **id**: `janssen-tablet-press-cm-line`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Janssen Pharmaceuticals (Johnson & Johnson)
- **disclosure**: FDA approval letter, Prezista (darunavir) supplemental NDA 21976/S-038 'continuous manufacturing process change', April 8 2016; Lee, S. L.; O'Connor, T. F.; Yang, X.; Cruz, C. N.; Chatterjee, S.; Madurawe, R. D.; Moore, C. M. V.; Yu, L. X.; Woodcock, J. 'Modernizing pharmaceutical manufacturing: from batch to continuous production' J. Pharm. Innov. 2015, 10, 191–199; Janssen press release April 8 2016
- **ip status**: patented
- **prior art notes**: Although tablet manufacturing is not microfluidic per se, the Janssen Prezista line is the canonical first-FDA-approved continuous-pharma supplemental NDA and has substantial spillover prior art for: (a) inline gravimetric feeders + continuous blenders + continuous tablet press as integrated CM line; (b) PAT-driven real-time release replacing batch quality holds (analogous to flow-chemistry PAT); (c) the regulatory precedent that enables Continuus ICM, On Demand Pharmaceuticals, and other downstream entries. Included for prior-art completeness on regulatory and architectural patterns shared with microreactor-based CM.

## Tidepool Loop DIY Closed-Loop Insulin Algorithm (2016-02 (Loop community); 2023-01 (FDA-cleared Tidepool Loop))

- **id**: `tidepool-loop-diy-closed-loop`
- **corpus**: open
- **device class**: flow-controller
- **creator**: Tidepool Project (501c3) and Loop open-source community (Pete Schwamb, Nate Racklyeft, Katie DiSimone, et al.)
- **disclosure**: GitHub LoopKit/Loop public repository (commits from Feb 2016 onward); Tidepool Loop FDA 510(k) K231039 January 2023
- **ip status**: open-permissive
- **prior art notes**: Pure-software flow controller for wearable microfluidic dispensers. Discloses an iPhone-based closed-loop control algorithm that ingests CGM glucose, predicts forward 6 hours, and commands an insulin pump (Omnipod, Medtronic) to dispense microliter insulin boluses. Anticipates: smartphone-as-closed-loop-controller topology; modular CGM-and-pump driver abstractions enabling third-party microfluidic dispensers to participate in any closed-loop ecosystem; open-source clearance pathway for AID software.

## Univercells scale-X Bioreactor (carbo / hydro / nitro) (2017)

- **id**: `univercells-scale-x-bioreactor`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Univercells Technologies
- **disclosure**: Univercells scale-X carbo product launch 2017; US patent US10,738,275B2 (Bioreactor with structured packing, Univercells, priority 2015); WO2016/110622A1; Univercells Technologies website and product literature
- **ip status**: patented
- **prior art notes**: Discloses a single-use fixed-bed bioreactor with proprietary structured packing (tightly-controlled void fraction and fluid distribution geometry) that achieves uniform perfusion through the cell-bearing matrix at high cell densities. The hydro variant is the small-scale (sub-200 mL working volume) sister product targeting process development. Anticipates: structured-packing fixed-bed perfusion bioreactor design for viral vector manufacturing where the packing geometry, not random ceramic discs (Pall iCellis), defines flow distribution; integration of bioreactor + on-deck concentration step (NevoLine) into a single intensified train. Element-by-element: media inlet manifold + structured-packed bed + outlet manifold + integrated downstream concentration loop.

## Endress+Hauser SpectraTec In-Line Spectrometer Series (2017)

- **id**: `endress-hauser-spectratec-spectrometer`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Endress+Hauser (Switzerland/Germany)
- **disclosure**: Endress+Hauser SpectraTec product brochure 2017-2020; Endress+Hauser Optical Analysis division technical bulletin
- **ip status**: patented
- **prior art notes**: Discloses Endress+Hauser SpectraTec process spectrometer family with hygienic stainless-steel housings and CIP/SIP-rated optical probes. Anticipates: (a) hygienic-design Raman and NIR process spectrometers for pharma/food PAT; (b) Industry 4.0 / WirelessHART integration of optical PAT probes; (c) the design template of co-located Raman + NIR probes sharing hygienic insertion fittings. Cite against later patents claiming hygienic-CIP/SIP-rated optical PAT probes with WirelessHART integration.

## Adva Biotechnology AdvaBio bioreactor (2018)

- **id**: `adva-biotechnology-advabio`
- **corpus**: private
- **device class**: single-cell-platform
- **creator**: Adva Biotechnology Ltd.
- **disclosure**: Adva Biotechnology Ltd. AdvaBio platform. https://www.advabio.com. Patent family: US10465155B2 (Adva Biotechnology; priority 2014).
- **ip status**: patented
- **prior art notes**: Closed single-use bioreactor for CGT expansion targeting smaller batch sizes than the Wave/Xuri family, with integrated process-analytical-technology (DO/pH/glucose) feedback. Anticipates: integration of in-line PAT sensors with closed single-use bioreactors at sub-litre scale for CGT-specific workflows.

## On Demand Pharmaceuticals Pharmacy-on-Demand (PoD) refrigerator-scale continuous manufacturing (2018)

- **id**: `on-demand-pharmaceuticals-pharmacy-on-demand`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: On Demand Pharmaceuticals Inc. (Maryland, US; DARPA PoD spinout)
- **disclosure**: Adamo, A.; Beingessner, R. L.; Behnam, M.; Chen, J.; Jamison, T. F.; Jensen, K. F. et al. 'On-demand continuous-flow production of pharmaceuticals in a compact, reconfigurable system' Science 2016, 352, 61–67; On Demand Pharmaceuticals Inc. founding 2018 (DARPA Pharmacy-on-Demand spinout); DARPA BAA 'Pharmacy on Demand' (PoD) program announcement 2014; FDA EUA submission 2020 hydroxychloroquine continuous manufacturing
- **ip status**: patented
- **prior art notes**: Direct commercial descendant of the Adamo 2016 MIT science paper. Discloses (a) refrigerator-sized footprint as design constraint for distributed pharmaceutical manufacturing — a more aggressive miniaturization target than Continuus ICM; (b) full reconfigurability across multiple drug products in the same hardware via swappable reaction-module cassettes; (c) DARPA-validated military-deployable form factor; (d) explicit goals around forward-deployed and disaster-response pharmaceutical manufacturing. Anticipates patent claims to compact (sub-cubic-meter) reconfigurable continuous-flow pharmaceutical manufacturing systems.

## Bruker Avance Neo / Fourier 80 In-Line NMR PAT (2018)

- **id**: `bruker-avance-neo-process-nmr`
- **corpus**: private
- **device class**: flow-controller
- **creator**: Bruker BioSpin (Germany/Switzerland/USA)
- **disclosure**: Bruker BioSpin Avance Neo product brochure 2017-2018; Wallace, M. et al. 'Online benchtop NMR for monitoring of pharmaceutical reactions.' Reaction Chemistry & Engineering 7, 1583-1593 (2022), doi:10.1039/D2RE00171C
- **ip status**: patented
- **prior art notes**: Discloses the Bruker Fourier 80 / Avance Neo benchtop process NMR with permanent-magnet (no helium) architecture and flow-cell probes for continuous-flow chemistry PAT integration. Anticipates: (a) helium-free permanent-magnet NMR spectrometers as practical PAT tools for continuous-flow chemistry lines; (b) integrated flow-cell probes for sub-mL in-line reaction monitoring; (c) the integration template for benchtop NMR into continuous-flow pharma synthesis lines (e.g., GSK CMAC, Vapourtec R-series). Cite against later patents claiming permanent-magnet flow-cell NMR PAT instruments.

## Tessera Therapeutics Gene Writing Manufacturing (2020)

- **id**: `tessera-therapeutics-gene-writing`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Tessera Therapeutics Inc.
- **disclosure**: Tessera Therapeutics company launch July 2020; Tessera patent estate US11,427,818B2 (Recombinase compositions and methods of use, priority 2020); Tessera R&D presentations 2022-2023
- **ip status**: patented
- **prior art notes**: Process disclosure for in vivo gene-writing manufacturing: mRNA encoding Tessera's mobile-element machinery is co-formulated with a target template oligo into LNPs via microfluidic impingement-jet or staggered-herringbone mixing; downstream tangential-flow filtration concentrates and buffer-exchanges; sterile fill into vial. Anticipates: combined-cargo LNP encapsulation in which a single LNP carries both the gene-writing enzyme mRNA and the donor template, manufactured in a continuous microfluidic train. Element-by-element: aqueous-phase mRNA + ethanol-phase lipid → microfluidic mixer → TFF → 0.2 µm sterile filtration → vial fill.

## Andelyn Biosciences AAV Manufacturing Platform (2020)

- **id**: `andelyn-biosciences-aav`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Andelyn Biosciences (spinout from Nationwide Children's Hospital)
- **disclosure**: Andelyn Biosciences spinout from Nationwide Children's Hospital 2020; Andelyn product/service literature 2021-2023; parent NCH viral vector manufacturing publications
- **ip status**: trade-secret
- **prior art notes**: Process disclosure: Andelyn's GMP AAV manufacturing train uses Pall iCellis fixed-bed adherent bioreactor seeded with HEK293 cells, transient triple-plasmid transfection (rep/cap, helper, transgene), harvest by detergent lysis, depth-filtration clarification, POROS AAVX affinity capture, anion-exchange polishing, TFF concentration/buffer-exchange, sterile fill. Microfluidic content is concentrated in the affinity column flow distribution, the TFF cassette flow-channel geometry, and the in-line PAT (UV/conductivity/pH probes). Anticipates: end-to-end GMP AAV manufacturing using fixed-bed adherent culture as the production unit (vs. suspension); and the affinity-capture-first downstream architecture standard in modern AAV CDMO operations. Trade-secret heavy; entry strength rests on process flow as published in Andelyn literature.

## Resilience CGT Manufacturing Platform (2020)

- **id**: `resilience-cgt-manufacturing-platform`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: National Resilience Inc.
- **disclosure**: National Resilience Inc. company launch 2020-11; Resilience press releases 2021-2023; multiple acquisitions including Ology Biosciences (CGT), Mibelle Biochemistry, Boston Children's pDNA facility
- **ip status**: trade-secret
- **prior art notes**: Process disclosure: Resilience operates a multi-modality CGT CDMO with shared infrastructure for mRNA-LNP (microfluidic mixer + TFF), AAV (iCellis or suspension + chromatography), lentivirus (suspension + TFF + chromatography), plasmid (fermenter + chromatography), and cell therapy (closed-train MaxCyte/CliniMACS-class workflows). The microfluidic content is the cumulative content of the modality-specific trains; Resilience's platform-level disclosure is the digital-twin orchestration across sites and the unified materials-management infrastructure. Trade-secret heavy; entry rests on press releases and public manufacturing capability disclosures.

## Verve Therapeutics In Vivo Base-Editing LNP Manufacturing (2021)

- **id**: `verve-therapeutics-in-vivo-base-editing`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Verve Therapeutics Inc.
- **disclosure**: Verve Therapeutics SEC S-1 (2021-06); Musunuru et al. 'In vivo CRISPR base editing of PCSK9 durably lowers cholesterol in primates,' Nature 593:429 (2021), doi:10.1038/s41586-021-03534-y; Verve clinical trial NCT05398029 (heart-1)
- **ip status**: patented
- **prior art notes**: Process disclosure: mRNA encoding adenine base editor is co-formulated with a chemically-modified sgRNA into hepatocyte-targeted LNPs via microfluidic mixing (T-junction or impingement-jet); downstream TFF concentration and buffer exchange; sterile-filtered fill. Distinguishable from Tessera by cargo identity (base editor + sgRNA, not a recombinase + template) but the manufacturing fluid path is the standard mRNA-LNP architecture. Anticipates: clinical-stage in vivo base-editing LNP manufacturing with a hepatocyte-targeted lipid in a continuous microfluidic train. Element-by-element: aqueous mRNA/sgRNA + ethanolic lipid mix → microfluidic mixer → dialysis/TFF → sterile fill → vial.
