#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d1-ckad..."
ssh controlplane '
rm -f /tmp/custom-kubeconfig
kubectl delete namespace ckad-dev-ns --ignore-not-found
'
echo "[✓] Reset complete."
