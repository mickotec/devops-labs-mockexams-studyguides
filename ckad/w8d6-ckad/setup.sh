#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d6-ckad (Kustomize: Overlays, Transformers & Patches)..."
ssh controlplane '
kubectl create namespace ckad-w8d6 --dry-run=client -o yaml | kubectl apply -f -
rm -rf /tmp/kustomize-store
mkdir -p /tmp/kustomize-store/base /tmp/kustomize-store/overlays/prod
cat << "EOF_BASE" > /tmp/kustomize-store/base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: nginx
        image: nginx:1.24-alpine
EOF_BASE

cat << "EOF_KUST" > /tmp/kustomize-store/base/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- deployment.yaml
EOF_KUST
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d6-ckad"
