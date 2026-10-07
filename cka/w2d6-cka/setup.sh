#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d6-cka (Week 2 Speed Drills & Controller Triathlon)..."
ssh controlplane '
kubectl delete namespace triathlon-w2 --grace-period=0 --force 2>/dev/null || true
sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
rm -f /opt/k8s/clean-export.yaml
'
echo "[✓] Environment ready. Review tasks with: ./lab show w2d6-cka"
