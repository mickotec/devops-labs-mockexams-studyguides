# [CKAD W8D2-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: RBAC Roles
```bash
ssh controlplane '
kubectl create sa app-operator -n ckad-w8d2

kubectl create role pod-admin -n ckad-w8d2   --verb=get,list,watch,create,delete   --resource=pods,pods/log

kubectl create rolebinding bind-pod-admin -n ckad-w8d2   --role=pod-admin   --serviceaccount=ckad-w8d2:app-operator
'
```
