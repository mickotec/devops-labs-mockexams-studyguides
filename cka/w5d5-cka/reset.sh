#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w5d5-cka..."
ssh controlplane 'rm -f /opt/k8s/certs_expiration.txt /opt/k8s/apiserver_sans.txt'
echo "[✓] Reset complete."
