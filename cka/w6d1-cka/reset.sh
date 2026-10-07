#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w6d1-cka..."
ssh controlplane '
  kubectl delete csr developer-bob-csr 2>/dev/null || true
  rm -rf /opt/k8s/developer-bob.* /opt/k8s/bob.kubeconfig
'
echo "[✓] Reset complete."
