#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d1-cka..."
ssh controlplane '
  kubectl delete namespace w3d1-sched --grace-period=0 --force 2>/dev/null || true
  kubectl label node node01 disktype- 2>/dev/null || true
  kubectl label node node02 environment- 2>/dev/null || true
  rm -rf /opt/k8s/orphan-pod.yaml
'
echo "[✓] Reset complete."
