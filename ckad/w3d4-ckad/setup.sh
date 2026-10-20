#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d4-ckad (Taints & Tolerations: Dedicated Workload Isolation)..."
ssh controlplane '
kubectl create namespace ckad-w3d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w3d4 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d4-ckad"
