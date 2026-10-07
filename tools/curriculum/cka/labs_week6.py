"""
Dedicated CKA Lab Definitions for Week 6 (Days 1 to 6).
"""

WEEK_6_LABS = [
    {
        "day": 1,
        "date": '2026-11-02',
        "title": 'Certificates API & KubeConfig Management',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: CertificateSigningRequest (CSR)
On `controlplane`, a certificate request file has been prepared at `/opt/k8s/developer-bob.csr`.
1. Create a Kubernetes `CertificateSigningRequest` named `developer-bob-csr`:
   - `signerName`: `kubernetes.io/kube-apiserver-client`
   - `request`: base64-encoded contents of `/opt/k8s/developer-bob.csr`
   - `usages`: `client auth`

### Task 2: Approve CSR & Export Certificate
1. Approve the request using `kubectl certificate approve developer-bob-csr`.
2. Extract the approved certificate to `/opt/k8s/developer-bob.crt`.

### Task 3: Kubeconfig Configuration
Configure a new user in `/opt/k8s/bob.kubeconfig`:
- Set credentials for `developer-bob` using client certificate `/opt/k8s/developer-bob.crt` and client key `/opt/k8s/developer-bob.key`.""",
        "setup": """ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  cd /opt/k8s
  openssl genrsa -out developer-bob.key 2048 2>/dev/null
  openssl req -new -key developer-bob.key -out developer-bob.csr -subj "/CN=developer-bob/O=developers" 2>/dev/null
  kubectl delete csr developer-bob-csr 2>/dev/null || true
  rm -f developer-bob.crt bob.kubeconfig
'""",
        "verify": """SCORE=0; TOTAL=3
# Task 1 & 2: CSR approved and certificate extracted
CSR_STAT=$(ssh controlplane 'kubectl get csr developer-bob-csr -o jsonpath="{.status.conditions[0].type}" 2>/dev/null || echo "None"')
CRT_EXISTS=$(ssh controlplane 'test -s /opt/k8s/developer-bob.crt && echo "yes" || echo "no"')

if [ "$CSR_STAT" == "Approved" ]; then
  echo -e "${GREEN}[PASS] Task 1: CertificateSigningRequest developer-bob-csr approved.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: developer-bob-csr status is $CSR_STAT (expected Approved).${NC}"
fi

if [ "$CRT_EXISTS" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 2: Certificate exported to /opt/k8s/developer-bob.crt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/developer-bob.crt missing or empty.${NC}"
fi

# Task 3: bob.kubeconfig has developer-bob user
if ssh controlplane 'test -f /opt/k8s/bob.kubeconfig && grep -q "developer-bob" /opt/k8s/bob.kubeconfig'; then
  echo -e "${GREEN}[PASS] Task 3: /opt/k8s/bob.kubeconfig configured with developer-bob.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /opt/k8s/bob.kubeconfig missing or does not reference developer-bob.${NC}"
fi""",
        "solution": """1. Create and apply CSR YAML:
```bash
B64_CSR=$(cat /opt/k8s/developer-bob.csr | base64 | tr -d '
')
cat << EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: developer-bob-csr
spec:
  request: $B64_CSR
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
EOF
```

2. Approve and extract:
`kubectl certificate approve developer-bob-csr`
`kubectl get csr developer-bob-csr -o jsonpath='{.status.certificate}' | base64 -d > /opt/k8s/developer-bob.crt`

3. Configure kubeconfig:
`kubectl config set-credentials developer-bob --client-certificate=/opt/k8s/developer-bob.crt --client-key=/opt/k8s/developer-bob.key --kubeconfig=/opt/k8s/bob.kubeconfig`""",
        "reset": """ssh controlplane '
  kubectl delete csr developer-bob-csr 2>/dev/null || true
  rm -rf /opt/k8s/developer-bob.* /opt/k8s/bob.kubeconfig
'""",
        "cka_title": 'Certificates API & KubeConfig Management',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: CertificateSigningRequest (CSR)
On `controlplane`, a certificate request file has been prepared at `/opt/k8s/developer-bob.csr`.
1. Create a Kubernetes `CertificateSigningRequest` named `developer-bob-csr`:
   - `signerName`: `kubernetes.io/kube-apiserver-client`
   - `request`: base64-encoded contents of `/opt/k8s/developer-bob.csr`
   - `usages`: `client auth`

### Task 2: Approve CSR & Export Certificate
1. Approve the request using `kubectl certificate approve developer-bob-csr`.
2. Extract the approved certificate to `/opt/k8s/developer-bob.crt`.

### Task 3: Kubeconfig Configuration
Configure a new user in `/opt/k8s/bob.kubeconfig`:
- Set credentials for `developer-bob` using client certificate `/opt/k8s/developer-bob.crt` and client key `/opt/k8s/developer-bob.key`.""",
        "cka_setup": """ssh controlplane '
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  cd /opt/k8s
  openssl genrsa -out developer-bob.key 2048 2>/dev/null
  openssl req -new -key developer-bob.key -out developer-bob.csr -subj "/CN=developer-bob/O=developers" 2>/dev/null
  kubectl delete csr developer-bob-csr 2>/dev/null || true
  rm -f developer-bob.crt bob.kubeconfig
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1 & 2: CSR approved and certificate extracted
CSR_STAT=$(ssh controlplane 'kubectl get csr developer-bob-csr -o jsonpath="{.status.conditions[0].type}" 2>/dev/null || echo "None"')
CRT_EXISTS=$(ssh controlplane 'test -s /opt/k8s/developer-bob.crt && echo "yes" || echo "no"')

if [ "$CSR_STAT" == "Approved" ]; then
  echo -e "${GREEN}[PASS] Task 1: CertificateSigningRequest developer-bob-csr approved.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: developer-bob-csr status is $CSR_STAT (expected Approved).${NC}"
fi

if [ "$CRT_EXISTS" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 2: Certificate exported to /opt/k8s/developer-bob.crt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /opt/k8s/developer-bob.crt missing or empty.${NC}"
fi

# Task 3: bob.kubeconfig has developer-bob user
if ssh controlplane 'test -f /opt/k8s/bob.kubeconfig && grep -q "developer-bob" /opt/k8s/bob.kubeconfig'; then
  echo -e "${GREEN}[PASS] Task 3: /opt/k8s/bob.kubeconfig configured with developer-bob.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /opt/k8s/bob.kubeconfig missing or does not reference developer-bob.${NC}"
fi""",
        "cka_solution": """1. Create and apply CSR YAML:
```bash
B64_CSR=$(cat /opt/k8s/developer-bob.csr | base64 | tr -d '
')
cat << EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: developer-bob-csr
spec:
  request: $B64_CSR
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
EOF
```

2. Approve and extract:
`kubectl certificate approve developer-bob-csr`
`kubectl get csr developer-bob-csr -o jsonpath='{.status.certificate}' | base64 -d > /opt/k8s/developer-bob.crt`

3. Configure kubeconfig:
`kubectl config set-credentials developer-bob --client-certificate=/opt/k8s/developer-bob.crt --client-key=/opt/k8s/developer-bob.key --kubeconfig=/opt/k8s/bob.kubeconfig`""",
        "cka_reset": """ssh controlplane '
  kubectl delete csr developer-bob-csr 2>/dev/null || true
  rm -rf /opt/k8s/developer-bob.* /opt/k8s/bob.kubeconfig
'""",
    },
    {
        "day": 2,
        "date": '2026-11-03',
        "title": 'RBAC (Roles, RoleBindings & ClusterRoles)',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Namespace Role & RoleBinding
In namespace `w6d2-rbac`:
1. Create a `Role` named `pod-operator` granting `get, list, watch, create, delete` permissions on `pods`.
2. Create a `RoleBinding` named `bind-pod-operator` binding `pod-operator` to ServiceAccount `dev-sa`.

### Task 2: ClusterRole & ClusterRoleBinding
1. Create a `ClusterRole` named `node-observer` granting `get, list, watch` permissions on `nodes`.
2. Create a `ClusterRoleBinding` named `bind-node-observer` binding `node-observer` to ServiceAccount `dev-sa` in namespace `w6d2-rbac`.

### Task 3: RBAC Authorization Verification
Verify authorization using `kubectl auth can-i`:
- Check if `dev-sa` in `w6d2-rbac` can list pods in `w6d2-rbac` (must be `yes`).
- Check if `dev-sa` in `w6d2-rbac` can list nodes cluster-wide (must be `yes`).""",
        "setup": """ssh controlplane '
  kubectl delete namespace w6d2-rbac --grace-period=0 --force 2>/dev/null || true
  kubectl delete clusterrole node-observer 2>/dev/null || true
  kubectl delete clusterrolebinding bind-node-observer 2>/dev/null || true
  kubectl create namespace w6d2-rbac
  kubectl create sa dev-sa -n w6d2-rbac
'""",
        "verify": """SCORE=0; TOTAL=2
# Task 1 & 3: Role and auth check
CAN_PODS=$(ssh controlplane 'kubectl auth can-i list pods -n w6d2-rbac --as=system:serviceaccount:w6d2-rbac:dev-sa 2>/dev/null || echo "no"')
if [ "$CAN_PODS" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 1: ServiceAccount dev-sa authorized to list pods in w6d2-rbac.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: dev-sa cannot list pods in w6d2-rbac.${NC}"
fi

# Task 2 & 3: ClusterRole and auth check
CAN_NODES=$(ssh controlplane 'kubectl auth can-i list nodes --as=system:serviceaccount:w6d2-rbac:dev-sa 2>/dev/null || echo "no"')
if [ "$CAN_NODES" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 2: ServiceAccount dev-sa authorized to list nodes cluster-wide.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: dev-sa cannot list nodes cluster-wide.${NC}"
fi""",
        "solution": """1. Role & RoleBinding:
`kubectl create role pod-operator -n w6d2-rbac --verb=get,list,watch,create,delete --resource=pods`
`kubectl create rolebinding bind-pod-operator -n w6d2-rbac --role=pod-operator --serviceaccount=w6d2-rbac:dev-sa`

2. ClusterRole & ClusterRoleBinding:
`kubectl create clusterrole node-observer --verb=get,list,watch --resource=nodes`
`kubectl create clusterrolebinding bind-node-observer --clusterrole=node-observer --serviceaccount=w6d2-rbac:dev-sa`

3. Verify:
`kubectl auth can-i list pods -n w6d2-rbac --as=system:serviceaccount:w6d2-rbac:dev-sa`
`kubectl auth can-i list nodes --as=system:serviceaccount:w6d2-rbac:dev-sa`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w6d2-rbac --grace-period=0 --force 2>/dev/null || true
  kubectl delete clusterrole node-observer 2>/dev/null || true
  kubectl delete clusterrolebinding bind-node-observer 2>/dev/null || true
'""",
        "cka_title": 'RBAC (Roles, RoleBindings & ClusterRoles)',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Namespace Role & RoleBinding
In namespace `w6d2-rbac`:
1. Create a `Role` named `pod-operator` granting `get, list, watch, create, delete` permissions on `pods`.
2. Create a `RoleBinding` named `bind-pod-operator` binding `pod-operator` to ServiceAccount `dev-sa`.

### Task 2: ClusterRole & ClusterRoleBinding
1. Create a `ClusterRole` named `node-observer` granting `get, list, watch` permissions on `nodes`.
2. Create a `ClusterRoleBinding` named `bind-node-observer` binding `node-observer` to ServiceAccount `dev-sa` in namespace `w6d2-rbac`.

### Task 3: RBAC Authorization Verification
Verify authorization using `kubectl auth can-i`:
- Check if `dev-sa` in `w6d2-rbac` can list pods in `w6d2-rbac` (must be `yes`).
- Check if `dev-sa` in `w6d2-rbac` can list nodes cluster-wide (must be `yes`).""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w6d2-rbac --grace-period=0 --force 2>/dev/null || true
  kubectl delete clusterrole node-observer 2>/dev/null || true
  kubectl delete clusterrolebinding bind-node-observer 2>/dev/null || true
  kubectl create namespace w6d2-rbac
  kubectl create sa dev-sa -n w6d2-rbac
'""",
        "cka_verify": """SCORE=0; TOTAL=2
# Task 1 & 3: Role and auth check
CAN_PODS=$(ssh controlplane 'kubectl auth can-i list pods -n w6d2-rbac --as=system:serviceaccount:w6d2-rbac:dev-sa 2>/dev/null || echo "no"')
if [ "$CAN_PODS" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 1: ServiceAccount dev-sa authorized to list pods in w6d2-rbac.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: dev-sa cannot list pods in w6d2-rbac.${NC}"
fi

# Task 2 & 3: ClusterRole and auth check
CAN_NODES=$(ssh controlplane 'kubectl auth can-i list nodes --as=system:serviceaccount:w6d2-rbac:dev-sa 2>/dev/null || echo "no"')
if [ "$CAN_NODES" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 2: ServiceAccount dev-sa authorized to list nodes cluster-wide.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: dev-sa cannot list nodes cluster-wide.${NC}"
fi""",
        "cka_solution": """1. Role & RoleBinding:
`kubectl create role pod-operator -n w6d2-rbac --verb=get,list,watch,create,delete --resource=pods`
`kubectl create rolebinding bind-pod-operator -n w6d2-rbac --role=pod-operator --serviceaccount=w6d2-rbac:dev-sa`

2. ClusterRole & ClusterRoleBinding:
`kubectl create clusterrole node-observer --verb=get,list,watch --resource=nodes`
`kubectl create clusterrolebinding bind-node-observer --clusterrole=node-observer --serviceaccount=w6d2-rbac:dev-sa`

3. Verify:
`kubectl auth can-i list pods -n w6d2-rbac --as=system:serviceaccount:w6d2-rbac:dev-sa`
`kubectl auth can-i list nodes --as=system:serviceaccount:w6d2-rbac:dev-sa`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w6d2-rbac --grace-period=0 --force 2>/dev/null || true
  kubectl delete clusterrole node-observer 2>/dev/null || true
  kubectl delete clusterrolebinding bind-node-observer 2>/dev/null || true
'""",
    },
    {
        "day": 3,
        "date": '2026-11-04',
        "title": 'ServiceAccounts & SecurityContexts',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Create ServiceAccount
In namespace `w6d3-sec`:
Create a ServiceAccount named `restricted-sa` with `automountServiceAccountToken: false`.

### Task 2: Hardened Pod SecurityContext
Deploy a Pod named `hardened-app` in namespace `w6d3-sec` (image: `nginx:alpine`):
- Associate with ServiceAccount `restricted-sa`.
- Pod-level `securityContext`:
  - `runAsNonRoot: true`
  - `runAsUser: 10001`
  - `fsGroup: 20000`
- Container-level `securityContext`:
  - `allowPrivilegeEscalation: false`
  - `readOnlyRootFilesystem: true`
  - `capabilities.drop: ["ALL"]`
- Mount an `emptyDir` volume at `/tmp` so nginx has a writable scratch space.
- Verify the pod runs successfully without crashing.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w6d3-sec --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w6d3-sec
'""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: ServiceAccount
AUTO_MNT=$(ssh controlplane 'kubectl get sa restricted-sa -n w6d3-sec -o jsonpath="{.automountServiceAccountToken}" 2>/dev/null || echo "true"')
if [ "$AUTO_MNT" == "false" ]; then
  echo -e "${GREEN}[PASS] Task 1: ServiceAccount restricted-sa configured with automountServiceAccountToken=false.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: ServiceAccount automountServiceAccountToken is $AUTO_MNT.${NC}"
fi

# Task 2: hardened-app securityContext
SEC_UID=$(ssh controlplane 'kubectl get pod hardened-app -n w6d3-sec -o jsonpath="{.spec.securityContext.runAsUser}" 2>/dev/null || echo "0"')
RO_FS=$(ssh controlplane 'kubectl get pod hardened-app -n w6d3-sec -o jsonpath="{.spec.containers[0].securityContext.readOnlyRootFilesystem}" 2>/dev/null || echo "false"')
PHASE=$(ssh controlplane 'kubectl get pod hardened-app -n w6d3-sec -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')

if [ "$SEC_UID" == "10001" ] && [ "$RO_FS" == "true" ] && [ "$PHASE" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: hardened-app running with runAsUser=10001 and readOnlyRootFilesystem=true.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Pod not running or securityContext mismatch (uid=$SEC_UID, ro_fs=$RO_FS, phase=$PHASE).${NC}"
fi""",
        "solution": """1. ServiceAccount:
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: restricted-sa
  namespace: w6d3-sec
automountServiceAccountToken: false
```
`kubectl apply -f sa.yaml`

2. Hardened Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hardened-app
  namespace: w6d3-sec
spec:
  serviceAccountName: restricted-sa
  securityContext:
    runAsNonRoot: true
    runAsUser: 10001
    fsGroup: 20000
  containers:
  - name: nginx
    image: nginx:alpine
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
    volumeMounts:
    - name: tmp-dir
      mountPath: /tmp
  volumes:
  - name: tmp-dir
    emptyDir: {}
```
`kubectl apply -f hardened.yaml`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w6d3-sec --grace-period=0 --force 2>/dev/null || true
'""",
        "cka_title": 'ServiceAccounts & SecurityContexts',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Create ServiceAccount
In namespace `w6d3-sec`:
Create a ServiceAccount named `restricted-sa` with `automountServiceAccountToken: false`.

### Task 2: Hardened Pod SecurityContext
Deploy a Pod named `hardened-app` in namespace `w6d3-sec` (image: `nginx:alpine`):
- Associate with ServiceAccount `restricted-sa`.
- Pod-level `securityContext`:
  - `runAsNonRoot: true`
  - `runAsUser: 10001`
  - `fsGroup: 20000`
- Container-level `securityContext`:
  - `allowPrivilegeEscalation: false`
  - `readOnlyRootFilesystem: true`
  - `capabilities.drop: ["ALL"]`
- Mount an `emptyDir` volume at `/tmp` so nginx has a writable scratch space.
- Verify the pod runs successfully without crashing.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w6d3-sec --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w6d3-sec
'""",
        "cka_verify": """SCORE=0; TOTAL=2
# Task 1: ServiceAccount
AUTO_MNT=$(ssh controlplane 'kubectl get sa restricted-sa -n w6d3-sec -o jsonpath="{.automountServiceAccountToken}" 2>/dev/null || echo "true"')
if [ "$AUTO_MNT" == "false" ]; then
  echo -e "${GREEN}[PASS] Task 1: ServiceAccount restricted-sa configured with automountServiceAccountToken=false.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: ServiceAccount automountServiceAccountToken is $AUTO_MNT.${NC}"
fi

# Task 2: hardened-app securityContext
SEC_UID=$(ssh controlplane 'kubectl get pod hardened-app -n w6d3-sec -o jsonpath="{.spec.securityContext.runAsUser}" 2>/dev/null || echo "0"')
RO_FS=$(ssh controlplane 'kubectl get pod hardened-app -n w6d3-sec -o jsonpath="{.spec.containers[0].securityContext.readOnlyRootFilesystem}" 2>/dev/null || echo "false"')
PHASE=$(ssh controlplane 'kubectl get pod hardened-app -n w6d3-sec -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')

if [ "$SEC_UID" == "10001" ] && [ "$RO_FS" == "true" ] && [ "$PHASE" == "Running" ]; then
  echo -e "${GREEN}[PASS] Task 2: hardened-app running with runAsUser=10001 and readOnlyRootFilesystem=true.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Pod not running or securityContext mismatch (uid=$SEC_UID, ro_fs=$RO_FS, phase=$PHASE).${NC}"
fi""",
        "cka_solution": """1. ServiceAccount:
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: restricted-sa
  namespace: w6d3-sec
automountServiceAccountToken: false
```
`kubectl apply -f sa.yaml`

2. Hardened Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hardened-app
  namespace: w6d3-sec
spec:
  serviceAccountName: restricted-sa
  securityContext:
    runAsNonRoot: true
    runAsUser: 10001
    fsGroup: 20000
  containers:
  - name: nginx
    image: nginx:alpine
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
    volumeMounts:
    - name: tmp-dir
      mountPath: /tmp
  volumes:
  - name: tmp-dir
    emptyDir: {}
```
`kubectl apply -f hardened.yaml`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w6d3-sec --grace-period=0 --force 2>/dev/null || true
'""",
    },
    {
        "day": 4,
        "date": '2026-11-05',
        "title": 'Storage: Volumes, PV, PVC & StorageClasses',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Create PersistentVolume
Create a PersistentVolume named `app-data-pv`:
- Capacity: `200Mi`
- AccessModes: `ReadWriteOnce`
- StorageClassName: `manual`
- HostPath: `/tmp/app-data-pv` (on `node01`)

### Task 2: Create PersistentVolumeClaim
In namespace `w6d4-storage`, create a PVC named `app-data-pvc`:
- AccessModes: `ReadWriteOnce`
- StorageClassName: `manual`
- Storage request: `100Mi`

### Task 3: Deploy Storage Workload
Deploy a Pod named `storage-writer` in namespace `w6d4-storage` (image: `busybox:1.36`):
- Mount `app-data-pvc` at `/mnt/data`
- Command: `sh -c "echo StorageVerified > /mnt/data/success.txt && sleep 3600"`
- Confirm the PVC is `Bound` and the Pod runs.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w6d4-storage --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv app-data-pv 2>/dev/null || true
  kubectl create namespace w6d4-storage
'""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: PV status
PV_STAT=$(ssh controlplane 'kubectl get pv app-data-pv -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PV_STAT" == "Bound" ] || [ "$PV_STAT" == "Available" ]; then
  echo -e "${GREEN}[PASS] Task 1: PersistentVolume app-data-pv exists.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: app-data-pv status is $PV_STAT.${NC}"
fi

# Task 2: PVC status
PVC_STAT=$(ssh controlplane 'kubectl get pvc app-data-pvc -n w6d4-storage -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PVC_STAT" == "Bound" ]; then
  echo -e "${GREEN}[PASS] Task 2: PersistentVolumeClaim app-data-pvc is Bound.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: app-data-pvc is $PVC_STAT (expected Bound).${NC}"
fi

# Task 3: storage-writer Pod and content
CONTENT=$(ssh controlplane 'kubectl exec storage-writer -n w6d4-storage -- cat /mnt/data/success.txt 2>/dev/null || true')
if [ "$CONTENT" == "StorageVerified" ]; then
  echo -e "${GREEN}[PASS] Task 3: storage-writer wrote to PV and verified data persistence.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /mnt/data/success.txt content mismatch: '$CONTENT'.${NC}"
fi""",
        "solution": """1. PV:
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: app-data-pv
spec:
  capacity:
    storage: 200Mi
  accessModes:
  - ReadWriteOnce
  storageClassName: manual
  hostPath:
    path: /tmp/app-data-pv
```
`kubectl apply -f pv.yaml`

2. PVC:
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data-pvc
  namespace: w6d4-storage
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: manual
  resources:
    requests:
      storage: 100Mi
```
`kubectl apply -f pvc.yaml`

3. Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: storage-writer
  namespace: w6d4-storage
spec:
  containers:
  - name: writer
    image: busybox:1.36
    command: ["sh", "-c", "echo StorageVerified > /mnt/data/success.txt && sleep 3600"]
    volumeMounts:
    - name: data-vol
      mountPath: /mnt/data
  volumes:
  - name: data-vol
    persistentVolumeClaim:
      claimName: app-data-pvc
```
`kubectl apply -f pod.yaml`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w6d4-storage --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv app-data-pv 2>/dev/null || true
'""",
        "cka_title": 'Storage: Volumes, PV, PVC & StorageClasses',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Create PersistentVolume
Create a PersistentVolume named `app-data-pv`:
- Capacity: `200Mi`
- AccessModes: `ReadWriteOnce`
- StorageClassName: `manual`
- HostPath: `/tmp/app-data-pv` (on `node01`)

### Task 2: Create PersistentVolumeClaim
In namespace `w6d4-storage`, create a PVC named `app-data-pvc`:
- AccessModes: `ReadWriteOnce`
- StorageClassName: `manual`
- Storage request: `100Mi`

### Task 3: Deploy Storage Workload
Deploy a Pod named `storage-writer` in namespace `w6d4-storage` (image: `busybox:1.36`):
- Mount `app-data-pvc` at `/mnt/data`
- Command: `sh -c "echo StorageVerified > /mnt/data/success.txt && sleep 3600"`
- Confirm the PVC is `Bound` and the Pod runs.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w6d4-storage --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv app-data-pv 2>/dev/null || true
  kubectl create namespace w6d4-storage
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: PV status
PV_STAT=$(ssh controlplane 'kubectl get pv app-data-pv -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PV_STAT" == "Bound" ] || [ "$PV_STAT" == "Available" ]; then
  echo -e "${GREEN}[PASS] Task 1: PersistentVolume app-data-pv exists.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: app-data-pv status is $PV_STAT.${NC}"
fi

# Task 2: PVC status
PVC_STAT=$(ssh controlplane 'kubectl get pvc app-data-pvc -n w6d4-storage -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PVC_STAT" == "Bound" ]; then
  echo -e "${GREEN}[PASS] Task 2: PersistentVolumeClaim app-data-pvc is Bound.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: app-data-pvc is $PVC_STAT (expected Bound).${NC}"
fi

# Task 3: storage-writer Pod and content
CONTENT=$(ssh controlplane 'kubectl exec storage-writer -n w6d4-storage -- cat /mnt/data/success.txt 2>/dev/null || true')
if [ "$CONTENT" == "StorageVerified" ]; then
  echo -e "${GREEN}[PASS] Task 3: storage-writer wrote to PV and verified data persistence.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /mnt/data/success.txt content mismatch: '$CONTENT'.${NC}"
fi""",
        "cka_solution": """1. PV:
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: app-data-pv
spec:
  capacity:
    storage: 200Mi
  accessModes:
  - ReadWriteOnce
  storageClassName: manual
  hostPath:
    path: /tmp/app-data-pv
```
`kubectl apply -f pv.yaml`

2. PVC:
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data-pvc
  namespace: w6d4-storage
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: manual
  resources:
    requests:
      storage: 100Mi
```
`kubectl apply -f pvc.yaml`

3. Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: storage-writer
  namespace: w6d4-storage
spec:
  containers:
  - name: writer
    image: busybox:1.36
    command: ["sh", "-c", "echo StorageVerified > /mnt/data/success.txt && sleep 3600"]
    volumeMounts:
    - name: data-vol
      mountPath: /mnt/data
  volumes:
  - name: data-vol
    persistentVolumeClaim:
      claimName: app-data-pvc
```
`kubectl apply -f pod.yaml`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w6d4-storage --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv app-data-pv 2>/dev/null || true
'""",
    },
    {
        "day": 5,
        "date": '2026-11-06',
        "title": 'Helm & Kustomize (2025 Updates)',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Create Kustomize Overlay
On `controlplane`, in directory `/opt/k8s/kustomize/base`:
A base deployment and service exist.
1. Create a `kustomization.yaml` file in `/opt/k8s/kustomize/base` defining:
   - `resources: [deployment.yaml, service.yaml]`
   - `namePrefix: prod-`
   - `commonLabels: env=production, tier=core`

### Task 2: Apply Declarative Kustomize Manifest
In namespace `w6d5-kustomize`:
1. Build and apply the overlay using `kubectl apply -k /opt/k8s/kustomize/base -n w6d5-kustomize`.
2. Verify that the deployment `prod-web-server` and service `prod-web-service` are created and running with label `env=production`.""",
        "setup": """ssh controlplane '
  kubectl delete namespace w6d5-kustomize --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w6d5-kustomize
  sudo mkdir -p /opt/k8s/kustomize/base && sudo chmod -R 777 /opt/k8s
  cat << "EOF" > /opt/k8s/kustomize/base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-server
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
EOF

  cat << "EOF" > /opt/k8s/kustomize/base/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 80
EOF
  rm -f /opt/k8s/kustomize/base/kustomization.yaml
'""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: kustomization.yaml exists
KUST=$(ssh controlplane 'test -f /opt/k8s/kustomize/base/kustomization.yaml && echo "yes" || echo "no"')
if [ "$KUST" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/kustomize/base/kustomization.yaml created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: kustomization.yaml missing.${NC}"
fi

# Task 2: prod-web-server deployment in w6d5-kustomize
DEP=$(ssh controlplane 'kubectl get deploy prod-web-server -n w6d5-kustomize -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
LBL=$(ssh controlplane 'kubectl get deploy prod-web-server -n w6d5-kustomize -o jsonpath="{.metadata.labels.env}" 2>/dev/null || echo "None"')

if [ "$DEP" -ge 2 ] && [ "$LBL" == "production" ]; then
  echo -e "${GREEN}[PASS] Task 2: prod-web-server applied with prefix and env=production label.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Deployment prod-web-server not running ($DEP/2) or label=$LBL.${NC}"
fi""",
        "solution": """1. Create `/opt/k8s/kustomize/base/kustomization.yaml`:
```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- deployment.yaml
- service.yaml
namePrefix: prod-
commonLabels:
  env: production
  tier: core
```

2. Apply:
`kubectl apply -k /opt/k8s/kustomize/base -n w6d5-kustomize`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w6d5-kustomize --grace-period=0 --force 2>/dev/null || true
  rm -rf /opt/k8s/kustomize
'""",
        "cka_title": 'Helm & Kustomize (2025 Updates)',
        "cka_diff": 'Medium',
        "cka_time": '35m',
        "cka_tasks": """### Task 1: Create Kustomize Overlay
On `controlplane`, in directory `/opt/k8s/kustomize/base`:
A base deployment and service exist.
1. Create a `kustomization.yaml` file in `/opt/k8s/kustomize/base` defining:
   - `resources: [deployment.yaml, service.yaml]`
   - `namePrefix: prod-`
   - `commonLabels: env=production, tier=core`

### Task 2: Apply Declarative Kustomize Manifest
In namespace `w6d5-kustomize`:
1. Build and apply the overlay using `kubectl apply -k /opt/k8s/kustomize/base -n w6d5-kustomize`.
2. Verify that the deployment `prod-web-server` and service `prod-web-service` are created and running with label `env=production`.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w6d5-kustomize --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w6d5-kustomize
  sudo mkdir -p /opt/k8s/kustomize/base && sudo chmod -R 777 /opt/k8s
  cat << "EOF" > /opt/k8s/kustomize/base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-server
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
EOF

  cat << "EOF" > /opt/k8s/kustomize/base/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 80
EOF
  rm -f /opt/k8s/kustomize/base/kustomization.yaml
'""",
        "cka_verify": """SCORE=0; TOTAL=2
# Task 1: kustomization.yaml exists
KUST=$(ssh controlplane 'test -f /opt/k8s/kustomize/base/kustomization.yaml && echo "yes" || echo "no"')
if [ "$KUST" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 1: /opt/k8s/kustomize/base/kustomization.yaml created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: kustomization.yaml missing.${NC}"
fi

# Task 2: prod-web-server deployment in w6d5-kustomize
DEP=$(ssh controlplane 'kubectl get deploy prod-web-server -n w6d5-kustomize -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
LBL=$(ssh controlplane 'kubectl get deploy prod-web-server -n w6d5-kustomize -o jsonpath="{.metadata.labels.env}" 2>/dev/null || echo "None"')

if [ "$DEP" -ge 2 ] && [ "$LBL" == "production" ]; then
  echo -e "${GREEN}[PASS] Task 2: prod-web-server applied with prefix and env=production label.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Deployment prod-web-server not running ($DEP/2) or label=$LBL.${NC}"
fi""",
        "cka_solution": """1. Create `/opt/k8s/kustomize/base/kustomization.yaml`:
```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- deployment.yaml
- service.yaml
namePrefix: prod-
commonLabels:
  env: production
  tier: core
```

2. Apply:
`kubectl apply -k /opt/k8s/kustomize/base -n w6d5-kustomize`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w6d5-kustomize --grace-period=0 --force 2>/dev/null || true
  rm -rf /opt/k8s/kustomize
'""",
    },
    {
        "day": 6,
        "date": '2026-11-07',
        "title": 'Security & Storage Lab Triathlon',
        "diff": 'Hard (Milestone Assessment 6)',
        "time": '45m',
        "tasks": """### Milestone 6 Triathlon Tasks:
In namespace `w6-milestone`:
1. **ServiceAccount & RBAC**:
   Create a ServiceAccount `vault-operator`.
   Create a Role `secret-reader` granting `get, list` on `secrets`.
   Bind `secret-reader` to `vault-operator` via RoleBinding `bind-secret-reader`.

2. **Persistent Storage**:
   Create a PersistentVolume `m6-pv` (150Mi, hostPath: `/tmp/m6-pv`, storageClassName: `fast-storage`).
   Create a PersistentVolumeClaim `m6-pvc` in `w6-milestone` (requesting 100Mi, storageClassName: `fast-storage`).

3. **Hardened Storage Pod**:
   Deploy Pod `vault-pod` in `w6-milestone` (image: `busybox:1.36`):
   - ServiceAccount: `vault-operator`
   - SecurityContext: `runAsUser: 10001`
   - Mount `m6-pvc` at `/data`
   - Command: `sh -c "echo Milestone6Complete > /data/flag.txt && sleep 3600"`""",
        "setup": """ssh controlplane '
  kubectl delete namespace w6-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv m6-pv 2>/dev/null || true
  kubectl create namespace w6-milestone
'""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: RBAC check
CAN_SEC=$(ssh controlplane 'kubectl auth can-i list secrets -n w6-milestone --as=system:serviceaccount:w6-milestone:vault-operator 2>/dev/null || echo "no"')
if [ "$CAN_SEC" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 1: vault-operator authorized to list secrets in w6-milestone.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: vault-operator cannot list secrets.${NC}"
fi

# Task 2: PVC bound
PVC_ST=$(ssh controlplane 'kubectl get pvc m6-pvc -n w6-milestone -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PVC_ST" == "Bound" ]; then
  echo -e "${GREEN}[PASS] Task 2: PersistentVolumeClaim m6-pvc is Bound.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: m6-pvc status is $PVC_ST (expected Bound).${NC}"
fi

# Task 3: Pod flag.txt
FLAG=$(ssh controlplane 'kubectl exec vault-pod -n w6-milestone -- cat /data/flag.txt 2>/dev/null || true')
if [ "$FLAG" == "Milestone6Complete" ]; then
  echo -e "${GREEN}[PASS] Task 3: vault-pod running with volume mount and verified flag.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /data/flag.txt mismatch: '$FLAG'.${NC}"
fi""",
        "solution": """1. ServiceAccount & RBAC:
`kubectl create sa vault-operator -n w6-milestone`
`kubectl create role secret-reader -n w6-milestone --verb=get,list --resource=secrets`
`kubectl create rolebinding bind-secret-reader -n w6-milestone --role=secret-reader --serviceaccount=w6-milestone:vault-operator`

2. PV & PVC:
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: m6-pv
spec:
  capacity:
    storage: 150Mi
  accessModes:
  - ReadWriteOnce
  storageClassName: fast-storage
  hostPath:
    path: /tmp/m6-pv
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: m6-pvc
  namespace: w6-milestone
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: fast-storage
  resources:
    requests:
      storage: 100Mi
```
`kubectl apply -f storage.yaml`

3. Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: vault-pod
  namespace: w6-milestone
spec:
  serviceAccountName: vault-operator
  securityContext:
    runAsUser: 10001
  containers:
  - name: box
    image: busybox:1.36
    command: ["sh", "-c", "echo Milestone6Complete > /data/flag.txt && sleep 3600"]
    volumeMounts:
    - name: vol
      mountPath: /data
  volumes:
  - name: vol
    persistentVolumeClaim:
      claimName: m6-pvc
```
`kubectl apply -f pod.yaml`""",
        "reset": """ssh controlplane '
  kubectl delete namespace w6-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv m6-pv 2>/dev/null || true
'""",
        "cka_title": 'Security & Storage Lab Triathlon',
        "cka_diff": 'Hard (Milestone Assessment 6)',
        "cka_time": '45m',
        "cka_tasks": """### Milestone 6 Triathlon Tasks:
In namespace `w6-milestone`:
1. **ServiceAccount & RBAC**:
   Create a ServiceAccount `vault-operator`.
   Create a Role `secret-reader` granting `get, list` on `secrets`.
   Bind `secret-reader` to `vault-operator` via RoleBinding `bind-secret-reader`.

2. **Persistent Storage**:
   Create a PersistentVolume `m6-pv` (150Mi, hostPath: `/tmp/m6-pv`, storageClassName: `fast-storage`).
   Create a PersistentVolumeClaim `m6-pvc` in `w6-milestone` (requesting 100Mi, storageClassName: `fast-storage`).

3. **Hardened Storage Pod**:
   Deploy Pod `vault-pod` in `w6-milestone` (image: `busybox:1.36`):
   - ServiceAccount: `vault-operator`
   - SecurityContext: `runAsUser: 10001`
   - Mount `m6-pvc` at `/data`
   - Command: `sh -c "echo Milestone6Complete > /data/flag.txt && sleep 3600"`""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w6-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv m6-pv 2>/dev/null || true
  kubectl create namespace w6-milestone
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: RBAC check
CAN_SEC=$(ssh controlplane 'kubectl auth can-i list secrets -n w6-milestone --as=system:serviceaccount:w6-milestone:vault-operator 2>/dev/null || echo "no"')
if [ "$CAN_SEC" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 1: vault-operator authorized to list secrets in w6-milestone.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: vault-operator cannot list secrets.${NC}"
fi

# Task 2: PVC bound
PVC_ST=$(ssh controlplane 'kubectl get pvc m6-pvc -n w6-milestone -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PVC_ST" == "Bound" ]; then
  echo -e "${GREEN}[PASS] Task 2: PersistentVolumeClaim m6-pvc is Bound.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: m6-pvc status is $PVC_ST (expected Bound).${NC}"
fi

# Task 3: Pod flag.txt
FLAG=$(ssh controlplane 'kubectl exec vault-pod -n w6-milestone -- cat /data/flag.txt 2>/dev/null || true')
if [ "$FLAG" == "Milestone6Complete" ]; then
  echo -e "${GREEN}[PASS] Task 3: vault-pod running with volume mount and verified flag.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /data/flag.txt mismatch: '$FLAG'.${NC}"
fi""",
        "cka_solution": """1. ServiceAccount & RBAC:
`kubectl create sa vault-operator -n w6-milestone`
`kubectl create role secret-reader -n w6-milestone --verb=get,list --resource=secrets`
`kubectl create rolebinding bind-secret-reader -n w6-milestone --role=secret-reader --serviceaccount=w6-milestone:vault-operator`

2. PV & PVC:
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: m6-pv
spec:
  capacity:
    storage: 150Mi
  accessModes:
  - ReadWriteOnce
  storageClassName: fast-storage
  hostPath:
    path: /tmp/m6-pv
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: m6-pvc
  namespace: w6-milestone
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: fast-storage
  resources:
    requests:
      storage: 100Mi
```
`kubectl apply -f storage.yaml`

3. Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: vault-pod
  namespace: w6-milestone
spec:
  serviceAccountName: vault-operator
  securityContext:
    runAsUser: 10001
  containers:
  - name: box
    image: busybox:1.36
    command: ["sh", "-c", "echo Milestone6Complete > /data/flag.txt && sleep 3600"]
    volumeMounts:
    - name: vol
      mountPath: /data
  volumes:
  - name: vol
    persistentVolumeClaim:
      claimName: m6-pvc
```
`kubectl apply -f pod.yaml`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w6-milestone --grace-period=0 --force 2>/dev/null || true
  kubectl delete pv m6-pv 2>/dev/null || true
'""",
    },
]
