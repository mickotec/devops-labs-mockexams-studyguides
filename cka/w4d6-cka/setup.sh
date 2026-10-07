#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d6-cka (Week 4 App Lifecycle & Secret Security Drill)..."
ssh controlplane '
  kubectl delete namespace w4-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4-milestone
'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d6-cka"
