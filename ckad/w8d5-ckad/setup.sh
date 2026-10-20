#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d5-ckad (Helm Package Management & Value Overrides)..."
ssh controlplane '
kubectl create namespace ckad-w8d5 --dry-run=client -o yaml | kubectl apply -f -
rm -rf /tmp/sample-chart
mkdir -p /tmp/sample-chart/templates
cat << "EOF_CHART" > /tmp/sample-chart/Chart.yaml
apiVersion: v2
name: sample-chart
version: 0.1.0
EOF_CHART

cat << "EOF_VALS" > /tmp/sample-chart/values.yaml
replicaCount: 1
image: nginx:alpine
EOF_VALS

cat << "EOF_DEP" > /tmp/sample-chart/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app: {{ .Release.Name }}
    spec:
      containers:
      - name: nginx
        image: {{ .Values.image }}
EOF_DEP
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d5-ckad"
