#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d4-lfcs (Timed Mock Exam 3 (Strict Exam Conditions))..."
sudo rm -rf /var/mock3_shared /var/tmp/suid_binaries.txt /etc/modules-load.d/dummy.conf
sudo iptables -D OUTPUT -p tcp -d 198.51.100.1 --dport 443 -j DROP 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show w8d4-lfcs"
