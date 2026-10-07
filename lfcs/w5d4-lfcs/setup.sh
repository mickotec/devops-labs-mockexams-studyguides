#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d4-lfcs (Kernel Runtime Tuning with Sysctl)..."
sudo rm -f /etc/sysctl.d/60-hardening.conf /var/tmp/kernel_params.txt
echo "[✓] Environment ready. Review tasks with: ./lab show w5d4-lfcs"
