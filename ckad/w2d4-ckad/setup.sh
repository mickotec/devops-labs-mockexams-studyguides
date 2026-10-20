#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d4-ckad (SecurityContexts: UID, GID & Linux Capabilities)..."
ssh controlplane '
kubectl create namespace ckad-w2d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w2d4 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w2d4-ckad"
