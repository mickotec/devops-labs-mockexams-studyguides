"""
Dedicated CKAD Lab Definitions for Week 2 (Days 1 to 6).
Aligned with KodeKloud CKAD Learning Modules: Configuration
"""

WEEK_2_LABS = [
    {
        "day": 1,
        "date": "2026-10-19",
        "title": "Container Commands & Arguments Execution",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Override Container Entrypoint & Arguments
1. In namespace `ckad-w2d1`, create a Pod named `report-worker` running image `busybox:1.36`.
2. Configure the container to override the default command and arguments:
   - `command`: `["/bin/sh"]`
   - `args`: `["-c", "mkdir -p /tmp/reports && while true; do date >> /tmp/reports/output.txt; sleep 3; done"]`
3. Ensure the pod transitions to `Running` state and `/tmp/reports/output.txt` is populated.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w2d1 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W2D1: Container Commands & Arguments in ckad-w2d1..."

PHASE=$(ssh controlplane 'kubectl get pod report-worker -n ckad-w2d1 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
OUTPUT=$(ssh controlplane 'kubectl exec report-worker -n ckad-w2d1 -- cat /tmp/reports/output.txt 2>/dev/null | head -n 1 || echo "Empty"')

if [ "$PHASE" == "Running" ] && [ "$OUTPUT" != "Empty" ]; then
  echo -e "\033[0;32m[PASS] Pod report-worker running with custom command & args generating output.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: '$PHASE' | Output: '$OUTPUT' (expected Running with report content).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Container Commands & Arguments
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: report-worker
  namespace: ckad-w2d1
spec:
  containers:
  - name: worker
    image: busybox:1.36
    command: ["/bin/sh"]
    args: ["-c", "mkdir -p /tmp/reports && while true; do date >> /tmp/reports/output.txt; sleep 3; done"]
EOF_POD
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w2d1 --ignore-not-found'"""
    },
    {
        "day": 2,
        "date": "2026-10-20",
        "title": "ConfigMaps & Environment Variable Injections",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Create ConfigMap & Inject via envFrom
1. In namespace `ckad-w2d2`, create a ConfigMap named `backend-config` with keys:
   - `DB_HOST=postgres.internal`
   - `DB_PORT=5432`
   - `CACHE_TTL=3600`
2. Deploy Pod `app-server` using image `busybox:1.36` sleeping continuously (`sleep 3600`).
3. Inject ALL keys from `backend-config` into the container using `envFrom.configMapRef`.
4. Also define an individual environment variable named `APP_ENV` with literal value `"production"` directly in `spec.containers[0].env`.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w2d2 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W2D2: ConfigMaps & Environment Variables in ckad-w2d2..."

PHASE=$(ssh controlplane 'kubectl get pod app-server -n ckad-w2d2 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
ENV_DB_HOST=$(ssh controlplane 'kubectl exec app-server -n ckad-w2d2 -- printenv DB_HOST 2>/dev/null || echo ""')
ENV_APP_ENV=$(ssh controlplane 'kubectl exec app-server -n ckad-w2d2 -- printenv APP_ENV 2>/dev/null || echo ""')

if [ "$PHASE" == "Running" ] && [ "$ENV_DB_HOST" == "postgres.internal" ] && [ "$ENV_APP_ENV" == "production" ]; then
  echo -e "\033[0;32m[PASS] Pod app-server successfully injected with envFrom ConfigMap and literal env.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: $PHASE | DB_HOST: '$ENV_DB_HOST' | APP_ENV: '$ENV_APP_ENV'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: ConfigMaps & Env
```bash
ssh controlplane '
kubectl create configmap backend-config -n ckad-w2d2 \
  --from-literal=DB_HOST=postgres.internal \
  --from-literal=DB_PORT=5432 \
  --from-literal=CACHE_TTL=3600

cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: app-server
  namespace: ckad-w2d2
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sleep", "3600"]
    env:
    - name: APP_ENV
      value: "production"
    envFrom:
    - configMapRef:
        name: backend-config
EOF_POD
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w2d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-10-21",
        "title": "Mounting ConfigMaps as Filesystem Volumes",
        "diff": "Medium",
        "time": "30m",
        "tasks": """### Task 1: Mount Custom Configuration File into Nginx
1. In namespace `ckad-w2d3`, create a ConfigMap named `custom-nginx-conf` containing key `default.conf` with content:
   `server { listen 8088; location / { return 200 "CUSTOM-PORT-OK\n"; } }`
2. Deploy Pod `nginx-custom-port` using image `nginx:1.24-alpine`.
3. Mount the ConfigMap volume at `/etc/nginx/conf.d` so Nginx loads the custom configuration.
4. Verify that running `wget -qO- 127.0.0.1:8088` inside the container returns `"CUSTOM-PORT-OK"`.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w2d3 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W2D3: ConfigMaps as Volumes in ckad-w2d3..."

PHASE=$(ssh controlplane 'kubectl get pod nginx-custom-port -n ckad-w2d3 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
RESP=$(ssh controlplane 'kubectl exec nginx-custom-port -n ckad-w2d3 -- wget -qO- 127.0.0.1:8088 2>/dev/null || echo "Failed"')

if [ "$PHASE" == "Running" ] && [[ "$RESP" =~ "CUSTOM-PORT-OK" ]]; then
  echo -e "\033[0;32m[PASS] Pod nginx-custom-port successfully loaded ConfigMap volume on port 8088.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: '$PHASE' | Curl Response: '$RESP' (expected CUSTOM-PORT-OK).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: ConfigMaps as Volumes
```bash
ssh controlplane '
cat << "EOF_CONF" | kubectl apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
  name: custom-nginx-conf
  namespace: ckad-w2d3
data:
  default.conf: |
    server {
      listen 8088;
      location / {
        return 200 "CUSTOM-PORT-OK\n";
      }
    }
---
apiVersion: v1
kind: Pod
metadata:
  name: nginx-custom-port
  namespace: ckad-w2d3
spec:
  volumes:
  - name: conf-vol
    configMap:
      name: custom-nginx-conf
  containers:
  - name: web
    image: nginx:1.24-alpine
    ports:
    - containerPort: 8088
    volumeMounts:
    - name: conf-vol
      mountPath: /etc/nginx/conf.d
EOF_CONF
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w2d3 --ignore-not-found'"""
    },
    {
        "day": 4,
        "date": "2026-10-22",
        "title": "Secrets Management & Restricted File Modes",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Mount Secret Volume with 0400 Permissions
1. In namespace `ckad-w2d4`, create an Opaque Secret named `api-credentials` containing keys:
   - `api-key`: `secret-alpha-9988`
   - `api-token`: `token-beta-7766`
2. Deploy Pod `auth-consumer` with image `busybox:1.36` sleeping continuously (`sleep 3600`).
3. Mount the Secret as a volume at `/etc/api-keys` with file permission mode `0400` (`r--------`).
4. Ensure the file `/etc/api-keys/api-key` is readable and its permission mode is verified.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w2d4 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W2D4: Secrets & File Modes in ckad-w2d4..."

PHASE=$(ssh controlplane 'kubectl get pod auth-consumer -n ckad-w2d4 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
CONTENT=$(ssh controlplane 'kubectl exec auth-consumer -n ckad-w2d4 -- cat /etc/api-keys/api-key 2>/dev/null || echo ""')
PERM=$(ssh controlplane 'kubectl exec auth-consumer -n ckad-w2d4 -- stat -c "%a" /etc/api-keys/api-key 2>/dev/null || echo ""')

if [ "$PHASE" == "Running" ] && [ "$CONTENT" == "secret-alpha-9988" ] && [ "$PERM" == "400" ]; then
  echo -e "\033[0;32m[PASS] Secret volume mounted with permission 0400 and valid credentials.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: $PHASE | Content: '$CONTENT' | Mode: '$PERM' (expected 400).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Secrets & Restricted Modes
```bash
ssh controlplane '
kubectl create secret generic api-credentials -n ckad-w2d4 \
  --from-literal=api-key=secret-alpha-9988 \
  --from-literal=api-token=token-beta-7766

cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: auth-consumer
  namespace: ckad-w2d4
spec:
  volumes:
  - name: secret-vol
    secret:
      secretName: api-credentials
      defaultMode: 0400
  containers:
  - name: app
    image: busybox:1.36
    command: ["sleep", "3600"]
    volumeMounts:
    - name: secret-vol
      mountPath: /etc/api-keys
EOF_POD
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w2d4 --ignore-not-found'"""
    },
    {
        "day": 5,
        "date": "2026-10-23",
        "title": "SecurityContexts, Non-Root & Linux Capabilities",
        "diff": "Hard",
        "time": "30m",
        "tasks": """### Task 1: Secure Container Execution Context
1. In namespace `ckad-w2d5`, create a secure Pod named `locked-container` using image `nginx:alpine`.
2. Configure Pod and Container SecurityContexts to enforce:
   - Pod level: `runAsUser: 2000`, `runAsGroup: 2000`, `runAsNonRoot: true`
   - Container level: `readOnlyRootFilesystem: true`
   - Container capabilities: drop `ALL`, add `NET_BIND_SERVICE`
3. Because the root filesystem is read-only, mount an `emptyDir` volume at `/var/cache/nginx`, `/var/run`, and `/tmp` so Nginx can write runtime PID and cache files.
4. Verify that `locked-container` achieves `Running` status (1/1 Ready).""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w2d5 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W2D5: SecurityContexts & Capabilities in ckad-w2d5..."

PHASE=$(ssh controlplane 'kubectl get pod locked-container -n ckad-w2d5 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
READY=$(ssh controlplane 'kubectl get pod locked-container -n ckad-w2d5 -o jsonpath="{.status.containerStatuses[0].ready}" 2>/dev/null || echo "false"')
UID_VAL=$(ssh controlplane 'kubectl get pod locked-container -n ckad-w2d5 -o jsonpath="{.spec.securityContext.runAsUser}" 2>/dev/null || echo 0')
READONLY=$(ssh controlplane 'kubectl get pod locked-container -n ckad-w2d5 -o jsonpath="{.spec.containers[0].securityContext.readOnlyRootFilesystem}" 2>/dev/null || echo "false"')

if [ "$PHASE" == "Running" ] && [ "$READY" == "true" ] && [ "$UID_VAL" -eq 2000 ] && [ "$READONLY" == "true" ]; then
  echo -e "\033[0;32m[PASS] Pod locked-container running as non-root (UID 2000) with readOnlyRootFilesystem.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: $PHASE, Ready: $READY, UID: $UID_VAL (expected 2000), ReadOnly: $READONLY (expected true).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: SecurityContexts
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: locked-container
  namespace: ckad-w2d5
spec:
  securityContext:
    runAsUser: 2000
    runAsGroup: 2000
    runAsNonRoot: true
  volumes:
  - name: cache-vol
    emptyDir: {}
  - name: run-vol
    emptyDir: {}
  - name: tmp-vol
    emptyDir: {}
  containers:
  - name: nginx
    image: nginx:alpine
    securityContext:
      readOnlyRootFilesystem: true
      capabilities:
        drop: ["ALL"]
        add: ["NET_BIND_SERVICE"]
    volumeMounts:
    - name: cache-vol
      mountPath: /var/cache/nginx
    - name: run-vol
      mountPath: /var/run
    - name: tmp-vol
      mountPath: /tmp
EOF_POD
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w2d5 --ignore-not-found'"""
    },
    {
        "day": 6,
        "date": "2026-10-24",
        "title": "ServiceAccounts & API Token Security",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Workload Identity & Token Mounting Control
1. In namespace `ckad-w2d6`, create a ServiceAccount named `build-deployer`.
2. Deploy a Pod named `isolated-agent` using image `busybox:1.36` sleeping continuously (`sleep 3600`).
3. Configure the pod to use ServiceAccount `build-deployer`.
4. Explicitly disable mounting the API token credential into the container by configuring:
   `automountServiceAccountToken: false` in the pod spec.
5. Verify that `/var/run/secrets/kubernetes.io/serviceaccount` does NOT exist inside the container.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w2d6 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W2D6: ServiceAccounts & Token Control in ckad-w2d6..."

PHASE=$(ssh controlplane 'kubectl get pod isolated-agent -n ckad-w2d6 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
SA=$(ssh controlplane 'kubectl get pod isolated-agent -n ckad-w2d6 -o jsonpath="{.spec.serviceAccountName}" 2>/dev/null || echo "none"')
AUTOMOUNT=$(ssh controlplane 'kubectl get pod isolated-agent -n ckad-w2d6 -o jsonpath="{.spec.automountServiceAccountToken}" 2>/dev/null || echo "true"')
TOKEN_CHECK=$(ssh controlplane 'kubectl exec isolated-agent -n ckad-w2d6 -- ls /var/run/secrets/kubernetes.io/serviceaccount 2>&1 || echo "NOT_FOUND"')

if [ "$PHASE" == "Running" ] && [ "$SA" == "build-deployer" ] && [ "$AUTOMOUNT" == "false" ] && [[ "$TOKEN_CHECK" =~ "NOT_FOUND" ]]; then
  echo -e "\033[0;32m[PASS] Pod isolated-agent assigned build-deployer with automountServiceAccountToken disabled.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: $PHASE, SA: $SA (expected build-deployer), Automount: $AUTOMOUNT (expected false).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: ServiceAccounts
```bash
ssh controlplane '
kubectl create serviceaccount build-deployer -n ckad-w2d6

cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: isolated-agent
  namespace: ckad-w2d6
spec:
  serviceAccountName: build-deployer
  automountServiceAccountToken: false
  containers:
  - name: agent
    image: busybox:1.36
    command: ["sleep", "3600"]
EOF_POD
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w2d6 --ignore-not-found'"""
    }
]
