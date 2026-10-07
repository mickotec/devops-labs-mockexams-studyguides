"""
Dedicated CKA Mock Exam Lab Definitions.
"""

MOCK_LABS = [
    {
        "lab_id": 'mock-cka-1',
        "track": 'CKA',
        "date": '2026-11-19',
        "title": 'CKA Full-Scale Timed Mock Exam 1',
        "diff": 'Hard (Mock Exam Simulation)',
        "time": '120m',
        "tasks": """# CKA Full-Scale Timed Mock Exam 1

**Passing Score:** 66% (Official Linux Foundation Threshold)  
**Time Limit:** 120 minutes  
**Target Cluster:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)

---

### Linux Foundation Official Domain Weights:
1. **Storage (10%)**
   - Implement storage classes and dynamic volume provisioning
   - Configure volume types, access modes and reclaim policies
   - Manage persistent volumes and persistent volume claims
2. **Troubleshooting (30%)**
   - Troubleshoot clusters and nodes
   - Troubleshoot cluster components
   - Monitor cluster and application resource usage
   - Manage and evaluate container output streams
   - Troubleshoot services and networking
3. **Workloads & Scheduling (15%)**
   - Understand application deployments and how to perform rolling update and rollbacks
   - Use ConfigMaps and Secrets to configure applications
   - Configure workload autoscaling
   - Understand the primitives used to create robust, self-healing, application deployments
   - Configure Pod admission and scheduling (limits, node affinity, etc.)
4. **Cluster Architecture, Installation & Configuration (25%)**
   - Manage role based access control (RBAC)
   - Prepare underlying infrastructure for installing a Kubernetes cluster
   - Create and manage Kubernetes clusters using kubeadm
   - Manage the lifecycle of Kubernetes clusters
   - Implement and configure a highly-available control plane
   - Use Helm and Kustomize to install cluster components
   - Understand extension interfaces (CNI, CSI, CRI, etc.)
   - Understand CRDs, install and configure operators
5. **Services & Networking (20%)**
   - Understand connectivity between Pods
   - Define and enforce Network Policies
   - Use ClusterIP, NodePort, LoadBalancer service types and endpoints
   - Use the Gateway API to manage Ingress traffic
   - Know how to use Ingress controllers and Ingress resources
   - Understand and use CoreDNS

---

### Questions Overview:

#### Domain: Cluster Architecture, Installation & Configuration (25% Weight - 4 Questions, 6.25% each)
- **Q1:** An administrative maintenance window is scheduled on the Kubernetes control plane. Before performing cluster maintenance, you must capture a point-in-time snapshot of the ETCD database:
  - Connect to the `controlplane` node.
  - Save the database snapshot file to `/opt/backup/etcd-backup.db`.
  - Authenticate against the active ETCD datastore using the appropriate trusted CA, server certificate, and private key located on the control plane.
  - Ensure the snapshot file is created, valid, and non-empty.
- **Q2:** An external compliance auditor named `jane` needs restricted access to inspect workloads in namespace `mock-cka-1-q2`:
  - In namespace `mock-cka-1-q2`, create a Role named `pod-reader`.
  - Configure the Role to grant permissions for `get`, `list`, and `watch` actions on `pods` resources.
  - In namespace `mock-cka-1-q2`, create a RoleBinding named `read-pods` binding user `jane` to the `pod-reader` Role.
- **Q3:** Node monitoring agents operating across all cluster nodes require cluster-wide visibility into node statuses:
  - Create a ClusterRole named `node-watcher` granting `get`, `list`, and `watch` permissions on `nodes` resources.
  - Create a ClusterRoleBinding named `node-watchers-binding` to bind the `node-watcher` ClusterRole to the group `system:nodes`.
- **Q4:** Developers on the platform team require an isolated kubeconfig file to test programmatic API access against the cluster:
  - Create a standalone kubeconfig file at `/opt/k8s/custom-kubeconfig`.
  - Define a cluster entry named `k8s-cluster` targeting server endpoint `https://172.16.16.210:6443`.
  - Define a user entry named `dev-user`.
  - Define a context named `dev-context` linking cluster `k8s-cluster` and user `dev-user`.
  - Set the `current-context` in the file to `dev-context`.

#### Domain: Workloads & Scheduling (15% Weight - 3 Questions, 5.0% each)
- **Q5:** An application upgrade deployed in namespace `mock-cka-1-q5` introduced unexpected regressions and must be reverted to its previous stable release:
  - In namespace `mock-cka-1-q5`, deploy a Deployment named `nginx-deploy` with 3 replicas using container image `nginx:1.24-alpine`.
  - Update the deployment image to `nginx:1.25-alpine` and wait for the rollout to complete.
  - Roll back the deployment to revision 1 so that the workload reverts to image `nginx:1.24-alpine`.
  - Verify all pods in `nginx-deploy` are running image `nginx:1.24-alpine`.
- **Q6:** A legacy application service writes operational output to a local log file, and a co-located sidecar container is required to stream these entries in real time:
  - In namespace `mock-cka-1-q6`, create a Pod named `multi-container-pod`.
  - Define a shared volume named `shared-data` using `emptyDir: {}`, mounted at path `/var/log` in both containers.
  - Primary container named `app` (image: `busybox:1.36`): continuously writes timestamped logs to `/var/log/app.log`.
  - Sidecar container named `sidecar` (image: `busybox:1.36`): streams the log file using `tail -f /var/log/app.log`.
  - Ensure both containers achieve `Running` state (2/2 Ready).
- **Q7:** A microservice workload requires runtime parameters and credentials injected dynamically without hardcoding them into the container image:
  - In namespace `mock-cka-1-q7`, create a ConfigMap named `app-config` containing entry `ENV_MODE=production`.
  - In the same namespace, create a Secret named `app-secret` containing entry `API_KEY=secret123`.
  - Create a Pod named `config-pod` (image: `busybox:1.36`, command: `sleep 3600`) that imports these values as environment variables:
    - Variable `CONFIG_VAL` populated from ConfigMap `app-config` (key `ENV_MODE`).
    - Variable `SECRET_VAL` populated from Secret `app-secret` (key `API_KEY`).
  - Verify the pod reaches `Running` state.

#### Domain: Services & Networking (20% Weight - 3 Questions, 6.67% each)
- **Q8:** Both internal cluster clients and external nodes require network routing to access deployment `web` in namespace `mock-cka-1-q8`:
  - In namespace `mock-cka-1-q8`, create a `ClusterIP` service named `web-svc` exposing port 80 targeting deployment `web`.
  - In the same namespace, create a `NodePort` service named `web-nodeport` exposing port 80 with static nodePort `31555` targeting deployment `web`.
  - Verify that both services resolve active endpoint addresses.
- **Q9:** Network security policy mandates strict ingress isolation for web tier pods in namespace `mock-cka-1-q9`:
  - In namespace `mock-cka-1-q9`, create a NetworkPolicy named `allow-client`.
  - The policy must apply ingress rules to pods labeled `app=nginx`.
  - Allow incoming connections only from pods labeled `role=client`.
  - Ensure all other ingress traffic to pods labeled `app=nginx` is denied.
- **Q10:** Validate internal cluster service discovery and name resolution provided by CoreDNS:
  - Perform a DNS lookup for the fully-qualified domain name of the default Kubernetes service: `kubernetes.default.svc.cluster.local`.
  - Save the command output containing the query resolution details and resolved IP address to `/opt/k8s/dns-test.txt`.

#### Domain: Storage (10% Weight - 2 Questions, 5.0% each)
- **Q11:** A database pod requires dedicated host-backed persistent volume storage:
  - Create a PersistentVolume named `mock-pv` with capacity `1Gi`, access mode `ReadWriteOnce`, and hostPath storage path `/mnt/mock-data`.
  - In namespace `mock-cka-1-q11`, create a PersistentVolumeClaim named `mock-pvc` requesting `1Gi` with access mode `ReadWriteOnce`.
  - Ensure `mock-pv` and `mock-pvc` bind successfully (`Bound` status).
- **Q12:** An application workload requires mounted persistent storage to store data across pod restarts:
  - In namespace `mock-cka-1-q12`, create a Pod named `storage-pod` using image `busybox:1.36`.
  - Mount the PersistentVolumeClaim `mock-pvc` at mount path `/data`.
  - Ensure the file `/data/status.txt` on the mounted volume contains the string `storage-ok`.
  - Verify the pod is in `Running` state.

#### Domain: Troubleshooting (30% Weight - 5 Questions, 6.0% each)
- **Q13:** The control plane pod scheduler has failed, preventing pending workloads from being assigned to cluster nodes:
  - Connect to the `controlplane` node.
  - Diagnose why the static pod `kube-scheduler-controlplane` in namespace `kube-system` is failing to run.
  - Review the static pod manifest `/etc/kubernetes/manifests/kube-scheduler.yaml` and identify the corrupted configuration parameter.
  - Correct the manifest so the scheduler references the valid administrative configuration file `/etc/kubernetes/scheduler.conf`.
  - Confirm that `kube-scheduler-controlplane` restarts and reaches `Running` state (1/1 Ready).
- **Q14:** An application deployment in namespace `mock-cka-1-q14` contains a pod stuck in an unstable crash loop:
  - Inspect pod `broken-worker` in namespace `mock-cka-1-q14` to determine why it is crash-looping.
  - Fix the container entrypoint command so that the container executes without error (e.g. running a persistent sleep or valid shell process).
  - Ensure `broken-worker` reaches and maintains `Running` state.
- **Q15:** Worker node `node01` was previously placed in maintenance mode and cannot accept newly scheduled workloads:
  - Check the scheduling status of all cluster nodes.
  - Return `node01` to active service by uncordoning it so it can accept pod scheduling.
  - Confirm `node01` is marked schedulable.
- **Q16:** Clients attempting to communicate with service `api-service` in namespace `mock-cka-1-q16` are experiencing connection timeouts:
  - Inspect the configuration of service `api-service` and its backend endpoints in namespace `mock-cka-1-q16`.
  - Compare the service selector against the labels of the running backend `api` pods.
  - Update the selector so it correctly matches label `app=api-v1`.
  - Verify that `api-service` now maps to active endpoint IP addresses.
- **Q17:** Pods belonging to deployment `db-client` in namespace `mock-cka-1-q17` fail on startup, resulting in 0/1 ready replicas:
  - Inspect the pod events and container logs for `db-client` to diagnose the startup failure.
  - Update the deployment specification to supply the required environment variable `DB_HOST` with value `10.0.0.1`.
  - Verify that the deployment completes its rollout and achieves 1/1 ready replicas.""",
        "setup": """# Setup CKA Mock Exam 1
ssh controlplane '
for q in q2 q3 q4 q5 q6 q7 q8 q9 q11 q12 q14 q16 q17; do
  kubectl create ns mock-cka-1-$q 2>/dev/null || true
  kubectl delete deploy,pod,svc,netpol,pvc,role,rolebinding,sa --all -n mock-cka-1-$q --grace-period=0 --force 2>/dev/null || true
done

# Q8 deployment
kubectl create deploy web -n mock-cka-1-q8 --image=nginx:alpine --replicas=2

# Q9 pods
kubectl run nginx -n mock-cka-1-q9 --image=nginx:alpine --labels=app=nginx
kubectl run client -n mock-cka-1-q9 --image=busybox:1.36 --labels=role=client -- sleep 3600

# Q11 host directory
sudo mkdir -p /mnt/mock-data && sudo chmod 777 /mnt/mock-data

# Q13 broken scheduler
if [ ! -f /etc/kubernetes/kube-scheduler.yaml.bak ]; then
  sudo cp /etc/kubernetes/manifests/kube-scheduler.yaml /etc/kubernetes/kube-scheduler.yaml.bak
fi
sudo sed -i "s|--kubeconfig=.*|--kubeconfig=/etc/kubernetes/scheduler-broken.conf|" /etc/kubernetes/manifests/kube-scheduler.yaml
CID=$(sudo crictl ps -q --name kube-scheduler 2>/dev/null || true)
if [ -n "$CID" ]; then
  sudo crictl stop "$CID" 2>/dev/null || true
  sudo crictl rm "$CID" 2>/dev/null || true
fi
sudo systemctl restart kubelet

# Q14 crash loop pod
cat << "EOF" | kubectl apply -n mock-cka-1-q14 -f -
apiVersion: v1
kind: Pod
metadata:
  name: broken-worker
spec:
  containers:
  - name: worker
    image: busybox:1.36
    command: ["sh", "-c", "sleep invalid_duration"]
EOF

# Q15 cordon node01
kubectl cordon node01 2>/dev/null || true

# Q16 broken service selector
kubectl create deploy api -n mock-cka-1-q16 --image=nginx:alpine --replicas=2
kubectl label pods -n mock-cka-1-q16 -l app=api app=api-v1 --overwrite
cat << "EOF" | kubectl apply -n mock-cka-1-q16 -f -
apiVersion: v1
kind: Service
metadata:
  name: api-service
spec:
  selector:
    app: api-broken-v2
  ports:
  - port: 80
    targetPort: 80
EOF

# Q17 missing env var deployment
cat << "EOF" | kubectl apply -n mock-cka-1-q17 -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: db-client
spec:
  replicas: 1
  selector:
    matchLabels:
      app: db-client
  template:
    metadata:
      labels:
        app: db-client
    spec:
      containers:
      - name: client
        image: busybox:1.36
        command: ["sh", "-c", "if [ -z $DB_HOST ]; then echo Missing DB_HOST; exit 1; else sleep 3600; fi"]
EOF

sudo mkdir -p /opt/backup /opt/k8s && sudo chmod 777 /opt/backup /opt/k8s
rm -f /opt/backup/etcd-backup.db /opt/k8s/custom-kubeconfig /opt/k8s/dns-test.txt
'""",
        "verify": """# Linux Foundation CKA Domain Tracking
SCORE_STOR=0; TOTAL_STOR=2       # 10%
SCORE_TROUBLE=0; TOTAL_TROUBLE=5   # 30%
SCORE_WORKLOAD=0; TOTAL_WORKLOAD=3 # 15%
SCORE_CLUSTER=0; TOTAL_CLUSTER=4   # 25%
SCORE_SVC=0; TOTAL_SVC=3           # 20%
TOTAL_PASSED=0; TOTAL_QUESTIONS=17
SCORE=0; TOTAL=17

echo -e "${BOLD}Evaluating CKA Mock Exam 1 against Linux Foundation Domain Weights...${NC}"

# Q1: ETCD Snapshot (Cluster Architecture - 25%)
if ssh controlplane 'sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-backup.db --write-out=table 2>/dev/null | grep -qiE "REVISION|TOTAL KEYS"'; then
  echo -e "${GREEN}[PASS] Q1: ETCD snapshot verified.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q1: /opt/backup/etcd-backup.db missing or invalid.${NC}"
fi

# Q2: RBAC Role & Binding (Cluster Architecture - 25%)
if ssh controlplane 'kubectl get rolebinding read-pods -n mock-cka-1-q2 -o jsonpath="{.roleRef.name}" 2>/dev/null | grep -qw "pod-reader"'; then
  echo -e "${GREEN}[PASS] Q2: RBAC pod-reader Role and read-pods RoleBinding verified.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q2: RoleBinding read-pods or Role pod-reader missing.${NC}"
fi

# Q3: ClusterRole & Binding (Cluster Architecture - 25%)
if ssh controlplane 'kubectl get clusterrolebinding node-watchers-binding -o jsonpath="{.roleRef.name}" 2>/dev/null | grep -qw "node-watcher"'; then
  echo -e "${GREEN}[PASS] Q3: ClusterRole node-watcher and Binding verified.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q3: ClusterRoleBinding node-watchers-binding missing.${NC}"
fi

# Q4: Kubeconfig (Cluster Architecture - 25%)
if ssh controlplane 'test -f /opt/k8s/custom-kubeconfig' && ssh controlplane 'grep -q "dev-context" /opt/k8s/custom-kubeconfig'; then
  echo -e "${GREEN}[PASS] Q4: /opt/k8s/custom-kubeconfig verified with dev-context.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q4: custom-kubeconfig missing or invalid.${NC}"
fi

# Q5: Deployment rollback (Workloads & Scheduling - 15%)
IMG5=$(ssh controlplane 'kubectl get deploy nginx-deploy -n mock-cka-1-q5 -o jsonpath="{.spec.template.spec.containers[0].image}" 2>/dev/null || echo "None"')
if [ "$IMG5" == "nginx:1.24-alpine" ]; then
  echo -e "${GREEN}[PASS] Q5: nginx-deploy rolled back to nginx:1.24-alpine.${NC}"; SCORE_WORKLOAD=$((SCORE_WORKLOAD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q5: nginx-deploy image is $IMG5 (expected nginx:1.24-alpine).${NC}"
fi

# Q6: Sidecar Pod (Workloads & Scheduling - 15%)
VOL6=$(ssh controlplane 'kubectl get pod multi-container-pod -n mock-cka-1-q6 -o jsonpath="{.spec.volumes[0].name}" 2>/dev/null || echo "None"')
C6=$(ssh controlplane 'kubectl get pod multi-container-pod -n mock-cka-1-q6 -o jsonpath="{.spec.containers[*].name}" 2>/dev/null || echo "None"')
if echo "$C6" | grep -qw "app" && echo "$C6" | grep -qw "sidecar" && [ "$VOL6" == "shared-data" ]; then
  echo -e "${GREEN}[PASS] Q6: Multi-container pod with shared volume verified.${NC}"; SCORE_WORKLOAD=$((SCORE_WORKLOAD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q6: multi-container-pod containers: $C6, volume: $VOL6.${NC}"
fi

# Q7: ConfigMap and Secret env injection (Workloads & Scheduling - 15%)
ENV7=$(ssh controlplane 'kubectl get pod config-pod -n mock-cka-1-q7 -o jsonpath="{.spec.containers[0].env[*].name}" 2>/dev/null || echo "None"')
if echo "$ENV7" | grep -qw "CONFIG_VAL" && echo "$ENV7" | grep -qw "SECRET_VAL"; then
  echo -e "${GREEN}[PASS] Q7: Pod config-pod env injection verified.${NC}"; SCORE_WORKLOAD=$((SCORE_WORKLOAD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q7: config-pod env vars: $ENV7.${NC}"
fi

# Q8: Services ClusterIP and NodePort (Services & Networking - 20%)
SVC8_C=$(ssh controlplane 'kubectl get svc web-svc -n mock-cka-1-q8 -o jsonpath="{.spec.type}" 2>/dev/null || echo "None"')
SVC8_N=$(ssh controlplane 'kubectl get svc web-nodeport -n mock-cka-1-q8 -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo "0"')
if [ "$SVC8_C" == "ClusterIP" ] && [ "$SVC8_N" == "31555" ]; then
  echo -e "${GREEN}[PASS] Q8: Services web-svc (ClusterIP) and web-nodeport (31555) verified.${NC}"; SCORE_SVC=$((SCORE_SVC + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q8: ClusterIP=$SVC8_C, NodePort=$SVC8_N.${NC}"
fi

# Q9: NetworkPolicy (Services & Networking - 20%)
NP9=$(ssh controlplane 'kubectl get netpol allow-client -n mock-cka-1-q9 -o jsonpath="{.metadata.name}" 2>/dev/null || echo "None"')
if [ "$NP9" == "allow-client" ]; then
  echo -e "${GREEN}[PASS] Q9: NetworkPolicy allow-client verified.${NC}"; SCORE_SVC=$((SCORE_SVC + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q9: NetworkPolicy allow-client missing.${NC}"
fi

# Q10: CoreDNS query test (Services & Networking - 20%)
DNS10=$(ssh controlplane 'cat /opt/k8s/dns-test.txt 2>/dev/null || true')
if echo "$DNS10" | grep -qi "kubernetes.default"; then
  echo -e "${GREEN}[PASS] Q10: CoreDNS resolution verified in /opt/k8s/dns-test.txt.${NC}"; SCORE_SVC=$((SCORE_SVC + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q10: /opt/k8s/dns-test.txt missing or lacks resolution.${NC}"
fi

# Q11: PersistentVolume & PVC (Storage - 10%)
PV11=$(ssh controlplane 'kubectl get pv mock-pv -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
PVC11=$(ssh controlplane 'kubectl get pvc mock-pvc -n mock-cka-1-q11 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PV11" == "Bound" ] && [ "$PVC11" == "Bound" ]; then
  echo -e "${GREEN}[PASS] Q11: PersistentVolume mock-pv and PVC mock-pvc Bound.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q11: PV=$PV11, PVC=$PVC11.${NC}"
fi

# Q12: Storage Pod mounting PVC (Storage - 10%)
POD12=$(ssh controlplane 'kubectl get pod storage-pod -n mock-cka-1-q12 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
FILE12=$(ssh controlplane 'cat /mnt/mock-data/status.txt 2>/dev/null || true')
if [ "$POD12" == "Running" ] && [ "$FILE12" == "storage-ok" ]; then
  echo -e "${GREEN}[PASS] Q12: Pod storage-pod Running and wrote storage-ok.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q12: storage-pod phase: $POD12, file content: '$FILE12'.${NC}"
fi

# Q13: Kube-scheduler troubleshooting (Troubleshooting - 30%)
SCHED13=$(ssh controlplane 'kubectl get pods -n kube-system -l component=kube-scheduler -o jsonpath="{.items[0].status.phase}" 2>/dev/null || echo "None"')
SCHED13_CONF=$(ssh controlplane 'grep "--kubeconfig" /etc/kubernetes/manifests/kube-scheduler.yaml 2>/dev/null || true')
if [ "$SCHED13" == "Running" ] && echo "$SCHED13_CONF" | grep -q "scheduler.conf" && ! echo "$SCHED13_CONF" | grep -q "broken"; then
  echo -e "${GREEN}[PASS] Q13: kube-scheduler repaired and Running.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q13: kube-scheduler status: $SCHED13, config: $SCHED13_CONF (expected scheduler.conf).${NC}"
fi

# Q14: CrashLoopBackOff fix (Troubleshooting - 30%)
POD14=$(ssh controlplane 'kubectl get pod broken-worker -n mock-cka-1-q14 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
CMD14=$(ssh controlplane 'kubectl get pod broken-worker -n mock-cka-1-q14 -o jsonpath="{.spec.containers[0].command}" 2>/dev/null || true')
if [ "$POD14" == "Running" ] && ! echo "$CMD14" | grep -q "invalid"; then
  echo -e "${GREEN}[PASS] Q14: broken-worker repaired and Running.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q14: broken-worker status: $POD14.${NC}"
fi

# Q15: Uncordon node01 (Troubleshooting - 30%)
SCHED15=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.spec.unschedulable}" 2>/dev/null || echo "false"')
if [ "$SCHED15" != "true" ]; then
  echo -e "${GREEN}[PASS] Q15: node01 is uncordoned and schedulable.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q15: node01 is still cordoned.${NC}"
fi

# Q16: Broken service selector fix (Troubleshooting - 30%)
EP16=$(ssh controlplane 'kubectl get endpoints api-service -n mock-cka-1-q16 -o jsonpath="{.subsets[0].addresses[0].ip}" 2>/dev/null || echo "None"')
SEL16=$(ssh controlplane 'kubectl get svc api-service -n mock-cka-1-q16 -o jsonpath="{.spec.selector.app}" 2>/dev/null || echo "None"')
if [ "$EP16" != "None" ] && [ "$SEL16" == "api-v1" ]; then
  echo -e "${GREEN}[PASS] Q16: Service api-service selector repaired with active endpoints.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q16: api-service selector: $SEL16 (expected api-v1).${NC}"
fi

# Q17: Deployment missing env var fix (Troubleshooting - 30%)
READY17=$(ssh controlplane 'kubectl get deploy db-client -n mock-cka-1-q17 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$READY17" == "1" ]; then
  echo -e "${GREEN}[PASS] Q17: Deployment db-client healthy with 1/1 ready replicas.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q17: db-client ready replicas: $READY17.${NC}"
fi""",
        "solution": """### Official Walkthrough & Solution Guide

#### Q1: ETCD Snapshot
```bash
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   snapshot save /opt/backup/etcd-backup.db
```

#### Q2: Role & RoleBinding
```bash
kubectl create role pod-reader --verb=get,list,watch --resource=pods -n mock-cka-1-q2
kubectl create rolebinding read-pods --role=pod-reader --user=jane -n mock-cka-1-q2
```

#### Q3: ClusterRole & ClusterRoleBinding
```bash
kubectl create clusterrole node-watcher --verb=get,list,watch --resource=nodes
kubectl create clusterrolebinding node-watchers-binding --clusterrole=node-watcher --group=system:nodes
```

#### Q4: Custom Kubeconfig
```bash
kubectl config --kubeconfig=/opt/k8s/custom-kubeconfig set-cluster k8s-cluster --server=https://172.16.16.210:6443 --insecure-skip-tls-verify=true
kubectl config --kubeconfig=/opt/k8s/custom-kubeconfig set-credentials dev-user --token=mock-token
kubectl config --kubeconfig=/opt/k8s/custom-kubeconfig set-context dev-context --cluster=k8s-cluster --user=dev-user
kubectl config --kubeconfig=/opt/k8s/custom-kubeconfig use-context dev-context
```

#### Q5: Deployment Rollback
```bash
kubectl set image deploy/nginx-deploy nginx=nginx:1.25-alpine -n mock-cka-1-q5
kubectl rollout undo deploy/nginx-deploy -n mock-cka-1-q5 --to-revision=1
```

#### Q6: Sidecar Pod
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-pod
  namespace: mock-cka-1-q6
spec:
  volumes:
  - name: shared-data
    emptyDir: {}
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo app running >> /var/log/app.log; sleep 2; done"]
    volumeMounts:
    - name: shared-data
      mountPath: /var/log
  - name: sidecar
    image: busybox:1.36
    command: ["sh", "-c", "tail -f /var/log/app.log"]
    volumeMounts:
    - name: shared-data
      mountPath: /var/log
```

#### Q7: ConfigMap & Secret Pod
```bash
kubectl create configmap app-config --from-literal=ENV_MODE=production -n mock-cka-1-q7
kubectl create secret generic app-secret --from-literal=API_KEY=secret123 -n mock-cka-1-q7
```
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: config-pod
  namespace: mock-cka-1-q7
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sleep", "3600"]
    env:
    - name: CONFIG_VAL
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: ENV_MODE
    - name: SECRET_VAL
      valueFrom:
        secretKeyRef:
          name: app-secret
          key: API_KEY
```

#### Q8: Services Exposure
```bash
kubectl expose deploy web -n mock-cka-1-q8 --name=web-svc --port=80
kubectl expose deploy web -n mock-cka-1-q8 --name=web-nodeport --type=NodePort --port=80
kubectl patch svc web-nodeport -n mock-cka-1-q8 --type='json' -p='[{"op":"replace","path":"/spec/ports/0/nodePort","value":31555}]'
```

#### Q9: NetworkPolicy
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-client
  namespace: mock-cka-1-q9
spec:
  podSelector:
    matchLabels:
      app: nginx
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: client
```

#### Q10: CoreDNS Query
```bash
ssh controlplane 'kubectl run dns-test --image=busybox:1.36 --restart=Never -- nslookup kubernetes.default.svc.cluster.local > /opt/k8s/dns-test.txt; kubectl delete pod dns-test'
```

#### Q11 & Q12: Storage PV/PVC & Pod
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mock-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /mnt/mock-data
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mock-pvc
  namespace: mock-cka-1-q11
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```
In Q12, create pod mounting `mock-pvc` at `/data` and write `storage-ok` to `/data/status.txt`.

#### Q13: Scheduler Repair
On `controlplane`:
`sudo sed -i 's|scheduler-broken.conf|scheduler.conf|' /etc/kubernetes/manifests/kube-scheduler.yaml`
`sudo systemctl restart kubelet`

#### Q14: CrashLoop Repair
Edit `broken-worker` command to `["sh", "-c", "sleep 3600"]`.

#### Q15: Uncordon Node
`kubectl uncordon node01`

#### Q16: Service Selector Repair
`kubectl patch svc api-service -n mock-cka-1-q16 --type='json' -p='[{"op":"replace","path":"/spec/selector/app","value":"api-v1"}]'`

#### Q17: Deployment Environment Variable
`kubectl set env deploy/db-client -n mock-cka-1-q17 DB_HOST=10.0.0.1`""",
        "reset": """ssh controlplane '
if [ -f /etc/kubernetes/kube-scheduler.yaml.bak ]; then
  sudo mv -f /etc/kubernetes/kube-scheduler.yaml.bak /etc/kubernetes/manifests/kube-scheduler.yaml
fi
sudo sed -i "s/scheduler-broken\.conf/scheduler\.conf/g" /etc/kubernetes/manifests/kube-scheduler.yaml 2>/dev/null || true
sudo systemctl restart kubelet
kubectl uncordon node01 2>/dev/null || true
kubectl delete ns mock-cka-1-q2 mock-cka-1-q3 mock-cka-1-q4 mock-cka-1-q5 mock-cka-1-q6 mock-cka-1-q7 mock-cka-1-q8 mock-cka-1-q9 mock-cka-1-q11 mock-cka-1-q12 mock-cka-1-q14 mock-cka-1-q16 mock-cka-1-q17 --grace-period=0 --force --wait=false 2>/dev/null || true
kubectl delete pv mock-pv 2>/dev/null || true
kubectl delete clusterrole node-watcher 2>/dev/null || true
kubectl delete clusterrolebinding node-watchers-binding 2>/dev/null || true
sudo rm -rf /opt/backup/etcd-backup.db /opt/k8s/custom-kubeconfig /mnt/mock-data
'""",
    },
    {
        "lab_id": 'mock-cka-2',
        "track": 'CKA',
        "date": '2026-11-20',
        "title": 'CKA Full-Scale Timed Mock Exam 2',
        "diff": 'Hard (Mock Exam Simulation)',
        "time": '120m',
        "tasks": """# CKA Full-Scale Timed Mock Exam 2

**Passing Score:** 66% (Official Linux Foundation Threshold)  
**Time Limit:** 120 minutes  
**Target Cluster:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)

---

### Linux Foundation Official Domain Weights:
1. **Storage (10%)**
   - Implement storage classes and dynamic volume provisioning
   - Configure volume types, access modes and reclaim policies
   - Manage persistent volumes and persistent volume claims
2. **Troubleshooting (30%)**
   - Troubleshoot clusters and nodes
   - Troubleshoot cluster components
   - Monitor cluster and application resource usage
   - Manage and evaluate container output streams
   - Troubleshoot services and networking
3. **Workloads & Scheduling (15%)**
   - Understand application deployments and how to perform rolling update and rollbacks
   - Use ConfigMaps and Secrets to configure applications
   - Configure workload autoscaling
   - Understand the primitives used to create robust, self-healing, application deployments
   - Configure Pod admission and scheduling (limits, node affinity, etc.)
4. **Cluster Architecture, Installation & Configuration (25%)**
   - Manage role based access control (RBAC)
   - Prepare underlying infrastructure for installing a Kubernetes cluster
   - Create and manage Kubernetes clusters using kubeadm
   - Manage the lifecycle of Kubernetes clusters
   - Implement and configure a highly-available control plane
   - Use Helm and Kustomize to install cluster components
   - Understand extension interfaces (CNI, CSI, CRI, etc.)
   - Understand CRDs, install and configure operators
5. **Services & Networking (20%)**
   - Understand connectivity between Pods
   - Define and enforce Network Policies
   - Use ClusterIP, NodePort, LoadBalancer service types and endpoints
   - Use the Gateway API to manage Ingress traffic
   - Know how to use Ingress controllers and Ingress resources
   - Understand and use CoreDNS

---

### Questions Overview:

#### Domain: Cluster Architecture, Installation & Configuration (25% Weight - 4 Questions, 6.25% each)
- **Q1:** An external Prometheus monitoring agent needs administrative read access to scrape workload, service, and node telemetry across all namespaces:
  - In namespace `mock-cka-2-q1`, create a ServiceAccount named `monitoring-sa`.
  - Create a ClusterRole named `monitoring-role` that permits `get`, `list`, and `watch` verbs on `pods`, `services`, and `nodes`.
  - Create a ClusterRoleBinding named `monitoring-binding` binding the ServiceAccount `mock-cka-2-q1/monitoring-sa` to the ClusterRole `monitoring-role`.
- **Q2:** Cluster administrators must audit control plane certificate lifecycles to avoid unexpected outages due to expired TLS certificates:
  - Connect to the `controlplane` node.
  - Audit the expiration dates of all Kubernetes control plane certificates managed by `kubeadm`.
  - Save the complete certificate expiration table output to file `/opt/k8s/apiserver-expiry.txt`.
- **Q3:** An edge monitoring agent must run directly on worker node `node01` as a static pod, managed exclusively by the local kubelet rather than the cluster API server:
  - Connect to worker node `node01`.
  - Locate or configure the kubelet's static pod manifest directory (`/etc/kubernetes/manifests`).
  - Create a static pod manifest named `static-web.yaml` deploying a pod named `static-web` with container image `nginx:alpine`.
  - Verify from `controlplane` that `static-web-node01` appears in the cluster and reaches `Running` state.
- **Q4:** Worker node `node02` is scheduled for routine kernel maintenance. The administrator must safely evacuate existing workloads before re-enabling the node:
  - Safely drain node `node02`, ignoring daemonsets and allowing eviction of pods with emptyDir storage.
  - Once drained, simulate maintenance completion and return `node02` to active service by uncordoning it.
  - Verify that `node02` is `Ready` and schedulable (`unschedulable` is false).

#### Domain: Workloads & Scheduling (15% Weight - 3 Questions, 5.0% each)
- **Q5:** An application initialization routine must generate a shared greeting file before the main web service begins execution:
  - In namespace `mock-cka-2-q5`, create a Pod named `init-volume-pod`.
  - Define an `emptyDir` volume mounted at `/shared` in both the init container and main container.
  - Configure an `initContainer` (image: `busybox:1.36`) that writes the string `init-data` to `/shared/greeting.txt` and exits cleanly.
  - Configure the main container (image: `busybox:1.36`) to execute a process that reads `/shared/greeting.txt` and runs continuously (e.g., `sleep 3600`).
  - Verify the pod reaches `Running` state and the file content is present.
- **Q6:** An internal microservice needs automatic horizontal scaling to handle sudden traffic spikes without manual intervention:
  - In namespace `mock-cka-2-q6`, create a Deployment named `hpa-deployment` with 2 initial replicas (image: `nginx:alpine`), configuring a container CPU resource request of `100m`.
  - Create a HorizontalPodAutoscaler targeting `hpa-deployment` that maintains an average CPU utilization of `60%`, with a minimum of 2 replicas and a maximum of 8 replicas.
  - Verify the HPA is created and tracking the deployment.
- **Q7:** A cleanup task needs to run periodically on a recurring schedule, but must never run concurrently if a previous execution is still in progress:
  - In namespace `mock-cka-2-q7`, create a CronJob named `periodic-task`.
  - Set the schedule to run every 5 minutes (`*/5 * * * *`).
  - Use image `busybox:1.36` with command `date`.
  - Configure the concurrency policy to `Forbid` so concurrent job runs are blocked.
  - Set the pod restart policy to `OnFailure`.

#### Domain: Services & Networking (20% Weight - 3 Questions, 6.67% each)
- **Q8:** A distributed stateful database cluster requires direct individual pod network addressing via DNS without proxy routing:
  - In namespace `mock-cka-2-q8`, create a headless Service named `db-headless` (with `clusterIP: None`) targeting pods with label `app=db` on port 80.
  - Create a Deployment named `db-deployment` with 3 replicas using image `nginx:alpine` and pod label `app=db`.
  - Verify that all 3 replicas are ready and endpoints are created for `db-headless`.
- **Q9:** Cross-namespace traffic segmentation requires that backend database pods in `mock-cka-2-q9` reject all traffic except from pods in the dedicated frontend namespace:
  - In namespace `mock-cka-2-q9`, create a NetworkPolicy named `allow-frontend`.
  - Apply the policy to pods with label `role=backend`.
  - Allow ingress traffic exclusively from pods residing in namespace `mock-cka-2-q9-frontend`.
  - Verify the NetworkPolicy is active in namespace `mock-cka-2-q9`.
- **Q10:** Application pods need to reference an external database host through standard Kubernetes service discovery rather than hardcoding external DNS names:
  - In namespace `mock-cka-2-q10`, create an `ExternalName` service named `db-external`.
  - Direct traffic for this service to the external canonical name `database.example.com`.

#### Domain: Storage (10% Weight - 2 Questions, 5.0% each)
- **Q11:** A persistent data store requires a dedicated storage class, a static persistent volume on host storage, and an application pod to consume it:
  - Create a PersistentVolume named `manual-pv` with capacity `2Gi`, access mode `ReadWriteOnce`, storageClassName `manual`, and hostPath `/mnt/manual-data`.
  - In namespace `mock-cka-2-q11`, create a PersistentVolumeClaim named `manual-pvc` requesting `2Gi` with storageClassName `manual` and access mode `ReadWriteOnce`.
  - Deploy a Pod named `pv-pod` in namespace `mock-cka-2-q11` (image: `nginx:alpine`) mounting `manual-pvc` at `/data`.
  - Verify `manual-pv` binds to `manual-pvc` and `pv-pod` reaches `Running` state.
- **Q12:** An application pod requires configuration values, security tokens, and downward API pod metadata consolidated into a single unified directory:
  - In namespace `mock-cka-2-q12`, create ConfigMap `app-config` (`KEY1=val1`) and Secret `app-secret` (`PASS=secval`).
  - Create a Pod named `projected-volume-pod` using image `busybox:1.36` (command: `sleep 3600`).
  - Configure a projected volume mounted at directory `/projected` that combines:
    - Sources from ConfigMap `app-config`
    - Sources from Secret `app-secret`
    - Downward API field `metadata.name` projected to path `pod-name`
  - Verify `projected-volume-pod` reaches `Running` state.

#### Domain: Troubleshooting (30% Weight - 5 Questions, 6.0% each)
- **Q13:** Node `node02` has stopped registering heartbeat updates and the node status on the control plane is showing issues:
  - Connect to worker node `node02`.
  - Investigate why the node agent service (`kubelet`) is stopped or failing.
  - Resolve the issue and start the `kubelet` service so it is active and running.
  - Verify that `systemctl is-active kubelet` reports `active`.
- **Q14:** Deployment workloads on worker node `node01` are failing to schedule, and pod `pending-pod` in namespace `mock-cka-2-q14` remains stuck in `Pending` state:
  - Inspect the events and scheduling constraints on `pending-pod`.
  - Investigate the taints on cluster node `node01`.
  - Remove the obstructing taint `tier=special:NoSchedule` from `node01` (or apply the required toleration) so the pod can schedule.
  - Verify that `pending-pod` transitions to `Running` state.
- **Q15:** In namespace `mock-cka-2-q15`, pod `broken-logger` is failing immediately upon pod creation due to an invalid container entrypoint command:
  - Inspect the pod status and logs in namespace `mock-cka-2-q15`.
  - Reconfigure the pod specification so the container executes a valid background logging loop (such as `sh -c 'while true; do date; sleep 5; done'`).
  - Verify that the updated pod achieves `Running` state without error exits.
- **Q16:** An Ingress controller is deployed in the cluster, and an Ingress routing rule is required to route external HTTP traffic to service `web-service` on port 80:
  - In namespace `mock-cka-2-q16`, create an Ingress resource named `app-ingress`.
  - Configure a host rule for `app.example.com` routing HTTP path `/` to service `web-service` on port 80.
  - Ensure the Ingress rule is correctly applied.
- **Q17:** Deployment `broken-deployment` in namespace `mock-cka-2-q17` has 0/1 ready replicas because the pod specification points to a nonexistent container image tag (`ImagePullBackOff`):
  - Inspect the rollout status and pod events for `broken-deployment`.
  - Update the container image to a valid, existing image tag: `nginx:1.25-alpine`.
  - Verify that the deployment completes its rollout with 1/1 ready replicas.""",
        "setup": """# Setup CKA Mock Exam 2
ssh controlplane '
for q in q1 q5 q6 q7 q8 q9 q9-frontend q10 q11 q12 q14 q15 q16 q17; do
  kubectl create ns mock-cka-2-$q 2>/dev/null || true
  kubectl delete deploy,pod,svc,netpol,pvc,role,rolebinding,sa --all -n mock-cka-2-$q --grace-period=0 --force 2>/dev/null || true
done

# Q4 cordon node02
kubectl cordon node02 2>/dev/null || true

# Q11 host directory
sudo mkdir -p /mnt/manual-data && sudo chmod 777 /mnt/manual-data

# Q14 taint node01 and deploy pending pod
kubectl taint nodes node01 tier=special:NoSchedule --overwrite 2>/dev/null || true
kubectl run pending-pod -n mock-cka-2-q14 --image=nginx:alpine --overrides='{"spec":{"nodeSelector":{"kubernetes.io/hostname":"node01"}}}'

# Q15 broken pod
cat << "EOF" | kubectl apply -n mock-cka-2-q15 -f -
apiVersion: v1
kind: Pod
metadata:
  name: broken-logger
spec:
  containers:
  - name: logger
    image: busybox:1.36
    command: ["sh", "-c", "invalid_logger_command; sleep 3600"]
EOF

# Q16 web-service
kubectl create deploy web-service -n mock-cka-2-q16 --image=nginx:alpine
kubectl expose deploy web-service -n mock-cka-2-q16 --port=80

# Q17 broken deployment
kubectl create deploy broken-deployment -n mock-cka-2-q17 --image=nginx:1.99-nonexistent

sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
rm -f /opt/k8s/apiserver-expiry.txt
'
# Q13 stop kubelet on node02
ssh node02 'sudo systemctl stop kubelet'""",
        "verify": """# Linux Foundation CKA Domain Tracking
SCORE_STOR=0; TOTAL_STOR=2       # 10%
SCORE_TROUBLE=0; TOTAL_TROUBLE=5   # 30%
SCORE_WORKLOAD=0; TOTAL_WORKLOAD=3 # 15%
SCORE_CLUSTER=0; TOTAL_CLUSTER=4   # 25%
SCORE_SVC=0; TOTAL_SVC=3           # 20%
TOTAL_PASSED=0; TOTAL_QUESTIONS=17
SCORE=0; TOTAL=17

echo -e "${BOLD}Evaluating CKA Mock Exam 2 against Linux Foundation Domain Weights...${NC}"

# Q1: SA & ClusterRole (Cluster Architecture - 25%)
SA1=$(ssh controlplane 'kubectl get sa monitoring-sa -n mock-cka-2-q1 -o jsonpath="{.metadata.name}" 2>/dev/null || echo "None"')
CRB1=$(ssh controlplane 'kubectl get clusterrolebinding monitoring-binding -o jsonpath="{.roleRef.name}" 2>/dev/null || echo "None"')
if [ "$SA1" == "monitoring-sa" ] && [ "$CRB1" == "monitoring-role" ]; then
  echo -e "${GREEN}[PASS] Q1: monitoring-sa and ClusterRoleBinding verified.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q1: SA=$SA1, CRB=$CRB1.${NC}"
fi

# Q2: Cert Expiry (Cluster Architecture - 25%)
if ssh controlplane 'test -f /opt/k8s/apiserver-expiry.txt' && ssh controlplane 'grep -qi "CERTIFICATE" /opt/k8s/apiserver-expiry.txt'; then
  echo -e "${GREEN}[PASS] Q2: apiserver-expiry.txt verified.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q2: apiserver-expiry.txt missing or lacks cert table.${NC}"
fi

# Q3: Worker static pod on node01 (Cluster Architecture - 25%)
POD3=$(ssh controlplane 'kubectl get pods -A 2>/dev/null | grep "static-web-node01" || true')
if [ -n "$POD3" ] && echo "$POD3" | grep -q "Running"; then
  echo -e "${GREEN}[PASS] Q3: Static pod static-web-node01 Running.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q3: static-web-node01 not running.${NC}"
fi

# Q4: Node02 maintenance / Ready (Cluster Architecture - 25%)
READY4=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.status.conditions[?(@.type=="Ready")].status}" 2>/dev/null || echo "False"')
SCHED4=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.spec.unschedulable}" 2>/dev/null || echo "false"')
if [ "$READY4" == "True" ] && [ "$SCHED4" != "true" ]; then
  echo -e "${GREEN}[PASS] Q4: node02 is Ready and schedulable.${NC}"; SCORE_CLUSTER=$((SCORE_CLUSTER + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q4: node02 Ready=$READY4, unschedulable=$SCHED4.${NC}"
fi

# Q5: Init container emptyDir pod (Workloads & Scheduling - 15%)
POD5=$(ssh controlplane 'kubectl get pod init-volume-pod -n mock-cka-2-q5 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
INIT5=$(ssh controlplane 'kubectl get pod init-volume-pod -n mock-cka-2-q5 -o jsonpath="{.spec.initContainers[0].name}" 2>/dev/null || echo "None"')
if [ "$POD5" == "Running" ] && [ "$INIT5" != "None" ]; then
  echo -e "${GREEN}[PASS] Q5: init-volume-pod running with initContainer.${NC}"; SCORE_WORKLOAD=$((SCORE_WORKLOAD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q5: init-volume-pod phase: $POD5, initContainer: $INIT5.${NC}"
fi

# Q6: HPA (Workloads & Scheduling - 15%)
HPA6=$(ssh controlplane 'kubectl get hpa hpa-deployment -n mock-cka-2-q6 -o jsonpath="{.spec.maxReplicas}" 2>/dev/null || echo "0"')
if [ "$HPA6" == "8" ]; then
  echo -e "${GREEN}[PASS] Q6: HPA hpa-deployment verified (maxReplicas=8).${NC}"; SCORE_WORKLOAD=$((SCORE_WORKLOAD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q6: HPA maxReplicas: $HPA6 (expected 8).${NC}"
fi

# Q7: CronJob (Workloads & Scheduling - 15%)
CJ7=$(ssh controlplane 'kubectl get cronjob periodic-task -n mock-cka-2-q7 -o jsonpath="{.spec.schedule}" 2>/dev/null || echo "None"')
if [ "$CJ7" == "*/5 * * * *" ]; then
  echo -e "${GREEN}[PASS] Q7: CronJob periodic-task verified with schedule */5 * * * *.${NC}"; SCORE_WORKLOAD=$((SCORE_WORKLOAD + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q7: CronJob schedule: $CJ7.${NC}"
fi

# Q8: Headless service & deployment (Services & Networking - 20%)
SVC8=$(ssh controlplane 'kubectl get svc db-headless -n mock-cka-2-q8 -o jsonpath="{.spec.clusterIP}" 2>/dev/null || echo "None"')
DEP8=$(ssh controlplane 'kubectl get deploy db-deployment -n mock-cka-2-q8 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$SVC8" == "None" ] && [ "$DEP8" == "3" ]; then
  echo -e "${GREEN}[PASS] Q8: Headless service (clusterIP: None) and deployment verified.${NC}"; SCORE_SVC=$((SCORE_SVC + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q8: clusterIP=$SVC8, replicas=$DEP8.${NC}"
fi

# Q9: NetworkPolicy allow-frontend (Services & Networking - 20%)
NP9=$(ssh controlplane 'kubectl get netpol allow-frontend -n mock-cka-2-q9 -o jsonpath="{.metadata.name}" 2>/dev/null || echo "None"')
if [ "$NP9" == "allow-frontend" ]; then
  echo -e "${GREEN}[PASS] Q9: NetworkPolicy allow-frontend verified.${NC}"; SCORE_SVC=$((SCORE_SVC + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q9: allow-frontend NetworkPolicy missing.${NC}"
fi

# Q10: ExternalName service (Services & Networking - 20%)
SVC10=$(ssh controlplane 'kubectl get svc db-external -n mock-cka-2-q10 -o jsonpath="{.spec.externalName}" 2>/dev/null || echo "None"')
if [ "$SVC10" == "database.example.com" ]; then
  echo -e "${GREEN}[PASS] Q10: ExternalName service verified.${NC}"; SCORE_SVC=$((SCORE_SVC + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q10: externalName is '$SVC10'.${NC}"
fi

# Q11: PV & PVC manual-pv (Storage - 10%)
PV11=$(ssh controlplane 'kubectl get pv manual-pv -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
POD11=$(ssh controlplane 'kubectl get pod pv-pod -n mock-cka-2-q11 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$PV11" == "Bound" ] && [ "$POD11" == "Running" ]; then
  echo -e "${GREEN}[PASS] Q11: PV manual-pv Bound and pv-pod Running.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q11: PV phase: $PV11, Pod phase: $POD11.${NC}"
fi

# Q12: Projected volume pod (Storage - 10%)
POD12=$(ssh controlplane 'kubectl get pod projected-volume-pod -n mock-cka-2-q12 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
PROJ12=$(ssh controlplane 'kubectl get pod projected-volume-pod -n mock-cka-2-q12 -o jsonpath="{.spec.volumes[0].projected.sources}" 2>/dev/null || echo "None"')
if [ "$POD12" == "Running" ] && [ "$PROJ12" != "None" ]; then
  echo -e "${GREEN}[PASS] Q12: projected-volume-pod Running with projected sources.${NC}"; SCORE_STOR=$((SCORE_STOR + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q12: projected-volume-pod status: $POD12.${NC}"
fi

# Q13: Kubelet on node02 (Troubleshooting - 30%)
KUB13=$(ssh node02 'systemctl is-active kubelet 2>/dev/null || echo "inactive"')
if [ "$KUB13" == "active" ]; then
  echo -e "${GREEN}[PASS] Q13: Kubelet on node02 is active.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q13: Kubelet on node02 is $KUB13.${NC}"
fi

# Q14: Pending pod scheduled (Troubleshooting - 30%)
POD14=$(ssh controlplane 'kubectl get pod pending-pod -n mock-cka-2-q14 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
if [ "$POD14" == "Running" ]; then
  echo -e "${GREEN}[PASS] Q14: pending-pod is now Running.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q14: pending-pod is $POD14.${NC}"
fi

# Q15: Broken logger troubleshooting (Troubleshooting - 30%)
POD15=$(ssh controlplane 'kubectl get pod broken-logger -n mock-cka-2-q15 -o jsonpath="{.status.phase}" 2>/dev/null || echo "None"')
CMD15=$(ssh controlplane 'kubectl get pod broken-logger -n mock-cka-2-q15 -o jsonpath="{.spec.containers[0].command}" 2>/dev/null || true')
if [ "$POD15" == "Running" ] && ! echo "$CMD15" | grep -q "invalid"; then
  echo -e "${GREEN}[PASS] Q15: broken-logger repaired and Running.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q15: broken-logger status: $POD15.${NC}"
fi

# Q16: Ingress app-ingress (Troubleshooting - 30%)
ING16=$(ssh controlplane 'kubectl get ingress app-ingress -n mock-cka-2-q16 -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo "None"')
if [ "$ING16" == "app.example.com" ]; then
  echo -e "${GREEN}[PASS] Q16: Ingress app-ingress verified for app.example.com.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q16: Ingress host: $ING16.${NC}"
fi

# Q17: Broken deployment image fix (Troubleshooting - 30%)
READY17=$(ssh controlplane 'kubectl get deploy broken-deployment -n mock-cka-2-q17 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo "0"')
if [ "$READY17" == "1" ]; then
  echo -e "${GREEN}[PASS] Q17: broken-deployment image fixed and ready.${NC}"; SCORE_TROUBLE=$((SCORE_TROUBLE + 1)); TOTAL_PASSED=$((TOTAL_PASSED + 1))
else
  echo -e "${RED}[FAIL] Q17: ready replicas: $READY17.${NC}"
fi""",
        "solution": """### Official Walkthrough & Solution Guide

#### Q1: ServiceAccount & ClusterRole
```bash
kubectl create sa monitoring-sa -n mock-cka-2-q1
kubectl create clusterrole monitoring-role --verb=get,list,watch --resource=pods,services,nodes
kubectl create clusterrolebinding monitoring-binding --clusterrole=monitoring-role --serviceaccount=mock-cka-2-q1:monitoring-sa
```

#### Q2: Certificate Expiry
```bash
kubeadm certs check-expiry > /opt/k8s/apiserver-expiry.txt
```

#### Q3: Worker Static Pod
On `node01`:
```bash
sudo tee /etc/kubernetes/manifests/static-web.yaml << 'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: static-web
spec:
  containers:
  - name: web
    image: nginx:alpine
EOF
```

#### Q4: Node Maintenance
```bash
kubectl drain node02 --ignore-daemonsets --delete-emptydir-data --force
sleep 5
kubectl uncordon node02
```

#### Q5: Init Container
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: init-volume-pod
  namespace: mock-cka-2-q5
spec:
  volumes:
  - name: work-vol
    emptyDir: {}
  initContainers:
  - name: init-writer
    image: busybox:1.36
    command: ["sh", "-c", "echo init-data > /shared/greeting.txt"]
    volumeMounts:
    - name: work-vol
      mountPath: /shared
  containers:
  - name: main-reader
    image: busybox:1.36
    command: ["sh", "-c", "cat /shared/greeting.txt && sleep 3600"]
    volumeMounts:
    - name: work-vol
      mountPath: /shared
```

#### Q6: HPA
```bash
kubectl autoscale deploy hpa-deployment --cpu-percent=60 --min=2 --max=8 -n mock-cka-2-q6
```

#### Q7: CronJob
```bash
kubectl create cronjob periodic-task --image=busybox:1.36 --schedule="*/5 * * * *" -n mock-cka-2-q7 -- sh -c "date"
kubectl patch cronjob periodic-task -n mock-cka-2-q7 -p '{"spec":{"concurrencyPolicy":"Forbid"}}'
```

#### Q8: Headless Service
```yaml
apiVersion: v1
kind: Service
metadata:
  name: db-headless
  namespace: mock-cka-2-q8
spec:
  clusterIP: None
  selector:
    app: db
  ports:
  - port: 3306
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: db-deployment
  namespace: mock-cka-2-q8
spec:
  replicas: 3
  selector:
    matchLabels:
      app: db
  template:
    metadata:
      labels:
        app: db
    spec:
      containers:
      - name: db
        image: nginx:alpine
```

#### Q9: Cross-Namespace NetworkPolicy
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend
  namespace: mock-cka-2-q9
spec:
  podSelector:
    matchLabels:
      role: backend
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: mock-cka-2-q9-frontend
```

#### Q10: ExternalName Service
```bash
kubectl create svc externalname db-external --external-name=database.example.com -n mock-cka-2-q10
```

#### Q11: Manual PV/PVC
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: manual-pv
spec:
  capacity:
    storage: 2Gi
  accessModes:
    - ReadWriteOnce
  storageClassName: manual
  hostPath:
    path: /mnt/manual-data
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: manual-pvc
  namespace: mock-cka-2-q11
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: manual
  resources:
    requests:
      storage: 2Gi
```

#### Q13: Restart Kubelet
`ssh node02 'sudo systemctl restart kubelet'`

#### Q14: Remove Node Taint
`kubectl taint nodes node01 tier=special:NoSchedule-`

#### Q15: Repair Broken Logger Pod
```bash
kubectl delete pod broken-logger -n mock-cka-2-q15 --force --grace-period=0
kubectl run broken-logger -n mock-cka-2-q15 --image=busybox:1.36 -- sh -c "while true; do date; sleep 5; done"
```

#### Q16: Ingress Resource
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  namespace: mock-cka-2-q16
spec:
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 80
```

#### Q17: Fix Deployment Image
`kubectl set image deploy/broken-deployment nginx=nginx:1.25-alpine -n mock-cka-2-q17`""",
        "reset": """ssh controlplane '
kubectl delete ns mock-cka-2-q1 mock-cka-2-q5 mock-cka-2-q6 mock-cka-2-q7 mock-cka-2-q8 mock-cka-2-q9 mock-cka-2-q9-frontend mock-cka-2-q10 mock-cka-2-q11 mock-cka-2-q12 mock-cka-2-q14 mock-cka-2-q15 mock-cka-2-q16 mock-cka-2-q17 --grace-period=0 --force --wait=false 2>/dev/null || true
kubectl delete pv manual-pv 2>/dev/null || true
kubectl delete clusterrole monitoring-role 2>/dev/null || true
kubectl delete clusterrolebinding monitoring-binding 2>/dev/null || true
kubectl taint nodes node01 tier=special:NoSchedule- 2>/dev/null || true
kubectl uncordon node02 2>/dev/null || true
kubectl delete pod static-web-node01 --force --grace-period=0 2>/dev/null || true
sudo rm -rf /opt/k8s/apiserver-expiry.txt /mnt/manual-data
'
ssh node01 '
sudo rm -f /etc/kubernetes/manifests/static-web.yaml
POD_ID=$(sudo crictl pods -q --name static-web-node01 2>/dev/null || true)
[ -n "$POD_ID" ] && sudo crictl stopp "$POD_ID" 2>/dev/null && sudo crictl rmp "$POD_ID" 2>/dev/null || true
'
ssh node02 'sudo systemctl restart kubelet 2>/dev/null || true'""",
    },
]
