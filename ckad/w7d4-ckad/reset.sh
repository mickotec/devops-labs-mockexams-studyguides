#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d4-ckad..."
ssh controlplane '
kubectl delete namespace ckad-w7d4 --ignore-not-found
kubectl delete pv persist-test-pv --ignore-not-found
'
echo "[✓] Reset complete."
