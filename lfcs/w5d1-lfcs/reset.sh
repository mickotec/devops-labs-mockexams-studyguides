#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w5d1-lfcs..."
sudo userdel -r devops_user 2>/dev/null || true
sudo groupdel devops_user 2>/dev/null || true
sudo userdel -r test_lock_user 2>/dev/null || true
echo "[✓] Reset complete."
