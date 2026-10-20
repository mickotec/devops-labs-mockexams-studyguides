#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up mock-ckad-1 (CKAD killer.sh Real Exam Simulator 1)..."
ssh controlplane '
for q in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16; do
  kubectl create namespace mock-ckad-1-q$q --dry-run=client -o yaml | kubectl apply -f -
done

# Q6 setup
kubectl run db-backend --image=nginx:alpine --port=5432 -n mock-ckad-1-q6 --labels="app=db" 2>/dev/null || true

# Q8 setup
kubectl create deployment store-api --image=nginx:1.24-alpine --replicas=3 -n mock-ckad-1-q8 --dry-run=client -o yaml | kubectl apply -f -

# Q9 setup
cat << "EOF_Q9" | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payments-blue
  namespace: mock-ckad-1-q9
spec:
  replicas: 2
  selector:
    matchLabels:
      app: payments
      version: v1
  template:
    metadata:
      labels:
        app: payments
        version: v1
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payments-green
  namespace: mock-ckad-1-q9
spec:
  replicas: 2
  selector:
    matchLabels:
      app: payments
      version: v2
  template:
    metadata:
      labels:
        app: payments
        version: v2
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
---
apiVersion: v1
kind: Service
metadata:
  name: payments-svc
  namespace: mock-ckad-1-q9
spec:
  selector:
    app: payments
    version: v1
  ports:
  - port: 80
    targetPort: 80
EOF_Q9

# Q10 setup
cat << "EOF_Q10" | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-stable
  namespace: mock-ckad-1-q10
spec:
  replicas: 8
  selector:
    matchLabels:
      app: frontend
      track: stable
  template:
    metadata:
      labels:
        app: frontend
        track: stable
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
EOF_Q10

# Q11 setup
kubectl run db-pod --image=nginx:alpine --port=5432 --labels="role=database" -n mock-ckad-1-q11 2>/dev/null || true
kubectl run backend-client --image=busybox:1.36 --labels="role=backend" -n mock-ckad-1-q11 -- sleep 3600 2>/dev/null || true
kubectl run rogue-client --image=busybox:1.36 --labels="role=rogue" -n mock-ckad-1-q11 -- sleep 3600 2>/dev/null || true

# Q12 setup
kubectl create service clusterip svc-v1 --tcp=8080:80 -n mock-ckad-1-q12 2>/dev/null || true
kubectl create service clusterip svc-v2 --tcp=8080:80 -n mock-ckad-1-q12 2>/dev/null || true

# Q13 setup
kubectl create deployment inventory-service --image=nginx:alpine --port=8080 -n mock-ckad-1-q13 --dry-run=client -o yaml | kubectl apply -f -

# Q15 setup
cat << "EOF_Q15" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: order-worker
  namespace: mock-ckad-1-q15
spec:
  containers:
  - name: worker
    image: busybox:1.36
    command: ["sh", "-c", "if [ -z \"$DB_HOST\" ]; then echo 'FATAL: Missing DB_HOST' >&2; exit 1; else sleep 3600; fi"]
EOF_Q15

# Q16 setup
cat << "EOF_Q16" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: gateway-hub
  namespace: mock-ckad-1-q16
spec:
  containers:
  - name: ingress-proxy
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo 'INFO 200 OK'; sleep 1; echo 'FATAL Gateway Timeout' >&2; sleep 2; done"]
  - name: egress-proxy
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo 'INFO outbound'; sleep 2; done"]
EOF_Q16
'
echo "[✓] Environment ready. Review tasks with: ./lab show mock-ckad-1"
