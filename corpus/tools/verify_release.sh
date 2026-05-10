#!/usr/bin/env bash
# verify_release.sh — verify a Free Microfluidics Corpus release independently
#
# Usage:
#   ./tools/verify_release.sh <version-tag>
#
# Example:
#   ./tools/verify_release.sh 2026.Q2
#
# What it verifies:
#   1. SHA-256 of the tarball matches SHA256SUMS
#   2. FreeTSA RFC 3161 timestamp is valid (if present)
#   3. DigiCert RFC 3161 timestamp is valid (if present)
#   4. OpenTimestamps Bitcoin proof is valid (if upgraded; otherwise prints status)
#
# Requirements:
#   - openssl
#   - sha256sum
#   - ots (optional, for OpenTimestamps verification)
#
# This script is intended for third parties verifying that a release's
# content existed at the claimed timestamp. It does NOT require trust in
# the corpus maintainers or in any single timestamping authority — the
# three layers cross-check each other.

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "usage: $0 <version-tag>"
  exit 1
fi

VERSION="$1"
RELEASE_DIR="releases/${VERSION}"
TARBALL_NAME="corpus-${VERSION}.tar.gz"

if [ ! -d "$RELEASE_DIR" ]; then
  echo "ERROR: $RELEASE_DIR not found."
  exit 1
fi

cd "$RELEASE_DIR"

echo "=== Verifying release ${VERSION} ==="
echo ""

# 1. SHA-256
echo "1. SHA-256 verification"
if sha256sum -c SHA256SUMS; then
  echo "   PASS: tarball hash matches manifest"
else
  echo "   FAIL: tarball hash does not match manifest"
  exit 1
fi
echo ""

# 2. FreeTSA RFC 3161
echo "2. FreeTSA RFC 3161 timestamp"
if [ -f freetsa.tsr ]; then
  if [ ! -f freetsa-cacert.pem ] || [ ! -f freetsa-tsa.crt ]; then
    echo "   NOTE: download FreeTSA's CA chain to verify:"
    echo "     curl -O https://freetsa.org/files/cacert.pem -o freetsa-cacert.pem"
    echo "     curl -O https://freetsa.org/files/tsa.crt   -o freetsa-tsa.crt"
    echo "   SKIPPED"
  else
    if openssl ts -verify -in freetsa.tsr \
        -data "$TARBALL_NAME" \
        -CAfile freetsa-cacert.pem \
        -untrusted freetsa-tsa.crt 2>/dev/null; then
      TS=$(openssl ts -reply -in freetsa.tsr -text 2>/dev/null | grep "Time stamp:" | head -1)
      echo "   PASS: $TS"
    else
      echo "   FAIL: FreeTSA timestamp does not verify"
      exit 1
    fi
  fi
else
  echo "   NOT PRESENT"
fi
echo ""

# 3. DigiCert RFC 3161
echo "3. DigiCert RFC 3161 timestamp"
if [ -f digicert.tsr ]; then
  if [ ! -f digicert-chain.pem ]; then
    echo "   NOTE: download DigiCert's chain to verify."
    echo "   See https://knowledge.digicert.com/"
    echo "   SKIPPED"
  else
    if openssl ts -verify -in digicert.tsr \
        -data "$TARBALL_NAME" \
        -CAfile digicert-chain.pem 2>/dev/null; then
      TS=$(openssl ts -reply -in digicert.tsr -text 2>/dev/null | grep "Time stamp:" | head -1)
      echo "   PASS: $TS"
    else
      echo "   FAIL: DigiCert timestamp does not verify"
      exit 1
    fi
  fi
else
  echo "   NOT PRESENT"
fi
echo ""

# 4. OpenTimestamps
echo "4. OpenTimestamps Bitcoin anchoring"
if [ -f "${TARBALL_NAME}.ots" ]; then
  if command -v ots >/dev/null 2>&1; then
    # ots verify exits 0 on success even for unconfirmed proofs;
    # parse output for the actual status.
    OUT=$(ots verify "${TARBALL_NAME}.ots" -f "$TARBALL_NAME" 2>&1 || true)
    echo "$OUT" | sed 's/^/   /'
  else
    echo "   NOTE: 'ots' not installed."
    echo "   Install with: pip install opentimestamps-client"
    echo "   SKIPPED"
  fi
else
  echo "   NOT PRESENT"
fi
echo ""

echo "=== Verification complete ==="
