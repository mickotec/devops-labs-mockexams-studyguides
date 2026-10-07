#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d2-cka (Taints, Tolerations & Node Affinity)..."
ssh controlplane '
  kubectl delete namespace w3d2-affinity --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d2-affinity
  kubectl taint node node01 workload- 2>/dev/null || true
'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d2-cka"
