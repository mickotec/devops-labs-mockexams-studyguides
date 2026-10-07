#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w5d3-lfcs..."
sudo rm -f /etc/skel/WELCOME.txt /etc/profile.d/corp_vars.sh /etc/security/limits.d/80-nofile.conf
echo "[✓] Reset complete."
