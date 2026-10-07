# [CKA MOCK-CKA-2] CKA Full-Scale Timed Mock Exam 2

**Date:** 2026-11-20  
**Time Limit:** 120m  
**Passing Score:** 66%  
**Difficulty:** Hard (Mock Exam Simulation)  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

# CKA Full-Scale Timed Mock Exam 2

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
  - Verify that the deployment completes its rollout with 1/1 ready replicas.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check mock-cka-2
```
