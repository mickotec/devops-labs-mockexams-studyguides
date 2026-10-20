# [CKAD W8D6-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Kustomize Overlays
```bash
ssh controlplane '
cat << "EOF_PROD" > /tmp/kustomize-store/overlays/prod/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: ckad-w8d6
resources:
- ../../base
namePrefix: prod-
commonLabels:
  env: production
  tier: web
patches:
- patch: |-
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: web-app
    spec:
      replicas: 3
  target:
    kind: Deployment
    name: web-app
EOF_PROD

kubectl apply -k /tmp/kustomize-store/overlays/prod
'
```
