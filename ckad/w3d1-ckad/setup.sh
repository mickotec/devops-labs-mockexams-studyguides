#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d1-ckad (Multi-Container Pods: Sidecar Log Streaming)..."
ssh controlplane 'kubectl create namespace ckad-w3d1 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d1-ckad"
