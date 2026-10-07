#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d1-lfcs (File Searching with Find and Locate)..."
sudo rm -f /var/tmp/large_logs.txt /var/tmp/recent_configs.txt /var/tmp/systemd_confs.txt
echo "[✓] Environment ready. Review tasks with: ./lab show w2d1-lfcs"
