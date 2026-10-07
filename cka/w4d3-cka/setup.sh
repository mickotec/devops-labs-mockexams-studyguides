#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d3-cka (Secrets Management & Encryption at Rest)..."
ssh controlplane '
  kubectl delete namespace w4d3-secrets --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4d3-secrets
'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d3-cka"
