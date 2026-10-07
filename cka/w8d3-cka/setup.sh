#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d3-cka (JSONPath Queries & Lightning Labs 1 & 2)..."
ssh controlplane '
  kubectl delete namespace w8d3-json w8d3-lightning --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d3-json
  kubectl create namespace w8d3-lightning
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/node_names.txt /opt/k8s/kube_system_images.txt /opt/k8s/pod_node_mapping.txt
  kubectl run pod-alpha -n w8d3-json --image=nginx:alpine
  kubectl run pod-beta -n w8d3-json --image=nginx:alpine
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d3-cka"
