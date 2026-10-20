#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d3-ckad (Multi-Container Pods: Ambassador Pattern)..."
ssh controlplane '
kubectl create namespace ckad-w3d3-infra --dry-run=client -o yaml | kubectl apply -f -
kubectl create namespace ckad-w3d3-apps --dry-run=client -o yaml | kubectl apply -f -

kubectl run redis-backend --image=redis:alpine -n ckad-w3d3-infra -l app=redis
kubectl expose pod redis-backend -n ckad-w3d3-infra --name=redis-svc --port=6379 --target-port=6379
'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d3-ckad"
