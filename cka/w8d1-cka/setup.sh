#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d1-cka (Troubleshooting: Control Plane & Applications)..."
ssh controlplane '
  kubectl delete namespace w8d1-trouble --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d1-trouble
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/apiserver_log_sample.txt

  # Task 1 broken static pod
  sudo tee /etc/kubernetes/manifests/broken-watchdog.yaml > /dev/null << "EOF"
apiVersion: v1
kind: Pod
metadata:
  name: broken-watchdog
spec:
  containers:
  - name: watchdog
    image: busybox:invalid-v999
    command: ["sh", "-c", "sleep 3600"]
EOF

  # Task 2 crashing app pod
  cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: db-connector
  namespace: w8d1-trouble
spec:
  containers:
  - name: connector
    image: busybox:1.36
    command: ["sh", "-c", "if [ -z \"$DB_HOST\" ]; then exit 1; else sleep 3600; fi"]
EOF
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d1-cka"
