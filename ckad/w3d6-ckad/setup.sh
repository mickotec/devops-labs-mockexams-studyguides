#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d6-ckad (Node Selectors & Required NodeAffinity)..."
ssh controlplane '
kubectl create namespace ckad-w3d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl label nodes node02 storage-tier- 2>/dev/null || true
'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d6-ckad"
