#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d3-ckad (ClusterRoles & ClusterRoleBindings)..."
ssh controlplane '
kubectl delete clusterrole cluster-inspector --ignore-not-found
kubectl delete clusterrolebinding bind-cluster-inspector --ignore-not-found
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d3-ckad"
