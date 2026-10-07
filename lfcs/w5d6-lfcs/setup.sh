#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d6-lfcs (Security Audit, User Quarantine & Recovery)..."
sudo userdel -r hacked_service 2>/dev/null || true
sudo useradd -m -s /bin/bash hacked_service
echo "hacked_service:P@ss123" | sudo chpasswd
sudo rm -f /etc/sysctl.d/99-security.conf
echo "[✓] Environment ready. Review tasks with: ./lab show w5d6-lfcs"
