#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d1-cka (Manual Scheduling, Labels & Selectors)..."
ssh controlplane '
  kubectl delete namespace w3d1-sched --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d1-sched
  kubectl label node node01 disktype- 2>/dev/null || true
  kubectl label node node02 environment- 2>/dev/null || true
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  cat << "EOF" > /opt/k8s/orphan-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: orphan-task
  namespace: w3d1-sched
spec:
  containers:
  - name: sleeper
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
EOF
'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d1-cka"
