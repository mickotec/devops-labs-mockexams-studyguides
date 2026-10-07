# [LFCS W6D2-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Format:
`sudo mkfs.ext4 -L DATA_STORE /dev/loop90`

2. UUID and fstab:
`UUID=$(sudo blkid -s UUID -o value /dev/loop90)`
`echo "UUID=$UUID /mnt/data_store ext4 defaults,noatime 0 2" | sudo tee -a /etc/fstab`

3. Mount:
`sudo mount -a`
