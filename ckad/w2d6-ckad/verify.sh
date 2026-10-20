#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W2D6: ServiceAccounts & Token Control in ckad-w2d6..."

PHASE=$(ssh controlplane 'kubectl get pod isolated-agent -n ckad-w2d6 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
SA=$(ssh controlplane 'kubectl get pod isolated-agent -n ckad-w2d6 -o jsonpath="{.spec.serviceAccountName}" 2>/dev/null || echo "none"')
AUTOMOUNT=$(ssh controlplane 'kubectl get pod isolated-agent -n ckad-w2d6 -o jsonpath="{.spec.automountServiceAccountToken}" 2>/dev/null || echo "true"')
TOKEN_CHECK=$(ssh controlplane 'kubectl exec isolated-agent -n ckad-w2d6 -- ls /var/run/secrets/kubernetes.io/serviceaccount 2>&1 || echo "NOT_FOUND"')

if [ "$PHASE" == "Running" ] && [ "$SA" == "build-deployer" ] && [ "$AUTOMOUNT" == "false" ] && [[ "$TOKEN_CHECK" =~ "NOT_FOUND" ]]; then
  echo -e "[0;32m[PASS] Pod isolated-agent assigned build-deployer with automountServiceAccountToken disabled.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Phase: $PHASE, SA: $SA (expected build-deployer), Automount: $AUTOMOUNT (expected false).[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi