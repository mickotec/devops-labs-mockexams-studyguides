#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d5-cka (Priority Classes & Multiple Schedulers)..."
ssh controlplane '
  kubectl delete namespace w3d5-priority --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d5-priority
  kubectl delete priorityclass mission-critical low-priority 2>/dev/null || true
'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d5-cka"
