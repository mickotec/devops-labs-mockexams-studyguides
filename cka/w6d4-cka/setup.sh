#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d4-cka (Storage: Volumes, PV, PVC & StorageClasses)..."
ssh controlplane '
  kubectl delete namespace w6d4-storage --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv app-data-pv 2>/dev/null || true
  kubectl create namespace w6d4-storage
'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d4-cka"
