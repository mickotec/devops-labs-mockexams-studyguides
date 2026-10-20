#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d5-ckad (Namespaces & Cross-Namespace DNS Communication)..."
ssh controlplane '
kubectl create namespace ckad-w1d5-backend --dry-run=client -o yaml | kubectl apply -f -
kubectl create namespace ckad-w1d5-frontend --dry-run=client -o yaml | kubectl apply -f -

kubectl run redis-pod --image=redis:alpine -n ckad-w1d5-backend -l app=redis --restart=Always
kubectl expose pod redis-pod -n ckad-w1d5-backend --name=db-service --port=6379 --target-port=6379
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d5-ckad"
