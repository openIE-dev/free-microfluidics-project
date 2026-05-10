# Release 2026.05.10

| | |
|---|---|
| Date (UTC) | 2026-05-10T23:06:05Z |
| Tarball | `corpus-2026.05.10.tar.gz` |
| SHA-256 | `3b56bbf6742b9a1845646af073a988f6466db172d6a3496e7da587c0778d90d9` |
| Entries |     1240 |

## Timestamping artifacts

| Layer | File | Status |
|---|---|---|
| RFC 3161 (FreeTSA) | `freetsa.tsr` | ✓ |
| RFC 3161 (DigiCert) | `digicert.tsr` | ✓ |
| OpenTimestamps | `corpus-2026.05.10.tar.gz.ots` | ✓ (initially unconfirmed) |

## Verification

See `tools/verify_release.sh` for the standard verification procedure,
or run individually:

```
# Verify hash
sha256sum -c SHA256SUMS

# Verify FreeTSA timestamp (download cacert.pem and tsa.crt from freetsa.org)
openssl ts -verify -in freetsa.tsr \
  -data corpus-2026.05.10.tar.gz \
  -CAfile cacert.pem -untrusted tsa.crt

# Verify DigiCert timestamp (download DigiCert chain)
openssl ts -verify -in digicert.tsr \
  -data corpus-2026.05.10.tar.gz \
  -CAfile digicert-chain.pem

# Verify OpenTimestamps proof
ots verify corpus-2026.05.10.tar.gz.ots -f corpus-2026.05.10.tar.gz
```

## What this release attests

The exact byte sequence of `corpus-2026.05.10.tar.gz` (SHA-256 `3b56bbf6742b9a1845646af073a988f6466db172d6a3496e7da587c0778d90d9`)
existed at or before the timestamps recorded in the .tsr and .ots files.
The contents of that tarball — including `corpus.jsonl` with its
    1240 entries — are therefore public disclosures as of those
timestamps, citable as 102 prior art against any patent with a later
effective filing date.

## Discoverability

After release, this tarball should be:

- [ ] Submitted to Google Patents non-patent literature corpus
- [ ] Registered with Crossref / OSF for DOI assignment
- [ ] Posted to arXiv (cs.RO category) as a citeable preprint
- [ ] Linked from openie.dev / project pages for crawler discovery
- [ ] Optionally: high-value entries submitted individually to IP.com

See `TIMESTAMPING.md` for full discoverability checklist.
