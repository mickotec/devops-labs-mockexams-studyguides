#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d6-lfcs (Week 1 Consolidation & Permission Security Triathlon)..."
sudo rm -rf /srv/secure_vault /var/tmp/suid_audit.txt /var/backups/vault_initial.tar.gz /opt/binaries
sudo mkdir -p /opt/binaries /var/backups
sudo touch /opt/binaries/tool_suid /opt/binaries/tool_normal
sudo chmod 4755 /opt/binaries/tool_suid
sudo chmod 755 /opt/binaries/tool_normal
sudo groupdel sysadmins 2>/dev/null || true
sudo groupdel contractors 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show w1d6-lfcs"
