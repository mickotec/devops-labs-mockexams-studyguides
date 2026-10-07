"""
Lab definitions for Week 3
"""

WEEK_3_LABS = [
    # Day 1
    {
        "day": 1,
        "date": "2026-10-12",
        "cka_title": "Manual Scheduling, Labels & Selectors",
        "cka_diff": "Medium",
        "cka_time": "35m",
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

        "lfcs_title": "Linux Boot Architecture & GRUB2",
        "lfcs_diff": "Medium",
        "lfcs_time": "35m",
        "lfcs_tasks": """### Task 1: GRUB Configuration Tuning
1. In `/etc/default/grub`, modify `GRUB_CMDLINE_LINUX_DEFAULT` to append the kernel boot parameter `consoleblank=600`.
2. Change the default boot timeout (`GRUB_TIMEOUT`) to `8` seconds.
3. Run `sudo update-grub` to regenerate `/boot/grub/grub.cfg`.

### Task 2: System Boot Diagnostic Report
Extract boot diagnostics to `/var/tmp/boot_diagnostic.txt`:
1. Use `dmesg` or `journalctl -b` to find the kernel command-line arguments used during current boot and save the line containing `Command line:` or `Kernel command line:` as the first line of `/var/tmp/boot_diagnostic.txt`.
2. Append the UUID of the root filesystem mounted at `/` (use `findmnt` or `lsblk`).""",
        "lfcs_setup": """sudo rm -f /var/tmp/boot_diagnostic.txt
if [ ! -f /etc/default/grub.bak ]; then
  sudo cp /etc/default/grub /etc/default/grub.bak
fi""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Check Task 1: GRUB configuration and generated grub.cfg
GRUB_PARAM=$(grep 'consoleblank=600' /etc/default/grub 2>/dev/null || true)
GRUB_TIME=$(grep 'GRUB_TIMEOUT=8' /etc/default/grub 2>/dev/null || true)
GRUB_CFG=$(sudo grep 'consoleblank=600' /boot/grub/grub.cfg 2>/dev/null || true)

if [ -n "$GRUB_PARAM" ] && [ -n "$GRUB_TIME" ] && [ -n "$GRUB_CFG" ]; then
  echo -e "${GREEN}[PASS] Task 1: GRUB default params and regenerated grub.cfg verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: GRUB config missing consoleblank=600, TIMEOUT=8, or update-grub not executed.${NC}"
fi

# Check Task 2: boot diagnostic report
if [ -f /var/tmp/boot_diagnostic.txt ] && grep -qiE "BOOT_IMAGE|vmlinuz|Command line" /var/tmp/boot_diagnostic.txt && grep -qiE "UUID=" /var/tmp/boot_diagnostic.txt; then
  echo -e "${GREEN}[PASS] Task 2: Boot diagnostic report verified with kernel cmdline and root UUID.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/boot_diagnostic.txt missing or incomplete.${NC}"
fi""",
        "lfcs_solution": """1. Edit `/etc/default/grub`:
Set `GRUB_TIMEOUT=8`
Update `GRUB_CMDLINE_LINUX_DEFAULT="... consoleblank=600"`
Run: `sudo update-grub`

2. Generate report:
`journalctl -b -k | grep -m1 -E "Command line|BOOT_IMAGE" > /var/tmp/boot_diagnostic.txt`
`findmnt / -no UUID | awk '{print "UUID="$1}' >> /var/tmp/boot_diagnostic.txt`""",
        "lfcs_reset": """if [ -f /etc/default/grub.bak ]; then
  sudo cp /etc/default/grub.bak /etc/default/grub
  sudo update-grub
fi
sudo rm -f /var/tmp/boot_diagnostic.txt"""
    },

    # Day 2
    {
        "day": 2,
        "date": "2026-10-13",
        "cka_title": "Taints, Tolerations & Node Affinity",
        "cka_diff": "Medium",
        "cka_time": "35m",
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
TAINT=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.spec.taints[?(@.key==\"workload\")].value}" 2>/dev/null || echo "None"')
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

        "lfcs_title": "Systemd Targets & Runlevel Management",
        "lfcs_diff": "Medium",
        "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Inspect and Set Default Target
1. Verify the current default systemd target.
2. Set the default system target to `multi-user.target` using `systemctl set-default`.

### Task 2: Create Custom Target
Create a custom systemd target unit file at `/etc/systemd/system/maintenance.target`:
- Description: `Maintenance Mode Target`
- Requires: `multi-user.target`
- Reload systemd manager configuration (`systemctl daemon-reload`).

### Task 3: Target Isolation Verification
Verify that `multi-user.target` is the active default target and record output of `systemctl get-default` into `/var/tmp/default_target.txt`.""",
        "lfcs_setup": """sudo rm -f /etc/systemd/system/maintenance.target /var/tmp/default_target.txt
sudo systemctl daemon-reload""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: default target is multi-user.target
DEF_TARGET=$(systemctl get-default 2>/dev/null || true)
if [ "$DEF_TARGET" == "multi-user.target" ]; then
  echo -e "${GREEN}[PASS] Task 1: Default target is multi-user.target.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Default target is '$DEF_TARGET' (expected multi-user.target).${NC}"
fi

# Task 2: maintenance.target unit file
if [ -f /etc/systemd/system/maintenance.target ] && grep -qi "Maintenance Mode" /etc/systemd/system/maintenance.target; then
  echo -e "${GREEN}[PASS] Task 2: /etc/systemd/system/maintenance.target created and validated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: maintenance.target missing or invalid description.${NC}"
fi

# Task 3: /var/tmp/default_target.txt
if [ -f /var/tmp/default_target.txt ] && grep -q "multi-user.target" /var/tmp/default_target.txt; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/default_target.txt recorded accurately.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/default_target.txt missing or empty.${NC}"
fi""",
        "lfcs_solution": """1. Set default target:
`sudo systemctl set-default multi-user.target`

2. Create `/etc/systemd/system/maintenance.target`:
```ini
[Unit]
Description=Maintenance Mode Target
Requires=multi-user.target
After=multi-user.target
AllowIsolate=yes
```
`sudo systemctl daemon-reload`

3. Save status:
`systemctl get-default > /var/tmp/default_target.txt`""",
        "lfcs_reset": """sudo rm -f /etc/systemd/system/maintenance.target /var/tmp/default_target.txt
sudo systemctl daemon-reload"""
    },

    # Day 3
    {
        "day": 3,
        "date": "2026-10-14",
        "cka_title": "Resource Requirements, Limits & LimitRanges",
        "cka_diff": "Medium",
        "cka_time": "35m",
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

        "lfcs_title": "Creating & Managing Systemd Services",
        "lfcs_diff": "Medium",
        "lfcs_time": "35m",
        "lfcs_tasks": """### Task 1: Create Worker Script
Create a background script at `/usr/local/bin/worker-daemon.sh`:
- Make it executable (`chmod 755`).
- Contents: An infinite loop that writes `Worker ping: $(date)` to `/var/log/worker-daemon.log` every 3 seconds.

### Task 2: Create Systemd Service Unit
Create `/etc/systemd/system/worker-daemon.service`:
- `Description=Worker Daemon Service`
- `ExecStart=/usr/local/bin/worker-daemon.sh`
- `Restart=always`
- `[Install]` section with `WantedBy=multi-user.target`

### Task 3: Service Activation
1. Reload systemd (`systemctl daemon-reload`).
2. Enable and start `worker-daemon.service`.
3. Verify the service is active and the log file `/var/log/worker-daemon.log` is receiving entries.""",
        "lfcs_setup": """sudo systemctl stop worker-daemon.service 2>/dev/null || true
sudo systemctl disable worker-daemon.service 2>/dev/null || true
sudo rm -f /etc/systemd/system/worker-daemon.service /usr/local/bin/worker-daemon.sh /var/log/worker-daemon.log
sudo systemctl daemon-reload""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: script exists and executable
if [ -x /usr/local/bin/worker-daemon.sh ]; then
  echo -e "${GREEN}[PASS] Task 1: /usr/local/bin/worker-daemon.sh executable verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /usr/local/bin/worker-daemon.sh missing or not executable.${NC}"
fi

# Task 2: service file
if [ -f /etc/systemd/system/worker-daemon.service ] && grep -qi "Restart=always" /etc/systemd/system/worker-daemon.service; then
  echo -e "${GREEN}[PASS] Task 2: worker-daemon.service unit file configured.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Service unit file missing or Restart directive absent.${NC}"
fi

# Task 3: service is running and logging
IS_ACTIVE=$(systemctl is-active worker-daemon.service 2>/dev/null || echo "inactive")
if [ "$IS_ACTIVE" == "active" ] && [ -f /var/log/worker-daemon.log ] && [ -s /var/log/worker-daemon.log ]; then
  echo -e "${GREEN}[PASS] Task 3: worker-daemon.service is active and writing to /var/log/worker-daemon.log.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Service is $IS_ACTIVE or /var/log/worker-daemon.log empty.${NC}"
fi""",
        "lfcs_solution": """1. Create script `/usr/local/bin/worker-daemon.sh`:
```bash
#!/usr/bin/env bash
while true; do
  echo "Worker ping: $(date)" >> /var/log/worker-daemon.log
  sleep 3
done
```
`sudo chmod 755 /usr/local/bin/worker-daemon.sh`

2. Create `/etc/systemd/system/worker-daemon.service`:
```ini
[Unit]
Description=Worker Daemon Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/worker-daemon.sh
Restart=always

[Install]
WantedBy=multi-user.target
```

3. Enable and start:
`sudo systemctl daemon-reload`
`sudo systemctl enable --now worker-daemon.service`""",
        "lfcs_reset": """sudo systemctl stop worker-daemon.service 2>/dev/null || true
sudo systemctl disable worker-daemon.service 2>/dev/null || true
sudo rm -f /etc/systemd/system/worker-daemon.service /usr/local/bin/worker-daemon.sh /var/log/worker-daemon.log
sudo systemctl daemon-reload"""
    },

    # Day 4
    {
        "day": 4,
        "date": "2026-10-15",
        "cka_title": "DaemonSets & Static Pods Architecture",
        "cka_diff": "Medium",
        "cka_time": "35m",
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

        "lfcs_title": "Process Diagnostics & Signal Management",
        "lfcs_diff": "Medium",
        "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Rogue Process Termination
A rogue process simulating a memory leak (`rogue-sim`) is running in the background.
1. Locate its PID using `pgrep` or `ps`.
2. Terminate it gracefully with `SIGTERM` (15); if it remains, force terminate with `SIGKILL` (9).

### Task 2: Nice Priority Adjustment
A background workload process `batch-calc` is running.
- Use `renice` to lower its scheduling priority to nice value `+12`.

### Task 3: Resource Inventory
Generate `/var/tmp/process_report.txt` containing:
- The top 5 memory-consuming processes formatted with headers: `PID,USER,%MEM,COMMAND`.""",
        "lfcs_setup": """sudo killall -9 rogue-sim batch-calc 2>/dev/null || true
# Start rogue process
nohup bash -c 'exec -a rogue-sim sleep 3600' >/dev/null 2>&1 &
# Start batch calc
nohup bash -c 'exec -a batch-calc sleep 3600' >/dev/null 2>&1 &
sudo rm -f /var/tmp/process_report.txt""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: rogue-sim killed
if ! pgrep -f "rogue-sim" >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 1: Rogue process rogue-sim has been terminated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: rogue-sim process is still running.${NC}"
fi

# Task 2: batch-calc reniced to 12
NI=$(ps -eo ni,cmd | grep "batch-calc" | grep -v grep | awk '{print $1}' | head -1 || echo "0")
if [ "$NI" == "12" ]; then
  echo -e "${GREEN}[PASS] Task 2: batch-calc has nice priority 12.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: batch-calc nice value is '$NI' (expected 12).${NC}"
fi

# Task 3: process_report.txt exists with at least 5 entries
if [ -f /var/tmp/process_report.txt ] && [ $(wc -l < /var/tmp/process_report.txt) -ge 5 ]; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/process_report.txt created with memory stats.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/process_report.txt missing or has fewer than 5 lines.${NC}"
fi""",
        "lfcs_solution": """1. Kill rogue process:
`killall -15 rogue-sim || killall -9 rogue-sim`

2. Renice batch-calc:
`renice -n 12 -p $(pgrep -f batch-calc)`

3. Top 5 memory processes:
`ps -eo pid,user,%mem,command --sort=-%mem | head -n 6 > /var/tmp/process_report.txt`""",
        "lfcs_reset": """sudo killall -9 rogue-sim batch-calc 2>/dev/null || true
sudo rm -f /var/tmp/process_report.txt"""
    },

    # Day 5
    {
        "day": 5,
        "date": "2026-10-16",
        "cka_title": "Priority Classes & Multiple Schedulers",
        "cka_diff": "Medium",
        "cka_time": "35m",
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

        "lfcs_title": "System Integrity, Resource Monitoring & Top",
        "lfcs_diff": "Medium",
        "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Hardware & Memory Profiling
Create an automated hardware summary at `/var/tmp/system_specs.txt`:
1. Total installed RAM in Megabytes (extracted from `/proc/meminfo` or `free -m`).
2. Number of CPU cores (from `/proc/cpuinfo` or `lscpu`).
3. Current system load average over 1, 5, 15 minutes (from `/proc/loadavg` or `uptime`).

### Task 2: VM Swappiness Tuning
Check the current `vm.swappiness` value and permanently tune it:
1. Append `vm.swappiness = 15` to `/etc/sysctl.d/99-swappiness.conf`.
2. Apply the change immediately with `sudo sysctl -p /etc/sysctl.d/99-swappiness.conf`.""",
        "lfcs_setup": """sudo rm -f /var/tmp/system_specs.txt /etc/sysctl.d/99-swappiness.conf
sudo sysctl -w vm.swappiness=60 >/dev/null""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: system_specs.txt
if [ -f /var/tmp/system_specs.txt ] && grep -qiE "RAM|Memory" /var/tmp/system_specs.txt && grep -qiE "CPU|Cores" /var/tmp/system_specs.txt && grep -qiE "Load" /var/tmp/system_specs.txt; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/system_specs.txt contains RAM, CPU, and Load metrics.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/system_specs.txt missing or incomplete metrics.${NC}"
fi

# Task 2: swappiness runtime and persistent
CURR_SWAP=$(sysctl -n vm.swappiness)
CONF_SWAP=$(grep -oE "vm.swappiness\\s*=\\s*15" /etc/sysctl.d/99-swappiness.conf 2>/dev/null || true)
if [ "$CURR_SWAP" == "15" ] && [ -n "$CONF_SWAP" ]; then
  echo -e "${GREEN}[PASS] Task 2: vm.swappiness=15 active and configured persistently in sysctl.d.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Runtime swappiness is $CURR_SWAP (expected 15) or config file missing.${NC}"
fi""",
        "lfcs_solution": """1. Hardware report:
```bash
MEM=$(free -m | awk '/Mem:/ {print "RAM: "$2"MB"}')
CPU=$(lscpu | awk -F: '/CPU\\(s\\):/ {print "CPU Cores: "$2}' | head -1)
LOAD=$(awk '{print "Load Average: "$1", "$2", "$3}' /proc/loadavg)
echo "$MEM" > /var/tmp/system_specs.txt
echo "$CPU" >> /var/tmp/system_specs.txt
echo "$LOAD" >> /var/tmp/system_specs.txt
```

2. Tune swappiness:
`echo "vm.swappiness = 15" | sudo tee /etc/sysctl.d/99-swappiness.conf`
`sudo sysctl -p /etc/sysctl.d/99-swappiness.conf`""",
        "lfcs_reset": """sudo rm -f /var/tmp/system_specs.txt /etc/sysctl.d/99-swappiness.conf
sudo sysctl -w vm.swappiness=60 >/dev/null"""
    },

    # Day 6
    {
        "day": 6,
        "date": "2026-10-17",
        "cka_title": "Week 3 Scheduling Troubleshooting Matrix",
        "cka_diff": "Hard (Milestone Assessment 3)",
        "cka_time": "45m",
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
TOL=$(ssh controlplane 'kubectl get pod stuck-taint -n w3-milestone -o jsonpath="{.spec.tolerations[?(@.key==\"dedicated\")].value}" 2>/dev/null || echo "None"')
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

        "lfcs_title": "Week 3 Systemd & Process Orchestration",
        "lfcs_diff": "Hard (Milestone Assessment 3)",
        "lfcs_time": "45m",
        "lfcs_tasks": """### Milestone 3 Triathlon Tasks:
1. **Automated Cleaning Service & Timer**:
   Create a systemd service `/etc/systemd/system/cache-cleaner.service` that removes files older than 7 days from `/var/tmp/cache` (`find /var/tmp/cache -type f -mtime +7 -delete`).
   Create a companion timer `/etc/systemd/system/cache-cleaner.timer` scheduled to trigger every hour (`OnCalendar=hourly`, `Persistent=true`).
   Enable and start `cache-cleaner.timer`.

2. **Fix Broken Systemd Service**:
   A service `payment-bridge.service` has a faulty unit file (`ExecStart` binary points to `/nonexistent/bridge`).
   Fix it to point to `/usr/local/bin/payment-bridge.sh`.
   Reload systemd and start the service so it is `active (running)`.

3. **Process Priority & Limit Hardening**:
   Configure `/etc/security/limits.d/50-worker.conf` to set a hard limit of `4096` open files (`nofile`) and max processes (`nproc`) of `2048` for user `student`.""",
        "lfcs_setup": """sudo mkdir -p /var/tmp/cache /usr/local/bin
sudo tee /usr/local/bin/payment-bridge.sh << 'EOF' >/dev/null
#!/usr/bin/env bash
while true; do sleep 3600; done
EOF
sudo chmod 755 /usr/local/bin/payment-bridge.sh

sudo tee /etc/systemd/system/payment-bridge.service << 'EOF' >/dev/null
[Unit]
Description=Payment Bridge Service
After=network.target

[Service]
Type=simple
ExecStart=/nonexistent/bridge
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo rm -f /etc/systemd/system/cache-cleaner.* /etc/security/limits.d/50-worker.conf
sudo systemctl daemon-reload""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: Timer active
TIMER_ACTIVE=$(systemctl is-active cache-cleaner.timer 2>/dev/null || echo "inactive")
if [ "$TIMER_ACTIVE" == "active" ]; then
  echo -e "${GREEN}[PASS] Task 1: cache-cleaner.timer is active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: cache-cleaner.timer is $TIMER_ACTIVE.${NC}"
fi

# Task 2: payment-bridge service fixed and running
SVC_ACTIVE=$(systemctl is-active payment-bridge.service 2>/dev/null || echo "inactive")
if [ "$SVC_ACTIVE" == "active" ]; then
  echo -e "${GREEN}[PASS] Task 2: payment-bridge.service is active (running).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: payment-bridge.service is $SVC_ACTIVE.${NC}"
fi

# Task 3: limits file
if [ -f /etc/security/limits.d/50-worker.conf ] && grep -q "student.*hard.*nofile.*4096" /etc/security/limits.d/50-worker.conf && grep -q "student.*hard.*nproc.*2048" /etc/security/limits.d/50-worker.conf; then
  echo -e "${GREEN}[PASS] Task 3: Security limits for student configured correctly.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /etc/security/limits.d/50-worker.conf missing or values incorrect.${NC}"
fi""",
        "lfcs_solution": """1. Cache cleaner timer:
`/etc/systemd/system/cache-cleaner.service`:
```ini
[Unit]
Description=Cache Cleaner
[Service]
Type=oneshot
ExecStart=/usr/bin/find /var/tmp/cache -type f -mtime +7 -delete
```
`/etc/systemd/system/cache-cleaner.timer`:
```ini
[Unit]
Description=Hourly Cache Cleaner Timer
[Timer]
OnCalendar=hourly
Persistent=true
[Install]
WantedBy=timers.target
```
`sudo systemctl daemon-reload && sudo systemctl enable --now cache-cleaner.timer`

2. Fix `/etc/systemd/system/payment-bridge.service`:
Change `ExecStart=/usr/local/bin/payment-bridge.sh`
`sudo systemctl daemon-reload && sudo systemctl restart payment-bridge.service`

3. Create `/etc/security/limits.d/50-worker.conf`:
```
student hard nofile 4096
student hard nproc 2048
```""",
        "lfcs_reset": """sudo systemctl stop cache-cleaner.timer payment-bridge.service 2>/dev/null || true
sudo systemctl disable cache-cleaner.timer payment-bridge.service 2>/dev/null || true
sudo rm -f /etc/systemd/system/cache-cleaner.* /etc/systemd/system/payment-bridge.service /usr/local/bin/payment-bridge.sh /etc/security/limits.d/50-worker.conf
sudo rm -rf /var/tmp/cache
sudo systemctl daemon-reload"""
    }
]
