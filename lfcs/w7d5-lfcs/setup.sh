#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d5-lfcs (SSH Hardening, Key Auth & Time Sync)..."
sudo rm -f /home/student/.ssh/id_admin_rsa /home/student/.ssh/id_admin_rsa.pub /etc/ssh/sshd_config.d/99-hardening.conf
echo "[✓] Environment ready. Review tasks with: ./lab show w7d5-lfcs"
