#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d5-ckad (CKAD killer.sh Mock Exam 1 (Timed Simulation))..."
ssh controlplane '
kubectl create namespace ckad-w8d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=mock-ckad-1 -n ckad-w8d5 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d5-ckad"
