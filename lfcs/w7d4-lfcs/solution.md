# [LFCS W7D4-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Configure persistent IP forwarding:
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
```
