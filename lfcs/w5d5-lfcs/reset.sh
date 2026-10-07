#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w5d5-lfcs..."
sudo rm -f /var/tmp/apparmor_summary.txt /var/tmp/apparmor_profiles.txt
echo "[✓] Reset complete."
