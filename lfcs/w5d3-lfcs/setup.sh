#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d3-lfcs (Profiles, Template Environments & User Limits)..."
sudo rm -f /etc/skel/WELCOME.txt /etc/profile.d/corp_vars.sh /etc/security/limits.d/80-nofile.conf
echo "[✓] Environment ready. Review tasks with: ./lab show w5d3-lfcs"
