#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d4-cka (Autoscaling: HPA, VPA & In-Place Pod Resize)..."
ssh controlplane '
  kubectl delete namespace w4d4-scale --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4d4-scale
'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d4-cka"
