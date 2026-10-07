#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d5-lfcs (System Integrity, Resource Monitoring & Top)..."
sudo rm -f /var/tmp/system_specs.txt /etc/sysctl.d/99-swappiness.conf
sudo sysctl -w vm.swappiness=60 >/dev/null
echo "[✓] Environment ready. Review tasks with: ./lab show w3d5-lfcs"
