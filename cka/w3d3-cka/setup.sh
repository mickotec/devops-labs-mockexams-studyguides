#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d3-cka (Resource Requirements, Limits & LimitRanges)..."
ssh controlplane '
  kubectl delete namespace w3d3-resources --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d3-resources
'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d3-cka"
