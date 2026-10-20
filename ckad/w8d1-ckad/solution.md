# [CKAD W8D1-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Kubeconfig Management
```bash
ssh controlplane '
kubectl --kubeconfig=/tmp/custom-kubeconfig config set-context developer-ctx   --cluster=kubernetes   --user=kubernetes-admin   --namespace=ckad-dev-ns

kubectl --kubeconfig=/tmp/custom-kubeconfig config use-context developer-ctx
'
```
