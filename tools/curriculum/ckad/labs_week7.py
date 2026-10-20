"""
Dedicated CKAD Lab Definitions for Week 7 (Days 1 to 6).
Aligned with KodeKloud CKAD Learning Modules: State Persistence
"""

WEEK_7_LABS = [
    {
        "day": 1,
        "date": "2026-11-23",
        "title": "Volumes: emptyDir Memory Cache & hostPath",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Configure In-Memory emptyDir Volume
1. In namespace `ckad-w7d1`, deploy Pod `cache-node` with image `busybox:1.36`.
2. Configure an `emptyDir` volume named `ram-cache` with `medium: Memory` and `sizeLimit: 64Mi`.
3. Mount `ram-cache` at `/cache` inside the container.
4. Also mount a `hostPath` volume named `host-logs` at `/node-logs` (path: `/var/log`, type: `Directory`, readOnly: true).
5. Verify `cache-node` runs and `df -T /cache` inside the pod reports `tmpfs`.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w7d1 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W7D1: emptyDir Memory in ckad-w7d1..."

PHASE=$(ssh controlplane 'kubectl get pod cache-node -n ckad-w7d1 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
FS_TYPE=$(ssh controlplane 'kubectl exec cache-node -n ckad-w7d1 -- df -T /cache 2>/dev/null | tail -n 1 | awk "{print \$2}" || echo ""')

if [ "$PHASE" == "Running" ] && [ "$FS_TYPE" == "tmpfs" ]; then
  echo -e "\033[0;32m[PASS] Pod cache-node running with in-memory emptyDir (tmpfs) mounted at /cache.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Phase: $PHASE | /cache filesystem type: '$FS_TYPE' (expected tmpfs).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: emptyDir Memory
```bash
ssh controlplane 'cat << "EOF_POD" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: cache-node
  namespace: ckad-w7d1
spec:
  volumes:
  - name: ram-cache
    emptyDir:
      medium: Memory
      sizeLimit: 64Mi
  - name: host-logs
    hostPath:
      path: /var/log
      type: Directory
  containers:
  - name: worker
    image: busybox:1.36
    command: ["sleep", "3600"]
    volumeMounts:
    - name: ram-cache
      mountPath: /cache
    - name: host-logs
      mountPath: /node-logs
      readOnly: true
EOF_POD
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w7d1 --ignore-not-found'"""
    },
    {
        "day": 2,
        "date": "2026-11-24",
        "title": "PersistentVolumes: AccessModes & Reclaim Policies",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Create PersistentVolume
1. Create a PersistentVolume named `app-storage-pv`:
   - Capacity: `2Gi`
   - `accessModes`: `ReadWriteOnce`
   - `persistentVolumeReclaimPolicy`: `Retain`
   - `storageClassName`: `manual-storage`
   - `hostPath`: `/mnt/k8s-pv-data` (type: `DirectoryOrCreate`)
2. Verify that `app-storage-pv` reports status `Available`.""",
        "setup": """ssh controlplane 'kubectl delete pv app-storage-pv --ignore-not-found'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W7D2: PersistentVolume app-storage-pv..."

CAP=$(ssh controlplane 'kubectl get pv app-storage-pv -o jsonpath="{.spec.capacity.storage}" 2>/dev/null || echo ""')
RECLAIM=$(ssh controlplane 'kubectl get pv app-storage-pv -o jsonpath="{.spec.persistentVolumeReclaimPolicy}" 2>/dev/null || echo ""')
STATUS=$(ssh controlplane 'kubectl get pv app-storage-pv -o jsonpath="{.status.phase}" 2>/dev/null || echo ""')

if [ "$CAP" == "2Gi" ] && [ "$RECLAIM" == "Retain" ] && [ "$STATUS" == "Available" ]; then
  echo -e "\033[0;32m[PASS] PersistentVolume app-storage-pv Available (2Gi, Retain, ReadWriteOnce).\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Capacity: $CAP | Reclaim: $RECLAIM | Status: $STATUS (expected Available).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: PersistentVolume
```bash
ssh controlplane 'cat << "EOF_PV" | kubectl apply -f -
apiVersion: v1
kind: PersistentVolume
metadata:
  name: app-storage-pv
spec:
  capacity:
    storage: 2Gi
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: manual-storage
  hostPath:
    path: /mnt/k8s-pv-data
    type: DirectoryOrCreate
EOF_PV
'
```""",
        "reset": """ssh controlplane 'kubectl delete pv app-storage-pv --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-11-25",
        "title": "PersistentVolumeClaims & Volume Binding",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Bind PersistentVolumeClaim
1. On the cluster, PV `claim-target-pv` (1Gi, `storageClassName: manual-target`) already exists in `Available` status.
2. In namespace `ckad-w7d3`, create a PersistentVolumeClaim named `app-storage-pvc`:
   - `storageClassName`: `manual-target`
   - `accessModes`: `ReadWriteOnce`
   - Requests: `1Gi` storage
3. Verify `app-storage-pvc` transitions from `Pending` to `Bound` to `claim-target-pv`.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w7d3 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_PV" | kubectl apply -f -
apiVersion: v1
kind: PersistentVolume
metadata:
  name: claim-target-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
  - ReadWriteOnce
  storageClassName: manual-target
  hostPath:
    path: /mnt/target-data
    type: DirectoryOrCreate
EOF_PV
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W7D3: PVC Binding in ckad-w7d3..."

STATUS=$(ssh controlplane 'kubectl get pvc app-storage-pvc -n ckad-w7d3 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
BOUND_PV=$(ssh controlplane 'kubectl get pvc app-storage-pvc -n ckad-w7d3 -o jsonpath="{.spec.volumeName}" 2>/dev/null || echo ""')

if [ "$STATUS" == "Bound" ] && [ "$BOUND_PV" == "claim-target-pv" ]; then
  echo -e "\033[0;32m[PASS] PVC app-storage-pvc successfully Bound to claim-target-pv.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Status: '$STATUS' (expected Bound) | Bound PV: '$BOUND_PV'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: PersistentVolumeClaims
```bash
ssh controlplane 'cat << "EOF_PVC" | kubectl apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-storage-pvc
  namespace: ckad-w7d3
spec:
  storageClassName: manual-target
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
EOF_PVC
'
```""",
        "reset": """ssh controlplane '
kubectl delete namespace ckad-w7d3 --ignore-not-found
kubectl delete pv claim-target-pv --ignore-not-found
'"""
    },
    {
        "day": 4,
        "date": "2026-11-26",
        "title": "Consuming PVCs in Pods & Data Persistence",
        "diff": "Hard",
        "time": "30m",
        "tasks": """### Task 1: Verify Storage Persistence Across Pod Lifecycle
1. In namespace `ckad-w7d4`, PVC `data-claim` is bound to a PersistentVolume.
2. Deploy a Pod named `state-writer`:
   - Image: `busybox:1.36`
   - Mount `data-claim` at `/var/storage`.
   - Command: `sh -c "echo 'PERSISTED_STATE_OK' > /var/storage/state.txt && sleep 3600"`
3. Verify `/var/storage/state.txt` is written.
4. Delete `state-writer`.
5. Deploy a second Pod named `state-reader`:
   - Image: `busybox:1.36`
   - Mount same `data-claim` at `/var/storage`.
   - Command: `sleep 3600`
6. Verify `state-reader` successfully reads `"PERSISTED_STATE_OK"` from `/var/storage/state.txt`.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w7d4 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_STORAGE" | kubectl apply -f -
apiVersion: v1
kind: PersistentVolume
metadata:
  name: persist-test-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
  - ReadWriteOnce
  storageClassName: persist-class
  hostPath:
    path: /mnt/persist-data
    type: DirectoryOrCreate
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - node01
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-claim
  namespace: ckad-w7d4
spec:
  storageClassName: persist-class
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
EOF_STORAGE
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W7D4: Data Persistence in ckad-w7d4..."

READER_PHASE=$(ssh controlplane 'kubectl get pod state-reader -n ckad-w7d4 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')
CONTENT=$(ssh controlplane 'kubectl exec state-reader -n ckad-w7d4 -- cat /var/storage/state.txt 2>/dev/null || echo ""')

if [ "$READER_PHASE" == "Running" ] && [[ "$CONTENT" =~ "PERSISTED_STATE_OK" ]]; then
  echo -e "\033[0;32m[PASS] Data persisted across pod deletion and read by state-reader.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] state-reader phase: $READER_PHASE | Content: '$CONTENT'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Data Persistence
```bash
ssh controlplane '
# 1. Run writer pod:
cat << "EOF_WRITER" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: state-writer
  namespace: ckad-w7d4
spec:
  volumes:
  - name: storage-vol
    persistentVolumeClaim:
      claimName: data-claim
  containers:
  - name: writer
    image: busybox:1.36
    command: ["sh", "-c", "echo 'PERSISTED_STATE_OK' > /var/storage/state.txt && sleep 10"]
    volumeMounts:
    - name: storage-vol
      mountPath: /var/storage
EOF_WRITER

kubectl wait --for=condition=Ready pod/state-writer -n ckad-w7d4 --timeout=30s 2>/dev/null && sleep 2
kubectl delete pod state-writer -n ckad-w7d4 --force --grace-period=0

# 2. Run reader pod:
cat << "EOF_READER" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: state-reader
  namespace: ckad-w7d4
spec:
  volumes:
  - name: storage-vol
    persistentVolumeClaim:
      claimName: data-claim
  containers:
  - name: reader
    image: busybox:1.36
    command: ["sleep", "3600"]
    volumeMounts:
    - name: storage-vol
      mountPath: /var/storage
EOF_READER
'
```""",
        "reset": """ssh controlplane '
kubectl delete namespace ckad-w7d4 --ignore-not-found
kubectl delete pv persist-test-pv --ignore-not-found
'"""
    },
    {
        "day": 5,
        "date": "2026-11-27",
        "title": "StorageClasses & Delayed Volume Binding",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Create StorageClass with WaitForFirstConsumer
1. Create a StorageClass named `delayed-storage`:
   - `provisioner`: `kubernetes.io/no-provisioner`
   - `volumeBindingMode`: `WaitForFirstConsumer`
2. In namespace `ckad-w7d5`, create PVC `delayed-pvc`:
   - `storageClassName`: `delayed-storage`
   - Requests: `1Gi`
   - `accessModes`: `ReadWriteOnce`
3. Verify that `delayed-pvc` remains in status `Pending` (because no consuming pod has been scheduled).""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w7d5 --dry-run=client -o yaml | kubectl apply -f -
kubectl delete sc delayed-storage --ignore-not-found
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W7D5: StorageClasses in ckad-w7d5..."

MODE=$(ssh controlplane 'kubectl get sc delayed-storage -o jsonpath="{.volumeBindingMode}" 2>/dev/null || echo ""')
PVC_STATUS=$(ssh controlplane 'kubectl get pvc delayed-pvc -n ckad-w7d5 -o jsonpath="{.status.phase}" 2>/dev/null || echo "Missing"')

if [ "$MODE" == "WaitForFirstConsumer" ] && [ "$PVC_STATUS" == "Pending" ]; then
  echo -e "\033[0;32m[PASS] StorageClass configured with WaitForFirstConsumer and PVC pending consumer scheduling.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] volumeBindingMode: '$MODE' (expected WaitForFirstConsumer) | PVC status: '$PVC_STATUS' (expected Pending).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: StorageClasses
```bash
ssh controlplane 'cat << "EOF_SC" | kubectl apply -f -
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: delayed-storage
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: delayed-pvc
  namespace: ckad-w7d5
spec:
  storageClassName: delayed-storage
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
EOF_SC
'
```""",
        "reset": """ssh controlplane '
kubectl delete namespace ckad-w7d5 --ignore-not-found
kubectl delete sc delayed-storage --ignore-not-found
'"""
    },
    {
        "day": 6,
        "date": "2026-11-28",
        "title": "StatefulSets & VolumeClaimTemplates",
        "diff": "Hard",
        "time": "30m",
        "tasks": """### Task 1: Deploy Clustered StatefulSet
1. In namespace `ckad-w7d6`, create a Headless Service named `redis-service` (`clusterIP: None`) on port `6379`.
2. Deploy a StatefulSet named `redis-cluster`:
   - `serviceName`: `redis-service`
   - Replicas: `2`
   - Image: `redis:alpine`
   - Container port: `6379`
   - `volumeClaimTemplates`: name `redis-data`, accessModes `ReadWriteOnce`, requests `200Mi`, `storageClassName: redis-sc`, mounted at `/data`.
3. Verify both replicas `redis-cluster-0` and `redis-cluster-1` are `Running` and both generate their own PVC.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w7d6 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_PV" | kubectl apply -f -
apiVersion: v1
kind: PersistentVolume
metadata:
  name: redis-pv-0
spec:
  capacity:
    storage: 500Mi
  accessModes:
  - ReadWriteOnce
  storageClassName: redis-sc
  hostPath:
    path: /mnt/redis-0
    type: DirectoryOrCreate
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: redis-pv-1
spec:
  capacity:
    storage: 500Mi
  accessModes:
  - ReadWriteOnce
  storageClassName: redis-sc
  hostPath:
    path: /mnt/redis-1
    type: DirectoryOrCreate
EOF_PV
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W7D6: StatefulSets in ckad-w7d6..."

REPLICAS=$(ssh controlplane 'kubectl get statefulset redis-cluster -n ckad-w7d6 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
PVC_0=$(ssh controlplane 'kubectl get pvc redis-data-redis-cluster-0 -n ckad-w7d6 -o jsonpath="{.metadata.name}" 2>/dev/null || echo ""')
PVC_1=$(ssh controlplane 'kubectl get pvc redis-data-redis-cluster-1 -n ckad-w7d6 -o jsonpath="{.metadata.name}" 2>/dev/null || echo ""')

if [ "$REPLICAS" -eq 2 ] && [ -n "$PVC_0" ] && [ -n "$PVC_1" ]; then
  echo -e "\\033[0;32m[PASS] StatefulSet redis-cluster 2/2 ready with dedicated volumeClaimTemplates PVCs.\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Ready replicas: $REPLICAS/2 | PVC 0: '\''$PVC_0'\'' | PVC 1: '\''$PVC_1'\''\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: StatefulSets
```bash
ssh controlplane 'cat << "EOF_STS" | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: redis-service
  namespace: ckad-w7d6
spec:
  clusterIP: None
  selector:
    app: redis-node
  ports:
  - port: 6379
    targetPort: 6379
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: redis-cluster
  namespace: ckad-w7d6
spec:
  serviceName: redis-service
  replicas: 2
  selector:
    matchLabels:
      app: redis-node
  template:
    metadata:
      labels:
        app: redis-node
    spec:
      containers:
      - name: redis
        image: redis:alpine
        ports:
        - containerPort: 6379
        volumeMounts:
        - name: redis-data
          mountPath: /data
  volumeClaimTemplates:
  - metadata:
      name: redis-data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: redis-sc
      resources:
        requests:
          storage: 200Mi
EOF_STS

kubectl rollout status statefulset/redis-cluster -n ckad-w7d6 --timeout=60s 2>/dev/null || true
'
```""",
        "reset": """ssh controlplane '
kubectl delete namespace ckad-w7d6 --ignore-not-found
kubectl delete pv redis-pv-0 redis-pv-1 --ignore-not-found
'"""
    }
]
