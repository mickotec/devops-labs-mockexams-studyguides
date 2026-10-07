#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d1-cka (Commands & Arguments (Docker vs Kubernetes))..."
ssh controlplane '
  kubectl delete namespace w4d1-cmd --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4d1-cmd
'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d1-cka"
