# [LFCS W1D3-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create group and users:
```bash
sudo groupadd -f devops_eng
sudo id alice &>/dev/null || sudo useradd -g devops_eng -m alice
sudo id bob &>/dev/null || sudo useradd -g devops_eng -m bob
```

2. Enforce recursive permissions:
```bash
sudo chgrp -R devops_eng /srv/data/engineering
sudo find /srv/data/engineering -type d -exec chmod 775 {} +
sudo find /srv/data/engineering -type f -exec chmod 664 {} +
```

3. Configure umask profile script:
```bash
sudo tee /etc/profile.d/devops_umask.sh << 'EOF'
if id -nG | grep -qw "devops_eng"; then
  umask 002
fi
EOF
sudo chmod 644 /etc/profile.d/devops_umask.sh
```
