#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d4-ckad..."
ssh controlplane 'kubectl delete namespace ckad-w2d4 --ignore-not-found'
echo "[✓] Reset complete."
