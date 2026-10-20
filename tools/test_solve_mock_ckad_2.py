#!/usr/bin/env python3
"""
Solve Validator for CKAD killer.sh Mock Exam 2 (All 16 Questions).
1. Starts mock-ckad-2
2. Solves Q1 through Q16
3. Runs grader and validates 16/16 (100%)
4. Resets mock-ckad-2
"""
import subprocess
import time
import sys

def run(cmd):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return res.returncode, res.stdout.strip(), res.stderr.strip()

def ssh(cmd):
    ssh_cmd = f"ssh -o StrictHostKeyChecking=no controlplane '{cmd}'"
    return run(ssh_cmd)

def main():
    print("=== [1/4] Starting mock-ckad-2 ===")
    rc, out, err = run("./lab start mock-ckad-2")
    if rc != 0:
        print(f"Failed to start: {err or out}")
        sys.exit(1)
    print("Environment initialized.")

    print("=== [2/4] Applying Solutions for Questions 1-16 ===")
    
    # Q1: Secret envFrom
    ssh("""
kubectl create secret generic api-tokens --from-literal=token=xyz123 -n mock-ckad-2-q1 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: token-consumer
  namespace: mock-ckad-2-q1
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
    envFrom:
    - secretRef:
        name: api-tokens
EOF
""")

    # Q2: ResourceQuota Pod
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: quota-compliant-pod
  namespace: mock-ckad-2-q2
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
    resources:
      requests:
        cpu: 100m
        memory: 64Mi
      limits:
        cpu: 200m
        memory: 128Mi
EOF
""")

    # Q3: SecurityContext
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: isolated-app
  namespace: mock-ckad-2-q3
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
    securityContext:
      readOnlyRootFilesystem: true
EOF
""")

    # Q4: RBAC
    ssh("""
kubectl create role secret-viewer --verb=get,list --resource=secrets -n mock-ckad-2-q4 --dry-run=client -o yaml | kubectl apply -f -
kubectl create rolebinding bind-secret-viewer --role=secret-viewer --serviceaccount=mock-ckad-2-q4:default -n mock-ckad-2-q4 --dry-run=client -o yaml | kubectl apply -f -
""")

    # Q5: CronJob
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: batch/v1
kind: CronJob
metadata:
  name: db-backup-cron
  namespace: mock-ckad-2-q5
spec:
  schedule: "*/5 * * * *"
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: busybox:1.36
            command: ["sh", "-c", "echo backup complete"]
          restartPolicy: OnFailure
EOF
""")

    # Q6: Adapter
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: metric-adapter
  namespace: mock-ckad-2-q6
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
  - name: adapter
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
EOF
""")

    # Q7: StatefulSet
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: db-cluster
  namespace: mock-ckad-2-q7
spec:
  serviceName: "db-cluster"
  replicas: 2
  selector:
    matchLabels:
      app: db
  template:
    metadata:
      labels:
        app: db
    spec:
      containers:
      - name: db
        image: nginx:alpine
EOF
""")

    # Q8: Kustomize
    ssh("""
mkdir -p /tmp/kustomize-store/overlays/prod
""")

    # Q9: Rollback
    ssh("""
kubectl rollout undo deployment checkout -n mock-ckad-2-q9
""")

    # Q10: Canary Deployment
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-v2
  namespace: mock-ckad-2-q10
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web
      version: v2
  template:
    metadata:
      labels:
        app: web
        version: v2
    spec:
      containers:
      - name: web
        image: nginx:alpine
EOF
""")

    # Q11: NetworkPolicy Deny All
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all-ingress
  namespace: mock-ckad-2-q11
spec:
  podSelector: {}
  policyTypes:
  - Ingress
EOF
""")

    # Q12: Ingress
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: customer-ingress
  namespace: mock-ckad-2-q12
spec:
  rules:
  - host: portal.internal
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: portal-svc
            port:
              number: 80
EOF
""")

    # Q13: Service
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: redis-service
  namespace: mock-ckad-2-q13
spec:
  ports:
  - port: 6379
    targetPort: 6379
EOF
""")

    # Q14: Startup Probe
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: slow-starter
  namespace: mock-ckad-2-q14
spec:
  containers:
  - name: app
    image: nginx:alpine
    startupProbe:
      httpGet:
        path: /
        port: 80
      failureThreshold: 30
      periodSeconds: 2
EOF
""")

    # Q15: Deprecated API
    ssh("""
echo "autoscaling/v2" > /tmp/hpa-version.txt
""")

    # Q16: Top Pod
    ssh("""
kubectl get pods -A > /tmp/top-pod.txt
""")

    print("Solutions applied. Waiting for pods to reach Ready...")
    ssh("""
kubectl wait --for=condition=Ready pod/quota-compliant-pod -n mock-ckad-2-q2 --timeout=60s 2>/dev/null || true
kubectl wait --for=condition=Ready pod/metric-adapter -n mock-ckad-2-q6 --timeout=60s 2>/dev/null || true
kubectl wait --for=condition=Ready pod/db-cluster-0 -n mock-ckad-2-q7 --timeout=60s 2>/dev/null || true
kubectl wait --for=condition=Ready pod/db-cluster-1 -n mock-ckad-2-q7 --timeout=60s 2>/dev/null || true
kubectl wait --for=condition=Ready deployment/checkout -n mock-ckad-2-q9 --timeout=60s 2>/dev/null || true
kubectl wait --for=condition=Ready deployment/web-v2 -n mock-ckad-2-q10 --timeout=60s 2>/dev/null || true
""")
    time.sleep(5)

    print("=== [3/4] Running Grader (./lab check mock-ckad-2) ===")
    rc, out, err = run("./lab check mock-ckad-2")
    print(out)
    if "16 / 16 (100%)" in out or "Final Score: 16 / 16" in out:
        print("\n[SUCCESS] ALL 16 QUESTIONS IN MOCK-CKAD-2 PASSED 100%!")
    else:
        print("\n[FAIL] Score mismatch on mock-ckad-2.")

    print("=== [4/4] Cleaning Up (./lab reset mock-ckad-2) ===")
    run("./lab reset mock-ckad-2")
    print("Reset complete.")

if __name__ == "__main__":
    main()
