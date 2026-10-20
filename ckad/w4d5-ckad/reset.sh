#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w4d5-ckad..."
ssh controlplane 'rm -f /tmp/top-cpu-pod.txt'
echo "[✓] Reset complete."
