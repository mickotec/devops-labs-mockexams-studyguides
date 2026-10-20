#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d4-ckad (Helm Fundamentals: Repos, Releases & Values Overrides)..."
ssh controlplane '
kubectl create namespace ckad-w7d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=helm -n ckad-w7d4 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d4-ckad"
