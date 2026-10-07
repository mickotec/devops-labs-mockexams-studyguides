#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d4-lfcs..."
sudo rm -f /var/tmp/stdout.log /var/tmp/stderr.log /var/tmp/process_dump.txt /var/tmp/process_count.txt /var/tmp/gen_health.sh /var/tmp/health.report
echo "[✓] Reset complete."
