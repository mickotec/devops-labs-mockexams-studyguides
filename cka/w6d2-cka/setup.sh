#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d2-cka (RBAC (Roles, RoleBindings & ClusterRoles))..."
ssh controlplane '
  kubectl delete namespace w6d2-rbac --grace-period=0 --force 2>/dev/null || true
  kubectl delete clusterrole node-observer 2>/dev/null || true
  kubectl delete clusterrolebinding bind-node-observer 2>/dev/null || true
  kubectl create namespace w6d2-rbac
  kubectl create sa dev-sa -n w6d2-rbac
'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d2-cka"
