# [CKA W3D6-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Label node02:
`kubectl label node node02 hardware=gpu`

2. Add toleration to `stuck-taint`:
`kubectl get pod stuck-taint -n w3-milestone -o yaml > /tmp/stuck-taint.yaml`
Add under spec:
```yaml
tolerations:
- key: dedicated
  operator: Equal
  value: web
  effect: NoSchedule
```
`kubectl replace --force -f /tmp/stuck-taint.yaml`

3. Patch DaemonSet to tolerate control plane taint:
`kubectl patch ds infra-agent -n w3-milestone --type=strategic -p '{"spec":{"template":{"spec":{"tolerations":[{"key":"node-role.kubernetes.io/control-plane","operator":"Exists","effect":"NoSchedule"}]}}}}'`
