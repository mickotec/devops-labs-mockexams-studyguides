#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w1d6-lfcs..."
sudo rm -rf /srv/secure_vault /var/tmp/suid_audit.txt /var/backups/vault_initial.tar.gz /opt/binaries
sudo groupdel sysadmins 2>/dev/null || true
sudo groupdel contractors 2>/dev/null || true
echo "[✓] Reset complete."
