#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d3-ckad (StorageClasses & Dynamic Volume Provisioning)..."
ssh controlplane '
kubectl create namespace ckad-w7d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w7d3 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d3-ckad"
