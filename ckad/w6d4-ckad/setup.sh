#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d4-ckad (NetworkPolicy: Egress Lockdown & DNS Resolution)..."
ssh controlplane '
kubectl create namespace ckad-w6d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w6d4 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d4-ckad"
