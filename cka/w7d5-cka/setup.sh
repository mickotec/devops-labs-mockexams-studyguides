#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w7d5-cka (Network Policies Deep Dive)..."
ssh controlplane '
  kubectl delete namespace w7d5-netpol --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d5-netpol
  kubectl run frontend -n w7d5-netpol --image=nginx:alpine --labels=role=frontend
  kubectl run backend -n w7d5-netpol --image=nginx:alpine --labels=role=backend
  kubectl run database -n w7d5-netpol --image=nginx:alpine --labels=role=db
'
echo "[✓] Environment ready. Review tasks with: ./lab show w7d5-cka"
