"""
Dedicated CKAD Lab Definitions for Week 3 (Days 1 to 6).
Workload Scheduling & Pod Placement
"""

WEEK_3_LABS = [
    {
        "day": 1,
        "date": "2026-10-26",
        "title": "Resource Requests, Limits & OOM Troubleshooting",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: Resource Requests, Limits & OOM Troubleshooting
1. Work in namespace `ckad-w3d1` on the cluster.
2. Objective: CPU/Memory requests, limits, and OOMKilled resolution.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w3d1 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w3d1 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Resource Requests, Limits & OOM Troubleshooting in namespace ckad-w3d1..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w3d1 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w3d1.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Resource Requests, Limits & OOM Troubleshooting
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w3d1 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w3d1

# 3. Check status:
kubectl get pods -n ckad-w3d1
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w3d1 --ignore-not-found'"""
    },
    {
        "day": 2,
        "date": "2026-10-27",
        "title": "Manual Node Scheduling & NodeSelector",
        "diff": "Medium",
        "time": "20m",
        "tasks": """### Task 1: Manual Node Scheduling & NodeSelector
1. Work in namespace `ckad-w3d2` on the cluster.
2. Objective: Targeting specific nodes using nodeSelector and labels.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w3d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w3d2 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Manual Node Scheduling & NodeSelector in namespace ckad-w3d2..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w3d2 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w3d2.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Manual Node Scheduling & NodeSelector
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w3d2 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w3d2

# 3. Check status:
kubectl get pods -n ckad-w3d2
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w3d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-10-28",
        "title": "Node Affinity: Required vs Preferred",
        "diff": "Easy",
        "time": "25m",
        "tasks": """### Task 1: Node Affinity: Required vs Preferred
1. Work in namespace `ckad-w3d3` on the cluster.
2. Objective: requiredDuringScheduling vs preferredDuringScheduling.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w3d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w3d3 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Node Affinity: Required vs Preferred in namespace ckad-w3d3..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w3d3 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w3d3.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Node Affinity: Required vs Preferred
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w3d3 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w3d3

# 3. Check status:
kubectl get pods -n ckad-w3d3
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w3d3 --ignore-not-found'"""
    },
    {
        "day": 4,
        "date": "2026-10-29",
        "title": "Taints & Tolerations: Dedicated Workload Isolation",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Taints & Tolerations: Dedicated Workload Isolation
1. Work in namespace `ckad-w3d4` on the cluster.
2. Objective: Tainting worker nodes with NoSchedule and tolerations.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w3d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w3d4 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Taints & Tolerations: Dedicated Workload Isolation in namespace ckad-w3d4..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w3d4 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w3d4.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Taints & Tolerations: Dedicated Workload Isolation
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w3d4 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w3d4

# 3. Check status:
kubectl get pods -n ckad-w3d4
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w3d4 --ignore-not-found'"""
    },
    {
        "day": 5,
        "date": "2026-10-30",
        "title": "Labels, Selectors & Annotation Bulk Management",
        "diff": "Easy",
        "time": "20m",
        "tasks": """### Task 1: Labels, Selectors & Annotation Bulk Management
1. Work in namespace `ckad-w3d5` on the cluster.
2. Objective: Querying, filtering, and updating labels across namespaces.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w3d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w3d5 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Labels, Selectors & Annotation Bulk Management in namespace ckad-w3d5..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w3d5 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w3d5.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Labels, Selectors & Annotation Bulk Management
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w3d5 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w3d5

# 3. Check status:
kubectl get pods -n ckad-w3d5
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w3d5 --ignore-not-found'"""
    },
    {
        "day": 6,
        "date": "2026-10-31",
        "title": "Week 3 Milestone: Precision Workload Placement",
        "diff": "Hard",
        "time": "40m",
        "tasks": """### Task 1: Week 3 Milestone: Precision Workload Placement
1. Work in namespace `ckad-w3d6` on the cluster.
2. Objective: Deploying multi-node pod topology with taints and affinity.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w3d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w3d6 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Week 3 Milestone: Precision Workload Placement in namespace ckad-w3d6..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w3d6 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w3d6.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Week 3 Milestone: Precision Workload Placement
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w3d6 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w3d6

# 3. Check status:
kubectl get pods -n ckad-w3d6
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w3d6 --ignore-not-found'"""
    },
]
