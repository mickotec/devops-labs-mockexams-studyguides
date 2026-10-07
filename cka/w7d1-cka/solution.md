# [CKA W7D1-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Check `/etc/cni/net.d/`:
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
`kubectl apply -f net-mesh.yaml`
