#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w4d5-cka..."
ssh controlplane 'rm -f /opt/k8s/enabled_admission_plugins.txt /opt/k8s/admission_rejection.log'
echo "[✓] Reset complete."
