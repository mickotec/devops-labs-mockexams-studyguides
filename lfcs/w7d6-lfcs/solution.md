# [LFCS W7D6-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Bridge configuration:
`sudo ip link add br-marathon type bridge`
`sudo ip addr add 172.25.1.1/24 dev br-marathon`
`sudo ip link set br-marathon up`

2. Veth pair:
`sudo ip link add veth-m1 type veth peer name veth-m2`
`sudo ip link set veth-m1 master br-marathon`
`sudo ip link set veth-m1 up`
`sudo ip link set veth-m2 up`

3. Firewall:
`sudo iptables -t nat -A PREROUTING -p tcp --dport 9090 -j REDIRECT --to-ports 80`
`sudo iptables -A INPUT -p udp --dport 5353 -j DROP`

4. Script:
```bash
sudo bash -c 'cat << "EOF" > /usr/local/bin/network_health.sh
#!/usr/bin/env bash
if ip link show br-marathon | grep -q "state UP\|UP"; then
  echo "STATUS=HEALTHY" > /var/log/net_marathon.status
fi
EOF'
sudo chmod +x /usr/local/bin/network_health.sh
sudo /usr/local/bin/network_health.sh
```
