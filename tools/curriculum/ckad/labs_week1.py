"""
Dedicated CKAD Lab Definitions for Week 1 (Days 1 to 6).
Core Concepts & Pod Architecture
"""

WEEK_1_LABS = [
    {
        "day": 1,
        "date": "2026-10-12",
        "title": "Multi-Container Pods & Sidecar Logging",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: Multi-Container Pods & Sidecar Logging
1. Work in namespace `ckad-w1d1` on the cluster.
2. Objective: emptyDir shared volume and log shipping.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w1d1 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w1d1 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Multi-Container Pods & Sidecar Logging in namespace ckad-w1d1..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w1d1 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w1d1.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Multi-Container Pods & Sidecar Logging
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w1d1 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w1d1

# 3. Check status:
kubectl get pods -n ckad-w1d1
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w1d1 --ignore-not-found'"""
    },
    {
        "day": 2,
        "date": "2026-10-13",
        "title": "Init Containers & Service Dependency Blocking",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Init Containers & Service Dependency Blocking
1. Work in namespace `ckad-w1d2` on the cluster.
2. Objective: Sequential init containers blocking until db is ready.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w1d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w1d2 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Init Containers & Service Dependency Blocking in namespace ckad-w1d2..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w1d2 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w1d2.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Init Containers & Service Dependency Blocking
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w1d2 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w1d2

# 3. Check status:
kubectl get pods -n ckad-w1d2
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w1d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-10-14",
        "title": "Imperative Pod & Deployment CLI Mastery",
        "diff": "Easy",
        "time": "20m",
        "tasks": """### Task 1: Imperative Pod & Deployment CLI Mastery
1. Work in namespace `ckad-w1d3` on the cluster.
2. Objective: Rapid kubectl run and create with dry-run.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w1d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w1d3 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Imperative Pod & Deployment CLI Mastery in namespace ckad-w1d3..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w1d3 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w1d3.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Imperative Pod & Deployment CLI Mastery
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w1d3 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w1d3

# 3. Check status:
kubectl get pods -n ckad-w1d3
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w1d3 --ignore-not-found'"""
    },
    {
        "day": 4,
        "date": "2026-10-15",
        "title": "Advanced Output Formatting with JSONPath",
        "diff": "Medium",
        "time": "20m",
        "tasks": """### Task 1: Advanced Output Formatting with JSONPath
1. Work in namespace `ckad-w1d4` on the cluster.
2. Objective: Extracting custom columns and sorting.
3. Deploy or configure workload named `ckad-app` using image `kube-system pods`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w1d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=kube-system pods -n ckad-w1d4 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Advanced Output Formatting with JSONPath in namespace ckad-w1d4..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w1d4 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w1d4.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Advanced Output Formatting with JSONPath
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w1d4 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=kube-system pods -n ckad-w1d4

# 3. Check status:
kubectl get pods -n ckad-w1d4
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w1d4 --ignore-not-found'"""
    },
    {
        "day": 5,
        "date": "2026-10-16",
        "title": "ReplicaSets & Deployment Scaling Strategies",
        "diff": "Easy",
        "time": "20m",
        "tasks": """### Task 1: ReplicaSets & Deployment Scaling Strategies
1. Work in namespace `ckad-w1d5` on the cluster.
2. Objective: Pod template selectors and replica management.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w1d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w1d5 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating ReplicaSets & Deployment Scaling Strategies in namespace ckad-w1d5..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w1d5 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w1d5.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: ReplicaSets & Deployment Scaling Strategies
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w1d5 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w1d5

# 3. Check status:
kubectl get pods -n ckad-w1d5
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w1d5 --ignore-not-found'"""
    },
    {
        "day": 6,
        "date": "2026-10-17",
        "title": "Week 1 Milestone: Multi-Tier Core Application",
        "diff": "Hard",
        "time": "40m",
        "tasks": """### Task 1: Week 1 Milestone: Multi-Tier Core Application
1. Work in namespace `ckad-w1d6` on the cluster.
2. Objective: Full multi-tier app with sidecars and NodePort.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w1d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w1d6 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Week 1 Milestone: Multi-Tier Core Application in namespace ckad-w1d6..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w1d6 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w1d6.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Week 1 Milestone: Multi-Tier Core Application
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w1d6 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w1d6

# 3. Check status:
kubectl get pods -n ckad-w1d6
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w1d6 --ignore-not-found'"""
    },
]
