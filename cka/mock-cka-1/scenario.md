# [CKA MOCK-CKA-1] CKA Full-Scale Timed Mock Exam 1

**Date:** 2026-11-19  
**Time Limit:** 120m  
**Passing Score:** 66%  
**Difficulty:** Hard (Mock Exam Simulation)  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

# CKA Full-Scale Timed Mock Exam 1

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
  - Verify that the deployment completes its rollout and achieves 1/1 ready replicas.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check mock-cka-1
```
