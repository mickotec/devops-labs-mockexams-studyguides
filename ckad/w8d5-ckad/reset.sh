#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d5-ckad..."
ssh controlplane '
helm uninstall frontend-app -n ckad-w8d5 2>/dev/null || true
kubectl delete namespace ckad-w8d5 --ignore-not-found
rm -rf /tmp/sample-chart
'
echo "[✓] Reset complete."
