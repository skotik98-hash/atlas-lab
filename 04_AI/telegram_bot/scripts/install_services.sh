#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
AGENTS="$HOME/Library/LaunchAgents"
DOMAIN="gui/$(id -u)"

CONTROL_PLIST="$AGENTS/com.atlaslab.controlbot.plist"
WATCHER_PLIST="$AGENTS/com.atlaslab.watcher.plist"

mkdir -p "$AGENTS" "$BOT_DIR/data"

if [ ! -x "$BOT_DIR/.venv/bin/python" ]; then
    echo "❌ Не найден Python Atlas: $BOT_DIR/.venv/bin/python"
    exit 1
fi

if [ ! -f "$BOT_DIR/bot.py" ]; then
    echo "❌ Не найден bot.py"
    exit 1
fi

if [ ! -f "$BOT_DIR/watcher.py" ]; then
    echo "❌ Не найден watcher.py"
    exit 1
fi

cat > "$CONTROL_PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.atlaslab.controlbot</string>

    <key>ProgramArguments</key>
    <array>
        <string>$BOT_DIR/.venv/bin/python</string>
        <string>$BOT_DIR/bot.py</string>
    </array>

    <key>WorkingDirectory</key>
    <string>$BOT_DIR</string>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>StandardOutPath</key>
    <string>$BOT_DIR/data/controlbot.log</string>

    <key>StandardErrorPath</key>
    <string>$BOT_DIR/data/controlbot-error.log</string>
</dict>
</plist>
EOF

cat > "$WATCHER_PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.atlaslab.watcher</string>

    <key>ProgramArguments</key>
    <array>
        <string>$BOT_DIR/.venv/bin/python</string>
        <string>$BOT_DIR/watcher.py</string>
        <string>--interval</string>
        <string>15</string>
    </array>

    <key>WorkingDirectory</key>
    <string>$BOT_DIR</string>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>StandardOutPath</key>
    <string>$BOT_DIR/data/watcher.log</string>

    <key>StandardErrorPath</key>
    <string>$BOT_DIR/data/watcher-error.log</string>
</dict>
</plist>
EOF

plutil -lint "$CONTROL_PLIST"
plutil -lint "$WATCHER_PLIST"

launchctl bootout "$DOMAIN/com.atlaslab.controlbot" 2>/dev/null || true
launchctl bootout "$DOMAIN/com.atlaslab.watcher" 2>/dev/null || true

launchctl bootstrap "$DOMAIN" "$CONTROL_PLIST"
launchctl bootstrap "$DOMAIN" "$WATCHER_PLIST"

launchctl enable "$DOMAIN/com.atlaslab.controlbot"
launchctl enable "$DOMAIN/com.atlaslab.watcher"

launchctl kickstart -k "$DOMAIN/com.atlaslab.controlbot"
launchctl kickstart -k "$DOMAIN/com.atlaslab.watcher"

sleep 2

echo ""
echo "✅ Atlas background services установлены"
echo "🤖 Control Bot: com.atlaslab.controlbot"
echo "👁 Watcher: com.atlaslab.watcher"
