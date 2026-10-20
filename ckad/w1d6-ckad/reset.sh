#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d6-ckad..."
ssh controlplane 'kubectl delete namespace ckad-w1d6 --ignore-not-found'
echo "[✓] Reset complete."
