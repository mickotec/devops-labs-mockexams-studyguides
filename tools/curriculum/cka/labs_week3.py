"""
Dedicated CKA Lab Definitions for Week 3 (Days 1 to 6).
"""

WEEK_3_LABS = [
    {
        "day": 1,
        "date": '2026-10-12',
        "title": 'Manual Scheduling, Labels & Selectors',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Node Labeling
1. Add the label `disktype=ssd` to `node01`.
2. Add the label `environment=production` to `node02`.

### Task 2: Constraint-based Scheduling with nodeSelector
Create a Pod named `storage-worker` in namespace `w3d1-sched` using image `nginx:alpine`:
- It must specify a `nodeSelector` requiring `disktype: ssd`.
- Verify it is scheduled and running on `node01`.

### Task 3: Manual Scheduling via nodeName
A manifest at `/opt/k8s/orphan-pod.yaml` on `controlplane` defines a Pod named `orphan-task` in namespace `w3d1-sched` (image: `busybox:1.36`, command: `sh -c "sleep 3600"`).
- Modify the manifest to directly assign it to `node02` using `spec.nodeName: node02` (bypassing `kube-scheduler`).
- Apply the manifest and verify the pod runs on `node02`.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w3d1-sched --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d1-sched
  kubectl label node node01 disktype- 2>/dev/null || true
  kubectl label node node02 environment- 2>/dev/null || true
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  cat << "EOF" > /opt/k8s/orphan-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: orphan-task
  namespace: w3d1-sched
spec:
  containers:
  - name: sleeper
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
EOF
'""",
        "verify": """SCORE=0; TOTAL=3
# Check Task 1: labels
L1=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.metadata.labels.disktype}" 2>/dev/null || echo "None"')
L2=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.metadata.labels.environment}" 2>/dev/null || echo "None"')
if [ "$L1" == "ssd" ] && [ "$L2" == "production" ]; then
  echo -e "${GREEN}[PASS] Task 1: Node labels verified on node01 and node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Labels missing or incorrect (node01=$L1, node02=$L2).${NC}"
fi

# Check Task 2: storage-worker on node01
NODE_SW=$(ssh controlplane 'kubectl get pod storage-worker -n w3d1-sched -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
STATUS_SW=$(ssh controlplane 'kubectl get pod storage-worker -n w3d1-sched -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$NODE_SW" == "node01" ] && [ "$STATUS_SW" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: storage-worker scheduled to node01 via nodeSelector and Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: storage-worker node=$NODE_SW, status=$STATUS_SW (expected node01, Running).${NC}"
fi

# Check Task 3: orphan-task on node02
NODE_OT=$(ssh controlplane 'kubectl get pod orphan-task -n w3d1-sched -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
STATUS_OT=$(ssh controlplane 'kubectl get pod orphan-task -n w3d1-sched -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$NODE_OT" == "node02" ] && [ "$STATUS_OT" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 3: orphan-task scheduled to node02 via nodeName.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: orphan-task node=$NODE_OT, status=$STATUS_OT (expected node02, Running).${NC}"
fi""",
        "solution": """1. Label nodes:
`kubectl label node node01 disktype=ssd`
`kubectl label node node02 environment=production`

2. Deploy `storage-worker`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: storage-worker
  namespace: w3d1-sched
spec:
  nodeSelector:
    disktype: ssd
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f storage-worker.yaml`

3. Modify `/opt/k8s/orphan-pod.yaml`: add `nodeName: node02` under `spec`:
```yaml
spec:
  nodeName: node02
  containers:
  ...
```
`kubectl apply -f /opt/k8s/orphan-pod.yaml`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w3d1-sched --grace-period=0 --force 2>/dev/null || true
  kubectl label node node01 disktype- 2>/dev/null || true
  kubectl label node node02 environment- 2>/dev/null || true
  rm -rf /opt/k8s/orphan-pod.yaml
'""",
        "cka_title": 'Manual Scheduling, Labels & Selectors',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Node Labeling
1. Add the label `disktype=ssd` to `node01`.
2. Add the label `environment=production` to `node02`.

### Task 2: Constraint-based Scheduling with nodeSelector
Create a Pod named `storage-worker` in namespace `w3d1-sched` using image `nginx:alpine`:
- It must specify a `nodeSelector` requiring `disktype: ssd`.
- Verify it is scheduled and running on `node01`.

### Task 3: Manual Scheduling via nodeName
A manifest at `/opt/k8s/orphan-pod.yaml` on `controlplane` defines a Pod named `orphan-task` in namespace `w3d1-sched` (image: `busybox:1.36`, command: `sh -c "sleep 3600"`).
- Modify the manifest to directly assign it to `node02` using `spec.nodeName: node02` (bypassing `kube-scheduler`).
- Apply the manifest and verify the pod runs on `node02`.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w3d1-sched --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d1-sched
  kubectl label node node01 disktype- 2>/dev/null || true
  kubectl label node node02 environment- 2>/dev/null || true
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  cat << "EOF" > /opt/k8s/orphan-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: orphan-task
  namespace: w3d1-sched
spec:
  containers:
  - name: sleeper
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
EOF
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Check Task 1: labels
L1=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.metadata.labels.disktype}" 2>/dev/null || echo "None"')
L2=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.metadata.labels.environment}" 2>/dev/null || echo "None"')
if [ "$L1" == "ssd" ] && [ "$L2" == "production" ]; then
  echo -e "${GREEN}[PASS] Task 1: Node labels verified on node01 and node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Labels missing or incorrect (node01=$L1, node02=$L2).${NC}"
fi

# Check Task 2: storage-worker on node01
NODE_SW=$(ssh controlplane 'kubectl get pod storage-worker -n w3d1-sched -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
STATUS_SW=$(ssh controlplane 'kubectl get pod storage-worker -n w3d1-sched -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$NODE_SW" == "node01" ] && [ "$STATUS_SW" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: storage-worker scheduled to node01 via nodeSelector and Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: storage-worker node=$NODE_SW, status=$STATUS_SW (expected node01, Running).${NC}"
fi

# Check Task 3: orphan-task on node02
NODE_OT=$(ssh controlplane 'kubectl get pod orphan-task -n w3d1-sched -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
STATUS_OT=$(ssh controlplane 'kubectl get pod orphan-task -n w3d1-sched -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$NODE_OT" == "node02" ] && [ "$STATUS_OT" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 3: orphan-task scheduled to node02 via nodeName.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: orphan-task node=$NODE_OT, status=$STATUS_OT (expected node02, Running).${NC}"
fi""",
        "cka_solution": """1. Label nodes:
`kubectl label node node01 disktype=ssd`
`kubectl label node node02 environment=production`

2. Deploy `storage-worker`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: storage-worker
  namespace: w3d1-sched
spec:
  nodeSelector:
    disktype: ssd
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f storage-worker.yaml`

3. Modify `/opt/k8s/orphan-pod.yaml`: add `nodeName: node02` under `spec`:
```yaml
spec:
  nodeName: node02
  containers:
  ...
```
`kubectl apply -f /opt/k8s/orphan-pod.yaml`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w3d1-sched --grace-period=0 --force 2>/dev/null || true
  kubectl label node node01 disktype- 2>/dev/null || true
  kubectl label node node02 environment- 2>/dev/null || true
  rm -rf /opt/k8s/orphan-pod.yaml
'""",
    },
    {
        "day": 2,
        "date": '2026-10-13',
        "title": 'Taints, Tolerations & Node Affinity',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Node Tainting
Taint node `node01` with `workload=critical:NoSchedule`.

### Task 2: Tolerations
Deploy a pod named `critical-processor` in namespace `w3d2-affinity` (image: `nginx:alpine`):
- Add a toleration matching `workload=critical:NoSchedule`.
- Schedule the pod explicitly to `node01` (using `nodeSelector` or `nodeName`).
- Confirm it achieves `Running` status on `node01`.

### Task 3: Required Node Affinity
Deploy a pod named `data-collector` in namespace `w3d2-affinity` (image: `nginx:alpine`):
- Use `affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution`.
- Target nodes with label `kubernetes.io/hostname` having value `node02`.
- Confirm the pod runs on `node02`.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w3d2-affinity --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d2-affinity
  kubectl taint node node01 workload- 2>/dev/null || true
'""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: Taint on node01
TAINT=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.spec.taints[?(@.key=="workload")].value}" 2>/dev/null || echo "None"')
if [ "$TAINT" == "critical" ]; then
  echo -e "${GREEN}[PASS] Task 1: Node node01 tainted with workload=critical:NoSchedule.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Taint not found on node01.${NC}"
fi

# Task 2: critical-processor on node01
NODE_CP=$(ssh controlplane 'kubectl get pod critical-processor -n w3d2-affinity -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
STATUS_CP=$(ssh controlplane 'kubectl get pod critical-processor -n w3d2-affinity -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$NODE_CP" == "node01" ] && [ "$STATUS_CP" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: critical-processor running on tainted node01.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: critical-processor status=$STATUS_CP on node=$NODE_CP (expected Running on node01).${NC}"
fi

# Task 3: data-collector node affinity to node02
NODE_DC=$(ssh controlplane 'kubectl get pod data-collector -n w3d2-affinity -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
AFF_KEY=$(ssh controlplane 'kubectl get pod data-collector -n w3d2-affinity -o jsonpath="{.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[0].matchExpressions[0].key}" 2>/dev/null || echo "None"')
if [ "$NODE_DC" == "node02" ] && [ "$AFF_KEY" == "kubernetes.io/hostname" ]; then
  echo -e "${GREEN}[PASS] Task 3: data-collector configured with nodeAffinity running on node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: data-collector node=$NODE_DC or affinity key=$AFF_KEY incorrect.${NC}"
fi""",
        "solution": """1. Taint node01:
`kubectl taint node node01 workload=critical:NoSchedule`

2. Deploy `critical-processor`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: critical-processor
  namespace: w3d2-affinity
spec:
  nodeName: node01
  tolerations:
  - key: "workload"
    operator: "Equal"
    value: "critical"
    effect: "NoSchedule"
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f critical-processor.yaml`

3. Deploy `data-collector`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: data-collector
  namespace: w3d2-affinity
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/hostname
            operator: In
            values:
            - node02
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f data-collector.yaml`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w3d2-affinity --grace-period=0 --force 2>/dev/null || true
  kubectl taint node node01 workload- 2>/dev/null || true
'""",
        "cka_title": 'Taints, Tolerations & Node Affinity',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Node Tainting
Taint node `node01` with `workload=critical:NoSchedule`.

### Task 2: Tolerations
Deploy a pod named `critical-processor` in namespace `w3d2-affinity` (image: `nginx:alpine`):
- Add a toleration matching `workload=critical:NoSchedule`.
- Schedule the pod explicitly to `node01` (using `nodeSelector` or `nodeName`).
- Confirm it achieves `Running` status on `node01`.

### Task 3: Required Node Affinity
Deploy a pod named `data-collector` in namespace `w3d2-affinity` (image: `nginx:alpine`):
- Use `affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution`.
- Target nodes with label `kubernetes.io/hostname` having value `node02`.
- Confirm the pod runs on `node02`.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w3d2-affinity --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d2-affinity
  kubectl taint node node01 workload- 2>/dev/null || true
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: Taint on node01
TAINT=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.spec.taints[?(@.key=="workload")].value}" 2>/dev/null || echo "None"')
if [ "$TAINT" == "critical" ]; then
  echo -e "${GREEN}[PASS] Task 1: Node node01 tainted with workload=critical:NoSchedule.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Taint not found on node01.${NC}"
fi

# Task 2: critical-processor on node01
NODE_CP=$(ssh controlplane 'kubectl get pod critical-processor -n w3d2-affinity -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
STATUS_CP=$(ssh controlplane 'kubectl get pod critical-processor -n w3d2-affinity -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$NODE_CP" == "node01" ] && [ "$STATUS_CP" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: critical-processor running on tainted node01.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: critical-processor status=$STATUS_CP on node=$NODE_CP (expected Running on node01).${NC}"
fi

# Task 3: data-collector node affinity to node02
NODE_DC=$(ssh controlplane 'kubectl get pod data-collector -n w3d2-affinity -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
AFF_KEY=$(ssh controlplane 'kubectl get pod data-collector -n w3d2-affinity -o jsonpath="{.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[0].matchExpressions[0].key}" 2>/dev/null || echo "None"')
if [ "$NODE_DC" == "node02" ] && [ "$AFF_KEY" == "kubernetes.io/hostname" ]; then
  echo -e "${GREEN}[PASS] Task 3: data-collector configured with nodeAffinity running on node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: data-collector node=$NODE_DC or affinity key=$AFF_KEY incorrect.${NC}"
fi""",
        "cka_solution": """1. Taint node01:
`kubectl taint node node01 workload=critical:NoSchedule`

2. Deploy `critical-processor`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: critical-processor
  namespace: w3d2-affinity
spec:
  nodeName: node01
  tolerations:
  - key: "workload"
    operator: "Equal"
    value: "critical"
    effect: "NoSchedule"
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f critical-processor.yaml`

3. Deploy `data-collector`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: data-collector
  namespace: w3d2-affinity
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/hostname
            operator: In
            values:
            - node02
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f data-collector.yaml`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w3d2-affinity --grace-period=0 --force 2>/dev/null || true
  kubectl taint node node01 workload- 2>/dev/null || true
'""",
    },
    {
        "day": 3,
        "date": '2026-10-14',
        "title": 'Resource Requirements, Limits & LimitRanges',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Configure LimitRange
In namespace `w3d3-resources`, create a `LimitRange` named `resource-bounds`:
- Default container request: `CPU: 100m`, `Memory: 64Mi`
- Default container limit: `CPU: 200m`, `Memory: 128Mi`
- Max container limit: `CPU: 500m`, `Memory: 256Mi`

### Task 2: Deploy Bounded Workload
Deploy a pod named `bounded-service` in namespace `w3d3-resources` (image: `nginx:alpine`):
- Explicit requests: `CPU: 150m`, `Memory: 100Mi`
- Explicit limits: `CPU: 300m`, `Memory: 200Mi`
- Verify it is running.

### Task 3: Test Default Limit Injection
Deploy a pod named `unconstrained-pod` in namespace `w3d3-resources` (image: `nginx:alpine`) without any resource specs.
- Verify that the `LimitRange` automatically injected the default requests (100m/64Mi) and limits (200m/128Mi).""",
        "setup": """ssh controlplane '
  kubectl delete namespace w3d3-resources --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d3-resources
'""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: LimitRange
LR=$(ssh controlplane 'kubectl get limitrange resource-bounds -n w3d3-resources -o jsonpath="{.spec.limits[0].default.memory}" 2>/dev/null || echo "None"')
if [ "$LR" == "128Mi" ]; then
  echo -e "${GREEN}[PASS] Task 1: LimitRange resource-bounds configured with default limit 128Mi.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: LimitRange resource-bounds missing or default memory is $LR.${NC}"
fi

# Task 2: bounded-service
BS_MEM=$(ssh controlplane 'kubectl get pod bounded-service -n w3d3-resources -o jsonpath="{.spec.containers[0].resources.limits.memory}" 2>/dev/null || echo "None"')
BS_STATUS=$(ssh controlplane 'kubectl get pod bounded-service -n w3d3-resources -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$BS_MEM" == "200Mi" ] && [ "$BS_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: bounded-service has 200Mi limit and is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: bounded-service limit=$BS_MEM, status=$BS_STATUS.${NC}"
fi

# Task 3: unconstrained-pod default injection
UP_LIMIT=$(ssh controlplane 'kubectl get pod unconstrained-pod -n w3d3-resources -o jsonpath="{.spec.containers[0].resources.limits.memory}" 2>/dev/null || echo "None"')
UP_REQ=$(ssh controlplane 'kubectl get pod unconstrained-pod -n w3d3-resources -o jsonpath="{.spec.containers[0].resources.requests.memory}" 2>/dev/null || echo "None"')
if [ "$UP_LIMIT" == "128Mi" ] && [ "$UP_REQ" == "64Mi" ]; then
  echo -e "${GREEN}[PASS] Task 3: unconstrained-pod received injected defaults from LimitRange (64Mi/128Mi).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Injected values mismatch: req=$UP_REQ, limit=$UP_LIMIT.${NC}"
fi""",
        "solution": """1. Create LimitRange manifest `limitrange.yaml`:
```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: resource-bounds
  namespace: w3d3-resources
spec:
  limits:
  - default:
      cpu: 200m
      memory: 128Mi
    defaultRequest:
      cpu: 100m
      memory: 64Mi
    max:
      cpu: 500m
      memory: 256Mi
    type: Container
```
`kubectl apply -f limitrange.yaml`

2. Deploy `bounded-service`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: bounded-service
  namespace: w3d3-resources
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    resources:
      requests:
        cpu: 150m
        memory: 100Mi
      limits:
        cpu: 300m
        memory: 200Mi
```
`kubectl apply -f bounded-service.yaml`

3. Deploy `unconstrained-pod`:
`kubectl run unconstrained-pod -n w3d3-resources --image=nginx:alpine`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w3d3-resources --grace-period=0 --force 2>/dev/null || true
'""",
        "cka_title": 'Resource Requirements, Limits & LimitRanges',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Configure LimitRange
In namespace `w3d3-resources`, create a `LimitRange` named `resource-bounds`:
- Default container request: `CPU: 100m`, `Memory: 64Mi`
- Default container limit: `CPU: 200m`, `Memory: 128Mi`
- Max container limit: `CPU: 500m`, `Memory: 256Mi`

### Task 2: Deploy Bounded Workload
Deploy a pod named `bounded-service` in namespace `w3d3-resources` (image: `nginx:alpine`):
- Explicit requests: `CPU: 150m`, `Memory: 100Mi`
- Explicit limits: `CPU: 300m`, `Memory: 200Mi`
- Verify it is running.

### Task 3: Test Default Limit Injection
Deploy a pod named `unconstrained-pod` in namespace `w3d3-resources` (image: `nginx:alpine`) without any resource specs.
- Verify that the `LimitRange` automatically injected the default requests (100m/64Mi) and limits (200m/128Mi).""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w3d3-resources --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d3-resources
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: LimitRange
LR=$(ssh controlplane 'kubectl get limitrange resource-bounds -n w3d3-resources -o jsonpath="{.spec.limits[0].default.memory}" 2>/dev/null || echo "None"')
if [ "$LR" == "128Mi" ]; then
  echo -e "${GREEN}[PASS] Task 1: LimitRange resource-bounds configured with default limit 128Mi.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: LimitRange resource-bounds missing or default memory is $LR.${NC}"
fi

# Task 2: bounded-service
BS_MEM=$(ssh controlplane 'kubectl get pod bounded-service -n w3d3-resources -o jsonpath="{.spec.containers[0].resources.limits.memory}" 2>/dev/null || echo "None"')
BS_STATUS=$(ssh controlplane 'kubectl get pod bounded-service -n w3d3-resources -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$BS_MEM" == "200Mi" ] && [ "$BS_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: bounded-service has 200Mi limit and is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: bounded-service limit=$BS_MEM, status=$BS_STATUS.${NC}"
fi

# Task 3: unconstrained-pod default injection
UP_LIMIT=$(ssh controlplane 'kubectl get pod unconstrained-pod -n w3d3-resources -o jsonpath="{.spec.containers[0].resources.limits.memory}" 2>/dev/null || echo "None"')
UP_REQ=$(ssh controlplane 'kubectl get pod unconstrained-pod -n w3d3-resources -o jsonpath="{.spec.containers[0].resources.requests.memory}" 2>/dev/null || echo "None"')
if [ "$UP_LIMIT" == "128Mi" ] && [ "$UP_REQ" == "64Mi" ]; then
  echo -e "${GREEN}[PASS] Task 3: unconstrained-pod received injected defaults from LimitRange (64Mi/128Mi).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Injected values mismatch: req=$UP_REQ, limit=$UP_LIMIT.${NC}"
fi""",
        "cka_solution": """1. Create LimitRange manifest `limitrange.yaml`:
```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: resource-bounds
  namespace: w3d3-resources
spec:
  limits:
  - default:
      cpu: 200m
      memory: 128Mi
    defaultRequest:
      cpu: 100m
      memory: 64Mi
    max:
      cpu: 500m
      memory: 256Mi
    type: Container
```
`kubectl apply -f limitrange.yaml`

2. Deploy `bounded-service`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: bounded-service
  namespace: w3d3-resources
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    resources:
      requests:
        cpu: 150m
        memory: 100Mi
      limits:
        cpu: 300m
        memory: 200Mi
```
`kubectl apply -f bounded-service.yaml`

3. Deploy `unconstrained-pod`:
`kubectl run unconstrained-pod -n w3d3-resources --image=nginx:alpine`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w3d3-resources --grace-period=0 --force 2>/dev/null || true
'""",
    },
    {
        "day": 4,
        "date": '2026-10-15',
        "title": 'DaemonSets & Static Pods Architecture',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Create DaemonSet
In namespace `w3d4-ds`, create a DaemonSet named `log-collector`:
- Image: `fluent/fluent-bit:2.1.8` (or `nginx:alpine` if offline)
- Labels: `app=log-collector, tier=monitoring`
- Ensure a pod runs on all available worker nodes.

### Task 2: Create Static Pod on Worker Node
Create a Static Pod named `node02-telemetry` on node `node02`:
- Image: `nginx:alpine`
- Path: place manifest in the kubelet static pod directory (`/etc/kubernetes/manifests/node02-telemetry.yaml`)
- Verify from `controlplane` that `node02-telemetry-node02` is registered and running.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w3d4-ds --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d4-ds
'
ssh node02 '
sudo rm -f /etc/kubernetes/manifests/node02-telemetry.yaml
POD_ID=$(sudo crictl pods -q --name node02-telemetry-node02 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: DaemonSet
DESIRED=$(ssh controlplane 'kubectl get ds log-collector -n w3d4-ds -o jsonpath="{.status.desiredNumberScheduled}" 2>/dev/null || echo "0"')
READY=$(ssh controlplane 'kubectl get ds log-collector -n w3d4-ds -o jsonpath="{.status.numberReady}" 2>/dev/null || echo "0"')
if [ "$DESIRED" -ge 2 ] && [ "$DESIRED" == "$READY" ]; then
  echo -e "${GREEN}[PASS] Task 1: DaemonSet log-collector is fully scheduled ($READY/$DESIRED ready).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: DaemonSet log-collector desired=$DESIRED, ready=$READY.${NC}"
fi

# Task 2: Static pod on node02
STATIC=$(ssh controlplane 'kubectl get pods -A 2>/dev/null | grep "node02-telemetry-node02" || true')
if [ -n "$STATIC" ] && echo "$STATIC" | grep -q "Running"; then
  echo -e "${GREEN}[PASS] Task 2: Static pod node02-telemetry-node02 is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Static pod node02-telemetry-node02 not found or not Running: $STATIC.${NC}"
fi""",
        "solution": """1. Create DaemonSet `ds.yaml`:
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: log-collector
  namespace: w3d4-ds
spec:
  selector:
    matchLabels:
      app: log-collector
  template:
    metadata:
      labels:
        app: log-collector
        tier: monitoring
    spec:
      containers:
      - name: collector
        image: nginx:alpine
```
`kubectl apply -f ds.yaml`

2. On node02:
`ssh node02`
`sudo tee /etc/kubernetes/manifests/node02-telemetry.yaml << 'EOF'`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: node02-telemetry
spec:
  containers:
  - name: telemetry
    image: nginx:alpine
```
`EOF`""",
        "reset": """ssh controlplane '
kubectl delete namespace w3d4-ds --grace-period=0 --force 2>/dev/null || true
kubectl delete pod node02-telemetry-node02 --force --grace-period=0 2>/dev/null || true
'
ssh node02 '
sudo rm -f /etc/kubernetes/manifests/node02-telemetry.yaml
POD_ID=$(sudo crictl pods -q --name node02-telemetry-node02 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'""",
        "cka_title": 'DaemonSets & Static Pods Architecture',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Create DaemonSet
In namespace `w3d4-ds`, create a DaemonSet named `log-collector`:
- Image: `fluent/fluent-bit:2.1.8` (or `nginx:alpine` if offline)
- Labels: `app=log-collector, tier=monitoring`
- Ensure a pod runs on all available worker nodes.

### Task 2: Create Static Pod on Worker Node
Create a Static Pod named `node02-telemetry` on node `node02`:
- Image: `nginx:alpine`
- Path: place manifest in the kubelet static pod directory (`/etc/kubernetes/manifests/node02-telemetry.yaml`)
- Verify from `controlplane` that `node02-telemetry-node02` is registered and running.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w3d4-ds --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d4-ds
'
ssh node02 '
sudo rm -f /etc/kubernetes/manifests/node02-telemetry.yaml
POD_ID=$(sudo crictl pods -q --name node02-telemetry-node02 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'""",
        "cka_verify": """SCORE=0; TOTAL=2
# Task 1: DaemonSet
DESIRED=$(ssh controlplane 'kubectl get ds log-collector -n w3d4-ds -o jsonpath="{.status.desiredNumberScheduled}" 2>/dev/null || echo "0"')
READY=$(ssh controlplane 'kubectl get ds log-collector -n w3d4-ds -o jsonpath="{.status.numberReady}" 2>/dev/null || echo "0"')
if [ "$DESIRED" -ge 2 ] && [ "$DESIRED" == "$READY" ]; then
  echo -e "${GREEN}[PASS] Task 1: DaemonSet log-collector is fully scheduled ($READY/$DESIRED ready).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: DaemonSet log-collector desired=$DESIRED, ready=$READY.${NC}"
fi

# Task 2: Static pod on node02
STATIC=$(ssh controlplane 'kubectl get pods -A 2>/dev/null | grep "node02-telemetry-node02" || true')
if [ -n "$STATIC" ] && echo "$STATIC" | grep -q "Running"; then
  echo -e "${GREEN}[PASS] Task 2: Static pod node02-telemetry-node02 is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Static pod node02-telemetry-node02 not found or not Running: $STATIC.${NC}"
fi""",
        "cka_solution": """1. Create DaemonSet `ds.yaml`:
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: log-collector
  namespace: w3d4-ds
spec:
  selector:
    matchLabels:
      app: log-collector
  template:
    metadata:
      labels:
        app: log-collector
        tier: monitoring
    spec:
      containers:
      - name: collector
        image: nginx:alpine
```
`kubectl apply -f ds.yaml`

2. On node02:
`ssh node02`
`sudo tee /etc/kubernetes/manifests/node02-telemetry.yaml << 'EOF'`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: node02-telemetry
spec:
  containers:
  - name: telemetry
    image: nginx:alpine
```
`EOF`""",
        "cka_reset": """ssh controlplane '
kubectl delete namespace w3d4-ds --grace-period=0 --force 2>/dev/null || true
kubectl delete pod node02-telemetry-node02 --force --grace-period=0 2>/dev/null || true
'
ssh node02 '
sudo rm -f /etc/kubernetes/manifests/node02-telemetry.yaml
POD_ID=$(sudo crictl pods -q --name node02-telemetry-node02 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'""",
    },
    {
        "day": 5,
        "date": '2026-10-16',
        "title": 'Priority Classes & Multiple Schedulers',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Define PriorityClasses
1. Create a `PriorityClass` named `mission-critical` with value `1000000` and `globalDefault: false`.
2. Create a `PriorityClass` named `low-priority` with value `500` and `preemptionPolicy: Never`.

### Task 2: Workload Priority Association
In namespace `w3d5-priority`:
1. Deploy pod `critical-db` (image: `nginx:alpine`) assigned to `priorityClassName: mission-critical`.
2. Deploy pod `batch-worker` (image: `nginx:alpine`) assigned to `priorityClassName: low-priority`.
3. Verify both pods run and reflect their assigned priority values.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w3d5-priority --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d5-priority
  kubectl delete priorityclass mission-critical low-priority 2>/dev/null || true
'""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: PriorityClasses
PC_VAL1=$(ssh controlplane 'kubectl get priorityclass mission-critical -o jsonpath="{.value}" 2>/dev/null || echo "0"')
PC_VAL2=$(ssh controlplane 'kubectl get priorityclass low-priority -o jsonpath="{.value}" 2>/dev/null || echo "0"')
if [ "$PC_VAL1" == "1000000" ] && [ "$PC_VAL2" == "500" ]; then
  echo -e "${GREEN}[PASS] Task 1: PriorityClasses mission-critical and low-priority verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: PriorityClass values incorrect: critical=$PC_VAL1, low=$PC_VAL2.${NC}"
fi

# Task 2: critical-db pod
P1_NAME=$(ssh controlplane 'kubectl get pod critical-db -n w3d5-priority -o jsonpath="{.spec.priorityClassName}" 2>/dev/null || echo "None"')
P1_STATUS=$(ssh controlplane 'kubectl get pod critical-db -n w3d5-priority -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$P1_NAME" == "mission-critical" ] && [ "$P1_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: Pod critical-db assigned mission-critical priority and Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: critical-db priority=$P1_NAME, status=$P1_STATUS.${NC}"
fi

# Task 3: batch-worker pod
P2_NAME=$(ssh controlplane 'kubectl get pod batch-worker -n w3d5-priority -o jsonpath="{.spec.priorityClassName}" 2>/dev/null || echo "None"')
P2_STATUS=$(ssh controlplane 'kubectl get pod batch-worker -n w3d5-priority -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$P2_NAME" == "low-priority" ] && [ "$P2_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 3: Pod batch-worker assigned low-priority and Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: batch-worker priority=$P2_NAME, status=$P2_STATUS.${NC}"
fi""",
        "solution": """1. Create PriorityClasses:
```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: mission-critical
value: 1000000
globalDefault: false
description: "Mission critical applications"
---
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: low-priority
value: 500
preemptionPolicy: Never
globalDefault: false
```
`kubectl apply -f priorities.yaml`

2. Deploy pods with `priorityClassName`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: critical-db
  namespace: w3d5-priority
spec:
  priorityClassName: mission-critical
  containers:
  - name: nginx
    image: nginx:alpine
---
apiVersion: v1
kind: Pod
metadata:
  name: batch-worker
  namespace: w3d5-priority
spec:
  priorityClassName: low-priority
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f pods.yaml`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w3d5-priority --grace-period=0 --force 2>/dev/null || true
  kubectl delete priorityclass mission-critical low-priority 2>/dev/null || true
'""",
        "cka_title": 'Priority Classes & Multiple Schedulers',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Define PriorityClasses
1. Create a `PriorityClass` named `mission-critical` with value `1000000` and `globalDefault: false`.
2. Create a `PriorityClass` named `low-priority` with value `500` and `preemptionPolicy: Never`.

### Task 2: Workload Priority Association
In namespace `w3d5-priority`:
1. Deploy pod `critical-db` (image: `nginx:alpine`) assigned to `priorityClassName: mission-critical`.
2. Deploy pod `batch-worker` (image: `nginx:alpine`) assigned to `priorityClassName: low-priority`.
3. Verify both pods run and reflect their assigned priority values.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w3d5-priority --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3d5-priority
  kubectl delete priorityclass mission-critical low-priority 2>/dev/null || true
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: PriorityClasses
PC_VAL1=$(ssh controlplane 'kubectl get priorityclass mission-critical -o jsonpath="{.value}" 2>/dev/null || echo "0"')
PC_VAL2=$(ssh controlplane 'kubectl get priorityclass low-priority -o jsonpath="{.value}" 2>/dev/null || echo "0"')
if [ "$PC_VAL1" == "1000000" ] && [ "$PC_VAL2" == "500" ]; then
  echo -e "${GREEN}[PASS] Task 1: PriorityClasses mission-critical and low-priority verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: PriorityClass values incorrect: critical=$PC_VAL1, low=$PC_VAL2.${NC}"
fi

# Task 2: critical-db pod
P1_NAME=$(ssh controlplane 'kubectl get pod critical-db -n w3d5-priority -o jsonpath="{.spec.priorityClassName}" 2>/dev/null || echo "None"')
P1_STATUS=$(ssh controlplane 'kubectl get pod critical-db -n w3d5-priority -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$P1_NAME" == "mission-critical" ] && [ "$P1_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: Pod critical-db assigned mission-critical priority and Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: critical-db priority=$P1_NAME, status=$P1_STATUS.${NC}"
fi

# Task 3: batch-worker pod
P2_NAME=$(ssh controlplane 'kubectl get pod batch-worker -n w3d5-priority -o jsonpath="{.spec.priorityClassName}" 2>/dev/null || echo "None"')
P2_STATUS=$(ssh controlplane 'kubectl get pod batch-worker -n w3d5-priority -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$P2_NAME" == "low-priority" ] && [ "$P2_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 3: Pod batch-worker assigned low-priority and Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: batch-worker priority=$P2_NAME, status=$P2_STATUS.${NC}"
fi""",
        "cka_solution": """1. Create PriorityClasses:
```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: mission-critical
value: 1000000
globalDefault: false
description: "Mission critical applications"
---
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: low-priority
value: 500
preemptionPolicy: Never
globalDefault: false
```
`kubectl apply -f priorities.yaml`

2. Deploy pods with `priorityClassName`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: critical-db
  namespace: w3d5-priority
spec:
  priorityClassName: mission-critical
  containers:
  - name: nginx
    image: nginx:alpine
---
apiVersion: v1
kind: Pod
metadata:
  name: batch-worker
  namespace: w3d5-priority
spec:
  priorityClassName: low-priority
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f pods.yaml`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w3d5-priority --grace-period=0 --force 2>/dev/null || true
  kubectl delete priorityclass mission-critical low-priority 2>/dev/null || true
'""",
    },
    {
        "day": 6,
        "date": '2026-10-17',
        "title": 'Week 3 Scheduling Troubleshooting Matrix',
        "diff": 'Hard (Milestone Assessment 3)',
        "time": '45m',
        "tasks": """### Milestone 3 Triathlon Tasks:
A set of broken scheduling scenarios has been injected into namespace `w3-milestone`:

1. **Fix Pending Pod `stuck-selector`**:
   It is stuck in `Pending` because its `nodeSelector` requires `hardware=gpu`, which no node has. Label `node02` with `hardware=gpu` to allow it to schedule.

2. **Fix Taint Mismatch on `stuck-taint`**:
   `node01` has been tainted with `dedicated=web:NoSchedule`. Update `stuck-taint` pod manifest or recreate it with a toleration for `dedicated=web:NoSchedule` so it runs on `node01`.

3. **Control Plane DaemonSet `infra-agent`**:
   DaemonSet `infra-agent` is only running on worker nodes because control plane nodes have the default `node-role.kubernetes.io/control-plane:NoSchedule` taint. Update the DaemonSet with a toleration so it schedules an agent on `controlplane` as well.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w3-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3-milestone
  kubectl label node node02 hardware- 2>/dev/null || true
  kubectl taint node node01 dedicated=web:NoSchedule --overwrite 2>/dev/null || true

  # Pod 1: Bad selector
  cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: stuck-selector
  namespace: w3-milestone
spec:
  nodeSelector:
    hardware: gpu
  containers:
  - name: nginx
    image: nginx:alpine
EOF

  # Pod 2: Taint mismatch
  cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: stuck-taint
  namespace: w3-milestone
spec:
  nodeSelector:
    kubernetes.io/hostname: node01
  containers:
  - name: nginx
    image: nginx:alpine
EOF

  # Pod 3: DaemonSet without controlplane toleration
  cat << "EOF" | kubectl apply -f -
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: infra-agent
  namespace: w3-milestone
spec:
  selector:
    matchLabels:
      app: infra-agent
  template:
    metadata:
      labels:
        app: infra-agent
    spec:
      containers:
      - name: agent
        image: nginx:alpine
EOF
'""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: stuck-selector is Running on node02
S1=$(ssh controlplane 'kubectl get pod stuck-selector -n w3-milestone -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
N1=$(ssh controlplane 'kubectl get pod stuck-selector -n w3-milestone -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
if [ "$S1" == "Running" ] && [ "$N1" == "node02" ]; then
  echo -e "${GREEN}[PASS] Task 1: stuck-selector is Running on node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: stuck-selector status=$S1, node=$N1.${NC}"
fi

# Task 2: stuck-taint has toleration and is Running
S2=$(ssh controlplane 'kubectl get pod stuck-taint -n w3-milestone -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
TOL=$(ssh controlplane 'kubectl get pod stuck-taint -n w3-milestone -o jsonpath="{.spec.tolerations[?(@.key=="dedicated")].value}" 2>/dev/null || echo "None"')
if [ "$S2" == "Running" ] && [ "$TOL" == "web" ]; then
  echo -e "${GREEN}[PASS] Task 2: stuck-taint has toleration and is Running on node01.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: stuck-taint status=$S2, toleration=$TOL.${NC}"
fi

# Task 3: infra-agent DaemonSet running on controlplane
CP_POD=$(ssh controlplane 'kubectl get pods -n w3-milestone -l app=infra-agent --field-selector spec.nodeName=controlplane -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$CP_POD" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 3: infra-agent DaemonSet scheduled and Running on controlplane.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: infra-agent pod on controlplane is $CP_POD.${NC}"
fi""",
        "solution": """1. Label node02:
`kubectl label node node02 hardware=gpu`

2. Add toleration to `stuck-taint`:
`kubectl get pod stuck-taint -n w3-milestone -o yaml > /tmp/stuck-taint.yaml`
Add under spec:
```yaml
tolerations:
- key: dedicated
  operator: Equal
  value: web
  effect: NoSchedule
```
`kubectl replace --force -f /tmp/stuck-taint.yaml`

3. Patch DaemonSet to tolerate control plane taint:
`kubectl patch ds infra-agent -n w3-milestone --type=strategic -p '{"spec":{"template":{"spec":{"tolerations":[{"key":"node-role.kubernetes.io/control-plane","operator":"Exists","effect":"NoSchedule"}]}}}}'`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w3-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl label node node02 hardware- 2>/dev/null || true
  kubectl taint node node01 dedicated- 2>/dev/null || true
'""",
        "cka_title": 'Week 3 Scheduling Troubleshooting Matrix',
        "cka_diff": 'Hard (Milestone Assessment 3)',
        "cka_time": '45m',
        "cka_tasks": """### Milestone 3 Triathlon Tasks:
A set of broken scheduling scenarios has been injected into namespace `w3-milestone`:

1. **Fix Pending Pod `stuck-selector`**:
   It is stuck in `Pending` because its `nodeSelector` requires `hardware=gpu`, which no node has. Label `node02` with `hardware=gpu` to allow it to schedule.

2. **Fix Taint Mismatch on `stuck-taint`**:
   `node01` has been tainted with `dedicated=web:NoSchedule`. Update `stuck-taint` pod manifest or recreate it with a toleration for `dedicated=web:NoSchedule` so it runs on `node01`.

3. **Control Plane DaemonSet `infra-agent`**:
   DaemonSet `infra-agent` is only running on worker nodes because control plane nodes have the default `node-role.kubernetes.io/control-plane:NoSchedule` taint. Update the DaemonSet with a toleration so it schedules an agent on `controlplane` as well.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w3-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w3-milestone
  kubectl label node node02 hardware- 2>/dev/null || true
  kubectl taint node node01 dedicated=web:NoSchedule --overwrite 2>/dev/null || true

  # Pod 1: Bad selector
  cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: stuck-selector
  namespace: w3-milestone
spec:
  nodeSelector:
    hardware: gpu
  containers:
  - name: nginx
    image: nginx:alpine
EOF

  # Pod 2: Taint mismatch
  cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: stuck-taint
  namespace: w3-milestone
spec:
  nodeSelector:
    kubernetes.io/hostname: node01
  containers:
  - name: nginx
    image: nginx:alpine
EOF

  # Pod 3: DaemonSet without controlplane toleration
  cat << "EOF" | kubectl apply -f -
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: infra-agent
  namespace: w3-milestone
spec:
  selector:
    matchLabels:
      app: infra-agent
  template:
    metadata:
      labels:
        app: infra-agent
    spec:
      containers:
      - name: agent
        image: nginx:alpine
EOF
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: stuck-selector is Running on node02
S1=$(ssh controlplane 'kubectl get pod stuck-selector -n w3-milestone -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
N1=$(ssh controlplane 'kubectl get pod stuck-selector -n w3-milestone -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
if [ "$S1" == "Running" ] && [ "$N1" == "node02" ]; then
  echo -e "${GREEN}[PASS] Task 1: stuck-selector is Running on node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: stuck-selector status=$S1, node=$N1.${NC}"
fi

# Task 2: stuck-taint has toleration and is Running
S2=$(ssh controlplane 'kubectl get pod stuck-taint -n w3-milestone -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
TOL=$(ssh controlplane 'kubectl get pod stuck-taint -n w3-milestone -o jsonpath="{.spec.tolerations[?(@.key=="dedicated")].value}" 2>/dev/null || echo "None"')
if [ "$S2" == "Running" ] && [ "$TOL" == "web" ]; then
  echo -e "${GREEN}[PASS] Task 2: stuck-taint has toleration and is Running on node01.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: stuck-taint status=$S2, toleration=$TOL.${NC}"
fi

# Task 3: infra-agent DaemonSet running on controlplane
CP_POD=$(ssh controlplane 'kubectl get pods -n w3-milestone -l app=infra-agent --field-selector spec.nodeName=controlplane -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$CP_POD" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 3: infra-agent DaemonSet scheduled and Running on controlplane.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: infra-agent pod on controlplane is $CP_POD.${NC}"
fi""",
        "cka_solution": """1. Label node02:
`kubectl label node node02 hardware=gpu`

2. Add toleration to `stuck-taint`:
`kubectl get pod stuck-taint -n w3-milestone -o yaml > /tmp/stuck-taint.yaml`
Add under spec:
```yaml
tolerations:
- key: dedicated
  operator: Equal
  value: web
  effect: NoSchedule
```
`kubectl replace --force -f /tmp/stuck-taint.yaml`

3. Patch DaemonSet to tolerate control plane taint:
`kubectl patch ds infra-agent -n w3-milestone --type=strategic -p '{"spec":{"template":{"spec":{"tolerations":[{"key":"node-role.kubernetes.io/control-plane","operator":"Exists","effect":"NoSchedule"}]}}}}'`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w3-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl label node node02 hardware- 2>/dev/null || true
  kubectl taint node node01 dedicated- 2>/dev/null || true
'""",
    },
]
