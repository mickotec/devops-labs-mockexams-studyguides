#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d3-lfcs..."
sudo rm -f /var/tmp/regular_users.txt /var/tmp/config_sample.ini /var/tmp/sales.csv /var/tmp/sales_total.txt
echo "[✓] Reset complete."
