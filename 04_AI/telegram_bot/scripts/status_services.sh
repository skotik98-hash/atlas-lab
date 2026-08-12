#!/bin/bash
set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DOMAIN="gui/$(id -u)"

echo "=== ATLAS CONTROL BOT ==="
launchctl print "$DOMAIN/com.atlaslab.controlbot" 2>/dev/null | \
grep -E 'state =|pid =|last exit code' || echo "❌ Не запущен"

echo ""
echo "=== ATLAS WATCHER ==="
launchctl print "$DOMAIN/com.atlaslab.watcher" 2>/dev/null | \
grep -E 'state =|pid =|last exit code' || echo "❌ Не запущен"

echo ""
echo "=== ERROR LOGS ==="

echo "--- Control Bot ---"
tail -n 5 "$BOT_DIR/data/controlbot-error.log" 2>/dev/null || true

echo "--- Watcher ---"
tail -n 5 "$BOT_DIR/data/watcher-error.log" 2>/dev/null || true
