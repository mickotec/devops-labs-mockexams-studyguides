#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d3-ckad (NetworkPolicies: Default Ingress Denial)..."
ssh controlplane '
kubectl create namespace ckad-w6d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run secure-db --image=redis:alpine -n ckad-w6d3 -l app=db
kubectl expose pod secure-db -n ckad-w6d3 --name=db-svc --port=6379
'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d3-ckad"
