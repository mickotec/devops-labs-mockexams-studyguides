#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W2D4: Secrets & File Modes in ckad-w2d4..."

PHASE=$(ssh controlplane 'kubectl get pod auth-consumer -n ckad-w2d4 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
CONTENT=$(ssh controlplane 'kubectl exec auth-consumer -n ckad-w2d4 -- cat /etc/api-keys/api-key 2>/dev/null || echo ""')
PERM=$(ssh controlplane 'kubectl exec auth-consumer -n ckad-w2d4 -- stat -c "%a" /etc/api-keys/api-key 2>/dev/null || echo ""')

if [ "$PHASE" == "Running" ] && [ "$CONTENT" == "secret-alpha-9988" ] && [ "$PERM" == "400" ]; then
  echo -e "[0;32m[PASS] Secret volume mounted with permission 0400 and valid credentials.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: $PHASE | Content: '$CONTENT' | Mode: '$PERM' (expected 400).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi