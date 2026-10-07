# [LFCS W8D3-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Archive config files:
`sudo find /etc -name "*.conf" | tar -czf /var/tmp/etc_configs.tar.gz -T - 2>/dev/null`

2. Create and enable swap:
```bash
sudo fallocate -l 128M /swapfile_mock2 || sudo dd if=/dev/zero of=/swapfile_mock2 bs=1M count=128
sudo chmod 0600 /swapfile_mock2
sudo mkswap /swapfile_mock2
sudo swapon /swapfile_mock2
```

3. Launch process with nice +10:
`nice -n 10 sleep 7200 &`

4. Count status in dpkg log:
`grep "status" /var/log/dpkg.log* 2>/dev/null | wc -l > /var/tmp/auth_summary.txt`
