#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d5-ckad (Kustomize Basics: Overlays, Patches & Transformers)..."
ssh controlplane '
kubectl create namespace ckad-w7d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=kustomize -n ckad-w7d5 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d5-ckad"
