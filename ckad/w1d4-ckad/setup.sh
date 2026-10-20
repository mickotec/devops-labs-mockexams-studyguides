#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d4-ckad (Advanced Output Formatting with JSONPath)..."
ssh controlplane '
kubectl create namespace ckad-w1d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=kube-system pods -n ckad-w1d4 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d4-ckad"
