#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d5-lfcs..."
sudo rm -f /home/student/.ssh/id_admin_rsa /home/student/.ssh/id_admin_rsa.pub /etc/ssh/sshd_config.d/99-hardening.conf
echo "[✓] Reset complete."
