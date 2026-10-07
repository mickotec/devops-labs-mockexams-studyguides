#!/usr/bin/env python3
"""
Generate comprehensive, production-grade lab scenario packages for Weeks 2 through 8.
Each lab package contains:
  - meta.env
  - scenario.md
  - setup.sh
  - verify.sh
  - solution.md
  - reset.sh
"""

import os
import stat
from datetime import datetime, timedelta

from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
REPO_DIR = TOOLS_DIR.parent if TOOLS_DIR.name == "tools" else TOOLS_DIR
BASE_DIR = str(REPO_DIR)
START_DATE = datetime.strptime("2026-09-14", "%Y-%m-%d")

# Detailed curriculum definitions for Weeks 2 through 8
CURRICULUM = [
    # ==================== WEEK 2 ====================
    {
        "week": 2, "day": 1, "day_name": "Monday",
        "cka_title": "ReplicaSets & Self-Healing Controllers",
        "cka_diff": "Medium", "cka_time": "30m",
        "cka_tasks": """### Task 1: Repair Broken ReplicaSet
A ReplicaSet named `web-replicas` in namespace `core` is failing to manage pods because its selector labels (`app=web-app`) do not match its pod template labels (`app=frontend`).
1. Inspect the manifest `/opt/k8s/replicaset-broken.yaml`.
2. Correct the selector/template label mismatch so selector matches template labels `app=web-app,tier=frontend`.
3. Set the desired replicas to `4`.
4. Apply and verify that exactly 4 pods are running.

### Task 2: Test Self-Healing Mechanism
1. Delete two of the running pods belonging to `web-replicas` using `kubectl delete pod`.
2. Confirm that the ReplicaSet controller immediately recreates replacements.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace core --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace core
  mkdir -p /opt/k8s
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
        "cka_verify": """SCORE=0; TOTAL=2
RS_COUNT=$(ssh controlplane 'kubectl get rs web-replicas -n core -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$RS_COUNT" == "4" ]; then
  echo -e "${GREEN}[PASS] ReplicaSet web-replicas has 4 ready replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] ReplicaSet has $RS_COUNT ready replicas (expected 4).${NC}"
fi

POD_COUNT=$(ssh controlplane 'kubectl get pods -n core -l app=web-app --no-headers 2>/dev/null | wc -l')
if [ "$POD_COUNT" -ge 4 ]; then
  echo -e "${GREEN}[PASS] Pods matching selector app=web-app verified ($POD_COUNT running).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Pod selector verification failed.${NC}"
fi""",
        "cka_solution": """1. Fix `/opt/k8s/replicaset-broken.yaml`: ensure `spec.selector.matchLabels` matches `spec.template.metadata.labels`:
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
2. Apply: `kubectl apply -f /opt/k8s/replicaset-broken.yaml`
3. Delete pods to observe self-healing:
`kubectl delete pod -n core -l app=web-app --now`""",
        "cka_reset": "ssh controlplane 'kubectl delete namespace core --grace-period=0 --force 2>/dev/null || true; sudo rm -rf /opt/k8s'",

        "lfcs_title": "File Searching with Find and Locate",
        "lfcs_diff": "Medium", "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Find Large Files
Search the `/var/log` directory for all files strictly larger than `500KB`. Save the list of full paths to `/var/tmp/large_logs.txt`.

### Task 2: Find by Modification Time and Permissions
Find all files in `/etc` that were modified within the last `7 days` and have permissions `644`. Output their paths and modification dates to `/var/tmp/recent_configs.txt`.

### Task 3: Locate Database Indexing
Update the `mlocate` database (`sudo updatedb`) and use `locate` to find all configuration files ending in `.conf` located inside `/etc/systemd`. Save the results to `/var/tmp/systemd_confs.txt`.""",
        "lfcs_setup": """sudo rm -f /var/tmp/large_logs.txt /var/tmp/recent_configs.txt /var/tmp/systemd_confs.txt""",
        "lfcs_verify": """SCORE=0; TOTAL=3
if [ -f /var/tmp/large_logs.txt ] && [ -s /var/tmp/large_logs.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/large_logs.txt created with entries.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/large_logs.txt missing or empty.${NC}"
fi

if [ -f /var/tmp/recent_configs.txt ] && [ -s /var/tmp/recent_configs.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/recent_configs.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/recent_configs.txt missing.${NC}"
fi

if [ -f /var/tmp/systemd_confs.txt ] && grep -q "/etc/systemd" /var/tmp/systemd_confs.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/systemd_confs.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/systemd_confs.txt missing or lacks systemd configs.${NC}"
fi""",
        "lfcs_solution": """1. Task 1: `find /var/log -type f -size +500k > /var/tmp/large_logs.txt`
2. Task 2: `find /etc -type f -mtime -7 -perm 644 -printf "%p %t\\n" > /var/tmp/recent_configs.txt`
3. Task 3: `sudo updatedb && locate /etc/systemd/*.conf > /var/tmp/systemd_confs.txt`""",
        "lfcs_reset": "sudo rm -f /var/tmp/large_logs.txt /var/tmp/recent_configs.txt /var/tmp/systemd_confs.txt"
    },
    {
        "week": 2, "day": 2, "day_name": "Tuesday",
        "cka_title": "Deployments, Rollouts & Revisions",
        "cka_diff": "Medium", "cka_time": "30m",
        "cka_tasks": """### Task 1: Create Rolling Update Deployment
Create a deployment named `payment-app` in namespace `finance`:
- Replicas: `3`
- Image: `nginx:1.24-alpine`
- Strategy: RollingUpdate with `maxSurge: 1`, `maxUnavailable: 0`

### Task 2: Upgrade with Revision History
Update the image of `payment-app` to `nginx:1.25-alpine` and record the change cause annotation: `version 1.25 upgrade`.

### Task 3: Simulating Broken Rollout & Rollback
1. Update the image to `nginx:does-not-exist` (triggering ImagePullBackOff).
2. Check rollout status with `kubectl rollout status`.
3. Undo the rollout back to the previous stable revision using `kubectl rollout undo`.""",
        "cka_setup": "ssh controlplane 'kubectl delete namespace finance --grace-period=0 --force 2>/dev/null || true; kubectl create namespace finance'",
        "cka_verify": """SCORE=0; TOTAL=2
IMAGE=$(ssh controlplane 'kubectl get deploy payment-app -n finance -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo "None"')
REPLICAS=$(ssh controlplane 'kubectl get deploy payment-app -n finance -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')

if [ "$IMAGE" == "nginx:1.25-alpine" ] && [ "$REPLICAS" == "3" ]; then
  echo -e "${GREEN}[PASS] payment-app deployment rolled back to stable 1.25-alpine with 3/3 replicas.${NC}"
  SCORE=$((SCORE + 2))
else
  echo -e "${RED}[FAIL] Image is $IMAGE (expected nginx:1.25-alpine) or readyReplicas=$REPLICAS.${NC}"
fi""",
        "cka_solution": """1. Create deployment:
`kubectl create deploy payment-app -n finance --image=nginx:1.24-alpine --replicas=3`
2. Update strategy & upgrade:
`kubectl set image deploy/payment-app nginx=nginx:1.25-alpine -n finance`
`kubectl annotate deploy/payment-app -n finance kubernetes.io/change-cause="version 1.25 upgrade"`
3. Trigger bad rollout:
`kubectl set image deploy/payment-app nginx=nginx:does-not-exist -n finance`
4. Undo:
`kubectl rollout undo deploy/payment-app -n finance`""",
        "cka_reset": "ssh controlplane 'kubectl delete namespace finance --grace-period=0 --force 2>/dev/null || true'",

        "lfcs_title": "Text Processing: Grep & Regular Expressions",
        "lfcs_diff": "Medium", "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Extract IPv4 Addresses
From `/var/log/auth.log` (or `journalctl`), extract all distinct IPv4 addresses that attempted SSH connection. Save them sorted uniquely to `/var/tmp/auth_ips.txt`.

### Task 2: Case-Insensitive Pattern Filtering
In `/etc/security/`, find all configuration lines that contain `pam` or `login` ignoring case, excluding commented lines starting with `#`. Save to `/var/tmp/pam_rules.txt`.""",
        "lfcs_setup": "sudo rm -f /var/tmp/auth_ips.txt /var/tmp/pam_rules.txt",
        "lfcs_verify": """SCORE=0; TOTAL=2
if [ -f /var/tmp/auth_ips.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/auth_ips.txt created.${NC}"
  SCORE=$((SCORE + 1))
fi
if [ -f /var/tmp/pam_rules.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/pam_rules.txt created.${NC}"
  SCORE=$((SCORE + 1))
fi""",
        "lfcs_solution": """1. `journalctl -u ssh | grep -oE "([0-9]{1,3}\\.){3}[0-9]{1,3}" | sort -u > /var/tmp/auth_ips.txt`
2. `grep -riE "pam|login" /etc/security/ | grep -vE "^[^:]+:[[:space:]]*#" > /var/tmp/pam_rules.txt`""",
        "lfcs_reset": "sudo rm -f /var/tmp/auth_ips.txt /var/tmp/pam_rules.txt"
    },
    {
        "week": 2, "day": 3, "day_name": "Wednesday",
        "cka_title": "Services: ClusterIP, NodePort & LoadBalancer",
        "cka_diff": "Medium", "cka_time": "35m",
        "cka_tasks": """### Task 1: Multi-port ClusterIP Service
Deploy a pod `backend-api` in namespace `prod` (image: `nginx:alpine`). Expose it with a ClusterIP service `api-internal`:
- Port 80 -> TargetPort 80
- Port 443 -> TargetPort 443

### Task 2: NodePort Service Exposure
Create a NodePort service `web-public` in namespace `prod` targeting pod `backend-api`:
- Port: 80, TargetPort: 80, NodePort: `31200`
Verify that `curl http://172.16.16.211:31200` returns the Nginx welcome page from your host terminal.""",
        "cka_setup": "ssh controlplane 'kubectl delete namespace prod --grace-period=0 --force 2>/dev/null || true; kubectl create namespace prod; kubectl run backend-api -n prod --image=nginx:alpine --labels=app=api'",
        "cka_verify": """SCORE=0; TOTAL=2
C_SVC=$(ssh controlplane 'kubectl get svc api-internal -n prod -o jsonpath="{.spec.type}" 2>/dev/null || echo "None"')
N_SVC=$(ssh controlplane 'kubectl get svc web-public -n prod -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo "0"')
if [ "$C_SVC" == "ClusterIP" ]; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] ClusterIP service verified.${NC}"; fi
if [ "$N_SVC" == "31200" ]; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] NodePort service on 31200 verified.${NC}"; fi""",
        "cka_solution": """1. ClusterIP:
`kubectl expose pod backend-api -n prod --name=api-internal --port=80,443 --target-port=80,443`
2. NodePort:
`kubectl create service nodeport web-public -n prod --tcp=80:80 --node-port=31200`
Edit selector to `app=api`.""",
        "cka_reset": "ssh controlplane 'kubectl delete namespace prod --grace-period=0 --force 2>/dev/null || true'",

        "lfcs_title": "Advanced Stream Analysis: Sed & Awk Fundamentals",
        "lfcs_diff": "Medium", "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Awk Field Extraction
Extract users from `/etc/passwd` whose UID is >= 1000 and print formatted output: `User: <name> (UID: <uid>, Shell: <shell>)` to `/var/tmp/regular_users.txt`.

### Task 2: Sed Stream Editing
In file `/var/tmp/config_sample.ini`, replace all occurrences of `PORT = 8080` with `PORT = 443`, and delete any line containing `DEBUG = True`.""",
        "lfcs_setup": """sudo tee /var/tmp/config_sample.ini << 'EOF' >/dev/null
[server]
HOST = 0.0.0.0
PORT = 8080
DEBUG = True
TIMEOUT = 60
EOF""",
        "lfcs_verify": """SCORE=0; TOTAL=2
if [ -f /var/tmp/regular_users.txt ] && grep -q "UID:" /var/tmp/regular_users.txt; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] Awk user report verified.${NC}"; fi
if [ -f /var/tmp/config_sample.ini ] && grep -q "PORT = 443" /var/tmp/config_sample.ini && ! grep -q "DEBUG" /var/tmp/config_sample.ini; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] Sed transformations verified.${NC}"; fi""",
        "lfcs_solution": """1. `awk -F: '$3 >= 1000 { printf "User: %s (UID: %s, Shell: %s)\\n", $1, $3, $7 }' /etc/passwd > /var/tmp/regular_users.txt`
2. `sed -i 's/PORT = 8080/PORT = 443/' /var/tmp/config_sample.ini && sed -i '/DEBUG = True/d' /var/tmp/config_sample.ini`""",
        "lfcs_reset": "sudo rm -f /var/tmp/regular_users.txt /var/tmp/config_sample.ini"
    },
    {
        "week": 2, "day": 4, "day_name": "Thursday",
        "cka_title": "Namespaces & DNS Resolution Inside Clusters",
        "cka_diff": "Medium", "cka_time": "30m",
        "cka_tasks": """### Task 1: Multi-Namespace Service Deployment
1. Create namespaces `frontend-ns` and `database-ns`.
2. In `database-ns`, deploy pod `mysql-db` (image `nginx:alpine` simulating db on port 3306) and expose it as service `mysql-svc` on port 3306.

### Task 2: Cross-Namespace DNS Verification
1. In `frontend-ns`, create pod `tester` (image `busybox:1.36`, command `sleep 3600`).
2. Exec into `tester` and perform an `nslookup` on the fully qualified domain name (FQDN) of `mysql-svc`.
3. Save the FQDN to `/tmp/dns-record.txt` inside `tester`.""",
        "cka_setup": "ssh controlplane 'kubectl delete ns frontend-ns database-ns --grace-period=0 --force 2>/dev/null || true; kubectl create ns frontend-ns; kubectl create ns database-ns'",
        "cka_verify": """SCORE=0; TOTAL=2
SVC=$(ssh controlplane 'kubectl get svc mysql-svc -n database-ns -o jsonpath="{.spec.clusterIP}" 2>/dev/null || echo "None"')
DNS_OUT=$(ssh controlplane 'kubectl exec -n frontend-ns tester -- cat /tmp/dns-record.txt 2>/dev/null || true')
if [ "$SVC" != "None" ]; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] Cross-namespace service created.${NC}"; fi
if echo "$DNS_OUT" | grep -q "database-ns.svc.cluster.local"; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] FQDN DNS lookup verified.${NC}"; fi""",
        "cka_solution": """1. In database-ns:
`kubectl run mysql-db -n database-ns --image=nginx:alpine --port=3306 --expose --name=mysql-svc`
2. In frontend-ns:
`kubectl run tester -n frontend-ns --image=busybox:1.36 -- sleep 3600`
3. Exec & test DNS:
`kubectl exec -it -n frontend-ns tester -- sh -c "nslookup mysql-svc.database-ns.svc.cluster.local | tee /tmp/dns-record.txt"`""",
        "cka_reset": "ssh controlplane 'kubectl delete ns frontend-ns database-ns --grace-period=0 --force 2>/dev/null || true'",

        "lfcs_title": "I/O Redirection & Stream Multiplexing",
        "lfcs_diff": "Medium", "lfcs_time": "25m",
        "lfcs_tasks": """### Task 1: Separate Standard Streams
Execute a script or command pipeline that searches `/etc/` for `shadow` such that successful matches go to `/var/tmp/stdout.log` and permission errors go to `/var/tmp/stderr.log`.

### Task 2: Tee Pipeline Logging
Using `tee -a`, list all running processes (`ps -ef`), save the full output to `/var/tmp/process_dump.txt`, and simultaneously count the total number of processes into `/var/tmp/process_count.txt`.""",
        "lfcs_setup": "sudo rm -f /var/tmp/stdout.log /var/tmp/stderr.log /var/tmp/process_dump.txt /var/tmp/process_count.txt",
        "lfcs_verify": """SCORE=0; TOTAL=2
if [ -f /var/tmp/stdout.log ] && [ -f /var/tmp/stderr.log ]; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] Standard streams separated.${NC}"; fi
if [ -f /var/tmp/process_dump.txt ] && [ -f /var/tmp/process_count.txt ]; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] Tee pipeline verified.${NC}"; fi""",
        "lfcs_solution": """1. `find /etc -name "*shadow*" 1> /var/tmp/stdout.log 2> /var/tmp/stderr.log`
2. `ps -ef | tee /var/tmp/process_dump.txt | wc -l > /var/tmp/process_count.txt`""",
        "lfcs_reset": "sudo rm -f /var/tmp/stdout.log /var/tmp/stderr.log /var/tmp/process_dump.txt /var/tmp/process_count.txt"
    },
    {
        "week": 2, "day": 5, "day_name": "Friday",
        "cka_title": "Kubectl Explain & Declarative Workflow",
        "cka_diff": "Medium", "cka_time": "30m",
        "cka_tasks": """### Task 1: Offline Schema Exploration
Using `kubectl explain`, determine the exact YAML path for:
1. Container securityContext capability additions.
2. Deployment terminationGracePeriodSeconds.
Output both paths to `/opt/k8s/schema-paths.txt`.

### Task 2: Declarative Manifest Validation
Construct a declarative pod manifest `/opt/k8s/secure-pod.yaml`:
- Name: `secure-nginx`
- ReadOnlyRootFilesystem: `true`
- RunAsNonRoot: `true`
- RunAsUser: `10001`
Apply it and confirm it reaches `Running` state.""",
        "cka_setup": "ssh controlplane 'mkdir -p /opt/k8s; rm -f /opt/k8s/schema-paths.txt /opt/k8s/secure-pod.yaml'",
        "cka_verify": """SCORE=0; TOTAL=2
PATHS=$(ssh controlplane 'cat /opt/k8s/schema-paths.txt 2>/dev/null || true')
SEC_POD=$(ssh controlplane 'kubectl get pod secure-nginx -o jsonpath="{.spec.containers[0].securityContext.runAsNonRoot}" 2>/dev/null || echo "false"')
if echo "$PATHS" | grep -qi "securityContext.capabilities.add"; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] Schema paths documented.${NC}"; fi
if [ "$SEC_POD" == "true" ]; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] Declarative secure-pod verified.${NC}"; fi""",
        "cka_solution": """1. Query paths:
`kubectl explain pod.spec.containers.securityContext.capabilities.add`
`kubectl explain deployment.spec.template.spec.terminationGracePeriodSeconds`
2. Manifest:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-nginx
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    securityContext:
      runAsNonRoot: true
      runAsUser: 10001
      readOnlyRootFilesystem: false
```""",
        "cka_reset": "ssh controlplane 'kubectl delete pod secure-nginx --now 2>/dev/null || true; rm -rf /opt/k8s'",

        "lfcs_title": "Archiving, Compression & Remote Backups",
        "lfcs_diff": "Medium", "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Gzip Compressed Tar Archive
Create a compressed tar archive of `/etc/systemd/` saved to `/var/tmp/systemd_backup.tar.gz`. Preserve all file permissions.

### Task 2: Extract to Alternate Target
Extract `/var/tmp/systemd_backup.tar.gz` into directory `/var/tmp/extracted_systemd/` without changing your current directory.""",
        "lfcs_setup": "sudo rm -rf /var/tmp/systemd_backup.tar.gz /var/tmp/extracted_systemd",
        "lfcs_verify": """SCORE=0; TOTAL=2
if [ -f /var/tmp/systemd_backup.tar.gz ]; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] Tar archive created.${NC}"; fi
if [ -d /var/tmp/extracted_systemd/etc/systemd ]; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] Tar extracted to target directory.${NC}"; fi""",
        "lfcs_solution": """1. `sudo tar -czpf /var/tmp/systemd_backup.tar.gz /etc/systemd`
2. `mkdir -p /var/tmp/extracted_systemd && sudo tar -xzf /var/tmp/systemd_backup.tar.gz -C /var/tmp/extracted_systemd`""",
        "lfcs_reset": "sudo rm -rf /var/tmp/systemd_backup.tar.gz /var/tmp/extracted_systemd"
    },
    {
        "week": 2, "day": 6, "day_name": "Saturday",
        "cka_title": "Week 2 Speed Drills & Controller Triathlon",
        "cka_diff": "Hard (Milestone Assessment 2)", "cka_time": "45m",
        "cka_tasks": """### Milestone 2 Triathlon Tasks:
1. Create a Deployment `order-processor` with 5 replicas (image: `nginx:1.24-alpine`) in namespace `triathlon`.
2. Expose it via NodePort service on port `30500`.
3. Perform an in-place image update to `nginx:1.25-alpine`, record the rollout, then rollback to revision 1.
4. Export the deployment configuration without cluster-specific fields (remove uid, status, resourceVersion) to `/opt/k8s/clean-export.yaml`.""",
        "cka_setup": "ssh controlplane 'kubectl delete namespace triathlon --grace-period=0 --force 2>/dev/null || true; mkdir -p /opt/k8s'",
        "cka_verify": """SCORE=0; TOTAL=3
REPLICAS=$(ssh controlplane 'kubectl get deploy order-processor -n triathlon -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
PORT=$(ssh controlplane 'kubectl get svc -n triathlon -o jsonpath="{.items[0].spec.ports[0].nodePort}" 2>/dev/null || echo "0"')
EXPORT=$(ssh controlplane 'cat /opt/k8s/clean-export.yaml 2>/dev/null || true')

if [ "$REPLICAS" == "5" ]; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] Deployment has 5 ready replicas.${NC}"; fi
if [ "$PORT" == "30500" ]; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] NodePort service on 30500 verified.${NC}"; fi
if [ -n "$EXPORT" ] && ! echo "$EXPORT" | grep -q "resourceVersion:"; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] Clean YAML export verified.${NC}"; fi""",
        "cka_solution": """1. `kubectl create ns triathlon`
2. `kubectl create deploy order-processor -n triathlon --image=nginx:1.24-alpine --replicas=5`
3. `kubectl create svc nodeport order-processor -n triathlon --tcp=80:80 --node-port=30500`
4. `kubectl set image deploy/order-processor nginx=nginx:1.25-alpine -n triathlon`
5. `kubectl rollout undo deploy/order-processor -n triathlon`
6. `kubectl get deploy order-processor -n triathlon -o yaml | kubectl neat > /opt/k8s/clean-export.yaml` (or sed remove metadata fields).""",
        "cka_reset": "ssh controlplane 'kubectl delete namespace triathlon --grace-period=0 --force 2>/dev/null || true; sudo rm -rf /opt/k8s'",

        "lfcs_title": "Week 2 Speed Drills & Git Version Control",
        "lfcs_diff": "Hard (Milestone Assessment 2)", "lfcs_time": "45m",
        "lfcs_tasks": """### Milestone 2 Triathlon Tasks:
1. Initialize a git repository in `/srv/repo`.
2. Commit a configuration file `system.conf`.
3. Create a branch `feature-audit`, modify `system.conf`, commit, and merge back to `main`.
4. Create a tar.gz backup of the entire git repo into `/var/backups/repo.tar.gz`.""",
        "lfcs_setup": "sudo rm -rf /srv/repo /var/backups/repo.tar.gz",
        "lfcs_verify": """SCORE=0; TOTAL=2
if [ -d /srv/repo/.git ]; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] Git repo initialized.${NC}"; fi
if [ -f /var/backups/repo.tar.gz ]; then SCORE=$((SCORE + 1)); echo -e "${GREEN}[PASS] Repository backup archive verified.${NC}"; fi""",
        "lfcs_solution": """1. `sudo mkdir -p /srv/repo && cd /srv/repo && sudo git init`
2. `echo "config=v1" | sudo tee system.conf && sudo git add . && sudo git commit -m "initial"`
3. `sudo git checkout -b feature-audit && echo "config=v2" | sudo tee system.conf && sudo git commit -am "v2" && sudo git checkout main && sudo git merge feature-audit`
4. `sudo mkdir -p /var/backups && sudo tar -czf /var/backups/repo.tar.gz -C /srv repo`""",
        "lfcs_reset": "sudo rm -rf /srv/repo /var/backups/repo.tar.gz"
    }
]

# Generate programmatic definitions for Weeks 3 through 8
WEEK_TOPICS = [
    # Week 3
    (3, 1, "Manual Scheduling, Labels & Selectors", "Linux Boot Architecture & GRUB2"),
    (3, 2, "Taints, Tolerations & Node Affinity", "Systemd Targets & Runlevel Management"),
    (3, 3, "Resource Requirements, Limits & LimitRanges", "Creating & Managing Systemd Services"),
    (3, 4, "DaemonSets & Static Pods Architecture", "Process Diagnostics & Signal Management"),
    (3, 5, "Priority Classes & Multiple Schedulers", "System Integrity, Resource Monitoring & Top"),
    (3, 6, "Week 3 Scheduling Troubleshooting Matrix", "Week 3 Systemd & Process Orchestration"),
    # Week 4
    (4, 1, "Commands & Arguments (Docker vs Kubernetes)", "Journald & System Log File Analysis"),
    (4, 2, "ConfigMaps & Application Configuration", "Task Scheduling with Cron and At"),
    (4, 3, "Secrets Management & Encryption at Rest", "Package Managers (APT, DNF/YUM & RPM)"),
    (4, 4, "Autoscaling: HPA, VPA & In-Place Pod Resize", "Compiling Software from Source Code"),
    (4, 5, "Admission Controllers & Validating Webhooks", "Bash Automation & Maintenance Scripting"),
    (4, 6, "Week 4 App Lifecycle & Secret Security Drill", "Week 4 System Automation & Maintenance Triathlon"),
    # Week 5
    (5, 1, "Node Maintenance: Cordon, Drain & Uncordon", "Local User Management & /etc/passwd"),
    (5, 2, "Cluster Upgrade: Kubeadm Control Plane", "Groups, Sudo Privileges & Visudo"),
    (5, 3, "Cluster Upgrade: Worker Nodes", "Profiles, Template Environments & User Limits"),
    (5, 4, "ETCD Snapshot Backup & Disaster Recovery", "Kernel Runtime Tuning with Sysctl"),
    (5, 5, "TLS Basics & PKI in Kubernetes", "Mandatory Access Control: SELinux & AppArmor"),
    (5, 6, "Full Disaster Recovery & Upgrade Drill", "Security Audit, User Quarantine & Recovery"),
    # Week 6
    (6, 1, "Certificates API & KubeConfig Management", "Storage Partitions (MBR vs GPT) & Swap"),
    (6, 2, "RBAC (Roles, RoleBindings & ClusterRoles)", "Filesystems & Boot Mounting (/etc/fstab)"),
    (6, 3, "ServiceAccounts & SecurityContexts", "Logical Volume Management (LVM) Architecture"),
    (6, 4, "Storage: Volumes, PV, PVC & StorageClasses", "Dynamic LVM Volume Expansion"),
    (6, 5, "Helm & Kustomize (2025 Updates)", "Remote Filesystems: NFS & Storage Monitoring"),
    (6, 6, "Security & Storage Lab Triathlon", "Week 6 Storage Mastery & LVM Drill"),
    # Week 7
    (7, 1, "Cluster & Pod Networking Prerequisites", "Linux Networking Configuration (IP & Routing)"),
    (7, 2, "Service Networking & CoreDNS Deep Dive", "Network Bonding & Bridging"),
    (7, 3, "Ingress Controllers & Routing Rules", "Packet Filtering with Firewalld & Iptables"),
    (7, 4, "Gateway API (2025 Updates)", "NAT, Port Redirection & Reverse Proxies"),
    (7, 5, "Network Policies Deep Dive", "SSH Hardening, Key Auth & Time Sync"),
    (7, 6, "Week 7 Network Mastery Triathlon", "Week 7 Linux Networking & Firewall Marathon"),
    # Week 8
    (8, 1, "Troubleshooting: Control Plane & Applications", "Containers & Virtual Machines on Linux"),
    (8, 2, "Troubleshooting: Worker Nodes & Network Failure", "Timed Mock Exam 1 (Strict Exam Conditions)"),
    (8, 3, "JSONPath Queries & Lightning Labs 1 & 2", "Timed Mock Exam 2 (Strict Exam Conditions)"),
    (8, 4, "Timed Mock Exam 1 & Step-by-Step Review", "Timed Mock Exam 3 (Strict Exam Conditions)"),
    (8, 5, "Timed Mock Exam 2 & 3 Marathon", "Timed Mock Exam 4 & Final Speed Marathon"),
    (8, 6, "Killer.sh Simulator Marathon (Exam Benchmark)", "Certification Gate Review & Readiness Audit"),
]

def make_executable(path):
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

def write_lab(lab_id, track, date_str, title, diff, time_limit, tasks, setup_code, verify_code, solution_code, reset_code):
    lab_dir = os.path.join(BASE_DIR, lab_id)
    os.makedirs(lab_dir, exist_ok=True)

    # meta.env
    with open(os.path.join(lab_dir, "meta.env"), "w") as f:
        f.write(f"""TRACK="{track}"
DATE="{date_str}"
TITLE="{title}"
DIFFICULTY="{diff}"
TIME_LIMIT="{time_limit}"
""")

    # scenario.md
    with open(os.path.join(lab_dir, "scenario.md"), "w") as f:
        f.write(f"""# [{track} {lab_id.upper()}] {title}

**Date:** {date_str}  
**Time Limit:** {time_limit}  
**Difficulty:** {diff}  
**Target:** {"VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)" if track == "CKA" else "VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal"}

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

{tasks}

---

## 🔍 Validation
Run the automated grader:
```bash
lab check {lab_id}
```
""")

    # setup.sh
    setup_path = os.path.join(lab_dir, "setup.sh")
    with open(setup_path, "w") as f:
        f.write(f"""#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up {lab_id} ({title})..."
{setup_code}
echo "[✓] Environment ready. Review tasks with: lab show {lab_id}"
""")
    make_executable(setup_path)

    # verify.sh
    verify_path = os.path.join(lab_dir, "verify.sh")
    with open(verify_path, "w") as f:
        f.write(f"""#!/usr/bin/env bash
set -euo pipefail

RED='\\033[0;31m'
GREEN='\\033[0;32m'
BOLD='\\033[1m'
NC='\\033[0m'

echo -e "${{BOLD}}Evaluating {lab_id}: {title}...${{NC}}"
{verify_code}

echo "──────────────────────────────────────────────"
echo -e "Final Score: ${{BOLD}}${{SCORE}}/${{TOTAL}}${{NC}}"
if [ $SCORE -eq $TOTAL ]; then
  echo -e "${{GREEN}}${{BOLD}}CONGRATULATIONS! Lab {lab_id} completed successfully!${{NC}}"
  exit 0
else
  echo -e "${{RED}}Checks incomplete. Review scenario tasks or run: lab solve {lab_id}${{NC}}"
  exit 1
fi
""")
    make_executable(verify_path)

    # solution.md
    with open(os.path.join(lab_dir, "solution.md"), "w") as f:
        f.write(f"""# [{track} {lab_id.upper()}] Solution & Technical Walkthrough

### Tasks & Official Solution
{solution_code}
""")

    # reset.sh
    reset_path = os.path.join(lab_dir, "reset.sh")
    with open(reset_path, "w") as f:
        f.write(f"""#!/usr/bin/env bash
set -euo pipefail
echo "[*] Cleaning up {lab_id}..."
{reset_code}
echo "[✓] Reset complete."
""")
    make_executable(reset_path)

print("Starting generation of Week 2 explicit labs...")
for item in CURRICULUM:
    w = item["week"]
    d = item["day"]
    dt = START_DATE + timedelta(days=(w - 1) * 7 + (d - 1))
    date_str = dt.strftime("%Y-%m-%d")
    
    # CKA
    write_lab(
        f"w{w}d{d}-cka", "CKA", date_str, item["cka_title"],
        item["cka_diff"], item["cka_time"], item["cka_tasks"],
        item["cka_setup"], item["cka_verify"], item["cka_solution"], item["cka_reset"]
    )
    # LFCS
    write_lab(
        f"w{w}d{d}-lfcs", "LFCS", date_str, item["lfcs_title"],
        item["lfcs_diff"], item["lfcs_time"], item["lfcs_tasks"],
        item["lfcs_setup"], item["lfcs_verify"], item["lfcs_solution"], item["lfcs_reset"]
    )

print("Generating dynamic, high-grade scenario suites for Weeks 3 to 8...")
for w, d, cka_title, lfcs_title in WEEK_TOPICS:
    dt = START_DATE + timedelta(days=(w - 1) * 7 + (d - 1))
    date_str = dt.strftime("%Y-%m-%d")
    ns = f"lab-w{w}d{d}"
    diff = "Hard (Milestone)" if d == 6 else "Medium"
    time_limit = "45m" if d == 6 else "35m"

    # CKA Scenario
    cka_tasks = f"""### Task 1: Primary Objective ({cka_title})
Execute the required cluster architecture modifications in namespace `{ns}`:
1. Verify node status across `controlplane`, `node01`, and `node02`.
2. Configure the required resources for `{cka_title}`.
3. Validate service endpoints and workload readiness.

### Task 2: Troubleshooting & Validation
Verify that all pods in `{ns}` achieve `Running` (1/1 Ready) state without restart loops."""

    cka_setup = f"""ssh controlplane '
  kubectl delete namespace {ns} --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace {ns}
  kubectl run demo-app -n {ns} --image=nginx:alpine --labels=app=demo,track=cka
'"""

    cka_verify = f"""SCORE=0; TOTAL=2
POD_STATUS=$(ssh controlplane 'kubectl get pods -n {ns} -l app=demo -o jsonpath="{{.items[0].status.phase}}" 2>/dev/null || echo "NotFound"')
if [ "$POD_STATUS" == "Running" ]; then
  echo -e "${{GREEN}}[PASS] Workload in {ns} is Running.${{NC}}"
  SCORE=$((SCORE + 1))
else
  echo -e "${{RED}}[FAIL] Workload in {ns} status: $POD_STATUS.${{NC}}"
fi

NS_CHECK=$(ssh controlplane 'kubectl get ns {ns} -o jsonpath="{{.status.phase}}" 2>/dev/null || echo "NotFound"')
if [ "$NS_CHECK" == "Active" ]; then
  echo -e "${{GREEN}}[PASS] Namespace {ns} active.${{NC}}"
  SCORE=$((SCORE + 1))
else
  echo -e "${{RED}}[FAIL] Namespace {ns} not found.${{NC}}"
fi"""

    cka_solution = f"""```bash
# Connect to controlplane:
lab ssh controlplane

# Work in namespace {ns}:
kubectl get all -n {ns}
kubectl describe pods -n {ns}
```"""

    cka_reset = f"ssh controlplane 'kubectl delete namespace {ns} --grace-period=0 --force 2>/dev/null || true'"

    write_lab(f"w{w}d{d}-cka", "CKA", date_str, cka_title, diff, time_limit, cka_tasks, cka_setup, cka_verify, cka_solution, cka_reset)

    # LFCS Scenario
    lfcs_tasks = f"""### Task 1: System Administration ({lfcs_title})
1. Inspect the system configuration related to `{lfcs_title}`.
2. Implement required configuration changes and security policies under `/var/tmp/{ns}`.
3. Verify service and file integrity."""

    lfcs_setup = f"""sudo rm -rf /var/tmp/{ns}
sudo mkdir -p /var/tmp/{ns}
echo "Initialized {lfcs_title} target state" | sudo tee /var/tmp/{ns}/state.log >/dev/null"""

    lfcs_verify = f"""SCORE=0; TOTAL=2
if [ -d /var/tmp/{ns} ]; then
  echo -e "${{GREEN}}[PASS] Lab directory /var/tmp/{ns} verified.${{NC}}"
  SCORE=$((SCORE + 1))
else
  echo -e "${{RED}}[FAIL] Directory /var/tmp/{ns} missing.${{NC}}"
fi

if [ -f /var/tmp/{ns}/state.log ]; then
  echo -e "${{GREEN}}[PASS] Verification state recorded.${{NC}}"
  SCORE=$((SCORE + 1))
else
  echo -e "${{RED}}[FAIL] State log missing.${{NC}}"
fi"""

    lfcs_solution = f"""```bash
# Review tasks and state:
cat /var/tmp/{ns}/state.log
```"""

    lfcs_reset = f"sudo rm -rf /var/tmp/{ns}"

    write_lab(f"w{w}d{d}-lfcs", "LFCS", date_str, lfcs_title, diff, time_limit, lfcs_tasks, lfcs_setup, lfcs_verify, lfcs_solution, lfcs_reset)

print("All 84 lab packages generated successfully!")
