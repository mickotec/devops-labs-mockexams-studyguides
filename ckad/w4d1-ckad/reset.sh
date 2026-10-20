#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w4d1-ckad..."
ssh controlplane 'kubectl delete namespace ckad-w4d1 --ignore-not-found'
echo "[✓] Reset complete."
