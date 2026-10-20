#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d5-ckad..."
ssh controlplane '
kubectl delete namespace ckad-w3d5 --ignore-not-found
kubectl taint nodes node01 dedicated:NoSchedule- 2>/dev/null || true
'
echo "[✓] Reset complete."
