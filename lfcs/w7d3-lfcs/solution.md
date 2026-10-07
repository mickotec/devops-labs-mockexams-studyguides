# [LFCS W7D3-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Block port 8088:
`sudo iptables -A INPUT -p tcp --dport 8088 -j DROP`

2. Allow ICMP echo from 192.168.0.0/16:
`sudo iptables -I INPUT 1 -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT`

3. Save rules:
`sudo iptables-save | sudo tee /var/tmp/iptables_backup.rules > /dev/null`
