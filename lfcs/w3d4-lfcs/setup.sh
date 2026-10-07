#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d4-lfcs (Process Diagnostics & Signal Management)..."
sudo killall -9 rogue-sim batch-calc 2>/dev/null || true
# Start rogue process
nohup bash -c 'exec -a rogue-sim sleep 3600' >/dev/null 2>&1 &
# Start batch calc
nohup bash -c 'exec -a batch-calc sleep 3600' >/dev/null 2>&1 &
sudo rm -f /var/tmp/process_report.txt
echo "[✓] Environment ready. Review tasks with: ./lab show w3d4-lfcs"
