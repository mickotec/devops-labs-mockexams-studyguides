"""
Dedicated CKAD Lab Definitions for Week 5 (Days 1 to 6).
Aligned with KodeKloud CKAD Learning Modules: POD Design
"""

WEEK_5_LABS = [
    {
        "day": 1,
        "date": "2026-11-09",
        "title": "Labels, Set-Based Selectors & Annotations",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Filter Pods & Apply Metadata
1. In namespace `ckad-w5d1`, there are several pods with various labels.
2. Filter the pods using set-based selector syntax for:
   `tier in (backend, cache), env!=dev`
3. Save the names of all matching pods to `/tmp/matched-pods.txt` on node `controlplane`.
4. Add the annotation `release.version=v3.2` to all matching pods in namespace `ckad-w5d1`.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w5d1 --dry-run=client -o yaml | kubectl apply -f -
rm -f /tmp/matched-pods.txt

kubectl run pod-1 -n ckad-w5d1 --image=nginx:alpine -l tier=backend,env=prod
kubectl run pod-2 -n ckad-w5d1 --image=nginx:alpine -l tier=cache,env=prod
kubectl run pod-3 -n ckad-w5d1 --image=nginx:alpine -l tier=frontend,env=prod
kubectl run pod-4 -n ckad-w5d1 --image=nginx:alpine -l tier=backend,env=dev
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W5D1: Labels & Selectors in ckad-w5d1..."

MATCHED=$(ssh controlplane 'cat /tmp/matched-pods.txt 2>/dev/null || echo ""')
ANNO_1=$(ssh controlplane 'kubectl get pod pod-1 -n ckad-w5d1 -o jsonpath="{.metadata.annotations.release\.version}" 2>/dev/null || echo ""')
ANNO_2=$(ssh controlplane 'kubectl get pod pod-2 -n ckad-w5d1 -o jsonpath="{.metadata.annotations.release\.version}" 2>/dev/null || echo ""')

if [[ "$MATCHED" =~ "pod-1" ]] && [[ "$MATCHED" =~ "pod-2" ]] && ! [[ "$MATCHED" =~ "pod-3" ]] && ! [[ "$MATCHED" =~ "pod-4" ]] && [ "$ANNO_1" == "v3.2" ] && [ "$ANNO_2" == "v3.2" ]; then
  echo -e "\033[0;32m[PASS] Set-based query accurate and release.version=v3.2 annotation applied.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Matched: '$MATCHED' | Anno 1: '$ANNO_1' | Anno 2: '$ANNO_2'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Labels & Selectors
```bash
ssh controlplane '
# 1. Query matching pods:
kubectl get pods -n ckad-w5d1 -l "tier in (backend, cache), env!=dev" -o jsonpath="{.items[*].metadata.name}" | tr " " "\n" > /tmp/matched-pods.txt

# 2. Apply annotation:
kubectl annotate pods -n ckad-w5d1 -l "tier in (backend, cache), env!=dev" release.version=v3.2
'
```""",
        "reset": """ssh controlplane '
kubectl delete namespace ckad-w5d1 --ignore-not-found
rm -f /tmp/matched-pods.txt
'"""
    },
    {
        "day": 2,
        "date": "2026-11-10",
        "title": "Rolling Updates with Zero-Downtime MaxSurge",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: Zero-Downtime Rolling Update
1. In namespace `ckad-w5d2`, inspect existing deployment `payment-gateway`.
2. Configure rolling update strategy parameters:
   - `maxSurge`: `2`
   - `maxUnavailable`: `0`
3. Update the container image to `nginx:1.25-alpine`.
4. Scale deployment to `5` replicas.
5. Track and ensure rollout completes successfully using `kubectl rollout status`.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w5d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl create deployment payment-gateway --image=nginx:1.24-alpine --replicas=3 -n ckad-w5d2
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W5D2: Rolling Updates in ckad-w5d2..."

IMG=$(ssh controlplane 'kubectl get deploy payment-gateway -n ckad-w5d2 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo ""')
REPLICAS=$(ssh controlplane 'kubectl get deploy payment-gateway -n ckad-w5d2 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
SURGE=$(ssh controlplane 'kubectl get deploy payment-gateway -n ckad-w5d2 -o jsonpath="{.spec.strategy.rollingUpdate.maxSurge}" 2>/dev/null || echo ""')
UNAVAIL=$(ssh controlplane 'kubectl get deploy payment-gateway -n ckad-w5d2 -o jsonpath="{.spec.strategy.rollingUpdate.maxUnavailable}" 2>/dev/null || echo ""')

if [[ "$IMG" =~ "nginx:1.25" ]] && [ "$REPLICAS" -eq 5 ] && [ "$SURGE" == "2" ] && [ "$UNAVAIL" == "0" ]; then
  echo -e "\033[0;32m[PASS] payment-gateway rolling update completed with maxSurge=2, maxUnavailable=0.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Image: $IMG, Replicas: $REPLICAS (expected 5), Surge: $SURGE, Unavail: $UNAVAIL\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Rolling Updates
```bash
ssh controlplane '
kubectl patch deployment payment-gateway -n ckad-w5d2 --type="strategic" -p "{\\"spec\\":{\\"strategy\\":{\\"rollingUpdate\\":{\\"maxSurge\\":2,\\"maxUnavailable\\":0}}}}"
kubectl set image deployment/payment-gateway nginx=nginx:1.25-alpine -n ckad-w5d2
kubectl scale deployment payment-gateway --replicas=5 -n ckad-w5d2
kubectl rollout status deployment/payment-gateway -n ckad-w5d2
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w5d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-11-11",
        "title": "Rollback Strategies & Historical Revisions",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Roll Back Faulty Deployment Revision
1. In namespace `ckad-w5d3`, deployment `checkout-api` is broken in revision 2 because an invalid image (`nginx:bad-tag-xyz`) was deployed.
2. Inspect rollout history using `kubectl rollout history deployment checkout-api -n ckad-w5d3`.
3. Roll back the deployment to healthy revision 1 using `kubectl rollout undo`.
4. Verify that the deployment restores running pods with image `nginx:1.24-alpine` and all 3 replicas become ready.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w5d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl create deployment checkout-api --image=nginx:1.24-alpine --replicas=3 -n ckad-w5d3
kubectl set image deployment/checkout-api nginx=nginx:bad-tag-xyz -n ckad-w5d3
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W5D3: Rollback in ckad-w5d3..."

IMG=$(ssh controlplane 'kubectl get deploy checkout-api -n ckad-w5d3 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo ""')
READY=$(ssh controlplane 'kubectl get deploy checkout-api -n ckad-w5d3 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')

if [[ "$IMG" =~ "nginx:1.24-alpine" ]] && [ "$READY" -eq 3 ]; then
  echo -e "\033[0;32m[PASS] checkout-api successfully rolled back to revision 1 (nginx:1.24-alpine, 3/3 Ready).\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Image: $IMG (expected nginx:1.24-alpine), Ready: $READY (expected 3).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Rollback Strategies
```bash
ssh controlplane '
kubectl rollout undo deployment/checkout-api -n ckad-w5d3
kubectl rollout status deployment/checkout-api -n ckad-w5d3
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w5d3 --ignore-not-found'"""
    },
    {
        "day": 4,
        "date": "2026-11-12",
        "title": "Blue-Green Deployment Cutover",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: Atomic Cutover to Green Release
1. In namespace `ckad-w5d4`, service `web-portal` currently routes to Blue release (`version=v1`).
2. Deploy the Green release:
   - Deployment Name: `portal-green`
   - Replicas: `3`
   - Labels: `app=portal,version=v2`
   - Image: `nginx:1.25-alpine`
3. Verify `portal-green` achieves 3/3 Ready status.
4. Atomically update Service `web-portal` selector to route 100% of incoming traffic to `version: v2`.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w5d4 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_BLUE" | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: portal-blue
  namespace: ckad-w5d4
spec:
  replicas: 3
  selector:
    matchLabels:
      app: portal
      version: v1
  template:
    metadata:
      labels:
        app: portal
        version: v1
    spec:
      containers:
      - name: web
        image: nginx:1.24-alpine
---
apiVersion: v1
kind: Service
metadata:
  name: web-portal
  namespace: ckad-w5d4
spec:
  selector:
    app: portal
    version: v1
  ports:
  - port: 80
    targetPort: 80
EOF_BLUE
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W5D4: Blue-Green Cutover in ckad-w5d4..."

GREEN_READY=$(ssh controlplane 'kubectl get deploy portal-green -n ckad-w5d4 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
SVC_VERSION=$(ssh controlplane 'kubectl get svc web-portal -n ckad-w5d4 -o jsonpath="{.spec.selector.version}" 2>/dev/null || echo "v1"')

if [ "$GREEN_READY" -eq 3 ] && [ "$SVC_VERSION" == "v2" ]; then
  echo -e "\033[0;32m[PASS] Green release ready (3/3) and web-portal service switched to version=v2.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] portal-green ready: $GREEN_READY/3 | web-portal selector version: '$SVC_VERSION' (expected v2).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Blue-Green Deployment
```bash
ssh controlplane '
# 1. Deploy portal-green:
cat << "EOF_GREEN" | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: portal-green
  namespace: ckad-w5d4
spec:
  replicas: 3
  selector:
    matchLabels:
      app: portal
      version: v2
  template:
    metadata:
      labels:
        app: portal
        version: v2
    spec:
      containers:
      - name: web
        image: nginx:1.25-alpine
EOF_GREEN

kubectl rollout status deployment/portal-green -n ckad-w5d4

# 2. Patch service selector to v2:
kubectl set selector service web-portal 'version=v2' -n ckad-w5d4
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w5d4 --ignore-not-found'"""
    },
    {
        "day": 5,
        "date": "2026-11-13",
        "title": "Canary Deployment Traffic Splitting",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Deploy Canary Workload
1. In namespace `ckad-w5d5`, service `catalog-svc` routes traffic to pods with label `app=catalog`.
2. Existing baseline deployment `catalog-stable` has `4` replicas of `nginx:1.24-alpine` with labels `app=catalog,track=stable`.
3. Create Canary deployment named `catalog-canary`:
   - Replicas: `1`
   - Labels: `app=catalog,track=canary`
   - Image: `nginx:1.25-alpine`
4. Verify that total endpoints for service `catalog-svc` equals `5` (4 stable + 1 canary, 20% traffic split).""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w5d5 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_CANARY" | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: catalog-stable
  namespace: ckad-w5d5
spec:
  replicas: 4
  selector:
    matchLabels:
      app: catalog
      track: stable
  template:
    metadata:
      labels:
        app: catalog
        track: stable
    spec:
      containers:
      - name: web
        image: nginx:1.24-alpine
---
apiVersion: v1
kind: Service
metadata:
  name: catalog-svc
  namespace: ckad-w5d5
spec:
  selector:
    app: catalog
  ports:
  - port: 80
    targetPort: 80
EOF_CANARY
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W5D5: Canary Deployment in ckad-w5d5..."

CANARY_READY=$(ssh controlplane 'kubectl get deploy catalog-canary -n ckad-w5d5 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
EP_COUNT=$(ssh controlplane 'kubectl get endpoints catalog-svc -n ckad-w5d5 -o jsonpath="{.subsets[*].addresses[*].ip}" 2>/dev/null | wc -w || echo 0')

if [ "$CANARY_READY" -eq 1 ] && [ "$EP_COUNT" -eq 5 ]; then
  echo -e "\033[0;32m[PASS] catalog-canary deployed (1 replica) and catalog-svc has 5 endpoints (20% canary split).\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Canary ready: $CANARY_READY/1 | Total endpoints: $EP_COUNT (expected 5).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Canary Deployment
```bash
ssh controlplane 'cat << "EOF_DEPLOY" | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: catalog-canary
  namespace: ckad-w5d5
spec:
  replicas: 1
  selector:
    matchLabels:
      app: catalog
      track: canary
  template:
    metadata:
      labels:
        app: catalog
        track: canary
    spec:
      containers:
      - name: web
        image: nginx:1.25-alpine
EOF_DEPLOY
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w5d5 --ignore-not-found'"""
    },
    {
        "day": 6,
        "date": "2026-11-14",
        "title": "Batch Jobs, CronJobs & Concurrency Policies",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: Create Batch Job & Scheduled CronJob
1. In namespace `ckad-w5d6`, create a Job named `db-indexer`:
   - Image: `busybox:1.36`
   - Command: `["sh", "-c", "echo Indexing complete; exit 0"]`
   - `completions`: `3`
   - `parallelism`: `2`
   - `backoffLimit`: `3`
2. Create a CronJob named `log-archiver`:
   - Schedule: every 5 minutes (`*/5 * * * *`)
   - Image: `busybox:1.36`
   - Command: `["echo", "Archive completed"]`
   - `concurrencyPolicy`: `Forbid`
   - `successfulJobsHistoryLimit`: `3`
3. Verify `db-indexer` reaches 3/3 completions and `log-archiver` is active.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w5d6 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W5D6: Jobs & CronJobs in ckad-w5d6..."

COMPLETIONS=$(ssh controlplane 'kubectl get job db-indexer -n ckad-w5d6 -o jsonpath="{.status.succeeded}" 2>/dev/null || echo 0')
CRON_POLICY=$(ssh controlplane 'kubectl get cronjob log-archiver -n ckad-w5d6 -o jsonpath="{.spec.concurrencyPolicy}" 2>/dev/null || echo ""')
CRON_SCHED=$(ssh controlplane 'kubectl get cronjob log-archiver -n ckad-w5d6 -o jsonpath="{.spec.schedule}" 2>/dev/null || echo ""')

if [ "$COMPLETIONS" -eq 3 ] && [ "$CRON_POLICY" == "Forbid" ] && [[ "$CRON_SCHED" =~ "5" ]]; then
  echo -e "\033[0;32m[PASS] Job db-indexer completed 3/3 and CronJob log-archiver active with Forbid policy.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Job completions: $COMPLETIONS/3 | Cron Policy: '$CRON_POLICY' | Sched: '$CRON_SCHED'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Jobs & CronJobs
```bash
ssh controlplane 'cat << "EOF_ALL" | kubectl apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: db-indexer
  namespace: ckad-w5d6
spec:
  completions: 3
  parallelism: 2
  backoffLimit: 3
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: indexer
        image: busybox:1.36
        command: ["sh", "-c", "echo Indexing complete; exit 0"]
---
apiVersion: batch/v1
kind: CronJob
metadata:
  name: log-archiver
  namespace: ckad-w5d6
spec:
  schedule: "*/5 * * * *"
  concurrencyPolicy: Forbid
  successfulJobsHistoryLimit: 3
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
          - name: archiver
            image: busybox:1.36
            command: ["echo", "Archive completed"]
EOF_ALL
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w5d6 --ignore-not-found'"""
    }
]
