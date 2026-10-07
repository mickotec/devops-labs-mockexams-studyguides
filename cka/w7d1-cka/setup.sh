#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d1-cka (Cluster & Pod Networking Prerequisites)..."
ssh controlplane '
  kubectl delete namespace w7d1-net --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d1-net
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/cni-plugin-type.txt /opt/k8s/node-podcidrs.txt
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d1-cka"
