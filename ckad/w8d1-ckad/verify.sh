#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W8D1: Kubeconfig Context in /tmp/custom-kubeconfig..."

CURRENT_CTX=$(ssh controlplane 'kubectl --kubeconfig=/tmp/custom-kubeconfig config current-context 2>/dev/null || echo ""')
NS=$(ssh controlplane 'kubectl --kubeconfig=/tmp/custom-kubeconfig config view --minify -o jsonpath="{.contexts[0].context.namespace}" 2>/dev/null || echo ""')

if [ "$CURRENT_CTX" == "developer-ctx" ] && [ "$NS" == "ckad-dev-ns" ]; then
  echo -e "[0;32m[PASS] custom-kubeconfig active context is developer-ctx with default namespace ckad-dev-ns.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] current-context: '$CURRENT_CTX' (expected developer-ctx) | default ns: '$NS'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi