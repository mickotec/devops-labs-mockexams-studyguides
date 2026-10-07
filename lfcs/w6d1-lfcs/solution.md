# [LFCS W6D1-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create & format swap:
`sudo dd if=/dev/zero of=/var/tmp/swapfile_extra bs=1M count=128`
`sudo chmod 600 /var/tmp/swapfile_extra`
`sudo mkswap /var/tmp/swapfile_extra`

2. Activate & persist:
`sudo swapon /var/tmp/swapfile_extra`
`echo "/var/tmp/swapfile_extra none swap sw 0 0" | sudo tee -a /etc/fstab`
