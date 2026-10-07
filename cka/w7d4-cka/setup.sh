#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d4-cka (Gateway API (2025 Updates))..."
ssh controlplane '
  kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.1.0/standard-install.yaml 2>/dev/null || true
  kubectl delete namespace w7d4-gw --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d4-gw
  cat << "EOF" | kubectl apply -f - 2>/dev/null || true
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: cluster-gateway-class
spec:
  controllerName: example.com/gateway-controller
EOF
  kubectl create deployment api-service -n w7d4-gw --image=nginx:alpine --port=8080
  kubectl expose deployment api-service -n w7d4-gw --port=8080
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d4-cka"
