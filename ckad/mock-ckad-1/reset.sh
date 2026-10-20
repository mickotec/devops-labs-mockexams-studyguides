#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up mock-ckad-1..."
ssh controlplane '
NS_LIST=$(for q in {1..16}; do echo -n "mock-ckad-1-q$q "; done)
kubectl delete namespace $NS_LIST --ignore-not-found --wait=false 2>/dev/null || true
kubectl delete pv mock1-pv --ignore-not-found --wait=false 2>/dev/null || true
rm -f /tmp/fatal-errors.txt
'
echo "[✓] Reset complete."
