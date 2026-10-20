#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d6-ckad (Imperative Commands & JSONPath Output Mastery)..."
ssh controlplane '
kubectl create namespace ckad-w1d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run target-alpha --image=nginx:alpine -n ckad-w1d6
rm -f /tmp/alpha-ip.txt /tmp/explain.txt
'
echo "[✓] Environment ready. Review tasks with: ./lab show w1d6-ckad"
