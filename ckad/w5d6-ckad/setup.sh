#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d6-ckad (Batch Jobs, CronJobs & Concurrency Policies)..."
ssh controlplane 'kubectl create namespace ckad-w5d6 --dry-run=client -o yaml | kubectl apply -f -'
echo "[✓] Environment ready. Review tasks with: ./lab show w5d6-ckad"
