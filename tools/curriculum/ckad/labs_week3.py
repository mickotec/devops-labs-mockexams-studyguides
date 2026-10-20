"""
Dedicated CKAD Lab Definitions for Week 3 (Days 1 to 6).
Aligned with KodeKloud CKAD Learning Modules: Multi-Container Pods & Scheduling
"""

WEEK_3_LABS = [
    {
        "day": 1,
        "date": "2026-10-26",
        "title": "Multi-Container Pods: Sidecar Log Streaming",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Sidecar Container Log Shipper
1. In namespace `ckad-w3d1`, deploy a multi-container Pod named `app-logger`.
2. Main container named `app`:
   - Image: `busybox:1.36`
   - Command: `sh -c "while true; do echo 'TRANSACTION_ID='$(date +%s%N) >> /var/log/app/tx.log; sleep 2; done"`
   - Mount volume `log-storage` at `/var/log/app`.
3. Sidecar container named `sidecar`:
   - Image: `busybox:1.36`
   - Command: `sh -c "tail -n+1 -F /var/log/app/tx.log"`
   - Mount same volume `log-storage` at `/var/log/app`.
4. Define volume `log-storage` as `emptyDir: {}`.
5. Verify both containers are 2/2 Ready and `kubectl logs app-logger -c sidecar` outputs the transaction logs.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w3d1 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W3D1: Sidecar Logging in ckad-w3d1..."

PHASE=$(ssh controlplane 'kubectl get pod app-logger -n ckad-w3d1 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
READY_COUNT=$(ssh controlplane 'kubectl get pod app-logger -n ckad-w3d1 -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null | grep -o "true" | wc -l || echo 0')
LOG_OUT=$(ssh controlplane 'kubectl logs app-logger -c sidecar -n ckad-w3d1 2>/dev/null | head -n 1 || echo ""')

if [ "$PHASE" == "Running" ] && [ "$READY_COUNT" -eq 2 ] && [[ "$LOG_OUT" =~ "TRANSACTION_ID" ]]; then
  echo -e "\033[0;32m[PASS] Pod app-logger running 2/2 with sidecar successfully streaming transaction logs.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: $PHASE, Ready: $READY_COUNT/2, Log: '$LOG_OUT'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Sidecar Log Streaming
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: app-logger
  namespace: ckad-w3d1
spec:
  volumes:
  - name: log-storage
    emptyDir: {}
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo 'TRANSACTION_ID='$(date +%s%N) >> /var/log/app/tx.log; sleep 2; done"]
    volumeMounts:
    - name: log-storage
      mountPath: /var/log/app
  - name: sidecar
    image: busybox:1.36
    command: ["sh", "-c", "tail -n+1 -F /var/log/app/tx.log"]
    volumeMounts:
    - name: log-storage
      mountPath: /var/log/app
EOF_POD
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w3d1 --ignore-not-found'"""
    },
    {
        "day": 2,
        "date": "2026-10-27",
        "title": "Multi-Container Pods: Adapter Pattern",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: Normalize Metrics via Adapter
1. In namespace `ckad-w3d2`, create Pod `metric-adapter-pod`.
2. Main container named `app`:
   - Image: `busybox:1.36`
   - Writes raw metrics `cpu_usage: 42` to `/var/metrics/system.raw` every 2 seconds.
   - Mount volume `metrics-vol` at `/var/metrics`.
3. Adapter container named `adapter`:
   - Image: `busybox:1.36`
   - Mounts `metrics-vol` at `/var/metrics`.
   - Reads `/var/metrics/system.raw` and formats it into Prometheus format `node_cpu_usage 42` written to `/var/metrics/metrics.prom`.
4. Verify both containers run and `/var/metrics/metrics.prom` contains `node_cpu_usage`.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w3d2 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W3D2: Adapter Pattern in ckad-w3d2..."

READY=$(ssh controlplane 'kubectl get pod metric-adapter-pod -n ckad-w3d2 -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null | grep -o "true" | wc -l || echo 0')
PROM=$(ssh controlplane 'kubectl exec metric-adapter-pod -c adapter -n ckad-w3d2 -- cat /var/metrics/metrics.prom 2>/dev/null || echo ""')

if [ "$READY" -eq 2 ] && [[ "$PROM" =~ "node_cpu_usage" ]]; then
  echo -e "\033[0;32m[PASS] Adapter container running and successfully normalized metrics output.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Ready containers: $READY/2 | Prometheus metric: '$PROM'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Adapter Pattern
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: metric-adapter-pod
  namespace: ckad-w3d2
spec:
  volumes:
  - name: metrics-vol
    emptyDir: {}
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo 'cpu_usage: 42' > /var/metrics/system.raw; sleep 2; done"]
    volumeMounts:
    - name: metrics-vol
      mountPath: /var/metrics
  - name: adapter
    image: busybox:1.36
    command: ["sh", "-c", "while true; do [ -f /var/metrics/system.raw ] && echo 'node_cpu_usage 42' > /var/metrics/metrics.prom; sleep 2; done"]
    volumeMounts:
    - name: metrics-vol
      mountPath: /var/metrics
EOF_POD
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w3d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-10-28",
        "title": "Multi-Container Pods: Ambassador Pattern",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Ambassador Local Proxy Routing
1. In namespace `ckad-w3d3-infra`, deploy a Redis pod named `redis-backend` exposed via ClusterIP service `redis-svc` on port 6379.
2. In namespace `ckad-w3d3-apps`, deploy Pod `client-ambassador`.
3. The pod has 2 containers:
   - `ambassador`: runs `alpine/socat:latest` or `busybox` listening on `localhost:6379` and proxying to `redis-svc.ckad-w3d3-infra.svc.cluster.local:6379`.
   - `client`: connects to `localhost:6379` using `nc -z localhost 6379` and writes `"AMBASSADOR_CONNECTED"` to `/tmp/proxy.log`.
4. Verify `/tmp/proxy.log` contains `"AMBASSADOR_CONNECTED"`.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w3d3-infra --dry-run=client -o yaml | kubectl apply -f -
kubectl create namespace ckad-w3d3-apps --dry-run=client -o yaml | kubectl apply -f -

kubectl run redis-backend --image=redis:alpine -n ckad-w3d3-infra -l app=redis
kubectl expose pod redis-backend -n ckad-w3d3-infra --name=redis-svc --port=6379 --target-port=6379
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W3D3: Ambassador Pattern in ckad-w3d3-apps..."

PHASE=$(ssh controlplane 'kubectl get pod client-ambassador -n ckad-w3d3-apps -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
LOG=$(ssh controlplane 'kubectl exec client-ambassador -c client -n ckad-w3d3-apps -- cat /tmp/proxy.log 2>/dev/null || echo ""')

if [ "$PHASE" == "Running" ] && [[ "$LOG" =~ "AMBASSADOR_CONNECTED" ]]; then
  echo -e "\033[0;32m[PASS] Client successfully accessed remote database through localhost ambassador proxy.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: $PHASE | Proxy log: '$LOG'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Ambassador Pattern
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: client-ambassador
  namespace: ckad-w3d3-apps
spec:
  containers:
  - name: client
    image: busybox:1.36
    command: ["sh", "-c"]
    args:
    - while true; do
        if nc -z localhost 6379; then
          echo "AMBASSADOR_CONNECTED" > /tmp/proxy.log;
        fi;
        sleep 2;
      done
  - name: ambassador
    image: busybox:1.36
    command: ["sh", "-c", "nc -lk -p 6379 -e nc redis-svc.ckad-w3d3-infra.svc.cluster.local 6379"]
EOF_POD
'
```""",
        "reset": """ssh controlplane '
kubectl delete namespace ckad-w3d3-infra --ignore-not-found
kubectl delete namespace ckad-w3d3-apps --ignore-not-found
'"""
    },
    {
        "day": 4,
        "date": "2026-10-29",
        "title": "Init Containers & Service Dependency Gating",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Unblock Pod Stuck in Init:0/1
1. In namespace `ckad-w3d4`, there is an existing pod named `webapp-gated` currently stuck in `Init:0/1`.
2. Inspect the pod specifications and init container logs to determine what dependency it is waiting for.
3. You will discover the init container is waiting for service `mysql-backend` on port `3306`.
4. Deploy a Pod `mysql-dummy` running `busybox:1.36` (listening on port 3306 with `nc -lk -p 3306`) and expose it as a ClusterIP service named `mysql-backend` on port `3306`.
5. Verify that `webapp-gated` completes its init step and transitions to `Running` (1/1 Ready).""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w3d4 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_GATED" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: webapp-gated
  namespace: ckad-w3d4
spec:
  initContainers:
  - name: check-mysql
    image: busybox:1.36
    command: ["sh", "-c", "until nc -z -w 2 mysql-backend 3306; do echo waiting for mysql; sleep 2; done"]
  containers:
  - name: web
    image: nginx:alpine
EOF_GATED
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W3D4: Init Container Unblocking in ckad-w3d4..."

PHASE=$(ssh controlplane 'kubectl get pod webapp-gated -n ckad-w3d4 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
READY=$(ssh controlplane 'kubectl get pod webapp-gated -n ckad-w3d4 -o jsonpath="{.status.containerStatuses[0].ready}" 2>/dev/null || echo "false"')

if [ "$PHASE" == "Running" ] && [ "$READY" == "true" ]; then
  echo -e "\033[0;32m[PASS] webapp-gated unblocked and Running 1/1 after service dependency fulfilled.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: $PHASE, Ready: $READY (expected 1/1 Running).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Init Containers
```bash
ssh controlplane '
# 1. Inspect init container:
kubectl describe pod webapp-gated -n ckad-w3d4

# 2. Deploy dummy backend and expose as mysql-backend:
kubectl run mysql-dummy --image=busybox:1.36 -n ckad-w3d4 --command -- nc -lk -p 3306
kubectl expose pod mysql-dummy -n ckad-w3d4 --name=mysql-backend --port=3306 --target-port=3306

# 3. Check webapp transitions to Running:
kubectl get pod webapp-gated -n ckad-w3d4
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w3d4 --ignore-not-found'"""
    },
    {
        "day": 5,
        "date": "2026-10-30",
        "title": "Node Taints, Effects & Pod Tolerations",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: Schedule Pod on Tainted Worker Node
1. Worker node `node01` has been tainted with:
   `dedicated=analytics:NoSchedule`
2. In namespace `ckad-w3d5`, create a Pod named `analytics-engine` using image `nginx:alpine`.
3. Add the required toleration so that `analytics-engine` can schedule onto `node01`.
4. Also add `spec.nodeName: node01` or `spec.nodeSelector` to guarantee it lands on `node01`.
5. Verify that `analytics-engine` is `Running` on `node01`.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w3d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl taint nodes node01 dedicated=analytics:NoSchedule --overwrite 2>/dev/null || true
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W3D5: Taints & Tolerations in ckad-w3d5..."

PHASE=$(ssh controlplane 'kubectl get pod analytics-engine -n ckad-w3d5 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
NODE=$(ssh controlplane 'kubectl get pod analytics-engine -n ckad-w3d5 -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "none"')
TOL_KEY=$(ssh controlplane 'kubectl get pod analytics-engine -n ckad-w3d5 -o jsonpath="{.spec.tolerations[?(@.key==\"dedicated\")].key}" 2>/dev/null || echo ""')

if [ "$PHASE" == "Running" ] && [ "$NODE" == "node01" ] && [ "$TOL_KEY" == "dedicated" ]; then
  echo -e "\033[0;32m[PASS] Pod analytics-engine running on tainted node01 with matching toleration.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: $PHASE, Node: $NODE (expected node01), Toleration: '$TOL_KEY'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Taints & Tolerations
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: analytics-engine
  namespace: ckad-w3d5
spec:
  nodeName: node01
  tolerations:
  - key: dedicated
    operator: Equal
    value: analytics
    effect: NoSchedule
  containers:
  - name: engine
    image: nginx:alpine
EOF_POD
'
```""",
        "reset": """ssh controlplane '
kubectl delete namespace ckad-w3d5 --ignore-not-found
kubectl taint nodes node01 dedicated:NoSchedule- 2>/dev/null || true
'"""
    },
    {
        "day": 6,
        "date": "2026-10-31",
        "title": "Node Selectors & Required NodeAffinity",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Attract Pods Using Required NodeAffinity
1. Label worker node `node02` with label `storage-tier=nvme`.
2. In namespace `ckad-w3d6`, create a Pod named `fast-io-worker` with image `redis:alpine`.
3. Configure `spec.affinity.nodeAffinity` using `requiredDuringSchedulingIgnoredDuringExecution` requiring that `storage-tier` is `In` values `["nvme"]`.
4. Verify that `fast-io-worker` schedules exclusively onto `node02` and enters `Running` state.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w3d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl label nodes node02 storage-tier- 2>/dev/null || true
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W3D6: NodeAffinity in ckad-w3d6..."

PHASE=$(ssh controlplane 'kubectl get pod fast-io-worker -n ckad-w3d6 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
NODE=$(ssh controlplane 'kubectl get pod fast-io-worker -n ckad-w3d6 -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "none"')
LABEL=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.metadata.labels.storage-tier}" 2>/dev/null || echo "none"')

if [ "$PHASE" == "Running" ] && [ "$NODE" == "node02" ] && [ "$LABEL" == "nvme" ]; then
  echo -e "\033[0;32m[PASS] Pod fast-io-worker scheduled on node02 matching required nodeAffinity.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: $PHASE, Node: $NODE (expected node02), node02 label: $LABEL (expected nvme).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: NodeAffinity
```bash
ssh controlplane '
# 1. Label node02:
kubectl label nodes node02 storage-tier=nvme --overwrite

# 2. Deploy pod with nodeAffinity:
cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: fast-io-worker
  namespace: ckad-w3d6
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: storage-tier
            operator: In
            values:
            - nvme
  containers:
  - name: redis
    image: redis:alpine
EOF_POD
'
```""",
        "reset": """ssh controlplane '
kubectl delete namespace ckad-w3d6 --ignore-not-found
kubectl label nodes node02 storage-tier- 2>/dev/null || true
'"""
    }
]
