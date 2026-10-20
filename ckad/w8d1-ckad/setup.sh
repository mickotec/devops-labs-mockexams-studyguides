#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d1-ckad (Kubeconfig Files & Context Management)..."
ssh controlplane '
cp ~/.kube/config /tmp/custom-kubeconfig 2>/dev/null || cp /etc/kubernetes/admin.conf /tmp/custom-kubeconfig
kubectl create namespace ckad-dev-ns --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d1-ckad"
