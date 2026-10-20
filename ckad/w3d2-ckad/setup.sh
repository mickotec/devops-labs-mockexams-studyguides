#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d2-ckad (Manual Node Scheduling & NodeSelector)..."
ssh controlplane '
kubectl create namespace ckad-w3d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w3d2 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d2-ckad"
