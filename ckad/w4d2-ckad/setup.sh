#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d2-ckad (Liveness Probes & Automated Container Healing)..."
ssh controlplane 'kubectl create namespace ckad-w4d2 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d2-ckad"
