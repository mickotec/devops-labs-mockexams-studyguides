#!/usr/bin/env python3
"""
End-to-End Solve Validation Harness for Weeks 1 and 2 (All 24 Labs).
For each lab:
  1. ./lab start <lab-id>       (Verify setup succeeds)
  2. ./lab check <lab-id>       (Verify pre-solve rejection - cannot auto-pass)
  3. Execute solution commands  (Apply documented candidate steps)
  4. ./lab check <lab-id>       (Verify 100% PASS with exit code 0)
  5. ./lab reset <lab-id>       (Verify cleanup succeeds with exit code 0)
"""

import subprocess
import sys
import time

LABS_WEEK_1_AND_2 = [
    # Week 1
    "w1d1-cka", "w1d1-lfcs",
    "w1d2-cka", "w1d2-lfcs",
    "w1d3-cka", "w1d3-lfcs",
    "w1d4-cka", "w1d4-lfcs",
    "w1d5-cka", "w1d5-lfcs",
    "w1d6-cka", "w1d6-lfcs",
    # Week 2
    "w2d1-cka", "w2d1-lfcs",
    "w2d2-cka", "w2d2-lfcs",
    "w2d3-cka", "w2d3-lfcs",
    "w2d4-cka", "w2d4-lfcs",
    "w2d5-cka", "w2d5-lfcs",
    "w2d6-cka", "w2d6-lfcs",
]

def run(cmd, input_data=None):
    res = subprocess.run(cmd, shell=True, input=input_data, capture_output=True, text=True)
    return res.returncode, res.stdout.strip(), res.stderr.strip()

def ssh_exec(host, cmd, input_data=None):
    res = subprocess.run(
        ["ssh", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", host, cmd],
        input=input_data,
        capture_output=True,
        text=True
    )
    return res.returncode, res.stdout.strip(), res.stderr.strip()

def solve_lab(lab_id):
    """Executes the exact solution steps for the specified lab."""
    if lab_id == "w1d1-cka":
        ssh_exec("controlplane", "sudo sed -i 's/^apiVersion: v1.0/apiVersion: v1/' /etc/kubernetes/manifests/kube-scheduler.yaml")
        ssh_exec("node01", 'CID=$(sudo crictl ps -a -q --name rogue-crypto-miner); [ -n "$CID" ] && sudo crictl stop "$CID" && sudo crictl rm "$CID" || true')
        monitor_yaml = """apiVersion: v1
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
"""
        ssh_exec("node01", "sudo tee /etc/kubernetes/manifests/node01-monitor.yaml > /dev/null", input_data=monitor_yaml)
        # Wait for scheduler, test pod, and static pod
        for _ in range(25):
            _, s_phase, _ = ssh_exec("controlplane", 'kubectl get pod -n kube-system -l component=kube-scheduler -o jsonpath="{.items[0].status.phase}" 2>/dev/null')
            _, t_phase, _ = ssh_exec("controlplane", 'kubectl get pod w1d1-pending-test -o jsonpath="{.status.phase}" 2>/dev/null')
            _, m_phase, _ = ssh_exec("controlplane", 'kubectl get pod node01-monitor-node01 -o jsonpath="{.status.phase}" 2>/dev/null')
            if s_phase == "Running" and t_phase == "Running" and m_phase == "Running":
                break
            time.sleep(2)

    elif lab_id == "w1d1-lfcs":
        ssh_exec("lfcs", 'apropos "partition table" > /var/tmp/lfcs-doc-search.txt && apropos "password file" >> /var/tmp/lfcs-doc-search.txt && man 5 passwd | col -b | head -n 30 > /var/tmp/lfcs-passwd-fields.txt')
        ssh_exec("lfcs", "mkdir -p /var/tmp/lfcs/a/b/c/d/e && touch /var/tmp/lfcs/a/b/c/d/e/evidence.txt")
        quickman_code = """#!/usr/bin/env bash
if [ -z "$1" ]; then
  echo "Usage: quickman <command>"
  exit 1
fi
man "$1" 2>/dev/null | col -b | sed -n '/^NAME/,/^[A-Z]/p' | head -n -1
man "$1" 2>/dev/null | col -b | sed -n '/^SYNOPSIS/,/^[A-Z]/p' | head -n -1
"""
        ssh_exec("lfcs", "sudo tee /usr/local/bin/quickman > /dev/null && sudo chmod 755 /usr/local/bin/quickman", input_data=quickman_code)

    elif lab_id == "w1d2-cka":
        cmd = """
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  endpoint health 2>&1 | sudo tee /opt/backup/etcd-health.txt > /dev/null

sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  snapshot save /opt/backup/etcd-snapshot-w1d2.db > /dev/null

sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup/etcd-snapshot-w1d2.db --write-out=table | sudo tee /opt/backup/snapshot-status.txt > /dev/null

kubectl get ns --no-headers | wc -l | tr -d "[:space:]" | sudo tee /opt/backup/namespace-count.txt > /dev/null
"""
        ssh_exec("controlplane", cmd)

    elif lab_id == "w1d2-lfcs":
        ssh_exec("lfcs", "sudo ln -sfn ../storage/v2/app-v2.conf /opt/link-lab/configs/active.conf")
        ssh_exec("lfcs", 'sudo ln /opt/link-lab/storage/v2/app-v2.conf /opt/link-lab/backup/app-v2.conf.hl && echo "BACKUP_ENABLED=true" | sudo tee -a /opt/link-lab/backup/app-v2.conf.hl')
        ssh_exec("lfcs", "find /opt/link-lab/orphan_links -xtype l | sudo tee /var/tmp/removed_links.txt && cat /var/tmp/removed_links.txt | xargs -r sudo rm -f")

    elif lab_id == "w1d3-cka":
        ssh_exec("controlplane", "kubectl create namespace fintech --dry-run=client -o yaml | kubectl apply -f -")
        pod_manifest = """apiVersion: v1
kind: Pod
metadata:
  name: transaction-processor
  namespace: fintech
spec:
  containers:
  - name: processor
    image: nginx:1.25-alpine
    env:
    - name: MAX_WORKERS
      value: "8"
    - name: CACHE_DIR
      value: "/tmp/cache"
    ports:
    - name: http
      containerPort: 8080
    - name: metrics
      containerPort: 9090
    resources:
      limits:
        memory: "128Mi"
        cpu: "200m"
    readinessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 2
"""
        ssh_exec("controlplane", "sudo tee /opt/k8s-manifests/broken-app.yaml > /dev/null && kubectl apply -f /opt/k8s-manifests/broken-app.yaml", input_data=pod_manifest)
        event_script = 'while true; do echo "[STREAM] Transaction event at $(date)" >> /tmp/stream.log; sleep 2; done'
        ssh_exec("controlplane", f'kubectl run event-streamer -n fintech --image=busybox:1.36 --restart=Always -- sh -c \'{event_script}\'')
        for _ in range(20):
            _, out1, _ = ssh_exec("controlplane", 'kubectl get pod transaction-processor -n fintech -o jsonpath="{.status.phase}" 2>/dev/null')
            _, out2, _ = ssh_exec("controlplane", 'kubectl get pod event-streamer -n fintech -o jsonpath="{.status.phase}" 2>/dev/null')
            _, log_check, _ = ssh_exec("controlplane", 'kubectl exec -n fintech event-streamer -- cat /tmp/stream.log 2>/dev/null | grep STREAM || true')
            if out1 == "Running" and out2 == "Running" and bool(log_check):
                break
            time.sleep(2)

    elif lab_id == "w1d3-lfcs":
        ssh_exec("lfcs", "sudo groupadd -f devops_eng && (id alice &>/dev/null || sudo useradd -g devops_eng -m alice) && (id bob &>/dev/null || sudo useradd -g devops_eng -m bob)")
        ssh_exec("lfcs", "sudo chgrp -R devops_eng /srv/data/engineering && sudo find /srv/data/engineering -type d -exec chmod 775 {} + && sudo find /srv/data/engineering -type f -exec chmod 664 {} +")
        umask_script = """if id -nG | grep -qw "devops_eng"; then
  umask 002
fi
"""
        ssh_exec("lfcs", "sudo tee /etc/profile.d/devops_umask.sh > /dev/null && sudo chmod 644 /etc/profile.d/devops_umask.sh", input_data=umask_script)

    elif lab_id == "w1d4-cka":
        ssh_exec("controlplane", "kubectl create namespace telemetry --dry-run=client -o yaml | kubectl apply -f -")
        order_manifest = """apiVersion: v1
kind: Pod
metadata:
  name: order-service
  namespace: telemetry
spec:
  volumes:
  - name: log-volume
    emptyDir: {}
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo \\"$(date) [ORDER] Transaction processed\\" >> /var/log/app/orders.log; sleep 1; done"]
    volumeMounts:
    - name: log-volume
      mountPath: /var/log/app
  - name: logger
    image: busybox:1.36
    command: ["sh", "-c", "tail -n+1 -f /var/log/app/orders.log"]
    volumeMounts:
    - name: log-volume
      mountPath: /var/log/app
      readOnly: true
---
apiVersion: v1
kind: Pod
metadata:
  name: web-portal
  namespace: telemetry
spec:
  volumes:
  - name: data-vol
    emptyDir: {}
  initContainers:
  - name: db-wait
    image: busybox:1.36
    command: ["sh", "-c", "echo ready > /opt/data/ready.flag"]
    volumeMounts:
    - name: data-vol
      mountPath: /opt/data
  containers:
  - name: web
    image: nginx:1.25-alpine
    volumeMounts:
    - name: data-vol
      mountPath: /opt/data
"""
        ssh_exec("controlplane", "kubectl apply -f -", input_data=order_manifest)
        for _ in range(25):
            _, p1, _ = ssh_exec("controlplane", 'kubectl get pod order-service -n telemetry -o jsonpath="{.status.phase}" 2>/dev/null')
            _, p2, _ = ssh_exec("controlplane", 'kubectl get pod web-portal -n telemetry -o jsonpath="{.status.phase}" 2>/dev/null')
            _, log_test, _ = ssh_exec("controlplane", 'kubectl logs -n telemetry order-service -c logger --tail=5 2>/dev/null | grep ORDER || true')
            if p1 == "Running" and p2 == "Running" and bool(log_test):
                break
            time.sleep(2)

    elif lab_id == "w1d4-lfcs":
        ssh_exec("lfcs", "sudo groupadd -f marketing && sudo mkdir -p /opt/campaigns/incoming && sudo chown root:marketing /opt/campaigns && sudo chmod 2770 /opt/campaigns && sudo chown root:marketing /opt/campaigns/incoming && sudo chmod 1770 /opt/campaigns/incoming")
        ssh_exec("lfcs", "sudo find /var/log -type f -perm -002 > /var/tmp/world_writable_audit.txt")

    elif lab_id == "w1d5-cka":
        cmd = """
grep -q "alias k=kubectl" ~/.bashrc || echo "alias k=kubectl" >> ~/.bashrc
grep -q "tabstop=2" ~/.vimrc 2>/dev/null || echo -e "set tabstop=2\\nset shiftwidth=2\\nset expandtab" >> ~/.vimrc
kubectl create deploy cache-redis -n speed-drill --image=redis:7-alpine --replicas=3
kubectl expose deploy cache-redis -n speed-drill --name=cache-service --port=6379
kubectl create secret generic redis-secret -n speed-drill --from-literal=auth=supersecret
kubectl get deploy cache-redis -n speed-drill -o yaml | grep -v "managedFields:" > /opt/k8s/clean-cache.yaml
"""
        ssh_exec("controlplane", cmd)
        ssh_exec("controlplane", "kubectl rollout status deploy/cache-redis -n speed-drill --timeout=30s")

    elif lab_id == "w1d5-lfcs":
        cmd = """
grep -q "tabstop=4" ~/.vimrc 2>/dev/null || echo -e "set number\\nsyntax on\\nset tabstop=4\\nset shiftwidth=4\\nset expandtab\\nset hlsearch\\nset incsearch" >> ~/.vimrc
sed -i "s/PORT = 8080/PORT = 8443/" /var/tmp/app_legacy.conf
sed -i "s/^# SSL_ENABLED = true/SSL_ENABLED = true/" /var/tmp/app_legacy.conf
sed -i "/DEPRECATED/d" /var/tmp/app_legacy.conf
grep -oE "STATUS: [0-9]+" /var/tmp/sample_audit.log | sort | uniq -c > /var/tmp/status_summary.txt
"""
        ssh_exec("lfcs", cmd)

    elif lab_id == "w1d6-cka":
        ssh_exec("controlplane", "if [ -d /etc/kubernetes/manifests_broken ]; then sudo mv /etc/kubernetes/manifests_broken /etc/kubernetes/manifests && sudo systemctl restart kubelet; fi")
        for _ in range(25):
            _, out, _ = ssh_exec("controlplane", 'kubectl get pod -l component=kube-apiserver -n kube-system -o jsonpath="{.items[0].status.phase}" 2>/dev/null')
            if out == "Running":
                break
            time.sleep(2)
        cmd = """
kubectl create ns triathlon-w1 --dry-run=client -o yaml | kubectl apply -f -
kubectl create deploy web-ui -n triathlon-w1 --image=nginx:1.25-alpine --replicas=2
kubectl set resources deploy web-ui -n triathlon-w1 --limits=cpu=150m,memory=128Mi
kubectl expose deploy web-ui -n triathlon-w1 --name=web-ui-svc --port=80
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  snapshot save /opt/backup/triathlon-etcd.db > /dev/null
"""
        ssh_exec("controlplane", cmd)
        worker_agent = """apiVersion: v1
kind: Pod
metadata:
  name: w1-worker-agent
spec:
  containers:
  - name: agent
    image: busybox:1.36
    command: ["sh", "-c", "sleep 3600"]
"""
        ssh_exec("node01", "sudo tee /etc/kubernetes/manifests/w1-worker-agent.yaml > /dev/null", input_data=worker_agent)
        for _ in range(20):
            _, out1, _ = ssh_exec("controlplane", 'kubectl get pod w1-worker-agent-node01 -o jsonpath="{.status.phase}" 2>/dev/null')
            _, out2, _ = ssh_exec("controlplane", 'kubectl get deploy web-ui -n triathlon-w1 -o jsonpath="{.status.readyReplicas}" 2>/dev/null')
            if out1 == "Running" and out2 == "2":
                break
            time.sleep(2)

    elif lab_id == "w1d6-lfcs":
        cmd = """
sudo groupadd -f sysadmins
sudo groupadd -f contractors
sudo mkdir -p /srv/secure_vault/incoming /srv/secure_vault/configs /srv/secure_vault/storage
sudo touch /srv/secure_vault/storage/vault.conf
sudo chown root:sysadmins /srv/secure_vault
sudo chmod 2770 /srv/secure_vault
sudo chown root:contractors /srv/secure_vault/incoming
sudo chmod 1775 /srv/secure_vault/incoming
sudo find /opt/binaries -type f \\( -perm -4000 -o -perm -2000 \\) > /var/tmp/suid_audit.txt
sudo ln -sf ../storage/vault.conf /srv/secure_vault/configs/current.conf
sudo tar -czpf /var/backups/vault_initial.tar.gz -C /srv secure_vault
"""
        ssh_exec("lfcs", cmd)

    # Week 2
    elif lab_id == "w2d1-cka":
        rs_yaml = """apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: web-replicas
  namespace: core
spec:
  replicas: 6
  selector:
    matchLabels:
      app: web-app
      tier: frontend
  template:
    metadata:
      labels:
        app: web-app
        tier: frontend
    spec:
      containers:
      - name: nginx
        image: nginx:1.25-alpine
"""
        ssh_exec("controlplane", "sudo tee /opt/k8s/replicaset-broken.yaml > /dev/null && kubectl apply -f /opt/k8s/replicaset-broken.yaml", input_data=rs_yaml)
        for _ in range(15):
            _, out, _ = ssh_exec("controlplane", 'kubectl get rs web-replicas -n core -o jsonpath="{.status.readyReplicas}" 2>/dev/null')
            if out == "6":
                break
            time.sleep(2)

    elif lab_id == "w2d1-lfcs":
        cmd = """
find /var/log -type f -size +500k > /var/tmp/large_logs.txt
find /etc -type f -mtime -7 -perm 644 > /var/tmp/recent_configs.txt
sudo updatedb
locate -r "^/etc/systemd/.*\\.conf$" > /var/tmp/systemd_confs.txt
"""
        ssh_exec("lfcs", cmd)

    elif lab_id == "w2d2-cka":
        deploy_yaml = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-app
  namespace: finance
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: payment-app
  template:
    metadata:
      labels:
        app: payment-app
    spec:
      containers:
      - name: nginx
        image: nginx:1.25-alpine
"""
        ssh_exec("controlplane", "kubectl apply -f -", input_data=deploy_yaml)
        ssh_exec("controlplane", "kubectl rollout status deploy/payment-app -n finance --timeout=30s")

    elif lab_id == "w2d2-lfcs":
        cmd = """
grep -oE "([0-9]{1,3}\\.){3}[0-9]{1,3}" /var/tmp/auth_sample.log | sort -u > /var/tmp/auth_ips.txt
grep -riE "pam|login" /etc/security/ 2>/dev/null | grep -vE "^[^:]+:[[:space:]]*#" > /var/tmp/pam_rules.txt || true
grep -E "Failed password|authentication failure" /var/tmp/auth_sample.log | wc -l > /var/tmp/error_count.txt
"""
        ssh_exec("lfcs", cmd)

    elif lab_id == "w2d3-cka":
        svc_yaml = """apiVersion: v1
kind: Service
metadata:
  name: api-internal
  namespace: prod
spec:
  type: ClusterIP
  selector:
    app: api
  ports:
  - name: http
    port: 80
    targetPort: 80
  - name: https
    port: 443
    targetPort: 443
---
apiVersion: v1
kind: Service
metadata:
  name: web-public
  namespace: prod
spec:
  type: NodePort
  selector:
    app: api
  ports:
  - port: 80
    targetPort: 80
    nodePort: 31200
"""
        ssh_exec("controlplane", "kubectl apply -f -", input_data=svc_yaml)

    elif lab_id == "w2d3-lfcs":
        cmd = """
awk -F: '$3 >= 1000 { printf "User: %s (UID: %s, Shell: %s)\\n", $1, $3, $7 }' /etc/passwd > /var/tmp/regular_users.txt
sed -i "s/PORT = 8080/PORT = 443/" /var/tmp/config_sample.ini
sed -i "/DEBUG = True/d" /var/tmp/config_sample.ini
sed -i "/\\[server\\]/a ENVIRONMENT = Production" /var/tmp/config_sample.ini
awk -F, 'NR>1 { sum += $2 } END { print sum }' /var/tmp/sales.csv > /var/tmp/sales_total.txt
"""
        ssh_exec("lfcs", cmd)

    elif lab_id == "w2d4-cka":
        ssh_exec("controlplane", "kubectl run mysql-db -n database-ns --image=nginx:alpine --labels=app=db")
        ssh_exec("controlplane", "kubectl expose pod mysql-db -n database-ns --name=mysql-svc --port=3306 --target-port=80")
        ssh_exec("controlplane", "kubectl run tester -n frontend-ns --image=busybox:1.36 -- sleep 3600")
        for _ in range(15):
            _, out, _ = ssh_exec("controlplane", 'kubectl get pod tester -n frontend-ns -o jsonpath="{.status.phase}" 2>/dev/null')
            if out == "Running":
                break
            time.sleep(2)
        ssh_exec("controlplane", 'kubectl exec -n frontend-ns tester -- sh -c "nslookup mysql-svc.database-ns.svc.cluster.local > /tmp/dns-record.txt"')

    elif lab_id == "w2d4-lfcs":
        cmd = """
find /etc -name "*shadow*" 1> /var/tmp/stdout.log 2> /var/tmp/stderr.log
ps -ef | tee /var/tmp/process_dump.txt | wc -l > /var/tmp/process_count.txt
echo -e "HOST: $(hostname)\\nKERNEL: $(uname -r)" > /var/tmp/health.report
"""
        ssh_exec("lfcs", cmd)

    elif lab_id == "w2d5-cka":
        paths_txt = """spec.containers.securityContext.capabilities.add
spec.terminationGracePeriodSeconds
"""
        ssh_exec("controlplane", "cat << 'EOF' > /opt/k8s/schema-paths.txt\nspec.containers.securityContext.capabilities.add\nspec.terminationGracePeriodSeconds\nEOF")
        sec_pod_yaml = """apiVersion: v1
kind: Pod
metadata:
  name: secure-nginx
  namespace: security-lab
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    command: ["sleep", "3600"]
    securityContext:
      runAsNonRoot: true
      runAsUser: 10001
      readOnlyRootFilesystem: false
"""
        ssh_exec("controlplane", "cat << 'EOF' > /opt/k8s/secure-pod.yaml\n" + sec_pod_yaml + "\nEOF\nkubectl apply -f /opt/k8s/secure-pod.yaml")
        for _ in range(15):
            _, out, _ = ssh_exec("controlplane", 'kubectl get pod secure-nginx -n security-lab -o jsonpath="{.status.phase}" 2>/dev/null')
            if out == "Running":
                break
            time.sleep(2)

    elif lab_id == "w2d5-lfcs":
        cmd = """
sudo tar -czpf /var/tmp/systemd_backup.tar.gz /etc/systemd
mkdir -p /var/tmp/extracted_systemd
sudo tar -xzf /var/tmp/systemd_backup.tar.gz -C /var/tmp/extracted_systemd
tar -tzf /var/tmp/systemd_backup.tar.gz > /var/tmp/archive_manifest.txt
"""
        ssh_exec("lfcs", cmd)

    elif lab_id == "w2d6-cka":
        cmd = """
kubectl create ns triathlon-w2 --dry-run=client -o yaml | kubectl apply -f -
kubectl create deploy order-processor -n triathlon-w2 --image=nginx:1.24-alpine --replicas=5
kubectl create svc nodeport order-service -n triathlon-w2 --tcp=80:80 --node-port=30500
kubectl get deploy order-processor -n triathlon-w2 -o yaml | grep -vE "resourceVersion:|uid:|creationTimestamp:|status:" > /opt/k8s/clean-export.yaml
"""
        ssh_exec("controlplane", cmd)
        for _ in range(15):
            _, out, _ = ssh_exec("controlplane", 'kubectl get deploy order-processor -n triathlon-w2 -o jsonpath="{.status.readyReplicas}" 2>/dev/null')
            if out == "5":
                break
            time.sleep(2)

    elif lab_id == "w2d6-lfcs":
        cmd = """
sudo mkdir -p /srv/repo
sudo chown -R $(whoami):$(whoami) /srv/repo
cd /srv/repo
git init -b main
git config user.name "Student"
git config user.email "student@example.com"
echo "config=v1" > system.conf
git add system.conf
git commit -m "initial commit"
git checkout -b feature-audit
echo "config=v2" > system.conf
git commit -am "feat: update v2"
git checkout main
git merge feature-audit
sudo mkdir -p /var/backups
sudo tar -czf /var/backups/repo.tar.gz -C /srv repo
"""
        ssh_exec("lfcs", cmd)

def main():
    print("=" * 75)
    print("STARTING COMPREHENSIVE END-TO-END SOLVE VALIDATION (WEEKS 1 & 2)")
    print("=" * 75)

    summary_records = []
    failed_labs = []

    target_labs = [arg for arg in sys.argv[1:] if not arg.startswith("-")] if len(sys.argv) > 1 else LABS_WEEK_1_AND_2
    for idx, lab_id in enumerate(target_labs, 1):
        print(f"\n[{idx}/{len(target_labs)}] === Validating {lab_id} ===")

        # Step 1: Start lab
        rc_start, out_start, err_start = run(f"./lab start {lab_id}")
        start_ok = (rc_start == 0)
        print(f"  [1/5] Start: {'PASS' if start_ok else 'FAIL'}")
        if not start_ok:
            print(f"    Error: {err_start or out_start}")

        # Step 2: Pre-check (MUST FAIL)
        rc_pre, out_pre, err_pre = run(f"./lab check {lab_id}")
        pre_ok = (rc_pre != 0)
        print(f"  [2/5] Pre-Solve Check (must reject uncompleted): {'REJECTED (Correct)' if pre_ok else 'AUTO-PASS BUG!'}")

        # Step 3: Solve
        t0 = time.time()
        solve_lab(lab_id)
        solve_time = round(time.time() - t0, 1)
        print(f"  [3/5] Solve Applied: Done in {solve_time}s")

        # Step 4: Post-check (MUST PASS 100%)
        rc_post, out_post, err_post = run(f"./lab check {lab_id}")
        post_ok = (rc_post == 0)
        print(f"  [4/5] Post-Solve Check: {'100% PASS' if post_ok else 'FAILED'}")
        if not post_ok:
            print(f"    Check Output:\n{out_post}")

        # Step 5: Reset
        rc_reset, out_reset, err_reset = run(f"./lab reset {lab_id}")
        reset_ok = (rc_reset == 0)
        print(f"  [5/5] Reset: {'CLEAN' if reset_ok else 'FAIL'}")
        if not reset_ok:
            print(f"    Error: {err_reset or out_reset}")

        all_ok = start_ok and pre_ok and post_ok and reset_ok
        summary_records.append({
            "lab": lab_id,
            "start": "PASS" if start_ok else "FAIL",
            "pre": "PASS" if pre_ok else "FAIL",
            "solve": "PASS" if post_ok else "FAIL",
            "reset": "PASS" if reset_ok else "FAIL",
            "overall": "PASS" if all_ok else "FAIL"
        })

        if not all_ok:
            failed_labs.append(lab_id)

    # Print Report Table
    print("\n" + "=" * 75)
    print("END-TO-END VALIDATION SUMMARY MATRIX (WEEKS 1 & 2)")
    print("=" * 75)
    print(f"{'Lab ID':<12} | {'Start':<6} | {'Pre-Check':<10} | {'Solve-Check':<12} | {'Reset':<6} | {'Verdict':<7}")
    print("-" * 75)
    for r in summary_records:
        print(f"{r['lab']:<12} | {r['start']:<6} | {r['pre']:<10} | {r['solve']:<12} | {r['reset']:<6} | {r['overall']:<7}")
    print("=" * 75)

    passed_count = sum(1 for r in summary_records if r['overall'] == "PASS")
    print(f"TOTAL: {passed_count}/{len(target_labs)} LABS PASSED END-TO-END SOLVE VALIDATION")
    if failed_labs:
        print(f"FAILED LABS: {', '.join(failed_labs)}")
        sys.exit(1)
    else:
        print("ALL 24 LABS IN WEEKS 1 AND 2 ARE FULLY VERIFIED AND PASSING 100%!")
        sys.exit(0)

if __name__ == "__main__":
    main()
