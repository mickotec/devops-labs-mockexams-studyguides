#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d3-ckad (Imperative Pod & Deployment CLI Mastery)..."
ssh controlplane '
kubectl create namespace ckad-w1d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w1d3 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d3-ckad"
