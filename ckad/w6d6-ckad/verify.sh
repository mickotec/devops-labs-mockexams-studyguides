#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W6D6: Ingress Rewrite-Target in ckad-w6d6..."

ANNO=$(ssh controlplane 'kubectl get ingress api-rewrite-ingress -n ckad-w6d6 -o jsonpath="{.metadata.annotations.nginx\.ingress\.kubernetes\.io/rewrite-target}" 2>/dev/null || echo ""')
PATH_DEF=$(ssh controlplane 'kubectl get ingress api-rewrite-ingress -n ckad-w6d6 -o jsonpath="{.spec.rules[0].http.paths[0].path}" 2>/dev/null || echo ""')

if [ "$ANNO" == "/$2" ] && [[ "$PATH_DEF" =~ "/api" ]]; then
  echo -e "[0;32m[PASS] api-rewrite-ingress configured with rewrite-target: /$2 and regex path.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Annotation: '$ANNO' (expected /$2) | Path: '$PATH_DEF'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi