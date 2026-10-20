#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up mock-ckad-2..."
ssh controlplane '
NS_LIST=$(for q in {1..16}; do echo -n "mock-ckad-2-q$q "; done)
kubectl delete namespace $NS_LIST --ignore-not-found --wait=false 2>/dev/null || true
rm -rf /tmp/kustomize-store /tmp/hpa-version.txt /tmp/top-pod.txt
'
echo "[✓] Reset complete."
