#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d5-cka (Admission Controllers & Validating Webhooks)..."
ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/enabled_admission_plugins.txt /opt/k8s/admission_rejection.log
'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d5-cka"
