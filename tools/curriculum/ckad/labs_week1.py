"""
Dedicated CKAD Lab Definitions for Week 1 (Days 1 to 6).
Aligned with KodeKloud CKAD Learning Modules: Core Concepts
"""

WEEK_1_LABS = [
    {
        "day": 1,
        "date": "2026-10-12",
        "title": "Pod Architecture & Multi-Container Pod Creation",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: Repair Broken Pod Manifest & Configure Multi-Container Pod
1. On node `controlplane`, a junior developer left a broken YAML manifest at `/tmp/webapp-core.yaml` intended to run in namespace `ckad-w1d1`.
2. Inspect and repair the syntax errors in `/tmp/webapp-core.yaml`:
   - Pod Name: `webapp-core`
   - Namespace: `ckad-w1d1`
   - Primary Container: named `web-app`, running image `nginx:1.24-alpine`, listening on containerPort `80`.
   - Sidecar Container: named `log-shipper`, running image `busybox:1.36`, executing the command:
     `sh -c "while true; do date >> /var/log/app/heartbeat.log; sleep 2; done"`
   - Storage: Mount a shared `emptyDir` volume named `shared-logs` at `/var/log/app` in **both** containers.
3. Apply the repaired manifest and verify that pod `webapp-core` enters `Running` status with both containers ready (`2/2`).""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w1d1 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_BROKEN" > /tmp/webapp-core.yaml
apiVersion: v1
kind: Pod
metadata:
  name: webapp-core
  namespace: ckad-w1d1
spec:
  volumes:
  - name: shared-logs
    emptyDir: {}
  containers:
  - name: web-app
    image: nginx:1.24-alpine
    ports:
    - containerPort: 80
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log/app
  - name: log-shipper
    image: busybox:1.36
    command: ["sh", "-c", "while true; do date >> /var/log/app/heartbeat.log; sleep 2; done"]
    volumeMounts:
    - name: wrong-vol-name
      mountPath: /var/log/app
EOF_BROKEN
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W1D1: Multi-Container Pod in namespace ckad-w1d1..."

POD_STATUS=$(ssh controlplane 'kubectl get pod webapp-core -n ckad-w1d1 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
READY_COUNT=$(ssh controlplane 'kubectl get pod webapp-core -n ckad-w1d1 -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null | grep -o "true" | wc -l || echo 0')

if [ "$POD_STATUS" != "Running" ] || [ "$READY_COUNT" -ne 2 ]; then
  echo -e "\\033[0;31m[FAIL] Pod webapp-core status is '$POD_STATUS' with $READY_COUNT/2 containers ready (expected 2/2 Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi

LOG_CHECK=$(ssh controlplane 'kubectl exec webapp-core -c web-app -n ckad-w1d1 -- cat /var/log/app/heartbeat.log 2>/dev/null | head -n 1 || echo "Empty"')
if [ "$LOG_CHECK" == "Empty" ] || [ -z "$LOG_CHECK" ]; then
  echo -e "\\033[0;31m[FAIL] /var/log/app/heartbeat.log not found or empty inside container web-app.\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi

echo -e "\\033[0;32m[PASS] Multi-container pod webapp-core running with shared volume and 2/2 containers ready.\\033[0m"
echo "Final Score: 1/1 (100%)"
exit 0""",
        "solution": """### Official Solution: Multi-Container Pod
```bash
# 1. Edit /tmp/webapp-core.yaml on controlplane:
# Fix the volumeMount name in container 'log-shipper' to match 'shared-logs':
ssh controlplane 'cat << "EOF_FIX" > /tmp/webapp-core.yaml
apiVersion: v1
kind: Pod
metadata:
  name: webapp-core
  namespace: ckad-w1d1
spec:
  volumes:
  - name: shared-logs
    emptyDir: {}
  containers:
  - name: web-app
    image: nginx:1.24-alpine
    ports:
    - containerPort: 80
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log/app
  - name: log-shipper
    image: busybox:1.36
    command: ["sh", "-c", "while true; do date >> /var/log/app/heartbeat.log; sleep 2; done"]
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log/app
EOF_FIX
kubectl apply -f /tmp/webapp-core.yaml
'
```""",
        "reset": """ssh controlplane '
kubectl delete namespace ckad-w1d1 --ignore-not-found
rm -f /tmp/webapp-core.yaml
'"""
    },
    {
        "day": 2,
        "date": "2026-10-13",
        "title": "Editing Pods & Command / Args Overrides",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Reconfigure Immutable Pod Command
1. In namespace `ckad-w1d2`, there is an existing running pod named `data-worker`.
2. Inspect the pod. Currently, it was started with a command that sleeps indefinitely.
3. Modify `data-worker` so that its container executes:
   - `command`: `["/bin/sh"]`
   - `args`: `["-c", "while true; do date >> /tmp/processed.log; sleep 2; done"]`
4. Since `spec.containers[*].command` is immutable, export the pod to YAML, delete/replace the pod, and ensure the updated pod runs with the new arguments and writes to `/tmp/processed.log`.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w1d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run data-worker --image=busybox:1.36 -n ckad-w1d2 --command -- sleep 3600
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W1D2: Editing Pod Command & Args in ckad-w1d2..."

PHASE=$(ssh controlplane 'kubectl get pod data-worker -n ckad-w1d2 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
if [ "$PHASE" != "Running" ]; then
  echo -e "\\033[0;31m[FAIL] Pod data-worker is '$PHASE' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi

ARGS=$(ssh controlplane 'kubectl get pod data-worker -n ckad-w1d2 -o jsonpath="{.spec.containers[0].args}" 2>/dev/null || echo ""')
LOG_CHECK=$(ssh controlplane 'kubectl exec data-worker -n ckad-w1d2 -- cat /tmp/processed.log 2>/dev/null | head -n 1 || echo "Empty"')

if [[ "$ARGS" =~ "processed.log" ]] && [ "$LOG_CHECK" != "Empty" ]; then
  echo -e "\\033[0;32m[PASS] Pod data-worker successfully updated with command/args loop.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Pod command/args not updated or /tmp/processed.log not generated.\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Editing Pods
```bash
# 1. Export pod spec to yaml:
ssh controlplane '
kubectl get pod data-worker -n ckad-w1d2 -o yaml > /tmp/worker.yaml

# 2. Update command and args in /tmp/worker.yaml and replace:
cat << "EOF_POD" > /tmp/worker.yaml
apiVersion: v1
kind: Pod
metadata:
  name: data-worker
  namespace: ckad-w1d2
spec:
  containers:
  - name: data-worker
    image: busybox:1.36
    command: ["/bin/sh"]
    args: ["-c", "while true; do date >> /tmp/processed.log; sleep 2; done"]
EOF_POD

kubectl replace --force -f /tmp/worker.yaml
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w1d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-10-14",
        "title": "ReplicaSets, Label Selectors & Pod Adoption",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: Create ReplicaSet & Adopt Orphaned Pod
1. In namespace `ckad-w1d3`, there is an unmanaged pod named `orphan-web` with label `app=frontend`.
2. Create a ReplicaSet named `frontend-rs` in namespace `ckad-w1d3`:
   - `spec.replicas`: `3`
   - `spec.selector.matchLabels`: `app=frontend,tier=web`
   - Pod Template Image: `nginx:1.24-alpine`
   - Template Labels: `app=frontend,tier=web`
3. Modify the labels of `orphan-web` to add `tier=web` so that `frontend-rs` acquires it.
4. Verify that total pods matching `app=frontend,tier=web` in namespace `ckad-w1d3` equals exactly 3.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w1d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run orphan-web --image=nginx:1.24-alpine -n ckad-w1d3 -l app=frontend
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W1D3: ReplicaSets & Pod Adoption in ckad-w1d3..."

RS_REPLICAS=$(ssh controlplane 'kubectl get rs frontend-rs -n ckad-w1d3 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
ORPHAN_LABEL=$(ssh controlplane 'kubectl get pod orphan-web -n ckad-w1d3 -o jsonpath="{.metadata.labels.tier}" 2>/dev/null || echo "none"')

if [ "$RS_REPLICAS" -eq 3 ] && [ "$ORPHAN_LABEL" == "web" ]; then
  echo -e "\\033[0;32m[PASS] ReplicaSet frontend-rs ready with 3 replicas including adopted orphan-web.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Ready replicas: $RS_REPLICAS (expected 3) | orphan-web tier label: $ORPHAN_LABEL (expected web).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: ReplicaSet & Label Selectors
```bash
# 1. Update labels on orphan-web:
ssh controlplane '
kubectl label pod orphan-web -n ckad-w1d3 tier=web

# 2. Create ReplicaSet manifest:
cat << "EOF_RS" | kubectl apply -f -
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: frontend-rs
  namespace: ckad-w1d3
spec:
  replicas: 3
  selector:
    matchLabels:
      app: frontend
      tier: web
  template:
    metadata:
      labels:
        app: frontend
        tier: web
    spec:
      containers:
      - name: nginx
        image: nginx:1.24-alpine
EOF_RS
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w1d3 --ignore-not-found'"""
    },
    {
        "day": 4,
        "date": "2026-10-15",
        "title": "Deployments, Zero-Downtime Rollouts & Scaling",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: Configure Rolling Update & Scale Deployment
1. In namespace `ckad-w1d4`, inspect existing deployment `api-gateway`.
2. Reconfigure its update strategy to:
   - `type`: `RollingUpdate`
   - `maxSurge`: `1`
   - `maxUnavailable`: `0`
3. Update the container image of `api-gateway` to `nginx:1.25-alpine`.
4. Scale the deployment to `4` replicas.
5. Wait for the rollout to complete successfully.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w1d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl create deployment api-gateway --image=nginx:1.24-alpine --replicas=2 -n ckad-w1d4
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W1D4: Deployments & Rolling Updates in ckad-w1d4..."

IMAGE=$(ssh controlplane 'kubectl get deploy api-gateway -n ckad-w1d4 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo "none"')
REPLICAS=$(ssh controlplane 'kubectl get deploy api-gateway -n ckad-w1d4 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
MAX_UNAVAIL=$(ssh controlplane 'kubectl get deploy api-gateway -n ckad-w1d4 -o jsonpath="{.spec.strategy.rollingUpdate.maxUnavailable}" 2>/dev/null || echo "none"')

if [[ "$IMAGE" =~ "nginx:1.25" ]] && [ "$REPLICAS" -eq 4 ] && [ "$MAX_UNAVAIL" == "0" ]; then
  echo -e "\\033[0;32m[PASS] api-gateway scaled to 4 replicas of nginx:1.25-alpine with maxUnavailable=0.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Image: $IMAGE, Replicas: $REPLICAS (expected 4), maxUnavailable: $MAX_UNAVAIL (expected 0).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Deployments & Rolling Updates
```bash
ssh controlplane '
kubectl patch deployment api-gateway -n ckad-w1d4 -p "{\"spec\":{\"strategy\":{\"type\":\"RollingUpdate\",\"rollingUpdate\":{\"maxSurge\":1,\"maxUnavailable\":0}}}}"
kubectl set image deployment/api-gateway api-gateway=nginx:1.25-alpine -n ckad-w1d4
kubectl scale deployment api-gateway --replicas=4 -n ckad-w1d4
kubectl rollout status deployment/api-gateway -n ckad-w1d4
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w1d4 --ignore-not-found'"""
    },
    {
        "day": 5,
        "date": "2026-10-16",
        "title": "Namespaces & Cross-Namespace DNS Communication",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Cross-Namespace Service Discovery
1. In namespace `ckad-w1d5-backend`, there is a service named `db-service` running on port `6379`.
2. In namespace `ckad-w1d5-frontend`, create a client pod named `query-client` using image `busybox:1.36`.
3. The container must run a shell script that resolves and pings the backend service using its fully qualified domain name (FQDN):
   `nc -z -w 3 db-service.ckad-w1d5-backend.svc.cluster.local 6379`
   and logs `"CONNECTION_SUCCESS"` to `/tmp/conn.log`.
4. Ensure `query-client` is running and `/tmp/conn.log` records successful connection.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w1d5-backend --dry-run=client -o yaml | kubectl apply -f -
kubectl create namespace ckad-w1d5-frontend --dry-run=client -o yaml | kubectl apply -f -

kubectl run redis-pod --image=redis:alpine -n ckad-w1d5-backend -l app=redis --restart=Always
kubectl expose pod redis-pod -n ckad-w1d5-backend --name=db-service --port=6379 --target-port=6379
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W1D5: Cross-Namespace DNS in ckad-w1d5-frontend..."

PHASE=$(ssh controlplane 'kubectl get pod query-client -n ckad-w1d5-frontend -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
LOG=$(ssh controlplane 'kubectl exec query-client -n ckad-w1d5-frontend -- cat /tmp/conn.log 2>/dev/null || echo "Missing"')

if [ "$PHASE" == "Running" ] && [[ "$LOG" =~ "CONNECTION_SUCCESS" ]]; then
  echo -e "\\033[0;32m[PASS] query-client successfully reached db-service across namespaces via CoreDNS.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] query-client phase: '$PHASE' | conn.log: '$LOG'\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Cross-Namespace DNS
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: query-client
  namespace: ckad-w1d5-frontend
spec:
  containers:
  - name: client
    image: busybox:1.36
    command: ["sh", "-c"]
    args:
    - while true; do
        if nc -z -w 3 db-service.ckad-w1d5-backend.svc.cluster.local 6379; then
          echo "CONNECTION_SUCCESS" > /tmp/conn.log;
        fi;
        sleep 2;
      done
EOF_POD
'
```""",
        "reset": """ssh controlplane '
kubectl delete namespace ckad-w1d5-backend --ignore-not-found
kubectl delete namespace ckad-w1d5-frontend --ignore-not-found
'"""
    },
    {
        "day": 6,
        "date": "2026-10-17",
        "title": "Imperative Commands & JSONPath Output Mastery",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Fast Imperative CLI & Data Extraction
1. In namespace `ckad-w1d6`, imperatively create a pod named `imperative-pod` with image `redis:7-alpine`, label `tier=cache`, and containerPort `6379`.
2. Extract the internal IP address of pod `target-alpha` in namespace `ckad-w1d6` using `kubectl ... -o jsonpath` and save ONLY the IP to `/tmp/alpha-ip.txt` on node `controlplane`.
3. Use `kubectl explain` to check the field name for pod's `terminationGracePeriodSeconds` and append the explanation title to `/tmp/explain.txt`.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w1d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run target-alpha --image=nginx:alpine -n ckad-w1d6
rm -f /tmp/alpha-ip.txt /tmp/explain.txt
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W1D6: Imperative Commands & JSONPath in ckad-w1d6..."

POD_PHASE=$(ssh controlplane 'kubectl get pod imperative-pod -n ckad-w1d6 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
POD_LABEL=$(ssh controlplane 'kubectl get pod imperative-pod -n ckad-w1d6 -o jsonpath="{.metadata.labels.tier}" 2>/dev/null || echo "none"')

ACTUAL_IP=$(ssh controlplane 'kubectl get pod target-alpha -n ckad-w1d6 -o jsonpath="{.status.podIP}" 2>/dev/null || echo "none"')
SAVED_IP=$(ssh controlplane 'cat /tmp/alpha-ip.txt 2>/dev/null || echo "empty"')

if [ "$POD_PHASE" == "Running" ] && [ "$POD_LABEL" == "cache" ] && [ "$SAVED_IP" == "$ACTUAL_IP" ] && [ "$SAVED_IP" != "empty" ]; then
  echo -e "\\033[0;32m[PASS] Imperative pod created and JSONPath IP correctly extracted to /tmp/alpha-ip.txt.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Phase: $POD_PHASE, Label: $POD_LABEL, Saved IP: '$SAVED_IP' vs Actual IP: '$ACTUAL_IP'\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Imperative CLI & JSONPath
```bash
ssh controlplane '
# 1. Imperatively create pod:
kubectl run imperative-pod --image=redis:7-alpine -n ckad-w1d6 --port=6379 -l tier=cache

# 2. Extract Pod IP:
kubectl get pod target-alpha -n ckad-w1d6 -o jsonpath="{.status.podIP}" > /tmp/alpha-ip.txt

# 3. Explain query:
kubectl explain pod.spec.terminationGracePeriodSeconds > /tmp/explain.txt
'
```""",
        "reset": """ssh controlplane '
kubectl delete namespace ckad-w1d6 --ignore-not-found
rm -f /tmp/alpha-ip.txt /tmp/explain.txt
'"""
    }
]
