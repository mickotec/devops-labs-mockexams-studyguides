#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d1-lfcs..."
podman rm -f web-container data-worker 2>/dev/null || true
sudo rm -rf /var/data/worker /var/tmp/container_ip.txt
echo "[✓] Reset complete."
