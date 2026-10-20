#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d6-ckad (ServiceAccounts & API Token Security)..."
ssh controlplane 'kubectl create namespace ckad-w2d6 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w2d6-ckad"
