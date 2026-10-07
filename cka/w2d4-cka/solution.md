# [CKA W2D4-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Deploy database and service:
```bash
kubectl run mysql-db -n database-ns --image=nginx:alpine --labels=app=db
kubectl expose pod mysql-db -n database-ns --name=mysql-svc --port=3306 --target-port=80
```

2. Deploy tester pod:
```bash
kubectl run tester -n frontend-ns --image=busybox:1.36 -- sleep 3600
```

3. Query DNS and save record:
```bash
kubectl exec -n frontend-ns tester -- sh -c "nslookup mysql-svc.database-ns.svc.cluster.local > /tmp/dns-record.txt"
```
