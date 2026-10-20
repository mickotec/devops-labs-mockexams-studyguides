#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d3-ckad..."
ssh controlplane 'kubectl delete namespace ckad-w8d3 --ignore-not-found'
echo "[✓] Reset complete."
