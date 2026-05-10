---
title: Timestamping
layout: default
nav_order: 6
---

# Timestamping the Corpus

## Why this matters

The corpus is the prior art commons. For an entry to function as defensive
publication, the date of public disclosure must be defensible against
challenge. Git commit timestamps are not third-party attested — they can be
rewritten, and they are not the kind of evidence courts expect. We need
external timestamping by recognized third parties.

This document specifies the ceremony, the choices, the verification procedure,
and the alternatives we evaluated and rejected.

## What gets timestamped

A release tarball containing:

- `corpus.jsonl` — the master corpus at release time
- `SCHEMA.md` — schema spec at release time
- `CORPUS_INDEX.md`, `lineage.json` — derived artifacts
- Per-corpus mirrors (private/open/fictional/academic .jsonl files)
- `cross_cuts/` — all subsystem cross-cut analyses

A SHA-256 hash is computed over the tarball, and the hash is what gets
submitted to the timestamping authorities. This means the timestamp asserts
"this exact byte sequence existed at this exact time" — the strongest form
of pre-existence proof.

## The three layers

### Layer 1: RFC 3161 — FreeTSA

FreeTSA is a free public timestamping authority operated as a service.
Its timestamps are RFC 3161 compliant and verifiable with standard OpenSSL
tooling. Free means we can run unlimited timestamping operations without
budget.

**Trust profile**: medium. FreeTSA is well-regarded but not as broadly
trusted in legal contexts as commercial TSAs. We use it as the always-on
free option.

**Verification**: standard `openssl ts -verify` against FreeTSA's published
CA chain.

### Layer 2: RFC 3161 — DigiCert

DigiCert operates a free public RFC 3161 endpoint at
`http://timestamp.digicert.com`. DigiCert is among the most-trusted
commercial CAs and TSAs in the world. Their timestamps are widely accepted
in legal and technical contexts.

**Trust profile**: high. DigiCert timestamps are accepted in nearly any
court that accepts digital evidence.

**Verification**: standard `openssl ts -verify` against DigiCert's
published certificate chain.

### Layer 3: OpenTimestamps (Bitcoin anchoring)

OpenTimestamps is a free, decentralized timestamping protocol that anchors
hashes into the Bitcoin blockchain. The cryptographic property is that
once a hash is anchored, falsifying its timestamp would require rewriting
the Bitcoin proof-of-work history — which is computationally infeasible.

**Trust profile**: cryptographically maximal. No trust in any single
authority; the proof rests on Bitcoin's hash power.

**Verification**: `ots verify` against the .ots receipt and the original
file.

**Latency**: OpenTimestamps initially produces an unconfirmed proof
within seconds. The proof is upgraded to a Bitcoin-anchored confirmed
proof after typically 1-6 hours. Run `ots upgrade *.ots` later to fetch
the upgraded proof and commit it.

## Why all three?

Belt and braces. Each layer fails differently:

- FreeTSA could go offline or rotate keys without notice. Other timestamps survive.
- DigiCert could change their free endpoint policy. Other timestamps survive.
- Bitcoin could face a 51% attack rewriting recent history (extraordinarily
  unlikely but theoretically possible). Other timestamps survive.

For zero marginal cost (all three are free) we get three independent proofs
of pre-existence. There is no reason not to do this.

## Release cadence

Quarterly tags are the minimum: 2026.Q2, 2026.Q3, etc. Each release
captures the corpus state at that moment with full timestamping.

For high-value individual entries — particularly those added specifically
to function as prior art against a known patent threat — interim
timestamping of just that entry is worth doing. The ceremony scales down:
just hash the entry's JSON line, submit hash to the three layers, commit
receipts under `releases/interim/<entry-id>/`.

## Verification by third parties

A third party (examiner, attorney, journalist) verifies a corpus claim as
follows:

```
# 1. Fetch the release tarball
git clone https://github.com/openie-dev/free-microfluidics-project
cd free-microfluidics-project/corpus
TAG=2026.Q2

# 2. Verify the SHA-256
cd releases/${TAG}
sha256sum -c SHA256SUMS

# 3. Verify the FreeTSA RFC 3161 timestamp
openssl ts -verify -in freetsa.tsr \
  -data corpus-${TAG}.tar.gz \
  -CAfile cacert.pem -untrusted tsa.crt

# 4. Verify the DigiCert RFC 3161 timestamp
openssl ts -verify -in digicert.tsr \
  -data corpus-${TAG}.tar.gz \
  -CAfile digicert-cacert.pem

# 5. Verify the OpenTimestamps Bitcoin proof
ots verify corpus-${TAG}.tar.gz.ots -f corpus-${TAG}.tar.gz
```

If all three verify, the third party has cryptographic proof that the exact
contents of the corpus.jsonl in that release existed at the timestamp moment.
Anything in that corpus.jsonl is therefore a public disclosure as of that
moment, citable as 102 prior art against any patent with a later effective
filing date.

## Alternatives evaluated and rejected

**IP.com defensive publications**. Real legal weight, examiner-discoverable,
but costs $200+ per publication. Not scalable for a 500+ entry commons.
Use IP.com selectively for the highest-value entries (deliberately filed
as defensive publications against specific patent threats), not for the
bulk.

**Bulletin board posting**. Old-school but works (USENET, mailing lists
with archives). Less rigorous than cryptographic timestamping. Skip.

**Notarization (RFC 3161 with notary signature)**. Adds physical-world
trust at high per-document cost. Skip for routine releases; use for
high-stakes filings if needed.

**Wayback Machine**. Indexes content but does not produce a verifiable
cryptographic timestamp. Useful supplement, not substitute. We should
ensure the public repo is crawled by Wayback for additional informal
timestamping.

## Examiner discoverability (separate from timestamping)

Timestamping proves WHEN the disclosure happened. Discoverability ensures
examiners FIND it. Both are necessary; one without the other is not enough.

Discoverability submissions per release:

1. **Google Patents non-patent literature corpus** — submit via Google
   Scholar indexing (the repo's GitHub Pages site, if we set one up,
   gets crawled).
2. **IP.com Prior Art Database** — selective, paid, for the highest-value
   entries.
3. **Crossref / OSF preprints** — register the release as a citable
   preprint with a DOI. This is among the cheapest ways to get into
   examiner search tools.
4. **arXiv** — if framed as a paper, the corpus releases could be
   submitted to arXiv (q-bio.QM, physics.flu-dyn category).
5. **CPC classification tags** — applied at entry level, ensure the corpus
   shows up in classification-based examiner searches.

These submissions are a separate work item from the cryptographic
timestamping; both must happen for the commons to actually function.
