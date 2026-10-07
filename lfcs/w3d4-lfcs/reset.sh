#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d4-lfcs..."
sudo killall -9 rogue-sim batch-calc 2>/dev/null || true
sudo rm -f /var/tmp/process_report.txt
echo "[✓] Reset complete."
