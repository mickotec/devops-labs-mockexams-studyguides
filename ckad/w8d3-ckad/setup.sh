#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d3-ckad (RBAC: ClusterRole & ClusterRoleBinding Global Rules)..."
ssh controlplane '
kubectl create namespace ckad-w8d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=rbac -n ckad-w8d3 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d3-ckad"
