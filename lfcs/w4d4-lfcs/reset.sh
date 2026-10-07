#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up w4d4-lfcs..."
sudo rm -rf /var/tmp/src-build /var/tmp/hello-c.tar.gz /usr/local/bin/hello-app /var/tmp/hello_output.txt
echo "[✓] Reset complete."
