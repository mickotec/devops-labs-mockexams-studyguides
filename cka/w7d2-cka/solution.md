# [CKA W7D2-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Deploy backend and ClusterIP service:
```bash
kubectl create deployment backend-app -n w7d2-dns --image=nginx:alpine --replicas=2
kubectl expose deployment backend-app -n w7d2-dns --name=backend-svc --port=8080 --target-port=80
```

2. Deploy frontend and NodePort service:
```bash
kubectl create deployment frontend-app -n w7d2-dns --image=nginx:alpine --replicas=1
kubectl create service nodeport frontend-nodeport -n w7d2-dns --tcp=80:80 --node-port=30080
kubectl set selector service frontend-nodeport -n w7d2-dns app=frontend-app
```

3. Test CoreDNS resolution:
```bash
kubectl run dns-tester -n w7d2-dns --image=busybox:1.36 --restart=Never --command -- nslookup backend-svc.w7d2-dns.svc.cluster.local
# Wait 3 seconds, then capture logs:
kubectl logs dns-tester -n w7d2-dns > /opt/k8s/dns_resolution.txt
```
