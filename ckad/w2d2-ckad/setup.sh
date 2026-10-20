#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d2-ckad (ConfigMaps from Literals, Files & Env Injection)..."
ssh controlplane '
kubectl create namespace ckad-w2d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=alpine:3.19 -n ckad-w2d2 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w2d2-ckad"
