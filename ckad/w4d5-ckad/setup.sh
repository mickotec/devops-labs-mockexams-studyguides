#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d5-ckad (CronJobs: Schedule Syntax & Concurrency Policies)..."
ssh controlplane '
kubectl create namespace ckad-w4d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w4d5 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d5-ckad"
