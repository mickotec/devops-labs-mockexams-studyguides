# [CKA W8D3-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Extract node names:
`kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"
"}{end}' | sort > /opt/k8s/node_names.txt`

2. Extract kube-system images:
`kubectl get pods -n kube-system -o jsonpath='{range .items[*]}{range .spec.containers[*]}{.image}{"
"}{end}{end}' | sort -u > /opt/k8s/kube_system_images.txt`

3. Custom columns query:
`kubectl get pods -n w8d3-json -o custom-columns=NAME:.metadata.name,NODE:.spec.nodeName > /opt/k8s/pod_node_mapping.txt`

4. Lightning challenge:
```bash
kubectl run fast-pod -n w8d3-lightning --image=redis:alpine --labels=app=fast-cache --port=6379
kubectl expose pod fast-pod -n w8d3-lightning --name=fast-svc --port=6379
```
