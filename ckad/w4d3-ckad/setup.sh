#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d3-ckad (Startup Probes for Slow Initialization Workloads)..."
ssh controlplane 'kubectl create namespace ckad-w4d3 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d3-ckad"
