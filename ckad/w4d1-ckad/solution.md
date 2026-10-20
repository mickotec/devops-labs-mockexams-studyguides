# [CKAD W4D1-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Readiness Probes
```bash
ssh controlplane 'cat << "EOF_ALL" | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: order-processor
  namespace: ckad-w4d1
  labels:
    app: order-proc
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    ports:
    - containerPort: 80
    readinessProbe:
      httpGet:
        path: /ready
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 3
      failureThreshold: 2
    lifecycle:
      postStart:
        exec:
          command: ["sh", "-c", "touch /usr/share/nginx/html/ready"]
---
apiVersion: v1
kind: Service
metadata:
  name: order-service
  namespace: ckad-w4d1
spec:
  selector:
    app: order-proc
  ports:
  - port: 80
    targetPort: 80
EOF_ALL
'
```
