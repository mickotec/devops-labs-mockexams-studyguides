# [LFCS W5D6-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Quarantine:
`sudo passwd -l hacked_service`
`sudo usermod -s /usr/sbin/nologin hacked_service`
`sudo chage -E 0 hacked_service`

2. Sudoers:
`sudo visudo -c`

3. Sysctl:
`echo -e "net.ipv4.tcp_syncookies = 1
net.ipv4.conf.all.rp_filter = 1" | sudo tee /etc/sysctl.d/99-security.conf`
`sudo sysctl -p /etc/sysctl.d/99-security.conf`
