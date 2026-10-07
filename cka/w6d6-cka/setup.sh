#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d6-cka (Security & Storage Lab Triathlon)..."
ssh controlplane '
  kubectl delete namespace w6-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv m6-pv 2>/dev/null || true
  kubectl create namespace w6-milestone
'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d6-cka"
