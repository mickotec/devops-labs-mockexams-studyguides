"""
Dedicated CKA Lab Definitions for Week 2 (Days 1 to 6).
"""

WEEK_2_LABS = [
    {
        "day": 1,
        "date": '2026-10-05',
        "title": 'ReplicaSets & Self-Healing Controllers',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Repair Broken ReplicaSet
A ReplicaSet named `web-replicas` in namespace `core` is failing to manage pods because its selector labels (`app=web-app`) do not match its pod template labels (`app=frontend`).
1. Inspect the manifest `/opt/k8s/replicaset-broken.yaml`.
2. Correct the selector/template label mismatch so selector matches template labels `app=web-app,tier=frontend`.
3. Set the desired replicas to `4`.
4. Apply and verify that exactly 4 pods are running.

### Task 2: Test Self-Healing Mechanism
1. Delete two of the running pods belonging to `web-replicas` using `kubectl delete pod`.
2. Confirm that the ReplicaSet controller immediately recreates replacements and keeps 4 ready replicas.

### Task 3: Scale ReplicaSet
1. Scale the `web-replicas` ReplicaSet to `6` replicas using `kubectl scale`.
2. Confirm that 6 pods are running and ready.""",
        "setup": """ssh controlplane '
kubectl delete namespace core --grace-period=0 --force 2>/dev/null || true
kubectl create namespace core
sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
cat << "EOF" > /opt/k8s/replicaset-broken.yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: web-replicas
  namespace: core
spec:
  replicas: 4
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: frontend
        tier: web
    spec:
      containers:
      - name: nginx
        image: nginx:1.25-alpine
EOF
'""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: ReplicaSet web-replicas in namespace core...${NC}"
RS_COUNT=$(ssh controlplane 'kubectl get rs web-replicas -n core -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$RS_COUNT" == "4" ] || [ "$RS_COUNT" == "6" ]; then
  echo -e "${GREEN}[PASS] ReplicaSet web-replicas has $RS_COUNT ready replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] ReplicaSet has $RS_COUNT ready replicas (expected at least 4).${NC}"
fi

echo -e "${BOLD}Checking Task 2: Pod labels and controller management...${NC}"
POD_COUNT=$(ssh controlplane 'kubectl get pods -n core -l app=web-app --no-headers 2>/dev/null | wc -l | tr -d "[:space:]"')
if [ -n "$POD_COUNT" ] && [ "$POD_COUNT" -ge 4 ]; then
  echo -e "${GREEN}[PASS] Pods matching selector app=web-app verified ($POD_COUNT running).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod selector verification failed (found $POD_COUNT pods).${NC}"
fi

echo -e "${BOLD}Checking Task 3: Scaled replicas (target: 6)...${NC}"
DESIRED=$(ssh controlplane 'kubectl get rs web-replicas -n core -o jsonpath="{.spec.replicas}" 2>/dev/null || echo "0"')
if [ "$DESIRED" == "6" ]; then
  echo -e "${GREEN}[PASS] ReplicaSet scaled to 6 replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] ReplicaSet desired replicas is $DESIRED (expected 6).${NC}"
fi""",
        "solution": """1. Fix `/opt/k8s/replicaset-broken.yaml`:
```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: web-replicas
  namespace: core
spec:
  replicas: 4
  selector:
    matchLabels:
      app: web-app
      tier: frontend
  template:
    metadata:
      labels:
        app: web-app
        tier: frontend
    spec:
      containers:
      - name: nginx
        image: nginx:1.25-alpine
```
`kubectl apply -f /opt/k8s/replicaset-broken.yaml`

2. Delete pods to observe self-healing:
`kubectl delete pod -n core -l app=web-app --now`

3. Scale to 6 replicas:
`kubectl scale rs web-replicas -n core --replicas=6`""",
        "reset": """ssh controlplane '
kubectl delete namespace core --grace-period=0 --force 2>/dev/null || true
sudo rm -rf /opt/k8s/replicaset-broken.yaml
'""",
        "cka_title": 'ReplicaSets & Self-Healing Controllers',
        "cka_diff": 'Medium',
        "cka_time": '30m',
        "cka_tasks": """### Task 1: Repair Broken ReplicaSet
A ReplicaSet named `web-replicas` in namespace `core` is failing to manage pods because its selector labels (`app=web-app`) do not match its pod template labels (`app=frontend`).
1. Inspect the manifest `/opt/k8s/replicaset-broken.yaml`.
2. Correct the selector/template label mismatch so selector matches template labels `app=web-app,tier=frontend`.
3. Set the desired replicas to `4`.
4. Apply and verify that exactly 4 pods are running.

### Task 2: Test Self-Healing Mechanism
1. Delete two of the running pods belonging to `web-replicas` using `kubectl delete pod`.
2. Confirm that the ReplicaSet controller immediately recreates replacements and keeps 4 ready replicas.

### Task 3: Scale ReplicaSet
1. Scale the `web-replicas` ReplicaSet to `6` replicas using `kubectl scale`.
2. Confirm that 6 pods are running and ready.""",
        "cka_setup": """ssh controlplane '
kubectl delete namespace core --grace-period=0 --force 2>/dev/null || true
kubectl create namespace core
sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
cat << "EOF" > /opt/k8s/replicaset-broken.yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: web-replicas
  namespace: core
spec:
  replicas: 4
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: frontend
        tier: web
    spec:
      containers:
      - name: nginx
        image: nginx:1.25-alpine
EOF
'""",
        "cka_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: ReplicaSet web-replicas in namespace core...${NC}"
RS_COUNT=$(ssh controlplane 'kubectl get rs web-replicas -n core -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$RS_COUNT" == "4" ] || [ "$RS_COUNT" == "6" ]; then
  echo -e "${GREEN}[PASS] ReplicaSet web-replicas has $RS_COUNT ready replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] ReplicaSet has $RS_COUNT ready replicas (expected at least 4).${NC}"
fi

echo -e "${BOLD}Checking Task 2: Pod labels and controller management...${NC}"
POD_COUNT=$(ssh controlplane 'kubectl get pods -n core -l app=web-app --no-headers 2>/dev/null | wc -l | tr -d "[:space:]"')
if [ -n "$POD_COUNT" ] && [ "$POD_COUNT" -ge 4 ]; then
  echo -e "${GREEN}[PASS] Pods matching selector app=web-app verified ($POD_COUNT running).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod selector verification failed (found $POD_COUNT pods).${NC}"
fi

echo -e "${BOLD}Checking Task 3: Scaled replicas (target: 6)...${NC}"
DESIRED=$(ssh controlplane 'kubectl get rs web-replicas -n core -o jsonpath="{.spec.replicas}" 2>/dev/null || echo "0"')
if [ "$DESIRED" == "6" ]; then
  echo -e "${GREEN}[PASS] ReplicaSet scaled to 6 replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] ReplicaSet desired replicas is $DESIRED (expected 6).${NC}"
fi""",
        "cka_solution": """1. Fix `/opt/k8s/replicaset-broken.yaml`:
```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: web-replicas
  namespace: core
spec:
  replicas: 4
  selector:
    matchLabels:
      app: web-app
      tier: frontend
  template:
    metadata:
      labels:
        app: web-app
        tier: frontend
    spec:
      containers:
      - name: nginx
        image: nginx:1.25-alpine
```
`kubectl apply -f /opt/k8s/replicaset-broken.yaml`

2. Delete pods to observe self-healing:
`kubectl delete pod -n core -l app=web-app --now`

3. Scale to 6 replicas:
`kubectl scale rs web-replicas -n core --replicas=6`""",
        "cka_reset": """ssh controlplane '
kubectl delete namespace core --grace-period=0 --force 2>/dev/null || true
sudo rm -rf /opt/k8s/replicaset-broken.yaml
'""",
    },
    {
        "day": 2,
        "date": '2026-10-06',
        "title": 'Deployments, Rollouts & Revisions',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Create Rolling Update Deployment
Create a deployment named `payment-app` in namespace `finance`:
- Replicas: `3`
- Image: `nginx:1.24-alpine`
- Strategy: RollingUpdate with `maxSurge: 1`, `maxUnavailable: 0`

### Task 2: Upgrade with Revision History Annotation
Update the image of `payment-app` to `nginx:1.25-alpine` and record the change cause annotation: `version 1.25 upgrade`.

### Task 3: Simulating Broken Rollout & Rollback
1. Update the image to `nginx:does-not-exist` (triggering ImagePullBackOff).
2. Check rollout status with `kubectl rollout status`.
3. Undo the rollout back to the previous stable revision using `kubectl rollout undo`.""",
        "setup": """ssh controlplane '
kubectl delete namespace finance --grace-period=0 --force 2>/dev/null || true
kubectl create namespace finance
'""",
        "verify": """SCORE=0; TOTAL=2

echo -e "${BOLD}Checking Task 1 & 2: Rolling update & image version...${NC}"
IMAGE=$(ssh controlplane 'kubectl get deploy payment-app -n finance -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo "None"')
REPLICAS=$(ssh controlplane 'kubectl get deploy payment-app -n finance -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')

if [ "$IMAGE" == "nginx:1.25-alpine" ] && [ "$REPLICAS" == "3" ]; then
  echo -e "${GREEN}[PASS] payment-app deployment rolled back to stable 1.25-alpine with 3/3 ready replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Image is '$IMAGE' (expected nginx:1.25-alpine) or readyReplicas=$REPLICAS (expected 3).${NC}"
fi

echo -e "${BOLD}Checking Task 3: Deployment strategy...${NC}"
SURGE=$(ssh controlplane 'kubectl get deploy payment-app -n finance -o jsonpath="{.spec.strategy.rollingUpdate.maxSurge}" 2>/dev/null || echo "None"')
UNAVAIL=$(ssh controlplane 'kubectl get deploy payment-app -n finance -o jsonpath="{.spec.strategy.rollingUpdate.maxUnavailable}" 2>/dev/null || echo "None"')

if [ "$SURGE" == "1" ] && [ "$UNAVAIL" == "0" ]; then
  echo -e "${GREEN}[PASS] RollingUpdate strategy verified (maxSurge=1, maxUnavailable=0).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Strategy: maxSurge=$SURGE, maxUnavailable=$UNAVAIL.${NC}"
fi""",
        "solution": """1. Create deployment:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-app
  namespace: finance
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: payment-app
  template:
    metadata:
      labels:
        app: payment-app
    spec:
      containers:
      - name: nginx
        image: nginx:1.24-alpine
```
`kubectl apply -f payment-app.yaml`

2. Upgrade image and annotate:
```bash
kubectl set image deploy/payment-app nginx=nginx:1.25-alpine -n finance
kubectl annotate deploy/payment-app -n finance kubernetes.io/change-cause="version 1.25 upgrade"
```

3. Broken rollout and undo:
```bash
kubectl set image deploy/payment-app nginx=nginx:does-not-exist -n finance
kubectl rollout undo deploy/payment-app -n finance
```""",
        "reset": "ssh controlplane 'kubectl delete namespace finance --grace-period=0 --force 2>/dev/null || true'",
        "cka_title": 'Deployments, Rollouts & Revisions',
        "cka_diff": 'Medium',
        "cka_time": '30m',
        "cka_tasks": """### Task 1: Create Rolling Update Deployment
Create a deployment named `payment-app` in namespace `finance`:
- Replicas: `3`
- Image: `nginx:1.24-alpine`
- Strategy: RollingUpdate with `maxSurge: 1`, `maxUnavailable: 0`

### Task 2: Upgrade with Revision History Annotation
Update the image of `payment-app` to `nginx:1.25-alpine` and record the change cause annotation: `version 1.25 upgrade`.

### Task 3: Simulating Broken Rollout & Rollback
1. Update the image to `nginx:does-not-exist` (triggering ImagePullBackOff).
2. Check rollout status with `kubectl rollout status`.
3. Undo the rollout back to the previous stable revision using `kubectl rollout undo`.""",
        "cka_setup": """ssh controlplane '
kubectl delete namespace finance --grace-period=0 --force 2>/dev/null || true
kubectl create namespace finance
'""",
        "cka_verify": """SCORE=0; TOTAL=2

echo -e "${BOLD}Checking Task 1 & 2: Rolling update & image version...${NC}"
IMAGE=$(ssh controlplane 'kubectl get deploy payment-app -n finance -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo "None"')
REPLICAS=$(ssh controlplane 'kubectl get deploy payment-app -n finance -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')

if [ "$IMAGE" == "nginx:1.25-alpine" ] && [ "$REPLICAS" == "3" ]; then
  echo -e "${GREEN}[PASS] payment-app deployment rolled back to stable 1.25-alpine with 3/3 ready replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Image is '$IMAGE' (expected nginx:1.25-alpine) or readyReplicas=$REPLICAS (expected 3).${NC}"
fi

echo -e "${BOLD}Checking Task 3: Deployment strategy...${NC}"
SURGE=$(ssh controlplane 'kubectl get deploy payment-app -n finance -o jsonpath="{.spec.strategy.rollingUpdate.maxSurge}" 2>/dev/null || echo "None"')
UNAVAIL=$(ssh controlplane 'kubectl get deploy payment-app -n finance -o jsonpath="{.spec.strategy.rollingUpdate.maxUnavailable}" 2>/dev/null || echo "None"')

if [ "$SURGE" == "1" ] && [ "$UNAVAIL" == "0" ]; then
  echo -e "${GREEN}[PASS] RollingUpdate strategy verified (maxSurge=1, maxUnavailable=0).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Strategy: maxSurge=$SURGE, maxUnavailable=$UNAVAIL.${NC}"
fi""",
        "cka_solution": """1. Create deployment:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-app
  namespace: finance
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: payment-app
  template:
    metadata:
      labels:
        app: payment-app
    spec:
      containers:
      - name: nginx
        image: nginx:1.24-alpine
```
`kubectl apply -f payment-app.yaml`

2. Upgrade image and annotate:
```bash
kubectl set image deploy/payment-app nginx=nginx:1.25-alpine -n finance
kubectl annotate deploy/payment-app -n finance kubernetes.io/change-cause="version 1.25 upgrade"
```

3. Broken rollout and undo:
```bash
kubectl set image deploy/payment-app nginx=nginx:does-not-exist -n finance
kubectl rollout undo deploy/payment-app -n finance
```""",
        "cka_reset": "ssh controlplane 'kubectl delete namespace finance --grace-period=0 --force 2>/dev/null || true'",
    },
    {
        "day": 3,
        "date": '2026-10-07',
        "title": 'Services: ClusterIP, NodePort & LoadBalancer',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Multi-port ClusterIP Service
Deploy a pod `backend-api` in namespace `prod` (image: `nginx:alpine`, label `app=api`).
Expose it with a ClusterIP service `api-internal` in namespace `prod`:
- Port 80 -> TargetPort 80 (name: `http`)
- Port 443 -> TargetPort 443 (name: `https`)

### Task 2: NodePort Service Exposure
Create a NodePort service `web-public` in namespace `prod` targeting pod `backend-api`:
- Port: 80, TargetPort: 80, NodePort: `31200`
- Selector: `app=api`

### Task 3: Endpoints Verification
Confirm that endpoints object `api-internal` in namespace `prod` actively lists the IP address of pod `backend-api`.""",
        "setup": """ssh controlplane '
kubectl delete namespace prod --grace-period=0 --force 2>/dev/null || true
kubectl create namespace prod
kubectl run backend-api -n prod --image=nginx:alpine --labels=app=api
'""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: ClusterIP service api-internal...${NC}"
C_TYPE=$(ssh controlplane 'kubectl get svc api-internal -n prod -o jsonpath="{.spec.type}" 2>/dev/null || echo "None"')
C_PORTS=$(ssh controlplane 'kubectl get svc api-internal -n prod -o jsonpath="{.spec.ports[*].port}" 2>/dev/null || true')
if [ "$C_TYPE" == "ClusterIP" ] && echo "$C_PORTS" | grep -qw "80" && echo "$C_PORTS" | grep -qw "443"; then
  echo -e "${GREEN}[PASS] ClusterIP service api-internal verified with ports 80 and 443.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Service api-internal: type=$C_TYPE, ports=$C_PORTS.${NC}"
fi

echo -e "${BOLD}Checking Task 2: NodePort service web-public...${NC}"
N_PORT=$(ssh controlplane 'kubectl get svc web-public -n prod -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo "0"')
if [ "$N_PORT" == "31200" ]; then
  echo -e "${GREEN}[PASS] NodePort service on port 31200 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] NodePort is $N_PORT (expected 31200).${NC}"
fi

echo -e "${BOLD}Checking Task 3: Endpoints populated...${NC}"
EP=$(ssh controlplane 'kubectl get endpoints api-internal -n prod -o jsonpath="{.subsets[0].addresses[0].ip}" 2>/dev/null || echo "None"')
POD_IP=$(ssh controlplane 'kubectl get pod backend-api -n prod -o jsonpath="{.status.podIP}" 2>/dev/null || echo "PodNone"')
if [ "$EP" != "None" ] && [ "$EP" == "$POD_IP" ]; then
  echo -e "${GREEN}[PASS] Service endpoints mapped to backend-api IP ($EP).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Endpoints IP '$EP' does not match Pod IP '$POD_IP'.${NC}"
fi""",
        "solution": """1. Multi-port ClusterIP:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: api-internal
  namespace: prod
spec:
  type: ClusterIP
  selector:
    app: api
  ports:
  - name: http
    port: 80
    targetPort: 80
  - name: https
    port: 443
    targetPort: 443
```
`kubectl apply -f api-internal.yaml`

2. NodePort:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-public
  namespace: prod
spec:
  type: NodePort
  selector:
    app: api
  ports:
  - port: 80
    targetPort: 80
    nodePort: 31200
```
`kubectl apply -f web-public.yaml`""",
        "reset": "ssh controlplane 'kubectl delete namespace prod --grace-period=0 --force 2>/dev/null || true'",
        "cka_title": 'Services: ClusterIP, NodePort & LoadBalancer',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Multi-port ClusterIP Service
Deploy a pod `backend-api` in namespace `prod` (image: `nginx:alpine`, label `app=api`).
Expose it with a ClusterIP service `api-internal` in namespace `prod`:
- Port 80 -> TargetPort 80 (name: `http`)
- Port 443 -> TargetPort 443 (name: `https`)

### Task 2: NodePort Service Exposure
Create a NodePort service `web-public` in namespace `prod` targeting pod `backend-api`:
- Port: 80, TargetPort: 80, NodePort: `31200`
- Selector: `app=api`

### Task 3: Endpoints Verification
Confirm that endpoints object `api-internal` in namespace `prod` actively lists the IP address of pod `backend-api`.""",
        "cka_setup": """ssh controlplane '
kubectl delete namespace prod --grace-period=0 --force 2>/dev/null || true
kubectl create namespace prod
kubectl run backend-api -n prod --image=nginx:alpine --labels=app=api
'""",
        "cka_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: ClusterIP service api-internal...${NC}"
C_TYPE=$(ssh controlplane 'kubectl get svc api-internal -n prod -o jsonpath="{.spec.type}" 2>/dev/null || echo "None"')
C_PORTS=$(ssh controlplane 'kubectl get svc api-internal -n prod -o jsonpath="{.spec.ports[*].port}" 2>/dev/null || true')
if [ "$C_TYPE" == "ClusterIP" ] && echo "$C_PORTS" | grep -qw "80" && echo "$C_PORTS" | grep -qw "443"; then
  echo -e "${GREEN}[PASS] ClusterIP service api-internal verified with ports 80 and 443.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Service api-internal: type=$C_TYPE, ports=$C_PORTS.${NC}"
fi

echo -e "${BOLD}Checking Task 2: NodePort service web-public...${NC}"
N_PORT=$(ssh controlplane 'kubectl get svc web-public -n prod -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo "0"')
if [ "$N_PORT" == "31200" ]; then
  echo -e "${GREEN}[PASS] NodePort service on port 31200 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] NodePort is $N_PORT (expected 31200).${NC}"
fi

echo -e "${BOLD}Checking Task 3: Endpoints populated...${NC}"
EP=$(ssh controlplane 'kubectl get endpoints api-internal -n prod -o jsonpath="{.subsets[0].addresses[0].ip}" 2>/dev/null || echo "None"')
POD_IP=$(ssh controlplane 'kubectl get pod backend-api -n prod -o jsonpath="{.status.podIP}" 2>/dev/null || echo "PodNone"')
if [ "$EP" != "None" ] && [ "$EP" == "$POD_IP" ]; then
  echo -e "${GREEN}[PASS] Service endpoints mapped to backend-api IP ($EP).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Endpoints IP '$EP' does not match Pod IP '$POD_IP'.${NC}"
fi""",
        "cka_solution": """1. Multi-port ClusterIP:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: api-internal
  namespace: prod
spec:
  type: ClusterIP
  selector:
    app: api
  ports:
  - name: http
    port: 80
    targetPort: 80
  - name: https
    port: 443
    targetPort: 443
```
`kubectl apply -f api-internal.yaml`

2. NodePort:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-public
  namespace: prod
spec:
  type: NodePort
  selector:
    app: api
  ports:
  - port: 80
    targetPort: 80
    nodePort: 31200
```
`kubectl apply -f web-public.yaml`""",
        "cka_reset": "ssh controlplane 'kubectl delete namespace prod --grace-period=0 --force 2>/dev/null || true'",
    },
    {
        "day": 4,
        "date": '2026-10-08',
        "title": 'Namespaces & DNS Resolution Inside Clusters',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Multi-Namespace Service Deployment
1. Create namespaces `frontend-ns` and `database-ns`.
2. In `database-ns`, deploy pod `mysql-db` (image: `nginx:alpine` simulating db) with label `app=db`.
3. Expose `mysql-db` as a service named `mysql-svc` in `database-ns` on port `3306` (targetPort: 80).

### Task 2: Cross-Namespace Client Pod
1. In `frontend-ns`, create pod `tester` (image: `busybox:1.36`, command `sleep 3600`).

### Task 3: Cross-Namespace DNS Verification
1. Exec into `tester` and perform an `nslookup` on the fully qualified domain name (FQDN):
   `mysql-svc.database-ns.svc.cluster.local`
2. Save the output of the DNS resolution to `/tmp/dns-record.txt` inside pod `tester`.""",
        "setup": """ssh controlplane '
kubectl delete ns frontend-ns database-ns --grace-period=0 --force 2>/dev/null || true
kubectl create ns frontend-ns
kubectl create ns database-ns
'""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Service in database-ns...${NC}"
SVC=$(ssh controlplane 'kubectl get svc mysql-svc -n database-ns -o jsonpath="{.spec.clusterIP}" 2>/dev/null || echo "None"')
if [ "$SVC" != "None" ]; then
  echo -e "${GREEN}[PASS] Service mysql-svc Active in database-ns ($SVC).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Service mysql-svc missing in database-ns.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Pod tester in frontend-ns...${NC}"
POD_STATUS=$(ssh controlplane 'kubectl get pod tester -n frontend-ns -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$POD_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Pod tester is Running in frontend-ns.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod tester status: $POD_STATUS.${NC}"
fi

echo -e "${BOLD}Checking Task 3: DNS resolution inside tester...${NC}"
DNS_OUT=$(ssh controlplane 'kubectl exec -n frontend-ns tester -- cat /tmp/dns-record.txt 2>/dev/null || true')
if echo "$DNS_OUT" | grep -q "database-ns.svc.cluster.local"; then
  echo -e "${GREEN}[PASS] Cross-namespace DNS lookup verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /tmp/dns-record.txt in tester lacks FQDN lookup.${NC}"
fi""",
        "solution": """1. Deploy database and service:
```bash
kubectl run mysql-db -n database-ns --image=nginx:alpine --labels=app=db
kubectl expose pod mysql-db -n database-ns --name=mysql-svc --port=3306 --target-port=80
```

2. Deploy tester pod:
```bash
kubectl run tester -n frontend-ns --image=busybox:1.36 -- sleep 3600
```

3. Query DNS and save record:
```bash
kubectl exec -n frontend-ns tester -- sh -c "nslookup mysql-svc.database-ns.svc.cluster.local > /tmp/dns-record.txt"
```""",
        "reset": "ssh controlplane 'kubectl delete ns frontend-ns database-ns --grace-period=0 --force 2>/dev/null || true'",
        "cka_title": 'Namespaces & DNS Resolution Inside Clusters',
        "cka_diff": 'Medium',
        "cka_time": '30m',
        "cka_tasks": """### Task 1: Multi-Namespace Service Deployment
1. Create namespaces `frontend-ns` and `database-ns`.
2. In `database-ns`, deploy pod `mysql-db` (image: `nginx:alpine` simulating db) with label `app=db`.
3. Expose `mysql-db` as a service named `mysql-svc` in `database-ns` on port `3306` (targetPort: 80).

### Task 2: Cross-Namespace Client Pod
1. In `frontend-ns`, create pod `tester` (image: `busybox:1.36`, command `sleep 3600`).

### Task 3: Cross-Namespace DNS Verification
1. Exec into `tester` and perform an `nslookup` on the fully qualified domain name (FQDN):
   `mysql-svc.database-ns.svc.cluster.local`
2. Save the output of the DNS resolution to `/tmp/dns-record.txt` inside pod `tester`.""",
        "cka_setup": """ssh controlplane '
kubectl delete ns frontend-ns database-ns --grace-period=0 --force 2>/dev/null || true
kubectl create ns frontend-ns
kubectl create ns database-ns
'""",
        "cka_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Service in database-ns...${NC}"
SVC=$(ssh controlplane 'kubectl get svc mysql-svc -n database-ns -o jsonpath="{.spec.clusterIP}" 2>/dev/null || echo "None"')
if [ "$SVC" != "None" ]; then
  echo -e "${GREEN}[PASS] Service mysql-svc Active in database-ns ($SVC).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Service mysql-svc missing in database-ns.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Pod tester in frontend-ns...${NC}"
POD_STATUS=$(ssh controlplane 'kubectl get pod tester -n frontend-ns -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$POD_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Pod tester is Running in frontend-ns.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod tester status: $POD_STATUS.${NC}"
fi

echo -e "${BOLD}Checking Task 3: DNS resolution inside tester...${NC}"
DNS_OUT=$(ssh controlplane 'kubectl exec -n frontend-ns tester -- cat /tmp/dns-record.txt 2>/dev/null || true')
if echo "$DNS_OUT" | grep -q "database-ns.svc.cluster.local"; then
  echo -e "${GREEN}[PASS] Cross-namespace DNS lookup verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /tmp/dns-record.txt in tester lacks FQDN lookup.${NC}"
fi""",
        "cka_solution": """1. Deploy database and service:
```bash
kubectl run mysql-db -n database-ns --image=nginx:alpine --labels=app=db
kubectl expose pod mysql-db -n database-ns --name=mysql-svc --port=3306 --target-port=80
```

2. Deploy tester pod:
```bash
kubectl run tester -n frontend-ns --image=busybox:1.36 -- sleep 3600
```

3. Query DNS and save record:
```bash
kubectl exec -n frontend-ns tester -- sh -c "nslookup mysql-svc.database-ns.svc.cluster.local > /tmp/dns-record.txt"
```""",
        "cka_reset": "ssh controlplane 'kubectl delete ns frontend-ns database-ns --grace-period=0 --force 2>/dev/null || true'",
    },
    {
        "day": 5,
        "date": '2026-10-09',
        "title": 'Kubectl Explain & Declarative Workflow',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Offline Schema Exploration
Using `kubectl explain`, determine the exact YAML paths for:
1. Container securityContext capabilities addition (`spec.containers.securityContext.capabilities.add`).
2. Pod termination grace period (`spec.terminationGracePeriodSeconds`).
Save both paths (one per line) to `/opt/k8s/schema-paths.txt`.

### Task 2: Declarative Manifest Validation
Construct a declarative pod manifest at `/opt/k8s/secure-pod.yaml`:
- Name: `secure-nginx`
- Namespace: `security-lab`
- Image: `nginx:alpine`
- Command: `["sleep", "3600"]`
- SecurityContext:
  - `runAsNonRoot: true`
  - `runAsUser: 10001`
  - `readOnlyRootFilesystem: false`
Apply the manifest and confirm `secure-nginx` reaches `Running` state.""",
        "setup": """ssh controlplane '
kubectl delete namespace security-lab --grace-period=0 --force 2>/dev/null || true
kubectl create namespace security-lab
sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
rm -f /opt/k8s/schema-paths.txt /opt/k8s/secure-pod.yaml
'""",
        "verify": """SCORE=0; TOTAL=2

echo -e "${BOLD}Checking Task 1: Schema paths documented...${NC}"
PATHS=$(ssh controlplane 'cat /opt/k8s/schema-paths.txt 2>/dev/null || true')
if echo "$PATHS" | grep -qi "capabilities" && echo "$PATHS" | grep -qi "terminationGracePeriodSeconds"; then
  echo -e "${GREEN}[PASS] Schema paths documented in /opt/k8s/schema-paths.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/k8s/schema-paths.txt missing or incomplete.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Declarative secure-pod...${NC}"
SEC_POD=$(ssh controlplane 'kubectl get pod secure-nginx -n security-lab -o jsonpath="{.spec.containers[0].securityContext.runAsNonRoot}" 2>/dev/null || echo "false"')
PHASE=$(ssh controlplane 'kubectl get pod secure-nginx -n security-lab -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')

if [ "$SEC_POD" == "true" ] && [ "$PHASE" == "Running" ]; then
  echo -e "${GREEN}[PASS] secure-nginx is Running with runAsNonRoot=true.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] secure-nginx: runAsNonRoot=$SEC_POD, phase=$PHASE.${NC}"
fi""",
        "solution": """1. Discover schema:
```bash
kubectl explain pod.spec.containers.securityContext.capabilities.add
kubectl explain pod.spec.terminationGracePeriodSeconds
```
Save paths:
```bash
cat << 'EOF' > /opt/k8s/schema-paths.txt
spec.containers.securityContext.capabilities.add
spec.terminationGracePeriodSeconds
EOF
```

2. Construct and apply `/opt/k8s/secure-pod.yaml`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-nginx
  namespace: security-lab
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    command: ["sleep", "3600"]
    securityContext:
      runAsNonRoot: true
      runAsUser: 10001
      readOnlyRootFilesystem: false
```
`kubectl apply -f /opt/k8s/secure-pod.yaml`""",
        "reset": """ssh controlplane '
kubectl delete namespace security-lab --grace-period=0 --force 2>/dev/null || true
rm -f /opt/k8s/schema-paths.txt /opt/k8s/secure-pod.yaml
'""",
        "cka_title": 'Kubectl Explain & Declarative Workflow',
        "cka_diff": 'Medium',
        "cka_time": '30m',
        "cka_tasks": """### Task 1: Offline Schema Exploration
Using `kubectl explain`, determine the exact YAML paths for:
1. Container securityContext capabilities addition (`spec.containers.securityContext.capabilities.add`).
2. Pod termination grace period (`spec.terminationGracePeriodSeconds`).
Save both paths (one per line) to `/opt/k8s/schema-paths.txt`.

### Task 2: Declarative Manifest Validation
Construct a declarative pod manifest at `/opt/k8s/secure-pod.yaml`:
- Name: `secure-nginx`
- Namespace: `security-lab`
- Image: `nginx:alpine`
- Command: `["sleep", "3600"]`
- SecurityContext:
  - `runAsNonRoot: true`
  - `runAsUser: 10001`
  - `readOnlyRootFilesystem: false`
Apply the manifest and confirm `secure-nginx` reaches `Running` state.""",
        "cka_setup": """ssh controlplane '
kubectl delete namespace security-lab --grace-period=0 --force 2>/dev/null || true
kubectl create namespace security-lab
sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
rm -f /opt/k8s/schema-paths.txt /opt/k8s/secure-pod.yaml
'""",
        "cka_verify": """SCORE=0; TOTAL=2

echo -e "${BOLD}Checking Task 1: Schema paths documented...${NC}"
PATHS=$(ssh controlplane 'cat /opt/k8s/schema-paths.txt 2>/dev/null || true')
if echo "$PATHS" | grep -qi "capabilities" && echo "$PATHS" | grep -qi "terminationGracePeriodSeconds"; then
  echo -e "${GREEN}[PASS] Schema paths documented in /opt/k8s/schema-paths.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/k8s/schema-paths.txt missing or incomplete.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Declarative secure-pod...${NC}"
SEC_POD=$(ssh controlplane 'kubectl get pod secure-nginx -n security-lab -o jsonpath="{.spec.containers[0].securityContext.runAsNonRoot}" 2>/dev/null || echo "false"')
PHASE=$(ssh controlplane 'kubectl get pod secure-nginx -n security-lab -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')

if [ "$SEC_POD" == "true" ] && [ "$PHASE" == "Running" ]; then
  echo -e "${GREEN}[PASS] secure-nginx is Running with runAsNonRoot=true.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] secure-nginx: runAsNonRoot=$SEC_POD, phase=$PHASE.${NC}"
fi""",
        "cka_solution": """1. Discover schema:
```bash
kubectl explain pod.spec.containers.securityContext.capabilities.add
kubectl explain pod.spec.terminationGracePeriodSeconds
```
Save paths:
```bash
cat << 'EOF' > /opt/k8s/schema-paths.txt
spec.containers.securityContext.capabilities.add
spec.terminationGracePeriodSeconds
EOF
```

2. Construct and apply `/opt/k8s/secure-pod.yaml`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-nginx
  namespace: security-lab
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    command: ["sleep", "3600"]
    securityContext:
      runAsNonRoot: true
      runAsUser: 10001
      readOnlyRootFilesystem: false
```
`kubectl apply -f /opt/k8s/secure-pod.yaml`""",
        "cka_reset": """ssh controlplane '
kubectl delete namespace security-lab --grace-period=0 --force 2>/dev/null || true
rm -f /opt/k8s/schema-paths.txt /opt/k8s/secure-pod.yaml
'""",
    },
    {
        "day": 6,
        "date": '2026-10-10',
        "title": 'Week 2 Speed Drills & Controller Triathlon',
        "diff": 'Hard (Milestone Assessment 2)',
        "time": '45m',
        "tasks": """### Milestone 2 Triathlon Tasks:
1. Create a Deployment `order-processor` with 5 replicas (image: `nginx:1.24-alpine`) in namespace `triathlon-w2`.
2. Expose it via NodePort service `order-service` on port `30500` (targetPort: 80).
3. Perform an in-place image update to `nginx:1.25-alpine`, record change-cause annotation, then rollback to revision 1.
4. Export the deployment configuration without cluster-specific fields (`uid`, `status`, `resourceVersion`) to `/opt/k8s/clean-export.yaml`.""",
        "setup": """ssh controlplane '
kubectl delete namespace triathlon-w2 --grace-period=0 --force 2>/dev/null || true
sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
rm -f /opt/k8s/clean-export.yaml
'""",
        "verify": """SCORE=0; TOTAL=4

echo -e "${BOLD}Checking Task 1: Deployment replicas in triathlon-w2...${NC}"
REPLICAS=$(ssh controlplane 'kubectl get deploy order-processor -n triathlon-w2 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$REPLICAS" == "5" ]; then
  echo -e "${GREEN}[PASS] Deployment order-processor has 5 ready replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Ready replicas: $REPLICAS (expected 5).${NC}"
fi

echo -e "${BOLD}Checking Task 2: NodePort service on 30500...${NC}"
PORT=$(ssh controlplane 'kubectl get svc order-service -n triathlon-w2 -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo "0"')
if [ "$PORT" == "30500" ]; then
  echo -e "${GREEN}[PASS] NodePort service on 30500 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] NodePort is $PORT (expected 30500).${NC}"
fi

echo -e "${BOLD}Checking Task 3: Image rolled back to 1.24-alpine...${NC}"
IMAGE=$(ssh controlplane 'kubectl get deploy order-processor -n triathlon-w2 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo "None"')
if [ "$IMAGE" == "nginx:1.24-alpine" ]; then
  echo -e "${GREEN}[PASS] Image is rolled back to nginx:1.24-alpine.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Image is $IMAGE (expected nginx:1.24-alpine).${NC}"
fi

echo -e "${BOLD}Checking Task 4: Clean YAML export...${NC}"
EXPORT=$(ssh controlplane 'cat /opt/k8s/clean-export.yaml 2>/dev/null || true')
if [ -n "$EXPORT" ] && ! echo "$EXPORT" | grep -q "resourceVersion:"; then
  echo -e "${GREEN}[PASS] Clean YAML export verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/k8s/clean-export.yaml missing or contains resourceVersion.${NC}"
fi""",
        "solution": """1. Deploy:
```bash
kubectl create ns triathlon-w2
kubectl create deploy order-processor -n triathlon-w2 --image=nginx:1.24-alpine --replicas=5
```

2. Expose NodePort:
```bash
kubectl create svc nodeport order-service -n triathlon-w2 --tcp=80:80 --node-port=30500
```
Update selector to `app=order-processor`.

3. Rollout and Rollback:
```bash
kubectl set image deploy/order-processor nginx=nginx:1.25-alpine -n triathlon-w2
kubectl rollout undo deploy/order-processor -n triathlon-w2
```

4. Export clean manifest:
```bash
kubectl get deploy order-processor -n triathlon-w2 -o yaml | grep -vE 'resourceVersion|uid|creationTimestamp|status:' > /opt/k8s/clean-export.yaml
```""",
        "reset": """ssh controlplane '
kubectl delete namespace triathlon-w2 --grace-period=0 --force 2>/dev/null || true
rm -f /opt/k8s/clean-export.yaml
'""",
        "cka_title": 'Week 2 Speed Drills & Controller Triathlon',
        "cka_diff": 'Hard (Milestone Assessment 2)',
        "cka_time": '45m',
        "cka_tasks": """### Milestone 2 Triathlon Tasks:
1. Create a Deployment `order-processor` with 5 replicas (image: `nginx:1.24-alpine`) in namespace `triathlon-w2`.
2. Expose it via NodePort service `order-service` on port `30500` (targetPort: 80).
3. Perform an in-place image update to `nginx:1.25-alpine`, record change-cause annotation, then rollback to revision 1.
4. Export the deployment configuration without cluster-specific fields (`uid`, `status`, `resourceVersion`) to `/opt/k8s/clean-export.yaml`.""",
        "cka_setup": """ssh controlplane '
kubectl delete namespace triathlon-w2 --grace-period=0 --force 2>/dev/null || true
sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
rm -f /opt/k8s/clean-export.yaml
'""",
        "cka_verify": """SCORE=0; TOTAL=4

echo -e "${BOLD}Checking Task 1: Deployment replicas in triathlon-w2...${NC}"
REPLICAS=$(ssh controlplane 'kubectl get deploy order-processor -n triathlon-w2 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$REPLICAS" == "5" ]; then
  echo -e "${GREEN}[PASS] Deployment order-processor has 5 ready replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Ready replicas: $REPLICAS (expected 5).${NC}"
fi

echo -e "${BOLD}Checking Task 2: NodePort service on 30500...${NC}"
PORT=$(ssh controlplane 'kubectl get svc order-service -n triathlon-w2 -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo "0"')
if [ "$PORT" == "30500" ]; then
  echo -e "${GREEN}[PASS] NodePort service on 30500 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] NodePort is $PORT (expected 30500).${NC}"
fi

echo -e "${BOLD}Checking Task 3: Image rolled back to 1.24-alpine...${NC}"
IMAGE=$(ssh controlplane 'kubectl get deploy order-processor -n triathlon-w2 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo "None"')
if [ "$IMAGE" == "nginx:1.24-alpine" ]; then
  echo -e "${GREEN}[PASS] Image is rolled back to nginx:1.24-alpine.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Image is $IMAGE (expected nginx:1.24-alpine).${NC}"
fi

echo -e "${BOLD}Checking Task 4: Clean YAML export...${NC}"
EXPORT=$(ssh controlplane 'cat /opt/k8s/clean-export.yaml 2>/dev/null || true')
if [ -n "$EXPORT" ] && ! echo "$EXPORT" | grep -q "resourceVersion:"; then
  echo -e "${GREEN}[PASS] Clean YAML export verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/k8s/clean-export.yaml missing or contains resourceVersion.${NC}"
fi""",
        "cka_solution": """1. Deploy:
```bash
kubectl create ns triathlon-w2
kubectl create deploy order-processor -n triathlon-w2 --image=nginx:1.24-alpine --replicas=5
```

2. Expose NodePort:
```bash
kubectl create svc nodeport order-service -n triathlon-w2 --tcp=80:80 --node-port=30500
```
Update selector to `app=order-processor`.

3. Rollout and Rollback:
```bash
kubectl set image deploy/order-processor nginx=nginx:1.25-alpine -n triathlon-w2
kubectl rollout undo deploy/order-processor -n triathlon-w2
```

4. Export clean manifest:
```bash
kubectl get deploy order-processor -n triathlon-w2 -o yaml | grep -vE 'resourceVersion|uid|creationTimestamp|status:' > /opt/k8s/clean-export.yaml
```""",
        "cka_reset": """ssh controlplane '
kubectl delete namespace triathlon-w2 --grace-period=0 --force 2>/dev/null || true
rm -f /opt/k8s/clean-export.yaml
'""",
    },
]
