# [CKA W5D5-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Check expiration:
`sudo kubeadm certs check-expiration | sudo tee /opt/k8s/certs_expiration.txt`

2. Extract SANs:
`sudo openssl x509 -in /etc/kubernetes/pki/apiserver.crt -noout -text | grep -A 1 "Subject Alternative Name" | sudo tee /opt/k8s/apiserver_sans.txt`
