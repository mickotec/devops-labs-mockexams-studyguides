#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d3-cka..."
ssh controlplane '
  kubectl delete namespace w8d3-json w8d3-lightning --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/node_names.txt /opt/k8s/kube_system_images.txt /opt/k8s/pod_node_mapping.txt
'
echo "[✓] Reset complete."
