# [CKAD MOCK-CKAD-2] CKAD killer.sh Real Exam Simulator 2

**Date:** 2026-11-21  
**Time Limit:** 120m  
**Passing Score:** 66%  
**Difficulty:** Exam Hard  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

**Passing Score:** 66% (Official Linux Foundation Threshold)
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
- **Q16:** Monitor cluster workloads using CLI: identify the pod with the highest CPU usage in namespace `kube-system` and save its name to `/tmp/top-pod.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check mock-ckad-2
```
