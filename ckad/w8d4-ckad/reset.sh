#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d4-ckad..."
ssh controlplane '
kubectl delete namespace ckad-w8d4 --ignore-not-found
rm -f /tmp/deprecated-ingress.yaml
'
echo "[✓] Reset complete."
