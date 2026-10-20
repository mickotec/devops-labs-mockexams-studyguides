# [CKAD W2D3-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: ConfigMaps as Volumes
```bash
ssh controlplane '
cat << "EOF_CONF" | kubectl apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
  name: custom-nginx-conf
  namespace: ckad-w2d3
data:
  default.conf: |
    server {
      listen 8088;
      location / {
        return 200 "CUSTOM-PORT-OK
";
      }
    }
---
apiVersion: v1
kind: Pod
metadata:
  name: nginx-custom-port
  namespace: ckad-w2d3
spec:
  volumes:
  - name: conf-vol
    configMap:
      name: custom-nginx-conf
  containers:
  - name: web
    image: nginx:1.24-alpine
    ports:
    - containerPort: 8088
    volumeMounts:
    - name: conf-vol
      mountPath: /etc/nginx/conf.d
EOF_CONF
'
```
