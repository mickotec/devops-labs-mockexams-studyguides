#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d2-ckad (PersistentVolumes & PersistentVolumeClaims)..."
ssh controlplane '
kubectl create namespace ckad-w7d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w7d2 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d2-ckad"
