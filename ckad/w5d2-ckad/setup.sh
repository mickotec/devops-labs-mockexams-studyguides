#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d2-ckad (Rolling Updates with Zero-Downtime MaxSurge)..."
ssh controlplane '
kubectl create namespace ckad-w5d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl create deployment payment-gateway --image=nginx:1.24-alpine --replicas=3 -n ckad-w5d2
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d2-ckad"
