#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W6D3: Default Deny NetworkPolicy in ckad-w6d3..."

TYPES=$(ssh controlplane 'kubectl get netpol default-deny-ingress -n ckad-w6d3 -o jsonpath="{.spec.policyTypes[*]}" 2>/dev/null || echo ""')
RULES=$(ssh controlplane 'kubectl get netpol default-deny-ingress -n ckad-w6d3 -o jsonpath="{.spec.ingress}" 2>/dev/null || echo "NONE"')

if [[ "$TYPES" =~ "Ingress" ]] && [ "$RULES" == "NONE" -o "$RULES" == "[]" ]; then
  echo -e "[0;32m[PASS] default-deny-ingress NetworkPolicy active with empty ingress rule (default-deny).[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] policyTypes: '$TYPES' | ingress rules: '$RULES'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi