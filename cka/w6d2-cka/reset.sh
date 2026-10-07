#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w6d2-cka..."
ssh controlplane '
  kubectl delete namespace w6d2-rbac --grace-period=0 --force 2>/dev/null || true
  kubectl delete clusterrole node-observer 2>/dev/null || true
  kubectl delete clusterrolebinding bind-node-observer 2>/dev/null || true
'
echo "[✓] Reset complete."
