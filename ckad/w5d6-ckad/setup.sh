#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d6-ckad (Week 5 Milestone: Comprehensive Health & Triage Suite)..."
ssh controlplane '
kubectl create namespace ckad-w5d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w5d6 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d6-ckad"
