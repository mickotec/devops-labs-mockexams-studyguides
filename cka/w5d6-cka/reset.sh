#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w5d6-cka..."
ssh controlplane '
  rm -f /opt/backup/milestone5-etcd.db /opt/k8s/m5_certs_audit.txt
  kubectl uncordon node02 2>/dev/null || true
'
echo "[✓] Reset complete."
