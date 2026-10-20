#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d2-ckad..."
ssh controlplane 'kubectl delete namespace ckad-w7d2 --ignore-not-found'
echo "[✓] Reset complete."
