#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d3-lfcs..."
sudo rm -rf /srv/data/engineering /etc/profile.d/devops_umask.sh
sudo userdel -r alice 2>/dev/null || true
sudo userdel -r bob 2>/dev/null || true
sudo groupdel devops_eng 2>/dev/null || true
echo "[✓] Reset complete."
