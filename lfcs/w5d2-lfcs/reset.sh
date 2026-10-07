#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w5d2-lfcs..."
sudo rm -f /etc/sudoers.d/90-sysaudit
sudo groupdel sysaudit 2>/dev/null || true
echo "[✓] Reset complete."
