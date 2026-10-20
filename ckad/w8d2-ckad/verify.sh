#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W8D2: RBAC in ckad-w8d2..."

CAN_CREATE=$(ssh controlplane 'kubectl auth can-i create pods -n ckad-w8d2 --as=system:serviceaccount:ckad-w8d2:app-operator 2>/dev/null || true')
CAN_DEPLOY=$(ssh controlplane 'kubectl auth can-i create deployments -n ckad-w8d2 --as=system:serviceaccount:ckad-w8d2:app-operator 2>/dev/null || true')

if [ "$CAN_CREATE" == "yes" ] && [ "$CAN_DEPLOY" == "no" ]; then
  echo -e "[0;32m[PASS] ServiceAccount app-operator has exact pod-admin permissions in ckad-w8d2.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] can-i create pods: '$CAN_CREATE' (expected yes) | can-i create deployments: '$CAN_DEPLOY' (expected no)[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi