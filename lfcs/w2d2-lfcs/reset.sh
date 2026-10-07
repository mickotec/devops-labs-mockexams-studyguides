#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d2-lfcs..."
sudo rm -f /var/tmp/auth_ips.txt /var/tmp/pam_rules.txt /var/tmp/error_count.txt /var/tmp/auth_sample.log
echo "[✓] Reset complete."
