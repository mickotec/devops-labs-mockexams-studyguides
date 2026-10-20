#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d6-ckad..."
ssh controlplane 'kubectl delete namespace ckad-w7d6 --ignore-not-found'
echo "[✓] Reset complete."
