#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W5D1: Labels & Selectors in ckad-w5d1..."

MATCHED=$(ssh controlplane 'cat /tmp/matched-pods.txt 2>/dev/null || echo ""')
ANNO_1=$(ssh controlplane 'kubectl get pod pod-1 -n ckad-w5d1 -o jsonpath="{.metadata.annotations.release\.version}" 2>/dev/null || echo ""')
ANNO_2=$(ssh controlplane 'kubectl get pod pod-2 -n ckad-w5d1 -o jsonpath="{.metadata.annotations.release\.version}" 2>/dev/null || echo ""')

if [[ "$MATCHED" =~ "pod-1" ]] && [[ "$MATCHED" =~ "pod-2" ]] && ! [[ "$MATCHED" =~ "pod-3" ]] && ! [[ "$MATCHED" =~ "pod-4" ]] && [ "$ANNO_1" == "v3.2" ] && [ "$ANNO_2" == "v3.2" ]; then
  echo -e "[0;32m[PASS] Set-based query accurate and release.version=v3.2 annotation applied.[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "[0;31m[FAIL] Matched: '$MATCHED' | Anno 1: '$ANNO_1' | Anno 2: '$ANNO_2'[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi