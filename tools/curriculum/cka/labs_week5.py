"""
Dedicated CKA Lab Definitions for Week 5 (Days 1 to 6).
"""

WEEK_5_LABS = [
    {
        "day": 1,
        "date": '2026-10-26',
        "title": 'Node Maintenance: Cordon, Drain & Uncordon',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Cordon Node
Mark worker node `node02` as unschedulable using `kubectl cordon node02`.
- Verify that `kubectl get nodes` displays `SchedulingDisabled` for `node02`.

### Task 2: Drain Node
Safely evict all running workloads from `node02` using `kubectl drain node02`:
- Ignore DaemonSets (`--ignore-daemonsets`)
- Delete emptyDir data (`--delete-emptydir-data`)
- Force eviction if needed (`--force`)
- Verify no user pods remain running on `node02`.

### Task 3: Return Node to Service
Uncordon `node02` using `kubectl uncordon node02` and verify it returns to `Ready` status without `SchedulingDisabled`.""",
        "setup": """ssh controlplane '
  kubectl uncordon node01 node02 2>/dev/null || true
  kubectl delete namespace w5d1-maint --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w5d1-maint
  kubectl create deployment test-maint -n w5d1-maint --image=nginx:alpine --replicas=3
'""",
        "verify": """SCORE=0; TOTAL=2
# Task 1 & 2: Verification of node02 status
UNSCHED=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.spec.unschedulable}" 2>/dev/null || echo "false"')
# Check user pods on node02 in w5d1-maint
PODS_ON_N2=$(ssh controlplane 'kubectl get pods -n w5d1-maint --field-selector spec.nodeName=node02 --no-headers 2>/dev/null | wc -l')

# Note: After maintenance test, candidate uncordons node02
if [ "$UNSCHED" != "true" ] && [ "$PODS_ON_N2" -eq 0 ]; then
  echo -e "${GREEN}[PASS] Tasks 1-3: node02 drained cleanly and returned to schedulable state.${NC}"
  SCORE=$((SCORE + 2))
elif [ "$UNSCHED" == "true" ]; then
  echo -e "${GREEN}[PASS] Node is currently cordoned. Now uncordon node02 to complete Task 3!${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Maintenance steps incomplete.${NC}"
fi""",
        "solution": """1. Cordon:
`kubectl cordon node02`

2. Drain:
`kubectl drain node02 --ignore-daemonsets --delete-emptydir-data --force`

3. Uncordon:
`kubectl uncordon node02`""",
        "reset": """ssh controlplane '
  kubectl uncordon node01 node02 2>/dev/null || true
  kubectl delete namespace w5d1-maint --grace-period=0 --force 2>/dev/null || true
'""",
        "cka_title": 'Node Maintenance: Cordon, Drain & Uncordon',
        "cka_diff": 'Medium',
        "cka_time": '30m',
        "cka_tasks": """### Task 1: Cordon Node
Mark worker node `node02` as unschedulable using `kubectl cordon node02`.
- Verify that `kubectl get nodes` displays `SchedulingDisabled` for `node02`.

### Task 2: Drain Node
Safely evict all running workloads from `node02` using `kubectl drain node02`:
- Ignore DaemonSets (`--ignore-daemonsets`)
- Delete emptyDir data (`--delete-emptydir-data`)
- Force eviction if needed (`--force`)
- Verify no user pods remain running on `node02`.

### Task 3: Return Node to Service
Uncordon `node02` using `kubectl uncordon node02` and verify it returns to `Ready` status without `SchedulingDisabled`.""",
        "cka_setup": """ssh controlplane '
  kubectl uncordon node01 node02 2>/dev/null || true
  kubectl delete namespace w5d1-maint --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w5d1-maint
  kubectl create deployment test-maint -n w5d1-maint --image=nginx:alpine --replicas=3
'""",
        "cka_verify": """SCORE=0; TOTAL=2
# Task 1 & 2: Verification of node02 status
UNSCHED=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.spec.unschedulable}" 2>/dev/null || echo "false"')
# Check user pods on node02 in w5d1-maint
PODS_ON_N2=$(ssh controlplane 'kubectl get pods -n w5d1-maint --field-selector spec.nodeName=node02 --no-headers 2>/dev/null | wc -l')

# Note: After maintenance test, candidate uncordons node02
if [ "$UNSCHED" != "true" ] && [ "$PODS_ON_N2" -eq 0 ]; then
  echo -e "${GREEN}[PASS] Tasks 1-3: node02 drained cleanly and returned to schedulable state.${NC}"
  SCORE=$((SCORE + 2))
elif [ "$UNSCHED" == "true" ]; then
  echo -e "${GREEN}[PASS] Node is currently cordoned. Now uncordon node02 to complete Task 3!${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Maintenance steps incomplete.${NC}"
fi""",
        "cka_solution": """1. Cordon:
`kubectl cordon node02`

2. Drain:
`kubectl drain node02 --ignore-daemonsets --delete-emptydir-data --force`

3. Uncordon:
`kubectl uncordon node02`""",
        "cka_reset": """ssh controlplane '
  kubectl uncordon node01 node02 2>/dev/null || true
  kubectl delete namespace w5d1-maint --grace-period=0 --force 2>/dev/null || true
'""",
    },
    {
        "day": 2,
        "date": '2026-10-27',
        "title": 'Cluster Upgrade: Kubeadm Control Plane',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Kubeadm Upgrade Plan Audit
On `controlplane`:
1. Run `kubeadm upgrade plan` using `sudo`.
2. Extract the current component versions table and save the output to `/opt/k8s/upgrade_plan.txt`.

### Task 2: Inspect Static Pod Manifests
Verify that all control plane static pod manifests in `/etc/kubernetes/manifests` (`kube-apiserver.yaml`, `kube-controller-manager.yaml`, `kube-scheduler.yaml`, `etcd.yaml`) are present, valid, and owned by `root:root`.""",
        "setup": """ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/upgrade_plan.txt
'""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: upgrade_plan.txt
PLAN=$(ssh controlplane 'cat /opt/k8s/upgrade_plan.txt 2>/dev/null || true')
if echo "$PLAN" | grep -qiE "Components that can be upgraded|kubeadm|CURRENT"; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/upgrade_plan.txt contains kubeadm upgrade plan.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/upgrade_plan.txt missing or empty.${NC}"
fi

# Task 2: Manifests exist
ALL_M=$(ssh controlplane 'ls /etc/kubernetes/manifests/{kube-apiserver.yaml,kube-controller-manager.yaml,kube-scheduler.yaml,etcd.yaml} 2>/dev/null | wc -l')
if [ "$ALL_M" -eq 4 ]; then
  echo -e "${GREEN}[PASS] Task 2: All 4 core control-plane static pod manifests verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: One or more static pod manifests missing in /etc/kubernetes/manifests.${NC}"
fi""",
        "solution": """1. Run plan:
`sudo kubeadm upgrade plan | sudo tee /opt/k8s/upgrade_plan.txt`

2. Verify manifests:
`ls -l /etc/kubernetes/manifests/`""",
        "reset": "ssh controlplane 'rm -f /opt/k8s/upgrade_plan.txt'",
        "cka_title": 'Cluster Upgrade: Kubeadm Control Plane',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Kubeadm Upgrade Plan Audit
On `controlplane`:
1. Run `kubeadm upgrade plan` using `sudo`.
2. Extract the current component versions table and save the output to `/opt/k8s/upgrade_plan.txt`.

### Task 2: Inspect Static Pod Manifests
Verify that all control plane static pod manifests in `/etc/kubernetes/manifests` (`kube-apiserver.yaml`, `kube-controller-manager.yaml`, `kube-scheduler.yaml`, `etcd.yaml`) are present, valid, and owned by `root:root`.""",
        "cka_setup": """ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/upgrade_plan.txt
'""",
        "cka_verify": """SCORE=0; TOTAL=2
# Task 1: upgrade_plan.txt
PLAN=$(ssh controlplane 'cat /opt/k8s/upgrade_plan.txt 2>/dev/null || true')
if echo "$PLAN" | grep -qiE "Components that can be upgraded|kubeadm|CURRENT"; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/upgrade_plan.txt contains kubeadm upgrade plan.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/upgrade_plan.txt missing or empty.${NC}"
fi

# Task 2: Manifests exist
ALL_M=$(ssh controlplane 'ls /etc/kubernetes/manifests/{kube-apiserver.yaml,kube-controller-manager.yaml,kube-scheduler.yaml,etcd.yaml} 2>/dev/null | wc -l')
if [ "$ALL_M" -eq 4 ]; then
  echo -e "${GREEN}[PASS] Task 2: All 4 core control-plane static pod manifests verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: One or more static pod manifests missing in /etc/kubernetes/manifests.${NC}"
fi""",
        "cka_solution": """1. Run plan:
`sudo kubeadm upgrade plan | sudo tee /opt/k8s/upgrade_plan.txt`

2. Verify manifests:
`ls -l /etc/kubernetes/manifests/`""",
        "cka_reset": "ssh controlplane 'rm -f /opt/k8s/upgrade_plan.txt'",
    },
    {
        "day": 3,
        "date": '2026-10-28',
        "title": 'Cluster Upgrade: Worker Nodes',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Prepare Worker Node for Upgrade
Prepare worker node `node01` for upgrade:
1. Drain `node01` safely (`kubectl drain node01 --ignore-daemonsets --delete-emptydir-data --force`) and save the output to `/opt/k8s/node01_drain.txt`.
2. Verify node01 is `SchedulingDisabled`.

### Task 2: Verify Kubelet Service Health
SSH to `node01` and verify that the `kubelet` service is active and running (`systemctl is-active kubelet`).

### Task 3: Restore Worker Node
Uncordon `node01` and verify it is `Ready` and schedulable.""",
        "setup": """ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/node01_drain.txt
  kubectl uncordon node01 node02 2>/dev/null || true
'""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: Drain verification
DRAIN_LOG=$(ssh controlplane 'cat /opt/k8s/node01_drain.txt 2>/dev/null || true')
if echo "$DRAIN_LOG" | grep -qiE "node01 already cordoned|cordoned|evicting|drained"; then
  echo -e "${GREEN}[PASS] Task 1: Drain operation verified in /opt/k8s/node01_drain.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/node01_drain.txt missing or did not contain drain output.${NC}"
fi

# Task 2 & 3: kubelet active and node01 uncordoned & Ready
KUBELET_STAT=$(ssh node01 'systemctl is-active kubelet 2>/dev/null || echo "inactive"')
N1_STATUS=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.status.conditions[?(@.type=="Ready")].status}" 2>/dev/null || echo "False"')
UNSCHED=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.spec.unschedulable}" 2>/dev/null || echo "false"')

if [ "$KUBELET_STAT" == "active" ] && [ "$N1_STATUS" == "True" ] && [ "$UNSCHED" != "true" ]; then
  echo -e "${GREEN}[PASS] Task 2 & 3: Worker node01 kubelet is active and node is Ready and schedulable.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2 & 3: kubelet=$KUBELET_STAT, Ready=$N1_STATUS, unschedulable=$UNSCHED.${NC}"
fi""",
        "solution": """1. Drain node01 and save output:
`kubectl drain node01 --ignore-daemonsets --delete-emptydir-data --force | sudo tee /opt/k8s/node01_drain.txt`

2. Check kubelet on node01:
`ssh node01 'sudo systemctl status kubelet'`

3. Uncordon:
`kubectl uncordon node01`""",
        "reset": """ssh controlplane '
  kubectl uncordon node01 node02 2>/dev/null || true
  rm -f /opt/k8s/node01_drain.txt
'""",
        "cka_title": 'Cluster Upgrade: Worker Nodes',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Prepare Worker Node for Upgrade
Prepare worker node `node01` for upgrade:
1. Drain `node01` safely (`kubectl drain node01 --ignore-daemonsets --delete-emptydir-data --force`) and save the output to `/opt/k8s/node01_drain.txt`.
2. Verify node01 is `SchedulingDisabled`.

### Task 2: Verify Kubelet Service Health
SSH to `node01` and verify that the `kubelet` service is active and running (`systemctl is-active kubelet`).

### Task 3: Restore Worker Node
Uncordon `node01` and verify it is `Ready` and schedulable.""",
        "cka_setup": """ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/node01_drain.txt
  kubectl uncordon node01 node02 2>/dev/null || true
'""",
        "cka_verify": """SCORE=0; TOTAL=2
# Task 1: Drain verification
DRAIN_LOG=$(ssh controlplane 'cat /opt/k8s/node01_drain.txt 2>/dev/null || true')
if echo "$DRAIN_LOG" | grep -qiE "node01 already cordoned|cordoned|evicting|drained"; then
  echo -e "${GREEN}[PASS] Task 1: Drain operation verified in /opt/k8s/node01_drain.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/node01_drain.txt missing or did not contain drain output.${NC}"
fi

# Task 2 & 3: kubelet active and node01 uncordoned & Ready
KUBELET_STAT=$(ssh node01 'systemctl is-active kubelet 2>/dev/null || echo "inactive"')
N1_STATUS=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.status.conditions[?(@.type=="Ready")].status}" 2>/dev/null || echo "False"')
UNSCHED=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.spec.unschedulable}" 2>/dev/null || echo "false"')

if [ "$KUBELET_STAT" == "active" ] && [ "$N1_STATUS" == "True" ] && [ "$UNSCHED" != "true" ]; then
  echo -e "${GREEN}[PASS] Task 2 & 3: Worker node01 kubelet is active and node is Ready and schedulable.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2 & 3: kubelet=$KUBELET_STAT, Ready=$N1_STATUS, unschedulable=$UNSCHED.${NC}"
fi""",
        "cka_solution": """1. Drain node01 and save output:
`kubectl drain node01 --ignore-daemonsets --delete-emptydir-data --force | sudo tee /opt/k8s/node01_drain.txt`

2. Check kubelet on node01:
`ssh node01 'sudo systemctl status kubelet'`

3. Uncordon:
`kubectl uncordon node01`""",
        "cka_reset": """ssh controlplane '
  kubectl uncordon node01 node02 2>/dev/null || true
  rm -f /opt/k8s/node01_drain.txt
'""",
    },
    {
        "day": 4,
        "date": '2026-10-29',
        "title": 'ETCD Snapshot Backup & Disaster Recovery',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Create Validated ETCD Snapshot
On `controlplane`, save an etcd snapshot to `/opt/backup/etcd-snapshot-w5.db`:
- Endpoints: `https://127.0.0.1:2379`
- CACert: `/etc/kubernetes/pki/etcd/ca.crt`
- Cert: `/etc/kubernetes/pki/etcd/server.crt`
- Key: `/etc/kubernetes/pki/etcd/server.key`

### Task 2: Verify Snapshot Integrity
Verify the saved snapshot status using `etcdctl snapshot status`:
- Write the status table output to `/opt/backup/etcd_snapshot_status.txt`.""",
        "setup": """ssh controlplane '
  mkdir -p /opt/backup
  rm -f /opt/backup/etcd-snapshot-w5.db /opt/backup/etcd_snapshot_status.txt
'""",
        "verify": """SCORE=0; TOTAL=2
# Task 1 & 2: etcd snapshot exists and is valid
IS_VALID=$(ssh controlplane 'sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-snapshot-w5.db --write-out=table 2>/dev/null | grep -iE "REVISION|TOTAL KEYS" || true')
STATUS_FILE=$(ssh controlplane 'cat /opt/backup/etcd_snapshot_status.txt 2>/dev/null | grep -iE "REVISION|TOTAL KEYS" || true')

if [ -n "$IS_VALID" ]; then
  echo -e "${GREEN}[PASS] Task 1: /opt/backup/etcd-snapshot-w5.db is a valid etcd snapshot.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Snapshot file missing or invalid.${NC}"
fi

if [ -n "$STATUS_FILE" ]; then
  echo -e "${GREEN}[PASS] Task 2: Snapshot status table saved to /opt/backup/etcd_snapshot_status.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/backup/etcd_snapshot_status.txt missing or empty.${NC}"
fi""",
        "solution": """1. Take snapshot on controlplane:
`sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /opt/backup/etcd-snapshot-w5.db`

2. Status table:
`sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-snapshot-w5.db --write-out=table | sudo tee /opt/backup/etcd_snapshot_status.txt`""",
        "reset": "ssh controlplane 'rm -f /opt/backup/etcd-snapshot-w5.db /opt/backup/etcd_snapshot_status.txt'",
        "cka_title": 'ETCD Snapshot Backup & Disaster Recovery',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Create Validated ETCD Snapshot
On `controlplane`, save an etcd snapshot to `/opt/backup/etcd-snapshot-w5.db`:
- Endpoints: `https://127.0.0.1:2379`
- CACert: `/etc/kubernetes/pki/etcd/ca.crt`
- Cert: `/etc/kubernetes/pki/etcd/server.crt`
- Key: `/etc/kubernetes/pki/etcd/server.key`

### Task 2: Verify Snapshot Integrity
Verify the saved snapshot status using `etcdctl snapshot status`:
- Write the status table output to `/opt/backup/etcd_snapshot_status.txt`.""",
        "cka_setup": """ssh controlplane '
  mkdir -p /opt/backup
  rm -f /opt/backup/etcd-snapshot-w5.db /opt/backup/etcd_snapshot_status.txt
'""",
        "cka_verify": """SCORE=0; TOTAL=2
# Task 1 & 2: etcd snapshot exists and is valid
IS_VALID=$(ssh controlplane 'sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-snapshot-w5.db --write-out=table 2>/dev/null | grep -iE "REVISION|TOTAL KEYS" || true')
STATUS_FILE=$(ssh controlplane 'cat /opt/backup/etcd_snapshot_status.txt 2>/dev/null | grep -iE "REVISION|TOTAL KEYS" || true')

if [ -n "$IS_VALID" ]; then
  echo -e "${GREEN}[PASS] Task 1: /opt/backup/etcd-snapshot-w5.db is a valid etcd snapshot.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Snapshot file missing or invalid.${NC}"
fi

if [ -n "$STATUS_FILE" ]; then
  echo -e "${GREEN}[PASS] Task 2: Snapshot status table saved to /opt/backup/etcd_snapshot_status.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/backup/etcd_snapshot_status.txt missing or empty.${NC}"
fi""",
        "cka_solution": """1. Take snapshot on controlplane:
`sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /opt/backup/etcd-snapshot-w5.db`

2. Status table:
`sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-snapshot-w5.db --write-out=table | sudo tee /opt/backup/etcd_snapshot_status.txt`""",
        "cka_reset": "ssh controlplane 'rm -f /opt/backup/etcd-snapshot-w5.db /opt/backup/etcd_snapshot_status.txt'",
    },
    {
        "day": 5,
        "date": '2026-10-30',
        "title": 'TLS Basics & PKI in Kubernetes',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Check Certificate Expiration
On `controlplane`:
1. Check expiration dates of all control plane certificates using `kubeadm certs check-expiration`.
2. Save the output table to `/opt/k8s/certs_expiration.txt`.

### Task 2: Extract API Server SANs
Inspect `/etc/kubernetes/pki/apiserver.crt` using `openssl x509`:
- Extract all Subject Alternative Names (DNS names and IP addresses).
- Save the names to `/opt/k8s/apiserver_sans.txt`.""",
        "setup": """ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/certs_expiration.txt /opt/k8s/apiserver_sans.txt
'""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: certs_expiration.txt
EXPIRE=$(ssh controlplane 'cat /opt/k8s/certs_expiration.txt 2>/dev/null || true')
if echo "$EXPIRE" | grep -qiE "CERTIFICATE|EXPIRES|RESIDUAL TIME"; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/certs_expiration.txt contains certificate expiration report.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/certs_expiration.txt missing or empty.${NC}"
fi

# Task 2: apiserver_sans.txt
SANS=$(ssh controlplane 'cat /opt/k8s/apiserver_sans.txt 2>/dev/null || true')
if echo "$SANS" | grep -qi "kubernetes"; then
  echo -e "${GREEN}[PASS] Task 2: /opt/k8s/apiserver_sans.txt contains API Server SANs.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/apiserver_sans.txt missing or lacks SANs.${NC}"
fi""",
        "solution": """1. Check expiration:
`sudo kubeadm certs check-expiration | sudo tee /opt/k8s/certs_expiration.txt`

2. Extract SANs:
`sudo openssl x509 -in /etc/kubernetes/pki/apiserver.crt -noout -text | grep -A 1 "Subject Alternative Name" | sudo tee /opt/k8s/apiserver_sans.txt`""",
        "reset": "ssh controlplane 'rm -f /opt/k8s/certs_expiration.txt /opt/k8s/apiserver_sans.txt'",
        "cka_title": 'TLS Basics & PKI in Kubernetes',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Check Certificate Expiration
On `controlplane`:
1. Check expiration dates of all control plane certificates using `kubeadm certs check-expiration`.
2. Save the output table to `/opt/k8s/certs_expiration.txt`.

### Task 2: Extract API Server SANs
Inspect `/etc/kubernetes/pki/apiserver.crt` using `openssl x509`:
- Extract all Subject Alternative Names (DNS names and IP addresses).
- Save the names to `/opt/k8s/apiserver_sans.txt`.""",
        "cka_setup": """ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/certs_expiration.txt /opt/k8s/apiserver_sans.txt
'""",
        "cka_verify": """SCORE=0; TOTAL=2
# Task 1: certs_expiration.txt
EXPIRE=$(ssh controlplane 'cat /opt/k8s/certs_expiration.txt 2>/dev/null || true')
if echo "$EXPIRE" | grep -qiE "CERTIFICATE|EXPIRES|RESIDUAL TIME"; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/certs_expiration.txt contains certificate expiration report.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/certs_expiration.txt missing or empty.${NC}"
fi

# Task 2: apiserver_sans.txt
SANS=$(ssh controlplane 'cat /opt/k8s/apiserver_sans.txt 2>/dev/null || true')
if echo "$SANS" | grep -qi "kubernetes"; then
  echo -e "${GREEN}[PASS] Task 2: /opt/k8s/apiserver_sans.txt contains API Server SANs.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/apiserver_sans.txt missing or lacks SANs.${NC}"
fi""",
        "cka_solution": """1. Check expiration:
`sudo kubeadm certs check-expiration | sudo tee /opt/k8s/certs_expiration.txt`

2. Extract SANs:
`sudo openssl x509 -in /etc/kubernetes/pki/apiserver.crt -noout -text | grep -A 1 "Subject Alternative Name" | sudo tee /opt/k8s/apiserver_sans.txt`""",
        "cka_reset": "ssh controlplane 'rm -f /opt/k8s/certs_expiration.txt /opt/k8s/apiserver_sans.txt'",
    },
    {
        "day": 6,
        "date": '2026-10-31',
        "title": 'Full Disaster Recovery & Upgrade Drill',
        "diff": 'Hard (Milestone Assessment 5)',
        "time": '45m',
        "tasks": """### Milestone 5 Triathlon Tasks:
1. **ETCD Cluster Snapshot**:
   Take an etcd snapshot and store it in `/opt/backup/milestone5-etcd.db`.
   Verify the snapshot status with `etcdctl snapshot status`.

2. **Drain and Upgrade Preparation for `node02`**:
   Drain `node02` ignoring daemonsets and deleting emptydir data.
   Confirm that `node02` has `SchedulingDisabled`.

3. **Certificate Auditing**:
   Export all expired or impending certificate warnings to `/opt/k8s/m5_certs_audit.txt` using `kubeadm certs check-expiration`.""",
        "setup": """ssh controlplane '
  mkdir -p /opt/backup /opt/k8s
  rm -f /opt/backup/milestone5-etcd.db /opt/k8s/m5_certs_audit.txt
  kubectl uncordon node02 2>/dev/null || true
'""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: etcd snapshot
SNAP_OK=$(ssh controlplane 'sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/milestone5-etcd.db --write-out=table 2>/dev/null | grep -iE "REVISION|TOTAL KEYS" || true')
if [ -n "$SNAP_OK" ]; then
  echo -e "${GREEN}[PASS] Task 1: /opt/backup/milestone5-etcd.db verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/backup/milestone5-etcd.db missing or invalid.${NC}"
fi

# Task 2: node02 drained
UNSCHED=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.spec.unschedulable}" 2>/dev/null || echo "false"')
if [ "$UNSCHED" == "true" ]; then
  echo -e "${GREEN}[PASS] Task 2: node02 is cordoned/drained for maintenance.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: node02 is not cordoned (unschedulable=$UNSCHED).${NC}"
fi

# Task 3: certs audit
if ssh controlplane 'test -s /opt/k8s/m5_certs_audit.txt'; then
  echo -e "${GREEN}[PASS] Task 3: /opt/k8s/m5_certs_audit.txt generated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /opt/k8s/m5_certs_audit.txt missing or empty.${NC}"
fi""",
        "solution": """1. Snapshot:
`sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /opt/backup/milestone5-etcd.db`

2. Drain:
`kubectl drain node02 --ignore-daemonsets --delete-emptydir-data --force`

3. Certs:
`sudo kubeadm certs check-expiration | sudo tee /opt/k8s/m5_certs_audit.txt`""",
        "reset": """ssh controlplane '
  rm -f /opt/backup/milestone5-etcd.db /opt/k8s/m5_certs_audit.txt
  kubectl uncordon node02 2>/dev/null || true
'""",
        "cka_title": 'Full Disaster Recovery & Upgrade Drill',
        "cka_diff": 'Hard (Milestone Assessment 5)',
        "cka_time": '45m',
        "cka_tasks": """### Milestone 5 Triathlon Tasks:
1. **ETCD Cluster Snapshot**:
   Take an etcd snapshot and store it in `/opt/backup/milestone5-etcd.db`.
   Verify the snapshot status with `etcdctl snapshot status`.

2. **Drain and Upgrade Preparation for `node02`**:
   Drain `node02` ignoring daemonsets and deleting emptydir data.
   Confirm that `node02` has `SchedulingDisabled`.

3. **Certificate Auditing**:
   Export all expired or impending certificate warnings to `/opt/k8s/m5_certs_audit.txt` using `kubeadm certs check-expiration`.""",
        "cka_setup": """ssh controlplane '
  mkdir -p /opt/backup /opt/k8s
  rm -f /opt/backup/milestone5-etcd.db /opt/k8s/m5_certs_audit.txt
  kubectl uncordon node02 2>/dev/null || true
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: etcd snapshot
SNAP_OK=$(ssh controlplane 'sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/milestone5-etcd.db --write-out=table 2>/dev/null | grep -iE "REVISION|TOTAL KEYS" || true')
if [ -n "$SNAP_OK" ]; then
  echo -e "${GREEN}[PASS] Task 1: /opt/backup/milestone5-etcd.db verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/backup/milestone5-etcd.db missing or invalid.${NC}"
fi

# Task 2: node02 drained
UNSCHED=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.spec.unschedulable}" 2>/dev/null || echo "false"')
if [ "$UNSCHED" == "true" ]; then
  echo -e "${GREEN}[PASS] Task 2: node02 is cordoned/drained for maintenance.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: node02 is not cordoned (unschedulable=$UNSCHED).${NC}"
fi

# Task 3: certs audit
if ssh controlplane 'test -s /opt/k8s/m5_certs_audit.txt'; then
  echo -e "${GREEN}[PASS] Task 3: /opt/k8s/m5_certs_audit.txt generated.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /opt/k8s/m5_certs_audit.txt missing or empty.${NC}"
fi""",
        "cka_solution": """1. Snapshot:
`sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /opt/backup/milestone5-etcd.db`

2. Drain:
`kubectl drain node02 --ignore-daemonsets --delete-emptydir-data --force`

3. Certs:
`sudo kubeadm certs check-expiration | sudo tee /opt/k8s/m5_certs_audit.txt`""",
        "cka_reset": """ssh controlplane '
  rm -f /opt/backup/milestone5-etcd.db /opt/k8s/m5_certs_audit.txt
  kubectl uncordon node02 2>/dev/null || true
'""",
    },
]
