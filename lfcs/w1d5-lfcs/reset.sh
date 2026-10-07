#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d5-lfcs..."
rm -f /var/tmp/app_legacy.conf /var/tmp/sample_audit.log /var/tmp/status_summary.txt
echo "[✓] Reset complete."
