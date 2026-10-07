#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d6-cka..."
ssh controlplane '
  kubectl delete namespace w8d6-benchmark --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/etcd-backup.db /tmp/bench.key /tmp/bench.crt
'
echo "[✓] Reset complete."
