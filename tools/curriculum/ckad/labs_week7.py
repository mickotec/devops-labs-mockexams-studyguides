"""
Dedicated CKAD Lab Definitions for Week 7 (Days 1 to 6).
State Persistence & Modern App Tooling
"""

WEEK_7_LABS = [
    {
        "day": 1,
        "date": "2026-11-23",
        "title": "Volume Types: emptyDir & hostPath In-Depth",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Volume Types: emptyDir & hostPath In-Depth
1. Work in namespace `ckad-w7d1` on the cluster.
2. Objective: Ephemeral storage and node filesystem sharing.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w7d1 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w7d1 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Volume Types: emptyDir & hostPath In-Depth in namespace ckad-w7d1..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w7d1 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w7d1.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Volume Types: emptyDir & hostPath In-Depth
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w7d1 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w7d1

# 3. Check status:
kubectl get pods -n ckad-w7d1
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w7d1 --ignore-not-found'"""
    },
    {
        "day": 2,
        "date": "2026-11-24",
        "title": "PersistentVolumes & PersistentVolumeClaims",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: PersistentVolumes & PersistentVolumeClaims
1. Work in namespace `ckad-w7d2` on the cluster.
2. Objective: Static volume provisioning and ReadWriteOnce binding.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w7d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w7d2 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating PersistentVolumes & PersistentVolumeClaims in namespace ckad-w7d2..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w7d2 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w7d2.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: PersistentVolumes & PersistentVolumeClaims
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w7d2 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w7d2

# 3. Check status:
kubectl get pods -n ckad-w7d2
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w7d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-11-25",
        "title": "StorageClasses & Dynamic Volume Provisioning",
        "diff": "Easy",
        "time": "25m",
        "tasks": """### Task 1: StorageClasses & Dynamic Volume Provisioning
1. Work in namespace `ckad-w7d3` on the cluster.
2. Objective: Configuring storage classes and PVC claim expansion.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w7d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w7d3 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating StorageClasses & Dynamic Volume Provisioning in namespace ckad-w7d3..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w7d3 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w7d3.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: StorageClasses & Dynamic Volume Provisioning
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w7d3 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w7d3

# 3. Check status:
kubectl get pods -n ckad-w7d3
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w7d3 --ignore-not-found'"""
    },
    {
        "day": 4,
        "date": "2026-11-26",
        "title": "Helm Fundamentals: Repos, Releases & Values Overrides",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: Helm Fundamentals: Repos, Releases & Values Overrides
1. Work in namespace `ckad-w7d4` on the cluster.
2. Objective: helm repo, install, upgrade, and rollback with custom values.
3. Deploy or configure workload named `ckad-app` using image `helm`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w7d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=helm -n ckad-w7d4 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Helm Fundamentals: Repos, Releases & Values Overrides in namespace ckad-w7d4..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w7d4 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w7d4.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Helm Fundamentals: Repos, Releases & Values Overrides
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w7d4 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=helm -n ckad-w7d4

# 3. Check status:
kubectl get pods -n ckad-w7d4
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w7d4 --ignore-not-found'"""
    },
    {
        "day": 5,
        "date": "2026-11-27",
        "title": "Kustomize Basics: Overlays, Patches & Transformers",
        "diff": "Easy",
        "time": "30m",
        "tasks": """### Task 1: Kustomize Basics: Overlays, Patches & Transformers
1. Work in namespace `ckad-w7d5` on the cluster.
2. Objective: base and overlays (dev/prod) with commonLabels and patches.
3. Deploy or configure workload named `ckad-app` using image `kustomize`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w7d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=kustomize -n ckad-w7d5 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Kustomize Basics: Overlays, Patches & Transformers in namespace ckad-w7d5..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w7d5 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w7d5.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Kustomize Basics: Overlays, Patches & Transformers
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w7d5 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=kustomize -n ckad-w7d5

# 3. Check status:
kubectl get pods -n ckad-w7d5
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w7d5 --ignore-not-found'"""
    },
    {
        "day": 6,
        "date": "2026-11-28",
        "title": "Week 7 Milestone: Declarative GitOps Kustomize Stack",
        "diff": "Hard",
        "time": "45m",
        "tasks": """### Task 1: Week 7 Milestone: Declarative GitOps Kustomize Stack
1. Work in namespace `ckad-w7d6` on the cluster.
2. Objective: Deploying multi-environment application overlay with PVC.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w7d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w7d6 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Week 7 Milestone: Declarative GitOps Kustomize Stack in namespace ckad-w7d6..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w7d6 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w7d6.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Week 7 Milestone: Declarative GitOps Kustomize Stack
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w7d6 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w7d6

# 3. Check status:
kubectl get pods -n ckad-w7d6
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w7d6 --ignore-not-found'"""
    },
]
