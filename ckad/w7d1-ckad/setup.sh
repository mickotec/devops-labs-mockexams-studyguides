#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d1-ckad (Volume Types: emptyDir & hostPath In-Depth)..."
ssh controlplane '
kubectl create namespace ckad-w7d1 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w7d1 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d1-ckad"
