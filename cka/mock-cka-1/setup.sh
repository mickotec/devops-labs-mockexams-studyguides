#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up mock-cka-1 (CKA Full-Scale Timed Mock Exam 1)..."
# Setup CKA Mock Exam 1
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
'
echo "[✓] Environment ready. Review tasks with: ./lab show mock-cka-1"
