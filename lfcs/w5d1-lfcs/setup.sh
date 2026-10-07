#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w5d1-lfcs (Local User Management & /etc/passwd)..."
sudo userdel -r devops_user 2>/dev/null || true
sudo groupdel devops_user 2>/dev/null || true
sudo userdel -r test_lock_user 2>/dev/null || true
sudo useradd -m -s /bin/bash test_lock_user
echo "test_lock_user:P@ssword123" | sudo chpasswd
echo "[✓] Environment ready. Review tasks with: ./lab show w5d1-lfcs"
