#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d6-lfcs..."
sudo ip link del veth-m1 2>/dev/null || true
sudo ip link del br-marathon 2>/dev/null || true
sudo iptables -t nat -D PREROUTING -p tcp --dport 9090 -j REDIRECT --to-ports 80 2>/dev/null || true
sudo iptables -D INPUT -p udp --dport 5353 -j DROP 2>/dev/null || true
sudo rm -f /usr/local/bin/network_health.sh /var/log/net_marathon.status
echo "[✓] Reset complete."
