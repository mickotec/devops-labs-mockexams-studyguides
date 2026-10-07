# [CKA W4D5-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Extract admission plugins:
`grep -oE -- '--enable-admission-plugins=[^ ]*' /etc/kubernetes/manifests/kube-apiserver.yaml | cut -d'=' -f2 | sudo tee /opt/k8s/enabled_admission_plugins.txt`

2. Capture rejection:
`kubectl run ghost-pod -n void-ns --image=nginx:alpine 2> /opt/k8s/admission_rejection.log || true`
