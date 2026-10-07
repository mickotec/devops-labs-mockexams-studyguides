#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d3-lfcs (Package Managers (APT, DNF/YUM & RPM))..."
sudo apt-mark unhold tar 2>/dev/null || true
sudo rm -rf /var/tmp/tar_package.txt /var/tmp/pkg_cache
mkdir -p /var/tmp/pkg_cache
echo "[✓] Environment ready. Review tasks with: ./lab show w4d3-lfcs"
