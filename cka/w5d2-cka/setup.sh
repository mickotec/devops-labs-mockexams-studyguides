#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d2-cka (Cluster Upgrade: Kubeadm Control Plane)..."
ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/upgrade_plan.txt
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d2-cka"
