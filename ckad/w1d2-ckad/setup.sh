#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d2-ckad (Editing Pods & Command / Args Overrides)..."
ssh controlplane '
kubectl create namespace ckad-w1d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run data-worker --image=busybox:1.36 -n ckad-w1d2 --command -- sleep 3600
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d2-ckad"
