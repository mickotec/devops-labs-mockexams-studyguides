# [CKA W8D2-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. SSH to `node02`:
`ssh node02`
`sudo systemctl enable --now kubelet`
`exit`

2. Remove taint on `controlplane`:
`kubectl taint node node02 trouble-`

3. Deploy canary pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: worker-canary
  namespace: w8d2-trouble
spec:
  nodeName: node02
  containers:
  - name: nginx
    image: nginx:alpine
```
`kubectl apply -f canary.yaml`
