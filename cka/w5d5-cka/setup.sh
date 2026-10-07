#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d5-cka (TLS Basics & PKI in Kubernetes)..."
ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/certs_expiration.txt /opt/k8s/apiserver_sans.txt
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d5-cka"
