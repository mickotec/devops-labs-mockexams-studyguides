#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d1-lfcs (Containers & Virtual Machines on Linux)..."
which podman >/dev/null 2>&1 || (sudo apt-get update -y && sudo apt-get install -y podman 2>/dev/null || true)
podman rm -f web-container data-worker 2>/dev/null || true
sudo rm -rf /var/data/worker /var/tmp/container_ip.txt
echo "[✓] Environment ready. Review tasks with: ./lab show w8d1-lfcs"
