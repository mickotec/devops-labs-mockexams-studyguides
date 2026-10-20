#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d6-ckad..."
ssh controlplane '
kubectl delete namespace ckad-w8d6 --ignore-not-found
rm -rf /tmp/kustomize-store
'
echo "[✓] Reset complete."
