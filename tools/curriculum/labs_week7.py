"""
Lab definitions for Week 7
Curriculum:
Day 1: Cluster & Pod Networking Prerequisites | Linux Networking Configuration (IP & Routing)
Day 2: Service Networking & CoreDNS Deep Dive | Network Bonding & Bridging
Day 3: Ingress Controllers & Routing Rules | Packet Filtering with Firewalld & Iptables
Day 4: Gateway API (2025 Updates) | NAT, Port Redirection & Reverse Proxies
Day 5: Network Policies Deep Dive | SSH Hardening, Key Auth & Time Sync
Day 6: Week 7 Network Mastery Triathlon | Week 7 Linux Networking & Firewall Marathon
"""

WEEK_7_LABS = [
    # Day 1
    {
        "day": 1,
        "date": "2026-11-09",
        "cka_title": "Cluster & Pod Networking Prerequisites",
        "cka_diff": "Medium",
        "cka_time": "35m",
        "cka_tasks": """### Task 1: Inspect Active CNI Plugin
1. On `controlplane`, inspect the CNI network configuration directory `/etc/cni/net.d/`.
2. Find the active CNI configuration file (e.g. `10-flannel.conflist` or similar).
3. Extract the primary plugin type (e.g. `flannel`, `calico`, or `bridge`) and write it into `/opt/k8s/cni-plugin-type.txt`.

### Task 2: Extract Node PodCIDR Allocations
1. Retrieve the assigned `podCIDR` for worker nodes `node01` and `node02` using `kubectl get nodes -o jsonpath`.
2. Write each node and its podCIDR formatted as `<nodeName>=<podCIDR>` on separate lines into `/opt/k8s/node-podcidrs.txt`.
   Example format:
   ```
   node01=10.244.1.0/24
   node02=10.244.2.0/24
   ```

### Task 3: Deploy Cross-Node Pod Mesh
In namespace `w7d1-net`:
1. Create a DaemonSet named `net-mesh` with container image `busybox:1.36` running command `["sleep", "3600"]`.
2. Verify that a pod is scheduled and running on each worker node (`node01` and `node02`) and each has acquired a valid pod IP.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w7d1-net --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d1-net
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/cni-plugin-type.txt /opt/k8s/node-podcidrs.txt
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: CNI plugin type file exists and has content
CNI_TYPE=$(ssh controlplane 'cat /opt/k8s/cni-plugin-type.txt 2>/dev/null | tr -d "[:space:]"')
if [ -n "$CNI_TYPE" ] && [[ "$CNI_TYPE" =~ (flannel|calico|bridge|weave|cilium|canal) ]]; then
  echo -e "${GREEN}[PASS] Task 1: Valid CNI plugin type recorded ($CNI_TYPE).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /opt/k8s/cni-plugin-type.txt missing or invalid: $CNI_TYPE.${NC}"
fi

# Task 2: Node podCIDRs recorded
CIDR1=$(ssh controlplane 'grep -E "^node01=" /opt/k8s/node-podcidrs.txt 2>/dev/null || true')
CIDR2=$(ssh controlplane 'grep -E "^node02=" /opt/k8s/node-podcidrs.txt 2>/dev/null || true')
ACTUAL1=$(ssh controlplane 'kubectl get node node01 -o jsonpath="{.spec.podCIDR}" 2>/dev/null || true')
ACTUAL2=$(ssh controlplane 'kubectl get node node02 -o jsonpath="{.spec.podCIDR}" 2>/dev/null || true')

if [ "$CIDR1" == "node01=$ACTUAL1" ] && [ "$CIDR2" == "node02=$ACTUAL2" ]; then
  echo -e "${GREEN}[PASS] Task 2: Node podCIDRs correctly recorded ($ACTUAL1, $ACTUAL2).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Node podCIDRs mismatch. Expected node01=$ACTUAL1 and node02=$ACTUAL2.${NC}"
fi

# Task 3: DaemonSet net-mesh running on worker nodes
READY_DS=$(ssh controlplane 'kubectl get ds net-mesh -n w7d1-net -o jsonpath="{.status.numberReady}" 2>/dev/null || echo "0"')
DESIRED_DS=$(ssh controlplane 'kubectl get ds net-mesh -n w7d1-net -o jsonpath="{.status.desiredNumberScheduled}" 2>/dev/null || echo "0"')
if [ "$READY_DS" -ge 2 ] && [ "$READY_DS" -eq "$DESIRED_DS" ]; then
  echo -e "${GREEN}[PASS] Task 3: DaemonSet net-mesh has $READY_DS/$DESIRED_DS ready pods.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: DaemonSet net-mesh ready pods: $READY_DS (expected >= 2).${NC}"
fi""",
        "cka_solution": """1. Check `/etc/cni/net.d/`:
`ls /etc/cni/net.d/`
`cat /etc/cni/net.d/*.conflist`
Write the plugin type to `/opt/k8s/cni-plugin-type.txt` (e.g. `flannel`).

2. Extract node podCIDRs:
```bash
echo "node01=$(kubectl get node node01 -o jsonpath='{.spec.podCIDR}')" > /opt/k8s/node-podcidrs.txt
echo "node02=$(kubectl get node node02 -o jsonpath='{.spec.podCIDR}')" >> /opt/k8s/node-podcidrs.txt
```

3. Deploy DaemonSet `net-mesh`:
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: net-mesh
  namespace: w7d1-net
spec:
  selector:
    matchLabels:
      app: net-mesh
  template:
    metadata:
      labels:
        app: net-mesh
    spec:
      containers:
      - name: busybox
        image: busybox:1.36
        command: ["sleep", "3600"]
```
`kubectl apply -f net-mesh.yaml`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w7d1-net --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/cni-plugin-type.txt /opt/k8s/node-podcidrs.txt
'""",

        "lfcs_title": "Linux Networking Configuration (IP & Routing)",
        "lfcs_diff": "Medium",
        "lfcs_time": "35m",
        "lfcs_tasks": """### Task 1: Create Dummy Network Interface
1. Create a dummy network interface named `dummy0` using `ip link`:
   `sudo ip link add dummy0 type dummy`
2. Bring the interface UP:
   `sudo ip link set dummy0 up`

### Task 2: Assign Static IP Address
1. Assign secondary static IP `10.10.20.50/24` to interface `dummy0`:
   `sudo ip addr add 10.10.20.50/24 dev dummy0`

### Task 3: Static Route Configuration
1. Add a static route for destination subnet `10.200.0.0/16` routed via device `dummy0`:
   `sudo ip route add 10.200.0.0/16 dev dummy0`

### Task 4: Network Diagnostic Audit Script
1. Create an executable bash script `/usr/local/bin/network_audit.sh`.
2. The script must write:
   - The default routing line (`ip route show default`)
   - All active nameserver entries from `/etc/resolv.conf` (`grep nameserver /etc/resolv.conf`)
   into `/var/log/network_audit.log`.
3. Set executable permissions on `/usr/local/bin/network_audit.sh` and run it once to initialize the log.""",
        "lfcs_setup": """sudo ip link del dummy0 2>/dev/null || true
sudo rm -f /usr/local/bin/network_audit.sh /var/log/network_audit.log""",
        "lfcs_verify": """SCORE=0; TOTAL=4
# Task 1: dummy0 interface exists and is up
if ip link show dummy0 2>/dev/null | grep -q "state UP\\|UP"; then
  echo -e "${GREEN}[PASS] Task 1: Interface dummy0 is UP.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Interface dummy0 missing or not UP.${NC}"
fi

# Task 2: IP 10.10.20.50/24 assigned to dummy0
if ip addr show dev dummy0 2>/dev/null | grep -q "10.10.20.50/24"; then
  echo -e "${GREEN}[PASS] Task 2: IP 10.10.20.50/24 assigned to dummy0.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: IP 10.10.20.50/24 not found on dummy0.${NC}"
fi

# Task 3: Route 10.200.0.0/16 exists
if ip route show 10.200.0.0/16 2>/dev/null | grep -q "dummy0"; then
  echo -e "${GREEN}[PASS] Task 3: Static route 10.200.0.0/16 via dummy0 exists.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Route 10.200.0.0/16 via dummy0 not found.${NC}"
fi

# Task 4: Audit script & log
if [ -x /usr/local/bin/network_audit.sh ] && [ -f /var/log/network_audit.log ] && grep -q "default" /var/log/network_audit.log && grep -q "nameserver" /var/log/network_audit.log; then
  echo -e "${GREEN}[PASS] Task 4: /usr/local/bin/network_audit.sh and /var/log/network_audit.log verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: Audit script or log file invalid.${NC}"
fi""",
        "lfcs_solution": """1. Create interface dummy0 and bring UP:
`sudo ip link add dummy0 type dummy`
`sudo ip link set dummy0 up`

2. Assign IP:
`sudo ip addr add 10.10.20.50/24 dev dummy0`

3. Add route:
`sudo ip route add 10.200.0.0/16 dev dummy0`

4. Create script `/usr/local/bin/network_audit.sh`:
```bash
sudo bash -c 'cat << "EOF" > /usr/local/bin/network_audit.sh
#!/usr/bin/env bash
ip route show default > /var/log/network_audit.log
grep nameserver /etc/resolv.conf >> /var/log/network_audit.log
EOF'
sudo chmod +x /usr/local/bin/network_audit.sh
sudo /usr/local/bin/network_audit.sh
```""",
        "lfcs_reset": """sudo ip link del dummy0 2>/dev/null || true
sudo rm -f /usr/local/bin/network_audit.sh /var/log/network_audit.log""",
    },

    # Day 2
    {
        "day": 2,
        "date": "2026-11-10",
        "cka_title": "Service Networking & CoreDNS Deep Dive",
        "cka_diff": "Medium",
        "cka_time": "35m",
        "cka_tasks": """### Task 1: ClusterIP Service Deployment
In namespace `w7d2-dns`:
1. Deploy a Deployment named `backend-app` with 2 replicas using image `nginx:alpine` (port 80, labels `app=backend-app`).
2. Create a ClusterIP Service named `backend-svc` exposing port `8080` targeting pod port `80`.

### Task 2: NodePort Service Deployment
In namespace `w7d2-dns`:
1. Deploy a Deployment named `frontend-app` with 1 replica using image `nginx:alpine` (port 80, labels `app=frontend-app`).
2. Create a Service named `frontend-nodeport` of type `NodePort` mapping port `80` (targetPort 80) to static `nodePort: 30080`.

### Task 3: CoreDNS Name Resolution Test
1. Run a one-off diagnostic pod `dns-tester` (image `busybox:1.36`, restart policy `Never`) in namespace `w7d2-dns`.
2. Inside the pod, run `nslookup backend-svc.w7d2-dns.svc.cluster.local`.
3. Save the DNS resolution output to `/opt/k8s/dns_resolution.txt` on `controlplane`.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w7d2-dns --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d2-dns
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/dns_resolution.txt
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: backend-svc ClusterIP
SVC_PORT=$(ssh controlplane 'kubectl get svc backend-svc -n w7d2-dns -o jsonpath="{.spec.ports[0].port}" 2>/dev/null || echo "0"')
SVC_TARGET=$(ssh controlplane 'kubectl get svc backend-svc -n w7d2-dns -o jsonpath="{.spec.ports[0].targetPort}" 2>/dev/null || echo "0"')
EP_COUNT=$(ssh controlplane 'kubectl get endpoints backend-svc -n w7d2-dns -o jsonpath="{.subsets[0].addresses[*].ip}" 2>/dev/null | wc -w')
if [ "$SVC_PORT" == "8080" ] && [ "$SVC_TARGET" == "80" ] && [ "$EP_COUNT" -ge 2 ]; then
  echo -e "${GREEN}[PASS] Task 1: backend-svc ClusterIP verified with 2 ready endpoints.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: backend-svc port=$SVC_PORT (exp 8080), target=$SVC_TARGET (exp 80), endpoints=$EP_COUNT (exp >=2).${NC}"
fi

# Task 2: frontend-nodeport NodePort 30080
NP_TYPE=$(ssh controlplane 'kubectl get svc frontend-nodeport -n w7d2-dns -o jsonpath="{.spec.type}" 2>/dev/null || echo "None"')
NODE_PORT=$(ssh controlplane 'kubectl get svc frontend-nodeport -n w7d2-dns -o jsonpath="{.spec.ports[0].nodePort}" 2>/dev/null || echo "0"')
if [ "$NP_TYPE" == "NodePort" ] && [ "$NODE_PORT" == "30080" ]; then
  echo -e "${GREEN}[PASS] Task 2: frontend-nodeport verified on NodePort 30080.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: frontend-nodeport type=$NP_TYPE (exp NodePort), nodePort=$NODE_PORT (exp 30080).${NC}"
fi

# Task 3: DNS resolution file exists and contains resolved IP
BACKEND_IP=$(ssh controlplane 'kubectl get svc backend-svc -n w7d2-dns -o jsonpath="{.spec.clusterIP}" 2>/dev/null || echo "MISSING"')
if ssh controlplane "test -s /opt/k8s/dns_resolution.txt && grep -q '$BACKEND_IP' /opt/k8s/dns_resolution.txt"; then
  echo -e "${GREEN}[PASS] Task 3: CoreDNS resolution verified for backend-svc ($BACKEND_IP).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /opt/k8s/dns_resolution.txt missing or does not contain clusterIP $BACKEND_IP.${NC}"
fi""",
        "cka_solution": """1. Deploy backend and ClusterIP service:
```bash
kubectl create deployment backend-app -n w7d2-dns --image=nginx:alpine --replicas=2
kubectl expose deployment backend-app -n w7d2-dns --name=backend-svc --port=8080 --target-port=80
```

2. Deploy frontend and NodePort service:
```bash
kubectl create deployment frontend-app -n w7d2-dns --image=nginx:alpine --replicas=1
kubectl create service nodeport frontend-nodeport -n w7d2-dns --tcp=80:80 --node-port=30080
kubectl set selector service frontend-nodeport -n w7d2-dns app=frontend-app
```

3. Test CoreDNS resolution:
```bash
kubectl run dns-tester -n w7d2-dns --image=busybox:1.36 --restart=Never --command -- nslookup backend-svc.w7d2-dns.svc.cluster.local
# Wait 3 seconds, then capture logs:
kubectl logs dns-tester -n w7d2-dns > /opt/k8s/dns_resolution.txt
```""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w7d2-dns --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/dns_resolution.txt
'""",

        "lfcs_title": "Network Bonding & Bridging",
        "lfcs_diff": "Medium",
        "lfcs_time": "35m",
        "lfcs_tasks": """### Task 1: Create Linux Software Bridge
1. Create a software bridge interface named `br0` using `ip link`:
   `sudo ip link add br0 type bridge`
2. Assign IP address `192.168.100.1/24` to `br0`.
3. Bring `br0` interface UP.

### Task 2: Create Virtual Ethernet Pair (veth)
1. Create a virtual ethernet pair named `veth-host` and `veth-guest`:
   `sudo ip link add veth-host type veth peer name veth-guest`

### Task 3: Attach Slave Interface to Bridge
1. Attach `veth-host` to bridge `br0` as a master bridge port:
   `sudo ip link set veth-host master br0`
2. Bring `veth-host` and `veth-guest` interfaces UP:
   `sudo ip link set veth-host up`
   `sudo ip link set veth-guest up`""",
        "lfcs_setup": """sudo ip link del veth-host 2>/dev/null || true
sudo ip link del br0 2>/dev/null || true""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: Bridge br0 has IP 192.168.100.1/24 and is up
if ip addr show dev br0 2>/dev/null | grep -q "192.168.100.1/24"; then
  echo -e "${GREEN}[PASS] Task 1: Bridge br0 exists with IP 192.168.100.1/24.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Bridge br0 missing or IP 192.168.100.1/24 not assigned.${NC}"
fi

# Task 2: veth pair exists
if ip link show dev veth-guest >/dev/null 2>&1 && ip link show dev veth-host >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 2: Virtual ethernet pair veth-host and veth-guest created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: veth pair missing.${NC}"
fi

# Task 3: veth-host attached to br0 as master
MASTER=$(ip link show dev veth-host 2>/dev/null | grep -o "master br0" || true)
if [ "$MASTER" == "master br0" ]; then
  echo -e "${GREEN}[PASS] Task 3: veth-host attached to master bridge br0.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: veth-host master is not br0.${NC}"
fi""",
        "lfcs_solution": """1. Create bridge br0:
`sudo ip link add br0 type bridge`
`sudo ip addr add 192.168.100.1/24 dev br0`
`sudo ip link set br0 up`

2. Create veth pair:
`sudo ip link add veth-host type veth peer name veth-guest`

3. Attach to bridge and bring up:
`sudo ip link set veth-host master br0`
`sudo ip link set veth-host up`
`sudo ip link set veth-guest up`""",
        "lfcs_reset": """sudo ip link del veth-host 2>/dev/null || true
sudo ip link del br0 2>/dev/null || true""",
    },

    # Day 3
    {
        "day": 3,
        "date": "2026-11-11",
        "cka_title": "Ingress Controllers & Routing Rules",
        "cka_diff": "Medium",
        "cka_time": "35m",
        "cka_tasks": """### Task 1: Deploy Backend Microservices
In namespace `w7d3-ingress`:
1. Deploy `catalog` (image: `nginx:alpine`, port 80, 1 replica) and expose it via ClusterIP Service `catalog-svc` on port 80.
2. Deploy `orders` (image: `httpd:alpine`, port 80, 1 replica) and expose it via ClusterIP Service `orders-svc` on port 80.

### Task 2: Ingress Resource with Path-Based Routing
Create an Ingress resource named `store-ingress` in namespace `w7d3-ingress`:
- `ingressClassName: nginx`
- Host: `store.internal.example.com`
- Paths:
  - Path `/catalog` with pathType `Prefix` routed to backend service `catalog-svc` port `80`.
  - Path `/orders` with pathType `Prefix` routed to backend service `orders-svc` port `80`.

### Task 3: Rewrite Annotation
Add the rewrite target annotation to `store-ingress`:
`nginx.ingress.kubernetes.io/rewrite-target: /`""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w7d3-ingress --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d3-ingress
  kubectl create deployment catalog -n w7d3-ingress --image=nginx:alpine --port=80
  kubectl expose deployment catalog -n w7d3-ingress --name=catalog-svc --port=80
  kubectl create deployment orders -n w7d3-ingress --image=httpd:alpine --port=80
  kubectl expose deployment orders -n w7d3-ingress --name=orders-svc --port=80
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: Services catalog-svc and orders-svc active
CSVC=$(ssh controlplane 'kubectl get svc catalog-svc -n w7d3-ingress -o jsonpath="{.spec.ports[0].port}" 2>/dev/null || echo "0"')
OSVC=$(ssh controlplane 'kubectl get svc orders-svc -n w7d3-ingress -o jsonpath="{.spec.ports[0].port}" 2>/dev/null || echo "0"')
if [ "$CSVC" == "80" ] && [ "$OSVC" == "80" ]; then
  echo -e "${GREEN}[PASS] Task 1: Backend services catalog-svc and orders-svc active on port 80.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Services missing or ports incorrect (catalog-svc=$CSVC, orders-svc=$OSVC).${NC}"
fi

# Task 2: Ingress store-ingress host and path routing
HOST=$(ssh controlplane 'kubectl get ingress store-ingress -n w7d3-ingress -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo "None"')
P1=$(ssh controlplane 'kubectl get ingress store-ingress -n w7d3-ingress -o jsonpath="{.spec.rules[0].http.paths[?(@.path==\"/catalog\")].backend.service.name}" 2>/dev/null || echo "None"')
P2=$(ssh controlplane 'kubectl get ingress store-ingress -n w7d3-ingress -o jsonpath="{.spec.rules[0].http.paths[?(@.path==\"/orders\")].backend.service.name}" 2>/dev/null || echo "None"')

if [ "$HOST" == "store.internal.example.com" ] && [ "$P1" == "catalog-svc" ] && [ "$P2" == "orders-svc" ]; then
  echo -e "${GREEN}[PASS] Task 2: Ingress store-ingress routes host $HOST to catalog-svc and orders-svc.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Ingress routing mismatch (host=$HOST, /catalog=$P1, /orders=$P2).${NC}"
fi

# Task 3: Rewrite annotation
REWRITE=$(ssh controlplane 'kubectl get ingress store-ingress -n w7d3-ingress -o jsonpath="{.metadata.annotations.nginx\\.ingress\\.kubernetes\\.io/rewrite-target}" 2>/dev/null || echo "None"')
if [ "$REWRITE" == "/" ]; then
  echo -e "${GREEN}[PASS] Task 3: Rewrite annotation nginx.ingress.kubernetes.io/rewrite-target: / verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Rewrite annotation is $REWRITE (expected /).${NC}"
fi""",
        "cka_solution": """Create manifest `store-ingress.yaml`:
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: store-ingress
  namespace: w7d3-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: store.internal.example.com
    http:
      paths:
      - path: /catalog
        pathType: Prefix
        backend:
          service:
            name: catalog-svc
            port:
              number: 80
      - path: /orders
        pathType: Prefix
        backend:
          service:
            name: orders-svc
            port:
              number: 80
```
`kubectl apply -f store-ingress.yaml`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w7d3-ingress --grace-period=0 --force 2>/dev/null || true
'""",

        "lfcs_title": "Packet Filtering with Firewalld & Iptables",
        "lfcs_diff": "Medium",
        "lfcs_time": "35m",
        "lfcs_tasks": """### Task 1: Block Port with Iptables
1. Append a rule to the `INPUT` chain that drops all incoming TCP packets destined for port `8088`:
   `sudo iptables -A INPUT -p tcp --dport 8088 -j DROP`

### Task 2: Allow Subnet ICMP Traffic
1. Insert a rule at position 1 in the `INPUT` chain that explicitly allows incoming ICMP echo-requests (ping) originating from `192.168.0.0/16`:
   `sudo iptables -I INPUT 1 -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT`

### Task 3: Backup Active Iptables Rules
1. Export the active IPv4 iptables ruleset to `/var/tmp/iptables_backup.rules` using `iptables-save`:
   `sudo iptables-save | sudo tee /var/tmp/iptables_backup.rules > /dev/null`""",
        "lfcs_setup": """sudo iptables -D INPUT -p tcp --dport 8088 -j DROP 2>/dev/null || true
sudo iptables -D INPUT -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT 2>/dev/null || true
sudo rm -f /var/tmp/iptables_backup.rules""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: DROP rule for port 8088
if sudo iptables -S INPUT | grep -q -- "-p tcp -m tcp --dport 8088 -j DROP\\|-p tcp --dport 8088 -j DROP"; then
  echo -e "${GREEN}[PASS] Task 1: Iptables rule dropping port 8088 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: DROP rule for port 8088 not found in INPUT chain.${NC}"
fi

# Task 2: ACCEPT rule for ICMP from 192.168.0.0/16
if sudo iptables -S INPUT | grep -q -- "-p icmp -m icmp --icmp-type 8 -s 192.168.0.0/16 -j ACCEPT\\|-s 192.168.0.0/16.*-p icmp.*-j ACCEPT"; then
  echo -e "${GREEN}[PASS] Task 2: Iptables rule allowing ICMP from 192.168.0.0/16 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: ACCEPT rule for ICMP from 192.168.0.0/16 not found in INPUT chain.${NC}"
fi

# Task 3: Rules backup file exists
if [ -s /var/tmp/iptables_backup.rules ] && grep -q "8088" /var/tmp/iptables_backup.rules; then
  echo -e "${GREEN}[PASS] Task 3: Active iptables rules successfully backed up to /var/tmp/iptables_backup.rules.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/iptables_backup.rules missing or empty.${NC}"
fi""",
        "lfcs_solution": """1. Block port 8088:
`sudo iptables -A INPUT -p tcp --dport 8088 -j DROP`

2. Allow ICMP echo from 192.168.0.0/16:
`sudo iptables -I INPUT 1 -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT`

3. Save rules:
`sudo iptables-save | sudo tee /var/tmp/iptables_backup.rules > /dev/null`""",
        "lfcs_reset": """sudo iptables -D INPUT -p tcp --dport 8088 -j DROP 2>/dev/null || true
sudo iptables -D INPUT -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT 2>/dev/null || true
sudo rm -f /var/tmp/iptables_backup.rules""",
    },

    # Day 4
    {
        "day": 4,
        "date": "2026-11-12",
        "cka_title": "Gateway API (2025 Updates)",
        "cka_diff": "Medium",
        "cka_time": "35m",
        "cka_tasks": """### Task 1: Verify GatewayClass
A GatewayClass named `cluster-gateway-class` is available in the cluster.
- Inspect it with `kubectl get gatewayclasses cluster-gateway-class`.

### Task 2: Create Gateway
In namespace `w7d4-gw`:
1. Create a Gateway resource named `prod-gateway`:
   - `gatewayClassName`: `cluster-gateway-class`
   - Listeners:
     - `name`: `http`
     - `port`: `80`
     - `protocol`: `HTTP`
     - `allowedRoutes`: `{ "namespaces": { "from": "Same" } }`

### Task 3: Create HTTPRoute
In namespace `w7d4-gw`:
1. Create an `HTTPRoute` resource named `api-route`:
   - Parent reference to `prod-gateway` (sectionName: `http`)
   - Hostname: `api.example.com`
   - Rules:
     - Match path prefix `/v1`
     - Route to backend service `api-service` on port `8080`.""",
        "cka_setup": """ssh controlplane '
  kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.1.0/standard-install.yaml 2>/dev/null || true
  kubectl delete namespace w7d4-gw --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d4-gw
  cat << "EOF" | kubectl apply -f - 2>/dev/null || true
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: cluster-gateway-class
spec:
  controllerName: example.com/gateway-controller
EOF
  kubectl create deployment api-service -n w7d4-gw --image=nginx:alpine --port=8080
  kubectl expose deployment api-service -n w7d4-gw --port=8080
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: GatewayClass exists
GW_CLASS=$(ssh controlplane 'kubectl get gatewayclass cluster-gateway-class -o jsonpath="{.spec.controllerName}" 2>/dev/null || echo "None"')
if [ "$GW_CLASS" != "None" ]; then
  echo -e "${GREEN}[PASS] Task 1: GatewayClass cluster-gateway-class verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: GatewayClass cluster-gateway-class not found.${NC}"
fi

# Task 2: Gateway prod-gateway in w7d4-gw
GW_NAME=$(ssh controlplane 'kubectl get gateway prod-gateway -n w7d4-gw -o jsonpath="{.metadata.name}" 2>/dev/null || echo "None"')
GW_PORT=$(ssh controlplane 'kubectl get gateway prod-gateway -n w7d4-gw -o jsonpath="{.spec.listeners[0].port}" 2>/dev/null || echo "0"')
if [ "$GW_NAME" == "prod-gateway" ] && [ "$GW_PORT" == "80" ]; then
  echo -e "${GREEN}[PASS] Task 2: Gateway prod-gateway listening on HTTP port 80 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Gateway prod-gateway missing or port is $GW_PORT (expected 80).${NC}"
fi

# Task 3: HTTPRoute api-route
ROUTE_NAME=$(ssh controlplane 'kubectl get httproute api-route -n w7d4-gw -o jsonpath="{.metadata.name}" 2>/dev/null || echo "None"')
ROUTE_BACKEND=$(ssh controlplane 'kubectl get httproute api-route -n w7d4-gw -o jsonpath="{.spec.rules[0].backendRefs[0].name}" 2>/dev/null || echo "None"')
if [ "$ROUTE_NAME" == "api-route" ] && [ "$ROUTE_BACKEND" == "api-service" ]; then
  echo -e "${GREEN}[PASS] Task 3: HTTPRoute api-route routes to api-service.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: HTTPRoute api-route invalid (name=$ROUTE_NAME, backend=$ROUTE_BACKEND).${NC}"
fi""",
        "cka_solution": """1. Create Gateway manifest `gateway.yaml`:
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: prod-gateway
  namespace: w7d4-gw
spec:
  gatewayClassName: cluster-gateway-class
  listeners:
  - name: http
    port: 80
    protocol: HTTP
    allowedRoutes:
      namespaces:
        from: Same
```
`kubectl apply -f gateway.yaml`

2. Create HTTPRoute manifest `httproute.yaml`:
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: api-route
  namespace: w7d4-gw
spec:
  parentRefs:
  - name: prod-gateway
    sectionName: http
  hostnames:
  - "api.example.com"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /v1
    backendRefs:
    - name: api-service
      port: 8080
```
`kubectl apply -f httproute.yaml`""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w7d4-gw --grace-period=0 --force 2>/dev/null || true
  kubectl delete gatewayclass cluster-gateway-class 2>/dev/null || true
'""",

        "lfcs_title": "NAT, Port Redirection & Reverse Proxies",
        "lfcs_diff": "Medium",
        "lfcs_time": "35m",
        "lfcs_tasks": """### Task 1: Kernel IP Packet Forwarding
1. Configure persistent IP packet forwarding in `/etc/sysctl.d/99-ipforward.conf`:
   `net.ipv4.ip_forward = 1`
2. Apply the setting immediately:
   `sudo sysctl -p /etc/sysctl.d/99-ipforward.conf`

### Task 2: Iptables NAT Port Redirection
1. Configure an iptables NAT table `PREROUTING` rule to redirect incoming TCP traffic on port `8080` to local port `80`:
   `sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-ports 80`

### Task 3: Reverse Proxy Configuration Template
1. Create a reverse proxy configuration file at `/var/tmp/reverse_proxy.conf` simulating an Nginx proxy pass:
```nginx
server {
    listen 8888;
    server_name localhost;

    location / {
        proxy_pass http://127.0.0.1:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```""",
        "lfcs_setup": """sudo rm -f /etc/sysctl.d/99-ipforward.conf /var/tmp/reverse_proxy.conf
sudo sysctl -w net.ipv4.ip_forward=0 >/dev/null 2>&1 || true
sudo iptables -t nat -D PREROUTING -p tcp --dport 8080 -j REDIRECT --to-ports 80 2>/dev/null || true""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: IP forward enabled in sysctl and file
SYSCTL_VAL=$(sysctl -n net.ipv4.ip_forward 2>/dev/null || echo "0")
if [ "$SYSCTL_VAL" == "1" ] && grep -q "net.ipv4.ip_forward.*=.*1" /etc/sysctl.d/99-ipforward.conf 2>/dev/null; then
  echo -e "${GREEN}[PASS] Task 1: IP packet forwarding enabled persistently.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: net.ipv4.ip_forward is $SYSCTL_VAL or /etc/sysctl.d/99-ipforward.conf missing.${NC}"
fi

# Task 2: iptables NAT redirection
if sudo iptables -t nat -S PREROUTING | grep -q -- "-p tcp -m tcp --dport 8080 -j REDIRECT --to-ports 80\\|-p tcp --dport 8080 -j REDIRECT --to-ports 80"; then
  echo -e "${GREEN}[PASS] Task 2: Iptables PREROUTING redirection 8080 -> 80 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: NAT PREROUTING redirection for port 8080 not found.${NC}"
fi

# Task 3: Reverse proxy configuration template
if [ -s /var/tmp/reverse_proxy.conf ] && grep -q "listen 8888" /var/tmp/reverse_proxy.conf && grep -q "proxy_pass http://127.0.0.1:80" /var/tmp/reverse_proxy.conf; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/reverse_proxy.conf reverse proxy configuration verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/reverse_proxy.conf missing or proxy settings incorrect.${NC}"
fi""",
        "lfcs_solution": """1. Configure persistent IP forwarding:
```bash
echo "net.ipv4.ip_forward = 1" | sudo tee /etc/sysctl.d/99-ipforward.conf
sudo sysctl -p /etc/sysctl.d/99-ipforward.conf
```

2. Configure NAT port redirect:
`sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-ports 80`

3. Create `/var/tmp/reverse_proxy.conf`:
```bash
cat << "EOF" > /var/tmp/reverse_proxy.conf
server {
    listen 8888;
    server_name localhost;

    location / {
        proxy_pass http://127.0.0.1:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
EOF
```""",
        "lfcs_reset": """sudo rm -f /etc/sysctl.d/99-ipforward.conf /var/tmp/reverse_proxy.conf
sudo iptables -t nat -D PREROUTING -p tcp --dport 8080 -j REDIRECT --to-ports 80 2>/dev/null || true""",
    },

    # Day 5
    {
        "day": 5,
        "date": "2026-11-13",
        "cka_title": "Network Policies Deep Dive",
        "cka_diff": "Medium",
        "cka_time": "35m",
        "cka_tasks": """### Task 1: Default-Deny Ingress Policy
In namespace `w7d5-netpol`:
Create a NetworkPolicy named `default-deny-ingress` that selects all pods (`podSelector: {}`) and denies all incoming ingress traffic.

### Task 2: Allow Frontend to Backend
In namespace `w7d5-netpol`:
Create a NetworkPolicy named `allow-fe-to-be`:
- `podSelector`: matching pods with label `role: backend`
- Ingress allowed only from pods labeled `role: frontend` on TCP port `80`.

### Task 3: Allow Backend to Database
In namespace `w7d5-netpol`:
Create a NetworkPolicy named `allow-be-to-db`:
- `podSelector`: matching pods with label `role: db`
- Ingress allowed only from pods labeled `role: backend` on TCP port `5432`.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w7d5-netpol --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d5-netpol
  kubectl run frontend -n w7d5-netpol --image=nginx:alpine --labels=role=frontend
  kubectl run backend -n w7d5-netpol --image=nginx:alpine --labels=role=backend
  kubectl run database -n w7d5-netpol --image=nginx:alpine --labels=role=db
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: default-deny-ingress
DD_MATCH=$(ssh controlplane 'kubectl get netpol default-deny-ingress -n w7d5-netpol -o jsonpath="{.spec.policyTypes[0]}" 2>/dev/null || echo "None"')
if [ "$DD_MATCH" == "Ingress" ]; then
  echo -e "${GREEN}[PASS] Task 1: default-deny-ingress policy verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: default-deny-ingress missing or policyType is $DD_MATCH.${NC}"
fi

# Task 2: allow-fe-to-be
FE_PORT=$(ssh controlplane 'kubectl get netpol allow-fe-to-be -n w7d5-netpol -o jsonpath="{.spec.ingress[0].ports[0].port}" 2>/dev/null || echo "0"')
FE_FROM=$(ssh controlplane 'kubectl get netpol allow-fe-to-be -n w7d5-netpol -o jsonpath="{.spec.ingress[0].from[0].podSelector.matchLabels.role}" 2>/dev/null || echo "None"')
if [ "$FE_PORT" == "80" ] && [ "$FE_FROM" == "frontend" ]; then
  echo -e "${GREEN}[PASS] Task 2: allow-fe-to-be allows role=frontend on port 80.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: allow-fe-to-be incorrect (from=$FE_FROM, port=$FE_PORT).${NC}"
fi

# Task 3: allow-be-to-db
DB_PORT=$(ssh controlplane 'kubectl get netpol allow-be-to-db -n w7d5-netpol -o jsonpath="{.spec.ingress[0].ports[0].port}" 2>/dev/null || echo "0"')
DB_FROM=$(ssh controlplane 'kubectl get netpol allow-be-to-db -n w7d5-netpol -o jsonpath="{.spec.ingress[0].from[0].podSelector.matchLabels.role}" 2>/dev/null || echo "None"')
if [ "$DB_PORT" == "5432" ] && [ "$DB_FROM" == "backend" ]; then
  echo -e "${GREEN}[PASS] Task 3: allow-be-to-db allows role=backend on port 5432.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: allow-be-to-db incorrect (from=$DB_FROM, port=$DB_PORT).${NC}"
fi""",
        "cka_solution": """1. Create `default-deny-ingress`:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: w7d5-netpol
spec:
  podSelector: {}
  policyTypes:
  - Ingress
```

2. Create `allow-fe-to-be`:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-fe-to-be
  namespace: w7d5-netpol
spec:
  podSelector:
    matchLabels:
      role: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
    ports:
    - protocol: TCP
      port: 80
```

3. Create `allow-be-to-db`:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-be-to-db
  namespace: w7d5-netpol
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: backend
    ports:
    - protocol: TCP
      port: 5432
```""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w7d5-netpol --grace-period=0 --force 2>/dev/null || true
'""",

        "lfcs_title": "SSH Hardening, Key Auth & Time Sync",
        "lfcs_diff": "Medium",
        "lfcs_time": "35m",
        "lfcs_tasks": """### Task 1: Generate & Authorize RSA SSH Key Pair
1. For user `student`, generate a 4096-bit RSA SSH key pair at `/home/student/.ssh/id_admin_rsa` without a passphrase:
   `ssh-keygen -t rsa -b 4096 -N "" -f /home/student/.ssh/id_admin_rsa`
2. Append the public key to `/home/student/.ssh/authorized_keys`.
3. Ensure file permissions are `0600` on `authorized_keys` and `0700` on `~/.ssh`.

### Task 2: SSH Server Configuration Hardening
1. Create a drop-in configuration file `/etc/ssh/sshd_config.d/99-hardening.conf` containing:
   ```
   PermitRootLogin no
   MaxAuthTries 3
   ClientAliveInterval 300
   ClientAliveCountMax 2
   ```
2. Test configuration syntax using `sudo sshd -t`.

### Task 3: Time Synchronization Verification
1. Ensure system NTP synchronization is active using `timedatectl`:
   `sudo timedatectl set-ntp true`
2. Confirm system clock synchronization state using `timedatectl status`.""",
        "lfcs_setup": """sudo rm -f /home/student/.ssh/id_admin_rsa /home/student/.ssh/id_admin_rsa.pub /etc/ssh/sshd_config.d/99-hardening.conf""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: Key exists, 4096 bit, authorized_keys has 0600
KEY_BITS=$(ssh-keygen -l -f /home/student/.ssh/id_admin_rsa 2>/dev/null | awk '{print $1}')
AUTH_PERMS=$(stat -c "%a" /home/student/.ssh/authorized_keys 2>/dev/null || echo "000")
if [ "$KEY_BITS" == "4096" ] && [ "$AUTH_PERMS" == "600" ]; then
  echo -e "${GREEN}[PASS] Task 1: 4096-bit SSH key generated and authorized_keys permissions verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Key bits=$KEY_BITS (exp 4096), authorized_keys perms=$AUTH_PERMS (exp 600).${NC}"
fi

# Task 2: sshd hardening drop-in and test
if [ -f /etc/ssh/sshd_config.d/99-hardening.conf ] && grep -q "PermitRootLogin no" /etc/ssh/sshd_config.d/99-hardening.conf && grep -q "MaxAuthTries 3" /etc/ssh/sshd_config.d/99-hardening.conf && sudo sshd -t; then
  echo -e "${GREEN}[PASS] Task 2: /etc/ssh/sshd_config.d/99-hardening.conf verified and sshd -t passed.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: sshd hardening configuration missing or syntax test failed.${NC}"
fi

# Task 3: NTP active
NTP_STATUS=$(timedatectl show -p NTP --value 2>/dev/null || echo "no")
if [ "$NTP_STATUS" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 3: System NTP synchronization is active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: NTP synchronization is $NTP_STATUS (expected yes).${NC}"
fi""",
        "lfcs_solution": """1. Generate key and authorize:
```bash
ssh-keygen -t rsa -b 4096 -N "" -f /home/student/.ssh/id_admin_rsa
cat /home/student/.ssh/id_admin_rsa.pub >> /home/student/.ssh/authorized_keys
chmod 700 /home/student/.ssh
chmod 600 /home/student/.ssh/authorized_keys
```

2. Hardening drop-in:
```bash
sudo bash -c 'cat << "EOF" > /etc/ssh/sshd_config.d/99-hardening.conf
PermitRootLogin no
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 2
EOF'
sudo sshd -t
```

3. Enable NTP:
`sudo timedatectl set-ntp true`""",
        "lfcs_reset": """sudo rm -f /home/student/.ssh/id_admin_rsa /home/student/.ssh/id_admin_rsa.pub /etc/ssh/sshd_config.d/99-hardening.conf""",
    },

    # Day 6
    {
        "day": 6,
        "date": "2026-11-14",
        "cka_title": "Week 7 Network Mastery Triathlon",
        "cka_diff": "Hard (Milestone)",
        "cka_time": "45m",
        "cka_tasks": """### Task 1: Multi-Service Architecture
In namespace `w7d6-triathlon`:
1. Deploy `web-frontend` (image `nginx:alpine`, 2 replicas, port 80, label `app=web-frontend`) and expose with ClusterIP service `frontend-svc` on port 80.
2. Deploy `api-backend` (image `nginx:alpine`, 2 replicas, port 80, label `app=api-backend`) and expose with ClusterIP service `backend-svc` on port 80.

### Task 2: TLS Secret & Ingress Routing
In namespace `w7d6-triathlon`:
1. Generate a self-signed TLS cert and private key for domain `triathlon.k8s.local` and create Secret `triathlon-tls`.
2. Create an Ingress named `triathlon-ingress` with `ingressClassName: nginx`:
   - Host: `triathlon.k8s.local`
   - TLS enabled using Secret `triathlon-tls`
   - Path `/api` (Prefix) -> `backend-svc:80`
   - Path `/` (Prefix) -> `frontend-svc:80`
   - Annotation `nginx.ingress.kubernetes.io/rewrite-target: /`

### Task 3: Network Isolation Policy
In namespace `w7d6-triathlon`:
1. Create a NetworkPolicy named `backend-isolation` targeting pods with `app: api-backend`.
2. Allow incoming traffic ONLY from pods with label `app: web-frontend` on TCP port `80`.""",
        "cka_setup": """ssh controlplane '
  kubectl delete namespace w7d6-triathlon --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d6-triathlon
'""",
        "cka_verify": """SCORE=0; TOTAL=3
# Task 1: Services frontend-svc and backend-svc
FE_EP=$(ssh controlplane 'kubectl get endpoints frontend-svc -n w7d6-triathlon -o jsonpath="{.subsets[0].addresses[*].ip}" 2>/dev/null | wc -w')
BE_EP=$(ssh controlplane 'kubectl get endpoints backend-svc -n w7d6-triathlon -o jsonpath="{.subsets[0].addresses[*].ip}" 2>/dev/null | wc -w')
if [ "$FE_EP" -ge 2 ] && [ "$BE_EP" -ge 2 ]; then
  echo -e "${GREEN}[PASS] Task 1: Multi-service endpoints verified (frontend=$FE_EP, backend=$BE_EP).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Service endpoints insufficient (frontend=$FE_EP, backend=$BE_EP, expected >=2).${NC}"
fi

# Task 2: Ingress with TLS
ING_TLS=$(ssh controlplane 'kubectl get ingress triathlon-ingress -n w7d6-triathlon -o jsonpath="{.spec.tls[0].secretName}" 2>/dev/null || echo "None"')
ING_HOST=$(ssh controlplane 'kubectl get ingress triathlon-ingress -n w7d6-triathlon -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo "None"')
if [ "$ING_TLS" == "triathlon-tls" ] && [ "$ING_HOST" == "triathlon.k8s.local" ]; then
  echo -e "${GREEN}[PASS] Task 2: Ingress triathlon-ingress with TLS termination verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Ingress TLS or host mismatch (tls=$ING_TLS, host=$ING_HOST).${NC}"
fi

# Task 3: NetworkPolicy backend-isolation
NP_TARGET=$(ssh controlplane 'kubectl get netpol backend-isolation -n w7d6-triathlon -o jsonpath="{.spec.podSelector.matchLabels.app}" 2>/dev/null || echo "None"')
NP_ALLOW=$(ssh controlplane 'kubectl get netpol backend-isolation -n w7d6-triathlon -o jsonpath="{.spec.ingress[0].from[0].podSelector.matchLabels.app}" 2>/dev/null || echo "None"')
if [ "$NP_TARGET" == "api-backend" ] && [ "$NP_ALLOW" == "web-frontend" ]; then
  echo -e "${GREEN}[PASS] Task 3: NetworkPolicy backend-isolation correctly restricts traffic.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: NetworkPolicy rule mismatch (target=$NP_TARGET, allow=$NP_ALLOW).${NC}"
fi""",
        "cka_solution": """1. Deploy services:
```bash
kubectl create deployment web-frontend -n w7d6-triathlon --image=nginx:alpine --replicas=2 --port=80
kubectl expose deployment web-frontend -n w7d6-triathlon --name=frontend-svc --port=80
kubectl create deployment api-backend -n w7d6-triathlon --image=nginx:alpine --replicas=2 --port=80
kubectl expose deployment api-backend -n w7d6-triathlon --name=backend-svc --port=80
```

2. Create TLS Secret and Ingress:
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /tmp/tls.key -out /tmp/tls.crt -subj "/CN=triathlon.k8s.local"
kubectl create secret tls triathlon-tls -n w7d6-triathlon --cert=/tmp/tls.crt --key=/tmp/tls.key
```
Ingress manifest:
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: triathlon-ingress
  namespace: w7d6-triathlon
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - triathlon.k8s.local
    secretName: triathlon-tls
  rules:
  - host: triathlon.k8s.local
    http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: backend-svc
            port:
              number: 80
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-svc
            port:
              number: 80
```

3. NetworkPolicy:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-isolation
  namespace: w7d6-triathlon
spec:
  podSelector:
    matchLabels:
      app: api-backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: web-frontend
    ports:
    - protocol: TCP
      port: 80
```""",
        "cka_reset": """ssh controlplane '
  kubectl delete namespace w7d6-triathlon --grace-period=0 --force 2>/dev/null || true
  rm -f /tmp/tls.key /tmp/tls.crt
'""",

        "lfcs_title": "Week 7 Linux Networking & Firewall Marathon",
        "lfcs_diff": "Hard (Milestone)",
        "lfcs_time": "45m",
        "lfcs_tasks": """### Task 1: Bridge Network Construction
1. Create a software bridge interface `br-marathon` with IP `172.25.1.1/24` and bring it UP:
   `sudo ip link add br-marathon type bridge`
   `sudo ip addr add 172.25.1.1/24 dev br-marathon`
   `sudo ip link set br-marathon up`

### Task 2: Virtual Interface Attachment
1. Create a veth pair `veth-m1` and `veth-m2`.
2. Attach `veth-m1` to `br-marathon` as a slave port.
3. Bring both `veth-m1` and `veth-m2` interfaces UP.

### Task 3: Firewall Filtering & NAT Redirection
1. Redirect incoming TCP traffic on port `9090` to local port `80` using iptables NAT table PREROUTING chain:
   `sudo iptables -t nat -A PREROUTING -p tcp --dport 9090 -j REDIRECT --to-ports 80`
2. Drop all incoming UDP traffic on port `5353` in the INPUT chain:
   `sudo iptables -A INPUT -p udp --dport 5353 -j DROP`

### Task 4: Network Health Check Script
1. Create an executable script `/usr/local/bin/network_health.sh`.
2. If `br-marathon` is in state UP, write `STATUS=HEALTHY` to `/var/log/net_marathon.status`.
3. Execute the script once to confirm.""",
        "lfcs_setup": """sudo ip link del veth-m1 2>/dev/null || true
sudo ip link del br-marathon 2>/dev/null || true
sudo iptables -t nat -D PREROUTING -p tcp --dport 9090 -j REDIRECT --to-ports 80 2>/dev/null || true
sudo iptables -D INPUT -p udp --dport 5353 -j DROP 2>/dev/null || true
sudo rm -f /usr/local/bin/network_health.sh /var/log/net_marathon.status""",
        "lfcs_verify": """SCORE=0; TOTAL=4
# Task 1: br-marathon exists with 172.25.1.1/24
if ip addr show dev br-marathon 2>/dev/null | grep -q "172.25.1.1/24"; then
  echo -e "${GREEN}[PASS] Task 1: Bridge br-marathon verified with IP 172.25.1.1/24.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Bridge br-marathon missing or IP not set.${NC}"
fi

# Task 2: veth-m1 attached to br-marathon
if ip link show dev veth-m1 2>/dev/null | grep -q "master br-marathon"; then
  echo -e "${GREEN}[PASS] Task 2: veth-m1 attached to master br-marathon.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: veth-m1 master is not br-marathon.${NC}"
fi

# Task 3: iptables rules
NAT_OK=$(sudo iptables -t nat -S PREROUTING 2>/dev/null | grep -E -- "--dport 9090.*REDIRECT.*--to-ports 80" || true)
IN_OK=$(sudo iptables -S INPUT 2>/dev/null | grep -E -- "-p udp.*--dport 5353.*-j DROP" || true)
if [ -n "$NAT_OK" ] && [ -n "$IN_OK" ]; then
  echo -e "${GREEN}[PASS] Task 3: NAT port 9090 redirection and UDP 5353 drop rules verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Firewall rules missing (NAT=$NAT_OK, INPUT=$IN_OK).${NC}"
fi

# Task 4: Health script and status log
if [ -x /usr/local/bin/network_health.sh ] && grep -q "STATUS=HEALTHY" /var/log/net_marathon.status 2>/dev/null; then
  echo -e "${GREEN}[PASS] Task 4: /usr/local/bin/network_health.sh and /var/log/net_marathon.status verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: /var/log/net_marathon.status missing or status not HEALTHY.${NC}"
fi""",
        "lfcs_solution": """1. Bridge configuration:
`sudo ip link add br-marathon type bridge`
`sudo ip addr add 172.25.1.1/24 dev br-marathon`
`sudo ip link set br-marathon up`

2. Veth pair:
`sudo ip link add veth-m1 type veth peer name veth-m2`
`sudo ip link set veth-m1 master br-marathon`
`sudo ip link set veth-m1 up`
`sudo ip link set veth-m2 up`

3. Firewall:
`sudo iptables -t nat -A PREROUTING -p tcp --dport 9090 -j REDIRECT --to-ports 80`
`sudo iptables -A INPUT -p udp --dport 5353 -j DROP`

4. Script:
```bash
sudo bash -c 'cat << "EOF" > /usr/local/bin/network_health.sh
#!/usr/bin/env bash
if ip link show br-marathon | grep -q "state UP\\|UP"; then
  echo "STATUS=HEALTHY" > /var/log/net_marathon.status
fi
EOF'
sudo chmod +x /usr/local/bin/network_health.sh
sudo /usr/local/bin/network_health.sh
```""",
        "lfcs_reset": """sudo ip link del veth-m1 2>/dev/null || true
sudo ip link del br-marathon 2>/dev/null || true
sudo iptables -t nat -D PREROUTING -p tcp --dport 9090 -j REDIRECT --to-ports 80 2>/dev/null || true
sudo iptables -D INPUT -p udp --dport 5353 -j DROP 2>/dev/null || true
sudo rm -f /usr/local/bin/network_health.sh /var/log/net_marathon.status""",
    },
]
