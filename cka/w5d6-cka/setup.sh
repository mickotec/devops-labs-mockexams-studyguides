#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d6-cka (Full Disaster Recovery & Upgrade Drill)..."
ssh controlplane '
  mkdir -p /opt/backup /opt/k8s
  rm -f /opt/backup/milestone5-etcd.db /opt/k8s/m5_certs_audit.txt
  kubectl uncordon node02 2>/dev/null || true
'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d6-cka"
