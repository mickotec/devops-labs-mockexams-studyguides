#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w8d4-ckad (API Versions & Deprecations Migration)..."
ssh controlplane '
kubectl create namespace ckad-w8d4 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_DEP" > /tmp/deprecated-ingress.yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: legacy-ingress
  namespace: ckad-w8d4
spec:
  rules:
  - host: legacy.example.com
    http:
      paths:
      - path: /
        backend:
          serviceName: web-svc
          servicePort: 80
EOF_DEP
'
echo "[✓] Environment ready. Review tasks with: ./lab show w8d4-ckad"
