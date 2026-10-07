#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d5-cka (Timed Mock Exam 2 & 3 Marathon)..."
ssh controlplane '
  kubectl delete namespace w8d5-marathon --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv pv-marathon-data 2>/dev/null || true
  kubectl create namespace w8d5-marathon
  kubectl label node node01 zone- 2>/dev/null || true
  kubectl taint node node02 dedicated- 2>/dev/null || true
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d5-cka"
