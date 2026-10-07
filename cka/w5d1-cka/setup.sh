#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d1-cka (Node Maintenance: Cordon, Drain & Uncordon)..."
ssh controlplane '
  kubectl uncordon node01 node02 2>/dev/null || true
  kubectl delete namespace w5d1-maint --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w5d1-maint
  kubectl create deployment test-maint -n w5d1-maint --image=nginx:alpine --replicas=3
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d1-cka"
