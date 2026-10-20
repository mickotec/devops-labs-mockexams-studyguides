#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d6-ckad (Week 7 Milestone: Declarative GitOps Kustomize Stack)..."
ssh controlplane '
kubectl create namespace ckad-w7d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w7d6 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d6-ckad"
