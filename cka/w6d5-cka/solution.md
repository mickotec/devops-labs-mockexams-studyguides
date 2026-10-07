# [CKA W6D5-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create `/opt/k8s/kustomize/base/kustomization.yaml`:
```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- deployment.yaml
- service.yaml
namePrefix: prod-
commonLabels:
  env: production
  tier: core
```

2. Apply:
`kubectl apply -k /opt/k8s/kustomize/base -n w6d5-kustomize`
