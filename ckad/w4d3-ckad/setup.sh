#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d3-ckad (Canary Deployment Strategy with Weighted Traffic)..."
ssh controlplane '
kubectl create namespace ckad-w4d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w4d3 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d3-ckad"
