#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d1-ckad (Readiness Probes & Service Endpoint Gating)..."
ssh controlplane 'kubectl create namespace ckad-w4d1 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d1-ckad"
