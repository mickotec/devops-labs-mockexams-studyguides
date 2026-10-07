#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w5d6-lfcs..."
sudo userdel -r hacked_service 2>/dev/null || true
sudo rm -f /etc/sysctl.d/99-security.conf
echo "[✓] Reset complete."
