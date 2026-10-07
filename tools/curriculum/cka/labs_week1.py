"""
Dedicated CKA Lab Definitions for Week 1 (Days 1 to 6).
"""

WEEK_1_LABS = [
    {
        "day": 1,
        "date": '2026-09-14',
        "title": 'Kubernetes Architecture & Container Runtimes',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Troubleshoot Control Plane Static Pod
1. Inspect the control plane static pod manifests located in `/etc/kubernetes/manifests/` on node `controlplane`.
2. Determine why `kube-scheduler` is failing to start. (Check `/var/log/pods` or kubelet journal on `controlplane`).
3. Correct the error in `/etc/kubernetes/manifests/kube-scheduler.yaml` without breaking other parameters.
4. Verify that the static pod `kube-scheduler-controlplane` is in `Running` state (1/1 Ready) and that the test pod `w1d1-pending-test` in namespace `default` transitions from `Pending` to `Running`.

### Task 2: CRI Runtime Inspection & Rogue Container Termination
1. SSH into worker node `node01`.
2. Using the CRI CLI utility (`crictl`), inspect the running containers managed by runtime `containerd`.
3. Locate the rogue container named `rogue-crypto-miner` that was started directly on the node bypassing the API server.
4. Stop and remove the rogue container using `crictl`.

### Task 3: Create a Worker Static Pod
1. On worker node `node01`, configure a static pod manifest named `node01-monitor.yaml` in kubelet's static pod manifest directory (`/etc/kubernetes/manifests/`).
2. The pod specification must satisfy:
   - Pod Name: `node01-monitor`
   - Image: `busybox:1.36`
   - Command: `["sh", "-c", "while true; do date >> /var/log/node-heartbeat.log; sleep 10; done"]`
   - Volume: Mount host directory `/var/log` into container directory `/var/log`.
3. Verify from `controlplane` that `node01-monitor-node01` appears in `kubectl get pods -A` and is in `Running` state.""",
        "setup": """# Setup Task 1: Break kube-scheduler on controlplane
ssh controlplane '
if [ ! -f /etc/kubernetes/kube-scheduler.yaml.orig ]; then
  sudo cp /etc/kubernetes/manifests/kube-scheduler.yaml /etc/kubernetes/kube-scheduler.yaml.orig
fi
sudo sed -i "s|^apiVersion: v1\$|apiVersion: v1.0|" /etc/kubernetes/manifests/kube-scheduler.yaml
CID=$(sudo crictl ps -q --name kube-scheduler 2>/dev/null || true)
if [ -n "$CID" ]; then
  sudo crictl stop "$CID" 2>/dev/null || true
  sudo crictl rm "$CID" 2>/dev/null || true
fi
sudo systemctl restart kubelet
'

# Deploy test pod that hangs in Pending
ssh controlplane '
kubectl delete pod w1d1-pending-test --force --grace-period=0 2>/dev/null || true
kubectl run w1d1-pending-test --image=nginx:alpine --restart=Never
'

# Setup Task 2: Rogue container on node01
ssh node01 '
sudo crictl inspecti docker.io/library/busybox:1.36 >/dev/null 2>&1 || sudo crictl pull docker.io/library/busybox:1.36 >/dev/null 2>&1

OLD_CID=$(sudo crictl ps -a -q --name rogue-crypto-miner 2>/dev/null || true)
if [ -n "$OLD_CID" ]; then
  sudo crictl stop "$OLD_CID" 2>/dev/null || true
  sudo crictl rm "$OLD_CID" 2>/dev/null || true
fi
OLD_SB=$(sudo crictl pods -q --name rogue-sandbox 2>/dev/null || true)
if [ -n "$OLD_SB" ]; then
  sudo crictl stopp "$OLD_SB" 2>/dev/null || true
  sudo crictl rmp -f "$OLD_SB" 2>/dev/null || true
fi

sudo rm -f /tmp/rogue-sandbox.json /tmp/rogue-container.json
sudo tee /tmp/rogue-sandbox.json << "EOF_SB" > /dev/null
{
  "metadata": { "name": "rogue-sandbox", "namespace": "default", "attempt": 0, "uid": "rogue-uid-001" },
  "log_directory": "/tmp/rogue-logs",
  "linux": {
    "cgroup_parent": "kubepods.slice",
    "security_context": { "namespace_options": { "network": 2, "pid": 1, "ipc": 1 }, "run_as_user": { "value": 0 } }
  }
}
EOF_SB

sudo mkdir -p /tmp/rogue-logs
SB=$(sudo crictl runp /tmp/rogue-sandbox.json 2>/dev/null || true)
if [ -n "$SB" ]; then
  sudo tee /tmp/rogue-container.json << "EOF_CN" > /dev/null
{
  "metadata": { "name": "rogue-crypto-miner" },
  "image": { "image": "docker.io/library/busybox:1.36" },
  "command": ["sh", "-c", "while true; do sleep 3600; done"],
  "log_path": "miner.log"
}
EOF_CN
  CN=$(sudo crictl create "$SB" /tmp/rogue-container.json /tmp/rogue-sandbox.json 2>/dev/null || true)
  if [ -n "$CN" ]; then
    sudo crictl start "$CN" >/dev/null 2>&1 || true
  fi
fi
sudo rm -f /etc/kubernetes/manifests/node01-monitor.yaml
POD_ID=$(sudo crictl pods -q --name node01-monitor-node01 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: kube-scheduler health & scheduled pod...${NC}"
SCHED_STATUS=$(ssh controlplane 'kubectl get pods -n kube-system -l component=kube-scheduler -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Unknown"')
TEST_POD_STATUS=$(ssh controlplane 'kubectl get pod w1d1-pending-test -o jsonpath="{.status.phase}" 2>/dev/null || echo "Unknown"')

if [ "$SCHED_STATUS" == "Running" ] && [ "$TEST_POD_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] kube-scheduler is Running and w1d1-pending-test scheduled successfully.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] kube-scheduler is '$SCHED_STATUS' (expected Running) or w1d1-pending-test is '$TEST_POD_STATUS'.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Rogue container on node01...${NC}"
ROGUE_CHECK=$(ssh -o BatchMode=yes -o ConnectTimeout=5 node01 'sudo crictl ps -a 2>/dev/null | grep rogue-crypto-miner || true' 2>/dev/null || true)
if [ -z "$ROGUE_CHECK" ]; then
  echo -e "${GREEN}[PASS] Rogue container 'rogue-crypto-miner' has been terminated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Rogue container 'rogue-crypto-miner' is still running on node01.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Static Pod 'node01-monitor' on node01...${NC}"
STATIC_POD=$(ssh controlplane 'kubectl get pods -A 2>/dev/null | grep "node01-monitor-node01" || true')
if [ -n "$STATIC_POD" ] && echo "$STATIC_POD" | grep -q "Running"; then
  echo -e "${GREEN}[PASS] Static pod 'node01-monitor-node01' is running and registered with API server.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Static pod 'node01-monitor-node01' not found or not in Running state.${NC}"
fi""",
        "solution": """### Task 1: Fix kube-scheduler
1. SSH into `controlplane`:
   `ssh controlplane`
2. Inspect the manifest:
   `sudo vim /etc/kubernetes/manifests/kube-scheduler.yaml`
3. Fix the first line:
   Change `apiVersion: v1.0` back to `apiVersion: v1`
4. Wait 10 seconds for kubelet to reload the static pod. Check:
   `kubectl get pods -n kube-system -l component=kube-scheduler`
   `kubectl get pod w1d1-pending-test`

### Task 2: Terminate Rogue Container on node01
1. SSH into `node01`:
   `ssh node01`
2. Find the rogue container:
   `sudo crictl ps -a | grep rogue-crypto-miner`
3. Stop and remove it:
   `sudo crictl stop <CONTAINER_ID>`
   `sudo crictl rm <CONTAINER_ID>`

### Task 3: Create Static Pod on node01
1. On `node01`:
   `sudo vim /etc/kubernetes/manifests/node01-monitor.yaml`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: node01-monitor
spec:
  containers:
  - name: monitor
    image: busybox:1.36
    command: ["sh", "-c", "while true; do date >> /var/log/node-heartbeat.log; sleep 10; done"]
    volumeMounts:
    - name: log-dir
      mountPath: /var/log
  volumes:
  - name: log-dir
    hostPath:
      path: /var/log
```""",
        "reset": """ssh controlplane '
if [ -f /etc/kubernetes/kube-scheduler.yaml.orig ]; then
  sudo mv -f /etc/kubernetes/kube-scheduler.yaml.orig /etc/kubernetes/manifests/kube-scheduler.yaml
else
  sudo sed -i "s/^apiVersion: v1.0/apiVersion: v1/" /etc/kubernetes/manifests/kube-scheduler.yaml 2>/dev/null || true
fi
sudo sed -i "s/scheduler-broken\.conf/scheduler\.conf/g" /etc/kubernetes/manifests/kube-scheduler.yaml 2>/dev/null || true
sudo systemctl restart kubelet
kubectl delete pod w1d1-pending-test node01-monitor-node01 --force --grace-period=0 2>/dev/null || true
'
ssh node01 '
sudo rm -f /etc/kubernetes/manifests/node01-monitor.yaml
POD_ID=$(sudo crictl pods -q --name node01-monitor-node01 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
CID=$(sudo crictl ps -a -q --name rogue-crypto-miner 2>/dev/null || true)
[ -n "$CID" ] && sudo crictl stop "$CID" 2>/dev/null && sudo crictl rm "$CID" 2>/dev/null || true
'""",
        "cka_title": 'Kubernetes Architecture & Container Runtimes',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Troubleshoot Control Plane Static Pod
1. Inspect the control plane static pod manifests located in `/etc/kubernetes/manifests/` on node `controlplane`.
2. Determine why `kube-scheduler` is failing to start. (Check `/var/log/pods` or kubelet journal on `controlplane`).
3. Correct the error in `/etc/kubernetes/manifests/kube-scheduler.yaml` without breaking other parameters.
4. Verify that the static pod `kube-scheduler-controlplane` is in `Running` state (1/1 Ready) and that the test pod `w1d1-pending-test` in namespace `default` transitions from `Pending` to `Running`.

### Task 2: CRI Runtime Inspection & Rogue Container Termination
1. SSH into worker node `node01`.
2. Using the CRI CLI utility (`crictl`), inspect the running containers managed by runtime `containerd`.
3. Locate the rogue container named `rogue-crypto-miner` that was started directly on the node bypassing the API server.
4. Stop and remove the rogue container using `crictl`.

### Task 3: Create a Worker Static Pod
1. On worker node `node01`, configure a static pod manifest named `node01-monitor.yaml` in kubelet's static pod manifest directory (`/etc/kubernetes/manifests/`).
2. The pod specification must satisfy:
   - Pod Name: `node01-monitor`
   - Image: `busybox:1.36`
   - Command: `["sh", "-c", "while true; do date >> /var/log/node-heartbeat.log; sleep 10; done"]`
   - Volume: Mount host directory `/var/log` into container directory `/var/log`.
3. Verify from `controlplane` that `node01-monitor-node01` appears in `kubectl get pods -A` and is in `Running` state.""",
        "cka_setup": """# Setup Task 1: Break kube-scheduler on controlplane
ssh controlplane '
if [ ! -f /etc/kubernetes/kube-scheduler.yaml.orig ]; then
  sudo cp /etc/kubernetes/manifests/kube-scheduler.yaml /etc/kubernetes/kube-scheduler.yaml.orig
fi
sudo sed -i "s|^apiVersion: v1\$|apiVersion: v1.0|" /etc/kubernetes/manifests/kube-scheduler.yaml
CID=$(sudo crictl ps -q --name kube-scheduler 2>/dev/null || true)
if [ -n "$CID" ]; then
  sudo crictl stop "$CID" 2>/dev/null || true
  sudo crictl rm "$CID" 2>/dev/null || true
fi
sudo systemctl restart kubelet
'

# Deploy test pod that hangs in Pending
ssh controlplane '
kubectl delete pod w1d1-pending-test --force --grace-period=0 2>/dev/null || true
kubectl run w1d1-pending-test --image=nginx:alpine --restart=Never
'

# Setup Task 2: Rogue container on node01
ssh node01 '
sudo crictl inspecti docker.io/library/busybox:1.36 >/dev/null 2>&1 || sudo crictl pull docker.io/library/busybox:1.36 >/dev/null 2>&1

OLD_CID=$(sudo crictl ps -a -q --name rogue-crypto-miner 2>/dev/null || true)
if [ -n "$OLD_CID" ]; then
  sudo crictl stop "$OLD_CID" 2>/dev/null || true
  sudo crictl rm "$OLD_CID" 2>/dev/null || true
fi
OLD_SB=$(sudo crictl pods -q --name rogue-sandbox 2>/dev/null || true)
if [ -n "$OLD_SB" ]; then
  sudo crictl stopp "$OLD_SB" 2>/dev/null || true
  sudo crictl rmp -f "$OLD_SB" 2>/dev/null || true
fi

sudo rm -f /tmp/rogue-sandbox.json /tmp/rogue-container.json
sudo tee /tmp/rogue-sandbox.json << "EOF_SB" > /dev/null
{
  "metadata": { "name": "rogue-sandbox", "namespace": "default", "attempt": 0, "uid": "rogue-uid-001" },
  "log_directory": "/tmp/rogue-logs",
  "linux": {
    "cgroup_parent": "kubepods.slice",
    "security_context": { "namespace_options": { "network": 2, "pid": 1, "ipc": 1 }, "run_as_user": { "value": 0 } }
  }
}
EOF_SB

sudo mkdir -p /tmp/rogue-logs
SB=$(sudo crictl runp /tmp/rogue-sandbox.json 2>/dev/null || true)
if [ -n "$SB" ]; then
  sudo tee /tmp/rogue-container.json << "EOF_CN" > /dev/null
{
  "metadata": { "name": "rogue-crypto-miner" },
  "image": { "image": "docker.io/library/busybox:1.36" },
  "command": ["sh", "-c", "while true; do sleep 3600; done"],
  "log_path": "miner.log"
}
EOF_CN
  CN=$(sudo crictl create "$SB" /tmp/rogue-container.json /tmp/rogue-sandbox.json 2>/dev/null || true)
  if [ -n "$CN" ]; then
    sudo crictl start "$CN" >/dev/null 2>&1 || true
  fi
fi
sudo rm -f /etc/kubernetes/manifests/node01-monitor.yaml
POD_ID=$(sudo crictl pods -q --name node01-monitor-node01 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'""",
        "cka_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: kube-scheduler health & scheduled pod...${NC}"
SCHED_STATUS=$(ssh controlplane 'kubectl get pods -n kube-system -l component=kube-scheduler -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "Unknown"')
TEST_POD_STATUS=$(ssh controlplane 'kubectl get pod w1d1-pending-test -o jsonpath="{.status.phase}" 2>/dev/null || echo "Unknown"')

if [ "$SCHED_STATUS" == "Running" ] && [ "$TEST_POD_STATUS" == "Running" ]; then
  echo -e "${GREEN}[PASS] kube-scheduler is Running and w1d1-pending-test scheduled successfully.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] kube-scheduler is '$SCHED_STATUS' (expected Running) or w1d1-pending-test is '$TEST_POD_STATUS'.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Rogue container on node01...${NC}"
ROGUE_CHECK=$(ssh -o BatchMode=yes -o ConnectTimeout=5 node01 'sudo crictl ps -a 2>/dev/null | grep rogue-crypto-miner || true' 2>/dev/null || true)
if [ -z "$ROGUE_CHECK" ]; then
  echo -e "${GREEN}[PASS] Rogue container 'rogue-crypto-miner' has been terminated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Rogue container 'rogue-crypto-miner' is still running on node01.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Static Pod 'node01-monitor' on node01...${NC}"
STATIC_POD=$(ssh controlplane 'kubectl get pods -A 2>/dev/null | grep "node01-monitor-node01" || true')
if [ -n "$STATIC_POD" ] && echo "$STATIC_POD" | grep -q "Running"; then
  echo -e "${GREEN}[PASS] Static pod 'node01-monitor-node01' is running and registered with API server.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Static pod 'node01-monitor-node01' not found or not in Running state.${NC}"
fi""",
        "cka_solution": """### Task 1: Fix kube-scheduler
1. SSH into `controlplane`:
   `ssh controlplane`
2. Inspect the manifest:
   `sudo vim /etc/kubernetes/manifests/kube-scheduler.yaml`
3. Fix the first line:
   Change `apiVersion: v1.0` back to `apiVersion: v1`
4. Wait 10 seconds for kubelet to reload the static pod. Check:
   `kubectl get pods -n kube-system -l component=kube-scheduler`
   `kubectl get pod w1d1-pending-test`

### Task 2: Terminate Rogue Container on node01
1. SSH into `node01`:
   `ssh node01`
2. Find the rogue container:
   `sudo crictl ps -a | grep rogue-crypto-miner`
3. Stop and remove it:
   `sudo crictl stop <CONTAINER_ID>`
   `sudo crictl rm <CONTAINER_ID>`

### Task 3: Create Static Pod on node01
1. On `node01`:
   `sudo vim /etc/kubernetes/manifests/node01-monitor.yaml`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: node01-monitor
spec:
  containers:
  - name: monitor
    image: busybox:1.36
    command: ["sh", "-c", "while true; do date >> /var/log/node-heartbeat.log; sleep 10; done"]
    volumeMounts:
    - name: log-dir
      mountPath: /var/log
  volumes:
  - name: log-dir
    hostPath:
      path: /var/log
```""",
        "cka_reset": """ssh controlplane '
if [ -f /etc/kubernetes/kube-scheduler.yaml.orig ]; then
  sudo mv -f /etc/kubernetes/kube-scheduler.yaml.orig /etc/kubernetes/manifests/kube-scheduler.yaml
else
  sudo sed -i "s/^apiVersion: v1.0/apiVersion: v1/" /etc/kubernetes/manifests/kube-scheduler.yaml 2>/dev/null || true
fi
sudo sed -i "s/scheduler-broken\.conf/scheduler\.conf/g" /etc/kubernetes/manifests/kube-scheduler.yaml 2>/dev/null || true
sudo systemctl restart kubelet
kubectl delete pod w1d1-pending-test node01-monitor-node01 --force --grace-period=0 2>/dev/null || true
'
ssh node01 '
sudo rm -f /etc/kubernetes/manifests/node01-monitor.yaml
POD_ID=$(sudo crictl pods -q --name node01-monitor-node01 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
CID=$(sudo crictl ps -a -q --name rogue-crypto-miner 2>/dev/null || true)
[ -n "$CID" ] && sudo crictl stop "$CID" 2>/dev/null && sudo crictl rm "$CID" 2>/dev/null || true
'""",
    },
    {
        "day": 2,
        "date": '2026-09-15',
        "title": 'ETCD Fundamentals & Cluster State Store',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: ETCD Endpoint Health & Member Inspection
1. SSH into `controlplane`.
2. Inspect the static pod manifest `/etc/kubernetes/manifests/etcd.yaml` to identify the client port, CA certificate, cert file, and key file.
3. Using `etcdctl` (with `ETCDCTL_API=3`), query the endpoint health using TLS certificates.
4. Export the endpoint health report to `/opt/backup/etcd-health.txt`.

### Task 2: Create a Validated ETCD Snapshot
1. Create directory `/opt/backup/` on `controlplane` if it does not already exist.
2. Using `etcdctl snapshot save`, save a point-in-time snapshot to `/opt/backup/etcd-snapshot-w1d2.db`.
3. Verify the snapshot using `etcdctl snapshot status --write-out=table`.
4. Ensure the snapshot status output is saved to `/opt/backup/snapshot-status.txt`.

### Task 3: Key Prefix Counting
1. Using `etcdctl get`, query the keys with prefix `/registry/namespaces` to count how many namespaces currently exist in the raw etcd store.
2. Save the count (number only) to `/opt/backup/namespace-count.txt`.""",
        "setup": """ssh controlplane '
sudo mkdir -p /opt/backup && sudo chmod 777 /opt/backup
rm -f /opt/backup/etcd-health.txt /opt/backup/etcd-snapshot-w1d2.db /opt/backup/snapshot-status.txt /opt/backup/namespace-count.txt
'""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: ETCD health export...${NC}"
HEALTH_CHECK=$(ssh controlplane 'sudo cat /opt/backup/etcd-health.txt 2>/dev/null || true')
if echo "$HEALTH_CHECK" | grep -qi "healthy"; then
  echo -e "${GREEN}[PASS] /opt/backup/etcd-health.txt contains verified health output.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/backup/etcd-health.txt missing or does not indicate healthy status.${NC}"
fi

echo -e "${BOLD}Checking Task 2: ETCD snapshot file & status table...${NC}"
SNAP_CHECK=$(ssh controlplane 'sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-snapshot-w1d2.db --write-out=table 2>/dev/null || true')
if echo "$SNAP_CHECK" | grep -qiE "REVISION|TOTAL KEYS"; then
  echo -e "${GREEN}[PASS] Snapshot /opt/backup/etcd-snapshot-w1d2.db is valid and readable.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Snapshot invalid or status verification failed.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Namespace count file...${NC}"
COUNT=$(ssh controlplane 'sudo cat /opt/backup/namespace-count.txt 2>/dev/null | tr -d "[:space:]" || true')
ACTUAL_NS_COUNT=$(ssh controlplane 'kubectl get ns --no-headers 2>/dev/null | wc -l | tr -d "[:space:]"')

if [ -n "$COUNT" ] && [ "$COUNT" == "$ACTUAL_NS_COUNT" ]; then
  echo -e "${GREEN}[PASS] Namespace count matched ($COUNT namespaces).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Namespace count was '$COUNT' (expected $ACTUAL_NS_COUNT).${NC}"
fi""",
        "solution": """1. Identify ETCD flags from `/etc/kubernetes/manifests/etcd.yaml`:
- CACERT: `/etc/kubernetes/pki/etcd/ca.crt`
- CERT: `/etc/kubernetes/pki/etcd/server.crt`
- KEY: `/etc/kubernetes/pki/etcd/server.key`
- ENDPOINT: `https://127.0.0.1:2379`

2. Task 1: Query endpoint health:
```bash
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   endpoint health | sudo tee /opt/backup/etcd-health.txt
```

3. Task 2: Snapshot save and verify status:
```bash
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   snapshot save /opt/backup/etcd-snapshot-w1d2.db

sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-snapshot-w1d2.db --write-out=table | sudo tee /opt/backup/snapshot-status.txt
```

4. Task 3: Query namespace prefix count:
```bash
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   get /registry/namespaces --prefix --keys-only | grep -v '^$' | wc -l | sudo tee /opt/backup/namespace-count.txt
```""",
        "reset": "ssh controlplane 'sudo rm -rf /opt/backup'",
        "cka_title": 'ETCD Fundamentals & Cluster State Store',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: ETCD Endpoint Health & Member Inspection
1. SSH into `controlplane`.
2. Inspect the static pod manifest `/etc/kubernetes/manifests/etcd.yaml` to identify the client port, CA certificate, cert file, and key file.
3. Using `etcdctl` (with `ETCDCTL_API=3`), query the endpoint health using TLS certificates.
4. Export the endpoint health report to `/opt/backup/etcd-health.txt`.

### Task 2: Create a Validated ETCD Snapshot
1. Create directory `/opt/backup/` on `controlplane` if it does not already exist.
2. Using `etcdctl snapshot save`, save a point-in-time snapshot to `/opt/backup/etcd-snapshot-w1d2.db`.
3. Verify the snapshot using `etcdctl snapshot status --write-out=table`.
4. Ensure the snapshot status output is saved to `/opt/backup/snapshot-status.txt`.

### Task 3: Key Prefix Counting
1. Using `etcdctl get`, query the keys with prefix `/registry/namespaces` to count how many namespaces currently exist in the raw etcd store.
2. Save the count (number only) to `/opt/backup/namespace-count.txt`.""",
        "cka_setup": """ssh controlplane '
sudo mkdir -p /opt/backup && sudo chmod 777 /opt/backup
rm -f /opt/backup/etcd-health.txt /opt/backup/etcd-snapshot-w1d2.db /opt/backup/snapshot-status.txt /opt/backup/namespace-count.txt
'""",
        "cka_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: ETCD health export...${NC}"
HEALTH_CHECK=$(ssh controlplane 'sudo cat /opt/backup/etcd-health.txt 2>/dev/null || true')
if echo "$HEALTH_CHECK" | grep -qi "healthy"; then
  echo -e "${GREEN}[PASS] /opt/backup/etcd-health.txt contains verified health output.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/backup/etcd-health.txt missing or does not indicate healthy status.${NC}"
fi

echo -e "${BOLD}Checking Task 2: ETCD snapshot file & status table...${NC}"
SNAP_CHECK=$(ssh controlplane 'sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-snapshot-w1d2.db --write-out=table 2>/dev/null || true')
if echo "$SNAP_CHECK" | grep -qiE "REVISION|TOTAL KEYS"; then
  echo -e "${GREEN}[PASS] Snapshot /opt/backup/etcd-snapshot-w1d2.db is valid and readable.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Snapshot invalid or status verification failed.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Namespace count file...${NC}"
COUNT=$(ssh controlplane 'sudo cat /opt/backup/namespace-count.txt 2>/dev/null | tr -d "[:space:]" || true')
ACTUAL_NS_COUNT=$(ssh controlplane 'kubectl get ns --no-headers 2>/dev/null | wc -l | tr -d "[:space:]"')

if [ -n "$COUNT" ] && [ "$COUNT" == "$ACTUAL_NS_COUNT" ]; then
  echo -e "${GREEN}[PASS] Namespace count matched ($COUNT namespaces).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Namespace count was '$COUNT' (expected $ACTUAL_NS_COUNT).${NC}"
fi""",
        "cka_solution": """1. Identify ETCD flags from `/etc/kubernetes/manifests/etcd.yaml`:
- CACERT: `/etc/kubernetes/pki/etcd/ca.crt`
- CERT: `/etc/kubernetes/pki/etcd/server.crt`
- KEY: `/etc/kubernetes/pki/etcd/server.key`
- ENDPOINT: `https://127.0.0.1:2379`

2. Task 1: Query endpoint health:
```bash
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   endpoint health | sudo tee /opt/backup/etcd-health.txt
```

3. Task 2: Snapshot save and verify status:
```bash
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   snapshot save /opt/backup/etcd-snapshot-w1d2.db

sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-snapshot-w1d2.db --write-out=table | sudo tee /opt/backup/snapshot-status.txt
```

4. Task 3: Query namespace prefix count:
```bash
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   get /registry/namespaces --prefix --keys-only | grep -v '^$' | wc -l | sudo tee /opt/backup/namespace-count.txt
```""",
        "cka_reset": "ssh controlplane 'sudo rm -rf /opt/backup'",
    },
    {
        "day": 3,
        "date": '2026-09-16',
        "title": 'Pod Internals & YAML Architecture',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Create Namespace `fintech`
Create a namespace named `fintech`.

### Task 2: Fix the Broken Manifest & Deploy
1. Inspect `/opt/k8s-manifests/broken-app.yaml` on `controlplane`.
2. Fix all syntax, schema, and indentation errors:
   - Pod Name: `transaction-processor`
   - Namespace: `fintech`
   - Container Name: `processor`
   - Image: `nginx:1.25-alpine`
   - Environment variables: `MAX_WORKERS=8` and `CACHE_DIR=/tmp/cache`
   - Container Ports: `8080` (name: `http`) and `9090` (name: `metrics`)
   - Resource limits: memory `128Mi`, CPU `200m`
   - Readiness probe: HTTP GET `/` on port `80` (nginx default) with `initialDelaySeconds: 5`
3. Apply the fixed manifest and ensure `transaction-processor` is in `Running` (1/1 Ready) state.

### Task 3: Imperative Pod with Command Override
1. Imperatively generate a pod named `event-streamer` in namespace `fintech`.
2. The pod must use image `busybox:1.36`.
3. Override its command so it executes:
   `["sh", "-c", "while true; do echo '[STREAM] Transaction event at $(date)' >> /tmp/stream.log; sleep 5; done"]`
4. Verify that `event-streamer` is `Running` and actively appending to `/tmp/stream.log`.""",
        "setup": """ssh controlplane '
kubectl delete namespace fintech --grace-period=0 --force 2>/dev/null || true
sudo mkdir -p /opt/k8s-manifests && sudo chmod 777 /opt/k8s-manifests
cat << "EOF" > /opt/k8s-manifests/broken-app.yaml
apiVersion: v1
kind: Pod
metadata:
name: transaction-processor
namespace: fintech
spec:
 containers:
 - name: processor
 image: nginx:1.25-alpine
 env:
 - MAX_WORKERS: 8
 - CACHE_DIR: /tmp/cache
 ports:
 - 8080
 - 9090
 resources:
  limits:
   memory: 128MB
   cpu: 200M
 readinessProbe:
   httpGet:
     path: /
     port: 80
   initialDelay: 5
EOF
'""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Namespace 'fintech'...${NC}"
NS_CHECK=$(ssh controlplane 'kubectl get ns fintech -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$NS_CHECK" == "Active" ]; then
  echo -e "${GREEN}[PASS] Namespace 'fintech' is Active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Namespace 'fintech' not found or inactive.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Repaired Pod 'transaction-processor'...${NC}"
POD1=$(ssh controlplane 'kubectl get pod transaction-processor -n fintech -o jsonpath="{.status.phase}_{.spec.containers[0].resources.limits.memory}_{.spec.containers[0].env[0].name}" 2>/dev/null || echo "NotFound"')
if [[ "$POD1" == Running* ]] && echo "$POD1" | grep -q "128Mi"; then
  echo -e "${GREEN}[PASS] Pod 'transaction-processor' is Running with validated resources and env schema.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod 'transaction-processor' not running or specification invalid. Status: '$POD1'.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Streamer pod 'event-streamer'...${NC}"
POD2=$(ssh controlplane 'kubectl get pod event-streamer -n fintech -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
LOG_CHECK=$(ssh controlplane 'kubectl exec -n fintech event-streamer -- cat /tmp/stream.log 2>/dev/null | grep STREAM || true')

if [ "$POD2" == "Running" ] && [ -n "$LOG_CHECK" ]; then
  echo -e "${GREEN}[PASS] Pod 'event-streamer' is Running and streaming logs successfully.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod 'event-streamer' not running or /tmp/stream.log missing.${NC}"
fi""",
        "solution": """1. Create namespace:
`kubectl create namespace fintech`

2. Fix `/opt/k8s-manifests/broken-app.yaml`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: transaction-processor
  namespace: fintech
spec:
  containers:
  - name: processor
    image: nginx:1.25-alpine
    env:
    - name: MAX_WORKERS
      value: "8"
    - name: CACHE_DIR
      value: "/tmp/cache"
    ports:
    - name: http
      containerPort: 8080
    - name: metrics
      containerPort: 9090
    resources:
      limits:
        memory: "128Mi"
        cpu: "200m"
    readinessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 5
```
Apply: `kubectl apply -f /opt/k8s-manifests/broken-app.yaml`

3. Deploy event-streamer:
```bash
kubectl run event-streamer -n fintech --image=busybox:1.36 --restart=Always -- \
  sh -c "while true; do echo '[STREAM] Transaction event at $(date)' >> /tmp/stream.log; sleep 5; done"
```""",
        "reset": """ssh controlplane '
kubectl delete namespace fintech --grace-period=0 --force 2>/dev/null || true
sudo rm -rf /opt/k8s-manifests
'""",
        "cka_title": 'Pod Internals & YAML Architecture',
        "cka_diff": 'Medium',
        "cka_time": '30m',
        "cka_tasks": """### Task 1: Create Namespace `fintech`
Create a namespace named `fintech`.

### Task 2: Fix the Broken Manifest & Deploy
1. Inspect `/opt/k8s-manifests/broken-app.yaml` on `controlplane`.
2. Fix all syntax, schema, and indentation errors:
   - Pod Name: `transaction-processor`
   - Namespace: `fintech`
   - Container Name: `processor`
   - Image: `nginx:1.25-alpine`
   - Environment variables: `MAX_WORKERS=8` and `CACHE_DIR=/tmp/cache`
   - Container Ports: `8080` (name: `http`) and `9090` (name: `metrics`)
   - Resource limits: memory `128Mi`, CPU `200m`
   - Readiness probe: HTTP GET `/` on port `80` (nginx default) with `initialDelaySeconds: 5`
3. Apply the fixed manifest and ensure `transaction-processor` is in `Running` (1/1 Ready) state.

### Task 3: Imperative Pod with Command Override
1. Imperatively generate a pod named `event-streamer` in namespace `fintech`.
2. The pod must use image `busybox:1.36`.
3. Override its command so it executes:
   `["sh", "-c", "while true; do echo '[STREAM] Transaction event at $(date)' >> /tmp/stream.log; sleep 5; done"]`
4. Verify that `event-streamer` is `Running` and actively appending to `/tmp/stream.log`.""",
        "cka_setup": """ssh controlplane '
kubectl delete namespace fintech --grace-period=0 --force 2>/dev/null || true
sudo mkdir -p /opt/k8s-manifests && sudo chmod 777 /opt/k8s-manifests
cat << "EOF" > /opt/k8s-manifests/broken-app.yaml
apiVersion: v1
kind: Pod
metadata:
name: transaction-processor
namespace: fintech
spec:
 containers:
 - name: processor
 image: nginx:1.25-alpine
 env:
 - MAX_WORKERS: 8
 - CACHE_DIR: /tmp/cache
 ports:
 - 8080
 - 9090
 resources:
  limits:
   memory: 128MB
   cpu: 200M
 readinessProbe:
   httpGet:
     path: /
     port: 80
   initialDelay: 5
EOF
'""",
        "cka_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Namespace 'fintech'...${NC}"
NS_CHECK=$(ssh controlplane 'kubectl get ns fintech -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$NS_CHECK" == "Active" ]; then
  echo -e "${GREEN}[PASS] Namespace 'fintech' is Active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Namespace 'fintech' not found or inactive.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Repaired Pod 'transaction-processor'...${NC}"
POD1=$(ssh controlplane 'kubectl get pod transaction-processor -n fintech -o jsonpath="{.status.phase}_{.spec.containers[0].resources.limits.memory}_{.spec.containers[0].env[0].name}" 2>/dev/null || echo "NotFound"')
if [[ "$POD1" == Running* ]] && echo "$POD1" | grep -q "128Mi"; then
  echo -e "${GREEN}[PASS] Pod 'transaction-processor' is Running with validated resources and env schema.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod 'transaction-processor' not running or specification invalid. Status: '$POD1'.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Streamer pod 'event-streamer'...${NC}"
POD2=$(ssh controlplane 'kubectl get pod event-streamer -n fintech -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
LOG_CHECK=$(ssh controlplane 'kubectl exec -n fintech event-streamer -- cat /tmp/stream.log 2>/dev/null | grep STREAM || true')

if [ "$POD2" == "Running" ] && [ -n "$LOG_CHECK" ]; then
  echo -e "${GREEN}[PASS] Pod 'event-streamer' is Running and streaming logs successfully.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod 'event-streamer' not running or /tmp/stream.log missing.${NC}"
fi""",
        "cka_solution": """1. Create namespace:
`kubectl create namespace fintech`

2. Fix `/opt/k8s-manifests/broken-app.yaml`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: transaction-processor
  namespace: fintech
spec:
  containers:
  - name: processor
    image: nginx:1.25-alpine
    env:
    - name: MAX_WORKERS
      value: "8"
    - name: CACHE_DIR
      value: "/tmp/cache"
    ports:
    - name: http
      containerPort: 8080
    - name: metrics
      containerPort: 9090
    resources:
      limits:
        memory: "128Mi"
        cpu: "200m"
    readinessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 5
```
Apply: `kubectl apply -f /opt/k8s-manifests/broken-app.yaml`

3. Deploy event-streamer:
```bash
kubectl run event-streamer -n fintech --image=busybox:1.36 --restart=Always -- \
  sh -c "while true; do echo '[STREAM] Transaction event at $(date)' >> /tmp/stream.log; sleep 5; done"
```""",
        "cka_reset": """ssh controlplane '
kubectl delete namespace fintech --grace-period=0 --force 2>/dev/null || true
sudo rm -rf /opt/k8s-manifests
'""",
    },
    {
        "day": 4,
        "date": '2026-09-17',
        "title": 'Multi-Container Pod Patterns & Init Containers',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Create Namespace `telemetry`
Create a namespace named `telemetry`.

### Task 2: Multi-Container Sidecar Pod (`order-service`)
Create a Pod named `order-service` in namespace `telemetry`:
1. Volume:
   - Name: `log-volume`
   - Type: `emptyDir: {}`
2. Container 1 (`app`):
   - Image: `busybox:1.36`
   - Command: `["sh", "-c", "while true; do echo "$(date) [ORDER] Transaction processed" >> /var/log/app/orders.log; sleep 2; done"]`
   - Mount: `log-volume` at `/var/log/app`
3. Container 2 (`logger`):
   - Image: `busybox:1.36`
   - Command: `["sh", "-c", "tail -n+1 -f /var/log/app/orders.log"]`
   - Mount: `log-volume` at `/var/log/app` (readOnly: true)

### Task 3: Init Container Dependency Gating (`web-portal`)
Create a Pod named `web-portal` in namespace `telemetry`:
1. Init Container (`db-wait`):
   - Image: `busybox:1.36`
   - Command: `["sh", "-c", "until [ -f /opt/data/ready.flag ]; do echo waiting for ready.flag; sleep 2; done"]`
   - Volume Mount: `data-vol` (emptyDir) at `/opt/data`
2. Application Container (`web`):
   - Image: `nginx:1.25-alpine`
   - Volume Mount: `data-vol` (emptyDir) at `/opt/data`
3. Simulate dependency completion by creating `/opt/data/ready.flag` or structuring the pod so it runs smoothly.""",
        "setup": """ssh controlplane '
kubectl delete namespace telemetry --grace-period=0 --force 2>/dev/null || true
kubectl create namespace telemetry
'""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Namespace 'telemetry'...${NC}"
NS_CHECK=$(ssh controlplane 'kubectl get ns telemetry -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$NS_CHECK" == "Active" ]; then
  echo -e "${GREEN}[PASS] Namespace 'telemetry' Active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Namespace 'telemetry' not found.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Sidecar Pod 'order-service'...${NC}"
C_COUNT=$(ssh controlplane 'kubectl get pod order-service -n telemetry -o jsonpath="{.spec.containers[*].name}" 2>/dev/null || true')
PHASE=$(ssh controlplane 'kubectl get pod order-service -n telemetry -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
LOG_TEST=$(ssh controlplane 'kubectl logs -n telemetry order-service -c logger --tail=5 2>/dev/null || true')

if [ "$PHASE" == "Running" ] && echo "$C_COUNT" | grep -qw "app" && echo "$C_COUNT" | grep -qw "logger" && echo "$LOG_TEST" | grep -q "ORDER"; then
  echo -e "${GREEN}[PASS] Multi-container pod 'order-service' running and logger streaming logs.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] order-service invalid or logger output missing. Phase: $PHASE, Containers: $C_COUNT.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Init Container Pod 'web-portal'...${NC}"
INIT_NAME=$(ssh controlplane 'kubectl get pod web-portal -n telemetry -o jsonpath="{.spec.initContainers[0].name}" 2>/dev/null || true')
if [ -n "$INIT_NAME" ]; then
  echo -e "${GREEN}[PASS] Init container '$INIT_NAME' defined on web-portal.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod web-portal missing or lacks init container.${NC}"
fi""",
        "solution": """1. Create namespace:
`kubectl create namespace telemetry`

2. Deploy `order-service`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: order-service
  namespace: telemetry
spec:
  volumes:
  - name: log-volume
    emptyDir: {}
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo "$(date) [ORDER] Transaction processed" >> /var/log/app/orders.log; sleep 2; done"]
    volumeMounts:
    - name: log-volume
      mountPath: /var/log/app
  - name: logger
    image: busybox:1.36
    command: ["sh", "-c", "tail -n+1 -f /var/log/app/orders.log"]
    volumeMounts:
    - name: log-volume
      mountPath: /var/log/app
      readOnly: true
```

3. Deploy `web-portal`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-portal
  namespace: telemetry
spec:
  volumes:
  - name: data-vol
    emptyDir: {}
  initContainers:
  - name: db-wait
    image: busybox:1.36
    command: ["sh", "-c", "echo ready > /opt/data/ready.flag"]
    volumeMounts:
    - name: data-vol
      mountPath: /opt/data
  containers:
  - name: web
    image: nginx:1.25-alpine
    volumeMounts:
    - name: data-vol
      mountPath: /opt/data
```""",
        "reset": "ssh controlplane 'kubectl delete namespace telemetry --grace-period=0 --force 2>/dev/null || true'",
        "cka_title": 'Multi-Container Pod Patterns & Init Containers',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Create Namespace `telemetry`
Create a namespace named `telemetry`.

### Task 2: Multi-Container Sidecar Pod (`order-service`)
Create a Pod named `order-service` in namespace `telemetry`:
1. Volume:
   - Name: `log-volume`
   - Type: `emptyDir: {}`
2. Container 1 (`app`):
   - Image: `busybox:1.36`
   - Command: `["sh", "-c", "while true; do echo "$(date) [ORDER] Transaction processed" >> /var/log/app/orders.log; sleep 2; done"]`
   - Mount: `log-volume` at `/var/log/app`
3. Container 2 (`logger`):
   - Image: `busybox:1.36`
   - Command: `["sh", "-c", "tail -n+1 -f /var/log/app/orders.log"]`
   - Mount: `log-volume` at `/var/log/app` (readOnly: true)

### Task 3: Init Container Dependency Gating (`web-portal`)
Create a Pod named `web-portal` in namespace `telemetry`:
1. Init Container (`db-wait`):
   - Image: `busybox:1.36`
   - Command: `["sh", "-c", "until [ -f /opt/data/ready.flag ]; do echo waiting for ready.flag; sleep 2; done"]`
   - Volume Mount: `data-vol` (emptyDir) at `/opt/data`
2. Application Container (`web`):
   - Image: `nginx:1.25-alpine`
   - Volume Mount: `data-vol` (emptyDir) at `/opt/data`
3. Simulate dependency completion by creating `/opt/data/ready.flag` or structuring the pod so it runs smoothly.""",
        "cka_setup": """ssh controlplane '
kubectl delete namespace telemetry --grace-period=0 --force 2>/dev/null || true
kubectl create namespace telemetry
'""",
        "cka_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Namespace 'telemetry'...${NC}"
NS_CHECK=$(ssh controlplane 'kubectl get ns telemetry -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$NS_CHECK" == "Active" ]; then
  echo -e "${GREEN}[PASS] Namespace 'telemetry' Active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Namespace 'telemetry' not found.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Sidecar Pod 'order-service'...${NC}"
C_COUNT=$(ssh controlplane 'kubectl get pod order-service -n telemetry -o jsonpath="{.spec.containers[*].name}" 2>/dev/null || true')
PHASE=$(ssh controlplane 'kubectl get pod order-service -n telemetry -o jsonpath="{.status.phase}" 2>/dev/null || echo "NotFound"')
LOG_TEST=$(ssh controlplane 'kubectl logs -n telemetry order-service -c logger --tail=5 2>/dev/null || true')

if [ "$PHASE" == "Running" ] && echo "$C_COUNT" | grep -qw "app" && echo "$C_COUNT" | grep -qw "logger" && echo "$LOG_TEST" | grep -q "ORDER"; then
  echo -e "${GREEN}[PASS] Multi-container pod 'order-service' running and logger streaming logs.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] order-service invalid or logger output missing. Phase: $PHASE, Containers: $C_COUNT.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Init Container Pod 'web-portal'...${NC}"
INIT_NAME=$(ssh controlplane 'kubectl get pod web-portal -n telemetry -o jsonpath="{.spec.initContainers[0].name}" 2>/dev/null || true')
if [ -n "$INIT_NAME" ]; then
  echo -e "${GREEN}[PASS] Init container '$INIT_NAME' defined on web-portal.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod web-portal missing or lacks init container.${NC}"
fi""",
        "cka_solution": """1. Create namespace:
`kubectl create namespace telemetry`

2. Deploy `order-service`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: order-service
  namespace: telemetry
spec:
  volumes:
  - name: log-volume
    emptyDir: {}
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo "$(date) [ORDER] Transaction processed" >> /var/log/app/orders.log; sleep 2; done"]
    volumeMounts:
    - name: log-volume
      mountPath: /var/log/app
  - name: logger
    image: busybox:1.36
    command: ["sh", "-c", "tail -n+1 -f /var/log/app/orders.log"]
    volumeMounts:
    - name: log-volume
      mountPath: /var/log/app
      readOnly: true
```

3. Deploy `web-portal`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-portal
  namespace: telemetry
spec:
  volumes:
  - name: data-vol
    emptyDir: {}
  initContainers:
  - name: db-wait
    image: busybox:1.36
    command: ["sh", "-c", "echo ready > /opt/data/ready.flag"]
    volumeMounts:
    - name: data-vol
      mountPath: /opt/data
  containers:
  - name: web
    image: nginx:1.25-alpine
    volumeMounts:
    - name: data-vol
      mountPath: /opt/data
```""",
        "cka_reset": "ssh controlplane 'kubectl delete namespace telemetry --grace-period=0 --force 2>/dev/null || true'",
    },
    {
        "day": 5,
        "date": '2026-09-18',
        "title": 'Fast Imperative CLI Mastery with Kubectl',
        "diff": 'Medium (Speed Drill)',
        "time": '25m',
        "tasks": """### Task 1: Terminal Supercharger Configuration
On `controlplane`, configure the environment in `~/.bashrc`:
1. Alias `k=kubectl` with completion: `alias k=kubectl` and `complete -o default -F __start_kubectl k`
2. Shorthand export variables:
   - `export do="--dry-run=client -o yaml"`
   - `export now="--force --grace-period=0"`
3. Configure `~/.vimrc` with:
   - `set tabstop=2`
   - `set shiftwidth=2`
   - `set expandtab`

### Task 2: High-Speed Imperative Resource Creation
Without writing YAML files from scratch, imperatively deploy in namespace `speed-drill`:
1. Deployment `cache-redis`: 3 replicas, image `redis:7-alpine`.
2. ClusterIP service `cache-service`: exposing deployment `cache-redis` on port `6379`.
3. Secret `redis-secret`: with key `auth=supersecret`.

### Task 3: Declarative Clean Export
Export the `cache-redis` deployment manifest to `/opt/k8s/clean-cache.yaml` stripped of cluster runtime fields (`status`, `managedFields`, `creationTimestamp`).""",
        "setup": """ssh controlplane '
kubectl delete namespace speed-drill --grace-period=0 --force 2>/dev/null || true
kubectl create namespace speed-drill
sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
rm -f /opt/k8s/clean-cache.yaml
'""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Shell environment & vimrc...${NC}"
BASH_CHECK=$(ssh controlplane 'grep -E "alias k=kubectl" ~/.bashrc 2>/dev/null || true')
VIM_CHECK=$(ssh controlplane 'grep -E "tabstop=2" ~/.vimrc 2>/dev/null || true')
if [ -n "$BASH_CHECK" ] && [ -n "$VIM_CHECK" ]; then
  echo -e "${GREEN}[PASS] Shell alias and ~/.vimrc configured.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] ~/.bashrc or ~/.vimrc missing required settings.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Imperative deployment, service, secret...${NC}"
DEPLOY=$(ssh controlplane 'kubectl get deploy cache-redis -n speed-drill -o jsonpath="{.spec.replicas}" 2>/dev/null || echo "0"')
SVC=$(ssh controlplane 'kubectl get svc cache-service -n speed-drill -o jsonpath="{.spec.ports[0].port}" 2>/dev/null || echo "0"')
SEC=$(ssh controlplane 'kubectl get secret redis-secret -n speed-drill -o jsonpath="{.data.auth}" 2>/dev/null || echo "none"')

if [ "$DEPLOY" == "3" ] && [ "$SVC" == "6379" ] && [ "$SEC" != "none" ]; then
  echo -e "${GREEN}[PASS] cache-redis (3 replicas), cache-service (6379), and redis-secret verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Resources incomplete: deploy replicas=$DEPLOY, svc port=$SVC, secret=$SEC.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Clean YAML export...${NC}"
EXPORT_FILE=$(ssh controlplane 'cat /opt/k8s/clean-cache.yaml 2>/dev/null || true')
if [ -n "$EXPORT_FILE" ] && ! echo "$EXPORT_FILE" | grep -q "managedFields"; then
  echo -e "${GREEN}[PASS] /opt/k8s/clean-cache.yaml is clean of managedFields.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/k8s/clean-cache.yaml missing or contains managedFields.${NC}"
fi""",
        "solution": """1. Update `~/.bashrc` and `~/.vimrc`:
```bash
echo "source <(kubectl completion bash)" >> ~/.bashrc
echo "alias k=kubectl" >> ~/.bashrc
echo "complete -o default -F __start_kubectl k" >> ~/.bashrc
echo 'export do="--dry-run=client -o yaml"' >> ~/.bashrc
echo 'export now="--force --grace-period=0"' >> ~/.bashrc

cat << 'EOF' >> ~/.vimrc
set tabstop=2
set shiftwidth=2
set expandtab
EOF
source ~/.bashrc
```

2. Rapid imperative commands:
```bash
k create namespace speed-drill
k create deploy cache-redis -n speed-drill --image=redis:7-alpine --replicas=3
k expose deploy cache-redis -n speed-drill --name=cache-service --port=6379
k create secret generic redis-secret -n speed-drill --from-literal=auth=supersecret
```

3. Export clean manifest:
```bash
k get deploy cache-redis -n speed-drill -o yaml | grep -v 'managedFields:' > /opt/k8s/clean-cache.yaml
```""",
        "reset": """ssh controlplane '
kubectl delete namespace speed-drill --grace-period=0 --force 2>/dev/null || true
rm -f /opt/k8s/clean-cache.yaml
'""",
        "cka_title": 'Fast Imperative CLI Mastery with Kubectl',
        "cka_diff": 'Medium (Speed Drill)',
        "cka_time": '25m',
        "cka_tasks": """### Task 1: Terminal Supercharger Configuration
On `controlplane`, configure the environment in `~/.bashrc`:
1. Alias `k=kubectl` with completion: `alias k=kubectl` and `complete -o default -F __start_kubectl k`
2. Shorthand export variables:
   - `export do="--dry-run=client -o yaml"`
   - `export now="--force --grace-period=0"`
3. Configure `~/.vimrc` with:
   - `set tabstop=2`
   - `set shiftwidth=2`
   - `set expandtab`

### Task 2: High-Speed Imperative Resource Creation
Without writing YAML files from scratch, imperatively deploy in namespace `speed-drill`:
1. Deployment `cache-redis`: 3 replicas, image `redis:7-alpine`.
2. ClusterIP service `cache-service`: exposing deployment `cache-redis` on port `6379`.
3. Secret `redis-secret`: with key `auth=supersecret`.

### Task 3: Declarative Clean Export
Export the `cache-redis` deployment manifest to `/opt/k8s/clean-cache.yaml` stripped of cluster runtime fields (`status`, `managedFields`, `creationTimestamp`).""",
        "cka_setup": """ssh controlplane '
kubectl delete namespace speed-drill --grace-period=0 --force 2>/dev/null || true
kubectl create namespace speed-drill
sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
rm -f /opt/k8s/clean-cache.yaml
'""",
        "cka_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Shell environment & vimrc...${NC}"
BASH_CHECK=$(ssh controlplane 'grep -E "alias k=kubectl" ~/.bashrc 2>/dev/null || true')
VIM_CHECK=$(ssh controlplane 'grep -E "tabstop=2" ~/.vimrc 2>/dev/null || true')
if [ -n "$BASH_CHECK" ] && [ -n "$VIM_CHECK" ]; then
  echo -e "${GREEN}[PASS] Shell alias and ~/.vimrc configured.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] ~/.bashrc or ~/.vimrc missing required settings.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Imperative deployment, service, secret...${NC}"
DEPLOY=$(ssh controlplane 'kubectl get deploy cache-redis -n speed-drill -o jsonpath="{.spec.replicas}" 2>/dev/null || echo "0"')
SVC=$(ssh controlplane 'kubectl get svc cache-service -n speed-drill -o jsonpath="{.spec.ports[0].port}" 2>/dev/null || echo "0"')
SEC=$(ssh controlplane 'kubectl get secret redis-secret -n speed-drill -o jsonpath="{.data.auth}" 2>/dev/null || echo "none"')

if [ "$DEPLOY" == "3" ] && [ "$SVC" == "6379" ] && [ "$SEC" != "none" ]; then
  echo -e "${GREEN}[PASS] cache-redis (3 replicas), cache-service (6379), and redis-secret verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Resources incomplete: deploy replicas=$DEPLOY, svc port=$SVC, secret=$SEC.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Clean YAML export...${NC}"
EXPORT_FILE=$(ssh controlplane 'cat /opt/k8s/clean-cache.yaml 2>/dev/null || true')
if [ -n "$EXPORT_FILE" ] && ! echo "$EXPORT_FILE" | grep -q "managedFields"; then
  echo -e "${GREEN}[PASS] /opt/k8s/clean-cache.yaml is clean of managedFields.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/k8s/clean-cache.yaml missing or contains managedFields.${NC}"
fi""",
        "cka_solution": """1. Update `~/.bashrc` and `~/.vimrc`:
```bash
echo "source <(kubectl completion bash)" >> ~/.bashrc
echo "alias k=kubectl" >> ~/.bashrc
echo "complete -o default -F __start_kubectl k" >> ~/.bashrc
echo 'export do="--dry-run=client -o yaml"' >> ~/.bashrc
echo 'export now="--force --grace-period=0"' >> ~/.bashrc

cat << 'EOF' >> ~/.vimrc
set tabstop=2
set shiftwidth=2
set expandtab
EOF
source ~/.bashrc
```

2. Rapid imperative commands:
```bash
k create namespace speed-drill
k create deploy cache-redis -n speed-drill --image=redis:7-alpine --replicas=3
k expose deploy cache-redis -n speed-drill --name=cache-service --port=6379
k create secret generic redis-secret -n speed-drill --from-literal=auth=supersecret
```

3. Export clean manifest:
```bash
k get deploy cache-redis -n speed-drill -o yaml | grep -v 'managedFields:' > /opt/k8s/clean-cache.yaml
```""",
        "cka_reset": """ssh controlplane '
kubectl delete namespace speed-drill --grace-period=0 --force 2>/dev/null || true
rm -f /opt/k8s/clean-cache.yaml
'""",
    },
    {
        "day": 6,
        "date": '2026-09-19',
        "title": 'Week 1 Integration & Milestone Triathlon',
        "diff": 'Hard (Milestone Assessment 1)',
        "time": '45m',
        "tasks": """### Milestone 1 Triathlon Tasks:
1. **Control-Plane Recovery:**
   On `controlplane`, static pod manifests were moved to `/etc/kubernetes/manifests_broken`. Restore them back to `/etc/kubernetes/manifests` and restart kubelet so control-plane static pods recover.
2. **Multi-Tier Workload Pipeline:**
   In namespace `triathlon-w1`:
   - Deploy `web-ui` with 2 replicas, image `nginx:1.25-alpine`, container port 80, CPU limit `150m`, memory limit `128Mi`.
   - Expose via ClusterIP service `web-ui-svc` on port `80`.
3. **ETCD Disaster Recovery Backup:**
   Create an etcd point-in-time snapshot saved to `/opt/backup/triathlon-etcd.db` using TLS credentials.
4. **Worker Static Pod:**
   Deploy a static pod on `node01` named `w1-worker-agent` (image: `busybox:1.36`, command `["sh", "-c", "sleep 3600"]`). Verify it appears in `kubectl get pods -A` as `w1-worker-agent-node01`.""",
        "setup": """ssh controlplane '
kubectl delete namespace triathlon-w1 --grace-period=0 --force 2>/dev/null || true
sudo mkdir -p /opt/backup && sudo chmod 777 /opt/backup
rm -f /opt/backup/triathlon-etcd.db
sudo bash -c "
if [ -d /etc/kubernetes/manifests ] && [ ! -d /etc/kubernetes/manifests_broken ]; then
  mv /etc/kubernetes/manifests /etc/kubernetes/manifests_broken
  systemctl restart kubelet
fi
"
'
ssh node01 '
sudo rm -f /etc/kubernetes/manifests/w1-worker-agent.yaml
POD_ID=$(sudo crictl pods -q --name w1-worker-agent-node01 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'""",
        "verify": """SCORE=0; TOTAL=4

echo -e "${BOLD}Checking Task 1: Control plane static pods...${NC}"
API_POD=$(ssh controlplane 'kubectl get pods -n kube-system -l component=kube-apiserver -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$API_POD" == "Running" ]; then
  echo -e "${GREEN}[PASS] Control-plane kube-apiserver is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] kube-apiserver status: $API_POD (manifests may still be misplaced).${NC}"
fi

echo -e "${BOLD}Checking Task 2: Workload in triathlon-w1...${NC}"
REPLICAS=$(ssh controlplane 'kubectl get deploy web-ui -n triathlon-w1 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
SVC=$(ssh controlplane 'kubectl get svc web-ui-svc -n triathlon-w1 -o jsonpath="{.spec.clusterIP}" 2>/dev/null || echo "None"')
if [ "$REPLICAS" == "2" ] && [ "$SVC" != "None" ]; then
  echo -e "${GREEN}[PASS] Deployment web-ui (2/2 ready) and service web-ui-svc verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Workload incomplete: replicas=$REPLICAS, svc=$SVC.${NC}"
fi

echo -e "${BOLD}Checking Task 3: ETCD snapshot...${NC}"
SNAP=$(ssh controlplane 'sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/triathlon-etcd.db --write-out=table 2>/dev/null || true')
if echo "$SNAP" | grep -qiE "REVISION|TOTAL KEYS"; then
  echo -e "${GREEN}[PASS] /opt/backup/triathlon-etcd.db is a valid snapshot.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Snapshot missing or invalid.${NC}"
fi

echo -e "${BOLD}Checking Task 4: Worker static pod on node01...${NC}"
AGENT=$(ssh controlplane 'kubectl get pods -A 2>/dev/null | grep "w1-worker-agent-node01" || true')
if [ -n "$AGENT" ] && echo "$AGENT" | grep -q "Running"; then
  echo -e "${GREEN}[PASS] Static pod w1-worker-agent-node01 is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Static pod w1-worker-agent-node01 not running.${NC}"
fi""",
        "solution": """1. Restore manifests directory:
```bash
sudo mv /etc/kubernetes/manifests_broken /etc/kubernetes/manifests
sudo systemctl restart kubelet
```

2. Multi-tier application:
```bash
kubectl create ns triathlon-w1
kubectl create deploy web-ui -n triathlon-w1 --image=nginx:1.25-alpine --replicas=2
kubectl set resources deploy web-ui -n triathlon-w1 --limits=cpu=150m,memory=128Mi
kubectl expose deploy web-ui -n triathlon-w1 --name=web-ui-svc --port=80
```

3. ETCD snapshot:
```bash
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   snapshot save /opt/backup/triathlon-etcd.db
```

4. Worker static pod on `node01`:
`ssh node01`
```bash
sudo tee /etc/kubernetes/manifests/w1-worker-agent.yaml << 'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: w1-worker-agent
spec:
  containers:
  - name: agent
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
EOF
```""",
        "reset": """ssh controlplane '
if [ -d /etc/kubernetes/manifests_broken ]; then
  sudo mv /etc/kubernetes/manifests_broken /etc/kubernetes/manifests
  sudo systemctl restart kubelet
fi
for i in $(seq 1 30); do
  kubectl get nodes >/dev/null 2>&1 && break
  sleep 1
done
kubectl delete namespace triathlon-w1 --grace-period=0 --force 2>/dev/null || true
kubectl delete pod w1-worker-agent-node01 --force --grace-period=0 2>/dev/null || true
sudo rm -rf /opt/backup
'
ssh node01 '
sudo rm -f /etc/kubernetes/manifests/w1-worker-agent.yaml
POD_ID=$(sudo crictl pods -q --name w1-worker-agent-node01 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'""",
        "cka_title": 'Week 1 Integration & Milestone Triathlon',
        "cka_diff": 'Hard (Milestone Assessment 1)',
        "cka_time": '45m',
        "cka_tasks": """### Milestone 1 Triathlon Tasks:
1. **Control-Plane Recovery:**
   On `controlplane`, static pod manifests were moved to `/etc/kubernetes/manifests_broken`. Restore them back to `/etc/kubernetes/manifests` and restart kubelet so control-plane static pods recover.
2. **Multi-Tier Workload Pipeline:**
   In namespace `triathlon-w1`:
   - Deploy `web-ui` with 2 replicas, image `nginx:1.25-alpine`, container port 80, CPU limit `150m`, memory limit `128Mi`.
   - Expose via ClusterIP service `web-ui-svc` on port `80`.
3. **ETCD Disaster Recovery Backup:**
   Create an etcd point-in-time snapshot saved to `/opt/backup/triathlon-etcd.db` using TLS credentials.
4. **Worker Static Pod:**
   Deploy a static pod on `node01` named `w1-worker-agent` (image: `busybox:1.36`, command `["sh", "-c", "sleep 3600"]`). Verify it appears in `kubectl get pods -A` as `w1-worker-agent-node01`.""",
        "cka_setup": """ssh controlplane '
kubectl delete namespace triathlon-w1 --grace-period=0 --force 2>/dev/null || true
sudo mkdir -p /opt/backup && sudo chmod 777 /opt/backup
rm -f /opt/backup/triathlon-etcd.db
sudo bash -c "
if [ -d /etc/kubernetes/manifests ] && [ ! -d /etc/kubernetes/manifests_broken ]; then
  mv /etc/kubernetes/manifests /etc/kubernetes/manifests_broken
  systemctl restart kubelet
fi
"
'
ssh node01 '
sudo rm -f /etc/kubernetes/manifests/w1-worker-agent.yaml
POD_ID=$(sudo crictl pods -q --name w1-worker-agent-node01 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'""",
        "cka_verify": """SCORE=0; TOTAL=4

echo -e "${BOLD}Checking Task 1: Control plane static pods...${NC}"
API_POD=$(ssh controlplane 'kubectl get pods -n kube-system -l component=kube-apiserver -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "NotFound"')
if [ "$API_POD" == "Running" ]; then
  echo -e "${GREEN}[PASS] Control-plane kube-apiserver is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] kube-apiserver status: $API_POD (manifests may still be misplaced).${NC}"
fi

echo -e "${BOLD}Checking Task 2: Workload in triathlon-w1...${NC}"
REPLICAS=$(ssh controlplane 'kubectl get deploy web-ui -n triathlon-w1 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
SVC=$(ssh controlplane 'kubectl get svc web-ui-svc -n triathlon-w1 -o jsonpath="{.spec.clusterIP}" 2>/dev/null || echo "None"')
if [ "$REPLICAS" == "2" ] && [ "$SVC" != "None" ]; then
  echo -e "${GREEN}[PASS] Deployment web-ui (2/2 ready) and service web-ui-svc verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Workload incomplete: replicas=$REPLICAS, svc=$SVC.${NC}"
fi

echo -e "${BOLD}Checking Task 3: ETCD snapshot...${NC}"
SNAP=$(ssh controlplane 'sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/triathlon-etcd.db --write-out=table 2>/dev/null || true')
if echo "$SNAP" | grep -qiE "REVISION|TOTAL KEYS"; then
  echo -e "${GREEN}[PASS] /opt/backup/triathlon-etcd.db is a valid snapshot.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Snapshot missing or invalid.${NC}"
fi

echo -e "${BOLD}Checking Task 4: Worker static pod on node01...${NC}"
AGENT=$(ssh controlplane 'kubectl get pods -A 2>/dev/null | grep "w1-worker-agent-node01" || true')
if [ -n "$AGENT" ] && echo "$AGENT" | grep -q "Running"; then
  echo -e "${GREEN}[PASS] Static pod w1-worker-agent-node01 is Running.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Static pod w1-worker-agent-node01 not running.${NC}"
fi""",
        "cka_solution": """1. Restore manifests directory:
```bash
sudo mv /etc/kubernetes/manifests_broken /etc/kubernetes/manifests
sudo systemctl restart kubelet
```

2. Multi-tier application:
```bash
kubectl create ns triathlon-w1
kubectl create deploy web-ui -n triathlon-w1 --image=nginx:1.25-alpine --replicas=2
kubectl set resources deploy web-ui -n triathlon-w1 --limits=cpu=150m,memory=128Mi
kubectl expose deploy web-ui -n triathlon-w1 --name=web-ui-svc --port=80
```

3. ETCD snapshot:
```bash
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   snapshot save /opt/backup/triathlon-etcd.db
```

4. Worker static pod on `node01`:
`ssh node01`
```bash
sudo tee /etc/kubernetes/manifests/w1-worker-agent.yaml << 'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: w1-worker-agent
spec:
  containers:
  - name: agent
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
EOF
```""",
        "cka_reset": """ssh controlplane '
if [ -d /etc/kubernetes/manifests_broken ]; then
  sudo mv /etc/kubernetes/manifests_broken /etc/kubernetes/manifests
  sudo systemctl restart kubelet
fi
for i in $(seq 1 30); do
  kubectl get nodes >/dev/null 2>&1 && break
  sleep 1
done
kubectl delete namespace triathlon-w1 --grace-period=0 --force 2>/dev/null || true
kubectl delete pod w1-worker-agent-node01 --force --grace-period=0 2>/dev/null || true
sudo rm -rf /opt/backup
'
ssh node01 '
sudo rm -f /etc/kubernetes/manifests/w1-worker-agent.yaml
POD_ID=$(sudo crictl pods -q --name w1-worker-agent-node01 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'""",
    },
]
