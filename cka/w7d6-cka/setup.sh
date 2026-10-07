#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d6-cka (Week 7 Network Mastery Triathlon)..."
ssh controlplane '
  kubectl delete namespace w7d6-triathlon --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d6-triathlon
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d6-cka"
