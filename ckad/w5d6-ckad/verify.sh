#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W5D6: Jobs & CronJobs in ckad-w5d6..."

COMPLETIONS=$(ssh controlplane 'kubectl get job db-indexer -n ckad-w5d6 -o jsonpath="{.status.succeeded}" 2>/dev/null || echo 0')
CRON_POLICY=$(ssh controlplane 'kubectl get cronjob log-archiver -n ckad-w5d6 -o jsonpath="{.spec.concurrencyPolicy}" 2>/dev/null || echo ""')
CRON_SCHED=$(ssh controlplane 'kubectl get cronjob log-archiver -n ckad-w5d6 -o jsonpath="{.spec.schedule}" 2>/dev/null || echo ""')

if [ "$COMPLETIONS" -eq 3 ] && [ "$CRON_POLICY" == "Forbid" ] && [[ "$CRON_SCHED" =~ "5" ]]; then
  echo -e "[0;32m[PASS] Job db-indexer completed 3/3 and CronJob log-archiver active with Forbid policy.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Job completions: $COMPLETIONS/3 | Cron Policy: '$CRON_POLICY' | Sched: '$CRON_SCHED'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi