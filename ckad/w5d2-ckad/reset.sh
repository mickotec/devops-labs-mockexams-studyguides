#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w5d2-ckad..."
ssh controlplane 'kubectl delete namespace ckad-w5d2 --ignore-not-found'
echo "[✓] Reset complete."
