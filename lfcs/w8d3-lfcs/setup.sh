#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d3-lfcs (Timed Mock Exam 2 (Strict Exam Conditions))..."
sudo swapoff /swapfile_mock2 2>/dev/null || true
sudo rm -f /swapfile_mock2 /var/tmp/etc_configs.tar.gz /var/tmp/auth_summary.txt
pkill -f "sleep 7200" 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show w8d3-lfcs"
