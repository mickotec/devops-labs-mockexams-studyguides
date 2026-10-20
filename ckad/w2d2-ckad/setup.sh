#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d2-ckad (ConfigMaps & Environment Variable Injections)..."
ssh controlplane 'kubectl create namespace ckad-w2d2 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w2d2-ckad"
