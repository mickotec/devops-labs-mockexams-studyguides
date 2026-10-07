# [LFCS W7D4-LFCS] NAT, Port Redirection & Reverse Proxies

**Date:** 2026-11-12  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Kernel IP Packet Forwarding
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
```

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w7d4-lfcs
```
