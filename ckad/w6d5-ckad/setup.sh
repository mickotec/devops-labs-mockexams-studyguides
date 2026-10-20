#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d5-ckad (Ingress Networking: Host & Path Routing)..."
ssh controlplane '
kubectl create namespace ckad-w6d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl create deployment orders-dep --image=nginx:alpine --replicas=1 -n ckad-w6d5
kubectl expose deployment orders-dep --name=orders-svc --port=8080 --target-port=80 -n ckad-w6d5

kubectl create deployment catalog-dep --image=nginx:alpine --replicas=1 -n ckad-w6d5
kubectl expose deployment catalog-dep --name=catalog-svc --port=8080 --target-port=80 -n ckad-w6d5
'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d5-ckad"
