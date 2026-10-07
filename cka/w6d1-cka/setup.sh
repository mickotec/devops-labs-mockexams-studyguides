#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w6d1-cka (Certificates API & KubeConfig Management)..."
ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  cd /opt/k8s
  openssl genrsa -out developer-bob.key 2048 2>/dev/null
  openssl req -new -key developer-bob.key -out developer-bob.csr -subj "/CN=developer-bob/O=developers" 2>/dev/null
  kubectl delete csr developer-bob-csr 2>/dev/null || true
  rm -f developer-bob.crt bob.kubeconfig
'
echo "[✓] Environment ready. Review tasks with: ./lab show w6d1-cka"
