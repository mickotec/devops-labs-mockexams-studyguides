#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d6-ckad (Ingress Rewrite-Target & Path Regex)..."
ssh controlplane '
kubectl create namespace ckad-w6d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl create deployment api-dep --image=nginx:alpine --replicas=1 -n ckad-w6d6
kubectl expose deployment api-dep --name=service-api --port=80 --target-port=80 -n ckad-w6d6
'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d6-ckad"
