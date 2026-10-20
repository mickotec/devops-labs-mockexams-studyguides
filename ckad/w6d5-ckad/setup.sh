#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d5-ckad (Ingress Networking: Host, Path Rules & Rewrite Target)..."
ssh controlplane '
kubectl create namespace ckad-w6d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w6d5 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d5-ckad"
