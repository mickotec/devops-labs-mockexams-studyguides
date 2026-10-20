#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d2-ckad (Readiness Probes & Service Traffic Gating)..."
ssh controlplane '
kubectl create namespace ckad-w5d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w5d2 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d2-ckad"
