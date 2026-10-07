# [CKA W1D1-CKA] Solution Walkthrough: Kubernetes Architecture & Container Runtimes

### Task 1: Fix kube-scheduler
1. SSH into `controlplane`:
   `ssh controlplane`
2. Inspect the manifest:
   `sudo vim /etc/kubernetes/manifests/kube-scheduler.yaml`
3. Fix the first line:
   Change `apiVersion: v1.0` back to `apiVersion: v1`
4. Wait 10 seconds for kubelet to reload the static pod. Check:
   `kubectl get pods -n kube-system -l component=kube-scheduler`
   `kubectl get pod w1d1-pending-test`

### Task 2: Terminate Rogue Container on node01
1. SSH into `node01`:
   `ssh node01`
2. Find the rogue container:
   `sudo crictl ps -a | grep rogue-crypto-miner`
3. Stop and remove it:
   `sudo crictl stop <CONTAINER_ID>`
   `sudo crictl rm <CONTAINER_ID>`

### Task 3: Create Static Pod on node01
1. On `node01`:
   `sudo vim /etc/kubernetes/manifests/node01-monitor.yaml`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: node01-monitor
spec:
  containers:
  - name: monitor
    image: busybox:1.36
    command: ["sh", "-c", "while true; do date >> /var/log/node-heartbeat.log; sleep 10; done"]
    volumeMounts:
    - name: log-dir
      mountPath: /var/log
  volumes:
  - name: log-dir
    hostPath:
      path: /var/log
```
