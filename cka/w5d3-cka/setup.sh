#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d3-cka (Cluster Upgrade: Worker Nodes)..."
ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/node01_drain.txt
  kubectl uncordon node01 node02 2>/dev/null || true
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d3-cka"
