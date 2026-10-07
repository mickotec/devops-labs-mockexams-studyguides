# [CKA W4D3-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create Secret:
`kubectl create secret generic db-credentials -n w4d3-secrets --from-literal=username=dbadmin --from-literal=password='S3cur3P@ssw0rd!'`

2. Deploy `vault-agent`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: vault-agent
  namespace: w4d3-secrets
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    volumeMounts:
    - name: sec-vol
      mountPath: /etc/vault/secrets
      readOnly: true
  volumes:
  - name: sec-vol
    secret:
      secretName: db-credentials
      defaultMode: 256
```
`kubectl apply -f vault-agent.yaml`
