#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d5-cka (Kubectl Explain & Declarative Workflow)..."
ssh controlplane '
kubectl delete namespace security-lab --grace-period=0 --force 2>/dev/null || true
kubectl create namespace security-lab
sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
rm -f /opt/k8s/schema-paths.txt /opt/k8s/secure-pod.yaml
'
echo "[✓] Environment ready. Review tasks with: ./lab show w2d5-cka"
