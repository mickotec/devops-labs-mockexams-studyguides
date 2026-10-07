#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d2-lfcs (Files, Directories, Hard & Soft Links)..."
sudo rm -rf /opt/link-lab /var/tmp/removed_links.txt
sudo mkdir -p /opt/link-lab/configs /opt/link-lab/storage/v2 /opt/link-lab/backup /opt/link-lab/orphan_links
sudo bash -c 'echo "DATABASE_PORT=5432" > /opt/link-lab/storage/v2/app-v2.conf'
sudo ln -sf /nonexistent/path/app.conf /opt/link-lab/configs/active.conf
sudo ln -sf /nonexistent/old_log.txt /opt/link-lab/orphan_links/broken1.link
sudo ln -sf /opt/link-lab/storage/v2/app-v2.conf /opt/link-lab/orphan_links/valid.link
sudo ln -sf /nonexistent/legacy.sock /opt/link-lab/orphan_links/broken2.link
echo "[✓] Environment ready. Review tasks with: ./lab show w1d2-lfcs"
