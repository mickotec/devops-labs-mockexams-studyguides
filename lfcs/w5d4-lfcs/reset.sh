#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w5d4-lfcs..."
sudo rm -f /etc/sysctl.d/60-hardening.conf /var/tmp/kernel_params.txt
echo "[✓] Reset complete."
