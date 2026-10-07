#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d4-lfcs (NAT, Port Redirection & Reverse Proxies)..."
sudo rm -f /etc/sysctl.d/99-ipforward.conf /var/tmp/reverse_proxy.conf
sudo sysctl -w net.ipv4.ip_forward=0 >/dev/null 2>&1 || true
sudo iptables -t nat -D PREROUTING -p tcp --dport 8080 -j REDIRECT --to-ports 80 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show w7d4-lfcs"
