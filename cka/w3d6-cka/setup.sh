#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d6-cka (Week 3 Scheduling Troubleshooting Matrix)..."
ssh controlplane '
  kubectl delete namespace w3-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3-milestone
  kubectl label node node02 hardware- 2>/dev/null || true
  kubectl taint node node01 dedicated=web:NoSchedule --overwrite 2>/dev/null || true

  # Pod 1: Bad selector
  cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: stuck-selector
  namespace: w3-milestone
spec:
  nodeSelector:
    hardware: gpu
  containers:
  - name: nginx
    image: nginx:alpine
EOF

  # Pod 2: Taint mismatch
  cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: stuck-taint
  namespace: w3-milestone
spec:
  nodeSelector:
    kubernetes.io/hostname: node01
  containers:
  - name: nginx
    image: nginx:alpine
EOF

  # Pod 3: DaemonSet without controlplane toleration
  cat << "EOF" | kubectl apply -f -
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: infra-agent
  namespace: w3-milestone
spec:
  selector:
    matchLabels:
      app: infra-agent
  template:
    metadata:
      labels:
        app: infra-agent
    spec:
      containers:
      - name: agent
        image: nginx:alpine
EOF
'
echo "[✓] Environment ready. Review tasks with: ./lab show w3d6-cka"
