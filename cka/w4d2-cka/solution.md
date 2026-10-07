# [CKA W4D2-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create ConfigMaps:
`kubectl create cm backend-config -n w4d2-config --from-literal=DB_HOST=postgres.internal --from-literal=DB_PORT=5432`
`kubectl create cm ui-settings -n w4d2-config --from-file=settings.json=/opt/k8s/settings.json`

2. Deploy `portal-app`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: portal-app
  namespace: w4d2-config
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    envFrom:
    - configMapRef:
        name: backend-config
    volumeMounts:
    - name: ui-vol
      mountPath: /etc/portal/config
      readOnly: true
  volumes:
  - name: ui-vol
    configMap:
      name: ui-settings
```
`kubectl apply -f portal.yaml`
