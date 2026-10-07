# [CKA W2D5-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Discover schema:
```bash
kubectl explain pod.spec.containers.securityContext.capabilities.add
kubectl explain pod.spec.terminationGracePeriodSeconds
```
Save paths:
```bash
cat << 'EOF' > /opt/k8s/schema-paths.txt
spec.containers.securityContext.capabilities.add
spec.terminationGracePeriodSeconds
EOF
```

2. Construct and apply `/opt/k8s/secure-pod.yaml`:
```yaml
apiVersion: v1
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
```
`kubectl apply -f /opt/k8s/secure-pod.yaml`
