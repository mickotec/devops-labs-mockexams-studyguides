#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d5-ckad (Metrics Server & CLI Resource Monitoring)..."
ssh controlplane '
kubectl create namespace ckad-w5d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=metrics-server -n ckad-w5d5 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d5-ckad"
