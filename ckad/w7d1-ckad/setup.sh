#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d1-ckad (Volumes: emptyDir Memory Cache & hostPath)..."
ssh controlplane 'kubectl create namespace ckad-w7d1 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d1-ckad"
