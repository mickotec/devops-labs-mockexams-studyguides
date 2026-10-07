"""
Lab definitions for Week 6
"""

WEEK_6_LABS = [
    # Day 1
    {
        "day": 1,
        "date": "2026-11-02",
        "cka_title": "Certificates API & KubeConfig Management",
        "cka_diff": "Medium",
        "cka_time": "35m",
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
B64_CSR=$(cat /opt/k8s/developer-bob.csr | base64 | tr -d '\n')
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

        "lfcs_title": "Storage Partitions (MBR vs GPT) & Swap",
        "lfcs_diff": "Medium",
        "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Dedicated Swap File Creation
1. Create a `128MB` swap file at `/var/tmp/swapfile_extra` (use `dd` or `fallocate`).
2. Set permissions strictly to `0600` (`chmod 600`).
3. Format it as swap space with `mkswap`.

### Task 2: Swap Space Activation & Persistence
1. Activate the swap file with `swapon /var/tmp/swapfile_extra`.
2. Append a persistent entry to `/etc/fstab` so it activates on boot:
   `/var/tmp/swapfile_extra none swap sw 0 0`
3. Verify that `swapon --show` displays `/var/tmp/swapfile_extra`.""",
        "lfcs_setup": """sudo swapoff /var/tmp/swapfile_extra 2>/dev/null || true
sudo rm -f /var/tmp/swapfile_extra
sudo sed -i '\|/var/tmp/swapfile_extra|d' /etc/fstab""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: Swap file permissions and active
SWAP_ACTIVE=$(swapon --show | grep "/var/tmp/swapfile_extra" || true)
PERM=$(stat -c "%a" /var/tmp/swapfile_extra 2>/dev/null || echo "0")

if [ -n "$SWAP_ACTIVE" ] && [ "$PERM" == "600" ]; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/swapfile_extra active as swap with permissions 600.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Swap file inactive or permissions=$PERM (expected 600).${NC}"
fi

# Task 2: /etc/fstab entry
if grep -q "/var/tmp/swapfile_extra.*swap" /etc/fstab; then
  echo -e "${GREEN}[PASS] Task 2: /etc/fstab contains persistent swap entry.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/fstab missing entry for /var/tmp/swapfile_extra.${NC}"
fi""",
        "lfcs_solution": """1. Create & format swap:
`sudo dd if=/dev/zero of=/var/tmp/swapfile_extra bs=1M count=128`
`sudo chmod 600 /var/tmp/swapfile_extra`
`sudo mkswap /var/tmp/swapfile_extra`

2. Activate & persist:
`sudo swapon /var/tmp/swapfile_extra`
`echo "/var/tmp/swapfile_extra none swap sw 0 0" | sudo tee -a /etc/fstab`""",
        "lfcs_reset": """sudo swapoff /var/tmp/swapfile_extra 2>/dev/null || true
sudo rm -f /var/tmp/swapfile_extra
sudo sed -i '\|/var/tmp/swapfile_extra|d' /etc/fstab"""
    },

    # Day 2
    {
        "day": 2,
        "date": "2026-11-03",
        "cka_title": "RBAC (Roles, RoleBindings & ClusterRoles)",
        "cka_diff": "Medium",
        "cka_time": "35m",
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

        "lfcs_title": "Filesystems & Boot Mounting (/etc/fstab)",
        "lfcs_diff": "Medium",
        "lfcs_time": "35m",
        "lfcs_tasks": """### Task 1: Loop Device Filesystem Formatting
A 150MB loop disk image `/var/tmp/data_store.img` has been initialized and associated with `/dev/loop90`.
- Format `/dev/loop90` with the `ext4` filesystem with filesystem label `DATA_STORE`.

### Task 2: Mount Point & Persistent /etc/fstab Entry
1. Create mount directory `/mnt/data_store`.
2. Extract the filesystem UUID of `/dev/loop90` using `blkid`.
3. Add an `/etc/fstab` entry:
   `UUID=<extracted-uuid> /mnt/data_store ext4 defaults,noatime 0 2`
4. Mount all filesystems with `sudo mount -a`.
5. Verify `/mnt/data_store` is mounted and writable.""",
        "lfcs_setup": """sudo umount /mnt/data_store 2>/dev/null || true
sudo losetup -d /dev/loop90 2>/dev/null || true
sudo sed -i '\|/mnt/data_store|d' /etc/fstab
sudo rm -rf /var/tmp/data_store.img /mnt/data_store
sudo mkdir -p /mnt/data_store && sudo chmod 777 /mnt/data_store
dd if=/dev/zero of=/var/tmp/data_store.img bs=1M count=150 >/dev/null 2>&1
sudo losetup /dev/loop90 /var/tmp/data_store.img""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1 & 2: Mounted filesystem
IS_MOUNTED=$(findmnt /mnt/data_store -o FSTYPE,OPTIONS -n 2>/dev/null || true)
if echo "$IS_MOUNTED" | grep -q "ext4" && echo "$IS_MOUNTED" | grep -q "noatime"; then
  echo -e "${GREEN}[PASS] Task 1: /mnt/data_store is mounted with ext4 and noatime.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /mnt/data_store not mounted or missing noatime option: $IS_MOUNTED.${NC}"
fi

# Task 2: /etc/fstab has UUID entry
if grep -qiE "UUID=.*\/mnt\/data_store.*ext4.*noatime" /etc/fstab; then
  echo -e "${GREEN}[PASS] Task 2: /etc/fstab configured with UUID and persistent options.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/fstab missing proper UUID entry for /mnt/data_store.${NC}"
fi""",
        "lfcs_solution": """1. Format:
`sudo mkfs.ext4 -L DATA_STORE /dev/loop90`

2. UUID and fstab:
`UUID=$(sudo blkid -s UUID -o value /dev/loop90)`
`echo "UUID=$UUID /mnt/data_store ext4 defaults,noatime 0 2" | sudo tee -a /etc/fstab`

3. Mount:
`sudo mount -a`""",
        "lfcs_reset": """sudo umount /mnt/data_store 2>/dev/null || true
sudo losetup -d /dev/loop90 2>/dev/null || true
sudo sed -i '\|/mnt/data_store|d' /etc/fstab
sudo rm -rf /var/tmp/data_store.img /mnt/data_store"""
    },

    # Day 3
    {
        "day": 3,
        "date": "2026-11-04",
        "cka_title": "ServiceAccounts & SecurityContexts",
        "cka_diff": "Medium",
        "cka_time": "35m",
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

        "lfcs_title": "Logical Volume Management (LVM) Architecture",
        "lfcs_diff": "Medium",
        "lfcs_time": "35m",
        "lfcs_tasks": """### Task 1: Create LVM Storage Hierarchy
Loop device `/dev/loop91` (250MB) has been prepared.
1. Initialize `/dev/loop91` as an LVM Physical Volume using `pvcreate`.
2. Create a Volume Group named `vg_database` containing `/dev/loop91`.
3. Create a Logical Volume named `lv_orders` with size `120MB` inside `vg_database`.

### Task 2: Format and Mount Logical Volume
1. Format `/dev/vg_database/lv_orders` with the `ext4` filesystem.
2. Mount it at `/mnt/orders_data`.
3. Confirm with `lvs` and `df -h /mnt/orders_data`.""",
        "lfcs_setup": """sudo umount /mnt/orders_data 2>/dev/null || true
sudo lvremove -f /dev/vg_database/lv_orders 2>/dev/null || true
sudo vgremove -f vg_database 2>/dev/null || true
sudo pvremove -f /dev/loop91 2>/dev/null || true
sudo losetup -d /dev/loop91 2>/dev/null || true
sudo rm -rf /var/tmp/lvm_backing.img /mnt/orders_data
sudo mkdir -p /mnt/orders_data && sudo chmod 777 /mnt/orders_data
dd if=/dev/zero of=/var/tmp/lvm_backing.img bs=1M count=250 >/dev/null 2>&1
sudo losetup /dev/loop91 /var/tmp/lvm_backing.img""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: LVM objects
LV_EXISTS=$(sudo lvs -o lv_name,vg_name --noheadings /dev/vg_database/lv_orders 2>/dev/null || echo "None")
if echo "$LV_EXISTS" | grep -q "lv_orders" && echo "$LV_EXISTS" | grep -q "vg_database"; then
  echo -e "${GREEN}[PASS] Task 1: Logical Volume lv_orders exists in vg_database.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Logical Volume /dev/vg_database/lv_orders not found.${NC}"
fi

# Task 2: Mounted
MNT_CHECK=$(findmnt /mnt/orders_data -o SOURCE,FSTYPE -n 2>/dev/null || true)
if echo "$MNT_CHECK" | grep -q "lv_orders" && echo "$MNT_CHECK" | grep -q "ext4"; then
  echo -e "${GREEN}[PASS] Task 2: /mnt/orders_data is mounted from lv_orders (ext4).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /mnt/orders_data not mounted from lv_orders: $MNT_CHECK.${NC}"
fi""",
        "lfcs_solution": """1. LVM setup:
`sudo pvcreate /dev/loop91`
`sudo vgcreate vg_database /dev/loop91`
`sudo lvcreate -L 120M -n lv_orders vg_database`

2. Format & mount:
`sudo mkfs.ext4 /dev/vg_database/lv_orders`
`sudo mount /dev/vg_database/lv_orders /mnt/orders_data`""",
        "lfcs_reset": """sudo umount /mnt/orders_data 2>/dev/null || true
sudo lvremove -f /dev/vg_database/lv_orders 2>/dev/null || true
sudo vgremove -f vg_database 2>/dev/null || true
sudo pvremove -f /dev/loop91 2>/dev/null || true
sudo losetup -d /dev/loop91 2>/dev/null || true
sudo rm -rf /var/tmp/lvm_backing.img /mnt/orders_data"""
    },

    # Day 4
    {
        "day": 4,
        "date": "2026-11-05",
        "cka_title": "Storage: Volumes, PV, PVC & StorageClasses",
        "cka_diff": "Medium",
        "cka_time": "35m",
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

        "lfcs_title": "Dynamic LVM Volume Expansion",
        "lfcs_diff": "Medium",
        "lfcs_time": "35m",
        "lfcs_tasks": """### Task 1: Extend Logical Volume
A Volume Group `vg_expand` (size 350MB) and mounted Logical Volume `lv_store` (initial size 100MB mounted at `/mnt/expand_store`) are active.
1. Extend `lv_store` by `100MB` (to total size 200MB) using `lvextend`.

### Task 2: Online Filesystem Resize
Resize the `ext4` filesystem online without unmounting using `resize2fs /dev/vg_expand/lv_store`.
- Confirm with `df -h /mnt/expand_store` that the filesystem reflects ~200MB.""",
        "lfcs_setup": """sudo umount /mnt/expand_store 2>/dev/null || true
sudo lvremove -f /dev/vg_expand/lv_store 2>/dev/null || true
sudo vgremove -f vg_expand 2>/dev/null || true
sudo pvremove -f /dev/loop92 2>/dev/null || true
sudo losetup -d /dev/loop92 2>/dev/null || true
sudo rm -rf /var/tmp/expand_backing.img /mnt/expand_store
sudo mkdir -p /mnt/expand_store && sudo chmod 777 /mnt/expand_store
dd if=/dev/zero of=/var/tmp/expand_backing.img bs=1M count=350 >/dev/null 2>&1
sudo losetup /dev/loop92 /var/tmp/expand_backing.img
sudo pvcreate /dev/loop92 >/dev/null 2>&1
sudo vgcreate vg_expand /dev/loop92 >/dev/null 2>&1
sudo lvcreate -L 100M -n lv_store vg_expand >/dev/null 2>&1
sudo mkfs.ext4 /dev/vg_expand/lv_store >/dev/null 2>&1
sudo mount /dev/vg_expand/lv_store /mnt/expand_store""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: LV Size is 200MB
LV_SZ=$(sudo lvs -o lv_size --units m --noheadings /dev/vg_expand/lv_store 2>/dev/null | tr -d ' ' || echo "0")
if echo "$LV_SZ" | grep -q "200"; then
  echo -e "${GREEN}[PASS] Task 1: Logical Volume lv_store extended to 200MB.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: lv_store size is $LV_SZ (expected 200MB).${NC}"
fi

# Task 2: Filesystem reflects expanded size
FS_SIZE=$(df -m /mnt/expand_store | tail -1 | awk '{print $2}' || echo "0")
if [ "$FS_SIZE" -ge 180 ]; then
  echo -e "${GREEN}[PASS] Task 2: Filesystem resized online ($FS_SIZE MB).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Filesystem size is $FS_SIZE MB (expected >= 180MB).${NC}"
fi""",
        "lfcs_solution": """1. Extend LV:
`sudo lvextend -L +100M /dev/vg_expand/lv_store`

2. Resize filesystem:
`sudo resize2fs /dev/vg_expand/lv_store`""",
        "lfcs_reset": """sudo umount /mnt/expand_store 2>/dev/null || true
sudo lvremove -f /dev/vg_expand/lv_store 2>/dev/null || true
sudo vgremove -f vg_expand 2>/dev/null || true
sudo pvremove -f /dev/loop92 2>/dev/null || true
sudo losetup -d /dev/loop92 2>/dev/null || true
sudo rm -rf /var/tmp/expand_backing.img /mnt/expand_store"""
    },

    # Day 5
    {
        "day": 5,
        "date": "2026-11-06",
        "cka_title": "Helm & Kustomize (2025 Updates)",
        "cka_diff": "Medium",
        "cka_time": "35m",
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

        "lfcs_title": "Remote Filesystems: NFS & Storage Monitoring",
        "lfcs_diff": "Medium",
        "lfcs_time": "30m",
        "lfcs_tasks": """### Task 1: Storage Monitoring Audit Script
Create a monitoring script at `/usr/local/bin/check-disk.sh`:
- Script is executable (`chmod 755`).
- Extract all mounted filesystems with their filesystem type and usage percentage into `/var/tmp/disk_audit.txt` (formatted with headers `Filesystem Type Size Used Avail Use% Mounted_on`).

### Task 2: Disk Alert Threshold
Configure the script so that if any filesystem usage exceeds `85%`, it appends `WARNING: High disk utilization detected` to `/var/log/disk_alert.log`.""",
        "lfcs_setup": """sudo rm -f /usr/local/bin/check-disk.sh /var/tmp/disk_audit.txt /var/log/disk_alert.log""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: check-disk.sh exists and produces output
if [ -x /usr/local/bin/check-disk.sh ]; then
  sudo /usr/local/bin/check-disk.sh
  if [ -f /var/tmp/disk_audit.txt ] && [ -s /var/tmp/disk_audit.txt ]; then
    echo -e "${GREEN}[PASS] Task 1: /usr/local/bin/check-disk.sh generated /var/tmp/disk_audit.txt.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Task 1: /var/tmp/disk_audit.txt not generated.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Task 1: /usr/local/bin/check-disk.sh missing or not executable.${NC}"
fi

# Task 2: check headers
if [ -f /var/tmp/disk_audit.txt ] && grep -qiE "Filesystem|Use%" /var/tmp/disk_audit.txt; then
  echo -e "${GREEN}[PASS] Task 2: Disk audit report format verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Report format missing headers.${NC}"
fi""",
        "lfcs_solution": """1. Create `/usr/local/bin/check-disk.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail
df -hT > /var/tmp/disk_audit.txt
df -hP | awk '0+$5 >= 85 {print "WARNING: High disk utilization on "$1" ("$5")"}' >> /var/log/disk_alert.log || true
```
`sudo chmod 755 /usr/local/bin/check-disk.sh`
`sudo /usr/local/bin/check-disk.sh`""",
        "lfcs_reset": """sudo rm -f /usr/local/bin/check-disk.sh /var/tmp/disk_audit.txt /var/log/disk_alert.log"""
    },

    # Day 6
    {
        "day": 6,
        "date": "2026-11-07",
        "cka_title": "Security & Storage Lab Triathlon",
        "cka_diff": "Hard (Milestone Assessment 6)",
        "cka_time": "45m",
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

        "lfcs_title": "Week 6 Storage Mastery & LVM Drill",
        "lfcs_diff": "Hard (Milestone Assessment 6)",
        "lfcs_time": "45m",
        "lfcs_tasks": """### Milestone 6 Triathlon Tasks:
1. **LVM Storage Creation**:
   Loop device `/dev/loop93` (300MB) has been prepared.
   - Create Volume Group `vg_secure`.
   - Create Logical Volume `lv_audit` (120MB).
   - Format with `ext4` and mount at `/mnt/secure_audit`.

2. **Access Control Lists (ACL)**:
   - Use `setfacl` to grant user `student` read, write, and execute permissions (`rwx`) on `/mnt/secure_audit` (`setfacl -m u:student:rwx /mnt/secure_audit`).
   - Confirm with `getfacl /mnt/secure_audit`.

3. **Online Volume Expansion**:
   Extend `lv_audit` by `60MB` and resize filesystem online (`resize2fs`).
   Verify total mounted size >= 170MB.""",
        "lfcs_setup": """sudo umount /mnt/secure_audit 2>/dev/null || true
sudo lvremove -f /dev/vg_secure/lv_audit 2>/dev/null || true
sudo vgremove -f vg_secure 2>/dev/null || true
sudo pvremove -f /dev/loop93 2>/dev/null || true
sudo losetup -d /dev/loop93 2>/dev/null || true
sudo rm -rf /var/tmp/m6_backing.img /mnt/secure_audit
sudo mkdir -p /mnt/secure_audit && sudo chmod 777 /mnt/secure_audit
dd if=/dev/zero of=/var/tmp/m6_backing.img bs=1M count=300 >/dev/null 2>&1
sudo losetup /dev/loop93 /var/tmp/m6_backing.img
sudo pvcreate /dev/loop93 >/dev/null 2>&1""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: LV and mount
MNT=$(findmnt /mnt/secure_audit -o SOURCE,FSTYPE -n 2>/dev/null || true)
if echo "$MNT" | grep -q "lv_audit" && echo "$MNT" | grep -q "ext4"; then
  echo -e "${GREEN}[PASS] Task 1: /mnt/secure_audit is mounted on lv_audit (ext4).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /mnt/secure_audit not mounted on lv_audit: $MNT.${NC}"
fi

# Task 2: ACL
ACL_CHECK=$(getfacl /mnt/secure_audit 2>/dev/null || true)
if echo "$ACL_CHECK" | grep -q "user:student:rwx"; then
  echo -e "${GREEN}[PASS] Task 2: ACL permissions user:student:rwx verified on /mnt/secure_audit.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: ACL missing user:student:rwx.${NC}"
fi

# Task 3: Size >= 170M
SZ=$(df -m /mnt/secure_audit | tail -1 | awk '{print $2}' || echo "0")
if [ "$SZ" -ge 160 ]; then
  echo -e "${GREEN}[PASS] Task 3: Online LVM expansion verified ($SZ MB).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Size is $SZ MB (expected >= 160MB).${NC}"
fi""",
        "lfcs_solution": """1. Create LVM & mount:
`sudo vgcreate vg_secure /dev/loop93`
`sudo lvcreate -L 120M -n lv_audit vg_secure`
`sudo mkfs.ext4 /dev/vg_secure/lv_audit`
`sudo mount /dev/vg_secure/lv_audit /mnt/secure_audit`

2. Set ACL:
`sudo setfacl -m u:student:rwx /mnt/secure_audit`

3. Extend:
`sudo lvextend -L +60M /dev/vg_secure/lv_audit`
`sudo resize2fs /dev/vg_secure/lv_audit`""",
        "lfcs_reset": """sudo umount /mnt/secure_audit 2>/dev/null || true
sudo lvremove -f /dev/vg_secure/lv_audit 2>/dev/null || true
sudo vgremove -f vg_secure 2>/dev/null || true
sudo pvremove -f /dev/loop93 2>/dev/null || true
sudo losetup -d /dev/loop93 2>/dev/null || true
sudo rm -rf /var/tmp/m6_backing.img /mnt/secure_audit"""
    }
]
