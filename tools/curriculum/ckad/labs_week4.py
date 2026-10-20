"""
Dedicated CKAD Lab Definitions for Week 4 (Days 1 to 6).
Aligned with KodeKloud CKAD Learning Modules: Observability & Maintenance
"""

WEEK_4_LABS = [
    {
        "day": 1,
        "date": "2026-11-02",
        "title": "Readiness Probes & Service Endpoint Gating",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Configure HTTP Readiness Probe
1. In namespace `ckad-w4d1`, create a Pod named `order-processor` running image `nginx:alpine`.
2. Configure an HTTP GET readiness probe on path `/ready` port `80`:
   - `initialDelaySeconds`: `5`
   - `periodSeconds`: `3`
   - `failureThreshold`: `2`
3. Expose `order-processor` with a ClusterIP service named `order-service` on port `80`.
4. Ensure the probe passes by creating `/usr/share/nginx/html/ready` inside the container.
5. Verify that `order-service` registers the pod IP as a healthy endpoint.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w4d1 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W4D1: Readiness Probes in ckad-w4d1..."

PHASE=$(ssh controlplane 'kubectl get pod order-processor -n ckad-w4d1 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
READY=$(ssh controlplane 'kubectl get pod order-processor -n ckad-w4d1 -o jsonpath="{.status.containerStatuses[0].ready}" 2>/dev/null || echo "false"')
EP=$(ssh controlplane 'kubectl get endpoints order-service -n ckad-w4d1 -o jsonpath="{.subsets[*].addresses[*].ip}" 2>/dev/null || echo ""')

if [ "$PHASE" == "Running" ] && [ "$READY" == "true" ] && [ -n "$EP" ]; then
  echo -e "\033[0;32m[PASS] Pod order-processor ready and registered in order-service endpoints.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: $PHASE, Ready: $READY, Endpoints: '$EP'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Readiness Probes
```bash
ssh controlplane 'cat << "EOF_ALL" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: order-processor
  namespace: ckad-w4d1
  labels:
    app: order-proc
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    ports:
    - containerPort: 80
    readinessProbe:
      httpGet:
        path: /ready
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 3
      failureThreshold: 2
    lifecycle:
      postStart:
        exec:
          command: ["sh", "-c", "touch /usr/share/nginx/html/ready"]
---
apiVersion: v1
kind: Service
metadata:
  name: order-service
  namespace: ckad-w4d1
spec:
  selector:
    app: order-proc
  ports:
  - port: 80
    targetPort: 80
EOF_ALL
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w4d1 --ignore-not-found'"""
    },
    {
        "day": 2,
        "date": "2026-11-03",
        "title": "Liveness Probes & Automated Container Healing",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Configure Exec Liveness Probe
1. In namespace `ckad-w4d2`, deploy Pod `health-monitor` running image `busybox:1.36`.
2. The container must touch `/tmp/healthy` at startup and sleep indefinitely:
   `command: ["sh", "-c", "touch /tmp/healthy && sleep 3600"]`
3. Configure an Exec liveness probe checking `cat /tmp/healthy`:
   - `initialDelaySeconds`: `5`
   - `periodSeconds`: `5`
4. Verify that `health-monitor` runs continuously without restarting.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w4d2 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W4D2: Liveness Probes in ckad-w4d2..."

PHASE=$(ssh controlplane 'kubectl get pod health-monitor -n ckad-w4d2 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
RESTARTS=$(ssh controlplane 'kubectl get pod health-monitor -n ckad-w4d2 -o jsonpath="{.status.containerStatuses[0].restartCount}" 2>/dev/null || echo 99')
PROBE=$(ssh controlplane 'kubectl get pod health-monitor -n ckad-w4d2 -o jsonpath="{.spec.containers[0].livenessProbe.exec.command}" 2>/dev/null || echo ""')

if [ "$PHASE" == "Running" ] && [ "$RESTARTS" -eq 0 ] && [[ "$PROBE" =~ "healthy" ]]; then
  echo -e "\033[0;32m[PASS] Pod health-monitor running 1/1 with active exec liveness probe (0 restarts).\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: $PHASE, Restarts: $RESTARTS (expected 0), Probe: '$PROBE'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Liveness Probes
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: health-monitor
  namespace: ckad-w4d2
spec:
  containers:
  - name: monitor
    image: busybox:1.36
    command: ["sh", "-c", "touch /tmp/healthy && sleep 3600"]
    livenessProbe:
      exec:
        command:
        - cat
        - /tmp/healthy
      initialDelaySeconds: 5
      periodSeconds: 5
EOF_POD
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w4d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-11-04",
        "title": "Startup Probes for Slow Initialization Workloads",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Shield Slow Boot with Startup Probe
1. In namespace `ckad-w4d3`, deploy Pod `slow-boot-app` with image `busybox:1.36`.
2. The container takes 20 seconds to initialize before creating `/tmp/initialized`:
   `command: ["sh", "-c", "sleep 20 && touch /tmp/initialized && sleep 3600"]`
3. Configure a Startup Probe:
   - Exec command: `cat /tmp/initialized`
   - `failureThreshold`: `15`
   - `periodSeconds`: `3`
4. Configure a Liveness Probe:
   - Exec command: `cat /tmp/initialized`
   - `periodSeconds`: `5`
5. Verify that the startup probe prevents premature liveness kills and the pod enters `Running` state cleanly.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w4d3 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W4D3: Startup Probes in ckad-w4d3..."

PHASE=$(ssh controlplane 'kubectl get pod slow-boot-app -n ckad-w4d3 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
RESTARTS=$(ssh controlplane 'kubectl get pod slow-boot-app -n ckad-w4d3 -o jsonpath="{.status.containerStatuses[0].restartCount}" 2>/dev/null || echo 99')
THRESHOLD=$(ssh controlplane 'kubectl get pod slow-boot-app -n ckad-w4d3 -o jsonpath="{.spec.containers[0].startupProbe.failureThreshold}" 2>/dev/null || echo 0')

if [ "$PHASE" == "Running" ] && [ "$RESTARTS" -eq 0 ] && [ "$THRESHOLD" -eq 15 ]; then
  echo -e "\033[0;32m[PASS] slow-boot-app successfully bootstrapped with startupProbe shield (0 restarts).\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: $PHASE, Restarts: $RESTARTS (expected 0), Startup failureThreshold: $THRESHOLD (expected 15).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Startup Probes
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: slow-boot-app
  namespace: ckad-w4d3
spec:
  containers:
  - name: slow-app
    image: busybox:1.36
    command: ["sh", "-c", "sleep 20 && touch /tmp/initialized && sleep 3600"]
    startupProbe:
      exec:
        command:
        - cat
        - /tmp/initialized
      failureThreshold: 15
      periodSeconds: 3
    livenessProbe:
      exec:
        command:
        - cat
        - /tmp/initialized
      periodSeconds: 5
EOF_POD
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w4d3 --ignore-not-found'"""
    },
    {
        "day": 4,
        "date": "2026-11-05",
        "title": "Multi-Container Logging & Crash Log Extraction",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Extract Previous Crash Logs
1. In namespace `ckad-w4d4`, inspect multi-container pod `microservice-pod`.
2. Container `database-sync` crashed and restarted.
3. Extract the crash logs of the previous terminated instance of container `database-sync` using `kubectl logs ... --previous`.
4. Filter out lines containing `"FATAL"` and save them to `/tmp/fatal-sync.log` on node `controlplane`.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w4d4 --dry-run=client -o yaml | kubectl apply -f -
rm -f /tmp/fatal-sync.log
cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: microservice-pod
  namespace: ckad-w4d4
spec:
  containers:
  - name: web
    image: nginx:alpine
  - name: database-sync
    image: busybox:1.36
    command: ["sh", "-c"]
    args:
    - if [ ! -f /tmp/crashed ]; then
        touch /tmp/crashed;
        echo "[FATAL] Connection timeout to db host" >&2;
        exit 1;
      else
        echo "Running healthy";
        sleep 3600;
      fi
EOF_POD
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W4D4: Previous Logs Extraction in ckad-w4d4..."

LOG_CONTENT=$(ssh controlplane 'cat /tmp/fatal-sync.log 2>/dev/null || echo ""')
if [[ "$LOG_CONTENT" =~ "FATAL" ]]; then
  echo -e "\033[0;32m[PASS] Fatal crash log correctly captured in /tmp/fatal-sync.log.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] /tmp/fatal-sync.log missing or does not contain FATAL log.\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Previous Logs Extraction
```bash
ssh controlplane '
kubectl logs microservice-pod -c database-sync -n ckad-w4d4 --previous | grep -i fatal > /tmp/fatal-sync.log
cat /tmp/fatal-sync.log
'
```""",
        "reset": """ssh controlplane '
kubectl delete namespace ckad-w4d4 --ignore-not-found
rm -f /tmp/fatal-sync.log
'"""
    },
    {
        "day": 5,
        "date": "2026-11-06",
        "title": "Workload Monitoring with Metrics Server (kubectl top)",
        "diff": "Medium",
        "time": "20m",
        "tasks": """### Task 1: Identify Highest Resource Consumer
1. In namespace `kube-system`, several core cluster workloads are running.
2. Using `kubectl top pod -n kube-system --sort-by=cpu`, identify the pod currently consuming the highest CPU.
3. Save the name of that highest CPU pod into `/tmp/top-cpu-pod.txt` on node `controlplane`.""",
        "setup": """ssh controlplane 'rm -f /tmp/top-cpu-pod.txt'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W4D5: kubectl top in kube-system..."

SAVED_POD=$(ssh controlplane 'cat /tmp/top-cpu-pod.txt 2>/dev/null | tr -d "[:space:]"')
TOP_POD=$(ssh controlplane 'kubectl top pod -n kube-system --sort-by=cpu --no-headers 2>/dev/null | head -n 1 | awk "{print \$1}" | tr -d "[:space:]"')

if [ -n "$SAVED_POD" ] && [ "$SAVED_POD" == "$TOP_POD" ]; then
  echo -e "\033[0;32m[PASS] Top CPU pod identified accurately: $SAVED_POD\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Saved pod: '$SAVED_POD' vs Actual top pod: '$TOP_POD'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: kubectl top
```bash
ssh controlplane '
kubectl top pod -n kube-system --sort-by=cpu --no-headers | head -n 1 | awk "{print \$1}" > /tmp/top-cpu-pod.txt
cat /tmp/top-cpu-pod.txt
'
```""",
        "reset": """ssh controlplane 'rm -f /tmp/top-cpu-pod.txt'"""
    },
    {
        "day": 6,
        "date": "2026-11-07",
        "title": "Debugging Pod Exit Codes: 137 OOMKilled & 127 Command",
        "diff": "Hard",
        "time": "30m",
        "tasks": """### Task 1: Fix OOMKilled Pod (Exit Code 137)
1. In namespace `ckad-w4d6`, pod `memory-hungry` is failing repeatedly with Exit Code 137 (OOMKilled) because its memory limit is set to `20Mi` while the container requires `64Mi`.
2. Inspect the pod and increase `spec.containers[0].resources.limits.memory` to `128Mi` (and requests to `64Mi`).
3. Recreate the pod so that it enters `Running` state without crash looping.

### Task 2: Fix Command Not Found (Exit Code 127)
1. In namespace `ckad-w4d6`, pod `broken-exec` is failing with Exit Code 127 because its command is set to `/usr/local/bin/nonexistent-binary`.
2. Change the command to `["/bin/sh", "-c", "sleep 3600"]`.
3. Verify both pods are in `Running` (1/1 Ready) state.""",
        "setup": """ssh controlplane '
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
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W4D6: Debugging Exit Codes in ckad-w4d6..."

MEM_PHASE=$(ssh controlplane 'kubectl get pod memory-hungry -n ckad-w4d6 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
MEM_READY=$(ssh controlplane 'kubectl get pod memory-hungry -n ckad-w4d6 -o jsonpath="{.status.containerStatuses[0].ready}" 2>/dev/null || echo "false"')

EXEC_PHASE=$(ssh controlplane 'kubectl get pod broken-exec -n ckad-w4d6 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
EXEC_READY=$(ssh controlplane 'kubectl get pod broken-exec -n ckad-w4d6 -o jsonpath="{.status.containerStatuses[0].ready}" 2>/dev/null || echo "false"')

if [ "$MEM_PHASE" == "Running" ] && [ "$MEM_READY" == "true" ] && [ "$EXEC_PHASE" == "Running" ] && [ "$EXEC_READY" == "true" ]; then
  echo -e "\033[0;32m[PASS] Both memory-hungry and broken-exec repaired and Running 1/1.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] memory-hungry: $MEM_PHASE ($MEM_READY) | broken-exec: $EXEC_PHASE ($EXEC_READY)\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Debugging Exit Codes
```bash
ssh controlplane '
# 1. Fix memory-hungry:
cat << "EOF_MEM" | kubectl replace --force -f -
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
        memory: "128Mi"
      requests:
        memory: "64Mi"
EOF_MEM

# 2. Fix broken-exec:
cat << "EOF_EXEC" | kubectl replace --force -f -
apiVersion: v1
kind: Pod
metadata:
  name: broken-exec
  namespace: ckad-w4d6
spec:
  containers:
  - name: exec
    image: busybox:1.36
    command: ["/bin/sh", "-c", "sleep 3600"]
EOF_EXEC
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w4d6 --ignore-not-found'"""
    }
]
