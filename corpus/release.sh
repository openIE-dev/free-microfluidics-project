#!/usr/bin/env bash
# release.sh — quarterly release ceremony for the Free Microfluidics Corpus
#
# Produces a cryptographically timestamped, third-party-attested release
# of the corpus. After this script runs successfully, every entry in the
# tarball is functionally citeable as 102 prior art with verifiable
# pre-existence proof.
#
# Usage:
#   ./release.sh <version-tag> [--dry-run]
#
# Examples:
#   ./release.sh 2026.Q2          # actual release
#   ./release.sh 2026.Q2 --dry-run # build artifacts, skip TSA submissions and git tag
#
# Requirements (install on your machine before running):
#   - python3 (3.8+)
#   - openssl (for RFC 3161)
#   - curl
#   - tar (GNU tar)
#   - sha256sum
#   - git
#   - ots (OpenTimestamps client): pip install opentimestamps-client
#
# Run from the repo root.

set -euo pipefail

# ---------- argument parsing ----------

if [ $# -lt 1 ]; then
  echo "usage: $0 <version-tag> [--dry-run]"
  echo "example: $0 2026.Q2"
  exit 1
fi

VERSION="$1"
DRY_RUN=0
if [ "${2:-}" = "--dry-run" ]; then
  DRY_RUN=1
  echo "[dry-run mode: will build artifacts and compute hash, but skip TSA submissions and git tag]"
fi

# Validate version tag format: YYYY.QN or YYYY.MM.DD or v-prefixed
if ! echo "$VERSION" | grep -Eq '^v?[0-9]{4}\.(Q[1-4]|[0-9]{2}\.[0-9]{2})$|^v[0-9]+\.[0-9]+\.[0-9]+$'; then
  echo "ERROR: version tag '$VERSION' should match YYYY.QN, YYYY.MM.DD, or vX.Y.Z"
  exit 1
fi

RELEASE_DIR="releases/${VERSION}"
TARBALL_NAME="corpus-${VERSION}.tar.gz"
TARBALL_PATH="${RELEASE_DIR}/${TARBALL_NAME}"

# ---------- preflight checks ----------

echo "=== Preflight checks ==="

# Tool availability
need_tool() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "ERROR: required tool '$1' not found in PATH"
    exit 1
  fi
}
need_tool python3
need_tool openssl
need_tool curl
need_tool sha256sum
need_tool git
# GNU tar is required for deterministic --sort/--mtime flags. On macOS
# bsdtar is the default; install GNU tar via `brew install gnu-tar` (gtar).
if command -v gtar >/dev/null 2>&1; then
  TAR=gtar
elif tar --version 2>/dev/null | grep -q "GNU tar"; then
  TAR=tar
else
  echo "ERROR: GNU tar required (bsdtar lacks --sort)."
  echo "  install with: brew install gnu-tar"
  exit 1
fi
if [ "$DRY_RUN" -eq 0 ]; then
  need_tool ots || {
    echo "ERROR: 'ots' (OpenTimestamps client) required for non-dry-run."
    echo "  install with: pip install opentimestamps-client"
    exit 1
  }
fi

# Repo state checks
if [ ! -f corpus.jsonl ]; then
  echo "ERROR: corpus.jsonl not found. Run from repo root."
  exit 1
fi

if [ "$DRY_RUN" -eq 0 ]; then
  if ! git diff --quiet HEAD 2>/dev/null; then
    echo "ERROR: working tree has uncommitted changes. Commit or stash first."
    git status --short
    exit 1
  fi

  if git rev-parse "$VERSION" >/dev/null 2>&1; then
    echo "ERROR: tag '$VERSION' already exists."
    exit 1
  fi
fi

# Already-released check
if [ -d "$RELEASE_DIR" ] && [ "$DRY_RUN" -eq 0 ]; then
  echo "ERROR: $RELEASE_DIR already exists."
  exit 1
fi

echo "  Preflight OK."

# ---------- step 1: validate corpus ----------

echo ""
echo "=== Step 1: validate corpus ==="
python3 tools/validate.py corpus.jsonl --strict
echo "  Validation passed."

# ---------- step 2: regenerate derived artifacts ----------

echo ""
echo "=== Step 2: regenerate derived artifacts ==="
python3 tools/index.py .
python3 tools/cross_cuts.py
echo "  Index, lineage, per-corpus mirrors, and cross-cuts regenerated."

# Detect drift: if regeneration produced different artifacts than what's
# committed, warn the user.
if [ "$DRY_RUN" -eq 0 ]; then
  if ! git diff --quiet CORPUS_INDEX.md lineage.json *.jsonl cross_cuts/ 2>/dev/null; then
    echo "WARNING: regenerated artifacts differ from committed versions."
    echo "         You probably want to commit these before tagging."
    echo "         Affected files:"
    git diff --name-only CORPUS_INDEX.md lineage.json *.jsonl cross_cuts/ | sed 's/^/           /'
    echo ""
    read -p "Continue anyway? [y/N] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
      exit 1
    fi
  fi
fi

# ---------- step 3: build deterministic release tarball ----------

echo ""
echo "=== Step 3: build release tarball ==="
mkdir -p "$RELEASE_DIR"

# Build with deterministic options so the SHA-256 is reproducible:
#   --sort=name             stable file ordering
#   --owner=0 --group=0     no owner-specific metadata
#   --numeric-owner         no name lookups
#   --mtime=...             pin mtime to the version date for reproducibility
#   --pax-option=...        suppress extended headers that vary by run

# Pin mtime to a version-derived date. For YYYY.QN tags, use the start
# of the quarter; for YYYY.MM.DD use the date directly.
case "$VERSION" in
  *.Q1) MTIME="${VERSION%.Q1}-01-01" ;;
  *.Q2) MTIME="${VERSION%.Q2}-04-01" ;;
  *.Q3) MTIME="${VERSION%.Q3}-07-01" ;;
  *.Q4) MTIME="${VERSION%.Q4}-10-01" ;;
  *.[0-9][0-9].[0-9][0-9]) MTIME=$(echo "$VERSION" | tr '.' '-') ;;
  v*) MTIME=$(date -u +"%Y-%m-%d") ;;
  *) MTIME=$(date -u +"%Y-%m-%d") ;;
esac

$TAR --use-compress-program='gzip -n' -cf "$TARBALL_PATH" \
  --sort=name \
  --owner=0 --group=0 --numeric-owner \
  --mtime="${MTIME}T00:00:00Z" \
  --pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime \
  corpus.jsonl \
  SCHEMA.md \
  CORPUS_INDEX.md \
  lineage.json \
  private.jsonl open.jsonl fictional.jsonl academic.jsonl \
  cross_cuts/ \
  README.md \
  LICENSE \
  CONTRIBUTING.md \
  TIMESTAMPING.md

HASH=$(sha256sum "$TARBALL_PATH" | cut -d' ' -f1)
echo "${HASH}  ${TARBALL_NAME}" > "${RELEASE_DIR}/SHA256SUMS"
echo "  Tarball: ${TARBALL_PATH}"
echo "  SHA-256: ${HASH}"
echo "  (deterministic: same content + same version tag = same hash)"

# Count what's inside
ENTRIES=$(wc -l < corpus.jsonl)
echo "  Contains: ${ENTRIES} corpus entries"

if [ "$DRY_RUN" -eq 1 ]; then
  echo ""
  echo "=== Dry-run complete ==="
  echo "Tarball built at: ${TARBALL_PATH}"
  echo "Hash recorded at: ${RELEASE_DIR}/SHA256SUMS"
  echo "Skipped: TSA submissions, OpenTimestamps anchoring, git tag."
  exit 0
fi

# ---------- step 4: RFC 3161 timestamping ----------

echo ""
echo "=== Step 4: RFC 3161 timestamping ==="

# Build the timestamp request once; submit to two TSAs.
openssl ts -query -data "$TARBALL_PATH" -sha256 -cert -no_nonce \
  -out "${RELEASE_DIR}/request.tsq"

echo "  Submitting to FreeTSA..."
if curl -sS --max-time 30 --fail \
    -H "Content-Type: application/timestamp-query" \
    --data-binary @"${RELEASE_DIR}/request.tsq" \
    https://freetsa.org/tsr \
    -o "${RELEASE_DIR}/freetsa.tsr"; then
  echo "    OK ($(wc -c < "${RELEASE_DIR}/freetsa.tsr") bytes)"
else
  echo "    WARNING: FreeTSA submission failed; continuing with other layers."
  rm -f "${RELEASE_DIR}/freetsa.tsr"
fi

echo "  Submitting to DigiCert..."
if curl -sS --max-time 30 --fail \
    -H "Content-Type: application/timestamp-query" \
    --data-binary @"${RELEASE_DIR}/request.tsq" \
    http://timestamp.digicert.com \
    -o "${RELEASE_DIR}/digicert.tsr"; then
  echo "    OK ($(wc -c < "${RELEASE_DIR}/digicert.tsr") bytes)"
else
  echo "    WARNING: DigiCert submission failed; continuing with other layers."
  rm -f "${RELEASE_DIR}/digicert.tsr"
fi

# Check we got at least one RFC 3161 timestamp
if [ ! -f "${RELEASE_DIR}/freetsa.tsr" ] && [ ! -f "${RELEASE_DIR}/digicert.tsr" ]; then
  echo "ERROR: both RFC 3161 submissions failed. Aborting."
  exit 1
fi

# ---------- step 5: OpenTimestamps Bitcoin anchoring ----------

echo ""
echo "=== Step 5: OpenTimestamps anchoring ==="
ots stamp "$TARBALL_PATH"
mv "${TARBALL_PATH}.ots" "${RELEASE_DIR}/${TARBALL_NAME}.ots"
echo "  OpenTimestamps proof recorded (initially unconfirmed)."
echo "  Run 'ots upgrade ${RELEASE_DIR}/${TARBALL_NAME}.ots' in ~6h to anchor."

# ---------- step 6: write release manifest ----------

echo ""
echo "=== Step 6: write manifest ==="
cat > "${RELEASE_DIR}/MANIFEST.md" <<EOF
# Release ${VERSION}

| | |
|---|---|
| Date (UTC) | $(date -u +"%Y-%m-%dT%H:%M:%SZ") |
| Tarball | \`${TARBALL_NAME}\` |
| SHA-256 | \`${HASH}\` |
| Entries | ${ENTRIES} |

## Timestamping artifacts

| Layer | File | Status |
|---|---|---|
| RFC 3161 (FreeTSA) | \`freetsa.tsr\` | $([ -f "${RELEASE_DIR}/freetsa.tsr" ] && echo "✓" || echo "✗ skipped") |
| RFC 3161 (DigiCert) | \`digicert.tsr\` | $([ -f "${RELEASE_DIR}/digicert.tsr" ] && echo "✓" || echo "✗ skipped") |
| OpenTimestamps | \`${TARBALL_NAME}.ots\` | ✓ (initially unconfirmed) |

## Verification

See \`tools/verify_release.sh\` for the standard verification procedure,
or run individually:

\`\`\`
# Verify hash
sha256sum -c SHA256SUMS

# Verify FreeTSA timestamp (download cacert.pem and tsa.crt from freetsa.org)
openssl ts -verify -in freetsa.tsr \\
  -data ${TARBALL_NAME} \\
  -CAfile cacert.pem -untrusted tsa.crt

# Verify DigiCert timestamp (download DigiCert chain)
openssl ts -verify -in digicert.tsr \\
  -data ${TARBALL_NAME} \\
  -CAfile digicert-chain.pem

# Verify OpenTimestamps proof
ots verify ${TARBALL_NAME}.ots -f ${TARBALL_NAME}
\`\`\`

## What this release attests

The exact byte sequence of \`${TARBALL_NAME}\` (SHA-256 \`${HASH}\`)
existed at or before the timestamps recorded in the .tsr and .ots files.
The contents of that tarball — including \`corpus.jsonl\` with its
${ENTRIES} entries — are therefore public disclosures as of those
timestamps, citable as 102 prior art against any patent with a later
effective filing date.

## Discoverability

After release, this tarball should be:

- [ ] Submitted to Google Patents non-patent literature corpus
- [ ] Registered with Crossref / OSF for DOI assignment
- [ ] Posted to arXiv (cs.RO category) as a citeable preprint
- [ ] Linked from openie.dev / project pages for crawler discovery
- [ ] Optionally: high-value entries submitted individually to IP.com

See \`TIMESTAMPING.md\` for full discoverability checklist.
EOF
echo "  ${RELEASE_DIR}/MANIFEST.md"

# ---------- step 7: git tag ----------

echo ""
echo "=== Step 7: git tag ==="
git add "$RELEASE_DIR"
git commit -m "release: ${VERSION}

${ENTRIES} corpus entries.
SHA-256: ${HASH}"

git tag -a "$VERSION" -m "Free Microfluidics Corpus release ${VERSION}

SHA-256: ${HASH}
Entries: ${ENTRIES}"

echo "  Tagged ${VERSION}."

# ---------- done ----------

echo ""
echo "=========================================="
echo "  Release ${VERSION} complete."
echo "=========================================="
echo ""
echo "Artifacts in: ${RELEASE_DIR}/"
echo ""
echo "Next steps:"
echo "  1. Push: git push origin main && git push origin ${VERSION}"
echo "  2. In ~6 hours, run: ots upgrade ${RELEASE_DIR}/${TARBALL_NAME}.ots"
echo "     then commit the upgraded proof:"
echo "       git add ${RELEASE_DIR}/${TARBALL_NAME}.ots"
echo "       git commit -m 'release: upgrade ${VERSION} OTS proof'"
echo "       git push"
echo "  3. Submit to discoverability indices (see MANIFEST.md checklist)"
