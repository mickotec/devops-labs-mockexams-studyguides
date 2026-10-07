#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d3-cka (Pod Internals & YAML Architecture)..."
ssh controlplane '
kubectl delete namespace fintech --grace-period=0 --force 2>/dev/null || true
sudo mkdir -p /opt/k8s-manifests && sudo chmod 777 /opt/k8s-manifests
cat << "EOF" > /opt/k8s-manifests/broken-app.yaml
apiVersion: v1
kind: Pod
metadata:
name: transaction-processor
namespace: fintech
spec:
 containers:
 - name: processor
 image: nginx:1.25-alpine
 env:
 - MAX_WORKERS: 8
 - CACHE_DIR: /tmp/cache
 ports:
 - 8080
 - 9090
 resources:
  limits:
   memory: 128MB
   cpu: 200M
 readinessProbe:
   httpGet:
     path: /
     port: 80
   initialDelay: 5
EOF
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d3-cka"
