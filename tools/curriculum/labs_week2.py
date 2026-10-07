"""
Lab definitions for Week 2 (Days 1 to 6) for both CKA and LFCS tracks.
"""

WEEK_2_LABS = [
    # ==================== DAY 1 ====================
    {
        "day": 1,
        "date": "2026-10-05",
        "cka_title": "ReplicaSets & Self-Healing Controllers",
        "cka_diff": "Medium",
        "cka_time": "30m",
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

        "lfcs_title": "File Searching with Find and Locate",
        "lfcs_diff": "Medium",
        "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Find Large Files
Search the `/var/log` directory for all files strictly larger than `500KB` (`+500k`). Save the list of full paths to `/var/tmp/large_logs.txt`.

### Task 2: Find by Modification Time and Permissions
Find all files in `/etc` that were modified within the last `7 days` (`-mtime -7`) and have permissions `644`. Output their paths to `/var/tmp/recent_configs.txt`.

### Task 3: Locate Database Indexing
Update the `mlocate` / `plocate` database (`sudo updatedb`) and use `locate` to find all configuration files ending in `.conf` located inside `/etc/systemd`. Save the results to `/var/tmp/systemd_confs.txt`.""",
        "lfcs_setup": """sudo rm -f /var/tmp/large_logs.txt /var/tmp/recent_configs.txt /var/tmp/systemd_confs.txt""",
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: /var/tmp/large_logs.txt...${NC}"
if [ -f /var/tmp/large_logs.txt ] && [ -s /var/tmp/large_logs.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/large_logs.txt created with entries.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/large_logs.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 2: /var/tmp/recent_configs.txt...${NC}"
if [ -f /var/tmp/recent_configs.txt ] && [ -s /var/tmp/recent_configs.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/recent_configs.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/recent_configs.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/systemd_confs.txt...${NC}"
if [ -f /var/tmp/systemd_confs.txt ] && grep -q "/etc/systemd" /var/tmp/systemd_confs.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/systemd_confs.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/systemd_confs.txt missing or lacks systemd configs.${NC}"
fi""",
        "lfcs_solution": """1. Large files:
```bash
find /var/log -type f -size +500k > /var/tmp/large_logs.txt
```

2. Recent configs:
```bash
find /etc -type f -mtime -7 -perm 644 > /var/tmp/recent_configs.txt
```

3. Locate query:
```bash
sudo updatedb && locate '/etc/systemd/*.conf' > /var/tmp/systemd_confs.txt
```""",
        "lfcs_reset": """sudo rm -f /var/tmp/large_logs.txt /var/tmp/recent_configs.txt /var/tmp/systemd_confs.txt"""
    },

    # ==================== DAY 2 ====================
    {
        "day": 2,
        "date": "2026-10-06",
        "cka_title": "Deployments, Rollouts & Revisions",
        "cka_diff": "Medium",
        "cka_time": "30m",
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
        "cka_reset": """ssh controlplane 'kubectl delete namespace finance --grace-period=0 --force 2>/dev/null || true'""",

        "lfcs_title": "Text Processing: Grep & Regular Expressions",
        "lfcs_diff": "Medium",
        "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Extract IPv4 Addresses
From `/var/tmp/auth_sample.log`, extract all distinct IPv4 addresses that attempted connection. Save them sorted uniquely to `/var/tmp/auth_ips.txt`.

### Task 2: Case-Insensitive Pattern Filtering
In `/etc/security/`, find all configuration lines that contain `pam` or `login` ignoring case, excluding commented lines starting with `#`. Save to `/var/tmp/pam_rules.txt`.

### Task 3: Log Error Frequency Count
In `/var/tmp/auth_sample.log`, count how many lines contain `Failed password` or `authentication failure`. Output the integer count to `/var/tmp/error_count.txt`.""",
        "lfcs_setup": """sudo rm -f /var/tmp/auth_ips.txt /var/tmp/pam_rules.txt /var/tmp/error_count.txt
cat << 'EOF' > /var/tmp/auth_sample.log
Sep 14 10:00:01 server sshd[1234]: Failed password for invalid user admin from 192.168.1.50 port 45231 ssh2
Sep 14 10:00:05 server sshd[1235]: Failed password for root from 10.0.0.15 port 51234 ssh2
Sep 14 10:00:10 server sshd[1236]: Accepted publickey for student from 172.16.16.1 port 38291 ssh2
Sep 14 10:00:12 server sshd[1237]: authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.1.50
Sep 14 10:00:15 server sshd[1238]: Failed password for root from 192.168.1.50 port 45233 ssh2
EOF""",
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: /var/tmp/auth_ips.txt...${NC}"
if [ -f /var/tmp/auth_ips.txt ] && grep -q "192.168.1.50" /var/tmp/auth_ips.txt && grep -q "10.0.0.15" /var/tmp/auth_ips.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/auth_ips.txt contains extracted IP addresses.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/auth_ips.txt missing or incomplete.${NC}"
fi

echo -e "${BOLD}Checking Task 2: /var/tmp/pam_rules.txt...${NC}"
if [ -f /var/tmp/pam_rules.txt ] && [ -s /var/tmp/pam_rules.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/pam_rules.txt verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/pam_rules.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/error_count.txt...${NC}"
if [ -f /var/tmp/error_count.txt ] && [ "$(tr -d '[:space:]' < /var/tmp/error_count.txt)" == "4" ]; then
  echo -e "${GREEN}[PASS] Error count matched expected count of 4.${NC}"
  SCORE=$((SCORE + 1))
else
  ACTUAL=$(cat /var/tmp/error_count.txt 2>/dev/null || echo "none")
  echo -e "${RED}[FAIL] Error count was '$ACTUAL' (expected 4).${NC}"
fi""",
        "lfcs_solution": """1. Extract IPs:
```bash
grep -oE '([0-9]{1,3}\\.){3}[0-9]{1,3}' /var/tmp/auth_sample.log | sort -u > /var/tmp/auth_ips.txt
```

2. Filter PAM rules:
```bash
grep -riE 'pam|login' /etc/security/ | grep -vE '^[^:]+:[[:space:]]*#' > /var/tmp/pam_rules.txt
```

3. Count failure lines:
```bash
grep -E 'Failed password|authentication failure' /var/tmp/auth_sample.log | wc -l > /var/tmp/error_count.txt
```""",
        "lfcs_reset": """sudo rm -f /var/tmp/auth_ips.txt /var/tmp/pam_rules.txt /var/tmp/error_count.txt /var/tmp/auth_sample.log"""
    },

    # ==================== DAY 3 ====================
    {
        "day": 3,
        "date": "2026-10-07",
        "cka_title": "Services: ClusterIP, NodePort & LoadBalancer",
        "cka_diff": "Medium",
        "cka_time": "35m",
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
        "cka_reset": """ssh controlplane 'kubectl delete namespace prod --grace-period=0 --force 2>/dev/null || true'""",

        "lfcs_title": "Advanced Stream Analysis: Sed & Awk Fundamentals",
        "lfcs_diff": "Medium",
        "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Awk Field Extraction
Extract users from `/etc/passwd` whose UID is >= 1000 and print formatted output:
`User: <name> (UID: <uid>, Shell: <shell>)`
Save output to `/var/tmp/regular_users.txt`.

### Task 2: Sed Stream Editing
In file `/var/tmp/config_sample.ini`:
1. Replace all occurrences of `PORT = 8080` with `PORT = 443`.
2. Delete any line containing `DEBUG = True`.
3. Insert `ENVIRONMENT = Production` on a new line immediately after `[server]`.

### Task 3: CSV Aggregation with Awk
Given `/var/tmp/sales.csv`, compute the total sum of the values in column 2 (revenue).
Output the total number as plain text to `/var/tmp/sales_total.txt`.""",
        "lfcs_setup": """sudo rm -f /var/tmp/regular_users.txt /var/tmp/sales_total.txt
cat << 'EOF' > /var/tmp/config_sample.ini
[server]
HOST = 0.0.0.0
PORT = 8080
DEBUG = True
TIMEOUT = 60
EOF

cat << 'EOF' > /var/tmp/sales.csv
item,price,quantity
widget,25,10
gadget,50,4
gizmo,15,20
EOF""",
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Awk regular users report...${NC}"
if [ -f /var/tmp/regular_users.txt ] && grep -q "UID:" /var/tmp/regular_users.txt; then
  echo -e "${GREEN}[PASS] Awk user report verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/regular_users.txt missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Sed transformations...${NC}"
CONF=$(cat /var/tmp/config_sample.ini 2>/dev/null || true)
if echo "$CONF" | grep -q "PORT = 443" && echo "$CONF" | grep -q "ENVIRONMENT = Production" && ! echo "$CONF" | grep -q "DEBUG"; then
  echo -e "${GREEN}[PASS] Sed transformations verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Transformations missing in /var/tmp/config_sample.ini.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Sales sum...${NC}"
if [ -f /var/tmp/sales_total.txt ] && [ "$(tr -d '[:space:]' < /var/tmp/sales_total.txt)" == "90" ]; then
  echo -e "${GREEN}[PASS] Sales sum matched 90 (25 + 50 + 15).${NC}"
  SCORE=$((SCORE + 1))
else
  VAL=$(cat /var/tmp/sales_total.txt 2>/dev/null || echo "none")
  echo -e "${RED}[FAIL] Sales sum was '$VAL' (expected 90).${NC}"
fi""",
        "lfcs_solution": """1. Awk user extraction:
```bash
awk -F: '$3 >= 1000 { printf "User: %s (UID: %s, Shell: %s)\\n", $1, $3, $7 }' /etc/passwd > /var/tmp/regular_users.txt
```

2. Sed transformations:
```bash
sed -i 's/PORT = 8080/PORT = 443/' /var/tmp/config_sample.ini
sed -i '/DEBUG = True/d' /var/tmp/config_sample.ini
sed -i '/\\[server\\]/a ENVIRONMENT = Production' /var/tmp/config_sample.ini
```

3. CSV aggregation:
```bash
awk -F, 'NR>1 { sum += $2 } END { print sum }' /var/tmp/sales.csv > /var/tmp/sales_total.txt
```""",
        "lfcs_reset": """sudo rm -f /var/tmp/regular_users.txt /var/tmp/config_sample.ini /var/tmp/sales.csv /var/tmp/sales_total.txt"""
    },

    # ==================== DAY 4 ====================
    {
        "day": 4,
        "date": "2026-10-08",
        "cka_title": "Namespaces & DNS Resolution Inside Clusters",
        "cka_diff": "Medium",
        "cka_time": "30m",
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
        "cka_reset": """ssh controlplane 'kubectl delete ns frontend-ns database-ns --grace-period=0 --force 2>/dev/null || true'""",

        "lfcs_title": "I/O Redirection & Stream Multiplexing",
        "lfcs_diff": "Medium",
        "lfcs_time": "25m",
        "lfcs_tasks": """### Task 1: Separate Standard Streams
Search the `/etc` directory for files containing `shadow`:
- Redirect all stdout matches to `/var/tmp/stdout.log` (`1>`).
- Redirect all stderr permission errors to `/var/tmp/stderr.log` (`2>`).

### Task 2: Tee Pipeline Logging
Using `ps -ef` and `tee`, generate a process snapshot:
- Write the full output to `/var/tmp/process_dump.txt`.
- Simultaneously count the total number of lines into `/var/tmp/process_count.txt` via pipe.

### Task 3: Automated Health Report via Heredoc
Write a bash script `/var/tmp/gen_health.sh`:
- When executed, it uses a Here-Document (`cat << 'EOF' > ...`) to write `/var/tmp/health.report`.
- The report must contain lines for `HOST: $(hostname)` and `KERNEL: $(uname -r)`.
- Execute the script and ensure `/var/tmp/health.report` exists.""",
        "lfcs_setup": """sudo rm -f /var/tmp/stdout.log /var/tmp/stderr.log /var/tmp/process_dump.txt /var/tmp/process_count.txt /var/tmp/gen_health.sh /var/tmp/health.report""",
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Separated standard streams...${NC}"
if [ -f /var/tmp/stdout.log ] && [ -f /var/tmp/stderr.log ]; then
  echo -e "${GREEN}[PASS] stdout.log and stderr.log created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Stream files missing.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Process dump and count...${NC}"
if [ -f /var/tmp/process_dump.txt ] && [ -f /var/tmp/process_count.txt ] && [ -s /var/tmp/process_count.txt ]; then
  echo -e "${GREEN}[PASS] Process dump and count verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Process dump files missing or empty.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Health report via heredoc...${NC}"
if [ -f /var/tmp/health.report ] && grep -q "HOST:" /var/tmp/health.report && grep -q "KERNEL:" /var/tmp/health.report; then
  echo -e "${GREEN}[PASS] Health report generated with HOST and KERNEL.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/health.report missing or incomplete.${NC}"
fi""",
        "lfcs_solution": """1. Stream separation:
```bash
find /etc -name "*shadow*" 1> /var/tmp/stdout.log 2> /var/tmp/stderr.log
```

2. Process tee pipeline:
```bash
ps -ef | tee /var/tmp/process_dump.txt | wc -l > /var/tmp/process_count.txt
```

3. Health script with heredoc:
```bash
cat << 'EOF' > /var/tmp/gen_health.sh
#!/usr/bin/env bash
cat << 'REPORT' > /var/tmp/health.report
HOST: $(hostname)
KERNEL: $(uname -r)
REPORT
EOF
chmod +x /var/tmp/gen_health.sh
bash /var/tmp/gen_health.sh
```""",
        "lfcs_reset": """sudo rm -f /var/tmp/stdout.log /var/tmp/stderr.log /var/tmp/process_dump.txt /var/tmp/process_count.txt /var/tmp/gen_health.sh /var/tmp/health.report"""
    },

    # ==================== DAY 5 ====================
    {
        "day": 5,
        "date": "2026-10-09",
        "cka_title": "Kubectl Explain & Declarative Workflow",
        "cka_diff": "Medium",
        "cka_time": "30m",
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

        "lfcs_title": "Archiving, Compression & Remote Backups",
        "lfcs_diff": "Medium",
        "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Gzip Compressed Tar Archive
Create a compressed tar archive of `/etc/systemd/` saved to `/var/tmp/systemd_backup.tar.gz`. Preserve all file permissions (`-p`).

### Task 2: Extract to Alternate Target
Extract `/var/tmp/systemd_backup.tar.gz` into directory `/var/tmp/extracted_systemd/` without changing your current directory.

### Task 3: Tarball Content Verification
List the table of contents of `/var/tmp/systemd_backup.tar.gz` (`-tzf`) and save the file list to `/var/tmp/archive_manifest.txt`.""",
        "lfcs_setup": """sudo rm -rf /var/tmp/systemd_backup.tar.gz /var/tmp/extracted_systemd /var/tmp/archive_manifest.txt""",
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: /var/tmp/systemd_backup.tar.gz...${NC}"
if [ -f /var/tmp/systemd_backup.tar.gz ] && tar -tzf /var/tmp/systemd_backup.tar.gz &>/dev/null; then
  echo -e "${GREEN}[PASS] Gzip tar archive created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/systemd_backup.tar.gz missing or invalid.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Extracted directory...${NC}"
if [ -d /var/tmp/extracted_systemd/etc/systemd ] || [ -d /var/tmp/extracted_systemd/systemd ]; then
  echo -e "${GREEN}[PASS] Archive extracted to target directory.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Extracted directory structure missing.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/archive_manifest.txt...${NC}"
if [ -f /var/tmp/archive_manifest.txt ] && grep -q "system.conf" /var/tmp/archive_manifest.txt; then
  echo -e "${GREEN}[PASS] Archive manifest verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/archive_manifest.txt missing or empty.${NC}"
fi""",
        "lfcs_solution": """1. Create archive:
```bash
sudo tar -czpf /var/tmp/systemd_backup.tar.gz /etc/systemd
```

2. Extract to destination:
```bash
mkdir -p /var/tmp/extracted_systemd
sudo tar -xzf /var/tmp/systemd_backup.tar.gz -C /var/tmp/extracted_systemd
```

3. Manifest:
```bash
tar -tzf /var/tmp/systemd_backup.tar.gz > /var/tmp/archive_manifest.txt
```""",
        "lfcs_reset": """sudo rm -rf /var/tmp/systemd_backup.tar.gz /var/tmp/extracted_systemd /var/tmp/archive_manifest.txt"""
    },

    # ==================== DAY 6 ====================
    {
        "day": 6,
        "date": "2026-10-10",
        "cka_title": "Week 2 Speed Drills & Controller Triathlon",
        "cka_diff": "Hard (Milestone Assessment 2)",
        "cka_time": "45m",
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

        "lfcs_title": "Week 2 Speed Drills & Git Version Control",
        "lfcs_diff": "Hard (Milestone Assessment 2)",
        "lfcs_time": "45m",
        "lfcs_tasks": """### Milestone 2 Triathlon Tasks:
1. Initialize a git repository in `/srv/repo`.
2. Create and commit a configuration file `system.conf` with content `config=v1`.
3. Create a branch `feature-audit`, modify `system.conf` to `config=v2`, commit with message `feat: update v2`, switch back to `main` (or `master`), and merge `feature-audit`.
4. Create a tar.gz backup of the entire git repo into `/var/backups/repo.tar.gz`.""",
        "lfcs_setup": """sudo rm -rf /srv/repo /var/backups/repo.tar.gz""",
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Git repository initialized...${NC}"
if [ -d /srv/repo/.git ]; then
  echo -e "${GREEN}[PASS] Git repo initialized in /srv/repo.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /srv/repo/.git directory not found.${NC}"
fi

echo -e "${BOLD}Checking Task 2 & 3: Branch merge & system.conf...${NC}"
sudo git config --system --add safe.directory /srv/repo 2>/dev/null || true
CONF=$(cat /srv/repo/system.conf 2>/dev/null || echo "None")
COMMITS=$(git -C /srv/repo rev-list --count HEAD 2>/dev/null || sudo git -C /srv/repo rev-list --count HEAD 2>/dev/null || echo "0")
if [ "$CONF" == "config=v2" ] && [ "$COMMITS" -ge 2 ]; then
  echo -e "${GREEN}[PASS] Branch merged with config=v2 and commit history.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] system.conf: $CONF, commits: $COMMITS.${NC}"
fi

echo -e "${BOLD}Checking Task 4: Backup archive...${NC}"
if [ -f /var/backups/repo.tar.gz ] && tar -tzf /var/backups/repo.tar.gz &>/dev/null; then
  echo -e "${GREEN}[PASS] Repository backup archive verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/backups/repo.tar.gz missing or invalid.${NC}"
fi""",
        "lfcs_solution": """1. Init repo:
```bash
sudo mkdir -p /srv/repo
sudo chown -R $(whoami):$(whoami) /srv/repo
cd /srv/repo
git init -b main
git config user.name "Student"
git config user.email "student@example.com"
echo "config=v1" > system.conf
git add system.conf
git commit -m "initial commit"
```

2. Branch and merge:
```bash
git checkout -b feature-audit
echo "config=v2" > system.conf
git commit -am "feat: update v2"
git checkout main
git merge feature-audit
```

3. Tarball backup:
```bash
sudo mkdir -p /var/backups
sudo tar -czf /var/backups/repo.tar.gz -C /srv repo
```""",
        "lfcs_reset": """sudo rm -rf /srv/repo /var/backups/repo.tar.gz"""
    }
]
