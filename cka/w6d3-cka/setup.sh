#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d3-cka (ServiceAccounts & SecurityContexts)..."
ssh controlplane '
  kubectl delete namespace w6d3-sec --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w6d3-sec
'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d3-cka"
