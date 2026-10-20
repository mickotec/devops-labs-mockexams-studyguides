#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d1-ckad (Multi-Container Pods & Sidecar Logging)..."
ssh controlplane '
kubectl create namespace ckad-w1d1 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w1d1 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d1-ckad"
