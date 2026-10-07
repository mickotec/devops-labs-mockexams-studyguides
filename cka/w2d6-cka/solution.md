# [CKA W2D6-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Deploy:
```bash
kubectl create ns triathlon-w2
kubectl create deploy order-processor -n triathlon-w2 --image=nginx:1.24-alpine --replicas=5
```

2. Expose NodePort:
```bash
kubectl create svc nodeport order-service -n triathlon-w2 --tcp=80:80 --node-port=30500
```
Update selector to `app=order-processor`.

3. Rollout and Rollback:
```bash
kubectl set image deploy/order-processor nginx=nginx:1.25-alpine -n triathlon-w2
kubectl rollout undo deploy/order-processor -n triathlon-w2
```

4. Export clean manifest:
```bash
kubectl get deploy order-processor -n triathlon-w2 -o yaml | grep -vE 'resourceVersion|uid|creationTimestamp|status:' > /opt/k8s/clean-export.yaml
```
