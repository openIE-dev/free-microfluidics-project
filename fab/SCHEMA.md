# Free Microfluidics Fab — Schema v0.1

## Status

v0.1 is the initial scaffold. Schema is expected to evolve as the seed
recipes expose inadequacies. Recipes-as-data is a less-mature pattern than
designs-as-data, so this schema is more conservative — it describes the
recipe but does not attempt to make the steps machine-executable.

## Purpose

A structured catalog of CC0 microfluidic fabrication recipes. Each entry
is a step-by-step procedure with critical-parameter documentation,
equipment requirements, validated outcomes, and known failure modes.

The intended audience is a working group with bench access who needs to
fabricate a microfluidic device but does not have the institutional
expertise to derive the recipe from scratch.

## Quality bar

A recipe is commons-grade when:

- `steps` are written at the level of "spin SU-8 2050 at 1500 rpm for 30 s
  after 5 s ramp at 100 rpm/s" — concrete enough that a competent process
  engineer can reproduce.
- `critical_parameters` enumerate the variables that, when off-spec,
  produce known failures, with target ranges and tolerances where available.
- `validated_outcome` cites a publication, internal report, or direct
  measurement of what the recipe produced.
- `equipment_required` lists specific instruments by class (and where
  relevant, model) so a fabrication facility can assess feasibility.
- `failure_modes` enumerates the known ways the recipe goes wrong, with
  diagnostic signatures and corrective actions.

Recipes below this bar may be merged with `draft: true`.

## License posture

CC0-1.0. Recipes are not patentable as recipes (the underlying processes
may be, but the recipe-as-text is unencumbered). Where a recipe implements
a patented process, the entry's `notes` flags the relevant patents so a
fabricator knows when use-in-research vs commercial-use distinctions matter.

## Entry schema

Each entry is one record. Required fields are marked [R], optional [O].

```
id                      [R]  slug, kebab-case, globally unique
canonical_name          [R]  the name most commonly used
aliases                 [O]  list of alternate names
contributor             [R]  person, lab, or org documenting the recipe
contributor_country     [O]  ISO country code
license                 [R]  CC0-1.0 expected; other CC0-equivalent OK
recipe_class            [R]  see recipe class taxonomy below
substrate_material      [R]  what's being fabricated on/from
output_artifact         [R]  what the recipe produces (e.g., "SU-8 master
                             mold ready for PDMS casting")
steps                   [R]  ordered list of step objects:
                             [{order, action, parameters, duration, notes}]
critical_parameters     [R]  list of {parameter, target, tolerance,
                             failure_at_off_spec}
equipment_required      [R]  list of {instrument_class, optional_model,
                             notes}
materials_required      [R]  list of {material, vendor, part_number_optional}
validated_outcome       [O]  measured outcomes (channel dimensions,
                             surface roughness, bond strength, yield)
failure_modes           [O]  list of {mode, diagnostic_signature,
                             corrective_action}
related_cad_designs     [O]  ids in ../cad/ this recipe produces or
                             supports
related_corpus_entries  [O]  ids in ../corpus/ this recipe implements or
                             descends from
publication_citation    [O]  primary citation if the recipe is from a
                             paper or thesis
sources                 [R]  references including SOPs, datasheets,
                             handbooks
notes                   [O]  free-text, including patent-encumbrance flags
draft                   [O]  boolean
schema_version          [R]  integer matching schema spec version
last_updated            [R]  ISO 8601 date
```

## Recipe class taxonomy

- `pdms-soft-lithography` — SU-8 master + PDMS replica + bonding
- `glass-photolithography` — mask sets, photoresist, HF or BHF etching
- `glass-bonding` — anodic, thermal, fusion bonding processes
- `silicon-bulk-micromachining` — KOH, TMAH, DRIE
- `silicon-surface-micromachining` — sacrificial layer processes
- `thermoplastic-injection-molding` — COC, PMMA, PC tooling
- `thermoplastic-hot-embossing` — pattern transfer to thermoplastic
- `thermoplastic-laser-ablation` — direct-write channel formation
- `paper-microfluidics-patterning` — wax printing, photoresist barriers
- `dlp-sla-enclosed-channels` — DLP-SLA print of internal microfluidics
- `2pp-direct-write` — two-photon polymerization
- `volumetric-3d-printing` — tomographic / DISH-style printing
- `xurography` — vinyl cutting + lamination
- `surface-modification` — plasma activation, silane chemistry, BSA passivation
- `electrode-integration` — thin-film deposition + lithography of electrodes
- `multilayer-lamination` — film-stack assembly with adhesive layers
- `other` — escape hatch with explanation in notes

## Storage format

Master catalog: `recipes.jsonl` — one JSON object per line, append-only,
git-tracked.

Long-form recipe documentation may live alongside in
`recipes/<id>/RECIPE.md` for narrative explanation that doesn't fit the
structured schema. The JSONL row references that file via `notes` or a
top-level `extended_documentation` field.

## Versioning

Schema version increments on breaking changes. Entries carry
`schema_version` so older entries can be migrated. Forks of a recipe that
diverge in steps get a new id, not a version bump on the original.
