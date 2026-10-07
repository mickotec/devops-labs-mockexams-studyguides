#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d6-cka..."
ssh controlplane '
  kubectl delete namespace w3-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl label node node02 hardware- 2>/dev/null || true
  kubectl taint node node01 dedicated- 2>/dev/null || true
'
echo "[✓] Reset complete."
