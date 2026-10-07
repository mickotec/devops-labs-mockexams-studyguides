#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w1d5-lfcs (Pagers, Vim Mastery & Terminal Editing)..."
cat << 'EOF' > /var/tmp/app_legacy.conf
[server]
HOST = 0.0.0.0
PORT = 8080
# SSL_ENABLED = true
DEPRECATED_FEATURE_A = enabled
TIMEOUT = 300
DEPRECATED_FEATURE_B = active
EOF

cat << 'EOF' > /var/tmp/sample_audit.log
2026-09-14 10:00:01 [AUTH] STATUS: 200 user=alice
2026-09-14 10:00:02 [AUTH] STATUS: 401 user=guest
2026-09-14 10:00:03 [AUTH] STATUS: 200 user=bob
2026-09-14 10:00:04 [AUTH] STATUS: 500 user=alice
2026-09-14 10:00:05 [AUTH] STATUS: 200 user=admin
EOF
rm -f /var/tmp/status_summary.txt
echo "[✓] Environment ready. Review tasks with: ./lab show w1d5-lfcs"
