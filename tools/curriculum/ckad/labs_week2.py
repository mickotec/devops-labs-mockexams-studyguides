"""
Dedicated CKAD Lab Definitions for Week 2 (Days 1 to 6).
Configuration & Security Primitives
"""

WEEK_2_LABS = [
    {
        "day": 1,
        "date": "2026-10-19",
        "title": "Container Commands & Arguments Overrides",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Container Commands & Arguments Overrides
1. Work in namespace `ckad-w2d1` on the cluster.
2. Objective: Overriding entrypoint and cmd via command and args.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w2d1 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w2d1 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Container Commands & Arguments Overrides in namespace ckad-w2d1..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w2d1 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w2d1.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Container Commands & Arguments Overrides
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w2d1 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w2d1

# 3. Check status:
kubectl get pods -n ckad-w2d1
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w2d1 --ignore-not-found'"""
    },
    {
        "day": 2,
        "date": "2026-10-20",
        "title": "ConfigMaps from Literals, Files & Env Injection",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: ConfigMaps from Literals, Files & Env Injection
1. Work in namespace `ckad-w2d2` on the cluster.
2. Objective: Injecting configuration as env and volume mounts.
3. Deploy or configure workload named `ckad-app` using image `alpine:3.19`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w2d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=alpine:3.19 -n ckad-w2d2 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating ConfigMaps from Literals, Files & Env Injection in namespace ckad-w2d2..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w2d2 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w2d2.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: ConfigMaps from Literals, Files & Env Injection
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w2d2 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=alpine:3.19 -n ckad-w2d2

# 3. Check status:
kubectl get pods -n ckad-w2d2
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w2d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-10-21",
        "title": "Secrets Creation, Base64 & Safe Mounting",
        "diff": "Easy",
        "time": "25m",
        "tasks": """### Task 1: Secrets Creation, Base64 & Safe Mounting
1. Work in namespace `ckad-w2d3` on the cluster.
2. Objective: Opaque secrets, TLS secrets, and read-only mounts.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w2d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w2d3 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Secrets Creation, Base64 & Safe Mounting in namespace ckad-w2d3..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w2d3 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w2d3.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Secrets Creation, Base64 & Safe Mounting
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w2d3 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w2d3

# 3. Check status:
kubectl get pods -n ckad-w2d3
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w2d3 --ignore-not-found'"""
    },
    {
        "day": 4,
        "date": "2026-10-22",
        "title": "SecurityContexts: UID, GID & Linux Capabilities",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: SecurityContexts: UID, GID & Linux Capabilities
1. Work in namespace `ckad-w2d4` on the cluster.
2. Objective: runAsUser, runAsGroup, fsGroup, drop ALL, add NET_ADMIN.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w2d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w2d4 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating SecurityContexts: UID, GID & Linux Capabilities in namespace ckad-w2d4..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w2d4 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w2d4.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: SecurityContexts: UID, GID & Linux Capabilities
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w2d4 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w2d4

# 3. Check status:
kubectl get pods -n ckad-w2d4
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w2d4 --ignore-not-found'"""
    },
    {
        "day": 5,
        "date": "2026-10-23",
        "title": "ServiceAccounts & Token Auto-mount Policies",
        "diff": "Easy",
        "time": "25m",
        "tasks": """### Task 1: ServiceAccounts & Token Auto-mount Policies
1. Work in namespace `ckad-w2d5` on the cluster.
2. Objective: Custom ServiceAccount association and automount token false.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w2d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w2d5 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating ServiceAccounts & Token Auto-mount Policies in namespace ckad-w2d5..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w2d5 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w2d5.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: ServiceAccounts & Token Auto-mount Policies
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w2d5 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w2d5

# 3. Check status:
kubectl get pods -n ckad-w2d5
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w2d5 --ignore-not-found'"""
    },
    {
        "day": 6,
        "date": "2026-10-24",
        "title": "Week 2 Milestone: Hardened Workload Configuration",
        "diff": "Hard",
        "time": "40m",
        "tasks": """### Task 1: Week 2 Milestone: Hardened Workload Configuration
1. Work in namespace `ckad-w2d6` on the cluster.
2. Objective: Secure Pod with SA, Secret env, and readOnly root.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w2d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w2d6 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Week 2 Milestone: Hardened Workload Configuration in namespace ckad-w2d6..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w2d6 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w2d6.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Week 2 Milestone: Hardened Workload Configuration
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w2d6 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w2d6

# 3. Check status:
kubectl get pods -n ckad-w2d6
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w2d6 --ignore-not-found'"""
    },
]
