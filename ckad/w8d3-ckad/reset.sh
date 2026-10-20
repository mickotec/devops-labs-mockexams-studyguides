#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d3-ckad..."
ssh controlplane '
kubectl delete clusterrole cluster-inspector --ignore-not-found
kubectl delete clusterrolebinding bind-cluster-inspector --ignore-not-found
'
echo "[✓] Reset complete."
