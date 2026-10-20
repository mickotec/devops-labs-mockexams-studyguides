#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d5-ckad..."
ssh controlplane '
kubectl delete namespace ckad-w1d5-backend --ignore-not-found
kubectl delete namespace ckad-w1d5-frontend --ignore-not-found
'
echo "[✓] Reset complete."
