#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d5-lfcs (Mandatory Access Control: SELinux & AppArmor)..."
sudo rm -f /var/tmp/apparmor_summary.txt /var/tmp/apparmor_profiles.txt
echo "[✓] Environment ready. Review tasks with: ./lab show w5d5-lfcs"
