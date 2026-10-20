#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d4-ckad (Secrets Management & Restricted File Modes)..."
ssh controlplane 'kubectl create namespace ckad-w2d4 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w2d4-ckad"
