# [LFCS W7D1-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create interface dummy0 and bring UP:
`sudo ip link add dummy0 type dummy`
`sudo ip link set dummy0 up`

2. Assign IP:
`sudo ip addr add 10.10.20.50/24 dev dummy0`

3. Add route:
`sudo ip route add 10.200.0.0/16 dev dummy0`

4. Create script `/usr/local/bin/network_audit.sh`:
```bash
sudo bash -c 'cat << "EOF" > /usr/local/bin/network_audit.sh
#!/usr/bin/env bash
ip route show default > /var/log/network_audit.log
grep nameserver /etc/resolv.conf >> /var/log/network_audit.log
EOF'
sudo chmod +x /usr/local/bin/network_audit.sh
sudo /usr/local/bin/network_audit.sh
```
