#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w5d2-cka..."
ssh controlplane 'rm -f /opt/k8s/upgrade_plan.txt'
echo "[✓] Reset complete."
