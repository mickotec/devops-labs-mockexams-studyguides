"""
Dedicated CKA Lab Definitions for Week 8 (Days 1 to 6).
"""

WEEK_8_LABS = [
    {
        "day": 1,
        "date": '2026-11-16',
        "title": 'Troubleshooting: Control Plane & Applications',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Repair Broken Static Pod
A static pod manifest on `controlplane` at `/etc/kubernetes/manifests/broken-watchdog.yaml` is failing to run due to an invalid image tag.
1. Inspect `/etc/kubernetes/manifests/broken-watchdog.yaml`.
2. Change the image to `busybox:1.36` and ensure its command is `["sh", "-c", "sleep 3600"]`.
3. Wait for the kubelet to reconcile and verify that static pod `broken-watchdog-controlplane` enters `Running` status.

### Task 2: Fix CrashLoopBackOff Application Pod
In namespace `w8d1-trouble`:
Pod `db-connector` is failing in a CrashLoopBackOff state because a required environment variable `DB_HOST` is missing and its exit code is non-zero.
1. Inspect logs using `kubectl logs db-connector -n w8d1-trouble`.
2. Edit or recreate the pod with:
   - Environment variable: `DB_HOST=10.0.0.1`
   - Command: `["sh", "-c", "echo DB_HOST=$DB_HOST; sleep 3600"]`
3. Verify that `db-connector` reaches `Running` status.

### Task 3: Export Control Plane Diagnostics
1. Capture the last 20 lines of the `kube-apiserver` static pod log on `controlplane` and save them to `/opt/k8s/apiserver_log_sample.txt`.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w8d1-trouble --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d1-trouble
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/apiserver_log_sample.txt

  # Task 1 broken static pod
  sudo tee /etc/kubernetes/manifests/broken-watchdog.yaml > /dev/null << "EOF"
apiVersion: v1
kind: Pod
metadata:
  name: broken-watchdog
spec:
  containers:
  - name: watchdog
    image: busybox:invalid-v999
    command: ["sh", "-c", "sleep 3600"]
EOF

  # Task 2 crashing app pod
  cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: db-connector
  namespace: w8d1-trouble
spec:
  containers:
  - name: connector
    image: busybox:1.36
    command: ["sh", "-c", "if [ -z \"$DB_HOST\" ]; then exit 1; else sleep 3600; fi"]
EOF
'""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: Static pod running
WATCHDOG_PHASE=$(ssh controlplane 'kubectl get pod -n default -l "" 2>/dev/null | grep broken-watchdog | awk '''{print $3}''' || echo "NotFound"')
if ssh controlplane 'kubectl get pods -A | grep broken-watchdog | grep -q Running'; then
  echo -e "${GREEN}[PASS] Task 1: Static pod broken-watchdog is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Static pod broken-watchdog not Running (status: $WATCHDOG_PHASE).${NC}"
fi

# Task 2: db-connector running with DB_HOST
DBC_PHASE=$(ssh controlplane 'kubectl get pod db-connector -n w8d1-trouble -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
DBC_ENV=$(ssh controlplane 'kubectl get pod db-connector -n w8d1-trouble -o jsonpath="{.spec.containers[0].env[?(@.name=="DB_HOST")].value}" 2>/dev/null || echo "None"')
if [ "$DBC_PHASE" == "Running" ] && [ "$DBC_ENV" == "10.0.0.1" ]; then
  echo -e "${GREEN}[PASS] Task 2: Pod db-connector Running with DB_HOST=10.0.0.1.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: db-connector phase=$DBC_PHASE, DB_HOST=$DBC_ENV.${NC}"
fi

# Task 3: apiserver log export
if ssh controlplane 'test -s /opt/k8s/apiserver_log_sample.txt && [ $(wc -l < /opt/k8s/apiserver_log_sample.txt) -ge 10 ]'; then
  echo -e "${GREEN}[PASS] Task 3: /opt/k8s/apiserver_log_sample.txt contains log diagnostics.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /opt/k8s/apiserver_log_sample.txt missing or has fewer than 10 lines.${NC}"
fi""",
        "solution": """1. Fix static pod:
On `controlplane`, edit `/etc/kubernetes/manifests/broken-watchdog.yaml`:
Change `image: busybox:invalid-v999` to `image: busybox:1.36`.
Save and wait for kubelet to restart the pod.

2. Fix `db-connector`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: db-connector
  namespace: w8d1-trouble
spec:
  containers:
  - name: connector
    image: busybox:1.36
    env:
    - name: DB_HOST
      value: "10.0.0.1"
    command: ["sh", "-c", "echo DB_HOST=$DB_HOST; sleep 3600"]
```
`kubectl replace --force -f db-connector.yaml`

3. Save kube-apiserver logs:
```bash
APIPOD=$(kubectl get pods -n kube-system -l component=kube-apiserver -o jsonpath='{.items[0].metadata.name}')
kubectl logs -n kube-system $APIPOD --tail=20 > /opt/k8s/apiserver_log_sample.txt
```""",
        "reset": """ssh controlplane '
  kubectl delete namespace w8d1-trouble --grace-period=0 --force 2>/dev/null || true
  sudo rm -f /etc/kubernetes/manifests/broken-watchdog.yaml
  POD_ID=$(sudo crictl pods -q --name broken-watchdog-controlplane 2>/dev/null || true)
  [ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
  kubectl delete pod broken-watchdog-controlplane --force --grace-period=0 2>/dev/null || true
  rm -f /opt/k8s/apiserver_log_sample.txt
'""",
        "cka_title": 'Troubleshooting: Control Plane & Applications',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Repair Broken Static Pod
A static pod manifest on `controlplane` at `/etc/kubernetes/manifests/broken-watchdog.yaml` is failing to run due to an invalid image tag.
1. Inspect `/etc/kubernetes/manifests/broken-watchdog.yaml`.
2. Change the image to `busybox:1.36` and ensure its command is `["sh", "-c", "sleep 3600"]`.
3. Wait for the kubelet to reconcile and verify that static pod `broken-watchdog-controlplane` enters `Running` status.

### Task 2: Fix CrashLoopBackOff Application Pod
In namespace `w8d1-trouble`:
Pod `db-connector` is failing in a CrashLoopBackOff state because a required environment variable `DB_HOST` is missing and its exit code is non-zero.
1. Inspect logs using `kubectl logs db-connector -n w8d1-trouble`.
2. Edit or recreate the pod with:
   - Environment variable: `DB_HOST=10.0.0.1`
   - Command: `["sh", "-c", "echo DB_HOST=$DB_HOST; sleep 3600"]`
3. Verify that `db-connector` reaches `Running` status.

### Task 3: Export Control Plane Diagnostics
1. Capture the last 20 lines of the `kube-apiserver` static pod log on `controlplane` and save them to `/opt/k8s/apiserver_log_sample.txt`.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w8d1-trouble --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d1-trouble
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/apiserver_log_sample.txt

  # Task 1 broken static pod
  sudo tee /etc/kubernetes/manifests/broken-watchdog.yaml > /dev/null << "EOF"
apiVersion: v1
kind: Pod
metadata:
  name: broken-watchdog
spec:
  containers:
  - name: watchdog
    image: busybox:invalid-v999
    command: ["sh", "-c", "sleep 3600"]
EOF

  # Task 2 crashing app pod
  cat << "EOF" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: db-connector
  namespace: w8d1-trouble
spec:
  containers:
  - name: connector
    image: busybox:1.36
    command: ["sh", "-c", "if [ -z \"$DB_HOST\" ]; then exit 1; else sleep 3600; fi"]
EOF
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: Static pod running
WATCHDOG_PHASE=$(ssh controlplane 'kubectl get pod -n default -l "" 2>/dev/null | grep broken-watchdog | awk '''{print $3}''' || echo "NotFound"')
if ssh controlplane 'kubectl get pods -A | grep broken-watchdog | grep -q Running'; then
  echo -e "${GREEN}[PASS] Task 1: Static pod broken-watchdog is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Static pod broken-watchdog not Running (status: $WATCHDOG_PHASE).${NC}"
fi

# Task 2: db-connector running with DB_HOST
DBC_PHASE=$(ssh controlplane 'kubectl get pod db-connector -n w8d1-trouble -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
DBC_ENV=$(ssh controlplane 'kubectl get pod db-connector -n w8d1-trouble -o jsonpath="{.spec.containers[0].env[?(@.name=="DB_HOST")].value}" 2>/dev/null || echo "None"')
if [ "$DBC_PHASE" == "Running" ] && [ "$DBC_ENV" == "10.0.0.1" ]; then
  echo -e "${GREEN}[PASS] Task 2: Pod db-connector Running with DB_HOST=10.0.0.1.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: db-connector phase=$DBC_PHASE, DB_HOST=$DBC_ENV.${NC}"
fi

# Task 3: apiserver log export
if ssh controlplane 'test -s /opt/k8s/apiserver_log_sample.txt && [ $(wc -l < /opt/k8s/apiserver_log_sample.txt) -ge 10 ]'; then
  echo -e "${GREEN}[PASS] Task 3: /opt/k8s/apiserver_log_sample.txt contains log diagnostics.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /opt/k8s/apiserver_log_sample.txt missing or has fewer than 10 lines.${NC}"
fi""",
        "cka_solution": """1. Fix static pod:
On `controlplane`, edit `/etc/kubernetes/manifests/broken-watchdog.yaml`:
Change `image: busybox:invalid-v999` to `image: busybox:1.36`.
Save and wait for kubelet to restart the pod.

2. Fix `db-connector`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: db-connector
  namespace: w8d1-trouble
spec:
  containers:
  - name: connector
    image: busybox:1.36
    env:
    - name: DB_HOST
      value: "10.0.0.1"
    command: ["sh", "-c", "echo DB_HOST=$DB_HOST; sleep 3600"]
```
`kubectl replace --force -f db-connector.yaml`

3. Save kube-apiserver logs:
```bash
APIPOD=$(kubectl get pods -n kube-system -l component=kube-apiserver -o jsonpath='{.items[0].metadata.name}')
kubectl logs -n kube-system $APIPOD --tail=20 > /opt/k8s/apiserver_log_sample.txt
```""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w8d1-trouble --grace-period=0 --force 2>/dev/null || true
  sudo rm -f /etc/kubernetes/manifests/broken-watchdog.yaml
  POD_ID=$(sudo crictl pods -q --name broken-watchdog-controlplane 2>/dev/null || true)
  [ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
  kubectl delete pod broken-watchdog-controlplane --force --grace-period=0 2>/dev/null || true
  rm -f /opt/k8s/apiserver_log_sample.txt
'""",
    },
    {
        "day": 2,
        "date": '2026-11-17',
        "title": 'Troubleshooting: Worker Nodes & Network Failure',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Restore NotReady Worker Node
Worker node `node02` is currently reporting `NotReady` or has a stopped kubelet service.
1. SSH to `node02` (`ssh node02`).
2. Inspect `kubelet` service status using `systemctl status kubelet`.
3. Start and enable `kubelet` using `sudo systemctl enable --now kubelet`.
4. Verify on `controlplane` that `node02` returns to `Ready` status.

### Task 2: Remove Degraded Taint
Worker node `node02` has been tainted with `trouble=unreachable:NoSchedule`.
1. Remove this taint from `node02` using `kubectl taint`.

### Task 3: Verify Workload Scheduling on node02
In namespace `w8d2-trouble`:
1. Create a Pod named `worker-canary` using image `nginx:alpine`.
2. Schedule it to `node02` (using `nodeName: node02` or `nodeSelector`).
3. Verify the pod is in `Running` state on `node02`.""",
        "setup": """ssh node02 'sudo systemctl stop kubelet'
ssh controlplane '
  kubectl delete namespace w8d2-trouble --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d2-trouble
  kubectl taint node node02 trouble=unreachable:NoSchedule --overwrite 2>/dev/null || true
'""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: node02 is Ready
N2_STATUS=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.status.conditions[?(@.type=="Ready")].status}" 2>/dev/null || echo "False"')
if [ "$N2_STATUS" == "True" ]; then
  echo -e "${GREEN}[PASS] Task 1: Worker node node02 is Ready.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: node02 Ready status is $N2_STATUS (expected True).${NC}"
fi

# Task 2: Taint removed
TAINT_CHECK=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.spec.taints[?(@.key=="trouble")].key}" 2>/dev/null || echo "None"')
if [ "$TAINT_CHECK" == "None" ] || [ -z "$TAINT_CHECK" ]; then
  echo -e "${GREEN}[PASS] Task 2: Taint trouble=unreachable:NoSchedule removed from node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Taint trouble still present on node02.${NC}"
fi

# Task 3: canary pod running on node02
POD_NODE=$(ssh controlplane 'kubectl get pod worker-canary -n w8d2-trouble -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
POD_STATUS=$(ssh controlplane 'kubectl get pod worker-canary -n w8d2-trouble -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$POD_NODE" == "node02" ] && [ "$POD_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 3: worker-canary running on node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: worker-canary node=$POD_NODE, status=$POD_STATUS (expected node02, Running).${NC}"
fi""",
        "solution": """1. SSH to `node02`:
`ssh node02`
`sudo systemctl enable --now kubelet`
`exit`

2. Remove taint on `controlplane`:
`kubectl taint node node02 trouble-`

3. Deploy canary pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: worker-canary
  namespace: w8d2-trouble
spec:
  nodeName: node02
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f canary.yaml`""",
        "reset": """ssh node02 'sudo systemctl enable --now kubelet 2>/dev/null || true'
ssh controlplane '
  kubectl taint node node02 trouble- 2>/dev/null || true
  kubectl delete namespace w8d2-trouble --grace-period=0 --force 2>/dev/null || true
'""",
        "cka_title": 'Troubleshooting: Worker Nodes & Network Failure',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Restore NotReady Worker Node
Worker node `node02` is currently reporting `NotReady` or has a stopped kubelet service.
1. SSH to `node02` (`ssh node02`).
2. Inspect `kubelet` service status using `systemctl status kubelet`.
3. Start and enable `kubelet` using `sudo systemctl enable --now kubelet`.
4. Verify on `controlplane` that `node02` returns to `Ready` status.

### Task 2: Remove Degraded Taint
Worker node `node02` has been tainted with `trouble=unreachable:NoSchedule`.
1. Remove this taint from `node02` using `kubectl taint`.

### Task 3: Verify Workload Scheduling on node02
In namespace `w8d2-trouble`:
1. Create a Pod named `worker-canary` using image `nginx:alpine`.
2. Schedule it to `node02` (using `nodeName: node02` or `nodeSelector`).
3. Verify the pod is in `Running` state on `node02`.""",
        "cka_setup": """ssh node02 'sudo systemctl stop kubelet'
ssh controlplane '
  kubectl delete namespace w8d2-trouble --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d2-trouble
  kubectl taint node node02 trouble=unreachable:NoSchedule --overwrite 2>/dev/null || true
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: node02 is Ready
N2_STATUS=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.status.conditions[?(@.type=="Ready")].status}" 2>/dev/null || echo "False"')
if [ "$N2_STATUS" == "True" ]; then
  echo -e "${GREEN}[PASS] Task 1: Worker node node02 is Ready.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: node02 Ready status is $N2_STATUS (expected True).${NC}"
fi

# Task 2: Taint removed
TAINT_CHECK=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.spec.taints[?(@.key=="trouble")].key}" 2>/dev/null || echo "None"')
if [ "$TAINT_CHECK" == "None" ] || [ -z "$TAINT_CHECK" ]; then
  echo -e "${GREEN}[PASS] Task 2: Taint trouble=unreachable:NoSchedule removed from node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Taint trouble still present on node02.${NC}"
fi

# Task 3: canary pod running on node02
POD_NODE=$(ssh controlplane 'kubectl get pod worker-canary -n w8d2-trouble -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
POD_STATUS=$(ssh controlplane 'kubectl get pod worker-canary -n w8d2-trouble -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$POD_NODE" == "node02" ] && [ "$POD_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 3: worker-canary running on node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: worker-canary node=$POD_NODE, status=$POD_STATUS (expected node02, Running).${NC}"
fi""",
        "cka_solution": """1. SSH to `node02`:
`ssh node02`
`sudo systemctl enable --now kubelet`
`exit`

2. Remove taint on `controlplane`:
`kubectl taint node node02 trouble-`

3. Deploy canary pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: worker-canary
  namespace: w8d2-trouble
spec:
  nodeName: node02
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f canary.yaml`""",
        "cka_reset": """ssh node02 'sudo systemctl enable --now kubelet 2>/dev/null || true'
ssh controlplane '
  kubectl taint node node02 trouble- 2>/dev/null || true
  kubectl delete namespace w8d2-trouble --grace-period=0 --force 2>/dev/null || true
'""",
    },
    {
        "day": 3,
        "date": '2026-11-18',
        "title": 'JSONPath Queries & Lightning Labs 1 & 2',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Node Names Extraction
1. Use `kubectl get nodes -o jsonpath` to extract the names of all nodes in the cluster.
2. Sort the names alphabetically, one per line, and save them to `/opt/k8s/node_names.txt`.

### Task 2: System Container Images Extraction
1. Extract all unique container image names running across all pods in the `kube-system` namespace.
2. Sort the list uniquely and save to `/opt/k8s/kube_system_images.txt`.

### Task 3: Custom Columns Pod Mapping
1. Query pods in namespace `w8d3-json` using custom columns formatted as `NAME:.metadata.name,NODE:.spec.nodeName`.
2. Save the output to `/opt/k8s/pod_node_mapping.txt`.

### Task 4: Lightning Challenge
In namespace `w8d3-lightning`:
1. Deploy a Pod named `fast-pod` using image `redis:alpine` with label `app=fast-cache`.
2. Expose `fast-pod` with a ClusterIP service named `fast-svc` on port `6379`.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w8d3-json w8d3-lightning --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d3-json
  kubectl create namespace w8d3-lightning
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/node_names.txt /opt/k8s/kube_system_images.txt /opt/k8s/pod_node_mapping.txt
  kubectl run pod-alpha -n w8d3-json --image=nginx:alpine
  kubectl run pod-beta -n w8d3-json --image=nginx:alpine
'""",
        "verify": """SCORE=0; TOTAL=4
# Task 1: node_names.txt contains nodes
if ssh controlplane 'test -s /opt/k8s/node_names.txt && grep -q controlplane /opt/k8s/node_names.txt && grep -q node01 /opt/k8s/node_names.txt'; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/node_names.txt contains cluster nodes.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/node_names.txt missing or incomplete.${NC}"
fi

# Task 2: kube_system_images.txt
if ssh controlplane 'test -s /opt/k8s/kube_system_images.txt && grep -q -E "(coredns|apiserver|etcd)" /opt/k8s/kube_system_images.txt'; then
  echo -e "${GREEN}[PASS] Task 2: /opt/k8s/kube_system_images.txt contains system container images.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/kube_system_images.txt missing or lacks system images.${NC}"
fi

# Task 3: pod_node_mapping.txt custom columns
if ssh controlplane 'test -s /opt/k8s/pod_node_mapping.txt && grep -q "NAME" /opt/k8s/pod_node_mapping.txt && grep -q "pod-alpha" /opt/k8s/pod_node_mapping.txt'; then
  echo -e "${GREEN}[PASS] Task 3: /opt/k8s/pod_node_mapping.txt custom columns verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /opt/k8s/pod_node_mapping.txt missing or invalid format.${NC}"
fi

# Task 4: Lightning challenge pod & service
LIGHT_PHASE=$(ssh controlplane 'kubectl get pod fast-pod -n w8d3-lightning -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
LIGHT_SVC=$(ssh controlplane 'kubectl get svc fast-svc -n w8d3-lightning -o jsonpath="{.spec.ports[0].port}" 2>/dev/null || echo "0"')
if [ "$LIGHT_PHASE" == "Running" ] && [ "$LIGHT_SVC" == "6379" ]; then
  echo -e "${GREEN}[PASS] Task 4: Lightning Pod fast-pod and Service fast-svc verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: fast-pod phase=$LIGHT_PHASE, fast-svc port=$LIGHT_SVC.${NC}"
fi""",
        "solution": """1. Extract node names:
`kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"
"}{end}' | sort > /opt/k8s/node_names.txt`

2. Extract kube-system images:
`kubectl get pods -n kube-system -o jsonpath='{range .items[*]}{range .spec.containers[*]}{.image}{"
"}{end}{end}' | sort -u > /opt/k8s/kube_system_images.txt`

3. Custom columns query:
`kubectl get pods -n w8d3-json -o custom-columns=NAME:.metadata.name,NODE:.spec.nodeName > /opt/k8s/pod_node_mapping.txt`

4. Lightning challenge:
```bash
kubectl run fast-pod -n w8d3-lightning --image=redis:alpine --labels=app=fast-cache --port=6379
kubectl expose pod fast-pod -n w8d3-lightning --name=fast-svc --port=6379
```""",
        "reset": """ssh controlplane '
  kubectl delete namespace w8d3-json w8d3-lightning --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/node_names.txt /opt/k8s/kube_system_images.txt /opt/k8s/pod_node_mapping.txt
'""",
        "cka_title": 'JSONPath Queries & Lightning Labs 1 & 2',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Node Names Extraction
1. Use `kubectl get nodes -o jsonpath` to extract the names of all nodes in the cluster.
2. Sort the names alphabetically, one per line, and save them to `/opt/k8s/node_names.txt`.

### Task 2: System Container Images Extraction
1. Extract all unique container image names running across all pods in the `kube-system` namespace.
2. Sort the list uniquely and save to `/opt/k8s/kube_system_images.txt`.

### Task 3: Custom Columns Pod Mapping
1. Query pods in namespace `w8d3-json` using custom columns formatted as `NAME:.metadata.name,NODE:.spec.nodeName`.
2. Save the output to `/opt/k8s/pod_node_mapping.txt`.

### Task 4: Lightning Challenge
In namespace `w8d3-lightning`:
1. Deploy a Pod named `fast-pod` using image `redis:alpine` with label `app=fast-cache`.
2. Expose `fast-pod` with a ClusterIP service named `fast-svc` on port `6379`.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w8d3-json w8d3-lightning --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d3-json
  kubectl create namespace w8d3-lightning
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/node_names.txt /opt/k8s/kube_system_images.txt /opt/k8s/pod_node_mapping.txt
  kubectl run pod-alpha -n w8d3-json --image=nginx:alpine
  kubectl run pod-beta -n w8d3-json --image=nginx:alpine
'""",
        "cka_verify": """SCORE=0; TOTAL=4
# Task 1: node_names.txt contains nodes
if ssh controlplane 'test -s /opt/k8s/node_names.txt && grep -q controlplane /opt/k8s/node_names.txt && grep -q node01 /opt/k8s/node_names.txt'; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/node_names.txt contains cluster nodes.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/node_names.txt missing or incomplete.${NC}"
fi

# Task 2: kube_system_images.txt
if ssh controlplane 'test -s /opt/k8s/kube_system_images.txt && grep -q -E "(coredns|apiserver|etcd)" /opt/k8s/kube_system_images.txt'; then
  echo -e "${GREEN}[PASS] Task 2: /opt/k8s/kube_system_images.txt contains system container images.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/kube_system_images.txt missing or lacks system images.${NC}"
fi

# Task 3: pod_node_mapping.txt custom columns
if ssh controlplane 'test -s /opt/k8s/pod_node_mapping.txt && grep -q "NAME" /opt/k8s/pod_node_mapping.txt && grep -q "pod-alpha" /opt/k8s/pod_node_mapping.txt'; then
  echo -e "${GREEN}[PASS] Task 3: /opt/k8s/pod_node_mapping.txt custom columns verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /opt/k8s/pod_node_mapping.txt missing or invalid format.${NC}"
fi

# Task 4: Lightning challenge pod & service
LIGHT_PHASE=$(ssh controlplane 'kubectl get pod fast-pod -n w8d3-lightning -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
LIGHT_SVC=$(ssh controlplane 'kubectl get svc fast-svc -n w8d3-lightning -o jsonpath="{.spec.ports[0].port}" 2>/dev/null || echo "0"')
if [ "$LIGHT_PHASE" == "Running" ] && [ "$LIGHT_SVC" == "6379" ]; then
  echo -e "${GREEN}[PASS] Task 4: Lightning Pod fast-pod and Service fast-svc verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: fast-pod phase=$LIGHT_PHASE, fast-svc port=$LIGHT_SVC.${NC}"
fi""",
        "cka_solution": """1. Extract node names:
`kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"
"}{end}' | sort > /opt/k8s/node_names.txt`

2. Extract kube-system images:
`kubectl get pods -n kube-system -o jsonpath='{range .items[*]}{range .spec.containers[*]}{.image}{"
"}{end}{end}' | sort -u > /opt/k8s/kube_system_images.txt`

3. Custom columns query:
`kubectl get pods -n w8d3-json -o custom-columns=NAME:.metadata.name,NODE:.spec.nodeName > /opt/k8s/pod_node_mapping.txt`

4. Lightning challenge:
```bash
kubectl run fast-pod -n w8d3-lightning --image=redis:alpine --labels=app=fast-cache --port=6379
kubectl expose pod fast-pod -n w8d3-lightning --name=fast-svc --port=6379
```""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w8d3-json w8d3-lightning --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/node_names.txt /opt/k8s/kube_system_images.txt /opt/k8s/pod_node_mapping.txt
'""",
    },
    {
        "day": 4,
        "date": '2026-11-19',
        "title": 'Timed Mock Exam 1 & Step-by-Step Review',
        "diff": 'Hard (Milestone)',
        "time": '45m',
        "tasks": """### Task 1: RBAC Role & Binding
In namespace `w8d4-exam`:
1. Create a ServiceAccount named `deploy-bot`.
2. Create a Role named `pod-reader` granting `["get", "list", "watch"]` permissions on `pods`.
3. Create a RoleBinding named `deploy-bot-reader` binding `deploy-bot` to Role `pod-reader`.

### Task 2: Multi-Container Pod with Shared Volume
In namespace `w8d4-exam`:
Create a Pod named `app-logger` sharing volume `shared-logs` (`emptyDir`):
1. Container `producer`: image `busybox:1.36`, command `["sh", "-c", "while true; do date >> /var/log/app.log; sleep 2; done"]`, mounting `shared-logs` to `/var/log`.
2. Container `consumer`: image `busybox:1.36`, command `["sh", "-c", "tail -f /var/log/app.log"]`, mounting `shared-logs` to `/var/log`.

### Task 3: Secrets Injected into Environment
In namespace `w8d4-exam`:
1. Create a Secret named `db-credentials` with `DB_USER=dbadmin` and `DB_PASS=SuperSecret101`.
2. Deploy a Pod named `db-client` (image `nginx:alpine`) that sets environment variables `DB_USER` and `DB_PASS` from `db-credentials`.

### Task 4: Sentinel DaemonSet
In namespace `w8d4-exam`:
1. Deploy a DaemonSet named `node-sentinel` using image `busybox:1.36` running `["sleep", "3600"]`.
2. Ensure sentinel pods run on every worker node.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w8d4-exam --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d4-exam
'""",
        "verify": """SCORE=0; TOTAL=4
# Task 1: RBAC can-i
AUTH_CHECK=$(ssh controlplane 'kubectl auth can-i get pods --as=system:serviceaccount:w8d4-exam:deploy-bot -n w8d4-exam 2>/dev/null || echo "no"')
if [ "$AUTH_CHECK" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 1: RBAC permissions for deploy-bot verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: deploy-bot cannot get pods in w8d4-exam.${NC}"
fi

# Task 2: Multi-container pod
C_READY=$(ssh controlplane 'kubectl get pod app-logger -n w8d4-exam -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null || echo ""')
if [ "$C_READY" == "true true" ]; then
  echo -e "${GREEN}[PASS] Task 2: Multi-container pod app-logger has 2 ready containers.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: app-logger containers ready: '$C_READY' (expected 'true true').${NC}"
fi

# Task 3: db-client env from secret
DBC_USER=$(ssh controlplane 'kubectl exec db-client -n w8d4-exam -- env 2>/dev/null | grep DB_USER=dbadmin || true')
DBC_PASS=$(ssh controlplane 'kubectl exec db-client -n w8d4-exam -- env 2>/dev/null | grep DB_PASS=SuperSecret101 || true')
if [ -n "$DBC_USER" ] && [ -n "$DBC_PASS" ]; then
  echo -e "${GREEN}[PASS] Task 3: db-client environment variables verified from secret.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: db-client environment variables missing or mismatch.${NC}"
fi

# Task 4: DaemonSet node-sentinel
DS_READY=$(ssh controlplane 'kubectl get ds node-sentinel -n w8d4-exam -o jsonpath="{.status.numberReady}" 2>/dev/null || echo "0"')
if [ "$DS_READY" -ge 2 ]; then
  echo -e "${GREEN}[PASS] Task 4: DaemonSet node-sentinel active on $DS_READY nodes.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: DaemonSet node-sentinel ready pods: $DS_READY (expected >= 2).${NC}"
fi""",
        "solution": """1. RBAC:
```bash
kubectl create sa deploy-bot -n w8d4-exam
kubectl create role pod-reader -n w8d4-exam --verb=get,list,watch --resource=pods
kubectl create rolebinding deploy-bot-reader -n w8d4-exam --role=pod-reader --serviceaccount=w8d4-exam:deploy-bot
```

2. Multi-container pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-logger
  namespace: w8d4-exam
spec:
  volumes:
  - name: shared-logs
    emptyDir: {}
  containers:
  - name: producer
    image: busybox:1.36
    command: ["sh", "-c", "while true; do date >> /var/log/app.log; sleep 2; done"]
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log
  - name: consumer
    image: busybox:1.36
    command: ["sh", "-c", "tail -f /var/log/app.log"]
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log
```

3. Secret and pod:
```bash
kubectl create secret generic db-credentials -n w8d4-exam --from-literal=DB_USER=dbadmin --from-literal=DB_PASS=SuperSecret101
```
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: db-client
  namespace: w8d4-exam
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    env:
    - name: DB_USER
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: DB_USER
    - name: DB_PASS
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: DB_PASS
```

4. DaemonSet:
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-sentinel
  namespace: w8d4-exam
spec:
  selector:
    matchLabels:
      app: node-sentinel
  template:
    metadata:
      labels:
        app: node-sentinel
    spec:
      containers:
      - name: sentinel
        image: busybox:1.36
        command: ["sleep", "3600"]
```""",
        "reset": """ssh controlplane '
  kubectl delete namespace w8d4-exam --grace-period=0 --force 2>/dev/null || true
'""",
        "cka_title": 'Timed Mock Exam 1 & Step-by-Step Review',
        "cka_diff": 'Hard (Milestone)',
        "cka_time": '45m',
        "cka_tasks": """### Task 1: RBAC Role & Binding
In namespace `w8d4-exam`:
1. Create a ServiceAccount named `deploy-bot`.
2. Create a Role named `pod-reader` granting `["get", "list", "watch"]` permissions on `pods`.
3. Create a RoleBinding named `deploy-bot-reader` binding `deploy-bot` to Role `pod-reader`.

### Task 2: Multi-Container Pod with Shared Volume
In namespace `w8d4-exam`:
Create a Pod named `app-logger` sharing volume `shared-logs` (`emptyDir`):
1. Container `producer`: image `busybox:1.36`, command `["sh", "-c", "while true; do date >> /var/log/app.log; sleep 2; done"]`, mounting `shared-logs` to `/var/log`.
2. Container `consumer`: image `busybox:1.36`, command `["sh", "-c", "tail -f /var/log/app.log"]`, mounting `shared-logs` to `/var/log`.

### Task 3: Secrets Injected into Environment
In namespace `w8d4-exam`:
1. Create a Secret named `db-credentials` with `DB_USER=dbadmin` and `DB_PASS=SuperSecret101`.
2. Deploy a Pod named `db-client` (image `nginx:alpine`) that sets environment variables `DB_USER` and `DB_PASS` from `db-credentials`.

### Task 4: Sentinel DaemonSet
In namespace `w8d4-exam`:
1. Deploy a DaemonSet named `node-sentinel` using image `busybox:1.36` running `["sleep", "3600"]`.
2. Ensure sentinel pods run on every worker node.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w8d4-exam --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d4-exam
'""",
        "cka_verify": """SCORE=0; TOTAL=4
# Task 1: RBAC can-i
AUTH_CHECK=$(ssh controlplane 'kubectl auth can-i get pods --as=system:serviceaccount:w8d4-exam:deploy-bot -n w8d4-exam 2>/dev/null || echo "no"')
if [ "$AUTH_CHECK" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 1: RBAC permissions for deploy-bot verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: deploy-bot cannot get pods in w8d4-exam.${NC}"
fi

# Task 2: Multi-container pod
C_READY=$(ssh controlplane 'kubectl get pod app-logger -n w8d4-exam -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null || echo ""')
if [ "$C_READY" == "true true" ]; then
  echo -e "${GREEN}[PASS] Task 2: Multi-container pod app-logger has 2 ready containers.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: app-logger containers ready: '$C_READY' (expected 'true true').${NC}"
fi

# Task 3: db-client env from secret
DBC_USER=$(ssh controlplane 'kubectl exec db-client -n w8d4-exam -- env 2>/dev/null | grep DB_USER=dbadmin || true')
DBC_PASS=$(ssh controlplane 'kubectl exec db-client -n w8d4-exam -- env 2>/dev/null | grep DB_PASS=SuperSecret101 || true')
if [ -n "$DBC_USER" ] && [ -n "$DBC_PASS" ]; then
  echo -e "${GREEN}[PASS] Task 3: db-client environment variables verified from secret.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: db-client environment variables missing or mismatch.${NC}"
fi

# Task 4: DaemonSet node-sentinel
DS_READY=$(ssh controlplane 'kubectl get ds node-sentinel -n w8d4-exam -o jsonpath="{.status.numberReady}" 2>/dev/null || echo "0"')
if [ "$DS_READY" -ge 2 ]; then
  echo -e "${GREEN}[PASS] Task 4: DaemonSet node-sentinel active on $DS_READY nodes.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: DaemonSet node-sentinel ready pods: $DS_READY (expected >= 2).${NC}"
fi""",
        "cka_solution": """1. RBAC:
```bash
kubectl create sa deploy-bot -n w8d4-exam
kubectl create role pod-reader -n w8d4-exam --verb=get,list,watch --resource=pods
kubectl create rolebinding deploy-bot-reader -n w8d4-exam --role=pod-reader --serviceaccount=w8d4-exam:deploy-bot
```

2. Multi-container pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-logger
  namespace: w8d4-exam
spec:
  volumes:
  - name: shared-logs
    emptyDir: {}
  containers:
  - name: producer
    image: busybox:1.36
    command: ["sh", "-c", "while true; do date >> /var/log/app.log; sleep 2; done"]
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log
  - name: consumer
    image: busybox:1.36
    command: ["sh", "-c", "tail -f /var/log/app.log"]
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log
```

3. Secret and pod:
```bash
kubectl create secret generic db-credentials -n w8d4-exam --from-literal=DB_USER=dbadmin --from-literal=DB_PASS=SuperSecret101
```
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: db-client
  namespace: w8d4-exam
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    env:
    - name: DB_USER
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: DB_USER
    - name: DB_PASS
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: DB_PASS
```

4. DaemonSet:
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-sentinel
  namespace: w8d4-exam
spec:
  selector:
    matchLabels:
      app: node-sentinel
  template:
    metadata:
      labels:
        app: node-sentinel
    spec:
      containers:
      - name: sentinel
        image: busybox:1.36
        command: ["sleep", "3600"]
```""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w8d4-exam --grace-period=0 --force 2>/dev/null || true
'""",
    },
    {
        "day": 5,
        "date": '2026-11-20',
        "title": 'Timed Mock Exam 2 & 3 Marathon',
        "diff": 'Hard (Milestone)',
        "time": '45m',
        "tasks": """### Task 1: PersistentVolume & Claim
1. Create a PersistentVolume named `pv-marathon-data`:
   - Capacity: `2Gi`
   - AccessModes: `ReadWriteOnce`
   - HostPath: `/data/pv-marathon`
2. In namespace `w8d5-marathon`, create a PersistentVolumeClaim named `pvc-marathon` requesting `2Gi` (accessModes: `ReadWriteOnce`).
3. Verify that the PVC reaches `Bound` status.

### Task 2: NodeAffinity Scheduling
1. Add label `zone=production-a` to node `node01`.
2. In namespace `w8d5-marathon`, deploy a Deployment named `zone-app` (image `nginx:alpine`, 2 replicas):
   - Configure `nodeAffinity` (`requiredDuringSchedulingIgnoredDuringExecution`) targeting nodes with key `zone` and value `production-a`.
3. Verify all pods run strictly on `node01`.

### Task 3: Taints & Tolerations
1. Taint node `node02` with `dedicated=special:NoSchedule`.
2. In namespace `w8d5-marathon`, deploy a Pod named `special-worker` (image `busybox:1.36`, command `["sleep", "3600"]`):
   - Add a toleration matching key `dedicated`, operator `Equal`, value `special`, effect `NoSchedule`.
   - Explicitly schedule it to `node02` (`nodeName: node02`).
3. Verify `special-worker` is `Running` on `node02`.

### Task 4: Deployment Rollout & Rollback
1. Update deployment `zone-app` image to `nginx:1.25.5-alpine`.
2. Verify the rollout completes.
3. Perform a rollout undo (`kubectl rollout undo deployment zone-app -n w8d5-marathon`) to roll back to the initial image `nginx:alpine`.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w8d5-marathon --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv pv-marathon-data 2>/dev/null || true
  kubectl create namespace w8d5-marathon
  kubectl label node node01 zone- 2>/dev/null || true
  kubectl taint node node02 dedicated- 2>/dev/null || true
'""",
        "verify": """SCORE=0; TOTAL=4
# Task 1: PVC Bound
PVC_STAT=$(ssh controlplane 'kubectl get pvc pvc-marathon -n w8d5-marathon -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$PVC_STAT" == "Bound" ]; then
  echo -e "${GREEN}[PASS] Task 1: PVC pvc-marathon is Bound.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: PVC pvc-marathon status is $PVC_STAT (expected Bound).${NC}"
fi

# Task 2: zone-app scheduled to node01
POD_NODES=$(ssh controlplane 'kubectl get pods -n w8d5-marathon -l app=zone-app -o jsonpath="{.items[*].spec.nodeName}" 2>/dev/null || echo ""')
if [ -n "$POD_NODES" ] && [[ ! "$POD_NODES" =~ node02 ]] && [[ "$POD_NODES" =~ node01 ]]; then
  echo -e "${GREEN}[PASS] Task 2: Deployment zone-app pods scheduled strictly on node01 ($POD_NODES).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Deployment zone-app pods nodes: '$POD_NODES' (expected only node01).${NC}"
fi

# Task 3: special-worker on node02
SW_STATUS=$(ssh controlplane 'kubectl get pod special-worker -n w8d5-marathon -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
SW_NODE=$(ssh controlplane 'kubectl get pod special-worker -n w8d5-marathon -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
if [ "$SW_STATUS" == "Running" ] && [ "$SW_NODE" == "node02" ]; then
  echo -e "${GREEN}[PASS] Task 3: special-worker running on tainted node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: special-worker status=$SW_STATUS, node=$SW_NODE.${NC}"
fi

# Task 4: zone-app image is nginx:alpine
CUR_IMG=$(ssh controlplane 'kubectl get deployment zone-app -n w8d5-marathon -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo ""')
if [ "$CUR_IMG" == "nginx:alpine" ]; then
  echo -e "${GREEN}[PASS] Task 4: Deployment zone-app rolled back to nginx:alpine.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: Deployment zone-app image is '$CUR_IMG' (expected nginx:alpine).${NC}"
fi""",
        "solution": """1. PV and PVC:
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-marathon-data
spec:
  capacity:
    storage: 2Gi
  accessModes:
  - ReadWriteOnce
  hostPath:
    path: /data/pv-marathon
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-marathon
  namespace: w8d5-marathon
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 2Gi
```

2. Label node01 and deploy with NodeAffinity:
`kubectl label node node01 zone=production-a`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: zone-app
  namespace: w8d5-marathon
spec:
  replicas: 2
  selector:
    matchLabels:
      app: zone-app
  template:
    metadata:
      labels:
        app: zone-app
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: zone
                operator: In
                values:
                - production-a
      containers:
      - name: nginx
        image: nginx:alpine
```

3. Taint node02 and deploy special-worker:
`kubectl taint node node02 dedicated=special:NoSchedule`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: special-worker
  namespace: w8d5-marathon
spec:
  nodeName: node02
  tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "special"
    effect: "NoSchedule"
  containers:
  - name: busybox
    image: busybox:1.36
    command: ["sleep", "3600"]
```

4. Rollout and rollback:
```bash
kubectl set image deployment/zone-app nginx=nginx:1.25.5-alpine -n w8d5-marathon
kubectl rollout status deployment/zone-app -n w8d5-marathon
kubectl rollout undo deployment/zone-app -n w8d5-marathon
```""",
        "reset": """ssh controlplane '
  kubectl delete namespace w8d5-marathon --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv pv-marathon-data 2>/dev/null || true
  kubectl label node node01 zone- 2>/dev/null || true
  kubectl taint node node02 dedicated- 2>/dev/null || true
'""",
        "cka_title": 'Timed Mock Exam 2 & 3 Marathon',
        "cka_diff": 'Hard (Milestone)',
        "cka_time": '45m',
        "cka_tasks": """### Task 1: PersistentVolume & Claim
1. Create a PersistentVolume named `pv-marathon-data`:
   - Capacity: `2Gi`
   - AccessModes: `ReadWriteOnce`
   - HostPath: `/data/pv-marathon`
2. In namespace `w8d5-marathon`, create a PersistentVolumeClaim named `pvc-marathon` requesting `2Gi` (accessModes: `ReadWriteOnce`).
3. Verify that the PVC reaches `Bound` status.

### Task 2: NodeAffinity Scheduling
1. Add label `zone=production-a` to node `node01`.
2. In namespace `w8d5-marathon`, deploy a Deployment named `zone-app` (image `nginx:alpine`, 2 replicas):
   - Configure `nodeAffinity` (`requiredDuringSchedulingIgnoredDuringExecution`) targeting nodes with key `zone` and value `production-a`.
3. Verify all pods run strictly on `node01`.

### Task 3: Taints & Tolerations
1. Taint node `node02` with `dedicated=special:NoSchedule`.
2. In namespace `w8d5-marathon`, deploy a Pod named `special-worker` (image `busybox:1.36`, command `["sleep", "3600"]`):
   - Add a toleration matching key `dedicated`, operator `Equal`, value `special`, effect `NoSchedule`.
   - Explicitly schedule it to `node02` (`nodeName: node02`).
3. Verify `special-worker` is `Running` on `node02`.

### Task 4: Deployment Rollout & Rollback
1. Update deployment `zone-app` image to `nginx:1.25.5-alpine`.
2. Verify the rollout completes.
3. Perform a rollout undo (`kubectl rollout undo deployment zone-app -n w8d5-marathon`) to roll back to the initial image `nginx:alpine`.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w8d5-marathon --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv pv-marathon-data 2>/dev/null || true
  kubectl create namespace w8d5-marathon
  kubectl label node node01 zone- 2>/dev/null || true
  kubectl taint node node02 dedicated- 2>/dev/null || true
'""",
        "cka_verify": """SCORE=0; TOTAL=4
# Task 1: PVC Bound
PVC_STAT=$(ssh controlplane 'kubectl get pvc pvc-marathon -n w8d5-marathon -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$PVC_STAT" == "Bound" ]; then
  echo -e "${GREEN}[PASS] Task 1: PVC pvc-marathon is Bound.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: PVC pvc-marathon status is $PVC_STAT (expected Bound).${NC}"
fi

# Task 2: zone-app scheduled to node01
POD_NODES=$(ssh controlplane 'kubectl get pods -n w8d5-marathon -l app=zone-app -o jsonpath="{.items[*].spec.nodeName}" 2>/dev/null || echo ""')
if [ -n "$POD_NODES" ] && [[ ! "$POD_NODES" =~ node02 ]] && [[ "$POD_NODES" =~ node01 ]]; then
  echo -e "${GREEN}[PASS] Task 2: Deployment zone-app pods scheduled strictly on node01 ($POD_NODES).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Deployment zone-app pods nodes: '$POD_NODES' (expected only node01).${NC}"
fi

# Task 3: special-worker on node02
SW_STATUS=$(ssh controlplane 'kubectl get pod special-worker -n w8d5-marathon -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
SW_NODE=$(ssh controlplane 'kubectl get pod special-worker -n w8d5-marathon -o jsonpath="{.spec.nodeName}" 2>/dev/null || echo "None"')
if [ "$SW_STATUS" == "Running" ] && [ "$SW_NODE" == "node02" ]; then
  echo -e "${GREEN}[PASS] Task 3: special-worker running on tainted node02.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: special-worker status=$SW_STATUS, node=$SW_NODE.${NC}"
fi

# Task 4: zone-app image is nginx:alpine
CUR_IMG=$(ssh controlplane 'kubectl get deployment zone-app -n w8d5-marathon -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo ""')
if [ "$CUR_IMG" == "nginx:alpine" ]; then
  echo -e "${GREEN}[PASS] Task 4: Deployment zone-app rolled back to nginx:alpine.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: Deployment zone-app image is '$CUR_IMG' (expected nginx:alpine).${NC}"
fi""",
        "cka_solution": """1. PV and PVC:
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-marathon-data
spec:
  capacity:
    storage: 2Gi
  accessModes:
  - ReadWriteOnce
  hostPath:
    path: /data/pv-marathon
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-marathon
  namespace: w8d5-marathon
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 2Gi
```

2. Label node01 and deploy with NodeAffinity:
`kubectl label node node01 zone=production-a`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: zone-app
  namespace: w8d5-marathon
spec:
  replicas: 2
  selector:
    matchLabels:
      app: zone-app
  template:
    metadata:
      labels:
        app: zone-app
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: zone
                operator: In
                values:
                - production-a
      containers:
      - name: nginx
        image: nginx:alpine
```

3. Taint node02 and deploy special-worker:
`kubectl taint node node02 dedicated=special:NoSchedule`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: special-worker
  namespace: w8d5-marathon
spec:
  nodeName: node02
  tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "special"
    effect: "NoSchedule"
  containers:
  - name: busybox
    image: busybox:1.36
    command: ["sleep", "3600"]
```

4. Rollout and rollback:
```bash
kubectl set image deployment/zone-app nginx=nginx:1.25.5-alpine -n w8d5-marathon
kubectl rollout status deployment/zone-app -n w8d5-marathon
kubectl rollout undo deployment/zone-app -n w8d5-marathon
```""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w8d5-marathon --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv pv-marathon-data 2>/dev/null || true
  kubectl label node node01 zone- 2>/dev/null || true
  kubectl taint node node02 dedicated- 2>/dev/null || true
'""",
    },
    {
        "day": 6,
        "date": '2026-11-21',
        "title": 'Killer.sh Simulator Marathon (Exam Benchmark)',
        "diff": 'Hard (Milestone)',
        "time": '45m',
        "tasks": """### Task 1: Sidecar Logging Architecture
In namespace `w8d6-benchmark`:
Create Pod `audit-counter` sharing an `emptyDir` volume `log-storage`:
1. Container `counter`: image `busybox:1.36`, command `["sh", "-c", "while true; do date >> /var/log/counter.log; sleep 1; done"]`, mounting `log-storage` at `/var/log`.
2. Container `sidecar`: image `busybox:1.36`, command `["sh", "-c", "tail -n+1 -f /var/log/counter.log"]`, mounting `log-storage` at `/var/log`.

### Task 2: ETCD Snapshot Backup
On `controlplane`:
1. Create a snapshot backup of etcd at `/opt/k8s/etcd-backup.db` using `etcdctl snapshot save`.
2. Use etcd endpoint `https://127.0.0.1:2379` and certificates:
   - CA: `/etc/kubernetes/pki/etcd/ca.crt`
   - Cert: `/etc/kubernetes/pki/etcd/server.crt`
   - Key: `/etc/kubernetes/pki/etcd/server.key`

### Task 3: Ingress with TLS Termination
In namespace `w8d6-benchmark`:
1. Deploy `frontend` (image `nginx:alpine`, port 80) and expose with ClusterIP service `frontend-svc` on port 80.
2. Generate a TLS secret `benchmark-tls` for hostname `benchmark.k8s.local`.
3. Create Ingress `benchmark-ingress` with `ingressClassName: nginx`:
   - Host: `benchmark.k8s.local`
   - TLS referencing `benchmark-tls`
   - Path `/` (Prefix) pointing to service `frontend-svc` port 80.

### Task 4: Database Network Isolation
In namespace `w8d6-benchmark`:
1. Deploy pod `database` with label `role=db` (image `nginx:alpine`).
2. Create NetworkPolicy `strict-db-policy` that isolates `database` allowing ingress ONLY from pods labeled `role=backend` on TCP port `5432`.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w8d6-benchmark --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d6-benchmark
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/etcd-backup.db
  kubectl run database -n w8d6-benchmark --image=nginx:alpine --labels=role=db
'""",
        "verify": """SCORE=0; TOTAL=4
# Task 1: audit-counter sidecar pod
AC_STATUS=$(ssh controlplane 'kubectl get pod audit-counter -n w8d6-benchmark -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null || echo ""')
if [ "$AC_STATUS" == "true true" ]; then
  echo -e "${GREEN}[PASS] Task 1: Pod audit-counter running with 2 ready containers.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: audit-counter status: '$AC_STATUS' (expected 'true true').${NC}"
fi

# Task 2: etcd snapshot backup
if ssh controlplane 'test -s /opt/k8s/etcd-backup.db && ETCDCTL_API=3 etcdctl snapshot status /opt/k8s/etcd-backup.db >/dev/null 2>&1'; then
  echo -e "${GREEN}[PASS] Task 2: Valid etcd snapshot verified at /opt/k8s/etcd-backup.db.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/etcd-backup.db missing or invalid etcd database.${NC}"
fi

# Task 3: Ingress with TLS
TLS_NAME=$(ssh controlplane 'kubectl get ingress benchmark-ingress -n w8d6-benchmark -o jsonpath="{.spec.tls[0].secretName}" 2>/dev/null || echo "None"')
HOST_NAME=$(ssh controlplane 'kubectl get ingress benchmark-ingress -n w8d6-benchmark -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo "None"')
if [ "$TLS_NAME" == "benchmark-tls" ] && [ "$HOST_NAME" == "benchmark.k8s.local" ]; then
  echo -e "${GREEN}[PASS] Task 3: Ingress benchmark-ingress with TLS verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Ingress TLS or host mismatch (tls=$TLS_NAME, host=$HOST_NAME).${NC}"
fi

# Task 4: NetworkPolicy strict-db-policy
NP_TARGET=$(ssh controlplane 'kubectl get netpol strict-db-policy -n w8d6-benchmark -o jsonpath="{.spec.podSelector.matchLabels.role}" 2>/dev/null || echo "None"')
NP_ALLOW=$(ssh controlplane 'kubectl get netpol strict-db-policy -n w8d6-benchmark -o jsonpath="{.spec.ingress[0].from[0].podSelector.matchLabels.role}" 2>/dev/null || echo "None"')
NP_PORT=$(ssh controlplane 'kubectl get netpol strict-db-policy -n w8d6-benchmark -o jsonpath="{.spec.ingress[0].ports[0].port}" 2>/dev/null || echo "0"')
if [ "$NP_TARGET" == "db" ] && [ "$NP_ALLOW" == "backend" ] && [ "$NP_PORT" == "5432" ]; then
  echo -e "${GREEN}[PASS] Task 4: NetworkPolicy strict-db-policy correctly isolates db on port 5432.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: NetworkPolicy rules mismatch (target=$NP_TARGET, allow=$NP_ALLOW, port=$NP_PORT).${NC}"
fi""",
        "solution": """1. Sidecar pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: audit-counter
  namespace: w8d6-benchmark
spec:
  volumes:
  - name: log-storage
    emptyDir: {}
  containers:
  - name: counter
    image: busybox:1.36
    command: ["sh", "-c", "while true; do date >> /var/log/counter.log; sleep 1; done"]
    volumeMounts:
    - name: log-storage
      mountPath: /var/log
  - name: sidecar
    image: busybox:1.36
    command: ["sh", "-c", "tail -n+1 -f /var/log/counter.log"]
    volumeMounts:
    - name: log-storage
      mountPath: /var/log
```

2. ETCD snapshot:
```bash
sudo ETCDCTL_API=3 etcdctl   --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   snapshot save /opt/k8s/etcd-backup.db
```

3. Ingress & TLS:
```bash
kubectl create deployment frontend -n w8d6-benchmark --image=nginx:alpine --port=80
kubectl expose deployment frontend -n w8d6-benchmark --name=frontend-svc --port=80
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /tmp/bench.key -out /tmp/bench.crt -subj "/CN=benchmark.k8s.local"
kubectl create secret tls benchmark-tls -n w8d6-benchmark --cert=/tmp/bench.crt --key=/tmp/bench.key
```
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: benchmark-ingress
  namespace: w8d6-benchmark
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - benchmark.k8s.local
    secretName: benchmark-tls
  rules:
  - host: benchmark.k8s.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-svc
            port:
              number: 80
```

4. NetworkPolicy:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: strict-db-policy
  namespace: w8d6-benchmark
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: backend
    ports:
    - protocol: TCP
      port: 5432
```""",
        "reset": """ssh controlplane '
  kubectl delete namespace w8d6-benchmark --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/etcd-backup.db /tmp/bench.key /tmp/bench.crt
'""",
        "cka_title": 'Killer.sh Simulator Marathon (Exam Benchmark)',
        "cka_diff": 'Hard (Milestone)',
        "cka_time": '45m',
        "cka_tasks": """### Task 1: Sidecar Logging Architecture
In namespace `w8d6-benchmark`:
Create Pod `audit-counter` sharing an `emptyDir` volume `log-storage`:
1. Container `counter`: image `busybox:1.36`, command `["sh", "-c", "while true; do date >> /var/log/counter.log; sleep 1; done"]`, mounting `log-storage` at `/var/log`.
2. Container `sidecar`: image `busybox:1.36`, command `["sh", "-c", "tail -n+1 -f /var/log/counter.log"]`, mounting `log-storage` at `/var/log`.

### Task 2: ETCD Snapshot Backup
On `controlplane`:
1. Create a snapshot backup of etcd at `/opt/k8s/etcd-backup.db` using `etcdctl snapshot save`.
2. Use etcd endpoint `https://127.0.0.1:2379` and certificates:
   - CA: `/etc/kubernetes/pki/etcd/ca.crt`
   - Cert: `/etc/kubernetes/pki/etcd/server.crt`
   - Key: `/etc/kubernetes/pki/etcd/server.key`

### Task 3: Ingress with TLS Termination
In namespace `w8d6-benchmark`:
1. Deploy `frontend` (image `nginx:alpine`, port 80) and expose with ClusterIP service `frontend-svc` on port 80.
2. Generate a TLS secret `benchmark-tls` for hostname `benchmark.k8s.local`.
3. Create Ingress `benchmark-ingress` with `ingressClassName: nginx`:
   - Host: `benchmark.k8s.local`
   - TLS referencing `benchmark-tls`
   - Path `/` (Prefix) pointing to service `frontend-svc` port 80.

### Task 4: Database Network Isolation
In namespace `w8d6-benchmark`:
1. Deploy pod `database` with label `role=db` (image `nginx:alpine`).
2. Create NetworkPolicy `strict-db-policy` that isolates `database` allowing ingress ONLY from pods labeled `role=backend` on TCP port `5432`.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w8d6-benchmark --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w8d6-benchmark
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/etcd-backup.db
  kubectl run database -n w8d6-benchmark --image=nginx:alpine --labels=role=db
'""",
        "cka_verify": """SCORE=0; TOTAL=4
# Task 1: audit-counter sidecar pod
AC_STATUS=$(ssh controlplane 'kubectl get pod audit-counter -n w8d6-benchmark -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null || echo ""')
if [ "$AC_STATUS" == "true true" ]; then
  echo -e "${GREEN}[PASS] Task 1: Pod audit-counter running with 2 ready containers.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: audit-counter status: '$AC_STATUS' (expected 'true true').${NC}"
fi

# Task 2: etcd snapshot backup
if ssh controlplane 'test -s /opt/k8s/etcd-backup.db && ETCDCTL_API=3 etcdctl snapshot status /opt/k8s/etcd-backup.db >/dev/null 2>&1'; then
  echo -e "${GREEN}[PASS] Task 2: Valid etcd snapshot verified at /opt/k8s/etcd-backup.db.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/etcd-backup.db missing or invalid etcd database.${NC}"
fi

# Task 3: Ingress with TLS
TLS_NAME=$(ssh controlplane 'kubectl get ingress benchmark-ingress -n w8d6-benchmark -o jsonpath="{.spec.tls[0].secretName}" 2>/dev/null || echo "None"')
HOST_NAME=$(ssh controlplane 'kubectl get ingress benchmark-ingress -n w8d6-benchmark -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo "None"')
if [ "$TLS_NAME" == "benchmark-tls" ] && [ "$HOST_NAME" == "benchmark.k8s.local" ]; then
  echo -e "${GREEN}[PASS] Task 3: Ingress benchmark-ingress with TLS verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Ingress TLS or host mismatch (tls=$TLS_NAME, host=$HOST_NAME).${NC}"
fi

# Task 4: NetworkPolicy strict-db-policy
NP_TARGET=$(ssh controlplane 'kubectl get netpol strict-db-policy -n w8d6-benchmark -o jsonpath="{.spec.podSelector.matchLabels.role}" 2>/dev/null || echo "None"')
NP_ALLOW=$(ssh controlplane 'kubectl get netpol strict-db-policy -n w8d6-benchmark -o jsonpath="{.spec.ingress[0].from[0].podSelector.matchLabels.role}" 2>/dev/null || echo "None"')
NP_PORT=$(ssh controlplane 'kubectl get netpol strict-db-policy -n w8d6-benchmark -o jsonpath="{.spec.ingress[0].ports[0].port}" 2>/dev/null || echo "0"')
if [ "$NP_TARGET" == "db" ] && [ "$NP_ALLOW" == "backend" ] && [ "$NP_PORT" == "5432" ]; then
  echo -e "${GREEN}[PASS] Task 4: NetworkPolicy strict-db-policy correctly isolates db on port 5432.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: NetworkPolicy rules mismatch (target=$NP_TARGET, allow=$NP_ALLOW, port=$NP_PORT).${NC}"
fi""",
        "cka_solution": """1. Sidecar pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: audit-counter
  namespace: w8d6-benchmark
spec:
  volumes:
  - name: log-storage
    emptyDir: {}
  containers:
  - name: counter
    image: busybox:1.36
    command: ["sh", "-c", "while true; do date >> /var/log/counter.log; sleep 1; done"]
    volumeMounts:
    - name: log-storage
      mountPath: /var/log
  - name: sidecar
    image: busybox:1.36
    command: ["sh", "-c", "tail -n+1 -f /var/log/counter.log"]
    volumeMounts:
    - name: log-storage
      mountPath: /var/log
```

2. ETCD snapshot:
```bash
sudo ETCDCTL_API=3 etcdctl   --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   snapshot save /opt/k8s/etcd-backup.db
```

3. Ingress & TLS:
```bash
kubectl create deployment frontend -n w8d6-benchmark --image=nginx:alpine --port=80
kubectl expose deployment frontend -n w8d6-benchmark --name=frontend-svc --port=80
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /tmp/bench.key -out /tmp/bench.crt -subj "/CN=benchmark.k8s.local"
kubectl create secret tls benchmark-tls -n w8d6-benchmark --cert=/tmp/bench.crt --key=/tmp/bench.key
```
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: benchmark-ingress
  namespace: w8d6-benchmark
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - benchmark.k8s.local
    secretName: benchmark-tls
  rules:
  - host: benchmark.k8s.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-svc
            port:
              number: 80
```

4. NetworkPolicy:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: strict-db-policy
  namespace: w8d6-benchmark
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: backend
    ports:
    - protocol: TCP
      port: 5432
```""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w8d6-benchmark --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/etcd-backup.db /tmp/bench.key /tmp/bench.crt
'""",
    },
]
