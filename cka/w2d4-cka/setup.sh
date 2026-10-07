#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d4-cka (Namespaces & DNS Resolution Inside Clusters)..."
ssh controlplane '
kubectl delete ns frontend-ns database-ns --grace-period=0 --force 2>/dev/null || true
kubectl create ns frontend-ns
kubectl create ns database-ns
'
echo "[✓] Environment ready. Review tasks with: ./lab show w2d4-cka"
