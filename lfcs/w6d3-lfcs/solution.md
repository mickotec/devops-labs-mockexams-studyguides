# [LFCS W6D3-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. LVM setup:
`sudo pvcreate /dev/loop91`
`sudo vgcreate vg_database /dev/loop91`
`sudo lvcreate -L 120M -n lv_orders vg_database`

2. Format & mount:
`sudo mkfs.ext4 /dev/vg_database/lv_orders`
`sudo mount /dev/vg_database/lv_orders /mnt/orders_data`
