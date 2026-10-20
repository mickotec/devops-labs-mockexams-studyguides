#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d5-ckad (ReplicaSets & Deployment Scaling Strategies)..."
ssh controlplane '
kubectl create namespace ckad-w1d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w1d5 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d5-ckad"
