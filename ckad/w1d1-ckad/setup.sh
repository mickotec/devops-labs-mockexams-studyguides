#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d1-ckad (Pod Architecture & Multi-Container Pod Creation)..."
ssh controlplane '
kubectl create namespace ckad-w1d1 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_BROKEN" > /tmp/webapp-core.yaml
apiVersion: v1
kind: Pod
metadata:
  name: webapp-core
  namespace: ckad-w1d1
spec:
  volumes:
  - name: shared-logs
    emptyDir: {}
  containers:
  - name: web-app
    image: nginx:1.24-alpine
    ports:
    - containerPort: 80
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log/app
  - name: log-shipper
    image: busybox:1.36
    command: ["sh", "-c", "while true; do date >> /var/log/app/heartbeat.log; sleep 2; done"]
    volumeMounts:
    - name: wrong-vol-name
      mountPath: /var/log/app
EOF_BROKEN
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d1-ckad"
