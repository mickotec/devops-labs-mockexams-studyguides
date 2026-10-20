#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d5-ckad..."
ssh controlplane 'kubectl delete namespace ckad-w2d5 --ignore-not-found'
echo "[✓] Reset complete."
