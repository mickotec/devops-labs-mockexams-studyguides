#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up mock-cka-2 (CKA Full-Scale Timed Mock Exam 2)..."
# Setup CKA Mock Exam 2
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
ssh node02 'sudo systemctl stop kubelet'
echo "[✓] Environment ready. Review tasks with: ./lab show mock-cka-2"
