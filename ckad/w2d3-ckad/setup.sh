#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d3-ckad (Mounting ConfigMaps as Filesystem Volumes)..."
ssh controlplane 'kubectl create namespace ckad-w2d3 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w2d3-ckad"
