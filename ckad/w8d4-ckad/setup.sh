#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d4-ckad (Custom Resource Definitions (CRDs) & API Extensions)..."
ssh controlplane '
kubectl create namespace ckad-w8d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=crd -n ckad-w8d4 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d4-ckad"
