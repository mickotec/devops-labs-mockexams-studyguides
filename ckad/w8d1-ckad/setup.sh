#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d1-ckad (Kubeconfig Architecture & Multi-Cluster Contexts)..."
ssh controlplane '
kubectl create namespace ckad-w8d1 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=kubeconfig -n ckad-w8d1 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d1-ckad"
