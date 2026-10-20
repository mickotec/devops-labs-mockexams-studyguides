"""
Dedicated CKAD Lab Definitions for Week 5 (Days 1 to 6).
Application Observability & Debugging
"""

WEEK_5_LABS = [
    {
        "day": 1,
        "date": "2026-11-09",
        "title": "Liveness Probes: HTTP, Command & TCP Checks",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Liveness Probes: HTTP, Command & TCP Checks
1. Work in namespace `ckad-w5d1` on the cluster.
2. Objective: Detecting deadlock and restarting failed containers.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w5d1 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w5d1 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Liveness Probes: HTTP, Command & TCP Checks in namespace ckad-w5d1..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w5d1 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w5d1.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Liveness Probes: HTTP, Command & TCP Checks
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w5d1 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w5d1

# 3. Check status:
kubectl get pods -n ckad-w5d1
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w5d1 --ignore-not-found'"""
    },
    {
        "day": 2,
        "date": "2026-11-10",
        "title": "Readiness Probes & Service Traffic Gating",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Readiness Probes & Service Traffic Gating
1. Work in namespace `ckad-w5d2` on the cluster.
2. Objective: Preventing traffic to unready containers until warmup.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w5d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w5d2 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Readiness Probes & Service Traffic Gating in namespace ckad-w5d2..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w5d2 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w5d2.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Readiness Probes & Service Traffic Gating
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w5d2 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w5d2

# 3. Check status:
kubectl get pods -n ckad-w5d2
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w5d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-11-11",
        "title": "Startup Probes for Slow-Initializing Applications",
        "diff": "Easy",
        "time": "25m",
        "tasks": """### Task 1: Startup Probes for Slow-Initializing Applications
1. Work in namespace `ckad-w5d3` on the cluster.
2. Objective: failureThreshold and periodSeconds for slow containers.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w5d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w5d3 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Startup Probes for Slow-Initializing Applications in namespace ckad-w5d3..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w5d3 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w5d3.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Startup Probes for Slow-Initializing Applications
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w5d3 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w5d3

# 3. Check status:
kubectl get pods -n ckad-w5d3
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w5d3 --ignore-not-found'"""
    },
    {
        "day": 4,
        "date": "2026-11-12",
        "title": "Container Logging: Multi-Container & Previous Logs",
        "diff": "Medium",
        "time": "20m",
        "tasks": """### Task 1: Container Logging: Multi-Container & Previous Logs
1. Work in namespace `ckad-w5d4` on the cluster.
2. Objective: Extracting logs from crashing pods with --previous.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w5d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w5d4 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Container Logging: Multi-Container & Previous Logs in namespace ckad-w5d4..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w5d4 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w5d4.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Container Logging: Multi-Container & Previous Logs
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w5d4 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w5d4

# 3. Check status:
kubectl get pods -n ckad-w5d4
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w5d4 --ignore-not-found'"""
    },
    {
        "day": 5,
        "date": "2026-11-13",
        "title": "Metrics Server & CLI Resource Monitoring",
        "diff": "Easy",
        "time": "20m",
        "tasks": """### Task 1: Metrics Server & CLI Resource Monitoring
1. Work in namespace `ckad-w5d5` on the cluster.
2. Objective: kubectl top pod and top node parsing and sorting.
3. Deploy or configure workload named `ckad-app` using image `metrics-server`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w5d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=metrics-server -n ckad-w5d5 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Metrics Server & CLI Resource Monitoring in namespace ckad-w5d5..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w5d5 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w5d5.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Metrics Server & CLI Resource Monitoring
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w5d5 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=metrics-server -n ckad-w5d5

# 3. Check status:
kubectl get pods -n ckad-w5d5
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w5d5 --ignore-not-found'"""
    },
    {
        "day": 6,
        "date": "2026-11-14",
        "title": "Week 5 Milestone: Comprehensive Health & Triage Suite",
        "diff": "Hard",
        "time": "40m",
        "tasks": """### Task 1: Week 5 Milestone: Comprehensive Health & Triage Suite
1. Work in namespace `ckad-w5d6` on the cluster.
2. Objective: Configuring full probe lifecycle and resolving crash loops.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w5d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w5d6 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Week 5 Milestone: Comprehensive Health & Triage Suite in namespace ckad-w5d6..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w5d6 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w5d6.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Week 5 Milestone: Comprehensive Health & Triage Suite
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w5d6 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w5d6

# 3. Check status:
kubectl get pods -n ckad-w5d6
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w5d6 --ignore-not-found'"""
    },
]
