# [CKA W6D2-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Role & RoleBinding:
`kubectl create role pod-operator -n w6d2-rbac --verb=get,list,watch,create,delete --resource=pods`
`kubectl create rolebinding bind-pod-operator -n w6d2-rbac --role=pod-operator --serviceaccount=w6d2-rbac:dev-sa`

2. ClusterRole & ClusterRoleBinding:
`kubectl create clusterrole node-observer --verb=get,list,watch --resource=nodes`
`kubectl create clusterrolebinding bind-node-observer --clusterrole=node-observer --serviceaccount=w6d2-rbac:dev-sa`

3. Verify:
`kubectl auth can-i list pods -n w6d2-rbac --as=system:serviceaccount:w6d2-rbac:dev-sa`
`kubectl auth can-i list nodes --as=system:serviceaccount:w6d2-rbac:dev-sa`
