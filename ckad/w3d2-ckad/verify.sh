#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W3D2: Adapter Pattern in ckad-w3d2..."

READY=$(ssh controlplane 'kubectl get pod metric-adapter-pod -n ckad-w3d2 -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null | grep -o "true" | wc -l || echo 0')
PROM=$(ssh controlplane 'kubectl exec metric-adapter-pod -c adapter -n ckad-w3d2 -- cat /var/metrics/metrics.prom 2>/dev/null || echo ""')

if [ "$READY" -eq 2 ] && [[ "$PROM" =~ "node_cpu_usage" ]]; then
  echo -e "[0;32m[PASS] Adapter container running and successfully normalized metrics output.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Ready containers: $READY/2 | Prometheus metric: '$PROM'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi