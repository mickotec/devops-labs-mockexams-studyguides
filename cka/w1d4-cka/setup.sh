#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d4-cka (Multi-Container Pod Patterns & Init Containers)..."
ssh controlplane '
kubectl delete namespace telemetry --grace-period=0 --force 2>/dev/null || true
kubectl create namespace telemetry
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d4-cka"
