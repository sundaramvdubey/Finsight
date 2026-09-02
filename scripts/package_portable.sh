#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/portable/finsight-v1"
ARCHIVE="$ROOT/portable/finsight-v1-static.zip"

cd "$ROOT"
pnpm build
rm -rf "$OUT"
mkdir -p "$OUT"
cp -R dist/public/. "$OUT/"
cp README.md LICENSE "$OUT/"
cp -R docs "$OUT/docs"
cat > "$OUT/run-local.sh" <<'RUNNER'
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
python3 -m http.server 4173
RUNNER
chmod +x "$OUT/run-local.sh"
rm -f "$ARCHIVE"
(cd "$ROOT/portable" && zip -qr "$(basename "$ARCHIVE")" finsight-v1)
printf 'Portable bundle: %s\nArchive: %s\n' "$OUT" "$ARCHIVE"
