#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d5-ckad (Workload Monitoring with Metrics Server (kubectl top))..."
ssh controlplane 'rm -f /tmp/top-cpu-pod.txt'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d5-ckad"
