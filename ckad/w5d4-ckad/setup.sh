#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d4-ckad (Container Logging: Multi-Container & Previous Logs)..."
ssh controlplane '
kubectl create namespace ckad-w5d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w5d4 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d4-ckad"
