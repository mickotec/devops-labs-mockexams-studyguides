"""
Lab definitions for Week 5
"""

WEEK_5_LABS = [
    # Day 1
    {
        "day": 1,
        "date": "2026-10-26",
        "cka_title": "Node Maintenance: Cordon, Drain & Uncordon",
        "cka_diff": "Medium",
        "cka_time": "30m",
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

        "lfcs_title": "Local User Management & /etc/passwd",
        "lfcs_diff": "Medium",
        "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Create Dedicated User
Create a user named `devops_user`:
- UID: `1600`
- Primary group: `devops_user`
- Shell: `/bin/bash`
- Home directory: `/home/devops_user`
- Comment: `DevOps Service Account`

### Task 2: Account Password Aging & Expiry
Using `chage`:
- Set account expiration date to `2027-12-31`.
- Set maximum password age to `90` days.
- Set password warning to `7` days.

### Task 3: Account Locking
Lock the user account `test_lock_user` using `passwd -l` so login is disabled.""",
        "lfcs_setup": """sudo userdel -r devops_user 2>/dev/null || true
sudo groupdel devops_user 2>/dev/null || true
sudo userdel -r test_lock_user 2>/dev/null || true
sudo useradd -m -s /bin/bash test_lock_user
echo "test_lock_user:P@ssword123" | sudo chpasswd""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: devops_user UID and shell
USER_INFO=$(getent passwd devops_user 2>/dev/null || true)
if echo "$USER_INFO" | grep -q ":1600:" && echo "$USER_INFO" | grep -q "/bin/bash"; then
  echo -e "${GREEN}[PASS] Task 1: devops_user created with UID 1600 and /bin/bash shell.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: devops_user missing or UID/shell incorrect: $USER_INFO.${NC}"
fi

# Task 2: chage settings
CHAGE_INFO=$(chage -l devops_user 2>/dev/null || true)
if echo "$CHAGE_INFO" | grep -qi "Dec 31, 2027" && echo "$CHAGE_INFO" | grep -q "90"; then
  echo -e "${GREEN}[PASS] Task 2: Password aging and expiry configured for devops_user.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: chage settings missing or incorrect.${NC}"
fi

# Task 3: test_lock_user locked
SHADOW_STAT=$(sudo passwd -S test_lock_user 2>/dev/null || true)
if echo "$SHADOW_STAT" | grep -qiE " L |locked"; then
  echo -e "${GREEN}[PASS] Task 3: test_lock_user account is locked.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: test_lock_user is not locked: $SHADOW_STAT.${NC}"
fi""",
        "lfcs_solution": """1. Create user:
`sudo useradd -u 1600 -m -s /bin/bash -c "DevOps Service Account" devops_user`

2. Set aging:
`sudo chage -E 2027-12-31 -M 90 -W 7 devops_user`

3. Lock account:
`sudo passwd -l test_lock_user`""",
        "lfcs_reset": """sudo userdel -r devops_user 2>/dev/null || true
sudo groupdel devops_user 2>/dev/null || true
sudo userdel -r test_lock_user 2>/dev/null || true"""
    },

    # Day 2
    {
        "day": 2,
        "date": "2026-10-27",
        "cka_title": "Cluster Upgrade: Kubeadm Control Plane",
        "cka_diff": "Medium",
        "cka_time": "35m",
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
        "cka_reset": """ssh controlplane 'rm -f /opt/k8s/upgrade_plan.txt'""",

        "lfcs_title": "Groups, Sudo Privileges & Visudo",
        "lfcs_diff": "Medium",
        "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Create Group & Assign Membership
1. Create a system group named `sysaudit` with GID `2800`.
2. Add user `student` to group `sysaudit` as a supplementary group.

### Task 2: Configure Passwordless Sudo for Specific Command
Create a sudoers drop-in file `/etc/sudoers.d/90-sysaudit`:
- Members of group `%sysaudit` must be permitted to execute `/usr/bin/journalctl` without password authentication (`NOPASSWD: /usr/bin/journalctl`).
- Validate syntax with `visudo -cf /etc/sudoers.d/90-sysaudit`.""",
        "lfcs_setup": """sudo rm -f /etc/sudoers.d/90-sysaudit
sudo groupdel sysaudit 2>/dev/null || true""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: sysaudit group and student member
GRP_GID=$(getent group sysaudit | cut -d: -f3 || echo "0")
if [ "$GRP_GID" == "2800" ] && id -Gn student | grep -q "sysaudit"; then
  echo -e "${GREEN}[PASS] Task 1: Group sysaudit (GID 2800) created and student is member.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Group sysaudit missing or student not member.${NC}"
fi

# Task 2: sudoers drop-in validation
if [ -f /etc/sudoers.d/90-sysaudit ] && sudo visudo -cf /etc/sudoers.d/90-sysaudit >/dev/null 2>&1; then
  if grep -q "%sysaudit.*NOPASSWD.*journalctl" /etc/sudoers.d/90-sysaudit; then
    echo -e "${GREEN}[PASS] Task 2: Sudoers rule validated for %sysaudit with NOPASSWD for journalctl.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Task 2: Rule content does not grant NOPASSWD for journalctl to %sysaudit.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Task 2: /etc/sudoers.d/90-sysaudit missing or syntax error.${NC}"
fi""",
        "lfcs_solution": """1. Group & user:
`sudo groupadd -g 2800 sysaudit`
`sudo usermod -aG sysaudit student`

2. Sudoers file:
`echo "%sysaudit ALL=(ALL) NOPASSWD: /usr/bin/journalctl" | sudo tee /etc/sudoers.d/90-sysaudit`
`sudo chmod 0440 /etc/sudoers.d/90-sysaudit`
`sudo visudo -cf /etc/sudoers.d/90-sysaudit`""",
        "lfcs_reset": """sudo rm -f /etc/sudoers.d/90-sysaudit
sudo groupdel sysaudit 2>/dev/null || true"""
    },

    # Day 3
    {
        "day": 3,
        "date": "2026-10-28",
        "cka_title": "Cluster Upgrade: Worker Nodes",
        "cka_diff": "Medium",
        "cka_time": "35m",
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
N1_STATUS=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.status.conditions[?(@.type==\"Ready\")].status}" 2>/dev/null || echo "False"')
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

        "lfcs_title": "Profiles, Template Environments & User Limits",
        "lfcs_diff": "Medium",
        "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Template Environment (/etc/skel)
Place a default welcome document in `/etc/skel/WELCOME.txt`:
- Contents: `Corporate System Policy: All activity is monitored.`
- Ensure default permissions (`644`).

### Task 2: Global Profile Environment Variable
Create `/etc/profile.d/corp_vars.sh`:
- Export `CORPORATE_ENV="production"`
- Make it readable by all users.

### Task 3: Security Limits Configuration
In `/etc/security/limits.d/80-nofile.conf`, set:
- User `student` soft limit for open files (`nofile`) to `2048`.
- User `student` hard limit for open files (`nofile`) to `4096`.""",
        "lfcs_setup": """sudo rm -f /etc/skel/WELCOME.txt /etc/profile.d/corp_vars.sh /etc/security/limits.d/80-nofile.conf""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: /etc/skel/WELCOME.txt
if [ -f /etc/skel/WELCOME.txt ] && grep -qi "All activity is monitored" /etc/skel/WELCOME.txt; then
  echo -e "${GREEN}[PASS] Task 1: /etc/skel/WELCOME.txt created and verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /etc/skel/WELCOME.txt missing or text mismatch.${NC}"
fi

# Task 2: /etc/profile.d/corp_vars.sh
if [ -f /etc/profile.d/corp_vars.sh ] && grep -q 'CORPORATE_ENV="production"' /etc/profile.d/corp_vars.sh; then
  echo -e "${GREEN}[PASS] Task 2: /etc/profile.d/corp_vars.sh exports CORPORATE_ENV.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/profile.d/corp_vars.sh missing or variable missing.${NC}"
fi

# Task 3: limits.d
if [ -f /etc/security/limits.d/80-nofile.conf ] && grep -q "student.*soft.*nofile.*2048" /etc/security/limits.d/80-nofile.conf && grep -q "student.*hard.*nofile.*4096" /etc/security/limits.d/80-nofile.conf; then
  echo -e "${GREEN}[PASS] Task 3: File limits for student configured in limits.d.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /etc/security/limits.d/80-nofile.conf missing or values incorrect.${NC}"
fi""",
        "lfcs_solution": """1. Welcome template:
`echo "Corporate System Policy: All activity is monitored." | sudo tee /etc/skel/WELCOME.txt`
`sudo chmod 644 /etc/skel/WELCOME.txt`

2. Profile variable:
`echo 'export CORPORATE_ENV="production"' | sudo tee /etc/profile.d/corp_vars.sh`
`sudo chmod 644 /etc/profile.d/corp_vars.sh`

3. Limits:
`echo -e "student soft nofile 2048\nstudent hard nofile 4096" | sudo tee /etc/security/limits.d/80-nofile.conf`""",
        "lfcs_reset": """sudo rm -f /etc/skel/WELCOME.txt /etc/profile.d/corp_vars.sh /etc/security/limits.d/80-nofile.conf"""
    },

    # Day 4
    {
        "day": 4,
        "date": "2026-10-29",
        "cka_title": "ETCD Snapshot Backup & Disaster Recovery",
        "cka_diff": "Medium",
        "cka_time": "35m",
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
        "cka_reset": """ssh controlplane 'rm -f /opt/backup/etcd-snapshot-w5.db /opt/backup/etcd_snapshot_status.txt'""",

        "lfcs_title": "Kernel Runtime Tuning with Sysctl",
        "lfcs_diff": "Medium",
        "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Network Parameter Hardening
Configure persistent network parameters in `/etc/sysctl.d/60-hardening.conf`:
- `net.ipv4.ip_forward = 1`
- `net.ipv4.icmp_echo_ignore_broadcasts = 1`

### Task 2: Apply and Verify Parameters
1. Apply the configuration immediately using `sysctl -p /etc/sysctl.d/60-hardening.conf`.
2. Save the active values of `net.ipv4.ip_forward` and `net.ipv4.icmp_echo_ignore_broadcasts` into `/var/tmp/kernel_params.txt`.""",
        "lfcs_setup": """sudo rm -f /etc/sysctl.d/60-hardening.conf /var/tmp/kernel_params.txt""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1 & 2: sysctl settings active
IP_FWD=$(sysctl -n net.ipv4.ip_forward 2>/dev/null || echo "0")
ICMP_IGN=$(sysctl -n net.ipv4.icmp_echo_ignore_broadcasts 2>/dev/null || echo "0")

if [ "$IP_FWD" == "1" ] && [ "$ICMP_IGN" == "1" ] && [ -f /etc/sysctl.d/60-hardening.conf ]; then
  echo -e "${GREEN}[PASS] Task 1: Kernel parameters active and configured in /etc/sysctl.d/60-hardening.conf.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Parameters not active (ip_forward=$IP_FWD, icmp_ignore=$ICMP_IGN).${NC}"
fi

if [ -f /var/tmp/kernel_params.txt ] && grep -q "net.ipv4.ip_forward = 1" /var/tmp/kernel_params.txt; then
  echo -e "${GREEN}[PASS] Task 2: Active parameters recorded in /var/tmp/kernel_params.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/kernel_params.txt missing or incomplete.${NC}"
fi""",
        "lfcs_solution": """1. Create sysctl configuration:
```ini
net.ipv4.ip_forward = 1
net.ipv4.icmp_echo_ignore_broadcasts = 1
```
`sudo tee /etc/sysctl.d/60-hardening.conf`
`sudo sysctl -p /etc/sysctl.d/60-hardening.conf`

2. Record:
`sysctl net.ipv4.ip_forward net.ipv4.icmp_echo_ignore_broadcasts > /var/tmp/kernel_params.txt`""",
        "lfcs_reset": """sudo rm -f /etc/sysctl.d/60-hardening.conf /var/tmp/kernel_params.txt"""
    },

    # Day 5
    {
        "day": 5,
        "date": "2026-10-30",
        "cka_title": "TLS Basics & PKI in Kubernetes",
        "cka_diff": "Medium",
        "cka_time": "35m",
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
        "cka_reset": """ssh controlplane 'rm -f /opt/k8s/certs_expiration.txt /opt/k8s/apiserver_sans.txt'""",

        "lfcs_title": "Mandatory Access Control: SELinux & AppArmor",
        "lfcs_diff": "Medium",
        "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Audit AppArmor Status
Check the status of AppArmor on Ubuntu:
1. Run `aa-status` to evaluate active profiles.
2. Save the summary of loaded and enforcing profiles to `/var/tmp/apparmor_summary.txt`.

### Task 2: Inspect Profile Directory
List all profiles located in `/etc/apparmor.d/` and output their names to `/var/tmp/apparmor_profiles.txt`.""",
        "lfcs_setup": """sudo rm -f /var/tmp/apparmor_summary.txt /var/tmp/apparmor_profiles.txt""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: apparmor_summary.txt
if [ -f /var/tmp/apparmor_summary.txt ] && grep -qiE "profiles are in enforce mode|profiles are loaded" /var/tmp/apparmor_summary.txt; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/apparmor_summary.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /var/tmp/apparmor_summary.txt missing or invalid.${NC}"
fi

# Task 2: apparmor_profiles.txt
if [ -f /var/tmp/apparmor_profiles.txt ] && [ $(wc -l < /var/tmp/apparmor_profiles.txt) -ge 5 ]; then
  echo -e "${GREEN}[PASS] Task 2: /var/tmp/apparmor_profiles.txt contains profile listings.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /var/tmp/apparmor_profiles.txt missing or has fewer than 5 entries.${NC}"
fi""",
        "lfcs_solution": """1. AppArmor status:
`sudo aa-status > /var/tmp/apparmor_summary.txt`

2. Profiles list:
`ls /etc/apparmor.d > /var/tmp/apparmor_profiles.txt`""",
        "lfcs_reset": """sudo rm -f /var/tmp/apparmor_summary.txt /var/tmp/apparmor_profiles.txt"""
    },

    # Day 6
    {
        "day": 6,
        "date": "2026-10-31",
        "cka_title": "Full Disaster Recovery & Upgrade Drill",
        "cka_diff": "Hard (Milestone Assessment 5)",
        "cka_time": "45m",
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

        "lfcs_title": "Security Audit, User Quarantine & Recovery",
        "lfcs_diff": "Hard (Milestone Assessment 5)",
        "lfcs_time": "45m",
        "lfcs_tasks": """### Milestone 5 Triathlon Tasks:
1. **Quarantine Compromised User Account**:
   A compromised user account `hacked_service` exists on the system.
   - Lock the password using `passwd -l`.
   - Change the login shell to `/usr/sbin/nologin` or `/bin/false`.
   - Expire the account immediately with `chage -E 0 hacked_service`.

2. **Sudoers Audit & Drop-In Hardening**:
   Ensure `/etc/sudoers.d/99-quarantine` allows user `student` full sudo with `NOPASSWD: ALL` and contains no insecure wildcard directives for quarantined users.

3. **Sysctl Kernel Protection**:
   Ensure `/etc/sysctl.d/99-security.conf` enforces `net.ipv4.tcp_syncookies = 1` and `net.ipv4.conf.all.rp_filter = 1`. Apply with `sysctl -p`.""",
        "lfcs_setup": """sudo userdel -r hacked_service 2>/dev/null || true
sudo useradd -m -s /bin/bash hacked_service
echo "hacked_service:P@ss123" | sudo chpasswd
sudo rm -f /etc/sysctl.d/99-security.conf""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: hacked_service quarantined
SHELL_HS=$(getent passwd hacked_service | cut -d: -f7 || echo "")
CHAGE_EXP=$(chage -l hacked_service | grep "Account expires" | awk -F: '{print $2}' | tr -d ' ' || echo "")
if [[ "$SHELL_HS" =~ (nologin|false) ]] && [ "$CHAGE_EXP" != "never" ]; then
  echo -e "${GREEN}[PASS] Task 1: hacked_service account is quarantined (shell=$SHELL_HS, expired).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: hacked_service still has shell $SHELL_HS or not expired ($CHAGE_EXP).${NC}"
fi

# Task 2: sudoers valid
if sudo visudo -c >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 2: Sudoers configuration syntax verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Sudoers configuration syntax error.${NC}"
fi

# Task 3: sysctl
SYNC=$(sysctl -n net.ipv4.tcp_syncookies 2>/dev/null || echo "0")
RPF=$(sysctl -n net.ipv4.conf.all.rp_filter 2>/dev/null || echo "0")
if [ "$SYNC" == "1" ] && [ "$RPF" == "1" ]; then
  echo -e "${GREEN}[PASS] Task 3: Kernel security parameters active (syncookies=1, rp_filter=1).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Parameters not set (syncookies=$SYNC, rp_filter=$RPF).${NC}"
fi""",
        "lfcs_solution": """1. Quarantine:
`sudo passwd -l hacked_service`
`sudo usermod -s /usr/sbin/nologin hacked_service`
`sudo chage -E 0 hacked_service`

2. Sudoers:
`sudo visudo -c`

3. Sysctl:
`echo -e "net.ipv4.tcp_syncookies = 1\nnet.ipv4.conf.all.rp_filter = 1" | sudo tee /etc/sysctl.d/99-security.conf`
`sudo sysctl -p /etc/sysctl.d/99-security.conf`""",
        "lfcs_reset": """sudo userdel -r hacked_service 2>/dev/null || true
sudo rm -f /etc/sysctl.d/99-security.conf"""
    }
]
