#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d2-cka..."
ssh controlplane '
  kubectl delete namespace w7d2-dns --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/dns_resolution.txt
'
echo "[✓] Reset complete."
