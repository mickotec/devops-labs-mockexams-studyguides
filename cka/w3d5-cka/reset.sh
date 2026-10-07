#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d5-cka..."
ssh controlplane '
  kubectl delete namespace w3d5-priority --grace-period=0 --force 2>/dev/null || true
  kubectl delete priorityclass mission-critical low-priority 2>/dev/null || true
'
echo "[✓] Reset complete."
