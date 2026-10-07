#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d3-cka (Services: ClusterIP, NodePort & LoadBalancer)..."
ssh controlplane '
kubectl delete namespace prod --grace-period=0 --force 2>/dev/null || true
kubectl create namespace prod
kubectl run backend-api -n prod --image=nginx:alpine --labels=app=api
'
echo "[✓] Environment ready. Review tasks with: ./lab show w2d3-cka"
