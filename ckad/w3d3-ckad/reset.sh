#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d3-ckad..."
ssh controlplane '
kubectl delete namespace ckad-w3d3-infra --ignore-not-found
kubectl delete namespace ckad-w3d3-apps --ignore-not-found
'
echo "[✓] Reset complete."
