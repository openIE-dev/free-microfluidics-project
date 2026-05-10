#!/usr/bin/env python3
"""lookup.py — patent-claim prior-art analyzer for microfluidics.

Given a claim phrase (or a free-form description of subject matter),
returns ranked corpus entries that disclose the matching subsystems,
in chronological order. The earliest disclosure with a tag match is
the strongest 102 prior art candidate.

Usage:
    python3 tools/lookup.py "pneumatically actuated membrane valve"
    python3 tools/lookup.py "staggered herringbone mixer" --before 2010 --limit 5
    python3 tools/lookup.py "PDMS soft lithography" --commons-only
    python3 tools/lookup.py --tag valve-quake-pneumatic-membrane

Ranking: tag matches (high weight) > prior_art_notes / details (medium)
> name / aliases (low). Ties broken by earlier disclosure date wins.

Output: per match, shows id, name, year, ip status, and the matched tags.
Pipe to less, grep, or jq-like filters to subset further.
"""
import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"

# Map common claim-language phrases / tokens onto subsystem tags.
# Each value is a tag from the corpus's disclosed_subsystems taxonomy.
# Keep these phrases conservative — if the claim says "Quake valve" it
# almost certainly hits valve-quake-pneumatic-membrane. If it says
# "valve", that's too generic to map.
TAG_KEYWORDS = {
    # fabrication
    "soft lithography": "fabrication-pdms-soft-lithography",
    "pdms soft lithography": "fabrication-pdms-soft-lithography",
    "pdms replica": "fabrication-pdms-replica-molding",
    "replica molding": "fabrication-pdms-replica-molding",
    "anodic bonding": "fabrication-glass-anodic-bonding",
    "thermal bonding": "fabrication-glass-thermal-bonding",
    "hf etching": "fabrication-glass-hf-etching",
    "hydrofluoric etching": "fabrication-glass-hf-etching",
    "drie": "fabrication-silicon-drie",
    "deep reactive ion etch": "fabrication-silicon-drie",
    "koh etching": "fabrication-silicon-koh-etching",
    "su-8": "fabrication-su8-photoresist",
    "su8": "fabrication-su8-photoresist",
    "injection molding": "fabrication-thermoplastic-injection-molding",
    "hot embossing": "fabrication-thermoplastic-hot-embossing",
    "laser cutting": "fabrication-thermoplastic-laser-cutting",
    "paper microfluidics": "fabrication-paper-microfluidics",
    "xurography": "fabrication-xurography",
    "vinyl cutting": "fabrication-xurography",
    "dlp 3d printing": "fabrication-dlp-sla-enclosed-channels",
    "dlp-sla": "fabrication-dlp-sla-enclosed-channels",
    "stereolithography": "fabrication-dlp-sla-enclosed-channels",
    "two-photon polymerization": "fabrication-2pp-direct-write",
    "2pp": "fabrication-2pp-direct-write",
    "nanoscribe": "fabrication-2pp-direct-write",
    "multi-resolution 3d printing": "fabrication-multi-resolution-3d-printing",
    "volumetric printing": "fabrication-volumetric-3d-printing",
    "tomographic 3d printing": "fabrication-volumetric-3d-printing",
    "computed axial lithography": "fabrication-volumetric-3d-printing",
    "lamination": "fabrication-multilayer-lamination",
    "cyclic olefin": "fabrication-cyclic-olefin-copolymer",
    "coc": "fabrication-cyclic-olefin-copolymer",
    "zeonor": "fabrication-cyclic-olefin-copolymer",
    # pumping
    "syringe pump": "pump-syringe-driven",
    "air over liquid": "pump-pressure-controlled-air-over-liquid",
    "pressure-controlled flow": "pump-pressure-controlled-air-over-liquid",
    "peristaltic": "pump-peristaltic-on-chip",
    "membrane pump": "pump-membrane-pneumatic",
    "pneumatic membrane pump": "pump-membrane-pneumatic",
    "disc pump": "pump-piezoelectric-disc",
    "ttp ventus": "pump-piezoelectric-disc",
    "piezoelectric pump": "pump-piezoelectric-stack",
    "electroosmotic": "pump-electroosmotic",
    "electro-osmotic": "pump-electroosmotic",
    "ehd pump": "pump-electrohydrodynamic",
    "electrohydrodynamic": "pump-electrohydrodynamic",
    "capillary pump": "pump-capillary-passive",
    "capillary-driven": "pump-capillary-passive",
    "centrifugal microfluidics": "pump-centrifugal-rotational",
    "lab-on-disc": "pump-centrifugal-rotational",
    "thermal bubble": "pump-thermal-bubble-jet",
    "bubble jet": "pump-thermal-bubble-jet",
    "acoustic streaming": "pump-acoustic-streaming",
    "solenoid pump": "pump-solenoid-displacement",
    "stepper pump": "pump-stepper-volumetric",
    # valves
    "quake valve": "valve-quake-pneumatic-membrane",
    "monolithic membrane valve": "valve-quake-pneumatic-membrane",
    "elastomeric valve": "valve-quake-pneumatic-membrane",
    "doormat valve": "valve-doormat-style",
    "torque-actuated valve": "valve-torque-actuated",
    "paraffin valve": "valve-thermal-paraffin",
    "phase-change valve": "valve-thermal-paraffin",
    "magnetic valve": "valve-magnetic",
    "burst valve": "valve-burst-frangible",
    "frangible seal": "valve-burst-frangible",
    "electrowetting valve": "valve-electrowetting",
    "capillary stop": "valve-capillary-stop",
    "check valve": "valve-check",
    "rotary valve": "valve-rotary-multiport",
    "multiport selector": "valve-rotary-multiport",
    # mixers
    "serpentine mixer": "mixer-passive-serpentine",
    "staggered herringbone": "mixer-passive-staggered-herringbone",
    "herringbone mixer": "mixer-passive-staggered-herringbone",
    "tesla mixer": "mixer-passive-tesla",
    "split and recombine": "mixer-passive-split-recombine",
    "interleaved stream mixer": "mixer-passive-interleaved-streams",
    "acoustic mixer": "mixer-active-acoustic",
    "electrokinetic mixer": "mixer-active-electrokinetic",
    "magnetic mixer": "mixer-active-magnetic",
    "tpms mixer": "mixer-tpms-embedded",
    # separation
    "deterministic lateral displacement": "separation-deterministic-lateral-displacement",
    "dld": "separation-deterministic-lateral-displacement",
    "pinched flow fractionation": "separation-pinched-flow-fractionation",
    "inertial focusing": "separation-inertial-focusing",
    "inertial microfluidics": "separation-inertial-focusing",
    "acoustophoresis": "separation-acoustophoresis",
    "saw separation": "separation-acoustophoresis",
    "dielectrophoresis": "separation-dielectrophoresis",
    "dep": "separation-dielectrophoresis",
    "magnetophoresis": "separation-magnetophoresis",
    "magnetic separation": "separation-magnetophoresis",
    "capillary electrophoresis": "separation-capillary-electrophoresis",
    "isoelectric focusing": "separation-isoelectric-focusing",
    "ief": "separation-isoelectric-focusing",
    "affinity capture": "separation-affinity-capture",
    "membrane filtration on chip": "separation-membrane-filtration-on-chip",
    "size exclusion chromatography on chip": "separation-size-exclusion-chromatography",
    # droplets
    "t-junction": "droplet-t-junction-generation",
    "flow focusing": "droplet-flow-focusing-generation",
    "flow-focusing droplet": "droplet-flow-focusing-generation",
    "coflow droplet": "droplet-coflow-generation",
    "step emulsification": "droplet-step-emulsification",
    "double emulsion": "droplet-double-emulsion",
    "droplet on demand": "droplet-on-demand",
    "electrocoalescence": "droplet-merging-electrocoalescence",
    "droplet merging": "droplet-merging-electrocoalescence",
    "droplet splitting": "droplet-splitting-bifurcation",
    "facs droplet": "droplet-sorting-fluorescence-activated",
    "fadcs": "droplet-sorting-fluorescence-activated",
    "ewod": "dmf-electrowetting-on-dielectric",
    "electrowetting on dielectric": "dmf-electrowetting-on-dielectric",
    "digital microfluidics": "dmf-electrowetting-on-dielectric",
    "addressable electrode": "dmf-addressable-electrode-array",
    # detection
    "on-chip fluorescence": "detection-fluorescence-on-chip",
    "fluorescence detection on chip": "detection-fluorescence-on-chip",
    "on-chip electrochemical": "detection-electrochemical-on-chip",
    "impedance cytometry": "detection-impedance-cytometry",
    "coulter on chip": "detection-impedance-cytometry",
    "spr on chip": "detection-surface-plasmon-resonance-on-chip",
    "surface plasmon resonance": "detection-surface-plasmon-resonance-on-chip",
    "nanofluidic scattering": "detection-nanofluidic-scattering-spectroscopy",
    "nss": "detection-nanofluidic-scattering-spectroscopy",
    "electrospray coupled": "detection-mass-spec-electrospray-coupled",
    "esi-ms": "detection-mass-spec-electrospray-coupled",
    "raman on chip": "detection-raman-on-chip",
    "label-free imaging": "detection-label-free-imaging",
    # cell handling
    "hydrodynamic trap": "cell-trap-hydrodynamic",
    "cell trap": "cell-trap-hydrodynamic",
    "acoustic streaming vortex": "cell-trap-acoustic-streaming-vortex",
    "dep trap": "cell-trap-dielectrophoretic",
    "microwell array": "cell-trap-microwell-array",
    "electroporation on chip": "cell-poration-electric",
    "mechanical poration": "cell-poration-mechanical-shear",
    "cell squeezing": "cell-poration-mechanical-shear",
    "acoustic poration": "cell-poration-acoustic",
    "photothermal poration": "cell-poration-photothermal",
    "droplet encapsulation": "cell-encapsulation-droplet",
    "single cell encapsulation": "cell-encapsulation-droplet",
    "organoid perfusion": "cell-organoid-perfusion",
    # thermal
    "peltier on chip": "thermal-on-chip-peltier",
    "on-chip heater": "thermal-on-chip-resistive-heater",
    "resistive heater": "thermal-on-chip-resistive-heater",
    "pcr cycling": "thermal-pcr-cycling",
    "ddpcr": "thermal-droplet-pcr-cycling",
    "droplet pcr": "thermal-droplet-pcr-cycling",
    "isothermal amplification": "thermal-isothermal-amplification",
    "lamp": "thermal-isothermal-amplification",
    "microchannel cooler": "thermal-microchannel-cooling-electronics",
    "two-phase cooling": "thermal-two-phase-cooling",
    "jet impingement": "thermal-jet-impingement",
    # interfaces / packaging
    "luer lock": "interface-luer-lock-port",
    "luer-lock": "interface-luer-lock-port",
    "o-ring seal": "interface-o-ring-seal",
    "fluidic edge connector": "interface-fluidic-edge-connector",
    "blister pack": "interface-blister-pack-reagent-storage",
    "foil pierce": "interface-foil-pierce-actuation",
    "pressure manifold": "interface-pressure-manifold",
    "borofloat window": "interface-optical-window-borofloat",
    "integrated electrode": "interface-electrode-integration",
    # surface chemistry
    "plasma bonding": "surface-pdms-plasma-bonding",
    "oxygen plasma": "surface-pdms-plasma-bonding",
    "protein passivation": "surface-protein-passivation",
    "bsa coating": "surface-protein-passivation",
    "hydrophilic treatment": "surface-hydrophilic-treatment",
    "superhydrophobic": "surface-superhydrophobic-patterning",
    "silane functionalization": "surface-functionalization-silane",
    "thiol-gold": "surface-functionalization-thiol-gold",
    # materials
    "pdms": "material-pdms-base",
    "pmma": "material-pmma-acrylic",
    "polycarbonate": "material-polycarbonate",
    "pegda": "material-pegda-photoresin",
    "borofloat 33": "material-borofloat-glass",
    "quartz substrate": "material-quartz",
    "thermal bonding film": "material-thermal-bonding-films",
    # architectures
    "stat test cartridge": "architecture-stat-test-cartridge",
    "multiplex cartridge": "architecture-multiplex-cartridge",
    "filmarray": "architecture-multiplex-cartridge",
    "droplet library": "architecture-droplet-library-screening",
    "vasculature on chip": "architecture-organ-on-chip-vasculature",
    "body on chip": "architecture-body-on-chip-coupled-organs",
    "process analytical": "architecture-process-analytical-technology",
    "on-chip incubator": "architecture-on-chip-incubator",
    "mass produced volumetric": "architecture-mass-production-volumetric-print",
}


def load_corpus():
    return [json.loads(l) for l in CORPUS.read_text().splitlines() if l.strip()]


def tags_from_claim(claim: str) -> dict:
    """Map a claim string to {tag: number_of_phrase_hits}.

    Longer phrases match before shorter ones (greedy), so "staggered herringbone"
    is preferred over a hypothetical bare "herringbone" key.
    """
    text = " " + claim.lower() + " "
    text = re.sub(r"[\(\)\.,;:/]", " ", text)
    hits = defaultdict(int)
    matched_spans = []
    phrases = sorted(TAG_KEYWORDS.keys(), key=len, reverse=True)
    for phrase in phrases:
        idx = 0
        while True:
            i = text.find(" " + phrase + " ", idx) if " " in phrase else text.find(phrase, idx)
            if i == -1:
                break
            if any(s <= i < e or s < i + len(phrase) <= e for s, e in matched_spans):
                idx = i + 1
                continue
            hits[TAG_KEYWORDS[phrase]] += 1
            matched_spans.append((i, i + len(phrase)))
            idx = i + len(phrase)
    return dict(hits)


def score_entry(entry: dict, tag_hits: dict, claim_lower: str) -> tuple:
    """Return a (score, tiebreaker, matched_tags) tuple. Higher score = better."""
    score = 0
    matched_tags = set()
    for t in entry.get("disclosed_subsystems") or []:
        if t in tag_hits:
            score += 10 * tag_hits[t]
            matched_tags.add(t)
    fields = [
        entry.get("prior_art_notes"),
        entry.get("channel_geometry"),
        entry.get("fabrication_method"),
        entry.get("flow_regime"),
        entry.get("control_architecture"),
        entry.get("sensing"),
        entry.get("notes"),
    ]
    for f in fields:
        if not f:
            continue
        f_lower = f.lower() if isinstance(f, str) else " ".join(f).lower()
        for term in claim_lower.split():
            if len(term) >= 4 and term in f_lower:
                score += 1
    name_lower = (entry.get("canonical_name") or "").lower()
    aliases = " ".join(entry.get("aliases") or []).lower()
    for term in claim_lower.split():
        if len(term) >= 4 and (term in name_lower or term in aliases):
            score += 1
    year_str = (entry.get("first_disclosure_date") or "")[:4]
    try:
        year = int(year_str)
    except ValueError:
        year = 9999
    return score, -year, matched_tags


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("claim", nargs="*", help="claim phrase or free-form description")
    p.add_argument("--tag", action="append", default=[], help="explicit tag(s) to look up; repeatable")
    p.add_argument("--before", type=int, help="only entries disclosed before this year")
    p.add_argument("--after", type=int, help="only entries disclosed after this year")
    p.add_argument("--commons-only", action="store_true", help="exclude draft entries")
    p.add_argument("--limit", type=int, default=15, help="max results to print (default 15)")
    p.add_argument("--json", action="store_true", help="output JSON instead of text")
    args = p.parse_args()

    if not args.claim and not args.tag:
        p.error("provide a claim phrase or --tag <tag>")

    claim = " ".join(args.claim)
    tag_hits = tags_from_claim(claim) if claim else {}
    for t in args.tag:
        tag_hits[t] = tag_hits.get(t, 0) + 1

    entries = load_corpus()
    scored = []
    for e in entries:
        if args.commons_only and e.get("draft"):
            continue
        year_str = (e.get("first_disclosure_date") or "")[:4]
        try:
            year = int(year_str)
        except ValueError:
            year = None
        if args.before is not None and (year is None or year >= args.before):
            continue
        if args.after is not None and (year is None or year <= args.after):
            continue
        s, neg_year, matched_tags = score_entry(e, tag_hits, claim.lower())
        if s > 0:
            scored.append((s, neg_year, matched_tags, e))
    scored.sort(key=lambda x: (-x[0], x[1]))

    if args.json:
        print(json.dumps([
            {
                "id": e["id"],
                "canonical_name": e["canonical_name"],
                "year": (e.get("first_disclosure_date") or "")[:4],
                "corpus": e["corpus"],
                "ip_status": e.get("ip_status"),
                "draft": bool(e.get("draft")),
                "score": s,
                "matched_tags": sorted(mt),
                "disclosure_citation": e.get("disclosure_citation"),
                "prior_art_notes": e.get("prior_art_notes"),
            }
            for s, _, mt, e in scored[:args.limit]
        ], indent=2, ensure_ascii=False))
        return

    if claim:
        print(f"Claim: {claim}")
    if tag_hits:
        print("Mapped tags:")
        for t, n in sorted(tag_hits.items(), key=lambda x: -x[1]):
            print(f"  {t} ×{n}")
    else:
        print("(no tag mapped from claim — see TAG_KEYWORDS in lookup.py to extend)")
    print()
    if not scored:
        print("No matching entries.")
        return
    print(f"Top {min(args.limit, len(scored))} of {len(scored)} matches (chronological tiebreak: earlier wins):")
    print("-" * 72)
    for s, _, mt, e in scored[:args.limit]:
        year = (e.get("first_disclosure_date") or "?")[:4]
        draft = " (draft)" if e.get("draft") else ""
        print(f"  {year}  {e['canonical_name']:<45.45} score={s} {e.get('ip_status', '?'):<14} {e['id']}{draft}")
        if mt:
            print(f"        tags: {', '.join(sorted(mt))}")
        if e.get("disclosure_citation"):
            cite = e["disclosure_citation"]
            if len(cite) > 200:
                cite = cite[:200] + "…"
            print(f"        cite: {cite}")
        print()


if __name__ == "__main__":
    main()
