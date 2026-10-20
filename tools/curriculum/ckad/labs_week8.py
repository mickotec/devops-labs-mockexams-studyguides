"""
Dedicated CKAD Lab Definitions for Week 8 (Days 1 to 6).
Aligned with KodeKloud CKAD Learning Modules: Security, Helm, Kustomize & CRDs
"""

WEEK_8_LABS = [
    {
        "day": 1,
        "date": "2026-11-30",
        "title": "Kubeconfig Files & Context Management",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Create Custom Context & Set Default Namespace
1. On node `controlplane`, create a working kubeconfig copy at `/tmp/custom-kubeconfig`.
2. Configure a new context named `developer-ctx` in `/tmp/custom-kubeconfig`:
   - `cluster`: `kubernetes`
   - `user`: `kubernetes-admin`
   - `namespace`: `ckad-dev-ns`
3. Set the current-context of `/tmp/custom-kubeconfig` to `developer-ctx`.
4. Verify that running `kubectl --kubeconfig=/tmp/custom-kubeconfig config current-context` outputs `developer-ctx`.""",
        "setup": """ssh controlplane '
cp ~/.kube/config /tmp/custom-kubeconfig 2>/dev/null || cp /etc/kubernetes/admin.conf /tmp/custom-kubeconfig
kubectl create namespace ckad-dev-ns --dry-run=client -o yaml | kubectl apply -f -
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W8D1: Kubeconfig Context in /tmp/custom-kubeconfig..."

CURRENT_CTX=$(ssh controlplane 'kubectl --kubeconfig=/tmp/custom-kubeconfig config current-context 2>/dev/null || echo ""')
NS=$(ssh controlplane 'kubectl --kubeconfig=/tmp/custom-kubeconfig config view --minify -o jsonpath="{.contexts[0].context.namespace}" 2>/dev/null || echo ""')

if [ "$CURRENT_CTX" == "developer-ctx" ] && [ "$NS" == "ckad-dev-ns" ]; then
  echo -e "\033[0;32m[PASS] custom-kubeconfig active context is developer-ctx with default namespace ckad-dev-ns.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] current-context: '$CURRENT_CTX' (expected developer-ctx) | default ns: '$NS'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Kubeconfig Management
```bash
ssh controlplane '
kubectl --kubeconfig=/tmp/custom-kubeconfig config set-context developer-ctx \
  --cluster=kubernetes \
  --user=kubernetes-admin \
  --namespace=ckad-dev-ns

kubectl --kubeconfig=/tmp/custom-kubeconfig config use-context developer-ctx
'
```""",
        "reset": """ssh controlplane '
rm -f /tmp/custom-kubeconfig
kubectl delete namespace ckad-dev-ns --ignore-not-found
'"""
    },
    {
        "day": 2,
        "date": "2026-12-01",
        "title": "RBAC: Roles & RoleBindings",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Create Role & RoleBinding
1. In namespace `ckad-w8d2`, create a ServiceAccount named `app-operator`.
2. Create a Role named `pod-admin` in namespace `ckad-w8d2`:
   - Resources: `pods`, `pods/log`
   - Verbs: `get`, `list`, `watch`, `create`, `delete`
3. Bind Role `pod-admin` to ServiceAccount `app-operator` using a RoleBinding named `bind-pod-admin`.
4. Verify permissions using:
   `kubectl auth can-i create pods -n ckad-w8d2 --as=system:serviceaccount:ckad-w8d2:app-operator`.""",
        "setup": """ssh controlplane 'kubectl create namespace ckad-w8d2 --dry-run=client -o yaml | kubectl apply -f -'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W8D2: RBAC in ckad-w8d2..."

CAN_CREATE=$(ssh controlplane 'kubectl auth can-i create pods -n ckad-w8d2 --as=system:serviceaccount:ckad-w8d2:app-operator 2>/dev/null || true')
CAN_DEPLOY=$(ssh controlplane 'kubectl auth can-i create deployments -n ckad-w8d2 --as=system:serviceaccount:ckad-w8d2:app-operator 2>/dev/null || true')

if [ "$CAN_CREATE" == "yes" ] && [ "$CAN_DEPLOY" == "no" ]; then
  echo -e "\033[0;32m[PASS] ServiceAccount app-operator has exact pod-admin permissions in ckad-w8d2.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] can-i create pods: '$CAN_CREATE' (expected yes) | can-i create deployments: '$CAN_DEPLOY' (expected no)\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: RBAC Roles
```bash
ssh controlplane '
kubectl create sa app-operator -n ckad-w8d2

kubectl create role pod-admin -n ckad-w8d2 \
  --verb=get,list,watch,create,delete \
  --resource=pods,pods/log

kubectl create rolebinding bind-pod-admin -n ckad-w8d2 \
  --role=pod-admin \
  --serviceaccount=ckad-w8d2:app-operator
'
```""",
        "reset": """ssh controlplane 'kubectl delete namespace ckad-w8d2 --ignore-not-found'"""
    },
    {
        "day": 3,
        "date": "2026-12-02",
        "title": "ClusterRoles & ClusterRoleBindings",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Grant Cluster-Wide Read Permissions
1. Create a ClusterRole named `cluster-inspector`:
   - Resources: `nodes`, `persistentvolumes`, `storageclasses`
   - Verbs: `get`, `list`, `watch`
2. Create a ServiceAccount named `auditor-sa` in namespace `default`.
3. Bind ClusterRole `cluster-inspector` to `auditor-sa` using a ClusterRoleBinding named `bind-cluster-inspector`.
4. Verify with `kubectl auth can-i get nodes --as=system:serviceaccount:default:auditor-sa`.""",
        "setup": """ssh controlplane '
kubectl delete clusterrole cluster-inspector --ignore-not-found
kubectl delete clusterrolebinding bind-cluster-inspector --ignore-not-found
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W8D3: ClusterRole cluster-inspector..."

CAN_NODES=$(ssh controlplane 'kubectl auth can-i get nodes --as=system:serviceaccount:default:auditor-sa 2>/dev/null || echo "no"')
CAN_PVS=$(ssh controlplane 'kubectl auth can-i get persistentvolumes --as=system:serviceaccount:default:auditor-sa 2>/dev/null || echo "no"')

if [ "$CAN_NODES" == "yes" ] && [ "$CAN_PVS" == "yes" ]; then
  echo -e "\033[0;32m[PASS] ClusterRoleBinding bind-cluster-inspector grants cluster-wide node & PV read access.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] can-i get nodes: '$CAN_NODES' | can-i get pvs: '$CAN_PVS'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: ClusterRoles
```bash
ssh controlplane '
kubectl create sa auditor-sa -n default

kubectl create clusterrole cluster-inspector \
  --verb=get,list,watch \
  --resource=nodes,persistentvolumes,storageclasses

kubectl create clusterrolebinding bind-cluster-inspector \
  --clusterrole=cluster-inspector \
  --serviceaccount=default:auditor-sa
'
```""",
        "reset": """ssh controlplane '
kubectl delete clusterrole cluster-inspector --ignore-not-found
kubectl delete clusterrolebinding bind-cluster-inspector --ignore-not-found
'"""
    },
    {
        "day": 4,
        "date": "2026-12-03",
        "title": "API Versions & Deprecations Migration",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Migrate Deprecated Ingress Manifest
1. On node `controlplane`, an outdated manifest exists at `/tmp/deprecated-ingress.yaml` written against `extensions/v1beta1`.
2. Convert the manifest to the current stable API version `networking.k8s.io/v1`:
   - Change `apiVersion` to `networking.k8s.io/v1`
   - Update path syntax to include `pathType: Prefix`
   - Update backend specification to `service: {name: web-svc, port: {number: 80}}`
3. Apply the updated manifest into namespace `ckad-w8d4` and verify it creates successfully.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w8d4 --dry-run=client -o yaml | kubectl apply -f -
cat << "EOF_DEP" > /tmp/deprecated-ingress.yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: legacy-ingress
  namespace: ckad-w8d4
spec:
  rules:
  - host: legacy.example.com
    http:
      paths:
      - path: /
        backend:
          serviceName: web-svc
          servicePort: 80
EOF_DEP
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W8D4: API Deprecations in ckad-w8d4..."

API_VER=$(ssh controlplane 'kubectl get ingress legacy-ingress -n ckad-w8d4 -o jsonpath="{.apiVersion}" 2>/dev/null || echo ""')
HOST=$(ssh controlplane 'kubectl get ingress legacy-ingress -n ckad-w8d4 -o jsonpath="{.spec.rules[0].host}" 2>/dev/null || echo ""')

if [ "$API_VER" == "networking.k8s.io/v1" ] && [ "$HOST" == "legacy.example.com" ]; then
  echo -e "\033[0;32m[PASS] Ingress successfully migrated to networking.k8s.io/v1 and applied.\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] apiVersion: '$API_VER' (expected networking.k8s.io/v1) | Host: '$HOST'\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: API Deprecations
```bash
ssh controlplane 'cat << "EOF_FIX" > /tmp/deprecated-ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: legacy-ingress
  namespace: ckad-w8d4
spec:
  rules:
  - host: legacy.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-svc
            port:
              number: 80
EOF_FIX
kubectl apply -f /tmp/deprecated-ingress.yaml
'
```""",
        "reset": """ssh controlplane '
kubectl delete namespace ckad-w8d4 --ignore-not-found
rm -f /tmp/deprecated-ingress.yaml
'"""
    },
    {
        "day": 5,
        "date": "2026-12-04",
        "title": "Helm Package Management & Value Overrides",
        "diff": "Medium",
        "time": "25m",
        "tasks": """### Task 1: Configure Helm Chart Release
1. In namespace `ckad-w8d5`, verify Helm is installed on `controlplane`.
2. A sample chart directory exists at `/tmp/sample-chart`.
3. Install a release named `frontend-app` from `/tmp/sample-chart` into namespace `ckad-w8d5`:
   - Override `replicaCount`: set to `3` using `--set replicaCount=3`
4. Verify the release status using `helm list -n ckad-w8d5` and ensure 3 pods are running.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w8d5 --dry-run=client -o yaml | kubectl apply -f -
rm -rf /tmp/sample-chart
mkdir -p /tmp/sample-chart/templates
cat << "EOF_CHART" > /tmp/sample-chart/Chart.yaml
apiVersion: v2
name: sample-chart
version: 0.1.0
EOF_CHART

cat << "EOF_VALS" > /tmp/sample-chart/values.yaml
replicaCount: 1
image: nginx:alpine
EOF_VALS

cat << "EOF_DEP" > /tmp/sample-chart/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app: {{ .Release.Name }}
    spec:
      containers:
      - name: nginx
        image: {{ .Values.image }}
EOF_DEP
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W8D5: Helm Release in ckad-w8d5..."

HELM_STATUS=$(ssh controlplane 'helm list -n ckad-w8d5 -q 2>/dev/null | grep "^frontend-app$" || echo ""')
REPLICAS=$(ssh controlplane 'kubectl get deploy frontend-app -n ckad-w8d5 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')

if [ -n "$HELM_STATUS" ] && [ "$REPLICAS" -eq 3 ]; then
  echo -e "\\033[0;32m[PASS] Helm release frontend-app deployed with replicaCount=3 (3/3 Ready).\\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\\033[0;31m[FAIL] Helm status: '\''$HELM_STATUS'\'' | Ready replicas: $REPLICAS (expected 3).\\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Helm Release Management
```bash
ssh controlplane '
helm install frontend-app /tmp/sample-chart -n ckad-w8d5 --set replicaCount=3
kubectl rollout status deployment/frontend-app -n ckad-w8d5 --timeout=60s
'
```""",
        "reset": """ssh controlplane '
helm uninstall frontend-app -n ckad-w8d5 2>/dev/null || true
kubectl delete namespace ckad-w8d5 --ignore-not-found
rm -rf /tmp/sample-chart
'"""
    },
    {
        "day": 6,
        "date": "2026-12-05",
        "title": "Kustomize: Overlays, Transformers & Patches",
        "diff": "Hard",
        "time": "30m",
        "tasks": """### Task 1: Build Multi-Environment Kustomize Overlay
1. On node `controlplane`, construct a Kustomize structure under `/tmp/kustomize-store`:
   - `base/deployment.yaml`: Deployment of `nginx:1.24-alpine` (replicas: 1)
   - `base/kustomization.yaml`: referencing `deployment.yaml`
   - `overlays/prod/kustomization.yaml`:
     - `resources`: referencing `../../base`
     - `namePrefix`: `prod-`
     - `commonLabels`: `env: production, tier: web`
     - Patch: increase replicas to `3`
2. Apply the overlay into namespace `ckad-w8d6` using `kubectl apply -k /tmp/kustomize-store/overlays/prod`.
3. Verify that deployment `prod-web-app` runs with 3 replicas and label `env=production`.""",
        "setup": """ssh controlplane '
kubectl create namespace ckad-w8d6 --dry-run=client -o yaml | kubectl apply -f -
rm -rf /tmp/kustomize-store
mkdir -p /tmp/kustomize-store/base /tmp/kustomize-store/overlays/prod
cat << "EOF_BASE" > /tmp/kustomize-store/base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: nginx
        image: nginx:1.24-alpine
EOF_BASE

cat << "EOF_KUST" > /tmp/kustomize-store/base/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- deployment.yaml
EOF_KUST
'""",
        "verify": """#!/usr/bin/env bash
set -uo pipefail
echo "[*] Evaluating CKAD W8D6: Kustomize Overlays in ckad-w8d6..."

REPLICAS=$(ssh controlplane 'kubectl get deploy prod-web-app -n ckad-w8d6 -o jsonpath="{.status.readyReplicas}" 2>/dev/null || echo 0')
LABEL_ENV=$(ssh controlplane 'kubectl get deploy prod-web-app -n ckad-w8d6 -o jsonpath="{.metadata.labels.env}" 2>/dev/null || echo ""')

if [ "$REPLICAS" -eq 3 ] && [ "$LABEL_ENV" == "production" ]; then
  echo -e "\033[0;32m[PASS] Kustomize overlay applied successfully (prod-web-app, 3/3 Ready, env=production).\033[0m"
  echo "Final Score: 1/1 (100%)"
  exit 0
else
  echo -e "\033[0;31m[FAIL] Ready replicas: $REPLICAS (expected 3) | Label env: '$LABEL_ENV' (expected production).\033[0m"
  echo "Final Score: 0/1 (0%)"
  exit 1
fi""",
        "solution": """### Official Solution: Kustomize Overlays
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
kubectl rollout status deployment/prod-web-app -n ckad-w8d6 --timeout=30s 2>/dev/null || true
'
```""",
        "reset": """ssh controlplane '
kubectl delete namespace ckad-w8d6 --ignore-not-found
rm -rf /tmp/kustomize-store
'"""
    }
]
