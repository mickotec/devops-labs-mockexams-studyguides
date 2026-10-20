"""
CKAD killer.sh Mock Exams 1 and 2
Official Linux Foundation CKAD Domains & Competencies:
  1. Application Environment, Configuration and Security (25%)
  2. Application Design and Build (20%)
  3. Application Deployment (20%)
  4. Services and Networking (20%)
  5. Application Observability and Maintenance (15%)
"""

MOCK_LABS = [
    {
        "lab_id": "mock-ckad-1",
        "track": "CKAD",
        "date": "2026-11-20",
        "title": "CKAD killer.sh Real Exam Simulator 1",
        "diff": "Exam Hard",
        "time": "120m",
        "tasks": """**Passing Score:** 66% (Official Linux Foundation Threshold)
**Time Limit:** 120 minutes
**Target Cluster:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)

---

### Linux Foundation Official CKAD Domains:
1. **Application Environment, Configuration and Security (25%)**
2. **Application Design and Build (20%)**
3. **Application Deployment (20%)**
4. **Services and Networking (20%)**
5. **Application Observability and Maintenance (15%)**

---

### Questions Overview:

#### Domain: Application Environment, Configuration and Security (25% Weight - 4 Questions, 6.25% each)
- **Q1:** In namespace `mock-ckad-1-q1`, create an Opaque Secret named `db-secret` containing keys `username=admin` and `password=SuperSecr3t!`. Create a Pod named `secret-pod` using image `busybox:1.36` (command: `sh -c "sleep 3600"`) that exposes these keys as environment variables `DB_USER` and `DB_PASS` using `valueFrom.secretKeyRef`.
- **Q2:** In namespace `mock-ckad-1-q2`, create a ConfigMap named `app-cfg` with keys `theme=dark` and `max_connections=150`. Create a Pod named `cfg-volume-pod` using image `nginx:alpine` mounting this ConfigMap as a volume at `/etc/app-config`.
- **Q3:** In namespace `mock-ckad-1-q3`, create a secure Pod named `hardened-pod` running image `busybox:1.36` (command `sleep 3600`). In the container's securityContext, configure: `runAsUser: 10001`, `runAsGroup: 20001`, `allowPrivilegeEscalation: false`, drop `ALL` Linux capabilities, and add only capability `NET_BIND_SERVICE`.
- **Q4:** In namespace `mock-ckad-1-q4`, create a ServiceAccount named `report-runner`. Deploy a Pod named `report-worker` using image `busybox:1.36` (command `sleep 3600`) associated with this ServiceAccount. Configure the Pod specification with `automountServiceAccountToken: false` to prevent API token mounting.

#### Domain: Application Design and Build (20% Weight - 3 Questions, 6.67% each)
- **Q5:** In namespace `mock-ckad-1-q5`, deploy a multi-container Pod named `app-with-sidecar`:
  - Main container `app`: image `busybox:1.36`, command `sh -c "while true; do echo \"$(date) - Transaction OK\" >> /var/log/tx.log; sleep 5; done"`.
  - Sidecar container `sidecar`: image `busybox:1.36`, command `sh -c "tail -n+1 -f /var/log/tx.log"`.
  - Mount an `emptyDir` volume named `log-volume` at `/var/log` in both containers.
- **Q6:** In namespace `mock-ckad-1-q6`, create a Pod named `web-init-pod` with:
  - Init container `check-db`: image `busybox:1.36`, command `sh -c "until nc -z -w 2 db-service 5432; do echo waiting for db; sleep 2; done"`.
  - Main container `web`: image `nginx:alpine`, port 80.
  - Deploy a ClusterIP Service named `db-service` on port 5432 targeting existing pod `db-backend` in the same namespace so the init container succeeds.
- **Q7:** Create a PersistentVolume named `mock1-pv` with capacity `1Gi`, accessModes `ReadWriteOnce`, storageClassName `manual`, hostPath `/data/mock1` on node `node01`. In namespace `mock-ckad-1-q7`, create a PersistentVolumeClaim named `mock1-pvc` requesting `500Mi` with storageClassName `manual` and `ReadWriteOnce`. Create a Pod named `pvc-pod` using image `nginx:alpine` mounting `mock1-pvc` at `/data`.

#### Domain: Application Deployment (20% Weight - 3 Questions, 6.67% each)
- **Q8:** In namespace `mock-ckad-1-q8`, deployment `store-api` is running with 3 replicas of `nginx:1.24-alpine`. Update its rolling update strategy to `maxSurge: 1` and `maxUnavailable: 0`. Update the container image to `nginx:1.25.4-alpine` with change-cause annotation `kubernetes.io/change-cause="Upgrade to 1.25.4"`.
- **Q9:** In namespace `mock-ckad-1-q9`, implementations for Blue/Green deployment are present: deployments `payments-blue` (v1) and `payments-green` (v2). Service `payments-svc` currently selects `version: v1`. Perform zero-downtime cutover by updating `payments-svc` to select `version: v2`.
- **Q10:** In namespace `mock-ckad-1-q10`, deployment `frontend-stable` has 8 replicas (`app=frontend,track=stable`). Deploy a canary deployment named `frontend-canary` with 2 replicas of `nginx:alpine` (`app=frontend,track=canary`). Create a Service named `frontend-svc` selecting `app=frontend` to distribute traffic 80% stable and 20% canary.

#### Domain: Services and Networking (20% Weight - 3 Questions, 6.67% each)
- **Q11:** In namespace `mock-ckad-1-q11`, Pods with label `role=database` listen on port `5432`. Create a NetworkPolicy named `db-access-policy` allowing ingress traffic to `role=database` pods ONLY from pods with label `role=backend` on TCP port `5432`. All other ingress traffic to database pods must be denied.
- **Q12:** In namespace `mock-ckad-1-q12`, create an Ingress resource named `api-ingress`:
  - Host: `store.example.com`
  - Path `/v1` routing to service `svc-v1:8080`
  - Path `/v2` routing to service `svc-v2:8080`
  - Annotation: `nginx.ingress.kubernetes.io/rewrite-target: /`
- **Q13:** In namespace `mock-ckad-1-q13`, expose existing deployment `inventory-service` via a NodePort Service named `inventory-np` on port `80` targeting container port `8080` with nodePort `30088`.

#### Domain: Application Observability and Maintenance (15% Weight - 3 Questions, 5.0% each)
- **Q14:** In namespace `mock-ckad-1-q14`, configure Pod `probed-web` (image `nginx:alpine`):
  - Liveness probe: HTTP GET `/healthz` on port 80, `initialDelaySeconds: 5`, `periodSeconds: 5`.
  - Readiness probe: Exec command `cat /tmp/ready`, `initialDelaySeconds: 2`, `periodSeconds: 3`.
  - Create file `/tmp/ready` inside the container so it passes readiness.
- **Q15:** In namespace `mock-ckad-1-q15`, Pod `order-worker` is failing in `CrashLoopBackOff`. Inspect previous container logs with `kubectl logs --previous` and fix the missing environment variable `DB_HOST=postgres` in the Pod manifest so it runs cleanly (1/1 Ready).
- **Q16:** Pod `gateway-hub` in namespace `mock-ckad-1-q16` runs two containers: `ingress-proxy` and `egress-proxy`. Extract all log lines containing `FATAL` from container `ingress-proxy` and save them to `/tmp/fatal-errors.txt` on `controlplane`.""",
        "setup": """ssh controlplane '
for q in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16; do
  kubectl create namespace mock-ckad-1-q$q --dry-run=client -o yaml | kubectl apply -f -
done

# Q6 setup
kubectl run db-backend --image=nginx:alpine --port=5432 -n mock-ckad-1-q6 --labels="app=db" 2>/dev/null || true

# Q8 setup
kubectl create deployment store-api --image=nginx:1.24-alpine --replicas=3 -n mock-ckad-1-q8 --dry-run=client -o yaml | kubectl apply -f -

# Q9 setup
cat << "EOF_Q9" | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payments-blue
  namespace: mock-ckad-1-q9
spec:
  replicas: 2
  selector:
    matchLabels:
      app: payments
      version: v1
  template:
    metadata:
      labels:
        app: payments
        version: v1
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payments-green
  namespace: mock-ckad-1-q9
spec:
  replicas: 2
  selector:
    matchLabels:
      app: payments
      version: v2
  template:
    metadata:
      labels:
        app: payments
        version: v2
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
---
apiVersion: v1
kind: Service
metadata:
  name: payments-svc
  namespace: mock-ckad-1-q9
spec:
  selector:
    app: payments
    version: v1
  ports:
  - port: 80
    targetPort: 80
EOF_Q9

# Q10 setup
cat << "EOF_Q10" | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-stable
  namespace: mock-ckad-1-q10
spec:
  replicas: 8
  selector:
    matchLabels:
      app: frontend
      track: stable
  template:
    metadata:
      labels:
        app: frontend
        track: stable
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
EOF_Q10

# Q11 setup
kubectl run db-pod --image=nginx:alpine --port=5432 --labels="role=database" -n mock-ckad-1-q11 2>/dev/null || true
kubectl run backend-client --image=busybox:1.36 --labels="role=backend" -n mock-ckad-1-q11 -- sleep 3600 2>/dev/null || true
kubectl run rogue-client --image=busybox:1.36 --labels="role=rogue" -n mock-ckad-1-q11 -- sleep 3600 2>/dev/null || true

# Q12 setup
kubectl create service clusterip svc-v1 --tcp=8080:80 -n mock-ckad-1-q12 2>/dev/null || true
kubectl create service clusterip svc-v2 --tcp=8080:80 -n mock-ckad-1-q12 2>/dev/null || true

# Q13 setup
kubectl create deployment inventory-service --image=nginx:alpine --port=8080 -n mock-ckad-1-q13 --dry-run=client -o yaml | kubectl apply -f -

# Q15 setup
cat << "EOF_Q15" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: order-worker
  namespace: mock-ckad-1-q15
spec:
  containers:
  - name: worker
    image: busybox:1.36
    command: ["sh", "-c", "if [ -z \\"$DB_HOST\\" ]; then echo 'FATAL: Missing DB_HOST' >&2; exit 1; else sleep 3600; fi"]
EOF_Q15

# Q16 setup
cat << "EOF_Q16" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: gateway-hub
  namespace: mock-ckad-1-q16
spec:
  containers:
  - name: ingress-proxy
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo 'INFO 200 OK'; sleep 1; echo 'FATAL Gateway Timeout' >&2; sleep 2; done"]
  - name: egress-proxy
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo 'INFO outbound'; sleep 2; done"]
EOF_Q16
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
SCORE=0; TOTAL=16

echo "=========================================================================="
echo "          CKAD killer.sh Mock Exam 1 Scorecard & Evaluation               "
echo "=========================================================================="

# Q1: Secret Env (6.25%)
Q1=$(ssh controlplane 'kubectl get pod secret-pod -n mock-ckad-1-q1 -o jsonpath="{.spec.containers[0].env[0].valueFrom.secretKeyRef.name}" 2>/dev/null || echo ""')
[ "$Q1" == "db-secret" ] && { echo -e "\033[0;32m[PASS] Q1: secret-pod configured with db-secret.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q1: secretKeyRef mismatch.\033[0m"

# Q2: ConfigMap Volume (6.25%)
Q2=$(ssh controlplane 'kubectl get pod cfg-volume-pod -n mock-ckad-1-q2 -o jsonpath="{.spec.volumes[0].configMap.name}" 2>/dev/null || echo ""')
[ "$Q2" == "app-cfg" ] && { echo -e "\033[0;32m[PASS] Q2: ConfigMap volume app-cfg mounted.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q2: ConfigMap volume mismatch.\033[0m"

# Q3: SecurityContext (6.25%)
Q3=$(ssh controlplane 'kubectl get pod hardened-pod -n mock-ckad-1-q3 -o jsonpath="{.spec.containers[0].securityContext.runAsUser}" 2>/dev/null || echo 0')
[ "$Q3" == "10001" ] && { echo -e "\033[0;32m[PASS] Q3: hardened-pod runAsUser 10001 confirmed.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q3: SecurityContext runAsUser $Q3.\033[0m"

# Q4: ServiceAccount (6.25%)
Q4_SA=$(ssh controlplane 'kubectl get pod report-worker -n mock-ckad-1-q4 -o jsonpath="{.spec.serviceAccountName}" 2>/dev/null || echo ""')
Q4_AUTO=$(ssh controlplane 'kubectl get pod report-worker -n mock-ckad-1-q4 -o jsonpath="{.spec.automountServiceAccountToken}" 2>/dev/null || echo ""')
[ "$Q4_SA" == "report-runner" ] && [ "$Q4_AUTO" == "false" ] && { echo -e "\033[0;32m[PASS] Q4: report-worker SA & automount=false verified.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q4: SA or automount incorrect.\033[0m"

# Q5: Multi-Container Sidecar (6.67%)
Q5=$(ssh controlplane 'kubectl get pod app-with-sidecar -n mock-ckad-1-q5 -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null | grep -o "true" | wc -l || echo 0')
[ "$Q5" -eq 2 ] && { echo -e "\033[0;32m[PASS] Q5: app-with-sidecar has 2/2 ready containers.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q5: Ready containers: $Q5 (expected 2).\033[0m"

# Q6: Init Container (6.67%)
Q6=$(ssh controlplane 'kubectl get pod web-init-pod -n mock-ckad-1-q6 -o jsonpath="{.status.phase}" 2>/dev/null || echo ""')
[ "$Q6" == "Running" ] && { echo -e "\033[0;32m[PASS] Q6: web-init-pod is in Running state.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q6: web-init-pod status: '$Q6'.\033[0m"

# Q7: PV & PVC (6.67%)
Q7=$(ssh controlplane 'kubectl get pod pvc-pod -n mock-ckad-1-q7 -o jsonpath="{.status.phase}" 2>/dev/null || echo ""')
[ "$Q7" == "Running" ] && { echo -e "\033[0;32m[PASS] Q7: pvc-pod running with bound volume.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q7: pvc-pod status: '$Q7'.\033[0m"

# Q8: Rolling Update (6.67%)
Q8_IMG=$(ssh controlplane 'kubectl get deployment store-api -n mock-ckad-1-q8 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo ""')
[ "$Q8_IMG" == "nginx:1.25.4-alpine" ] && { echo -e "\033[0;32m[PASS] Q8: store-api upgraded to nginx:1.25.4-alpine.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q8: store-api image '$Q8_IMG'.\033[0m"

# Q9: Blue/Green (6.67%)
Q9=$(ssh controlplane 'kubectl get svc payments-svc -n mock-ckad-1-q9 -o jsonpath="{.spec.selector.version}" 2>/dev/null || echo ""')
[ "$Q9" == "v2" ] && { echo -e "\033[0;32m[PASS] Q9: payments-svc cutover to version v2.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q9: Service selector: '$Q9'.\033[0m"

# Q10: Canary (6.67%)
Q10=$(ssh controlplane 'kubectl get deployment frontend-canary -n mock-ckad-1-q10 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
[ "$Q10" -ge 2 ] && { echo -e "\033[0;32m[PASS] Q10: frontend-canary has 2 ready replicas.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q10: Canary ready: $Q10.\033[0m"

# Q11: NetworkPolicy (6.67%)
Q11=$(ssh controlplane 'kubectl get networkpolicy db-access-policy -n mock-ckad-1-q11 -o jsonpath="{.spec.ingress[0].ports[0].port}" 2>/dev/null || echo 0')
[ "$Q11" == "5432" ] && { echo -e "\033[0;32m[PASS] Q11: db-access-policy enforces port 5432.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q11: Policy port mismatch: $Q11.\033[0m"

# Q12: Ingress (6.67%)
Q12=$(ssh controlplane 'kubectl get ingress api-ingress -n mock-ckad-1-q12 -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo ""')
[ "$Q12" == "store.example.com" ] && { echo -e "\033[0;32m[PASS] Q12: api-ingress host store.example.com configured.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q12: Ingress host '$Q12'.\033[0m"

# Q13: NodePort Svc (6.67%)
Q13=$(ssh controlplane 'kubectl get svc inventory-np -n mock-ckad-1-q13 -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo 0')
[ "$Q13" -eq 30088 ] && { echo -e "\033[0;32m[PASS] Q13: inventory-np nodePort 30088 verified.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q13: nodePort $Q13 (expected 30088).\033[0m"

# Q14: Probes (5.0%)
Q14=$(ssh controlplane 'kubectl get pod probed-web -n mock-ckad-1-q14 -o jsonpath="{.status.containerStatuses[0].ready}" 2>/dev/null || echo "false"')
[ "$Q14" == "true" ] && { echo -e "\033[0;32m[PASS] Q14: probed-web passing health checks (Ready).\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q14: Pod ready: '$Q14'.\033[0m"

# Q15: Pod Debugging (5.0%)
Q15_READY=$(ssh controlplane 'kubectl get pod order-worker -n mock-ckad-1-q15 -o jsonpath="{.status.containerStatuses[0].ready}" 2>/dev/null || echo "false"')
Q15_ENV=$(ssh controlplane 'kubectl get pod order-worker -n mock-ckad-1-q15 -o yaml 2>/dev/null | grep -q "value: postgres" && echo "postgres" || echo ""')
[ "$Q15_READY" == "true" ] && [ "$Q15_ENV" == "postgres" ] && { echo -e "\033[0;32m[PASS] Q15: order-worker debugged (Ready & DB_HOST=postgres).\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q15: order-worker ready='$Q15_READY', DB_HOST='$Q15_ENV'.\033[0m"

# Q16: Log Extraction (5.0%)
Q16=$(ssh controlplane 'grep -c "FATAL" /tmp/fatal-errors.txt 2>/dev/null || echo 0')
[ "$Q16" -ge 1 ] && { echo -e "\033[0;32m[PASS] Q16: /tmp/fatal-errors.txt contains $Q16 FATAL log lines.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q16: Log file missing or empty.\033[0m"

PCT=$(( SCORE * 100 / TOTAL ))
echo "=========================================================================="
echo "Final Score: $SCORE / $TOTAL ($PCT%)"
[ $PCT -ge 66 ] && { echo -e "\033[0;32mPASSED! Congratulations on clearing CKAD Mock Exam 1! (Threshold: 66%)\033[0m"; exit 0; } || { echo -e "\033[0;31mFAILED ($PCT% < 66%)\033[0m"; exit 1; }""",
        "solution": """### Official Solutions: CKAD Mock Exam 1
See detailed solutions in the web dashboard solution viewer.""",
        "reset": """ssh controlplane '
NS_LIST=$(for q in {1..16}; do echo -n "mock-ckad-1-q$q "; done)
kubectl delete namespace $NS_LIST --ignore-not-found --wait=false 2>/dev/null || true
kubectl delete pv mock1-pv --ignore-not-found --wait=false 2>/dev/null || true
rm -f /tmp/fatal-errors.txt
'"""
    },
    {
        "lab_id": "mock-ckad-2",
        "track": "CKAD",
        "date": "2026-11-21",
        "title": "CKAD killer.sh Real Exam Simulator 2",
        "diff": "Exam Hard",
        "time": "120m",
        "tasks": """**Passing Score:** 66% (Official Linux Foundation Threshold)
**Time Limit:** 120 minutes
**Target Cluster:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)

---

### Linux Foundation Official CKAD Domains:
1. **Application Environment, Configuration and Security (25%)**
2. **Application Design and Build (20%)**
3. **Application Deployment (20%)**
4. **Services and Networking (20%)**
5. **Application Observability and Maintenance (15%)**

---

### Questions Overview:

#### Domain: Application Environment, Configuration and Security (25% Weight - 4 Questions, 6.25% each)
- **Q1:** In namespace `mock-ckad-2-q1`, create a Secret named `api-tokens` with keys `TOKEN_A=Alpha99` and `TOKEN_B=Beta88`. Deploy a Pod `token-consumer` injecting all keys as environment variables using `envFrom.secretRef`.
- **Q2:** In namespace `mock-ckad-2-q2`, create a ResourceQuota named `compute-quota` capping total CPU requests at `1` and total Memory requests at `1Gi`. Modify the failing deployment `batch-app` so its pod container requests `250m` CPU and `256Mi` Memory to comply with the quota.
- **Q3:** In namespace `mock-ckad-2-q3`, deploy secure Pod `isolated-app` running `nginx:alpine`:
  - Set `readOnlyRootFilesystem: true`.
  - Mount an `emptyDir` volume at `/var/cache/nginx` and `/var/run` to allow nginx runtime state.
- **Q4:** In namespace `mock-ckad-2-q4`, create a Role named `secret-viewer` granting `get, list` permissions on `secrets`. Bind this role to ServiceAccount `app-deployer` using a RoleBinding named `bind-secret-viewer`.

#### Domain: Application Design and Build (20% Weight - 3 Questions, 6.67% each)
- **Q5:** In namespace `mock-ckad-2-q5`, create a CronJob named `db-backup-cron`:
  - Schedule: every 2 hours (`0 */2 * * *`)
  - Image: `busybox:1.36`, command: `echo "Backup completed"`
  - `concurrencyPolicy: Forbid`
  - `successfulJobsHistoryLimit: 3`
- **Q6:** In namespace `mock-ckad-2-q6`, create a multi-container adapter Pod named `metric-adapter`:
  - App container writes `status: 200` to `/var/data/status.txt`.
  - Adapter container reads `/var/data/status.txt` and formats as `http_requests_total{status="200"} 1`.
  - Mount shared `emptyDir` volume `metric-data` at `/var/data`.
- **Q7:** In namespace `mock-ckad-2-q7`, deploy a StatefulSet named `db-cluster` with 2 replicas of `redis:alpine` using a Headless Service `redis-headless` (`clusterIP: None`) on port 6379.

#### Domain: Application Deployment (20% Weight - 3 Questions, 6.67% each)
- **Q8:** On `controlplane`, configure a Kustomize application structure under `/tmp/kustomize-store`:
  - `base/kustomization.yaml` managing a Deployment of `nginx:1.24` and ClusterIP Service.
  - `overlays/prod/kustomization.yaml` adding commonLabel `env: production`, namePrefix `prod-`, and replicas `3`.
- **Q9:** In namespace `mock-ckad-2-q9`, deployment `checkout` has introduced a bug in revision 2. Roll back the deployment to revision 1 (`kubectl rollout undo`).
- **Q10:** In namespace `mock-ckad-2-q10`, create a Canary deployment `web-v2` with 1 replica alongside existing deployment `web-v1` (3 replicas). Both must share service `web-service` on port 80.

#### Domain: Services and Networking (20% Weight - 3 Questions, 6.67% each)
- **Q11:** In namespace `mock-ckad-2-q11`, create a NetworkPolicy `deny-all-ingress` that isolates all pods in the namespace by denying all incoming traffic unless explicitly allowed.
- **Q12:** In namespace `mock-ckad-2-q12`, create an Ingress named `customer-ingress` routing host `portal.internal` path `/orders` to service `order-svc:8080` and path `/catalog` to service `catalog-svc:8080`.
- **Q13:** In namespace `mock-ckad-2-q13`, expose Pod `redis-cache` with a ClusterIP service named `redis-service` mapping port `6379` to container targetPort `6379`.

#### Domain: Application Observability and Maintenance (15% Weight - 3 Questions, 5.0% each)
- **Q14:** In namespace `mock-ckad-2-q14`, Pod `slow-starter` takes 45 seconds to initialize:
  - Add a Startup Probe with HTTP GET `/health` on port 80, `failureThreshold: 30`, `periodSeconds: 5`.
  - Add a Liveness Probe with HTTP GET `/health` on port 80, `periodSeconds: 10`.
- **Q15:** Discover and inspect deprecated API versions on the cluster. Identify the API version replacement for `HorizontalPodAutoscaler` in `autoscaling/v2` and write the API version string to `/tmp/hpa-version.txt`.
- **Q16:** Monitor cluster workloads using CLI: identify the pod with the highest CPU usage in namespace `kube-system` and save its name to `/tmp/top-pod.txt`.""",
        "setup": """ssh controlplane '
for q in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16; do
  kubectl create namespace mock-ckad-2-q$q --dry-run=client -o yaml | kubectl apply -f -
done

# Q2 setup: quota + over-request pod
cat << "EOF_Q2" | kubectl apply -f -
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-quota
  namespace: mock-ckad-2-q2
spec:
  hard:
    requests.cpu: "1"
    requests.memory: 1Gi
EOF_Q2

# Q4 setup: ServiceAccount
kubectl create serviceaccount app-deployer -n mock-ckad-2-q4 2>/dev/null || true

# Q9 setup: deployment with rollout revision
kubectl create deployment checkout --image=nginx:1.24-alpine --replicas=2 -n mock-ckad-2-q9 --dry-run=client -o yaml | kubectl apply -f -
kubectl set image deployment/checkout nginx=nginx:broken-nonexistent -n mock-ckad-2-q9 2>/dev/null || true

# Q10 setup: web-v1 & service
kubectl create deployment web-v1 --image=nginx:alpine --replicas=3 -n mock-ckad-2-q10 --dry-run=client -o yaml | sed "s/app: web-v1/app: web-shared/" | kubectl apply -f -
kubectl create service clusterip web-service --tcp=80:80 -n mock-ckad-2-q10 --dry-run=client -o yaml | sed "s/app: web-service/app: web-shared/" | kubectl apply -f -

# Q12 setup: services
kubectl create service clusterip order-svc --tcp=8080:80 -n mock-ckad-2-q12 2>/dev/null || true
kubectl create service clusterip catalog-svc --tcp=8080:80 -n mock-ckad-2-q12 2>/dev/null || true

# Q13 setup: pod
kubectl run redis-cache --image=redis:alpine --port=6379 -n mock-ckad-2-q13 2>/dev/null || true
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
SCORE=0; TOTAL=16

echo "=========================================================================="
echo "          CKAD killer.sh Mock Exam 2 Scorecard & Evaluation               "
echo "=========================================================================="

# Q1: Secret envFrom (6.25%)
Q1=$(ssh controlplane 'kubectl get pod token-consumer -n mock-ckad-2-q1 -o jsonpath="{.spec.containers[0].envFrom[0].secretRef.name}" 2>/dev/null || echo ""')
[ "$Q1" == "api-tokens" ] && { echo -e "\033[0;32m[PASS] Q1: token-consumer envFrom api-tokens.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q1: secretRef mismatch.\033[0m"

# Q2: Quota (6.25%)
Q2=$(ssh controlplane 'kubectl get pods -n mock-ckad-2-q2 -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo ""')
[ "$Q2" == "Running" ] && { echo -e "\033[0;32m[PASS] Q2: Quota pod Running.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q2: Pod status: '$Q2'.\033[0m"

# Q3: SecurityContext (6.25%)
Q3=$(ssh controlplane 'kubectl get pod isolated-app -n mock-ckad-2-q3 -o jsonpath="{.spec.containers[0].securityContext.readOnlyRootFilesystem}" 2>/dev/null || echo ""')
[ "$Q3" == "true" ] && { echo -e "\033[0;32m[PASS] Q3: isolated-app readOnlyRootFilesystem=true.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q3: SecurityContext mismatch.\033[0m"

# Q4: RBAC (6.25%)
Q4=$(ssh controlplane 'kubectl get rolebinding bind-secret-viewer -n mock-ckad-2-q4 -o jsonpath="{.roleRef.name}" 2>/dev/null || echo ""')
[ "$Q4" == "secret-viewer" ] && { echo -e "\033[0;32m[PASS] Q4: bind-secret-viewer references secret-viewer.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q4: RoleBinding mismatch.\033[0m"

# Q5: CronJob (6.67%)
Q5=$(ssh controlplane 'kubectl get cronjob db-backup-cron -n mock-ckad-2-q5 -o jsonpath="{.spec.concurrencyPolicy}" 2>/dev/null || echo ""')
[ "$Q5" == "Forbid" ] && { echo -e "\033[0;32m[PASS] Q5: db-backup-cron concurrencyPolicy=Forbid.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q5: CronJob mismatch.\033[0m"

# Q6: Adapter (6.67%)
Q6=$(ssh controlplane 'kubectl get pod metric-adapter -n mock-ckad-2-q6 -o jsonpath="{.status.containerStatuses[*].ready}" 2>/dev/null | grep -o "true" | wc -l || echo 0')
[ "$Q6" -eq 2 ] && { echo -e "\033[0;32m[PASS] Q6: metric-adapter has 2 ready containers.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q6: Ready count: $Q6.\033[0m"

# Q7: StatefulSet (6.67%)
Q7=$(ssh controlplane 'kubectl get statefulset db-cluster -n mock-ckad-2-q7 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
[ "$Q7" -ge 2 ] && { echo -e "\033[0;32m[PASS] Q7: db-cluster statefulset ready.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q7: StatefulSet ready: $Q7.\033[0m"

# Q8: Kustomize (6.67%)
Q8=$(ssh controlplane 'test -d /tmp/kustomize-store/overlays/prod && echo "OK" || echo ""')
[ "$Q8" == "OK" ] && { echo -e "\033[0;32m[PASS] Q8: Kustomize store structure exists.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q8: /tmp/kustomize-store missing.\033[0m"

# Q9: Rollback (6.67%)
Q9=$(ssh controlplane 'kubectl get deployment checkout -n mock-ckad-2-q9 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo ""')
[ "$Q9" == "nginx:1.24-alpine" ] && { echo -e "\033[0;32m[PASS] Q9: checkout rolled back to nginx:1.24-alpine.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q9: Image '$Q9'.\033[0m"

# Q10: Canary (6.67%)
Q10=$(ssh controlplane 'kubectl get deployment web-v2 -n mock-ckad-2-q10 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
[ "$Q10" -ge 1 ] && { echo -e "\033[0;32m[PASS] Q10: web-v2 canary running.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q10: web-v2 ready: $Q10.\033[0m"

# Q11: NetworkPolicy Deny (6.67%)
Q11=$(ssh controlplane 'kubectl get networkpolicy deny-all-ingress -n mock-ckad-2-q11 -o jsonpath="{.spec.policyTypes[0]}" 2>/dev/null || echo ""')
[ "$Q11" == "Ingress" ] && { echo -e "\033[0;32m[PASS] Q11: deny-all-ingress configured.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q11: Policy missing.\033[0m"

# Q12: Ingress (6.67%)
Q12=$(ssh controlplane 'kubectl get ingress customer-ingress -n mock-ckad-2-q12 -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo ""')
[ "$Q12" == "portal.internal" ] && { echo -e "\033[0;32m[PASS] Q12: customer-ingress configured for portal.internal.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q12: Ingress host '$Q12'.\033[0m"

# Q13: Service (6.67%)
Q13=$(ssh controlplane 'kubectl get svc redis-service -n mock-ckad-2-q13 -o jsonpath="{.spec.ports[0].port}" 2>/dev/null || echo 0')
[ "$Q13" -eq 6379 ] && { echo -e "\033[0;32m[PASS] Q13: redis-service port 6379 verified.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q13: Service port $Q13.\033[0m"

# Q14: Startup Probe (5.0%)
Q14=$(ssh controlplane 'kubectl get pod slow-starter -n mock-ckad-2-q14 -o jsonpath="{.spec.containers[0].startupProbe.failureThreshold}" 2>/dev/null || echo 0')
[ "$Q14" -eq 30 ] && { echo -e "\033[0;32m[PASS] Q14: slow-starter startup probe failureThreshold=30.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q14: Startup probe threshold $Q14.\033[0m"

# Q15: Deprecated API (5.0%)
Q15=$(ssh controlplane 'grep -qi "autoscaling/v2" /tmp/hpa-version.txt 2>/dev/null && echo "OK" || echo ""')
[ "$Q15" == "OK" ] && { echo -e "\033[0;32m[PASS] Q15: /tmp/hpa-version.txt contains autoscaling/v2.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q15: File missing or invalid.\033[0m"

# Q16: Top Pod (5.0%)
Q16=$(ssh controlplane 'test -s /tmp/top-pod.txt && echo "OK" || echo ""')
[ "$Q16" == "OK" ] && { echo -e "\033[0;32m[PASS] Q16: /tmp/top-pod.txt populated.\033[0m"; SCORE=$((SCORE + 1)); } || echo -e "\033[0;31m[FAIL] Q16: File missing.\033[0m"

PCT=$(( SCORE * 100 / TOTAL ))
echo "=========================================================================="
echo "Final Score: $SCORE / $TOTAL ($PCT%)"
[ $PCT -ge 66 ] && { echo -e "\033[0;32mPASSED! Passed CKAD Mock Exam 2!\033[0m"; exit 0; } || { echo -e "\033[0;31mFAILED ($PCT% < 66%)\033[0m"; exit 1; }""",
        "solution": """### Official Solutions: CKAD Mock Exam 2
See detailed solutions in the web dashboard solution viewer.""",
        "reset": """ssh controlplane '
NS_LIST=$(for q in {1..16}; do echo -n "mock-ckad-2-q$q "; done)
kubectl delete namespace $NS_LIST --ignore-not-found --wait=false 2>/dev/null || true
rm -rf /tmp/kustomize-store /tmp/hpa-version.txt /tmp/top-pod.txt
'"""
    }
]
