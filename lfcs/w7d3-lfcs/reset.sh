#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d3-lfcs..."
sudo iptables -D INPUT -p tcp --dport 8088 -j DROP 2>/dev/null || true
sudo iptables -D INPUT -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT 2>/dev/null || true
sudo rm -f /var/tmp/iptables_backup.rules
echo "[✓] Reset complete."
