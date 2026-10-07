#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d2-cka (Deployments, Rollouts & Revisions)..."
ssh controlplane '
kubectl delete namespace finance --grace-period=0 --force 2>/dev/null || true
kubectl create namespace finance
'
echo "[✓] Environment ready. Review tasks with: ./lab show w2d2-cka"
