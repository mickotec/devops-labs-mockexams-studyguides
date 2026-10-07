#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d1-cka..."
ssh controlplane '
  kubectl delete namespace w7d1-net --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/cni-plugin-type.txt /opt/k8s/node-podcidrs.txt
'
echo "[✓] Reset complete."
