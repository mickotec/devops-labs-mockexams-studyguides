#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w5d1-ckad..."
ssh controlplane '
kubectl delete namespace ckad-w5d1 --ignore-not-found
rm -f /tmp/matched-pods.txt
'
echo "[✓] Reset complete."
