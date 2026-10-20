#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d1-ckad (Labels, Set-Based Selectors & Annotations)..."
ssh controlplane '
kubectl create namespace ckad-w5d1 --dry-run=client -o yaml | kubectl apply -f -
rm -f /tmp/matched-pods.txt

kubectl run pod-1 -n ckad-w5d1 --image=nginx:alpine -l tier=backend,env=prod
kubectl run pod-2 -n ckad-w5d1 --image=nginx:alpine -l tier=cache,env=prod
kubectl run pod-3 -n ckad-w5d1 --image=nginx:alpine -l tier=frontend,env=prod
kubectl run pod-4 -n ckad-w5d1 --image=nginx:alpine -l tier=backend,env=dev
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d1-ckad"
