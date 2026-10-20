#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d2-ckad (Headless Services & Direct Pod Discovery)..."
ssh controlplane 'kubectl create namespace ckad-w6d2 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d2-ckad"
