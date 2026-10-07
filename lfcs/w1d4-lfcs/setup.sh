#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d4-lfcs (Special Permissions: SUID, SGID & Sticky Bit)..."
sudo rm -rf /opt/campaigns /var/tmp/world_writable_audit.txt
sudo groupdel marketing 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show w1d4-lfcs"
