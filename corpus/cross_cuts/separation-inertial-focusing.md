---
title: separation-inertial-focusing
parent: Cross-cuts
layout: default
---

# Cross-cut: `separation-inertial-focusing`

**20 corpus entries disclose this subsystem.**

Earliest disclosure: 1883

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Reynolds Number Re = rho U L / mu (1883)

- **id**: `reynolds-number-dimensionless-group`
- **corpus**: academic
- **device class**: other
- **creator**: Osborne Reynolds (group); Arnold Sommerfeld (naming)
- **disclosure**: Reynolds, O. (1883). 'An experimental investigation of the circumstances which determine whether the motion of water shall be direct or sinuous.' Phil. Trans. R. Soc. 174: 935-982. doi:10.1098/rstl.1883.0029. Group named by Sommerfeld in 1908.
- **ip status**: public-domain
- **prior art notes**: Reynolds number is the single most invoked dimensionless group in microfluidic literature; nearly every microfluidic chip operates at Re << 1 by design (channel size ~10 to 100 microns; velocity ~mm/s; water viscosity). Anchors: (a) all 'laminar flow chip' patents (Yager H-filter, parallel-stream extraction); (b) all 'inertial microfluidics' (Di Carlo 2007) patents that explicitly key on Re ~ 1-100; (c) the Purcell scallop theorem foundation (Purcell 1977); (d) Reynolds-controlled droplet generation regime. Codified by Sommerfeld in 1908. Together with Reynolds 1883 (the experimental paper) this anchors all dimensionless-group reasoning that microfluidic IP relies on.

## Prandtl 1904 — Boundary Layer Theory (1904-08)

- **id**: `prandtl-1904-boundary-layer-theory`
- **corpus**: academic
- **device class**: other
- **creator**: Ludwig Prandtl
- **disclosure**: Prandtl, L. (1904). 'Ueber Fluessigkeitsbewegung bei sehr kleiner Reibung.' Verhandlungen des dritten internationalen Mathematiker-Kongresses, Heidelberg, 8-13 August 1904: 484-491. Teubner, Leipzig (1905).
- **ip status**: public-domain
- **prior art notes**: While microfluidic flows are typically low-Reynolds (laminar throughout), Prandtl's boundary-layer concept is foundational for: (a) entry-length analysis in microchannels (Schlichting boundary-layer growth in developing flow); (b) high-Re inertial microfluidics (Di Carlo 2007 and descendants — particles migrate based on competing inertial lift and shear forces, both of which derive from boundary-layer arguments); (c) jet-impingement microchannel cooling (Tuckerman-Pease descendants). Anticipates: any patent claiming 'particle focusing by boundary-layer-mediated inertial lift' to the extent it recites boundary-layer physics generally rather than a specific non-obvious channel geometry.

## Weissenberg Number Wi = gamma_dot * tau (1947)

- **id**: `weissenberg-number-dimensionless-group`
- **corpus**: academic
- **device class**: other
- **creator**: Karl Weissenberg
- **disclosure**: Weissenberg, K. (1947). 'A continuum theory of rheological phenomena.' Nature 159(4035): 310-311. doi:10.1038/159310a0
- **ip status**: public-domain
- **prior art notes**: Weissenberg number governs whether a viscoelastic fluid in a microchannel exhibits elastic instabilities (Pakdel-McKinley criterion: Wi sqrt(L/R) > critical). Anchors: (a) elastic-instability micromixers (passive mixing in viscoelastic solutions at low Re); (b) viscoelastic single-cell focusing (Yang 2011 and descendants); (c) polymer-solution droplet generation regime maps; (d) cell-deformability assays in polymer solutions. Any patent claim that recites 'mixing or focusing in viscoelastic fluid' is anticipated by Weissenberg-number scaling.

## Segre & Silberberg 1962 - Behaviour of macroscopic rigid spheres in Poiseuille flow (1962)

- **id**: `segre-silberberg-1962-inertial-focusing`
- **corpus**: academic
- **device class**: other
- **creator**: Gershon Segre; Alexander Silberberg
- **disclosure**: Segre, G., Silberberg, A. (1962). 'Behaviour of macroscopic rigid spheres in Poiseuille flow. Part 2.' J. Fluid Mech. 14(1): 136-157. doi:10.1017/S0022112062001111. Companion: Segre-Silberberg, Nature 189, 209 (1961).
- **ip status**: public-domain
- **prior art notes**: Segre-Silberberg 1961-1962 is the foundational experimental paper documenting the tubular-pinch effect: rigid spheres in laminar pipe flow at finite Re migrate to an equilibrium radial position. Anticipates the entire inertial-focusing microfluidic ecosystem: Di Carlo group spiral inertial focusing, sheath-free flow cytometry, particle-sorting-by-inertial-equilibrium-position, and every patent reciting 'particles focused to an equilibrium streamline by inertia' (Di Carlo, Vortex Bio, Forte Bio, Velocyto). 60 years of microfluidic inertial focusing reduces to Segre-Silberberg.

## Karnis & Mason 1963 - Particle migration in Poiseuille flow (1963)

- **id**: `karnis-mason-1963-particle-migration-tubes`
- **corpus**: academic
- **device class**: other
- **creator**: Andrew Karnis; Stanley G. Mason
- **disclosure**: Karnis, A., Mason, S. G. (1963). 'Particle motions in sheared suspensions: XXIII. Wall migration of fluid drops.' J. Colloid Sci. 18: 257-281.
- **ip status**: public-domain
- **prior art notes**: Karnis-Mason 1963 systematically documents particle and drop migration in Poiseuille and shear flow, including wall-migration of deformable drops. Anticipates droplet-focusing microfluidic claims keyed on drop deformability, cell-sorting by deformability in inertial channels (Di Carlo deformability cytometry), and any 'cross-stream migration' patent for cells or droplets in laminar tube flow. Companion to Segre-Silberberg 1962.

## Deborah Number De = tau / T (Reiner 1964) (1964-01)

- **id**: `deborah-number-reiner-1964`
- **corpus**: academic
- **device class**: other
- **creator**: Markus Reiner
- **disclosure**: Reiner, M. (1964). 'The Deborah Number.' Physics Today 17(1): 62. doi:10.1063/1.3051374
- **ip status**: public-domain
- **prior art notes**: Deborah number anchors viscoelastic microfluidics: any chip that handles polymer solutions, biopolymer solutions, mucus, blood, or DNA solutions with significant relaxation time operates at finite De and exhibits non-Newtonian flow features (elastic instabilities, secondary flows, viscoelastic focusing). Anticipates: (a) elasto-inertial focusing patents; (b) DNA-stretching-on-chip patents; (c) viscoelastic-focusing single-cell platforms; (d) DEAN-flow vortex generators in viscoelastic fluids.

## Saffman 1965 - The lift on a small sphere in a slow shear flow (1965)

- **id**: `saffman-1965-shear-lift-force`
- **corpus**: academic
- **device class**: other
- **creator**: Philip G. Saffman
- **disclosure**: Saffman, P. G. (1965). 'The lift on a small sphere in a slow shear flow.' J. Fluid Mech. 22(2): 385-400. doi:10.1017/S0022112065000824
- **ip status**: public-domain
- **prior art notes**: Saffman 1965 derives the lift force on a small sphere in slow shear flow - the theoretical anchor for inertial-focusing microfluidics, complementary to the experimental Segre-Silberberg 1962. Anticipates patent claims reciting Saffman-lift-driven cross-stream migration or shear-gradient particle focusing in microchannels. Required clearance for any 'lateral lift force microfluidic separator' patent.

## Boger 1977 - A highly elastic constant-viscosity fluid (1977)

- **id**: `boger-1977-elastic-fluid-definition`
- **corpus**: academic
- **device class**: other
- **creator**: David V. Boger
- **disclosure**: Boger, D. V. (1977). 'A highly elastic constant-viscosity fluid.' J. Non-Newtonian Fluid Mech. 3(1): 87-91. doi:10.1016/0377-0257(77)80014-1
- **ip status**: public-domain
- **prior art notes**: Defines the Boger fluid: a dilute polymer solution (typically polyisobutylene in low-MW solvent) with significant first normal-stress difference but nearly constant shear viscosity. Boger fluids are the standard test medium for every viscoelastic microfluidic disclosure - elastic turbulence (Groisman-Steinberg 2000), Pakdel-McKinley instabilities (1996), viscoelastic particle focusing, viscoelastic flow rectification. Anticipates patent claims keyed on 'constant-viscosity elastic test fluid in microchannel', 'first-normal-stress-driven flow instability in serpentine channel', or 'separating shear from elastic effects via Boger-type fluid'.

## Larson 1988 - Constitutive Equations for Polymer Melts and Solutions (1988)

- **id**: `larson-1988-constitutive-equations-textbook`
- **corpus**: academic
- **device class**: other
- **creator**: Ronald G. Larson
- **disclosure**: Larson, R. G. (1988). 'Constitutive Equations for Polymer Melts and Solutions.' Butterworth-Heinemann. ISBN 978-0-409-90119-1.
- **ip status**: public-domain
- **prior art notes**: Larson 1988 is the standard textbook on viscoelastic constitutive equations. Anticipates patent claims involving viscoelastic flow predictions in microchannels using a specific constitutive model (Oldroyd-B, FENE-P, etc.), Wi-keyed flow phenomena, shear-thinning or extension-thickening flow in serpentine microchannels. Any patent asserting novelty around a specific viscoelastic constitutive law in microfluidics must clear Larson 1988.

## Abbott Cell-Dyn Sapphire Hematology Optical/Impedance Flow Cell (2003)

- **id**: `abbott-cell-dyn-sapphire-flow-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Abbott Laboratories (Abbott Hematology / Cell-Dyn)
- **disclosure**: Abbott Cell-Dyn Sapphire 510(k) K022428 (cleared 2003-04); peer-reviewed evaluation Bruegel et al., Clin Lab Haematol 2004
- **ip status**: patented
- **prior art notes**: Discloses Multi-Angle Polarized Scatter Separation (MAPSS) optical flow cytometry for white-blood-cell five-part differentiation: hydrodynamically focused single-cell stream illuminated at four angles (intermediate-angle scatter, polarized side scatter, depolarized side scatter, axial light loss) plus 488 nm laser fluorescence channel for retic/NRBC. The fluidic architecture pairs a sheath-focused optical flow cell for WBC/diff/retic with a Coulter-principle sapphire impedance aperture for RBC/PLT in parallel, with shared sample dilution stages. Anticipates: hybrid optical-impedance hematology fluidic stages sharing sample dilution; depolarized side-scatter eosinophil identification via crystalline content; sapphire as orifice material for impedance counting (durability against erosion vs ruby/glass).

## FLIR IBAC bioaerosol identifier and particulate-collector unit (2004-08-26)

- **id**: `flir-ibac-bioaerosol-trigger-collector`
- **corpus**: private
- **device class**: point-of-care-cartridge
- **creator**: FLIR Systems (via ICx Technologies / BioVigilant); related fielded units include the US JBPDS triggers
- **disclosure**: US20040159799A1 / US7126687B2 Method and instrument for detecting biological agents in aerosol (Hairston/Ho-style UV laser-induced fluorescence; ICx BioVigilant / FLIR lineage); see also Ho, Future of biological aerosol detection, Anal. Chim. Acta 457, 125 (2002).
- **ip status**: patented
- **prior art notes**: Discloses an aerodynamic micro-nozzle/virtual-impactor concentrator feeding a single-particle UV-LIF interrogation cell, plus an integrated aerosol-to-liquid microfluidic collector for confirmatory assays - a trigger-and-collect bioaerosol microfluidic system. Anticipates claims to (a) aerodynamic-focusing micro-nozzle into a single-particle UV-fluorescence/scatter bioaerosol cell; (b) intrinsic-fluorophore (tryptophan/NADH) single-particle bio-trigger; (c) integrated aerosol-to-liquid collector capturing trigger-flagged particles for PCR/immunoassay confirmation; (d) networked bioaerosol warning sensor with on-board collection. Prior art for FLIR/ICx/BioVigilant and competing UV-LIF bioaerosol-detector patents.

## Continuous inertial focusing, ordering, and separation of particles in microchannels (2007)

- **id**: `di-carlo-2007-inertial-microfluidics`
- **corpus**: academic
- **device class**: separator-component
- **creator**: Di Carlo, Toner et al. (Harvard / Mass General)
- **disclosure**: Di Carlo, D.; Irimia, D.; Tompkins, R. G.; Toner, M. Continuous inertial focusing, ordering, and separation of particles in microchannels. Proc. Natl. Acad. Sci. USA 2007, 104, 18892–18897. DOI: 10.1073/pnas.0704958104
- **ip status**: patented
- **prior art notes**: Established inertial microfluidics as a continuous-flow particle-separation regime exploiting Dean drag and shear-gradient lift in curving and straight channels at intermediate Reynolds numbers (Re~10–100). Anticipates: spiral and serpentine inertial focusing geometries, label-free CTC enrichment by inertial migration, sheath-free particle ordering, and the entire inertial-microfluidics subfield as commercialized by Vortex Biosciences, ClearCell, and the iCellate / iChip CTC platforms. Together with Sturm/Huang DLD (2004) it defines the dominant label-free continuous-separation paradigms.

## NUS microfluidic platforms (Lim group, Chen group) (2008)

- **id**: `nus-microfluidics-lim`
- **corpus**: academic
- **device class**: other
- **creator**: Chwee Teck Lim group / various, National University of Singapore
- **disclosure**: Various NUS / NTU Singapore publications on microfluidic CTC isolation and cell-mechanics platforms.
- **ip status**: patented
- **prior art notes**: Composite reference for the Singapore microfluidics ecosystem anchored at NUS and NTU. Lim group at NUS produced significant work on inertial CTC isolation that was commercialized through Clearbridge BioMedics (acquired by Biolidics 2018). Singapore-based academic-to-commercial pipeline is among the more productive in Asia for microfluidic technology transfer.

## IDEXX ProCyte Dx Veterinary Hematology Analyzer Optical/Impedance Flow Cell (2010)

- **id**: `idexx-procyte-dx-veterinary-hematology`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: IDEXX Laboratories
- **disclosure**: IDEXX ProCyte Dx launch 2010-09; ProCyte One launch 2020-06
- **ip status**: patented
- **prior art notes**: Discloses an in-clinic veterinary hematology analyzer based on a Sysmex-licensed dual-modality flow cell (impedance + flow cytometry with side scatter and side fluorescence), ported to a compact bench-top form factor with species-specific reagent and algorithm sets. Anticipates: in-clinic veterinary applications of hybrid impedance + optical hematology platforms; the multi-species calibration architecture (RBC volume, MCV, WBC subtype distributions vary substantially across species — the analyzer must select species-specific reference distributions). Important prior art for the veterinary in-clinic hematology market as it differentiates from human-clinical-only platforms (Sysmex XN, Beckman DxH, Mindray BC). Companion to ProCyte One (2020) which uses a different IDEXX-internal optical fluorescent imaging architecture rather than Sysmex licensure.

## Mindray BC-6800 Hematology Analyzer SF Cube Flow Cell (2011)

- **id**: `mindray-bc-6800-hematology-flow-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Shenzhen Mindray Bio-Medical Electronics
- **disclosure**: Mindray BC-6800 launch 2011-11; FDA 510(k) K121734; BC-7500 launch 2018
- **ip status**: patented
- **prior art notes**: Discloses the SF Cube hematology flow-cell architecture: a single sheath-focused stream subjected to both impedance counting (sapphire aperture for RBC/PLT) and downstream optical interrogation by 633 nm laser with side-scatter + dual-wavelength side-fluorescence channels (one for nucleic-acid binding dye discriminating reticulocytes/NRBC, one for cytoplasmic dye discriminating granulocyte subclasses). Three-axis (SSC × SFL1 × SFL2) cytogram enables 5-part diff with built-in IG (immature granulocyte) detection. Anticipates: dual-wavelength fluorescence + scatter cytometry on a single hematology flow cell (independent prior art relative to Sysmex XN/Beckman DxH but architecturally similar) — strengthening the commons against narrow-claim assertions on this design space.

## Sysmex XN-9000 Modular Hematology Track Sample-Aspiration Subsystem (2011)

- **id**: `sysmex-xn-9000-track-hematology`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Sysmex Corporation
- **disclosure**: Sysmex XN-Series launch 2011-09; XN-9000 modular configuration 2013; FDA 510(k) K112763 (XN); extends sysmex-cbc-cartridge entry already in corpus
- **ip status**: patented
- **prior art notes**: Discloses the Sysmex XN-9000 modular hematology track architecture extending the existing sysmex-cbc-cartridge entry (in corpus) with: (1) primary-tube cap-piercing sample aspiration sharing one probe across multiple downstream analyzer modules; (2) the WDF channel using a polymethine fluorescent dye that selectively stains WBC nucleic acid + cytoplasmic granularity, enabling true 5-part diff via two-color cytogram (side scatter × side fluorescence) — replacing the earlier-generation impedance-only differential; (3) the WPC channel using a different polymethine dye selective for blast cells, enabling automated reflexing for hematological malignancy screening; (4) the modular XN-9000 configuration linking up to 6 analyzer modules on a sample-routing track. Anticipates: high-throughput modular hematology with primary-tube cap-piercing + multi-channel optical/impedance + fluorescent intracellular staining for cell classification.

## CTC-iChip: inertial focusing for high-throughput rare-cell isolation (2013)

- **id**: `ozkumur-2013-ctc-iChip`
- **corpus**: academic
- **device class**: single-cell-platform
- **creator**: Toner / Maheswaran / Haber labs (Mass General)
- **disclosure**: Ozkumur, E.; Shah, A. M.; Ciciliano, J. C.; Emmink, B. L.; Miyamoto, D. T.; Brachtel, E.; Yu, M.; Chen, P.-i.; Morgan, B.; Trautwein, J.; Kimura, A.; Sengupta, S.; Stott, S. L.; Karabacak, N. M.; Barber, T. A.; Walsh, J. R.; Smith, K.; Spuhler, P. S.; Sullivan, J. P.; Lee, R. J.; Ting, D. T.; Luo, X.; Shaw, A. T.; Bardia, A.; Sequist, L. V.; Louis, D. N.; Maheswaran, S.; Kapur, R.; Haber, D. A.; Toner, M. Inertial focusing for tumor antigen-dependent and -independent sorting of rare circulating tumor cells. Sci. Transl. Med. 2013, 5, 179ra47. DOI: 10.1126/scitranslmed.3005616
- **ip status**: patented
- **prior art notes**: Translational descendant of Di Carlo 2007 demonstrating clinical-grade circulating tumor cell isolation by combining hydrodynamic size-based debulking, inertial focusing into a single streamline, and immunomagnetic deflection in series. Anticipates: integrated multi-modal CTC-isolation cartridge architecture, sheath-flow whole-blood debulking with leukocyte depletion, and antigen-independent rare-cell capture as a clinical workflow. Direct ancestor of multiple commercial CTC platforms.

## Vortex chip for label-free CTC isolation (Sollier 2014) (2014)

- **id**: `sollier-2014-vortex-chip`
- **corpus**: academic
- **device class**: separator-component
- **creator**: Di Carlo group, UCLA / Vortex Biosciences
- **disclosure**: Sollier, E. et al. Size-selective collection of circulating tumor cells using Vortex technology. Lab Chip 2014, 14, 63–77. DOI: 10.1039/C3LC50689D
- **ip status**: patented
- **prior art notes**: Disclosed vortex-chamber inertial separation: large CTCs are trapped in microscale vortex chambers via inertial migration while smaller blood cells flow through, enabling label-free size-based CTC enrichment. Anticipates: vortex-chamber-as-cell-trap architecture, label-free CTC isolation by inertial trapping (distinct from inertial focusing for streamline ordering). Commercial implementation: Vortex Biosciences VTX-1 (now part of NanoString).

## Beckman Coulter DxH 900 Hematology VCSn Flow Cell (2017)

- **id**: `beckman-coulter-dxh-900-flow-cell`
- **corpus**: private
- **device class**: lab-on-chip
- **creator**: Beckman Coulter (Danaher)
- **disclosure**: Beckman Coulter DxH 900 launch 2017-08; FDA 510(k) K162970
- **ip status**: patented
- **prior art notes**: Discloses VCSn technology: simultaneous Volume (low-frequency Coulter impedance for DC volume), Conductivity (high-frequency RF impedance probing internal cell density), and 5-angle Light Scatter (axial light loss + multiple side-scatter angles for granularity, lobularity, complexity) in a single hydrodynamically-focused fluidic stage. The fluid path co-locates the impedance aperture and the optical interrogation zone so each cell event is measured by all modalities within microseconds. Anticipates: combined impedance + multi-angle scatter cytometry on a single flow cell for hematology classifier inputs; 'NEW' designation marks redesigned aperture geometry vs the LH series predecessor. Element-by-element: dilution chamber, sheath formation, aperture-with-electrodes, laser interrogation downstream, post-aperture flush.

## Microfluidic rare-cell isolation (2023-onward methods) (2023)

- **id**: `microfluidic-rare-cell-academic-2023`
- **corpus**: academic
- **device class**: separator-component
- **creator**: Various groups
- **disclosure**: Various 2023-2026 publications on next-generation rare-cell isolation. Representative: cancer-cell-on-chip cluster-isolation methods.
- **ip status**: patented
- **prior art notes**: Composite reference for 2023-onward rare-cell isolation work: CTC-cluster isolation (rather than single CTC), circulating immune-cell phenotyping, antigen-independent capture by combined biophysical + biochemical signatures. Cumulative architectural disclosures from this period define current state-of-the-art in rare-cell microfluidic isolation, complementing the foundational 2007-2013 work (Di Carlo, Toner, etc.).
