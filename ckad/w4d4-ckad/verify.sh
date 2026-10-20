#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W4D4: Previous Logs Extraction in ckad-w4d4..."

LOG_CONTENT=$(ssh controlplane 'cat /tmp/fatal-sync.log 2>/dev/null || echo ""')
if [[ "$LOG_CONTENT" =~ "FATAL" ]]; then
  echo -e "[0;32m[PASS] Fatal crash log correctly captured in /tmp/fatal-sync.log.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] /tmp/fatal-sync.log missing or does not contain FATAL log.[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi