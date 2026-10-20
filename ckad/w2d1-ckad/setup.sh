#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d1-ckad (Container Commands & Arguments Execution)..."
ssh controlplane 'kubectl create namespace ckad-w2d1 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w2d1-ckad"
