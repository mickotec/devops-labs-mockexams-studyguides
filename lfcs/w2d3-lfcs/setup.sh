#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d3-lfcs (Advanced Stream Analysis: Sed & Awk Fundamentals)..."
sudo rm -f /var/tmp/regular_users.txt /var/tmp/sales_total.txt
cat << 'EOF' > /var/tmp/config_sample.ini
[server]
HOST = 0.0.0.0
PORT = 8080
DEBUG = True
TIMEOUT = 60
EOF

cat << 'EOF' > /var/tmp/sales.csv
item,price,quantity
widget,25,10
gadget,50,4
gizmo,15,20
EOF
echo "[✓] Environment ready. Review tasks with: ./lab show w2d3-lfcs"
