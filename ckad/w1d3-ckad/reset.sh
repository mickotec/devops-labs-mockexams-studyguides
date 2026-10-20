#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d3-ckad..."
ssh controlplane 'kubectl delete namespace ckad-w1d3 --ignore-not-found'
echo "[✓] Reset complete."
