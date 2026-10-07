"""
Dedicated LFCS Lab Definitions for Week 7 (Days 1 to 6).
"""

WEEK_7_LABS = [
    {
        "day": 1,
        "date": '2026-11-09',
        "title": 'Linux Networking Configuration (IP & Routing)',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Create Dummy Network Interface
1. Create a dummy network interface named `dummy0` using `ip link`:
   `sudo ip link add dummy0 type dummy`
2. Bring the interface UP:
   `sudo ip link set dummy0 up`

### Task 2: Assign Static IP Address
1. Assign secondary static IP `10.10.20.50/24` to interface `dummy0`:
   `sudo ip addr add 10.10.20.50/24 dev dummy0`

### Task 3: Static Route Configuration
1. Add a static route for destination subnet `10.200.0.0/16` routed via device `dummy0`:
   `sudo ip route add 10.200.0.0/16 dev dummy0`

### Task 4: Network Diagnostic Audit Script
1. Create an executable bash script `/usr/local/bin/network_audit.sh`.
2. The script must write:
   - The default routing line (`ip route show default`)
   - All active nameserver entries from `/etc/resolv.conf` (`grep nameserver /etc/resolv.conf`)
   into `/var/log/network_audit.log`.
3. Set executable permissions on `/usr/local/bin/network_audit.sh` and run it once to initialize the log.""",
        "setup": """sudo ip link del dummy0 2>/dev/null || true
sudo rm -f /usr/local/bin/network_audit.sh /var/log/network_audit.log""",
        "verify": """SCORE=0; TOTAL=4
# Task 1: dummy0 interface exists and is up
if ip link show dummy0 2>/dev/null | grep -q "state UP\|UP"; then
  echo -e "${GREEN}[PASS] Task 1: Interface dummy0 is UP.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Interface dummy0 missing or not UP.${NC}"
fi

# Task 2: IP 10.10.20.50/24 assigned to dummy0
if ip addr show dev dummy0 2>/dev/null | grep -q "10.10.20.50/24"; then
  echo -e "${GREEN}[PASS] Task 2: IP 10.10.20.50/24 assigned to dummy0.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: IP 10.10.20.50/24 not found on dummy0.${NC}"
fi

# Task 3: Route 10.200.0.0/16 exists
if ip route show 10.200.0.0/16 2>/dev/null | grep -q "dummy0"; then
  echo -e "${GREEN}[PASS] Task 3: Static route 10.200.0.0/16 via dummy0 exists.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Route 10.200.0.0/16 via dummy0 not found.${NC}"
fi

# Task 4: Audit script & log
if [ -x /usr/local/bin/network_audit.sh ] && [ -f /var/log/network_audit.log ] && grep -q "default" /var/log/network_audit.log && grep -q "nameserver" /var/log/network_audit.log; then
  echo -e "${GREEN}[PASS] Task 4: /usr/local/bin/network_audit.sh and /var/log/network_audit.log verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: Audit script or log file invalid.${NC}"
fi""",
        "solution": """1. Create interface dummy0 and bring UP:
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
```""",
        "reset": """sudo ip link del dummy0 2>/dev/null || true
sudo rm -f /usr/local/bin/network_audit.sh /var/log/network_audit.log""",
        "lfcs_title": 'Linux Networking Configuration (IP & Routing)',
        "lfcs_diff": 'Medium',
        "lfcs_time": '35m',
        "lfcs_tasks": """### Task 1: Create Dummy Network Interface
1. Create a dummy network interface named `dummy0` using `ip link`:
   `sudo ip link add dummy0 type dummy`
2. Bring the interface UP:
   `sudo ip link set dummy0 up`

### Task 2: Assign Static IP Address
1. Assign secondary static IP `10.10.20.50/24` to interface `dummy0`:
   `sudo ip addr add 10.10.20.50/24 dev dummy0`

### Task 3: Static Route Configuration
1. Add a static route for destination subnet `10.200.0.0/16` routed via device `dummy0`:
   `sudo ip route add 10.200.0.0/16 dev dummy0`

### Task 4: Network Diagnostic Audit Script
1. Create an executable bash script `/usr/local/bin/network_audit.sh`.
2. The script must write:
   - The default routing line (`ip route show default`)
   - All active nameserver entries from `/etc/resolv.conf` (`grep nameserver /etc/resolv.conf`)
   into `/var/log/network_audit.log`.
3. Set executable permissions on `/usr/local/bin/network_audit.sh` and run it once to initialize the log.""",
        "lfcs_setup": """sudo ip link del dummy0 2>/dev/null || true
sudo rm -f /usr/local/bin/network_audit.sh /var/log/network_audit.log""",
        "lfcs_verify": """SCORE=0; TOTAL=4
# Task 1: dummy0 interface exists and is up
if ip link show dummy0 2>/dev/null | grep -q "state UP\|UP"; then
  echo -e "${GREEN}[PASS] Task 1: Interface dummy0 is UP.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Interface dummy0 missing or not UP.${NC}"
fi

# Task 2: IP 10.10.20.50/24 assigned to dummy0
if ip addr show dev dummy0 2>/dev/null | grep -q "10.10.20.50/24"; then
  echo -e "${GREEN}[PASS] Task 2: IP 10.10.20.50/24 assigned to dummy0.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: IP 10.10.20.50/24 not found on dummy0.${NC}"
fi

# Task 3: Route 10.200.0.0/16 exists
if ip route show 10.200.0.0/16 2>/dev/null | grep -q "dummy0"; then
  echo -e "${GREEN}[PASS] Task 3: Static route 10.200.0.0/16 via dummy0 exists.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Route 10.200.0.0/16 via dummy0 not found.${NC}"
fi

# Task 4: Audit script & log
if [ -x /usr/local/bin/network_audit.sh ] && [ -f /var/log/network_audit.log ] && grep -q "default" /var/log/network_audit.log && grep -q "nameserver" /var/log/network_audit.log; then
  echo -e "${GREEN}[PASS] Task 4: /usr/local/bin/network_audit.sh and /var/log/network_audit.log verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: Audit script or log file invalid.${NC}"
fi""",
        "lfcs_solution": """1. Create interface dummy0 and bring UP:
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
```""",
        "lfcs_reset": """sudo ip link del dummy0 2>/dev/null || true
sudo rm -f /usr/local/bin/network_audit.sh /var/log/network_audit.log""",
    },
    {
        "day": 2,
        "date": '2026-11-10',
        "title": 'Network Bonding & Bridging',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Create Linux Software Bridge
1. Create a software bridge interface named `br0` using `ip link`:
   `sudo ip link add br0 type bridge`
2. Assign IP address `192.168.100.1/24` to `br0`.
3. Bring `br0` interface UP.

### Task 2: Create Virtual Ethernet Pair (veth)
1. Create a virtual ethernet pair named `veth-host` and `veth-guest`:
   `sudo ip link add veth-host type veth peer name veth-guest`

### Task 3: Attach Slave Interface to Bridge
1. Attach `veth-host` to bridge `br0` as a master bridge port:
   `sudo ip link set veth-host master br0`
2. Bring `veth-host` and `veth-guest` interfaces UP:
   `sudo ip link set veth-host up`
   `sudo ip link set veth-guest up`""",
        "setup": """sudo ip link del veth-host 2>/dev/null || true
sudo ip link del br0 2>/dev/null || true""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: Bridge br0 has IP 192.168.100.1/24 and is up
if ip addr show dev br0 2>/dev/null | grep -q "192.168.100.1/24"; then
  echo -e "${GREEN}[PASS] Task 1: Bridge br0 exists with IP 192.168.100.1/24.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Bridge br0 missing or IP 192.168.100.1/24 not assigned.${NC}"
fi

# Task 2: veth pair exists
if ip link show dev veth-guest >/dev/null 2>&1 && ip link show dev veth-host >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 2: Virtual ethernet pair veth-host and veth-guest created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: veth pair missing.${NC}"
fi

# Task 3: veth-host attached to br0 as master
MASTER=$(ip link show dev veth-host 2>/dev/null | grep -o "master br0" || true)
if [ "$MASTER" == "master br0" ]; then
  echo -e "${GREEN}[PASS] Task 3: veth-host attached to master bridge br0.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: veth-host master is not br0.${NC}"
fi""",
        "solution": """1. Create bridge br0:
`sudo ip link add br0 type bridge`
`sudo ip addr add 192.168.100.1/24 dev br0`
`sudo ip link set br0 up`

2. Create veth pair:
`sudo ip link add veth-host type veth peer name veth-guest`

3. Attach to bridge and bring up:
`sudo ip link set veth-host master br0`
`sudo ip link set veth-host up`
`sudo ip link set veth-guest up`""",
        "reset": """sudo ip link del veth-host 2>/dev/null || true
sudo ip link del br0 2>/dev/null || true""",
        "lfcs_title": 'Network Bonding & Bridging',
        "lfcs_diff": 'Medium',
        "lfcs_time": '35m',
        "lfcs_tasks": """### Task 1: Create Linux Software Bridge
1. Create a software bridge interface named `br0` using `ip link`:
   `sudo ip link add br0 type bridge`
2. Assign IP address `192.168.100.1/24` to `br0`.
3. Bring `br0` interface UP.

### Task 2: Create Virtual Ethernet Pair (veth)
1. Create a virtual ethernet pair named `veth-host` and `veth-guest`:
   `sudo ip link add veth-host type veth peer name veth-guest`

### Task 3: Attach Slave Interface to Bridge
1. Attach `veth-host` to bridge `br0` as a master bridge port:
   `sudo ip link set veth-host master br0`
2. Bring `veth-host` and `veth-guest` interfaces UP:
   `sudo ip link set veth-host up`
   `sudo ip link set veth-guest up`""",
        "lfcs_setup": """sudo ip link del veth-host 2>/dev/null || true
sudo ip link del br0 2>/dev/null || true""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: Bridge br0 has IP 192.168.100.1/24 and is up
if ip addr show dev br0 2>/dev/null | grep -q "192.168.100.1/24"; then
  echo -e "${GREEN}[PASS] Task 1: Bridge br0 exists with IP 192.168.100.1/24.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Bridge br0 missing or IP 192.168.100.1/24 not assigned.${NC}"
fi

# Task 2: veth pair exists
if ip link show dev veth-guest >/dev/null 2>&1 && ip link show dev veth-host >/dev/null 2>&1; then
  echo -e "${GREEN}[PASS] Task 2: Virtual ethernet pair veth-host and veth-guest created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: veth pair missing.${NC}"
fi

# Task 3: veth-host attached to br0 as master
MASTER=$(ip link show dev veth-host 2>/dev/null | grep -o "master br0" || true)
if [ "$MASTER" == "master br0" ]; then
  echo -e "${GREEN}[PASS] Task 3: veth-host attached to master bridge br0.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: veth-host master is not br0.${NC}"
fi""",
        "lfcs_solution": """1. Create bridge br0:
`sudo ip link add br0 type bridge`
`sudo ip addr add 192.168.100.1/24 dev br0`
`sudo ip link set br0 up`

2. Create veth pair:
`sudo ip link add veth-host type veth peer name veth-guest`

3. Attach to bridge and bring up:
`sudo ip link set veth-host master br0`
`sudo ip link set veth-host up`
`sudo ip link set veth-guest up`""",
        "lfcs_reset": """sudo ip link del veth-host 2>/dev/null || true
sudo ip link del br0 2>/dev/null || true""",
    },
    {
        "day": 3,
        "date": '2026-11-11',
        "title": 'Packet Filtering with Firewalld & Iptables',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Block Port with Iptables
1. Append a rule to the `INPUT` chain that drops all incoming TCP packets destined for port `8088`:
   `sudo iptables -A INPUT -p tcp --dport 8088 -j DROP`

### Task 2: Allow Subnet ICMP Traffic
1. Insert a rule at position 1 in the `INPUT` chain that explicitly allows incoming ICMP echo-requests (ping) originating from `192.168.0.0/16`:
   `sudo iptables -I INPUT 1 -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT`

### Task 3: Backup Active Iptables Rules
1. Export the active IPv4 iptables ruleset to `/var/tmp/iptables_backup.rules` using `iptables-save`:
   `sudo iptables-save | sudo tee /var/tmp/iptables_backup.rules > /dev/null`""",
        "setup": """sudo iptables -D INPUT -p tcp --dport 8088 -j DROP 2>/dev/null || true
sudo iptables -D INPUT -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT 2>/dev/null || true
sudo rm -f /var/tmp/iptables_backup.rules""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: DROP rule for port 8088
if sudo iptables -S INPUT | grep -q -- "-p tcp -m tcp --dport 8088 -j DROP\|-p tcp --dport 8088 -j DROP"; then
  echo -e "${GREEN}[PASS] Task 1: Iptables rule dropping port 8088 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: DROP rule for port 8088 not found in INPUT chain.${NC}"
fi

# Task 2: ACCEPT rule for ICMP from 192.168.0.0/16
if sudo iptables -S INPUT | grep -q -- "-p icmp -m icmp --icmp-type 8 -s 192.168.0.0/16 -j ACCEPT\|-s 192.168.0.0/16.*-p icmp.*-j ACCEPT"; then
  echo -e "${GREEN}[PASS] Task 2: Iptables rule allowing ICMP from 192.168.0.0/16 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: ACCEPT rule for ICMP from 192.168.0.0/16 not found in INPUT chain.${NC}"
fi

# Task 3: Rules backup file exists
if [ -s /var/tmp/iptables_backup.rules ] && grep -q "8088" /var/tmp/iptables_backup.rules; then
  echo -e "${GREEN}[PASS] Task 3: Active iptables rules successfully backed up to /var/tmp/iptables_backup.rules.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/iptables_backup.rules missing or empty.${NC}"
fi""",
        "solution": """1. Block port 8088:
`sudo iptables -A INPUT -p tcp --dport 8088 -j DROP`

2. Allow ICMP echo from 192.168.0.0/16:
`sudo iptables -I INPUT 1 -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT`

3. Save rules:
`sudo iptables-save | sudo tee /var/tmp/iptables_backup.rules > /dev/null`""",
        "reset": """sudo iptables -D INPUT -p tcp --dport 8088 -j DROP 2>/dev/null || true
sudo iptables -D INPUT -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT 2>/dev/null || true
sudo rm -f /var/tmp/iptables_backup.rules""",
        "lfcs_title": 'Packet Filtering with Firewalld & Iptables',
        "lfcs_diff": 'Medium',
        "lfcs_time": '35m',
        "lfcs_tasks": """### Task 1: Block Port with Iptables
1. Append a rule to the `INPUT` chain that drops all incoming TCP packets destined for port `8088`:
   `sudo iptables -A INPUT -p tcp --dport 8088 -j DROP`

### Task 2: Allow Subnet ICMP Traffic
1. Insert a rule at position 1 in the `INPUT` chain that explicitly allows incoming ICMP echo-requests (ping) originating from `192.168.0.0/16`:
   `sudo iptables -I INPUT 1 -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT`

### Task 3: Backup Active Iptables Rules
1. Export the active IPv4 iptables ruleset to `/var/tmp/iptables_backup.rules` using `iptables-save`:
   `sudo iptables-save | sudo tee /var/tmp/iptables_backup.rules > /dev/null`""",
        "lfcs_setup": """sudo iptables -D INPUT -p tcp --dport 8088 -j DROP 2>/dev/null || true
sudo iptables -D INPUT -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT 2>/dev/null || true
sudo rm -f /var/tmp/iptables_backup.rules""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: DROP rule for port 8088
if sudo iptables -S INPUT | grep -q -- "-p tcp -m tcp --dport 8088 -j DROP\|-p tcp --dport 8088 -j DROP"; then
  echo -e "${GREEN}[PASS] Task 1: Iptables rule dropping port 8088 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: DROP rule for port 8088 not found in INPUT chain.${NC}"
fi

# Task 2: ACCEPT rule for ICMP from 192.168.0.0/16
if sudo iptables -S INPUT | grep -q -- "-p icmp -m icmp --icmp-type 8 -s 192.168.0.0/16 -j ACCEPT\|-s 192.168.0.0/16.*-p icmp.*-j ACCEPT"; then
  echo -e "${GREEN}[PASS] Task 2: Iptables rule allowing ICMP from 192.168.0.0/16 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: ACCEPT rule for ICMP from 192.168.0.0/16 not found in INPUT chain.${NC}"
fi

# Task 3: Rules backup file exists
if [ -s /var/tmp/iptables_backup.rules ] && grep -q "8088" /var/tmp/iptables_backup.rules; then
  echo -e "${GREEN}[PASS] Task 3: Active iptables rules successfully backed up to /var/tmp/iptables_backup.rules.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/iptables_backup.rules missing or empty.${NC}"
fi""",
        "lfcs_solution": """1. Block port 8088:
`sudo iptables -A INPUT -p tcp --dport 8088 -j DROP`

2. Allow ICMP echo from 192.168.0.0/16:
`sudo iptables -I INPUT 1 -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT`

3. Save rules:
`sudo iptables-save | sudo tee /var/tmp/iptables_backup.rules > /dev/null`""",
        "lfcs_reset": """sudo iptables -D INPUT -p tcp --dport 8088 -j DROP 2>/dev/null || true
sudo iptables -D INPUT -p icmp --icmp-type echo-request -s 192.168.0.0/16 -j ACCEPT 2>/dev/null || true
sudo rm -f /var/tmp/iptables_backup.rules""",
    },
    {
        "day": 4,
        "date": '2026-11-12',
        "title": 'NAT, Port Redirection & Reverse Proxies',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Kernel IP Packet Forwarding
1. Configure persistent IP packet forwarding in `/etc/sysctl.d/99-ipforward.conf`:
   `net.ipv4.ip_forward = 1`
2. Apply the setting immediately:
   `sudo sysctl -p /etc/sysctl.d/99-ipforward.conf`

### Task 2: Iptables NAT Port Redirection
1. Configure an iptables NAT table `PREROUTING` rule to redirect incoming TCP traffic on port `8080` to local port `80`:
   `sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-ports 80`

### Task 3: Reverse Proxy Configuration Template
1. Create a reverse proxy configuration file at `/var/tmp/reverse_proxy.conf` simulating an Nginx proxy pass:
```nginx
server {
    listen 8888;
    server_name localhost;

    location / {
        proxy_pass http://127.0.0.1:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```""",
        "setup": """sudo rm -f /etc/sysctl.d/99-ipforward.conf /var/tmp/reverse_proxy.conf
sudo sysctl -w net.ipv4.ip_forward=0 >/dev/null 2>&1 || true
sudo iptables -t nat -D PREROUTING -p tcp --dport 8080 -j REDIRECT --to-ports 80 2>/dev/null || true""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: IP forward enabled in sysctl and file
SYSCTL_VAL=$(sysctl -n net.ipv4.ip_forward 2>/dev/null || echo "0")
if [ "$SYSCTL_VAL" == "1" ] && grep -q "net.ipv4.ip_forward.*=.*1" /etc/sysctl.d/99-ipforward.conf 2>/dev/null; then
  echo -e "${GREEN}[PASS] Task 1: IP packet forwarding enabled persistently.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: net.ipv4.ip_forward is $SYSCTL_VAL or /etc/sysctl.d/99-ipforward.conf missing.${NC}"
fi

# Task 2: iptables NAT redirection
if sudo iptables -t nat -S PREROUTING | grep -q -- "-p tcp -m tcp --dport 8080 -j REDIRECT --to-ports 80\|-p tcp --dport 8080 -j REDIRECT --to-ports 80"; then
  echo -e "${GREEN}[PASS] Task 2: Iptables PREROUTING redirection 8080 -> 80 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: NAT PREROUTING redirection for port 8080 not found.${NC}"
fi

# Task 3: Reverse proxy configuration template
if [ -s /var/tmp/reverse_proxy.conf ] && grep -q "listen 8888" /var/tmp/reverse_proxy.conf && grep -q "proxy_pass http://127.0.0.1:80" /var/tmp/reverse_proxy.conf; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/reverse_proxy.conf reverse proxy configuration verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/reverse_proxy.conf missing or proxy settings incorrect.${NC}"
fi""",
        "solution": """1. Configure persistent IP forwarding:
```bash
echo "net.ipv4.ip_forward = 1" | sudo tee /etc/sysctl.d/99-ipforward.conf
sudo sysctl -p /etc/sysctl.d/99-ipforward.conf
```

2. Configure NAT port redirect:
`sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-ports 80`

3. Create `/var/tmp/reverse_proxy.conf`:
```bash
cat << "EOF" > /var/tmp/reverse_proxy.conf
server {
    listen 8888;
    server_name localhost;

    location / {
        proxy_pass http://127.0.0.1:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
EOF
```""",
        "reset": """sudo rm -f /etc/sysctl.d/99-ipforward.conf /var/tmp/reverse_proxy.conf
sudo iptables -t nat -D PREROUTING -p tcp --dport 8080 -j REDIRECT --to-ports 80 2>/dev/null || true""",
        "lfcs_title": 'NAT, Port Redirection & Reverse Proxies',
        "lfcs_diff": 'Medium',
        "lfcs_time": '35m',
        "lfcs_tasks": """### Task 1: Kernel IP Packet Forwarding
1. Configure persistent IP packet forwarding in `/etc/sysctl.d/99-ipforward.conf`:
   `net.ipv4.ip_forward = 1`
2. Apply the setting immediately:
   `sudo sysctl -p /etc/sysctl.d/99-ipforward.conf`

### Task 2: Iptables NAT Port Redirection
1. Configure an iptables NAT table `PREROUTING` rule to redirect incoming TCP traffic on port `8080` to local port `80`:
   `sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-ports 80`

### Task 3: Reverse Proxy Configuration Template
1. Create a reverse proxy configuration file at `/var/tmp/reverse_proxy.conf` simulating an Nginx proxy pass:
```nginx
server {
    listen 8888;
    server_name localhost;

    location / {
        proxy_pass http://127.0.0.1:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```""",
        "lfcs_setup": """sudo rm -f /etc/sysctl.d/99-ipforward.conf /var/tmp/reverse_proxy.conf
sudo sysctl -w net.ipv4.ip_forward=0 >/dev/null 2>&1 || true
sudo iptables -t nat -D PREROUTING -p tcp --dport 8080 -j REDIRECT --to-ports 80 2>/dev/null || true""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: IP forward enabled in sysctl and file
SYSCTL_VAL=$(sysctl -n net.ipv4.ip_forward 2>/dev/null || echo "0")
if [ "$SYSCTL_VAL" == "1" ] && grep -q "net.ipv4.ip_forward.*=.*1" /etc/sysctl.d/99-ipforward.conf 2>/dev/null; then
  echo -e "${GREEN}[PASS] Task 1: IP packet forwarding enabled persistently.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: net.ipv4.ip_forward is $SYSCTL_VAL or /etc/sysctl.d/99-ipforward.conf missing.${NC}"
fi

# Task 2: iptables NAT redirection
if sudo iptables -t nat -S PREROUTING | grep -q -- "-p tcp -m tcp --dport 8080 -j REDIRECT --to-ports 80\|-p tcp --dport 8080 -j REDIRECT --to-ports 80"; then
  echo -e "${GREEN}[PASS] Task 2: Iptables PREROUTING redirection 8080 -> 80 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: NAT PREROUTING redirection for port 8080 not found.${NC}"
fi

# Task 3: Reverse proxy configuration template
if [ -s /var/tmp/reverse_proxy.conf ] && grep -q "listen 8888" /var/tmp/reverse_proxy.conf && grep -q "proxy_pass http://127.0.0.1:80" /var/tmp/reverse_proxy.conf; then
  echo -e "${GREEN}[PASS] Task 3: /var/tmp/reverse_proxy.conf reverse proxy configuration verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: /var/tmp/reverse_proxy.conf missing or proxy settings incorrect.${NC}"
fi""",
        "lfcs_solution": """1. Configure persistent IP forwarding:
```bash
echo "net.ipv4.ip_forward = 1" | sudo tee /etc/sysctl.d/99-ipforward.conf
sudo sysctl -p /etc/sysctl.d/99-ipforward.conf
```

2. Configure NAT port redirect:
`sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-ports 80`

3. Create `/var/tmp/reverse_proxy.conf`:
```bash
cat << "EOF" > /var/tmp/reverse_proxy.conf
server {
    listen 8888;
    server_name localhost;

    location / {
        proxy_pass http://127.0.0.1:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
EOF
```""",
        "lfcs_reset": """sudo rm -f /etc/sysctl.d/99-ipforward.conf /var/tmp/reverse_proxy.conf
sudo iptables -t nat -D PREROUTING -p tcp --dport 8080 -j REDIRECT --to-ports 80 2>/dev/null || true""",
    },
    {
        "day": 5,
        "date": '2026-11-13',
        "title": 'SSH Hardening, Key Auth & Time Sync',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Generate & Authorize RSA SSH Key Pair
1. For user `student`, generate a 4096-bit RSA SSH key pair at `/home/student/.ssh/id_admin_rsa` without a passphrase:
   `ssh-keygen -t rsa -b 4096 -N "" -f /home/student/.ssh/id_admin_rsa`
2. Append the public key to `/home/student/.ssh/authorized_keys`.
3. Ensure file permissions are `0600` on `authorized_keys` and `0700` on `~/.ssh`.

### Task 2: SSH Server Configuration Hardening
1. Create a drop-in configuration file `/etc/ssh/sshd_config.d/99-hardening.conf` containing:
   ```
   PermitRootLogin no
   MaxAuthTries 3
   ClientAliveInterval 300
   ClientAliveCountMax 2
   ```
2. Test configuration syntax using `sudo sshd -t`.

### Task 3: Time Synchronization Verification
1. Ensure system NTP synchronization is active using `timedatectl`:
   `sudo timedatectl set-ntp true`
2. Confirm system clock synchronization state using `timedatectl status`.""",
        "setup": 'sudo rm -f /home/student/.ssh/id_admin_rsa /home/student/.ssh/id_admin_rsa.pub /etc/ssh/sshd_config.d/99-hardening.conf',
        "verify": """SCORE=0; TOTAL=3
# Task 1: Key exists, 4096 bit, authorized_keys has 0600
KEY_BITS=$(ssh-keygen -l -f /home/student/.ssh/id_admin_rsa 2>/dev/null | awk '{print $1}')
AUTH_PERMS=$(stat -c "%a" /home/student/.ssh/authorized_keys 2>/dev/null || echo "000")
if [ "$KEY_BITS" == "4096" ] && [ "$AUTH_PERMS" == "600" ]; then
  echo -e "${GREEN}[PASS] Task 1: 4096-bit SSH key generated and authorized_keys permissions verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Key bits=$KEY_BITS (exp 4096), authorized_keys perms=$AUTH_PERMS (exp 600).${NC}"
fi

# Task 2: sshd hardening drop-in and test
if [ -f /etc/ssh/sshd_config.d/99-hardening.conf ] && grep -q "PermitRootLogin no" /etc/ssh/sshd_config.d/99-hardening.conf && grep -q "MaxAuthTries 3" /etc/ssh/sshd_config.d/99-hardening.conf && sudo sshd -t; then
  echo -e "${GREEN}[PASS] Task 2: /etc/ssh/sshd_config.d/99-hardening.conf verified and sshd -t passed.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: sshd hardening configuration missing or syntax test failed.${NC}"
fi

# Task 3: NTP active
NTP_STATUS=$(timedatectl show -p NTP --value 2>/dev/null || echo "no")
if [ "$NTP_STATUS" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 3: System NTP synchronization is active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: NTP synchronization is $NTP_STATUS (expected yes).${NC}"
fi""",
        "solution": """1. Generate key and authorize:
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
`sudo timedatectl set-ntp true`""",
        "reset": 'sudo rm -f /home/student/.ssh/id_admin_rsa /home/student/.ssh/id_admin_rsa.pub /etc/ssh/sshd_config.d/99-hardening.conf',
        "lfcs_title": 'SSH Hardening, Key Auth & Time Sync',
        "lfcs_diff": 'Medium',
        "lfcs_time": '35m',
        "lfcs_tasks": """### Task 1: Generate & Authorize RSA SSH Key Pair
1. For user `student`, generate a 4096-bit RSA SSH key pair at `/home/student/.ssh/id_admin_rsa` without a passphrase:
   `ssh-keygen -t rsa -b 4096 -N "" -f /home/student/.ssh/id_admin_rsa`
2. Append the public key to `/home/student/.ssh/authorized_keys`.
3. Ensure file permissions are `0600` on `authorized_keys` and `0700` on `~/.ssh`.

### Task 2: SSH Server Configuration Hardening
1. Create a drop-in configuration file `/etc/ssh/sshd_config.d/99-hardening.conf` containing:
   ```
   PermitRootLogin no
   MaxAuthTries 3
   ClientAliveInterval 300
   ClientAliveCountMax 2
   ```
2. Test configuration syntax using `sudo sshd -t`.

### Task 3: Time Synchronization Verification
1. Ensure system NTP synchronization is active using `timedatectl`:
   `sudo timedatectl set-ntp true`
2. Confirm system clock synchronization state using `timedatectl status`.""",
        "lfcs_setup": 'sudo rm -f /home/student/.ssh/id_admin_rsa /home/student/.ssh/id_admin_rsa.pub /etc/ssh/sshd_config.d/99-hardening.conf',
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: Key exists, 4096 bit, authorized_keys has 0600
KEY_BITS=$(ssh-keygen -l -f /home/student/.ssh/id_admin_rsa 2>/dev/null | awk '{print $1}')
AUTH_PERMS=$(stat -c "%a" /home/student/.ssh/authorized_keys 2>/dev/null || echo "000")
if [ "$KEY_BITS" == "4096" ] && [ "$AUTH_PERMS" == "600" ]; then
  echo -e "${GREEN}[PASS] Task 1: 4096-bit SSH key generated and authorized_keys permissions verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Key bits=$KEY_BITS (exp 4096), authorized_keys perms=$AUTH_PERMS (exp 600).${NC}"
fi

# Task 2: sshd hardening drop-in and test
if [ -f /etc/ssh/sshd_config.d/99-hardening.conf ] && grep -q "PermitRootLogin no" /etc/ssh/sshd_config.d/99-hardening.conf && grep -q "MaxAuthTries 3" /etc/ssh/sshd_config.d/99-hardening.conf && sudo sshd -t; then
  echo -e "${GREEN}[PASS] Task 2: /etc/ssh/sshd_config.d/99-hardening.conf verified and sshd -t passed.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: sshd hardening configuration missing or syntax test failed.${NC}"
fi

# Task 3: NTP active
NTP_STATUS=$(timedatectl show -p NTP --value 2>/dev/null || echo "no")
if [ "$NTP_STATUS" == "yes" ]; then
  echo -e "${GREEN}[PASS] Task 3: System NTP synchronization is active.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: NTP synchronization is $NTP_STATUS (expected yes).${NC}"
fi""",
        "lfcs_solution": """1. Generate key and authorize:
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
`sudo timedatectl set-ntp true`""",
        "lfcs_reset": 'sudo rm -f /home/student/.ssh/id_admin_rsa /home/student/.ssh/id_admin_rsa.pub /etc/ssh/sshd_config.d/99-hardening.conf',
    },
    {
        "day": 6,
        "date": '2026-11-14',
        "title": 'Week 7 Linux Networking & Firewall Marathon',
        "diff": 'Hard (Milestone)',
        "time": '45m',
        "tasks": """### Task 1: Bridge Network Construction
1. Create a software bridge interface `br-marathon` with IP `172.25.1.1/24` and bring it UP:
   `sudo ip link add br-marathon type bridge`
   `sudo ip addr add 172.25.1.1/24 dev br-marathon`
   `sudo ip link set br-marathon up`

### Task 2: Virtual Interface Attachment
1. Create a veth pair `veth-m1` and `veth-m2`.
2. Attach `veth-m1` to `br-marathon` as a slave port.
3. Bring both `veth-m1` and `veth-m2` interfaces UP.

### Task 3: Firewall Filtering & NAT Redirection
1. Redirect incoming TCP traffic on port `9090` to local port `80` using iptables NAT table PREROUTING chain:
   `sudo iptables -t nat -A PREROUTING -p tcp --dport 9090 -j REDIRECT --to-ports 80`
2. Drop all incoming UDP traffic on port `5353` in the INPUT chain:
   `sudo iptables -A INPUT -p udp --dport 5353 -j DROP`

### Task 4: Network Health Check Script
1. Create an executable script `/usr/local/bin/network_health.sh`.
2. If `br-marathon` is in state UP, write `STATUS=HEALTHY` to `/var/log/net_marathon.status`.
3. Execute the script once to confirm.""",
        "setup": """sudo ip link del veth-m1 2>/dev/null || true
sudo ip link del br-marathon 2>/dev/null || true
sudo iptables -t nat -D PREROUTING -p tcp --dport 9090 -j REDIRECT --to-ports 80 2>/dev/null || true
sudo iptables -D INPUT -p udp --dport 5353 -j DROP 2>/dev/null || true
sudo rm -f /usr/local/bin/network_health.sh /var/log/net_marathon.status""",
        "verify": """SCORE=0; TOTAL=4
# Task 1: br-marathon exists with 172.25.1.1/24
if ip addr show dev br-marathon 2>/dev/null | grep -q "172.25.1.1/24"; then
  echo -e "${GREEN}[PASS] Task 1: Bridge br-marathon verified with IP 172.25.1.1/24.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Bridge br-marathon missing or IP not set.${NC}"
fi

# Task 2: veth-m1 attached to br-marathon
if ip link show dev veth-m1 2>/dev/null | grep -q "master br-marathon"; then
  echo -e "${GREEN}[PASS] Task 2: veth-m1 attached to master br-marathon.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: veth-m1 master is not br-marathon.${NC}"
fi

# Task 3: iptables rules
NAT_OK=$(sudo iptables -t nat -S PREROUTING 2>/dev/null | grep -E -- "--dport 9090.*REDIRECT.*--to-ports 80" || true)
IN_OK=$(sudo iptables -S INPUT 2>/dev/null | grep -E -- "-p udp.*--dport 5353.*-j DROP" || true)
if [ -n "$NAT_OK" ] && [ -n "$IN_OK" ]; then
  echo -e "${GREEN}[PASS] Task 3: NAT port 9090 redirection and UDP 5353 drop rules verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Firewall rules missing (NAT=$NAT_OK, INPUT=$IN_OK).${NC}"
fi

# Task 4: Health script and status log
if [ -x /usr/local/bin/network_health.sh ] && grep -q "STATUS=HEALTHY" /var/log/net_marathon.status 2>/dev/null; then
  echo -e "${GREEN}[PASS] Task 4: /usr/local/bin/network_health.sh and /var/log/net_marathon.status verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: /var/log/net_marathon.status missing or status not HEALTHY.${NC}"
fi""",
        "solution": """1. Bridge configuration:
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
```""",
        "reset": """sudo ip link del veth-m1 2>/dev/null || true
sudo ip link del br-marathon 2>/dev/null || true
sudo iptables -t nat -D PREROUTING -p tcp --dport 9090 -j REDIRECT --to-ports 80 2>/dev/null || true
sudo iptables -D INPUT -p udp --dport 5353 -j DROP 2>/dev/null || true
sudo rm -f /usr/local/bin/network_health.sh /var/log/net_marathon.status""",
        "lfcs_title": 'Week 7 Linux Networking & Firewall Marathon',
        "lfcs_diff": 'Hard (Milestone)',
        "lfcs_time": '45m',
        "lfcs_tasks": """### Task 1: Bridge Network Construction
1. Create a software bridge interface `br-marathon` with IP `172.25.1.1/24` and bring it UP:
   `sudo ip link add br-marathon type bridge`
   `sudo ip addr add 172.25.1.1/24 dev br-marathon`
   `sudo ip link set br-marathon up`

### Task 2: Virtual Interface Attachment
1. Create a veth pair `veth-m1` and `veth-m2`.
2. Attach `veth-m1` to `br-marathon` as a slave port.
3. Bring both `veth-m1` and `veth-m2` interfaces UP.

### Task 3: Firewall Filtering & NAT Redirection
1. Redirect incoming TCP traffic on port `9090` to local port `80` using iptables NAT table PREROUTING chain:
   `sudo iptables -t nat -A PREROUTING -p tcp --dport 9090 -j REDIRECT --to-ports 80`
2. Drop all incoming UDP traffic on port `5353` in the INPUT chain:
   `sudo iptables -A INPUT -p udp --dport 5353 -j DROP`

### Task 4: Network Health Check Script
1. Create an executable script `/usr/local/bin/network_health.sh`.
2. If `br-marathon` is in state UP, write `STATUS=HEALTHY` to `/var/log/net_marathon.status`.
3. Execute the script once to confirm.""",
        "lfcs_setup": """sudo ip link del veth-m1 2>/dev/null || true
sudo ip link del br-marathon 2>/dev/null || true
sudo iptables -t nat -D PREROUTING -p tcp --dport 9090 -j REDIRECT --to-ports 80 2>/dev/null || true
sudo iptables -D INPUT -p udp --dport 5353 -j DROP 2>/dev/null || true
sudo rm -f /usr/local/bin/network_health.sh /var/log/net_marathon.status""",
        "lfcs_verify": """SCORE=0; TOTAL=4
# Task 1: br-marathon exists with 172.25.1.1/24
if ip addr show dev br-marathon 2>/dev/null | grep -q "172.25.1.1/24"; then
  echo -e "${GREEN}[PASS] Task 1: Bridge br-marathon verified with IP 172.25.1.1/24.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Bridge br-marathon missing or IP not set.${NC}"
fi

# Task 2: veth-m1 attached to br-marathon
if ip link show dev veth-m1 2>/dev/null | grep -q "master br-marathon"; then
  echo -e "${GREEN}[PASS] Task 2: veth-m1 attached to master br-marathon.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: veth-m1 master is not br-marathon.${NC}"
fi

# Task 3: iptables rules
NAT_OK=$(sudo iptables -t nat -S PREROUTING 2>/dev/null | grep -E -- "--dport 9090.*REDIRECT.*--to-ports 80" || true)
IN_OK=$(sudo iptables -S INPUT 2>/dev/null | grep -E -- "-p udp.*--dport 5353.*-j DROP" || true)
if [ -n "$NAT_OK" ] && [ -n "$IN_OK" ]; then
  echo -e "${GREEN}[PASS] Task 3: NAT port 9090 redirection and UDP 5353 drop rules verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Firewall rules missing (NAT=$NAT_OK, INPUT=$IN_OK).${NC}"
fi

# Task 4: Health script and status log
if [ -x /usr/local/bin/network_health.sh ] && grep -q "STATUS=HEALTHY" /var/log/net_marathon.status 2>/dev/null; then
  echo -e "${GREEN}[PASS] Task 4: /usr/local/bin/network_health.sh and /var/log/net_marathon.status verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 4: /var/log/net_marathon.status missing or status not HEALTHY.${NC}"
fi""",
        "lfcs_solution": """1. Bridge configuration:
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
```""",
        "lfcs_reset": """sudo ip link del veth-m1 2>/dev/null || true
sudo ip link del br-marathon 2>/dev/null || true
sudo iptables -t nat -D PREROUTING -p tcp --dport 9090 -j REDIRECT --to-ports 80 2>/dev/null || true
sudo iptables -D INPUT -p udp --dport 5353 -j DROP 2>/dev/null || true
sudo rm -f /usr/local/bin/network_health.sh /var/log/net_marathon.status""",
    },
]
