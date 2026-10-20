#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d4-ckad (Blue-Green Deployment Cutover)..."
ssh controlplane '
kubectl create namespace ckad-w5d4 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_BLUE" | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: portal-blue
  namespace: ckad-w5d4
spec:
  replicas: 3
  selector:
    matchLabels:
      app: portal
      version: v1
  template:
    metadata:
      labels:
        app: portal
        version: v1
    spec:
      containers:
      - name: web
        image: nginx:1.24-alpine
---
apiVersion: v1
kind: Service
metadata:
  name: web-portal
  namespace: ckad-w5d4
spec:
  selector:
    app: portal
    version: v1
  ports:
  - port: 80
    targetPort: 80
EOF_BLUE
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d4-ckad"
