#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d2-ckad..."
ssh controlplane 'kubectl delete namespace ckad-w8d2 --ignore-not-found'
echo "[✓] Reset complete."
