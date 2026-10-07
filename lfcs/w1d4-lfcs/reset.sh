#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d4-lfcs..."
sudo rm -rf /opt/campaigns /var/tmp/world_writable_audit.txt
sudo groupdel marketing 2>/dev/null || true
echo "[✓] Reset complete."
