"""
Dedicated CKA Lab Definitions for Week 4 (Days 1 to 6).
"""

WEEK_4_LABS = [
    {
        "day": 1,
        "date": '2026-10-19',
        "title": 'Commands & Arguments (Docker vs Kubernetes)',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Override Entrypoint with Command
In namespace `w4d1-cmd`, deploy a Pod named `custom-streamer` (image: `busybox:1.36`):
- Override the default entrypoint (`command`): `["/bin/sh", "-c"]`
- Override the arguments (`args`): `["while true; do echo STREAMING_EVENT; sleep 2; done"]`
- Verify the pod runs and streams `STREAMING_EVENT` to its standard output.

### Task 2: Interpolate Environment Variables into Arguments
Deploy a Pod named `env-interpolator` in namespace `w4d1-cmd` (image: `busybox:1.36`):
- Define an environment variable: `CLUSTER_ROLE=processor`
- Set `command`: `["/bin/sh", "-c"]`
- Set `args`: `["echo Initialized as $(CLUSTER_ROLE) && sleep 3600"]`
- Confirm that the container stdout shows `Initialized as processor`.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w4d1-cmd --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4d1-cmd
'""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: custom-streamer
LOGS_CS=$(ssh controlplane 'kubectl logs custom-streamer -n w4d1-cmd --tail=5 2>/dev/null || true')
PHASE_CS=$(ssh controlplane 'kubectl get pod custom-streamer -n w4d1-cmd -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PHASE_CS" == "Running" ] && echo "$LOGS_CS" | grep -q "STREAMING_EVENT"; then
  echo -e "${GREEN}[PASS] Task 1: custom-streamer is Running and streaming logs.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: custom-streamer status=$PHASE_CS or logs empty.${NC}"
fi

# Task 2: env-interpolator
LOGS_EI=$(ssh controlplane 'kubectl logs env-interpolator -n w4d1-cmd 2>/dev/null || true')
PHASE_EI=$(ssh controlplane 'kubectl get pod env-interpolator -n w4d1-cmd -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PHASE_EI" == "Running" ] && echo "$LOGS_EI" | grep -q "Initialized as processor"; then
  echo -e "${GREEN}[PASS] Task 2: env-interpolator is Running with interpolated variable.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: env-interpolator status=$PHASE_EI or logs missing 'Initialized as processor'.${NC}"
fi""",
        "solution": """1. Deploy `custom-streamer`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: custom-streamer
  namespace: w4d1-cmd
spec:
  containers:
  - name: streamer
    image: busybox:1.36
    command: ["/bin/sh", "-c"]
    args: ["while true; do echo STREAMING_EVENT; sleep 2; done"]
```
`kubectl apply -f streamer.yaml`

2. Deploy `env-interpolator`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: env-interpolator
  namespace: w4d1-cmd
spec:
  containers:
  - name: interpolator
    image: busybox:1.36
    env:
    - name: CLUSTER_ROLE
      value: "processor"
    command: ["/bin/sh", "-c"]
    args: ["echo Initialized as $(CLUSTER_ROLE) && sleep 3600"]
```
`kubectl apply -f interpolator.yaml`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w4d1-cmd --grace-period=0 --force 2>/dev/null || true
'""",
        "cka_title": 'Commands & Arguments (Docker vs Kubernetes)',
        "cka_diff": 'Medium',
        "cka_time": '30m',
        "cka_tasks": """### Task 1: Override Entrypoint with Command
In namespace `w4d1-cmd`, deploy a Pod named `custom-streamer` (image: `busybox:1.36`):
- Override the default entrypoint (`command`): `["/bin/sh", "-c"]`
- Override the arguments (`args`): `["while true; do echo STREAMING_EVENT; sleep 2; done"]`
- Verify the pod runs and streams `STREAMING_EVENT` to its standard output.

### Task 2: Interpolate Environment Variables into Arguments
Deploy a Pod named `env-interpolator` in namespace `w4d1-cmd` (image: `busybox:1.36`):
- Define an environment variable: `CLUSTER_ROLE=processor`
- Set `command`: `["/bin/sh", "-c"]`
- Set `args`: `["echo Initialized as $(CLUSTER_ROLE) && sleep 3600"]`
- Confirm that the container stdout shows `Initialized as processor`.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w4d1-cmd --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4d1-cmd
'""",
        "cka_verify": """SCORE=0; TOTAL=2
# Task 1: custom-streamer
LOGS_CS=$(ssh controlplane 'kubectl logs custom-streamer -n w4d1-cmd --tail=5 2>/dev/null || true')
PHASE_CS=$(ssh controlplane 'kubectl get pod custom-streamer -n w4d1-cmd -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PHASE_CS" == "Running" ] && echo "$LOGS_CS" | grep -q "STREAMING_EVENT"; then
  echo -e "${GREEN}[PASS] Task 1: custom-streamer is Running and streaming logs.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: custom-streamer status=$PHASE_CS or logs empty.${NC}"
fi

# Task 2: env-interpolator
LOGS_EI=$(ssh controlplane 'kubectl logs env-interpolator -n w4d1-cmd 2>/dev/null || true')
PHASE_EI=$(ssh controlplane 'kubectl get pod env-interpolator -n w4d1-cmd -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PHASE_EI" == "Running" ] && echo "$LOGS_EI" | grep -q "Initialized as processor"; then
  echo -e "${GREEN}[PASS] Task 2: env-interpolator is Running with interpolated variable.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: env-interpolator status=$PHASE_EI or logs missing 'Initialized as processor'.${NC}"
fi""",
        "cka_solution": """1. Deploy `custom-streamer`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: custom-streamer
  namespace: w4d1-cmd
spec:
  containers:
  - name: streamer
    image: busybox:1.36
    command: ["/bin/sh", "-c"]
    args: ["while true; do echo STREAMING_EVENT; sleep 2; done"]
```
`kubectl apply -f streamer.yaml`

2. Deploy `env-interpolator`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: env-interpolator
  namespace: w4d1-cmd
spec:
  containers:
  - name: interpolator
    image: busybox:1.36
    env:
    - name: CLUSTER_ROLE
      value: "processor"
    command: ["/bin/sh", "-c"]
    args: ["echo Initialized as $(CLUSTER_ROLE) && sleep 3600"]
```
`kubectl apply -f interpolator.yaml`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w4d1-cmd --grace-period=0 --force 2>/dev/null || true
'""",
    },
    {
        "day": 2,
        "date": '2026-10-20',
        "title": 'ConfigMaps & Application Configuration',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Create ConfigMaps
In namespace `w4d2-config`:
1. Create a ConfigMap named `backend-config` from literals:
   - `DB_HOST=postgres.internal`
   - `DB_PORT=5432`
2. Create a ConfigMap named `ui-settings` from file `/opt/k8s/settings.json`.

### Task 2: Consume ConfigMaps via envFrom and Volume Mount
Deploy a Pod named `portal-app` in namespace `w4d2-config` (image: `nginx:alpine`):
- Inject all keys from `backend-config` as environment variables using `envFrom`.
- Mount `ui-settings` as a volume at `/etc/portal/config/` (read-only).
- Verify the pod runs and the configuration file is present at `/etc/portal/config/settings.json`.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w4d2-config --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4d2-config
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  cat << "EOF" > /opt/k8s/settings.json
{
  "theme": "dark",
  "refreshInterval": 30
}
EOF
'""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: ConfigMaps
CM1=$(ssh controlplane 'kubectl get cm backend-config -n w4d2-config -o jsonpath="{.data.DB_HOST}" 2>/dev/null || echo "None"')
CM2=$(ssh controlplane 'kubectl get cm ui-settings -n w4d2-config -o jsonpath="{.data.settings\.json}" 2>/dev/null || echo "None"')
if [ "$CM1" == "postgres.internal" ] && [ "$CM2" != "None" ]; then
  echo -e "${GREEN}[PASS] Task 1: ConfigMaps backend-config and ui-settings created accurately.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: ConfigMaps missing or invalid (DB_HOST=$CM1).${NC}"
fi

# Task 2: portal-app envFrom and Volume Mount
P_ENV=$(ssh controlplane 'kubectl exec portal-app -n w4d2-config -- printenv DB_PORT 2>/dev/null || echo "None"')
P_FILE=$(ssh controlplane 'kubectl exec portal-app -n w4d2-config -- cat /etc/portal/config/settings.json 2>/dev/null || true')
if [ "$P_ENV" == "5432" ] && echo "$P_FILE" | grep -q "dark"; then
  echo -e "${GREEN}[PASS] Task 2: portal-app has DB_PORT env var and /etc/portal/config/settings.json mounted.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: env DB_PORT=$P_ENV or mounted file missing.${NC}"
fi""",
        "solution": """1. Create ConfigMaps:
`kubectl create cm backend-config -n w4d2-config --from-literal=DB_HOST=postgres.internal --from-literal=DB_PORT=5432`
`kubectl create cm ui-settings -n w4d2-config --from-file=settings.json=/opt/k8s/settings.json`

2. Deploy `portal-app`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: portal-app
  namespace: w4d2-config
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    envFrom:
    - configMapRef:
        name: backend-config
    volumeMounts:
    - name: ui-vol
      mountPath: /etc/portal/config
      readOnly: true
  volumes:
  - name: ui-vol
    configMap:
      name: ui-settings
```
`kubectl apply -f portal.yaml`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w4d2-config --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/settings.json
'""",
        "cka_title": 'ConfigMaps & Application Configuration',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Create ConfigMaps
In namespace `w4d2-config`:
1. Create a ConfigMap named `backend-config` from literals:
   - `DB_HOST=postgres.internal`
   - `DB_PORT=5432`
2. Create a ConfigMap named `ui-settings` from file `/opt/k8s/settings.json`.

### Task 2: Consume ConfigMaps via envFrom and Volume Mount
Deploy a Pod named `portal-app` in namespace `w4d2-config` (image: `nginx:alpine`):
- Inject all keys from `backend-config` as environment variables using `envFrom`.
- Mount `ui-settings` as a volume at `/etc/portal/config/` (read-only).
- Verify the pod runs and the configuration file is present at `/etc/portal/config/settings.json`.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w4d2-config --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4d2-config
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  cat << "EOF" > /opt/k8s/settings.json
{
  "theme": "dark",
  "refreshInterval": 30
}
EOF
'""",
        "cka_verify": """SCORE=0; TOTAL=2
# Task 1: ConfigMaps
CM1=$(ssh controlplane 'kubectl get cm backend-config -n w4d2-config -o jsonpath="{.data.DB_HOST}" 2>/dev/null || echo "None"')
CM2=$(ssh controlplane 'kubectl get cm ui-settings -n w4d2-config -o jsonpath="{.data.settings\.json}" 2>/dev/null || echo "None"')
if [ "$CM1" == "postgres.internal" ] && [ "$CM2" != "None" ]; then
  echo -e "${GREEN}[PASS] Task 1: ConfigMaps backend-config and ui-settings created accurately.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: ConfigMaps missing or invalid (DB_HOST=$CM1).${NC}"
fi

# Task 2: portal-app envFrom and Volume Mount
P_ENV=$(ssh controlplane 'kubectl exec portal-app -n w4d2-config -- printenv DB_PORT 2>/dev/null || echo "None"')
P_FILE=$(ssh controlplane 'kubectl exec portal-app -n w4d2-config -- cat /etc/portal/config/settings.json 2>/dev/null || true')
if [ "$P_ENV" == "5432" ] && echo "$P_FILE" | grep -q "dark"; then
  echo -e "${GREEN}[PASS] Task 2: portal-app has DB_PORT env var and /etc/portal/config/settings.json mounted.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: env DB_PORT=$P_ENV or mounted file missing.${NC}"
fi""",
        "cka_solution": """1. Create ConfigMaps:
`kubectl create cm backend-config -n w4d2-config --from-literal=DB_HOST=postgres.internal --from-literal=DB_PORT=5432`
`kubectl create cm ui-settings -n w4d2-config --from-file=settings.json=/opt/k8s/settings.json`

2. Deploy `portal-app`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: portal-app
  namespace: w4d2-config
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    envFrom:
    - configMapRef:
        name: backend-config
    volumeMounts:
    - name: ui-vol
      mountPath: /etc/portal/config
      readOnly: true
  volumes:
  - name: ui-vol
    configMap:
      name: ui-settings
```
`kubectl apply -f portal.yaml`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w4d2-config --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/settings.json
'""",
    },
    {
        "day": 3,
        "date": '2026-10-21',
        "title": 'Secrets Management & Encryption at Rest',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Generic Secret
In namespace `w4d3-secrets`, create a generic Secret named `db-credentials`:
- Key `username`: `dbadmin`
- Key `password`: `S3cur3P@ssw0rd!`

### Task 2: Mount Secret as Read-Only File Volume
Deploy a Pod named `vault-agent` in namespace `w4d3-secrets` (image: `nginx:alpine`):
- Mount the Secret `db-credentials` as a volume at `/etc/vault/secrets`
- Set `defaultMode: 256` (octal `0400` read-only for owner)
- Verify the pod runs and `/etc/vault/secrets/password` exists with the decrypted content.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w4d3-secrets --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4d3-secrets
'""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: Secret db-credentials
SEC_PASS=$(ssh controlplane 'kubectl get secret db-credentials -n w4d3-secrets -o jsonpath="{.data.password}" 2>/dev/null | base64 -d || echo "None"')
if [ "$SEC_PASS" == "S3cur3P@ssw0rd!" ]; then
  echo -e "${GREEN}[PASS] Task 1: Secret db-credentials verified with expected password.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Secret missing or password mismatch: $SEC_PASS.${NC}"
fi

# Task 2: vault-agent pod and mounted volume
PASS_FILE=$(ssh controlplane 'kubectl exec vault-agent -n w4d3-secrets -- cat /etc/vault/secrets/password 2>/dev/null || true')
PERM_MODE=$(ssh controlplane 'kubectl get pod vault-agent -n w4d3-secrets -o jsonpath="{.spec.volumes[0].secret.defaultMode}" 2>/dev/null || echo "0"')
if [ "$PASS_FILE" == "S3cur3P@ssw0rd!" ] && [ "$PERM_MODE" == "256" ]; then
  echo -e "${GREEN}[PASS] Task 2: Secret mounted at /etc/vault/secrets with defaultMode 256 (0400).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Mounted pass='$PASS_FILE' or defaultMode=$PERM_MODE (expected 256).${NC}"
fi""",
        "solution": """1. Create Secret:
`kubectl create secret generic db-credentials -n w4d3-secrets --from-literal=username=dbadmin --from-literal=password='S3cur3P@ssw0rd!'`

2. Deploy `vault-agent`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: vault-agent
  namespace: w4d3-secrets
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    volumeMounts:
    - name: sec-vol
      mountPath: /etc/vault/secrets
      readOnly: true
  volumes:
  - name: sec-vol
    secret:
      secretName: db-credentials
      defaultMode: 256
```
`kubectl apply -f vault-agent.yaml`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w4d3-secrets --grace-period=0 --force 2>/dev/null || true
'""",
        "cka_title": 'Secrets Management & Encryption at Rest',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Generic Secret
In namespace `w4d3-secrets`, create a generic Secret named `db-credentials`:
- Key `username`: `dbadmin`
- Key `password`: `S3cur3P@ssw0rd!`

### Task 2: Mount Secret as Read-Only File Volume
Deploy a Pod named `vault-agent` in namespace `w4d3-secrets` (image: `nginx:alpine`):
- Mount the Secret `db-credentials` as a volume at `/etc/vault/secrets`
- Set `defaultMode: 256` (octal `0400` read-only for owner)
- Verify the pod runs and `/etc/vault/secrets/password` exists with the decrypted content.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w4d3-secrets --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4d3-secrets
'""",
        "cka_verify": """SCORE=0; TOTAL=2
# Task 1: Secret db-credentials
SEC_PASS=$(ssh controlplane 'kubectl get secret db-credentials -n w4d3-secrets -o jsonpath="{.data.password}" 2>/dev/null | base64 -d || echo "None"')
if [ "$SEC_PASS" == "S3cur3P@ssw0rd!" ]; then
  echo -e "${GREEN}[PASS] Task 1: Secret db-credentials verified with expected password.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Secret missing or password mismatch: $SEC_PASS.${NC}"
fi

# Task 2: vault-agent pod and mounted volume
PASS_FILE=$(ssh controlplane 'kubectl exec vault-agent -n w4d3-secrets -- cat /etc/vault/secrets/password 2>/dev/null || true')
PERM_MODE=$(ssh controlplane 'kubectl get pod vault-agent -n w4d3-secrets -o jsonpath="{.spec.volumes[0].secret.defaultMode}" 2>/dev/null || echo "0"')
if [ "$PASS_FILE" == "S3cur3P@ssw0rd!" ] && [ "$PERM_MODE" == "256" ]; then
  echo -e "${GREEN}[PASS] Task 2: Secret mounted at /etc/vault/secrets with defaultMode 256 (0400).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Mounted pass='$PASS_FILE' or defaultMode=$PERM_MODE (expected 256).${NC}"
fi""",
        "cka_solution": """1. Create Secret:
`kubectl create secret generic db-credentials -n w4d3-secrets --from-literal=username=dbadmin --from-literal=password='S3cur3P@ssw0rd!'`

2. Deploy `vault-agent`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: vault-agent
  namespace: w4d3-secrets
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    volumeMounts:
    - name: sec-vol
      mountPath: /etc/vault/secrets
      readOnly: true
  volumes:
  - name: sec-vol
    secret:
      secretName: db-credentials
      defaultMode: 256
```
`kubectl apply -f vault-agent.yaml`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w4d3-secrets --grace-period=0 --force 2>/dev/null || true
'""",
    },
    {
        "day": 4,
        "date": '2026-10-22',
        "title": 'Autoscaling: HPA, VPA & In-Place Pod Resize',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Deploy Workload with Resource Requests
In namespace `w4d4-scale`, create a Deployment named `order-backend`:
- Replicas: `2`
- Image: `nginx:alpine`
- Container resource requests: `cpu: 50m`, `memory: 64Mi`
- Container resource limits: `cpu: 200m`, `memory: 128Mi`

### Task 2: Configure HorizontalPodAutoscaler (HPA)
Create an HPA named `order-backend-hpa` in namespace `w4d4-scale` targeting `deployment/order-backend`:
- Min replicas: `2`
- Max replicas: `6`
- Target CPU utilization percentage: `50%`
- Verify that `kubectl get hpa -n w4d4-scale` shows the target and minimum/maximum replicas.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w4d4-scale --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4d4-scale
'""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: Deployment order-backend
DEP_REQS=$(ssh controlplane 'kubectl get deploy order-backend -n w4d4-scale -o jsonpath="{.spec.template.spec.containers[0].resources.requests.cpu}" 2>/dev/null || echo "None"')
DEP_REP=$(ssh controlplane 'kubectl get deploy order-backend -n w4d4-scale -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$DEP_REQS" == "50m" ] && [ "$DEP_REP" -ge 2 ]; then
  echo -e "${GREEN}[PASS] Task 1: Deployment order-backend running with 50m CPU requests.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: order-backend cpu requests=$DEP_REQS, readyReplicas=$DEP_REP.${NC}"
fi

# Task 2: HPA
HPA_MAX=$(ssh controlplane 'kubectl get hpa order-backend-hpa -n w4d4-scale -o jsonpath="{.spec.maxReplicas}" 2>/dev/null || echo "0"')
HPA_MIN=$(ssh controlplane 'kubectl get hpa order-backend-hpa -n w4d4-scale -o jsonpath="{.spec.minReplicas}" 2>/dev/null || echo "0"')
HPA_TARGET=$(ssh controlplane 'kubectl get hpa order-backend-hpa -n w4d4-scale -o jsonpath="{.spec.scaleTargetRef.name}" 2>/dev/null || echo "None"')
if [ "$HPA_MAX" == "6" ] && [ "$HPA_MIN" == "2" ] && [ "$HPA_TARGET" == "order-backend" ]; then
  echo -e "${GREEN}[PASS] Task 2: order-backend-hpa configured with min=2, max=6 targeting order-backend.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: HPA target=$HPA_TARGET, min=$HPA_MIN, max=$HPA_MAX.${NC}"
fi""",
        "solution": """1. Create deployment:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-backend
  namespace: w4d4-scale
spec:
  replicas: 2
  selector:
    matchLabels:
      app: order-backend
  template:
    metadata:
      labels:
        app: order-backend
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        resources:
          requests:
            cpu: 50m
            memory: 64Mi
          limits:
            cpu: 200m
            memory: 128Mi
```
`kubectl apply -f order-backend.yaml`

2. Create HPA:
`kubectl autoscale deployment order-backend -n w4d4-scale --cpu-percent=50 --min=2 --max=6 --name=order-backend-hpa`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w4d4-scale --grace-period=0 --force 2>/dev/null || true
'""",
        "cka_title": 'Autoscaling: HPA, VPA & In-Place Pod Resize',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Deploy Workload with Resource Requests
In namespace `w4d4-scale`, create a Deployment named `order-backend`:
- Replicas: `2`
- Image: `nginx:alpine`
- Container resource requests: `cpu: 50m`, `memory: 64Mi`
- Container resource limits: `cpu: 200m`, `memory: 128Mi`

### Task 2: Configure HorizontalPodAutoscaler (HPA)
Create an HPA named `order-backend-hpa` in namespace `w4d4-scale` targeting `deployment/order-backend`:
- Min replicas: `2`
- Max replicas: `6`
- Target CPU utilization percentage: `50%`
- Verify that `kubectl get hpa -n w4d4-scale` shows the target and minimum/maximum replicas.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w4d4-scale --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4d4-scale
'""",
        "cka_verify": """SCORE=0; TOTAL=2
# Task 1: Deployment order-backend
DEP_REQS=$(ssh controlplane 'kubectl get deploy order-backend -n w4d4-scale -o jsonpath="{.spec.template.spec.containers[0].resources.requests.cpu}" 2>/dev/null || echo "None"')
DEP_REP=$(ssh controlplane 'kubectl get deploy order-backend -n w4d4-scale -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$DEP_REQS" == "50m" ] && [ "$DEP_REP" -ge 2 ]; then
  echo -e "${GREEN}[PASS] Task 1: Deployment order-backend running with 50m CPU requests.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: order-backend cpu requests=$DEP_REQS, readyReplicas=$DEP_REP.${NC}"
fi

# Task 2: HPA
HPA_MAX=$(ssh controlplane 'kubectl get hpa order-backend-hpa -n w4d4-scale -o jsonpath="{.spec.maxReplicas}" 2>/dev/null || echo "0"')
HPA_MIN=$(ssh controlplane 'kubectl get hpa order-backend-hpa -n w4d4-scale -o jsonpath="{.spec.minReplicas}" 2>/dev/null || echo "0"')
HPA_TARGET=$(ssh controlplane 'kubectl get hpa order-backend-hpa -n w4d4-scale -o jsonpath="{.spec.scaleTargetRef.name}" 2>/dev/null || echo "None"')
if [ "$HPA_MAX" == "6" ] && [ "$HPA_MIN" == "2" ] && [ "$HPA_TARGET" == "order-backend" ]; then
  echo -e "${GREEN}[PASS] Task 2: order-backend-hpa configured with min=2, max=6 targeting order-backend.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: HPA target=$HPA_TARGET, min=$HPA_MIN, max=$HPA_MAX.${NC}"
fi""",
        "cka_solution": """1. Create deployment:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-backend
  namespace: w4d4-scale
spec:
  replicas: 2
  selector:
    matchLabels:
      app: order-backend
  template:
    metadata:
      labels:
        app: order-backend
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        resources:
          requests:
            cpu: 50m
            memory: 64Mi
          limits:
            cpu: 200m
            memory: 128Mi
```
`kubectl apply -f order-backend.yaml`

2. Create HPA:
`kubectl autoscale deployment order-backend -n w4d4-scale --cpu-percent=50 --min=2 --max=6 --name=order-backend-hpa`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w4d4-scale --grace-period=0 --force 2>/dev/null || true
'""",
    },
    {
        "day": 5,
        "date": '2026-10-23',
        "title": 'Admission Controllers & Validating Webhooks',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Audit Enabled Admission Plugins
Query the `kube-apiserver` static pod manifest on `controlplane` to inspect active admission plugins:
1. Extract the `--enable-admission-plugins` configuration flag.
2. Save the comma-separated list of enabled admission plugins to `/opt/k8s/enabled_admission_plugins.txt`.

### Task 2: Test NamespaceLifecycle Admission Controller
Verify that the `NamespaceLifecycle` admission controller actively rejects pod creation in a non-existent namespace:
- Run a test command attempting to create pod `ghost-pod` in non-existent namespace `void-ns` and save stderr output to `/opt/k8s/admission_rejection.log`.""",
        "setup": """ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/enabled_admission_plugins.txt /opt/k8s/admission_rejection.log
'""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: enabled_admission_plugins.txt
PLUGINS=$(ssh controlplane 'cat /opt/k8s/enabled_admission_plugins.txt 2>/dev/null || true')
if [ -n "$PLUGINS" ] && echo "$PLUGINS" | grep -qiE "NodeRestriction|NamespaceLifecycle|LimitRanger"; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/enabled_admission_plugins.txt contains active admission plugins.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/enabled_admission_plugins.txt missing or lacks recognized plugins.${NC}"
fi

# Task 2: admission_rejection.log
REJECT=$(ssh controlplane 'cat /opt/k8s/admission_rejection.log 2>/dev/null || true')
if echo "$REJECT" | grep -qiE "NotFound|not found|namespaces.*void-ns"; then
  echo -e "${GREEN}[PASS] Task 2: NamespaceLifecycle admission rejection logged.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/admission_rejection.log missing or did not capture rejection.${NC}"
fi""",
        "solution": """1. Extract admission plugins:
`grep -oE -- '--enable-admission-plugins=[^ ]*' /etc/kubernetes/manifests/kube-apiserver.yaml | cut -d'=' -f2 | sudo tee /opt/k8s/enabled_admission_plugins.txt`

2. Capture rejection:
`kubectl run ghost-pod -n void-ns --image=nginx:alpine 2> /opt/k8s/admission_rejection.log || true`""",
        "reset": "ssh controlplane 'rm -f /opt/k8s/enabled_admission_plugins.txt /opt/k8s/admission_rejection.log'",
        "cka_title": 'Admission Controllers & Validating Webhooks',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Audit Enabled Admission Plugins
Query the `kube-apiserver` static pod manifest on `controlplane` to inspect active admission plugins:
1. Extract the `--enable-admission-plugins` configuration flag.
2. Save the comma-separated list of enabled admission plugins to `/opt/k8s/enabled_admission_plugins.txt`.

### Task 2: Test NamespaceLifecycle Admission Controller
Verify that the `NamespaceLifecycle` admission controller actively rejects pod creation in a non-existent namespace:
- Run a test command attempting to create pod `ghost-pod` in non-existent namespace `void-ns` and save stderr output to `/opt/k8s/admission_rejection.log`.""",
        "cka_setup": """ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/enabled_admission_plugins.txt /opt/k8s/admission_rejection.log
'""",
        "cka_verify": """SCORE=0; TOTAL=2
# Task 1: enabled_admission_plugins.txt
PLUGINS=$(ssh controlplane 'cat /opt/k8s/enabled_admission_plugins.txt 2>/dev/null || true')
if [ -n "$PLUGINS" ] && echo "$PLUGINS" | grep -qiE "NodeRestriction|NamespaceLifecycle|LimitRanger"; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/enabled_admission_plugins.txt contains active admission plugins.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/enabled_admission_plugins.txt missing or lacks recognized plugins.${NC}"
fi

# Task 2: admission_rejection.log
REJECT=$(ssh controlplane 'cat /opt/k8s/admission_rejection.log 2>/dev/null || true')
if echo "$REJECT" | grep -qiE "NotFound|not found|namespaces.*void-ns"; then
  echo -e "${GREEN}[PASS] Task 2: NamespaceLifecycle admission rejection logged.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/admission_rejection.log missing or did not capture rejection.${NC}"
fi""",
        "cka_solution": """1. Extract admission plugins:
`grep -oE -- '--enable-admission-plugins=[^ ]*' /etc/kubernetes/manifests/kube-apiserver.yaml | cut -d'=' -f2 | sudo tee /opt/k8s/enabled_admission_plugins.txt`

2. Capture rejection:
`kubectl run ghost-pod -n void-ns --image=nginx:alpine 2> /opt/k8s/admission_rejection.log || true`""",
        "cka_reset": "ssh controlplane 'rm -f /opt/k8s/enabled_admission_plugins.txt /opt/k8s/admission_rejection.log'",
    },
    {
        "day": 6,
        "date": '2026-10-24',
        "title": 'Week 4 App Lifecycle & Secret Security Drill',
        "diff": 'Hard (Milestone Assessment 4)',
        "time": '45m',
        "tasks": """### Milestone 4 Triathlon Tasks:
In namespace `w4-milestone`:
1. **ConfigMap & Secret Injection**:
   Create a ConfigMap `app-settings` with `APP_MODE=production`.
   Create a Secret `app-auth` with `API_KEY=Alpha99SecretToken`.
   Deploy a deployment `secure-frontend` (2 replicas, image `nginx:alpine`):
   - Inject `APP_MODE` as an env var from ConfigMap `app-settings`.
   - Inject `API_KEY` as an env var from Secret `app-auth`.
   - Set container resource requests: `cpu: 30m`, `memory: 64Mi`.

2. **Horizontal Pod Autoscaling**:
   Configure an HPA named `secure-frontend-hpa` targeting `secure-frontend`:
   - Min replicas: `2`, Max replicas: `5`, Target CPU: `60%`.

3. **Secret File Volume**:
   Mount Secret `app-auth` inside the container as a file at `/etc/auth/token` (read-only, defaultMode: `0400`).""",
        "setup": """ssh controlplane '
  kubectl delete namespace w4-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4-milestone
'""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: secure-frontend deployment env vars
POD_NAME=$(ssh controlplane 'kubectl get pods -n w4-milestone -l app=secure-frontend -o jsonpath="{.items[0].metadata.name}" 2>/dev/null || echo "None"')
APP_MODE=$(ssh controlplane "kubectl exec $POD_NAME -n w4-milestone -- printenv APP_MODE 2>/dev/null || echo 'None'")
API_KEY=$(ssh controlplane "kubectl exec $POD_NAME -n w4-milestone -- printenv API_KEY 2>/dev/null || echo 'None'")
if [ "$APP_MODE" == "production" ] && [ "$API_KEY" == "Alpha99SecretToken" ]; then
  echo -e "${GREEN}[PASS] Task 1: Environment variables APP_MODE and API_KEY injected into workload.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Environment variables missing (APP_MODE=$APP_MODE, API_KEY=$API_KEY).${NC}"
fi

# Task 2: HPA
HPA_MAX=$(ssh controlplane 'kubectl get hpa secure-frontend-hpa -n w4-milestone -o jsonpath="{.spec.maxReplicas}" 2>/dev/null || echo "0"')
if [ "$HPA_MAX" == "5" ]; then
  echo -e "${GREEN}[PASS] Task 2: secure-frontend-hpa configured with max 5 replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: secure-frontend-hpa max replicas is $HPA_MAX (expected 5).${NC}"
fi

# Task 3: Volume mounted secret at /etc/auth/token
SECRET_CONTENT=$(ssh controlplane "kubectl exec $POD_NAME -n w4-milestone -- cat /etc/auth/token/API_KEY 2>/dev/null || true")
if [ "$SECRET_CONTENT" == "Alpha99SecretToken" ]; then
  echo -e "${GREEN}[PASS] Task 3: Secret mounted successfully at /etc/auth/token.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Secret file missing at /etc/auth/token.${NC}"
fi""",
        "solution": """1. Create ConfigMap and Secret:
`kubectl create cm app-settings -n w4-milestone --from-literal=APP_MODE=production`
`kubectl create secret generic app-auth -n w4-milestone --from-literal=API_KEY=Alpha99SecretToken`

2. Deploy `secure-frontend`:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secure-frontend
  namespace: w4-milestone
spec:
  replicas: 2
  selector:
    matchLabels:
      app: secure-frontend
  template:
    metadata:
      labels:
        app: secure-frontend
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        env:
        - name: APP_MODE
          valueFrom:
            configMapKeyRef:
              name: app-settings
              key: APP_MODE
        - name: API_KEY
          valueFrom:
            secretKeyRef:
              name: app-auth
              key: API_KEY
        resources:
          requests:
            cpu: 30m
            memory: 64Mi
        volumeMounts:
        - name: secret-vol
          mountPath: /etc/auth/token
          readOnly: true
      volumes:
      - name: secret-vol
        secret:
          secretName: app-auth
          defaultMode: 256
```
`kubectl apply -f deployment.yaml`

3. Create HPA:
`kubectl autoscale deployment secure-frontend -n w4-milestone --cpu-percent=60 --min=2 --max=5 --name=secure-frontend-hpa`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w4-milestone --grace-period=0 --force 2>/dev/null || true
'""",
        "cka_title": 'Week 4 App Lifecycle & Secret Security Drill',
        "cka_diff": 'Hard (Milestone Assessment 4)',
        "cka_time": '45m',
        "cka_tasks": """### Milestone 4 Triathlon Tasks:
In namespace `w4-milestone`:
1. **ConfigMap & Secret Injection**:
   Create a ConfigMap `app-settings` with `APP_MODE=production`.
   Create a Secret `app-auth` with `API_KEY=Alpha99SecretToken`.
   Deploy a deployment `secure-frontend` (2 replicas, image `nginx:alpine`):
   - Inject `APP_MODE` as an env var from ConfigMap `app-settings`.
   - Inject `API_KEY` as an env var from Secret `app-auth`.
   - Set container resource requests: `cpu: 30m`, `memory: 64Mi`.

2. **Horizontal Pod Autoscaling**:
   Configure an HPA named `secure-frontend-hpa` targeting `secure-frontend`:
   - Min replicas: `2`, Max replicas: `5`, Target CPU: `60%`.

3. **Secret File Volume**:
   Mount Secret `app-auth` inside the container as a file at `/etc/auth/token` (read-only, defaultMode: `0400`).""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w4-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w4-milestone
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: secure-frontend deployment env vars
POD_NAME=$(ssh controlplane 'kubectl get pods -n w4-milestone -l app=secure-frontend -o jsonpath="{.items[0].metadata.name}" 2>/dev/null || echo "None"')
APP_MODE=$(ssh controlplane "kubectl exec $POD_NAME -n w4-milestone -- printenv APP_MODE 2>/dev/null || echo 'None'")
API_KEY=$(ssh controlplane "kubectl exec $POD_NAME -n w4-milestone -- printenv API_KEY 2>/dev/null || echo 'None'")
if [ "$APP_MODE" == "production" ] && [ "$API_KEY" == "Alpha99SecretToken" ]; then
  echo -e "${GREEN}[PASS] Task 1: Environment variables APP_MODE and API_KEY injected into workload.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Environment variables missing (APP_MODE=$APP_MODE, API_KEY=$API_KEY).${NC}"
fi

# Task 2: HPA
HPA_MAX=$(ssh controlplane 'kubectl get hpa secure-frontend-hpa -n w4-milestone -o jsonpath="{.spec.maxReplicas}" 2>/dev/null || echo "0"')
if [ "$HPA_MAX" == "5" ]; then
  echo -e "${GREEN}[PASS] Task 2: secure-frontend-hpa configured with max 5 replicas.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: secure-frontend-hpa max replicas is $HPA_MAX (expected 5).${NC}"
fi

# Task 3: Volume mounted secret at /etc/auth/token
SECRET_CONTENT=$(ssh controlplane "kubectl exec $POD_NAME -n w4-milestone -- cat /etc/auth/token/API_KEY 2>/dev/null || true")
if [ "$SECRET_CONTENT" == "Alpha99SecretToken" ]; then
  echo -e "${GREEN}[PASS] Task 3: Secret mounted successfully at /etc/auth/token.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Secret file missing at /etc/auth/token.${NC}"
fi""",
        "cka_solution": """1. Create ConfigMap and Secret:
`kubectl create cm app-settings -n w4-milestone --from-literal=APP_MODE=production`
`kubectl create secret generic app-auth -n w4-milestone --from-literal=API_KEY=Alpha99SecretToken`

2. Deploy `secure-frontend`:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secure-frontend
  namespace: w4-milestone
spec:
  replicas: 2
  selector:
    matchLabels:
      app: secure-frontend
  template:
    metadata:
      labels:
        app: secure-frontend
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        env:
        - name: APP_MODE
          valueFrom:
            configMapKeyRef:
              name: app-settings
              key: APP_MODE
        - name: API_KEY
          valueFrom:
            secretKeyRef:
              name: app-auth
              key: API_KEY
        resources:
          requests:
            cpu: 30m
            memory: 64Mi
        volumeMounts:
        - name: secret-vol
          mountPath: /etc/auth/token
          readOnly: true
      volumes:
      - name: secret-vol
        secret:
          secretName: app-auth
          defaultMode: 256
```
`kubectl apply -f deployment.yaml`

3. Create HPA:
`kubectl autoscale deployment secure-frontend -n w4-milestone --cpu-percent=60 --min=2 --max=5 --name=secure-frontend-hpa`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w4-milestone --grace-period=0 --force 2>/dev/null || true
'""",
    },
]
