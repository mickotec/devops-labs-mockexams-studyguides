#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w3d6-lfcs..."
sudo systemctl stop cache-cleaner.timer payment-bridge.service 2>/dev/null || true
sudo systemctl disable cache-cleaner.timer payment-bridge.service 2>/dev/null || true
sudo rm -f /etc/systemd/system/cache-cleaner.* /etc/systemd/system/payment-bridge.service /usr/local/bin/payment-bridge.sh /etc/security/limits.d/50-worker.conf
sudo rm -rf /var/tmp/cache
sudo systemctl daemon-reload
echo "[✓] Reset complete."
