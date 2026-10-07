#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d2-cka (Service Networking & CoreDNS Deep Dive)..."
ssh controlplane '
  kubectl delete namespace w7d2-dns --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d2-dns
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/dns_resolution.txt
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d2-cka"
