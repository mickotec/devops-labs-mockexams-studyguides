#!/usr/bin/env python3
"""
Solve Validator for CKAD killer.sh Mock Exam 1 (All 16 Questions).
1. Starts mock-ckad-1
2. Solves Q1 through Q16
3. Runs grader and validates 16/16 (100%)
4. Resets mock-ckad-1
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
    print("=== [1/4] Starting mock-ckad-1 ===")
    rc, out, err = run("./lab start mock-ckad-1")
    if rc != 0:
        print(f"Failed to start: {err or out}")
        sys.exit(1)
    print("Environment initialized.")

    print("=== [2/4] Applying Solutions for Questions 1-16 ===")
    
    # Q1: Secret Env
    ssh("""
kubectl create secret generic db-secret --from-literal=username=admin --from-literal=password='SuperSecr3t!' -n mock-ckad-1-q1 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: secret-pod
  namespace: mock-ckad-1-q1
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
    env:
    - name: DB_USER
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: username
    - name: DB_PASS
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: password
EOF
""")

    # Q2: ConfigMap Volume
    ssh("""
kubectl create configmap app-cfg --from-literal=theme=dark --from-literal=max_connections=150 -n mock-ckad-1-q2 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: cfg-volume-pod
  namespace: mock-ckad-1-q2
spec:
  volumes:
  - name: cfg-vol
    configMap:
      name: app-cfg
  containers:
  - name: web
    image: nginx:alpine
    volumeMounts:
    - name: cfg-vol
      mountPath: /etc/app-config
EOF
""")

    # Q3: SecurityContext
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: hardened-pod
  namespace: mock-ckad-1-q3
spec:
  containers:
  - name: secured
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
    securityContext:
      runAsUser: 10001
      runAsGroup: 20001
      allowPrivilegeEscalation: false
      capabilities:
        drop: ["ALL"]
        add: ["NET_BIND_SERVICE"]
EOF
""")

    # Q4: ServiceAccount
    ssh("""
kubectl create serviceaccount report-runner -n mock-ckad-1-q4 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: report-worker
  namespace: mock-ckad-1-q4
spec:
  serviceAccountName: report-runner
  automountServiceAccountToken: false
  containers:
  - name: worker
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
EOF
""")

    # Q5: Sidecar
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: app-with-sidecar
  namespace: mock-ckad-1-q5
spec:
  volumes:
  - name: log-vol
    emptyDir: {}
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "while true; do date >> /var/log/app.log; sleep 2; done"]
    volumeMounts:
    - name: log-vol
      mountPath: /var/log
  - name: sidecar
    image: busybox:1.36
    command: ["sh", "-c", "tail -F /var/log/app.log"]
    volumeMounts:
    - name: log-vol
      mountPath: /var/log
EOF
""")

    # Q6: Init Container
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: web-init-pod
  namespace: mock-ckad-1-q6
spec:
  volumes:
  - name: html-vol
    emptyDir: {}
  initContainers:
  - name: init-html
    image: busybox:1.36
    command: ["sh", "-c", "echo 'Init Completed' > /work/index.html"]
    volumeMounts:
    - name: html-vol
      mountPath: /work
  containers:
  - name: web
    image: nginx:alpine
    volumeMounts:
    - name: html-vol
      mountPath: /usr/share/nginx/html
EOF
""")

    # Q7: PV & PVC
    run("ssh -o StrictHostKeyChecking=no node01 'sudo mkdir -p /data/mock1 && sudo chmod 777 /data/mock1'")
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mock1-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  storageClassName: manual
  hostPath:
    path: /data/mock1
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mock1-pvc
  namespace: mock-ckad-1-q7
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: manual
  resources:
    requests:
      storage: 500Mi
---
apiVersion: v1
kind: Pod
metadata:
  name: pvc-pod
  namespace: mock-ckad-1-q7
spec:
  volumes:
  - name: my-vol
    persistentVolumeClaim:
      claimName: mock1-pvc
  containers:
  - name: web
    image: nginx:alpine
    volumeMounts:
    - name: my-vol
      mountPath: /data
EOF
""")

    # Q8: Rolling Update
    ssh("""
kubectl set image deployment/store-api nginx=nginx:1.25.4-alpine -n mock-ckad-1-q8
""")

    # Q9: Blue/Green
    ssh("""
kubectl set selector service payments-svc 'version=v2' -n mock-ckad-1-q9
""")

    # Q10: Canary
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-canary
  namespace: mock-ckad-1-q10
spec:
  replicas: 2
  selector:
    matchLabels:
      app: frontend
      track: canary
  template:
    metadata:
      labels:
        app: frontend
        track: canary
    spec:
      containers:
      - name: web
        image: nginx:alpine
EOF
""")

    # Q11: NetworkPolicy
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: db-access-policy
  namespace: mock-ckad-1-q11
spec:
  podSelector:
    matchLabels:
      role: database
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: backend
    ports:
    - protocol: TCP
      port: 5432
EOF
""")

    # Q12: Ingress
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: api-ingress
  namespace: mock-ckad-1-q12
spec:
  rules:
  - host: store.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: svc-v1
            port:
              number: 8080
EOF
""")

    # Q13: NodePort
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: inventory-np
  namespace: mock-ckad-1-q13
spec:
  type: NodePort
  selector:
    app: inventory-service
  ports:
  - port: 8080
    targetPort: 8080
    nodePort: 30088
EOF
""")

    # Q14: Probes
    ssh("""
cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: probed-web
  namespace: mock-ckad-1-q14
spec:
  containers:
  - name: web
    image: nginx:alpine
    livenessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 2
      periodSeconds: 5
    readinessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 2
      periodSeconds: 5
EOF
""")

    # Q15: Pod Debugging
    ssh("""
kubectl delete pod order-worker -n mock-ckad-1-q15 --now 2>/dev/null || true
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
    command: ["sh", "-c", "if [ -z \\"$DB_HOST\\" ]; then echo 'FATAL: Missing DB_HOST' >&2; exit 1; else sleep 3600; fi"]
    env:
    - name: DB_HOST
      value: "postgres"
EOF_Q15
""")

    # Q16: Log Extraction
    ssh("""
kubectl logs gateway-hub -c ingress-proxy -n mock-ckad-1-q16 | grep "FATAL" > /tmp/fatal-errors.txt || true
""")

    print("Solutions applied. Waiting for pods to reach Ready...")
    ssh("""
kubectl wait --for=condition=Ready pod/app-with-sidecar -n mock-ckad-1-q5 --timeout=60s 2>/dev/null || true
kubectl wait --for=condition=Ready pod/web-init-pod -n mock-ckad-1-q6 --timeout=60s 2>/dev/null || true
kubectl wait --for=condition=Ready pod/pvc-pod -n mock-ckad-1-q7 --timeout=60s 2>/dev/null || true
kubectl wait --for=condition=Ready pod/probed-web -n mock-ckad-1-q14 --timeout=60s 2>/dev/null || true
""")
    time.sleep(5)

    print("=== [3/4] Running Grader (./lab check mock-ckad-1) ===")
    rc, out, err = run("./lab check mock-ckad-1")
    print(out)
    if "16 / 16 (100%)" in out or "Final Score: 16 / 16" in out:
        print("\n[SUCCESS] ALL 16 QUESTIONS IN MOCK-CKAD-1 PASSED 100%!")
    else:
        print("\n[FAIL] Score mismatch on mock-ckad-1.")

    print("=== [4/4] Cleaning Up (./lab reset mock-ckad-1) ===")
    run("./lab reset mock-ckad-1")
    print("Reset complete.")

if __name__ == "__main__":
    main()
