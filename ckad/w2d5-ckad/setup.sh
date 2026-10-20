#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d5-ckad (SecurityContexts, Non-Root & Linux Capabilities)..."
ssh controlplane 'kubectl create namespace ckad-w2d5 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w2d5-ckad"
