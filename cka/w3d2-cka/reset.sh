#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d2-cka..."
ssh controlplane '
  kubectl delete namespace w3d2-affinity --grace-period=0 --force 2>/dev/null || true
  kubectl taint node node01 workload- 2>/dev/null || true
'
echo "[✓] Reset complete."
