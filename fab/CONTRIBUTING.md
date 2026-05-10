# Contributing to Free Microfluidics Fab

Thank you for considering a contribution. Before you submit a recipe,
please read this carefully — the contribution model here is unusual.

## What you are doing when you contribute

**You are publishing a fabrication procedure that a competent process
engineer can reproduce, with critical-parameter ranges, equipment
requirements, validated outcomes, and known failure modes documented.**

The catalog exists because microfluidic fabrication is folkloric.
Recipes circulate as Word documents between collaborating groups; SI
sections of papers are typically inadequate; muscle memory of senior
cleanroom staff doesn't scale. A deposit here turns one lab's working
procedure into reproducible practice for everyone else.

## CC0 dedication

By submitting a contribution you dedicate it to the public domain
under CC0 1.0. Recipes implementing patented process steps are
allowed but the encumbrance must be flagged in `notes` so commercial
users can assess freedom-to-operate. Most recipes are not patentable
as recipes, but specific equipment usages or proprietary materials
sometimes are.

## What counts as a commons-grade entry

An entry is **commons-grade** (`draft: false`) when it satisfies all
five criteria:

### 1. Critical parameters are explicit, with ranges

The `steps` array must enumerate every step that materially affects
yield, with parameter ranges for spin speed, bake time/temperature,
exposure dose, develop time, etch rate, bond pressure, etc. Single
values without tolerance are a draft signal. "Bake at 95°C for 60s"
is fine; "soft bake the resist" is not.

### 2. Equipment requirements are named explicitly

Equipment categories matter: contact aligner vs. mask aligner vs. UV
LED panel; spin coater vs. drop-cast vs. spray; convection oven vs.
hotplate vs. IR cure. Recipes here must be reproducible without a
Class 100 cleanroom — when a cleanroom-grade step has a benchtop
substitute, document the substitution.

### 3. Validated outcomes are quantitative

The `validated_outcomes` field captures what the recipe actually
produces: feature resolution achieved, surface roughness, bond
strength, yield over runs. Numbers, not adjectives. "Produces clean
features" is not an outcome; "100 µm features at 95% yield over 12
runs, sidewall roughness <50 nm" is.

### 4. Known failure modes are enumerated

The `failure_modes` array lists each common failure (delamination,
incomplete bonding, channel collapse, residual photoresist, voids in
the cure) along with its diagnostic signature (what it looks like)
and the corrective action. Recipes without failure modes documented
are recipes without battle scars — likely incomplete.

### 5. Sources are primary references

The `sources` array lists SOPs, datasheets, handbooks, theses, or
primary papers. Aggregator URLs are acceptable as supplements only.

## Submitting a draft

Mark the entry `"draft": true` and document in `notes` what work would
be needed to clear the bar. Drafts capture what is known and identify
the strengthening work needed. The 1 current draft entry needs
additional critical-parameter documentation before it clears the
commons-grade bar.

## Practical workflow

1. Run `python3 tools/validate.py recipes.jsonl --strict` before
   submitting. This catches structural errors and quality-bar failures.
2. Append a new line to `recipes.jsonl` matching `SCHEMA.md`.
3. Optionally, place extended narrative documentation at
   `recipes/<id>/RECIPE.md` (photos, oscilloscope traces, alignment
   tips, failure-mode photographs).
4. Open a pull request.

## Choosing a good slug

The `id` field is a kebab-case slug used in cross-references from
`../cad/` and `../control/`. Pick one that disambiguates on process
class, substrate, and any distinguishing parameter:

- `<class>-<substrate>-<variant>` — e.g.,
  `pdms-su8-soft-lithography-baseline`,
  `dlp-sla-enclosed-channels-pegda-baseline`
- `<class>-<distinguishing-feature>` — e.g.,
  `glass-hf-etch-buffered-low-roughness`

Slugs are immutable once an entry is referenced by another sub-tree.
Choose carefully.

## Cross-references to other sub-trees

`related_cad_designs` references designs in `../cad/` that this recipe
produces or supports. `related_corpus_entries` references prior-art
entries in `../corpus/` that this recipe implements or descends from.

## Questions

Open an issue. Discussion of process-class taxonomy, parameter-range
conventions, and quality-bar calibration is welcome.
