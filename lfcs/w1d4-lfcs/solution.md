# [LFCS W1D4-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create group and configure SGID directory:
```bash
sudo groupadd -f marketing
sudo mkdir -p /opt/campaigns
sudo chown root:marketing /opt/campaigns
sudo chmod 2770 /opt/campaigns
```

2. Configure Sticky bit directory:
```bash
sudo mkdir -p /opt/campaigns/incoming
sudo chown root:marketing /opt/campaigns/incoming
sudo chmod 1770 /opt/campaigns/incoming
```

3. World-writable audit:
```bash
sudo find /var/log -type f -perm -002 > /var/tmp/world_writable_audit.txt
```
