"""
Dedicated CKAD Lab Definitions for Week 4 (Days 1 to 6).
Workload Controllers & Deployment Strategies
"""

WEEK_4_LABS = [
    {
        "day": 1,
        "date": "2026-11-02",
        "title": "Rolling Updates, Rollout History & Undo/Rollback",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: Rolling Updates, Rollout History & Undo/Rollback
1. Work in namespace `ckad-w4d1` on the cluster.
2. Objective: maxSurge, maxUnavailable, change-cause, and rollback.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w4d1 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w4d1 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Rolling Updates, Rollout History & Undo/Rollback in namespace ckad-w4d1..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w4d1 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w4d1.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Rolling Updates, Rollout History & Undo/Rollback
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w4d1 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w4d1

# 3. Check status:
kubectl get pods -n ckad-w4d1
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w4d1 --ignore-not-found'"""
    },
    {
        "day": 2,
        "date": "2026-11-03",
        "title": "Blue-Green Deployment Cutover Pattern",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Blue-Green Deployment Cutover Pattern
1. Work in namespace `ckad-w4d2` on the cluster.
2. Objective: Switching traffic between v1 and v2 via service selector.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w4d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w4d2 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Blue-Green Deployment Cutover Pattern in namespace ckad-w4d2..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w4d2 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w4d2.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Blue-Green Deployment Cutover Pattern
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w4d2 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w4d2

# 3. Check status:
kubectl get pods -n ckad-w4d2
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w4d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-11-04",
        "title": "Canary Deployment Strategy with Weighted Traffic",
        "diff": "Easy",
        "time": "25m",
        "tasks": """### Task 1: Canary Deployment Strategy with Weighted Traffic
1. Work in namespace `ckad-w4d3` on the cluster.
2. Objective: Splitting traffic 80/20 across stable and canary deployments.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w4d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w4d3 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Canary Deployment Strategy with Weighted Traffic in namespace ckad-w4d3..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w4d3 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w4d3.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Canary Deployment Strategy with Weighted Traffic
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w4d3 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w4d3

# 3. Check status:
kubectl get pods -n ckad-w4d3
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w4d3 --ignore-not-found'"""
    },
    {
        "day": 4,
        "date": "2026-11-05",
        "title": "Batch Jobs: Completions, Parallelism & Retries",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Batch Jobs: Completions, Parallelism & Retries
1. Work in namespace `ckad-w4d4` on the cluster.
2. Objective: Configuring job completions, parallelism, and backoffLimit.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w4d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w4d4 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Batch Jobs: Completions, Parallelism & Retries in namespace ckad-w4d4..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w4d4 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w4d4.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Batch Jobs: Completions, Parallelism & Retries
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w4d4 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w4d4

# 3. Check status:
kubectl get pods -n ckad-w4d4
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w4d4 --ignore-not-found'"""
    },
    {
        "day": 5,
        "date": "2026-11-06",
        "title": "CronJobs: Schedule Syntax & Concurrency Policies",
        "diff": "Easy",
        "time": "25m",
        "tasks": """### Task 1: CronJobs: Schedule Syntax & Concurrency Policies
1. Work in namespace `ckad-w4d5` on the cluster.
2. Objective: ConcurrencyPolicy Forbid, history limits, and schedules.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w4d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w4d5 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CronJobs: Schedule Syntax & Concurrency Policies in namespace ckad-w4d5..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w4d5 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w4d5.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: CronJobs: Schedule Syntax & Concurrency Policies
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w4d5 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w4d5

# 3. Check status:
kubectl get pods -n ckad-w4d5
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w4d5 --ignore-not-found'"""
    },
    {
        "day": 6,
        "date": "2026-11-07",
        "title": "Week 4 Milestone: Resilient Canary & Scheduled Jobs",
        "diff": "Hard",
        "time": "40m",
        "tasks": """### Task 1: Week 4 Milestone: Resilient Canary & Scheduled Jobs
1. Work in namespace `ckad-w4d6` on the cluster.
2. Objective: Production canary release and automated database cleaner.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w4d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w4d6 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Week 4 Milestone: Resilient Canary & Scheduled Jobs in namespace ckad-w4d6..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w4d6 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w4d6.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Week 4 Milestone: Resilient Canary & Scheduled Jobs
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w4d6 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w4d6

# 3. Check status:
kubectl get pods -n ckad-w4d6
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w4d6 --ignore-not-found'"""
    },
]
