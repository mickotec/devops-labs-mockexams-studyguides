#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d1-cka (ReplicaSets & Self-Healing Controllers)..."
ssh controlplane '
kubectl delete namespace core --grace-period=0 --force 2>/dev/null || true
kubectl create namespace core
sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
cat << "EOF" > /opt/k8s/replicaset-broken.yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: web-replicas
  namespace: core
spec:
  replicas: 4
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: frontend
        tier: web
    spec:
      containers:
      - name: nginx
        image: nginx:1.25-alpine
EOF
'
echo "[✓] Environment ready. Review tasks with: ./lab show w2d1-cka"
