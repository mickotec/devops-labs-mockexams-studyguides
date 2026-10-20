#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d5-ckad (Canary Deployment Traffic Splitting)..."
ssh controlplane '
kubectl create namespace ckad-w5d5 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_CANARY" | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: catalog-stable
  namespace: ckad-w5d5
spec:
  replicas: 4
  selector:
    matchLabels:
      app: catalog
      track: stable
  template:
    metadata:
      labels:
        app: catalog
        track: stable
    spec:
      containers:
      - name: web
        image: nginx:1.24-alpine
---
apiVersion: v1
kind: Service
metadata:
  name: catalog-svc
  namespace: ckad-w5d5
spec:
  selector:
    app: catalog
  ports:
  - port: 80
    targetPort: 80
EOF_CANARY
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d5-ckad"
