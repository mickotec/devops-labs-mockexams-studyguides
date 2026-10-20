#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d3-ckad (NetworkPolicy: Ingress Isolation & Pod Selectors)..."
ssh controlplane '
kubectl create namespace ckad-w6d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w6d3 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d3-ckad"
