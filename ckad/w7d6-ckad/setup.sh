#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d6-ckad (StatefulSets & VolumeClaimTemplates)..."
ssh controlplane 'kubectl create namespace ckad-w7d6 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d6-ckad"
