#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w2d1-ckad..."
ssh controlplane 'kubectl delete namespace ckad-w2d1 --ignore-not-found'
echo "[✓] Reset complete."
