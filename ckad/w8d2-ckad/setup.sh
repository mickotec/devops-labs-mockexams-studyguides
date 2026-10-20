#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d2-ckad (RBAC: Roles & RoleBindings)..."
ssh controlplane 'kubectl create namespace ckad-w8d2 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d2-ckad"
