# [CKA W1D5-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Update `~/.bashrc` and `~/.vimrc`:
```bash
echo "source <(kubectl completion bash)" >> ~/.bashrc
echo "alias k=kubectl" >> ~/.bashrc
echo "complete -o default -F __start_kubectl k" >> ~/.bashrc
echo 'export do="--dry-run=client -o yaml"' >> ~/.bashrc
echo 'export now="--force --grace-period=0"' >> ~/.bashrc

cat << 'EOF' >> ~/.vimrc
set tabstop=2
set shiftwidth=2
set expandtab
EOF
source ~/.bashrc
```

2. Rapid imperative commands:
```bash
k create namespace speed-drill
k create deploy cache-redis -n speed-drill --image=redis:7-alpine --replicas=3
k expose deploy cache-redis -n speed-drill --name=cache-service --port=6379
k create secret generic redis-secret -n speed-drill --from-literal=auth=supersecret
```

3. Export clean manifest:
```bash
k get deploy cache-redis -n speed-drill -o yaml | grep -v 'managedFields:' > /opt/k8s/clean-cache.yaml
```
