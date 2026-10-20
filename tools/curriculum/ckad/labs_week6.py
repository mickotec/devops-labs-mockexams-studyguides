"""
Dedicated CKAD Lab Definitions for Week 6 (Days 1 to 6).
Services & Advanced Networking
"""

WEEK_6_LABS = [
    {
        "day": 1,
        "date": "2026-11-16",
        "title": "Services: ClusterIP, NodePort & TargetPort Matching",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Services: ClusterIP, NodePort & TargetPort Matching
1. Work in namespace `ckad-w6d1` on the cluster.
2. Objective: Exposing pods and validating endpoints.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w6d1 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w6d1 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Services: ClusterIP, NodePort & TargetPort Matching in namespace ckad-w6d1..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w6d1 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w6d1.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Services: ClusterIP, NodePort & TargetPort Matching
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w6d1 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w6d1

# 3. Check status:
kubectl get pods -n ckad-w6d1
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w6d1 --ignore-not-found'"""
    },
    {
        "day": 2,
        "date": "2026-11-17",
        "title": "Headless Services & StatefulSets Architecture",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: Headless Services & StatefulSets Architecture
1. Work in namespace `ckad-w6d2` on the cluster.
2. Objective: clusterIP None with stable network identities.
3. Deploy or configure workload named `ckad-app` using image `redis:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w6d2 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=redis:alpine -n ckad-w6d2 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Headless Services & StatefulSets Architecture in namespace ckad-w6d2..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w6d2 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w6d2.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Headless Services & StatefulSets Architecture
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w6d2 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=redis:alpine -n ckad-w6d2

# 3. Check status:
kubectl get pods -n ckad-w6d2
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w6d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-11-18",
        "title": "NetworkPolicy: Ingress Isolation & Pod Selectors",
        "diff": "Easy",
        "time": "30m",
        "tasks": """### Task 1: NetworkPolicy: Ingress Isolation & Pod Selectors
1. Work in namespace `ckad-w6d3` on the cluster.
2. Objective: Restricting incoming traffic to database pods.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w6d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w6d3 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating NetworkPolicy: Ingress Isolation & Pod Selectors in namespace ckad-w6d3..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w6d3 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w6d3.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: NetworkPolicy: Ingress Isolation & Pod Selectors
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w6d3 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w6d3

# 3. Check status:
kubectl get pods -n ckad-w6d3
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w6d3 --ignore-not-found'"""
    },
    {
        "day": 4,
        "date": "2026-11-19",
        "title": "NetworkPolicy: Egress Lockdown & DNS Resolution",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: NetworkPolicy: Egress Lockdown & DNS Resolution
1. Work in namespace `ckad-w6d4` on the cluster.
2. Objective: Default deny egress while allowing CoreDNS port 53.
3. Deploy or configure workload named `ckad-app` using image `busybox:1.36`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w6d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=busybox:1.36 -n ckad-w6d4 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating NetworkPolicy: Egress Lockdown & DNS Resolution in namespace ckad-w6d4..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w6d4 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w6d4.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: NetworkPolicy: Egress Lockdown & DNS Resolution
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w6d4 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=busybox:1.36 -n ckad-w6d4

# 3. Check status:
kubectl get pods -n ckad-w6d4
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w6d4 --ignore-not-found'"""
    },
    {
        "day": 5,
        "date": "2026-11-20",
        "title": "Ingress Networking: Host, Path Rules & Rewrite Target",
        "diff": "Easy",
        "time": "30m",
        "tasks": """### Task 1: Ingress Networking: Host, Path Rules & Rewrite Target
1. Work in namespace `ckad-w6d5` on the cluster.
2. Objective: Ingress controller routing /app and /api with rewrite.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w6d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w6d5 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Ingress Networking: Host, Path Rules & Rewrite Target in namespace ckad-w6d5..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w6d5 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w6d5.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Ingress Networking: Host, Path Rules & Rewrite Target
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w6d5 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w6d5

# 3. Check status:
kubectl get pods -n ckad-w6d5
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w6d5 --ignore-not-found'"""
    },
    {
        "day": 6,
        "date": "2026-11-21",
        "title": "Week 6 Milestone: Microservices Network Security Sandbox",
        "diff": "Hard",
        "time": "45m",
        "tasks": """### Task 1: Week 6 Milestone: Microservices Network Security Sandbox
1. Work in namespace `ckad-w6d6` on the cluster.
2. Objective: Securing multi-tier application with NetworkPolicies & Ingress.
3. Deploy or configure workload named `ckad-app` using image `nginx:alpine`.
4. Ensure all pods are in `Running` state (Ready) and meet specifications.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w6d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl run ckad-app --image=nginx:alpine -n ckad-w6d6 --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating Week 6 Milestone: Microservices Network Security Sandbox in namespace ckad-w6d6..."
READY=$(ssh controlplane 'kubectl get pods -n ckad-w6d6 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Missing"')
if [ "$READY" == "Running" ]; then
  echo -e "\\033[0;32m[PASS] Workload ckad-app is Running successfully in ckad-w6d6.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Workload ckad-app status is '$READY' (expected Running).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Week 6 Milestone: Microservices Network Security Sandbox
```bash
# 1. Create or verify namespace:
kubectl create namespace ckad-w6d6 --dry-run=client -o yaml | kubectl apply -f -

# 2. Run workload:
kubectl run ckad-app --image=nginx:alpine -n ckad-w6d6

# 3. Check status:
kubectl get pods -n ckad-w6d6
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w6d6 --ignore-not-found'"""
    },
]
