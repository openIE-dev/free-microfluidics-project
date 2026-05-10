---
title: Contributing
layout: default
nav_order: 5
---

# Contributing to the Free Microfluidics Corpus

Thank you for considering a contribution. Before you write an entry,
please read this carefully — the contribution model here is unusual.

## What you are doing when you contribute

**You are writing a defensive publication, not a Wikipedia entry.**

Every entry in this corpus is, at the moment of timestamped release,
a public disclosure citable as 102 prior art against any patent with a
later effective filing date. That is the corpus's reason for existing
and the reason it works.

This means contributions carry weight that ordinary catalog entries do
not. Sloppy citations, fuzzy dates, or hand-wavy prior art notes
weaken the commons for everyone. Tight, primary-sourced, element-by-element
entries strengthen it.

## CC0 dedication

By submitting a contribution you dedicate it to the public domain under
CC0 1.0. The contribution must be your own work or already in the public
domain. Do not copy text wholesale from copyrighted sources — paraphrase
in your own words and cite the source.

## What counts as a good entry

An entry is **commons-grade** (`draft: false`) when it satisfies all five
criteria:

### 1. The disclosure citation resolves to a primary source

The `disclosure_citation` field must point at something a third party can
actually retrieve and verify. Acceptable: a paper with a DOI, a patent
number, a book with an ISBN, a public press release with a date, an
arXiv identifier, an episode of a TV series with first-air-date.

Not acceptable: "Wikipedia," "company website" (without a specific page
and date), "I read this somewhere," secondhand summaries.

### 2. The first disclosure date is defensible

The `first_disclosure_date` must be the earliest verifiable public
disclosure, not the earliest plausible date or the date you happened
to learn about it.

If a robot was demoed at a conference in October 2023 but the company
issued a press release in August 2023, the August date is correct.
If a sci-fi character first appeared in a 1958 novel that was later
adapted into a 1984 film, the 1958 novel is correct.

When in doubt, choose the earliest date you can cite to a primary source.

### 3. The prior art notes are element-by-element analysis

This is the field that does the most work. `prior_art_notes` should read
as the kind of analysis a competent patent examiner or invalidity-contention
attorney would write. It identifies *specific* subsystems disclosed and
what claims those disclosures could anticipate.

Bad example:
> This is an important robot in the field.

Good example:
> Establishes the quasi-direct-drive electric actuator topology with
> proprioceptive backdrivability in a working dynamic-quadruped platform.
> Wensing 2017 IEEE T-RO paper provides full design disclosure including
> motor selection, gear ratio rationale, and torque-control bandwidth
> measurements. Anticipates QDD-claim humanoid actuator patents post-2017.

If you cannot write the second kind, mark the entry `draft: true` and
note in the `notes` field what work would be needed to clear the bar.

### 4. Sources are primary references

The `sources` array should list papers, patents, books, episodes, or
official corporate disclosures. Aggregators (Wikipedia, secondary news
coverage) are acceptable only as supplements, not as the primary citation.

### 5. Patented entries enumerate patents

If `ip_status` is `patented`, then `ip_citations` must list at least one
actual patent number. "Patent filings exist" is not sufficient.

## Submitting an entry below the quality bar

Mark the entry `"draft": true` and document in `notes` what work would
be needed to clear the bar. Drafts are welcome — they make incremental
progress visible without polluting the commons-grade entry pool.

A draft entry is still useful: it reserves the slug, captures what is
known, and identifies the strengthening work needed. Many existing
drafts in the corpus are recent commercial humanoids where public
technical disclosure remains thin; they will become commons-grade as
patents are published or third-party teardowns appear.

## Practical workflow

1. Run `python3 tools/validate.py corpus.jsonl --strict` before submitting.
   This catches structural errors and quality bar failures.
2. Run `python3 tools/index.py .` to regenerate CORPUS_INDEX.md, lineage.json,
   and per-corpus mirrors.
3. Run `python3 tools/cross_cuts.py` to regenerate the prior art views.
4. Commit the regenerated artifacts alongside your entry — they are
   committed deliberately so browsing on GitHub shows the working state.
5. Open a pull request.

## Choosing a good slug

The `id` field is a kebab-case slug used in lineage edges, cross-cuts,
and citations. Pick one that disambiguates well.

- For commercial products: `<company>-<product>` (e.g., `figure-01`,
  `unitree-h1`)
- For academic platforms: `<lab-or-institution>-<name>` (e.g.,
  `mit-cheetah-2`, `berkeley-humanoid`)
- For fictional entities: `<franchise>-<name>` or canonical name
  (e.g., `t-800-terminator`, `data-tng`)
- For software/concepts: descriptive (e.g., `control-barrier-functions`,
  `sherman-simplex-architecture`)

Slugs are immutable once an entry is referenced by another entry's
lineage edges. Choose carefully.

## Subsystem tagging

The `disclosed_subsystems` field uses the controlled vocabulary defined
in SCHEMA.md. Tag every subsystem the entry discloses with enough
specificity to be citeable. Do not invent new tags casually — propose
them in a separate PR if needed, with a rationale.

## Lineage edges

`lineage_ancestors` lists the ids of entries this entry descends from.
`lineage_descendants` is filled in symmetrically by other entries pointing
back, but you can pre-fill it where you know the descendants.

The indexer detects cycles and surfaces missing references as warnings.
Both are diagnostic outputs, not errors — you can submit a PR that
references entries not yet in the corpus and the warning becomes a
to-do item for a later contributor.

## Questions

Open an issue. Discussion of methodology, taxonomy gaps, and quality bar
calibration is welcome.
