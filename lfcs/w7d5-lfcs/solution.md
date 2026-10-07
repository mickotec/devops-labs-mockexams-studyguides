# [LFCS W7D5-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Generate key and authorize:
```bash
ssh-keygen -t rsa -b 4096 -N "" -f /home/student/.ssh/id_admin_rsa
cat /home/student/.ssh/id_admin_rsa.pub >> /home/student/.ssh/authorized_keys
chmod 700 /home/student/.ssh
chmod 600 /home/student/.ssh/authorized_keys
```

2. Hardening drop-in:
```bash
sudo bash -c 'cat << "EOF" > /etc/ssh/sshd_config.d/99-hardening.conf
PermitRootLogin no
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 2
EOF'
sudo sshd -t
```

3. Enable NTP:
`sudo timedatectl set-ntp true`
