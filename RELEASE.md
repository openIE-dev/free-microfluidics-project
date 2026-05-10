# Release model — Free Microfluidics Project

The four sub-trees release on independent quarterly cadences. Each
sub-tree builds its own deterministic tarball, gets its own SHA-256
hash, and gets its own triple-cryptographic timestamp (FreeTSA +
DigiCert + OpenTimestamps).

## Per-sub-tree status

| Sub-tree | Release ceremony | Status |
|:---|:---|:---|
| `corpus/` | [corpus/RELEASE_RUNBOOK.md](corpus/RELEASE_RUNBOOK.md), [corpus/TIMESTAMPING.md](corpus/TIMESTAMPING.md), [corpus/release.sh](corpus/release.sh) | Ready — 2026.Q2 dry-run built, awaiting first signed release |
| `cad/` | Inherits the corpus ceremony pattern; per-sub-tree `release.sh` not yet written | Needs first commons-grade entries before a release tarball is meaningful |
| `fab/` | Inherits the corpus ceremony pattern; per-sub-tree `release.sh` not yet written | Has 24 commons-grade entries; release ceremony is the next mechanical step |
| `control/` | Inherits the corpus ceremony pattern; per-sub-tree `release.sh` not yet written | Needs first commons-grade entries before a release tarball is meaningful |

## Cadence

Quarterly tags: `2026.Q2`, `2026.Q3`, `2026.Q4`, `2027.Q1`. Each
sub-tree tags as `<sub-tree>-<quarter>`, e.g., `corpus-2026.Q2`,
`fab-2026.Q3`. The corpus may release more frequently than other
sub-trees if its expansion rate warrants it.

## Validation gate

Every release is gated on `./validate-all.sh --strict` passing across
all four sub-trees. A release on one sub-tree should not break the
others; if it does, that's a cross-tree consistency bug to fix before
tagging.

## Why not bundle?

A single quarterly tarball-of-everything is appealing for symmetry but
would couple release cadences — corpus expansion would block on cad
artifact deposition, etc. Independent per-sub-tree releases let each
mature on its own schedule. The umbrella repo coordinates discovery
and governance, not release timing.
