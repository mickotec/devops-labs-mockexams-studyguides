#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d3-cka (Ingress Controllers & Routing Rules)..."
ssh controlplane '
  kubectl delete namespace w7d3-ingress --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d3-ingress
  kubectl create deployment catalog -n w7d3-ingress --image=nginx:alpine --port=80
  kubectl expose deployment catalog -n w7d3-ingress --name=catalog-svc --port=80
  kubectl create deployment orders -n w7d3-ingress --image=httpd:alpine --port=80
  kubectl expose deployment orders -n w7d3-ingress --name=orders-svc --port=80
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d3-cka"
