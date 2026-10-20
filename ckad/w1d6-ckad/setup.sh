#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d6-ckad (Imperative Commands & JSONPath Output Mastery)..."
ssh controlplane '
kubectl create namespace ckad-w1d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run target-alpha --image=nginx:alpine -n ckad-w1d6
kubectl wait --for=condition=Ready pod/target-alpha -n ckad-w1d6 --timeout=30s 2>/dev/null || true
rm -f /tmp/alpha-ip.txt /tmp/explain.txt
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d6-ckad"
