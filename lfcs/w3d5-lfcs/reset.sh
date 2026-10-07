#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d5-lfcs..."
sudo rm -f /var/tmp/system_specs.txt /etc/sysctl.d/99-swappiness.conf
sudo sysctl -w vm.swappiness=60 >/dev/null
echo "[✓] Reset complete."
