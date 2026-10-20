#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d4-ckad (Batch Jobs: Completions, Parallelism & Retries)..."
ssh controlplane '
kubectl create namespace ckad-w4d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w4d4 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d4-ckad"
