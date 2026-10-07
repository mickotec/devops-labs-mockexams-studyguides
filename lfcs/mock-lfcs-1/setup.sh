#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up mock-lfcs-1 (LFCS Full-Scale Timed Mock Exam 1)..."
sudo rm -rf /var/tmp/mock-lfcs-1 /etc/sysctl.d/99-swappiness.conf /etc/systemd/system/mock-monitor.service /etc/ssh/sshd_config.d/99-hardening.conf
sudo mkdir -p /var/tmp/mock-lfcs-1/shared && sudo chown -R student:student /var/tmp/mock-lfcs-1 && sudo chmod -R 777 /var/tmp/mock-lfcs-1
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /tmp/key.pem -out /var/tmp/mock-lfcs-1/exam.crt -subj "/CN=exam.local/O=MockCorp" 2>/dev/null || true
rm -f /tmp/key.pem
# Create sample file for Q3
dd if=/dev/urandom of=/var/tmp/mock-lfcs-1/sample_large.bin bs=1K count=150 2>/dev/null || true
# Ensure users/groups clean
sudo userdel -r devops 2>/dev/null || true
sudo userdel -r tester 2>/dev/null || true
sudo groupdel infrateam 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show mock-lfcs-1"
