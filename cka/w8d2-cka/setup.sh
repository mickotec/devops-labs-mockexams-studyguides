#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d2-cka (Troubleshooting: Worker Nodes & Network Failure)..."
ssh node02 'sudo systemctl stop kubelet'
ssh controlplane '
  kubectl delete namespace w8d2-trouble --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d2-trouble
  kubectl taint node node02 trouble=unreachable:NoSchedule --overwrite 2>/dev/null || true
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d2-cka"
