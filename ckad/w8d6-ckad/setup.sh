#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d6-ckad (CKAD killer.sh Mock Exam 2 (Timed Simulation))..."
ssh controlplane '
kubectl create namespace ckad-w8d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=mock-ckad-2 -n ckad-w8d6 --dry-run=client -o yaml | kubectl apply -f -
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d6-ckad"
