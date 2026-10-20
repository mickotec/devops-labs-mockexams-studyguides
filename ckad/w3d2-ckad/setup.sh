#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d2-ckad (Multi-Container Pods: Adapter Pattern)..."
ssh controlplane 'kubectl create namespace ckad-w3d2 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d2-ckad"
