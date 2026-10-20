#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d6-ckad (Week 4 Milestone: Resilient Canary & Scheduled Jobs)..."
ssh controlplane '
kubectl create namespace ckad-w4d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w4d6 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d6-ckad"
