#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d4-ckad (Multi-Container Logging & Crash Log Extraction)..."
ssh controlplane '
kubectl create namespace ckad-w4d4 --dry-run=client -o yaml | kubectl apply -f -
rm -f /tmp/fatal-sync.log
cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: microservice-pod
  namespace: ckad-w4d4
spec:
  containers:
  - name: web
    image: nginx:alpine
  - name: database-sync
    image: busybox:1.36
    command: ["sh", "-c"]
    args:
    - if [ ! -f /tmp/crashed ]; then
        touch /tmp/crashed;
        echo "[FATAL] Connection timeout to db host" >&2;
        exit 1;
      else
        echo "Running healthy";
        sleep 3600;
      fi
EOF_POD
'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d4-ckad"
