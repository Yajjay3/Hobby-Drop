#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
EXT_DIR="$ROOT_DIR/extension"
OUT_FILE="$ROOT_DIR/Hobby-Drop-Firefox.zip"
STAGE_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$STAGE_DIR"
}
trap cleanup EXIT

cp -R "$EXT_DIR"/. "$STAGE_DIR"/
cp "$EXT_DIR/manifest.firefox.json" "$STAGE_DIR/manifest.json"
rm -f "$STAGE_DIR/manifest.firefox.json"

(
  cd "$STAGE_DIR"
  rm -f "$OUT_FILE"
  zip -r "$OUT_FILE" . -x '*.DS_Store' '*/.DS_Store' >/tmp/hobbydrop_firefox_zip.log
)

echo "Created Firefox package: $OUT_FILE"
