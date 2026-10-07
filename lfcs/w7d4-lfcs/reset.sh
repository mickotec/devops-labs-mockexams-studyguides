#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d4-lfcs..."
sudo rm -f /etc/sysctl.d/99-ipforward.conf /var/tmp/reverse_proxy.conf
sudo iptables -t nat -D PREROUTING -p tcp --dport 8080 -j REDIRECT --to-ports 80 2>/dev/null || true
echo "[✓] Reset complete."
