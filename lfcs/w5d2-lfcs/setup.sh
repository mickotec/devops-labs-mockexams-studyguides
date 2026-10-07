#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d2-lfcs (Groups, Sudo Privileges & Visudo)..."
sudo rm -f /etc/sudoers.d/90-sysaudit
sudo groupdel sysaudit 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show w5d2-lfcs"
