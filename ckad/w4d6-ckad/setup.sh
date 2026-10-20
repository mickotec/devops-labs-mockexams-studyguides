#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d6-ckad (Debugging Pod Exit Codes: 137 OOMKilled & 127 Command)..."
ssh controlplane '
kubectl create namespace ckad-w4d6 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_PODS" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: memory-hungry
  namespace: ckad-w4d6
spec:
  containers:
  - name: mem
    image: busybox:1.36
    command: ["sh", "-c", "head -c 40M </dev/zero | tail -c 40M; sleep 3600"]
    resources:
      limits:
        memory: "20Mi"
---
apiVersion: v1
kind: Pod
metadata:
  name: broken-exec
  namespace: ckad-w4d6
spec:
  containers:
  - name: exec
    image: busybox:1.36
    command: ["/usr/local/bin/nonexistent-binary"]
EOF_PODS
'
echo "[✓] Environment ready. Review tasks with: ./lab show w4d6-ckad"
