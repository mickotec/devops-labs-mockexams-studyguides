#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d2-ckad..."
ssh controlplane 'kubectl delete pv app-storage-pv --ignore-not-found'
echo "[✓] Reset complete."
