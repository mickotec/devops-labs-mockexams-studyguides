# [LFCS W8D4-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Set ACL:
```bash
sudo mkdir -p /var/mock3_shared
sudo setfacl -m u:student:rwx /var/mock3_shared
sudo setfacl -d -m u:student:rwx /var/mock3_shared
```

2. Audit SUID binaries:
`find /usr/bin -type f -perm -4000 | sort > /var/tmp/suid_binaries.txt`

3. Kernel module:
```bash
sudo modprobe dummy
echo "dummy" | sudo tee /etc/modules-load.d/dummy.conf
```

4. Firewall rule:
`sudo iptables -A OUTPUT -p tcp -d 198.51.100.1 --dport 443 -j DROP`
