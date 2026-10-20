#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d5-ckad (Node Taints, Effects & Pod Tolerations)..."
ssh controlplane '
kubectl create namespace ckad-w3d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl taint nodes node01 dedicated=analytics:NoSchedule --overwrite 2>/dev/null || true
'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d5-ckad"
