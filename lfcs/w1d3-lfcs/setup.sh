#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d3-lfcs (Standard Linux File Permissions)..."
sudo rm -rf /srv/data/engineering /etc/profile.d/devops_umask.sh
sudo mkdir -p /srv/data/engineering/src /srv/data/engineering/docs
sudo touch /srv/data/engineering/README.md /srv/data/engineering/src/main.py /srv/data/engineering/docs/spec.txt
sudo chmod 777 /srv/data/engineering/README.md /srv/data/engineering/src/main.py
sudo chmod 700 /srv/data/engineering/src /srv/data/engineering/docs
echo "[✓] Environment ready. Review tasks with: ./lab show w1d3-lfcs"
