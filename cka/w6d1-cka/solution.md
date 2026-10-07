# [CKA W6D1-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create and apply CSR YAML:
```bash
B64_CSR=$(cat /opt/k8s/developer-bob.csr | base64 | tr -d '
')
cat << EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: developer-bob-csr
spec:
  request: $B64_CSR
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
EOF
```

2. Approve and extract:
`kubectl certificate approve developer-bob-csr`
`kubectl get csr developer-bob-csr -o jsonpath='{.status.certificate}' | base64 -d > /opt/k8s/developer-bob.crt`

3. Configure kubeconfig:
`kubectl config set-credentials developer-bob --client-certificate=/opt/k8s/developer-bob.crt --client-key=/opt/k8s/developer-bob.key --kubeconfig=/opt/k8s/bob.kubeconfig`
