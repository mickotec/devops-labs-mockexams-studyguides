#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d4-lfcs (I/O Redirection & Stream Multiplexing)..."
sudo rm -f /var/tmp/stdout.log /var/tmp/stderr.log /var/tmp/process_dump.txt /var/tmp/process_count.txt /var/tmp/gen_health.sh /var/tmp/health.report
echo "[✓] Environment ready. Review tasks with: ./lab show w2d4-lfcs"
