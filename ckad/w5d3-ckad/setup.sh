#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d3-ckad (Rollback Strategies & Historical Revisions)..."
ssh controlplane '
kubectl create namespace ckad-w5d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl create deployment checkout-api --image=nginx:1.24-alpine --replicas=3 -n ckad-w5d3
kubectl set image deployment/checkout-api checkout-api=nginx:bad-tag-xyz -n ckad-w5d3
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d3-ckad"
