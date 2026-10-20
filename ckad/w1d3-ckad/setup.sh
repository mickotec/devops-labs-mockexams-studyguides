#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d3-ckad (ReplicaSets, Label Selectors & Pod Adoption)..."
ssh controlplane '
kubectl create namespace ckad-w1d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run orphan-web --image=nginx:1.24-alpine -n ckad-w1d3 -l app=frontend
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d3-ckad"
