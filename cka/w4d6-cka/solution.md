# [CKA W4D6-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create ConfigMap and Secret:
`kubectl create cm app-settings -n w4-milestone --from-literal=APP_MODE=production`
`kubectl create secret generic app-auth -n w4-milestone --from-literal=API_KEY=Alpha99SecretToken`

2. Deploy `secure-frontend`:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secure-frontend
  namespace: w4-milestone
spec:
  replicas: 2
  selector:
    matchLabels:
      app: secure-frontend
  template:
    metadata:
      labels:
        app: secure-frontend
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        env:
        - name: APP_MODE
          valueFrom:
            configMapKeyRef:
              name: app-settings
              key: APP_MODE
        - name: API_KEY
          valueFrom:
            secretKeyRef:
              name: app-auth
              key: API_KEY
        resources:
          requests:
            cpu: 30m
            memory: 64Mi
        volumeMounts:
        - name: secret-vol
          mountPath: /etc/auth/token
          readOnly: true
      volumes:
      - name: secret-vol
        secret:
          secretName: app-auth
          defaultMode: 256
```
`kubectl apply -f deployment.yaml`

3. Create HPA:
`kubectl autoscale deployment secure-frontend -n w4-milestone --cpu-percent=60 --min=2 --max=5 --name=secure-frontend-hpa`
