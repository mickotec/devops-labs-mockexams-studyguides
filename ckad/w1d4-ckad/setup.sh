#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d4-ckad (Deployments, Zero-Downtime Rollouts & Scaling)..."
ssh controlplane '
kubectl create namespace ckad-w1d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl create deployment api-gateway --image=nginx:1.24-alpine --replicas=2 -n ckad-w1d4
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d4-ckad"
