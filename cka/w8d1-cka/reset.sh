#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w8d1-cka..."
ssh controlplane '
  kubectl delete namespace w8d1-trouble --grace-period=0 --force 2>/dev/null || true
  sudo rm -f /etc/kubernetes/manifests/broken-watchdog.yaml
  POD_ID=$(sudo crictl pods -q --name broken-watchdog-controlplane 2>/dev/null || true)
  [ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
  kubectl delete pod broken-watchdog-controlplane --force --grace-period=0 2>/dev/null || true
  rm -f /opt/k8s/apiserver_log_sample.txt
'
echo "[✓] Reset complete."
