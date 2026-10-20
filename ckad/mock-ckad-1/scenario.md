# [CKAD MOCK-CKAD-1] CKAD killer.sh Real Exam Simulator 1

**Date:** 2026-11-20  
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
- **Q1:** In namespace `mock-ckad-1-q1`, create an Opaque Secret named `db-secret` containing keys `username=admin` and `password=SuperSecr3t!`. Create a Pod named `secret-pod` using image `busybox:1.36` (command: `sh -c "sleep 3600"`) that exposes these keys as environment variables `DB_USER` and `DB_PASS` using `valueFrom.secretKeyRef`.
- **Q2:** In namespace `mock-ckad-1-q2`, create a ConfigMap named `app-cfg` with keys `theme=dark` and `max_connections=150`. Create a Pod named `cfg-volume-pod` using image `nginx:alpine` mounting this ConfigMap as a volume at `/etc/app-config`.
- **Q3:** In namespace `mock-ckad-1-q3`, create a secure Pod named `hardened-pod` running image `busybox:1.36` (command `sleep 3600`). In the container's securityContext, configure: `runAsUser: 10001`, `runAsGroup: 20001`, `allowPrivilegeEscalation: false`, drop `ALL` Linux capabilities, and add only capability `NET_BIND_SERVICE`.
- **Q4:** In namespace `mock-ckad-1-q4`, create a ServiceAccount named `report-runner`. Deploy a Pod named `report-worker` using image `busybox:1.36` (command `sleep 3600`) associated with this ServiceAccount. Configure the Pod specification with `automountServiceAccountToken: false` to prevent API token mounting.

#### Domain: Application Design and Build (20% Weight - 3 Questions, 6.67% each)
- **Q5:** In namespace `mock-ckad-1-q5`, deploy a multi-container Pod named `app-with-sidecar`:
  - Main container `app`: image `busybox:1.36`, command `sh -c "while true; do echo "$(date) - Transaction OK" >> /var/log/tx.log; sleep 5; done"`.
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
- **Q16:** Pod `gateway-hub` in namespace `mock-ckad-1-q16` runs two containers: `ingress-proxy` and `egress-proxy`. Extract all log lines containing `FATAL` from container `ingress-proxy` and save them to `/tmp/fatal-errors.txt` on `controlplane`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check mock-ckad-1
```
