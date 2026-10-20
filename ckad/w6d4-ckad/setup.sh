#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d4-ckad (NetworkPolicies: Pod & Port Specific Ingress Rules)..."
ssh controlplane '
kubectl create namespace ckad-w6d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run api-backend --image=nginx:alpine -n ckad-w6d4 -l tier=backend
'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d4-ckad"
