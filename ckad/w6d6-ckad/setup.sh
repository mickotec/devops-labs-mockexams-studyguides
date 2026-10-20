#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d6-ckad (Week 6 Milestone: Microservices Network Security Sandbox)..."
ssh controlplane '
kubectl create namespace ckad-w6d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w6d6 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d6-ckad"
