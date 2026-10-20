#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d1-ckad (Services: ClusterIP, NodePort & Port Mapping)..."
ssh controlplane 'kubectl create namespace ckad-w6d1 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d1-ckad"
