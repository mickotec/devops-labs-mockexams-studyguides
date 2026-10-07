#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d1-lfcs (Consoles, Navigation & System Documentation)..."
sudo rm -rf /var/tmp/lfcs*
sudo rm -f /usr/local/bin/quickman
echo "[✓] Environment ready. Review tasks with: ./lab show w1d1-lfcs"
