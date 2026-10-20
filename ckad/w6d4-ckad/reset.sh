#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w6d4-ckad..."
ssh controlplane 'kubectl delete namespace ckad-w6d4 --ignore-not-found'
echo "[✓] Reset complete."
