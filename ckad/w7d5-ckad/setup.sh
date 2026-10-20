#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d5-ckad (StorageClasses & Delayed Volume Binding)..."
ssh controlplane '
kubectl create namespace ckad-w7d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl delete sc delayed-storage --ignore-not-found
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d5-ckad"
