# [CKAD W8D3-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: ClusterRoles
```bash
ssh controlplane '
kubectl create sa auditor-sa -n default

kubectl create clusterrole cluster-inspector   --verb=get,list,watch   --resource=nodes,persistentvolumes,storageclasses

kubectl create clusterrolebinding bind-cluster-inspector   --clusterrole=cluster-inspector   --serviceaccount=default:auditor-sa
'
```
