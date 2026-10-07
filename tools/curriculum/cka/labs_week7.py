"""
Dedicated CKA Lab Definitions for Week 7 (Days 1 to 6).
"""

WEEK_7_LABS = [
    {
        "day": 1,
        "date": '2026-11-09',
        "title": 'Cluster & Pod Networking Prerequisites',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Inspect Active CNI Plugin
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
        "setup": """ssh controlplane '
  kubectl delete namespace w7d1-net --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d1-net
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/cni-plugin-type.txt /opt/k8s/node-podcidrs.txt
'""",
        "verify": """SCORE=0; TOTAL=3
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
        "solution": """1. Check `/etc/cni/net.d/`:
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
        "reset": """ssh controlplane '
  kubectl delete namespace w7d1-net --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/cni-plugin-type.txt /opt/k8s/node-podcidrs.txt
'""",
        "cka_title": 'Cluster & Pod Networking Prerequisites',
        "cka_diff": 'Medium',
        "cka_time": '35m',
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
    },
    {
        "day": 2,
        "date": '2026-11-10',
        "title": 'Service Networking & CoreDNS Deep Dive',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: ClusterIP Service Deployment
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
        "setup": """ssh controlplane '
  kubectl delete namespace w7d2-dns --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d2-dns
  sudo mkdir -p /opt/k8s && sudo chmod 777 /opt/k8s
  rm -f /opt/k8s/dns_resolution.txt
'""",
        "verify": """SCORE=0; TOTAL=3
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
        "solution": """1. Deploy backend and ClusterIP service:
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
        "reset": """ssh controlplane '
  kubectl delete namespace w7d2-dns --grace-period=0 --force 2>/dev/null || true
  rm -f /opt/k8s/dns_resolution.txt
'""",
        "cka_title": 'Service Networking & CoreDNS Deep Dive',
        "cka_diff": 'Medium',
        "cka_time": '35m',
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
    },
    {
        "day": 3,
        "date": '2026-11-11',
        "title": 'Ingress Controllers & Routing Rules',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Deploy Backend Microservices
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
        "setup": """ssh controlplane '
  kubectl delete namespace w7d3-ingress --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d3-ingress
  kubectl create deployment catalog -n w7d3-ingress --image=nginx:alpine --port=80
  kubectl expose deployment catalog -n w7d3-ingress --name=catalog-svc --port=80
  kubectl create deployment orders -n w7d3-ingress --image=httpd:alpine --port=80
  kubectl expose deployment orders -n w7d3-ingress --name=orders-svc --port=80
'""",
        "verify": """SCORE=0; TOTAL=3
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
P1=$(ssh controlplane 'kubectl get ingress store-ingress -n w7d3-ingress -o jsonpath="{.spec.rules[0].http.paths[?(@.path=="/catalog")].backend.service.name}" 2>/dev/null || echo "None"')
P2=$(ssh controlplane 'kubectl get ingress store-ingress -n w7d3-ingress -o jsonpath="{.spec.rules[0].http.paths[?(@.path=="/orders")].backend.service.name}" 2>/dev/null || echo "None"')

if [ "$HOST" == "store.internal.example.com" ] && [ "$P1" == "catalog-svc" ] && [ "$P2" == "orders-svc" ]; then
  echo -e "${GREEN}[PASS] Task 2: Ingress store-ingress routes host $HOST to catalog-svc and orders-svc.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Ingress routing mismatch (host=$HOST, /catalog=$P1, /orders=$P2).${NC}"
fi

# Task 3: Rewrite annotation
REWRITE=$(ssh controlplane 'kubectl get ingress store-ingress -n w7d3-ingress -o jsonpath="{.metadata.annotations.nginx\.ingress\.kubernetes\.io/rewrite-target}" 2>/dev/null || echo "None"')
if [ "$REWRITE" == "/" ]; then
  echo -e "${GREEN}[PASS] Task 3: Rewrite annotation nginx.ingress.kubernetes.io/rewrite-target: / verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Rewrite annotation is $REWRITE (expected /).${NC}"
fi""",
        "solution": """Create manifest `store-ingress.yaml`:
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
        "reset": """ssh controlplane '
  kubectl delete namespace w7d3-ingress --grace-period=0 --force 2>/dev/null || true
'""",
        "cka_title": 'Ingress Controllers & Routing Rules',
        "cka_diff": 'Medium',
        "cka_time": '35m',
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
P1=$(ssh controlplane 'kubectl get ingress store-ingress -n w7d3-ingress -o jsonpath="{.spec.rules[0].http.paths[?(@.path=="/catalog")].backend.service.name}" 2>/dev/null || echo "None"')
P2=$(ssh controlplane 'kubectl get ingress store-ingress -n w7d3-ingress -o jsonpath="{.spec.rules[0].http.paths[?(@.path=="/orders")].backend.service.name}" 2>/dev/null || echo "None"')

if [ "$HOST" == "store.internal.example.com" ] && [ "$P1" == "catalog-svc" ] && [ "$P2" == "orders-svc" ]; then
  echo -e "${GREEN}[PASS] Task 2: Ingress store-ingress routes host $HOST to catalog-svc and orders-svc.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Ingress routing mismatch (host=$HOST, /catalog=$P1, /orders=$P2).${NC}"
fi

# Task 3: Rewrite annotation
REWRITE=$(ssh controlplane 'kubectl get ingress store-ingress -n w7d3-ingress -o jsonpath="{.metadata.annotations.nginx\.ingress\.kubernetes\.io/rewrite-target}" 2>/dev/null || echo "None"')
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
    },
    {
        "day": 4,
        "date": '2026-11-12',
        "title": 'Gateway API (2025 Updates)',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Verify GatewayClass
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
        "setup": """ssh controlplane '
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
        "verify": """SCORE=0; TOTAL=3
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
        "solution": """1. Create Gateway manifest `gateway.yaml`:
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
        "reset": """ssh controlplane '
  kubectl delete namespace w7d4-gw --grace-period=0 --force 2>/dev/null || true
  kubectl delete gatewayclass cluster-gateway-class 2>/dev/null || true
'""",
        "cka_title": 'Gateway API (2025 Updates)',
        "cka_diff": 'Medium',
        "cka_time": '35m',
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
    },
    {
        "day": 5,
        "date": '2026-11-13',
        "title": 'Network Policies Deep Dive',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Default-Deny Ingress Policy
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
        "setup": """ssh controlplane '
  kubectl delete namespace w7d5-netpol --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d5-netpol
  kubectl run frontend -n w7d5-netpol --image=nginx:alpine --labels=role=frontend
  kubectl run backend -n w7d5-netpol --image=nginx:alpine --labels=role=backend
  kubectl run database -n w7d5-netpol --image=nginx:alpine --labels=role=db
'""",
        "verify": """SCORE=0; TOTAL=3
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
        "solution": """1. Create `default-deny-ingress`:
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
        "reset": """ssh controlplane '
  kubectl delete namespace w7d5-netpol --grace-period=0 --force 2>/dev/null || true
'""",
        "cka_title": 'Network Policies Deep Dive',
        "cka_diff": 'Medium',
        "cka_time": '35m',
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
    },
    {
        "day": 6,
        "date": '2026-11-14',
        "title": 'Week 7 Network Mastery Triathlon',
        "diff": 'Hard (Milestone)',
        "time": '45m',
        "tasks": """### Task 1: Multi-Service Architecture
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
        "setup": """ssh controlplane '
  kubectl delete namespace w7d6-triathlon --grace-period=0 --force 2>/dev/null || true
  kubectl create namespace w7d6-triathlon
'""",
        "verify": """SCORE=0; TOTAL=3
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
        "solution": """1. Deploy services:
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
        "reset": """ssh controlplane '
  kubectl delete namespace w7d6-triathlon --grace-period=0 --force 2>/dev/null || true
  rm -f /tmp/tls.key /tmp/tls.crt
'""",
        "cka_title": 'Week 7 Network Mastery Triathlon',
        "cka_diff": 'Hard (Milestone)',
        "cka_time": '45m',
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
    },
]
