#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d5-cka (Helm & Kustomize (2025 Updates))..."
ssh controlplane '
  kubectl delete namespace w6d5-kustomize --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w6d5-kustomize
  sudo mkdir -p /opt/k8s/kustomize/base && sudo chmod -R 777 /opt/k8s
  cat << "EOF" > /opt/k8s/kustomize/base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-server
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
EOF

  cat << "EOF" > /opt/k8s/kustomize/base/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 80
EOF
  rm -f /opt/k8s/kustomize/base/kustomization.yaml
'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d5-cka"
