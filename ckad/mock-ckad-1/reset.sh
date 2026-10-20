#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up mock-ckad-1..."
ssh controlplane '
for q in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16; do
  kubectl delete namespace mock-ckad-1-q$q --ignore-not-found
done
kubectl delete pv mock1-pv --ignore-not-found
rm -f /tmp/fatal-errors.txt
'
echo "[✓] Reset complete."
