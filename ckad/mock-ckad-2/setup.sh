#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up mock-ckad-2 (CKAD killer.sh Real Exam Simulator 2)..."
ssh controlplane '
for q in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16; do
  kubectl create namespace mock-ckad-2-q$q --dry-run=client -o yaml | kubectl apply -f -
done

# Q2 setup: quota + over-request pod
cat << "EOF_Q2" | kubectl apply -f -
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-quota
  namespace: mock-ckad-2-q2
spec:
  hard:
    requests.cpu: "1"
    requests.memory: 1Gi
EOF_Q2

# Q4 setup: ServiceAccount
kubectl create serviceaccount app-deployer -n mock-ckad-2-q4 2>/dev/null || true

# Q9 setup: deployment with rollout revision
kubectl create deployment checkout --image=nginx:1.24-alpine --replicas=2 -n mock-ckad-2-q9 --dry-run=client -o yaml | kubectl apply -f -
kubectl set image deployment/checkout nginx=nginx:broken-nonexistent -n mock-ckad-2-q9 2>/dev/null || true

# Q10 setup: web-v1 & service
kubectl create deployment web-v1 --image=nginx:alpine --replicas=3 -n mock-ckad-2-q10 --dry-run=client -o yaml | sed "s/app: web-v1/app: web-shared/" | kubectl apply -f -
kubectl create service clusterip web-service --tcp=80:80 -n mock-ckad-2-q10 --dry-run=client -o yaml | sed "s/app: web-service/app: web-shared/" | kubectl apply -f -

# Q12 setup: services
kubectl create service clusterip order-svc --tcp=8080:80 -n mock-ckad-2-q12 2>/dev/null || true
kubectl create service clusterip catalog-svc --tcp=8080:80 -n mock-ckad-2-q12 2>/dev/null || true

# Q13 setup: pod
kubectl run redis-cache --image=redis:alpine --port=6379 -n mock-ckad-2-q13 2>/dev/null || true
'
echo "[✓] Environment ready. Review tasks with: ./lab show mock-ckad-2"
