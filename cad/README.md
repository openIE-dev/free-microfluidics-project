# Free Microfluidics CAD

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

A CC0 catalog of microfluidic chip designs. Every entry includes the actual
CAD files plus the structured metadata needed to fabricate, evaluate, and
cite the design.

Part of the [Free Microfluidics Project](https://github.com/openIE-dev/free-microfluidics-project).

**Status: seeded (38 designs, all draft).** Schema is in place,
validation tooling is functional, and 38 seed designs are populated as
templates. Most carry empty CAD-file stubs — flipping a design from
draft to commons-grade requires real GDSII / DXF / STL artifacts plus
characterization data.

## Why this exists

Microfluidic chip designs are the substrate of every published paper and
every commercial product, but they almost never travel with the publication.
A reader can see the figures, sometimes the geometric dimensions in the
methods section, occasionally the masks in supplementary information — but
fabricating the design requires reverse-engineering, and any fork is
research time spent re-deriving rather than improving.

Addgene solved this for plasmids. PDB solved it for protein structures.
There is no equivalent for chip designs.

The intent here is to be that deposit, with the same operating model: CC0,
structured metadata, characterization data co-located, and trivial CAD
file download.

## What's in here

```
SCHEMA.md           — design-entry schema
designs.jsonl       — master catalog (one JSON object per line)
designs/            — actual CAD files, one subdirectory per design id
INDEX.md            — generated alphabetical index
tools/
  validate.py       — schema and quality-bar enforcement
LICENSE             — CC0-1.0
```

## Quick start

```bash
git clone https://github.com/openIE-dev/free-microfluidics-project.git
cd free-microfluidics-project/cad

# Validate the catalog
python3 tools/validate.py designs.jsonl --strict

# Browse the seed designs
ls designs/
```

## What's seeded

The 38 seed designs span droplet generators, mixers, separators
(DLD, inertial, magnetic, acoustic), traps and incubators,
organ-on-chip platforms, paper microfluidics, point-of-care cartridges,
digital microfluidics electrode arrays, and 96-well plate footprints.
Device classes covered: `droplet-generator`, `mixer-component`,
`organ-on-chip`, `lab-on-chip`, `digital-microfluidics`, `other`.

The seed entries are *intentional placeholders*: the schema entries are
real and the CAD-file slots exist, but the actual GDSII/DXF/STL files
are empty stubs. They serve as templates for community contributions
that supply real artifacts.

## Contributing

If you have a microfluidic chip design that:
- works (validated by you or your group),
- is yours to dedicate (CC0 or permissive license you can release),
- is documented to a level a fabricator could reproduce,

…it belongs here. Open a PR with:

1. A new directory `designs/<id>/` with the CAD files.
2. A new line appended to `designs.jsonl` matching the schema in
   `SCHEMA.md`.
3. The line passing `python3 tools/validate.py designs.jsonl --strict`.

## License

CC0-1.0 across the catalog metadata. Individual CAD files declare their
own license in the `license` field of each entry; CC0-1.0 is preferred
but CERN-OHL-P or compatible permissive licenses are accepted.

---

Public domain (CC0 1.0). Part of the
[Free Microfluidics Project](https://github.com/openIE-dev/free-microfluidics-project).
