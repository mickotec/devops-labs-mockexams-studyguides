#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d2-lfcs (Network Bonding & Bridging)..."
sudo ip link del veth-host 2>/dev/null || true
sudo ip link del br0 2>/dev/null || true
echo "[✓] Environment ready. Review tasks with: ./lab show w7d2-lfcs"
