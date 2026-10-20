#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d5-ckad (Labels, Selectors & Annotation Bulk Management)..."
ssh controlplane '
kubectl create namespace ckad-w3d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w3d5 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d5-ckad"
