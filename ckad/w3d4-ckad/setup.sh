#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d4-ckad (Init Containers & Service Dependency Gating)..."
ssh controlplane '
kubectl create namespace ckad-w3d4 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_GATED" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: webapp-gated
  namespace: ckad-w3d4
spec:
  initContainers:
  - name: check-mysql
    image: busybox:1.36
    command: ["sh", "-c", "until nc -z -w 2 mysql-backend 3306; do echo waiting for mysql; sleep 2; done"]
  containers:
  - name: web
    image: nginx:alpine
EOF_GATED
'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d4-ckad"
