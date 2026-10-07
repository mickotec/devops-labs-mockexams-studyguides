#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d4-cka (Timed Mock Exam 1 & Step-by-Step Review)..."
ssh controlplane '
  kubectl delete namespace w8d4-exam --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d4-exam
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d4-cka"
