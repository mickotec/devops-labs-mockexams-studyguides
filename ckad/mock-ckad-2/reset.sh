#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up mock-ckad-2..."
ssh controlplane '
for q in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16; do
  kubectl delete namespace mock-ckad-2-q$q --ignore-not-found
done
rm -rf /tmp/kustomize-store /tmp/hpa-version.txt /tmp/top-pod.txt
'
echo "[✓] Reset complete."
