"""
Dedicated CKAD Lab Definitions for Week 6 (Days 1 to 6).
Aligned with KodeKloud CKAD Learning Modules: Services & Networking
"""

WEEK_6_LABS = [
    {
        "day": 1,
        "date": "2026-11-16",
        "title": "Services: ClusterIP, NodePort & Port Mapping",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Expose Deployments with ClusterIP & NodePort
1. In namespace `ckad-w6d1`, deploy `backend-deploy` (image `redis:alpine`, 2 replicas) and `frontend-deploy` (image `nginx:alpine`, 2 replicas).
2. Create a ClusterIP Service named `backend-svc` exposing `backend-deploy` on port `6379` mapping to targetPort `6379`.
3. Create a NodePort Service named `frontend-svc` exposing `frontend-deploy` on port `80`, mapping to targetPort `80`, with `nodePort: 30080`.
4. Verify both services are registered with active endpoints.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w6d1 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W6D1: Services & NodePort in ckad-w6d1..."

BACKEND_TYPE=$(ssh controlplane 'kubectl get svc backend-svc -n ckad-w6d1 -o jsonpath="{.spec.type}" 2>/dev/null || echo ""')
FRONTEND_TYPE=$(ssh controlplane 'kubectl get svc frontend-svc -n ckad-w6d1 -o jsonpath="{.spec.type}" 2>/dev/null || echo ""')
FRONTEND_NP=$(ssh controlplane 'kubectl get svc frontend-svc -n ckad-w6d1 -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo 0')

if [ "$BACKEND_TYPE" == "ClusterIP" ] && [ "$FRONTEND_TYPE" == "NodePort" ] && [ "$FRONTEND_NP" -eq 30080 ]; then
  echo -e "\033[0;32m[PASS] backend-svc (ClusterIP) and frontend-svc (NodePort: 30080) created successfully.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] backend type: '$BACKEND_TYPE' | frontend type: '$FRONTEND_TYPE' | nodePort: $FRONTEND_NP\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Services
```bash
ssh controlplane '
# 1. Deploy workloads:
kubectl create deployment backend-deploy --image=redis:alpine --replicas=2 -n ckad-w6d1
kubectl create deployment frontend-deploy --image=nginx:alpine --replicas=2 -n ckad-w6d1

# 2. Expose backend as ClusterIP:
kubectl expose deployment backend-deploy --name=backend-svc --port=6379 --target-port=6379 -n ckad-w6d1

# 3. Expose frontend as NodePort 30080:
cat << "EOF_NP" | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: frontend-svc
  namespace: ckad-w6d1
spec:
  type: NodePort
  selector:
    app: frontend-deploy
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30080
EOF_NP
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w6d1 --ignore-not-found'"""
    },
    {
        "day": 2,
        "date": "2026-11-17",
        "title": "Headless Services & Direct Pod Discovery",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Create Headless Service for Clustered Pods
1. In namespace `ckad-w6d2`, deploy two pods named `db-node-0` and `db-node-1` with labels `app=database` using image `redis:alpine`.
2. Create a Headless Service named `db-headless` (`clusterIP: None`):
   - Selector: `app=database`
   - Port: `6379`
   - TargetPort: `6379`
3. Verify `clusterIP` is set to `None` and running `nslookup db-headless.ckad-w6d2.svc.cluster.local` returns both pod IPs.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w6d2 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W6D2: Headless Service in ckad-w6d2..."

CIP=$(ssh controlplane 'kubectl get svc db-headless -n ckad-w6d2 -o jsonpath="{.spec.clusterIP}" 2>/dev/null || echo "not-found"')
EP_COUNT=$(ssh controlplane 'kubectl get endpoints db-headless -n ckad-w6d2 -o jsonpath="{.subsets[*].addresses[*].ip}" 2>/dev/null | wc -w || echo 0')

if [ "$CIP" == "None" ] && [ "$EP_COUNT" -eq 2 ]; then
  echo -e "\033[0;32m[PASS] Headless service db-headless (clusterIP: None) successfully tracking 2 pod endpoints.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] clusterIP: '$CIP' (expected None) | Endpoint count: $EP_COUNT (expected 2).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Headless Service
```bash
ssh controlplane '
kubectl run db-node-0 --image=redis:alpine -n ckad-w6d2 -l app=database
kubectl run db-node-1 --image=redis:alpine -n ckad-w6d2 -l app=database

cat << "EOF_HL" | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: db-headless
  namespace: ckad-w6d2
spec:
  clusterIP: None
  selector:
    app: database
  ports:
  - port: 6379
    targetPort: 6379
EOF_HL
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w6d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-11-18",
        "title": "NetworkPolicies: Default Ingress Denial",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Isolate Namespace with Default-Deny
1. In namespace `ckad-w6d3`, deploy Pod `secure-db` running `redis:alpine` exposed by service `db-svc:6379`.
2. Create a NetworkPolicy named `default-deny-ingress`:
   - Match all pods in namespace `ckad-w6d3` (`podSelector: {}`).
   - `policyTypes`: `[Ingress]`.
   - Leave `ingress` rules empty to deny all incoming connections.
3. Verify policy is created and inspect policy types using `kubectl describe netpol`.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w6d3 --dry-run=client -o yaml | kubectl apply -f -
kubectl run secure-db --image=redis:alpine -n ckad-w6d3 -l app=db
kubectl expose pod secure-db -n ckad-w6d3 --name=db-svc --port=6379
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W6D3: Default Deny NetworkPolicy in ckad-w6d3..."

TYPES=$(ssh controlplane 'kubectl get netpol default-deny-ingress -n ckad-w6d3 -o jsonpath="{.spec.policyTypes[*]}" 2>/dev/null || echo ""')
RULES=$(ssh controlplane 'kubectl get netpol default-deny-ingress -n ckad-w6d3 -o jsonpath="{.spec.ingress}" 2>/dev/null || echo "NONE"')

if [[ "$TYPES" =~ "Ingress" ]] && [ "$RULES" == "NONE" -o "$RULES" == "[]" ]; then
  echo -e "\033[0;32m[PASS] default-deny-ingress NetworkPolicy active with empty ingress rule (default-deny).\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] policyTypes: '$TYPES' | ingress rules: '$RULES'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Default Deny Ingress
```bash
ssh controlplane 'cat << "EOF_NP" | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: ckad-w6d3
spec:
  podSelector: {}
  policyTypes:
  - Ingress
EOF_NP
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w6d3 --ignore-not-found'"""
    },
    {
        "day": 4,
        "date": "2026-11-19",
        "title": "NetworkPolicies: Pod & Port Specific Ingress Rules",
        "diff": "Hard",
        "time": "30m",
        "tasks": """### Task 1: Allow Ingress Only From Authorized Pod
1. In namespace `ckad-w6d4`, target pod `api-backend` has label `tier=backend`.
2. Create a NetworkPolicy named `allow-frontend-only`:
   - Apply policy to pods matching `tier=backend`.
   - `policyTypes`: `[Ingress]`.
   - Allow ingress traffic ONLY from pods in the same namespace matching label `tier=frontend`.
   - Restrict allowed port strictly to TCP port `8080`.
3. Verify that all other pods are blocked from accessing `api-backend` on port `8080`.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w6d4 --dry-run=client -o yaml | kubectl apply -f -
kubectl run api-backend --image=nginx:alpine -n ckad-w6d4 -l tier=backend
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W6D4: Pod Ingress Rules in ckad-w6d4..."

TARGET=$(ssh controlplane 'kubectl get netpol allow-frontend-only -n ckad-w6d4 -o jsonpath="{.spec.podSelector.matchLabels.tier}" 2>/dev/null || echo ""')
ALLOW_TIER=$(ssh controlplane 'kubectl get netpol allow-frontend-only -n ckad-w6d4 -o jsonpath="{.spec.ingress[*].from[*].podSelector.matchLabels.tier}" 2>/dev/null || echo ""')
PORT=$(ssh controlplane 'kubectl get netpol allow-frontend-only -n ckad-w6d4 -o jsonpath="{.spec.ingress[*].ports[*].port}" 2>/dev/null || echo 0')

if [ "$TARGET" == "backend" ] && [ "$ALLOW_TIER" == "frontend" ] && [ "$PORT" -eq 8080 ]; then
  echo -e "\033[0;32m[PASS] NetworkPolicy allow-frontend-only correctly permits tier=frontend on TCP 8080.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Target tier: '$TARGET' | Allow tier: '$ALLOW_TIER' | Port: $PORT\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Fine-Grained NetworkPolicy
```bash
ssh controlplane 'cat << "EOF_NP" | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-only
  namespace: ckad-w6d4
spec:
  podSelector:
    matchLabels:
      tier: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          tier: frontend
    ports:
    - protocol: TCP
      port: 8080
EOF_NP
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w6d4 --ignore-not-found'"""
    },
    {
        "day": 5,
        "date": "2026-11-20",
        "title": "Ingress Networking: Host & Path Routing",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Configure Multi-Path Ingress Resource
1. In namespace `ckad-w6d5`, deploy services `orders-svc` (port 8080) and `catalog-svc` (port 8080).
2. Create an Ingress named `ecommerce-ingress`:
   - Host: `store.internal`
   - Path `/orders` (Prefix) routing to service `orders-svc:8080`
   - Path `/catalog` (Prefix) routing to service `catalog-svc:8080`
3. Verify the Ingress routes both paths to the corresponding services.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w6d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl create deployment orders-dep --image=nginx:alpine --replicas=1 -n ckad-w6d5
kubectl expose deployment orders-dep --name=orders-svc --port=8080 --target-port=80 -n ckad-w6d5

kubectl create deployment catalog-dep --image=nginx:alpine --replicas=1 -n ckad-w6d5
kubectl expose deployment catalog-dep --name=catalog-svc --port=8080 --target-port=80 -n ckad-w6d5
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W6D5: Ingress Routing in ckad-w6d5..."

HOST=$(ssh controlplane 'kubectl get ingress ecommerce-ingress -n ckad-w6d5 -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo ""')
PATHS=$(ssh controlplane 'kubectl get ingress ecommerce-ingress -n ckad-w6d5 -o jsonpath="{.spec.rules[0].http.paths[*].path}" 2>/dev/null || echo ""')

if [ "$HOST" == "store.internal" ] && [[ "$PATHS" =~ "/orders" ]] && [[ "$PATHS" =~ "/catalog" ]]; then
  echo -e "\033[0;32m[PASS] Ingress ecommerce-ingress successfully routes host store.internal on /orders and /catalog.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Host: '$HOST' | Paths: '$PATHS'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Ingress Routing
```bash
ssh controlplane 'cat << "EOF_ING" | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ecommerce-ingress
  namespace: ckad-w6d5
spec:
  rules:
  - host: store.internal
    http:
      paths:
      - path: /orders
        pathType: Prefix
        backend:
          service:
            name: orders-svc
            port:
              number: 8080
      - path: /catalog
        pathType: Prefix
        backend:
          service:
            name: catalog-svc
            port:
              number: 8080
EOF_ING
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w6d5 --ignore-not-found'"""
    },
    {
        "day": 6,
        "date": "2026-11-21",
        "title": "Ingress Rewrite-Target & Path Regex",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Configure URL Rewrite Annotation
1. In namespace `ckad-w6d6`, deploy backend service `service-api:80`.
2. Create Ingress `api-rewrite-ingress`:
   - Annotation: `nginx.ingress.kubernetes.io/rewrite-target: /$2`
   - Path: `/api(/|$)(.*)` with `pathType: ImplementationSpecific`
   - Backend: `service-api` on port `80`
3. Verify the rewrite-target annotation is active on the Ingress resource.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w6d6 --dry-run=client -o yaml | kubectl apply -f -
kubectl create deployment api-dep --image=nginx:alpine --replicas=1 -n ckad-w6d6
kubectl expose deployment api-dep --name=service-api --port=80 --target-port=80 -n ckad-w6d6
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W6D6: Ingress Rewrite-Target in ckad-w6d6..."

ANNO=$(ssh controlplane 'kubectl get ingress api-rewrite-ingress -n ckad-w6d6 -o jsonpath="{.metadata.annotations.nginx\.ingress\.kubernetes\.io/rewrite-target}" 2>/dev/null || echo ""')
PATH_DEF=$(ssh controlplane 'kubectl get ingress api-rewrite-ingress -n ckad-w6d6 -o jsonpath="{.spec.rules[0].http.paths[0].path}" 2>/dev/null || echo ""')

if [ "$ANNO" == "/$2" ] && [[ "$PATH_DEF" =~ "/api" ]]; then
  echo -e "\033[0;32m[PASS] api-rewrite-ingress configured with rewrite-target: /$2 and regex path.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Annotation: '$ANNO' (expected /$2) | Path: '$PATH_DEF'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Ingress Rewrite-Target
```bash
ssh controlplane 'cat << "EOF_ING" | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: api-rewrite-ingress
  namespace: ckad-w6d6
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /$2
spec:
  rules:
  - http:
      paths:
      - path: /api(/|$)(.*)
        pathType: ImplementationSpecific
        backend:
          service:
            name: service-api
            port:
              number: 80
EOF_ING
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w6d6 --ignore-not-found'"""
    }
]
