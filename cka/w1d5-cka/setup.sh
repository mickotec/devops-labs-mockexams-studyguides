#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d5-cka (Fast Imperative CLI Mastery with Kubectl)..."
ssh controlplane '
kubectl delete namespace speed-drill --grace-period=0 --force 2>/dev/null || true
kubectl create namespace speed-drill
sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
rm -f /opt/k8s/clean-cache.yaml
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d5-cka"
