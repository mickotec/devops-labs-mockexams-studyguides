#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w5d3-cka..."
ssh controlplane '
  kubectl uncordon node01 node02 2>/dev/null || true
  rm -f /opt/k8s/node01_drain.txt
'
echo "[✓] Reset complete."
