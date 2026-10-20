#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d2-ckad (RBAC: Role & RoleBinding Scoped Authorizations)..."
ssh controlplane '
kubectl create namespace ckad-w8d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=rbac -n ckad-w8d2 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d2-ckad"
