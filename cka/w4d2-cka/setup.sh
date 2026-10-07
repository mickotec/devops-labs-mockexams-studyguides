#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d2-cka (ConfigMaps & Application Configuration)..."
ssh controlplane '
  kubectl delete namespace w4d2-config --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4d2-config
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  cat << "EOF" > /opt/k8s/settings.json
{
  "theme": "dark",
  "refreshInterval": 30
}
EOF
'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d2-cka"
