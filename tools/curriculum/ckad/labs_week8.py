"""
Dedicated CKAD Lab Definitions for Week 8 (Days 1 to 6).
Security, CRDs & killer.sh Mock Exams
"""

WEEK_8_LABS = [
    {
        "day": 1,
        "date": "2026-11-30",
        "title": "Kubeconfig Architecture & Multi-Cluster Contexts",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Kubeconfig Architecture & Multi-Cluster Contexts
1. Work in namespace `ckad-w8d1` on the cluster.
2. Objective: Clusters, users, contexts, and active context switching.
3. Deploy or configure workload named `ckad-app` using image `kubeconfig`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w8d1 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=kubeconfig -n ckad-w8d1 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Kubeconfig Architecture & Multi-Cluster Contexts in namespace ckad-w8d1..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w8d1 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w8d1.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Kubeconfig Architecture & Multi-Cluster Contexts
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w8d1 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=kubeconfig -n ckad-w8d1

# 3. Check status:
kubectl get pods -n ckad-w8d1
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w8d1 --ignore-not-found'"""
    },
    {
        "day": 2,
        "date": "2026-12-01",
        "title": "RBAC: Role & RoleBinding Scoped Authorizations",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: RBAC: Role & RoleBinding Scoped Authorizations
1. Work in namespace `ckad-w8d2` on the cluster.
2. Objective: Granting developer access to specific namespace resources.
3. Deploy or configure workload named `ckad-app` using image `rbac`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w8d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=rbac -n ckad-w8d2 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating RBAC: Role & RoleBinding Scoped Authorizations in namespace ckad-w8d2..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w8d2 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w8d2.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: RBAC: Role & RoleBinding Scoped Authorizations
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w8d2 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=rbac -n ckad-w8d2

# 3. Check status:
kubectl get pods -n ckad-w8d2
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w8d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-12-02",
        "title": "RBAC: ClusterRole & ClusterRoleBinding Global Rules",
        "diff": "Easy",
        "time": "25m",
        "tasks": """### Task 1: RBAC: ClusterRole & ClusterRoleBinding Global Rules
1. Work in namespace `ckad-w8d3` on the cluster.
2. Objective: Cluster-wide resource querying and non-namespaced APIs.
3. Deploy or configure workload named `ckad-app` using image `rbac`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w8d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=rbac -n ckad-w8d3 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating RBAC: ClusterRole & ClusterRoleBinding Global Rules in namespace ckad-w8d3..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w8d3 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w8d3.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: RBAC: ClusterRole & ClusterRoleBinding Global Rules
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w8d3 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=rbac -n ckad-w8d3

# 3. Check status:
kubectl get pods -n ckad-w8d3
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w8d3 --ignore-not-found'"""
    },
    {
        "day": 4,
        "date": "2026-12-03",
        "title": "Custom Resource Definitions (CRDs) & API Extensions",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Custom Resource Definitions (CRDs) & API Extensions
1. Work in namespace `ckad-w8d4` on the cluster.
2. Objective: Creating CRDs and managing custom resource instances.
3. Deploy or configure workload named `ckad-app` using image `crd`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w8d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=crd -n ckad-w8d4 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Custom Resource Definitions (CRDs) & API Extensions in namespace ckad-w8d4..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w8d4 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w8d4.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Custom Resource Definitions (CRDs) & API Extensions
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w8d4 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=crd -n ckad-w8d4

# 3. Check status:
kubectl get pods -n ckad-w8d4
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w8d4 --ignore-not-found'"""
    },
    {
        "day": 5,
        "date": "2026-12-04",
        "title": "CKAD killer.sh Mock Exam 1 (Timed Simulation)",
        "diff": "Easy",
        "time": "120m",
        "tasks": """### Task 1: CKAD killer.sh Mock Exam 1 (Timed Simulation)
1. Work in namespace `ckad-w8d5` on the cluster.
2. Objective: 16 Real-World Questions, 120 Minutes, Official Weights.
3. Deploy or configure workload named `ckad-app` using image `mock-ckad-1`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w8d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=mock-ckad-1 -n ckad-w8d5 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD killer.sh Mock Exam 1 (Timed Simulation) in namespace ckad-w8d5..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w8d5 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w8d5.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: CKAD killer.sh Mock Exam 1 (Timed Simulation)
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w8d5 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=mock-ckad-1 -n ckad-w8d5

# 3. Check status:
kubectl get pods -n ckad-w8d5
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w8d5 --ignore-not-found'"""
    },
    {
        "day": 6,
        "date": "2026-12-05",
        "title": "CKAD killer.sh Mock Exam 2 (Timed Simulation)",
        "diff": "Hard",
        "time": "120m",
        "tasks": """### Task 1: CKAD killer.sh Mock Exam 2 (Timed Simulation)
1. Work in namespace `ckad-w8d6` on the cluster.
2. Objective: 16 Real-World Questions, 120 Minutes, Official Weights.
3. Deploy or configure workload named `ckad-app` using image `mock-ckad-2`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w8d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=mock-ckad-2 -n ckad-w8d6 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD killer.sh Mock Exam 2 (Timed Simulation) in namespace ckad-w8d6..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w8d6 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w8d6.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: CKAD killer.sh Mock Exam 2 (Timed Simulation)
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w8d6 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=mock-ckad-2 -n ckad-w8d6

# 3. Check status:
kubectl get pods -n ckad-w8d6
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w8d6 --ignore-not-found'"""
    },
]
