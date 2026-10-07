#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w7d2-lfcs..."
sudo ip link del veth-host 2>/dev/null || true
sudo ip link del br0 2>/dev/null || true
echo "[✓] Reset complete."
