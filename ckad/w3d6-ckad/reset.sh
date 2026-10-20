#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d6-ckad..."
ssh controlplane 'kubectl delete namespace ckad-w3d6 --ignore-not-found'
echo "[✓] Reset complete."
