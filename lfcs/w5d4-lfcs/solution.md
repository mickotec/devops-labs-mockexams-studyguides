# [LFCS W5D4-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create sysctl configuration:
```ini
net.ipv4.ip_forward = 1
net.ipv4.icmp_echo_ignore_broadcasts = 1
```
`sudo tee /etc/sysctl.d/60-hardening.conf`
`sudo sysctl -p /etc/sysctl.d/60-hardening.conf`

2. Record:
`sysctl net.ipv4.ip_forward net.ipv4.icmp_echo_ignore_broadcasts > /var/tmp/kernel_params.txt`
