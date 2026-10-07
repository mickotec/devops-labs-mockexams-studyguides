# [CKA W6D3-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. ServiceAccount:
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: restricted-sa
  namespace: w6d3-sec
automountServiceAccountToken: false
```
`kubectl apply -f sa.yaml`

2. Hardened Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hardened-app
  namespace: w6d3-sec
spec:
  serviceAccountName: restricted-sa
  securityContext:
    runAsNonRoot: true
    runAsUser: 10001
    fsGroup: 20000
  containers:
  - name: nginx
    image: nginx:alpine
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
    volumeMounts:
    - name: tmp-dir
      mountPath: /tmp
  volumes:
  - name: tmp-dir
    emptyDir: {}
```
`kubectl apply -f hardened.yaml`
