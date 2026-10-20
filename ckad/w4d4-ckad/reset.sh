#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w4d4-ckad..."
ssh controlplane 'kubectl delete namespace ckad-w4d4 --ignore-not-found'
echo "[✓] Reset complete."
