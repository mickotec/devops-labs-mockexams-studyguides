#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d5-cka..."
ssh controlplane '
  kubectl delete namespace w8d5-marathon --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv pv-marathon-data 2>/dev/null || true
  kubectl label node node01 zone- 2>/dev/null || true
  kubectl taint node node02 dedicated- 2>/dev/null || true
'
echo "[✓] Reset complete."
