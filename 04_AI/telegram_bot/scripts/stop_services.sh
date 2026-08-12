#!/bin/bash
set -u

DOMAIN="gui/$(id -u)"

launchctl bootout "$DOMAIN/com.atlaslab.controlbot" 2>/dev/null || true
launchctl bootout "$DOMAIN/com.atlaslab.watcher" 2>/dev/null || true

echo "⏹ Atlas Control Bot остановлен"
echo "⏹ Atlas Watcher остановлен"
