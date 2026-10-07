#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d1-lfcs (Journald & System Log File Analysis)..."
sudo rm -f /var/tmp/system_errors.log /var/tmp/ssh_service.log /var/tmp/journal_usage.txt
echo "[✓] Environment ready. Review tasks with: ./lab show w4d1-lfcs"
