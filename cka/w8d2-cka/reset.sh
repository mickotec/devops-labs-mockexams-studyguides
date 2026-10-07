#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d2-cka..."
ssh node02 'sudo systemctl enable --now kubelet 2>/dev/null || true'
ssh controlplane '
  kubectl taint node node02 trouble- 2>/dev/null || true
  kubectl delete namespace w8d2-trouble --grace-period=0 --force 2>/dev/null || true
'
echo "[✓] Reset complete."
