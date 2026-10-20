#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d3-ckad..."
ssh controlplane '
kubectl delete namespace ckad-w7d3 --ignore-not-found
kubectl delete pv claim-target-pv --ignore-not-found
'
echo "[✓] Reset complete."
