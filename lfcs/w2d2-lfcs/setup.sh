#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w2d2-lfcs (Text Processing: Grep & Regular Expressions)..."
sudo rm -f /var/tmp/auth_ips.txt /var/tmp/pam_rules.txt /var/tmp/error_count.txt
cat << 'EOF' > /var/tmp/auth_sample.log
Sep 14 10:00:01 server sshd[1234]: Failed password for invalid user admin from 192.168.1.50 port 45231 ssh2
Sep 14 10:00:05 server sshd[1235]: Failed password for root from 10.0.0.15 port 51234 ssh2
Sep 14 10:00:10 server sshd[1236]: Accepted publickey for student from 172.16.16.1 port 38291 ssh2
Sep 14 10:00:12 server sshd[1237]: authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.1.50
Sep 14 10:00:15 server sshd[1238]: Failed password for root from 192.168.1.50 port 45233 ssh2
EOF
echo "[✓] Environment ready. Review tasks with: ./lab show w2d2-lfcs"
