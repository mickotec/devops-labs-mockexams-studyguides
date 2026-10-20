#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d1-ckad..."
ssh controlplane '
kubectl delete namespace ckad-w1d1 --ignore-not-found
rm -f /tmp/webapp-core.yaml
'
echo "[✓] Reset complete."
