#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w4d3-lfcs..."
sudo apt-mark unhold tar 2>/dev/null || true
sudo rm -rf /var/tmp/tar_package.txt /var/tmp/pkg_cache
echo "[✓] Reset complete."
