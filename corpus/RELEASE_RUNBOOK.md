---
title: Release runbook
layout: default
nav_order: 7
---

# Release Runbook — 2026.Q2

This is the step-by-step procedure for cutting the first quarterly
release on your machine. Everything in this directory is ready to ship;
the steps below are the external actions that require your credentials
and machine.

## Pre-built artifacts in this directory

A dry-run release has already been built and verified:

- `releases/2026.Q2/corpus-2026.Q2.tar.gz` — release tarball (376 entries)
- `releases/2026.Q2/SHA256SUMS` — `<computed at first release>`

The tarball is **deterministic**: rebuilding on your machine from the same
source produces byte-identical output and the same SHA-256. This matters
because it means anyone can independently verify the release content from
the source repo.

## Step 1: Create the GitHub repo

The umbrella monorepo holds the corpus, cad, fab, and control sub-trees.
Create it once via the GitHub CLI:

```bash
gh repo create openie-dev/free-microfluidics-project \
  --public \
  --description "Four-layer CC0 microfluidics commons (corpus, CAD, fab, control)." \
  --homepage "https://openie.dev"
```

Or via the web UI at https://github.com/organizations/openie-dev/repositories/new
with the same name, public, no README/license/gitignore (those are in
the directory already).

## Step 2: Push the prepared directory

From the **monorepo root** (one level above this corpus subdir):

```bash
cd ..   # if currently in corpus/
git init -b main
git add .
git commit -m "Initial commit: free-microfluidics-project seed

corpus/   — 376 entries, 375 commons-grade, 1 draft, 92 cross-cuts
cad/      — 38 designs (all draft, awaiting CAD artifacts)
fab/      — 25 recipes, 24 commons-grade, 1 draft
control/  — 32 instruments (all draft, awaiting hardware/firmware)

Schema versions per sub-tree. Validation clean across all four.
See README.md and per-sub-tree READMEs for context."

git remote add origin git@github.com:openie-dev/free-microfluidics-project.git
git push -u origin main
```

If you already initialized git, just `git add . && git commit && git push`.

## Step 3: Install OpenTimestamps client

The release script needs `ots` for Bitcoin anchoring. Install it once:

```bash
pip install opentimestamps-client
# or
pipx install opentimestamps-client
```

Confirm:
```bash
ots --version
```

## Step 4: Run the release ceremony

Before running the actual release, **delete the dry-run artifacts** so
the script can build them fresh with real timestamping:

```bash
rm -rf releases/2026.Q2
git add -A && git commit -m "chore: clear dry-run release dir before real release"
```

Now run the release:

```bash
./release.sh 2026.Q2
```

The script will:

1. Validate the corpus passes strict mode
2. Regenerate CORPUS_INDEX.md, lineage.json, per-corpus mirrors, cross-cuts
3. Build the deterministic tarball (will produce the same SHA-256:
   `<computed at first release>`)
4. Submit the hash to FreeTSA (RFC 3161, free)
5. Submit the hash to DigiCert (RFC 3161, free)
6. Submit to OpenTimestamps (Bitcoin anchoring, free)
7. Write `MANIFEST.md` documenting the release
8. Commit the release directory and tag the commit `2026.Q2`

If FreeTSA or DigiCert is temporarily down, the script will warn and
continue — as long as at least one RFC 3161 layer succeeds plus
OpenTimestamps, the release is valid. (You can also re-run the script
later if needed; the deterministic tarball means re-submission produces
the same hash.)

## Step 5: Push the release

```bash
git push origin main
git push origin 2026.Q2
```

## Step 6: Upgrade the OpenTimestamps proof (in ~6 hours)

OpenTimestamps initially produces an unconfirmed proof. After a few
hours, the proof is upgraded to a Bitcoin-anchored confirmed proof.
Run this then:

```bash
ots upgrade releases/2026.Q2/corpus-2026.Q2.tar.gz.ots
git add releases/2026.Q2/corpus-2026.Q2.tar.gz.ots
git commit -m "release: upgrade 2026.Q2 OpenTimestamps proof"
git push
```

This is when the Bitcoin-anchored proof becomes verifiable. Before this
upgrade, the proof exists but verification just shows "pending."

## Step 7: Verify the release independently

To confirm everything worked:

```bash
./tools/verify_release.sh 2026.Q2
```

This is the same script third parties (examiners, attorneys) will run
to verify the release. It checks the SHA-256, the RFC 3161 timestamps,
and the OpenTimestamps proof.

## Step 8: Discoverability submissions

After the release tag is pushed and the OTS proof upgraded, the corpus
exists publicly with cryptographic proof of pre-existence. The remaining
work is making sure examiners and invalidity-contention attorneys
actually find it.

In rough priority order:

### 8a. Crossref / OSF / Zenodo for DOI assignment

The fastest path to a citable DOI is **Zenodo**. Zenodo integrates with
GitHub:

1. Go to https://zenodo.org/account/settings/github/
2. Sign in with GitHub
3. Find `openie-dev/free-microfluidics-project` and toggle it on
4. Trigger a Zenodo deposit by creating a GitHub release pointing at
   the `2026.Q2` tag (use the GitHub web UI: Releases → Draft new release →
   Choose tag `2026.Q2` → Publish release)
5. Zenodo automatically mints a DOI and archives the release tarball

Once the DOI is assigned, add it to the README and to MANIFEST.md.

### 8b. arXiv preprint

Optionally, write a short paper describing the corpus methodology and
post to arXiv (q-bio.QM (with cross-listing to physics.flu-dyn) category). The corpus tarball can be referenced
as supplementary material via the Zenodo DOI. This puts the corpus into
arXiv's index, which is heavily used by researchers and increasingly by
patent examiners.

A 2-3 page methods paper is sufficient: schema, quality bar, timestamping
ceremony, intended use as defensive publication.

### 8c. Google Patents non-patent literature

Google Patents indexes a subset of the open web. Once the repo is public
and has incoming links from openie.dev or other indexed sites, it should
get crawled. To accelerate:

1. Add the repo URL to openie.dev with descriptive anchor text
2. Submit the URL to Google Search Console
3. If you've gone the arXiv route, the arXiv URL is already in Google
   Patents' NPL corpus

### 8d. Internet Archive / Wayback Machine

Submit the GitHub repo URL and the release tarball URL to the Wayback
Machine. This adds another independent timestamping layer:

```
https://web.archive.org/save/https://github.com/openie-dev/free-microfluidics-project
https://web.archive.org/save/https://github.com/openie-dev/free-microfluidics-project/releases/tag/2026.Q2
```

### 8e. Strategic announcements

Once the above is in place, the release becomes useful to others. Worth
considering:

- Blog post on openie.dev introducing the corpus and its purpose
- Posts to relevant communities (r/microfluidics, r/labrats, Hacker News, robotics-worldwide
  mailing list, RAS distinguished list)
- Direct outreach to academic labs with open hardware programs (K-Scale,
  Berkeley Humanoid lab, ETH RSL, etc.) — they are likely contributors
  and benefit from the commons existing
- Direct outreach to patent attorneys working invalidity contention
  in robotics — they are the consumers of the cross-cuts

## What "done" looks like

After all steps above, the corpus has:

1. A public GitHub repo with the full data, tools, and documentation
2. A tagged release with a deterministic, hash-verifiable tarball
3. Three independent cryptographic timestamps (FreeTSA, DigiCert,
   OpenTimestamps Bitcoin) attesting to pre-existence
4. A Zenodo-minted DOI for academic citation
5. Indexing into examiner-discoverable channels (Google Patents NPL,
   arXiv, Wayback Machine)
6. Public announcement so contributors and consumers find it

At that point, every entry in the corpus is functionally citeable as
102 prior art globally, and the corpus has begun to serve its purpose
as a defensive publication archive for microfluidics.

## If something goes wrong

The release script is idempotent within a version. If a step fails, fix
the underlying issue and re-run — the deterministic tarball means the
hash stays stable.

The one thing that can't be retried: once a git tag is pushed to the
public remote, deleting and re-tagging is bad form and confuses
downstream consumers. So don't push the tag until you're confident the
release directory is correct.

If you need to fix something **after** the tag is pushed, cut a new tag
(`2026.Q2.1` or move on to `2026.Q3`) rather than rewriting history.

## Quarterly cadence

After 2026.Q2 ships, the cadence is:

- 2026.Q3 in early July 2026
- 2026.Q4 in early October 2026
- 2027.Q1 in early January 2027

Each quarter captures the corpus state at that moment with full
timestamping. New entries added between quarters get their commons-grade
status at the next release.

For high-value entries added specifically to function as prior art
against a known patent threat, interim timestamping of the individual
entry is worth doing — see TIMESTAMPING.md.
