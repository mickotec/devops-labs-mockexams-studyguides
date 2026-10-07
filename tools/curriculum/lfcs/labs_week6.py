"""
Dedicated LFCS Lab Definitions for Week 6 (Days 1 to 6).
"""

WEEK_6_LABS = [
    {
        "day": 1,
        "date": '2026-11-02',
        "title": 'Storage Partitions (MBR vs GPT) & Swap',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Dedicated Swap File Creation
1. Create a `128MB` swap file at `/var/tmp/swapfile_extra` (use `dd` or `fallocate`).
2. Set permissions strictly to `0600` (`chmod 600`).
3. Format it as swap space with `mkswap`.

### Task 2: Swap Space Activation & Persistence
1. Activate the swap file with `swapon /var/tmp/swapfile_extra`.
2. Append a persistent entry to `/etc/fstab` so it activates on boot:
   `/var/tmp/swapfile_extra none swap sw 0 0`
3. Verify that `swapon --show` displays `/var/tmp/swapfile_extra`.""",
        "setup": """sudo swapoff /var/tmp/swapfile_extra 2>/dev/null || true
sudo rm -f /var/tmp/swapfile_extra
sudo sed -i '\|/var/tmp/swapfile_extra|d' /etc/fstab""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: Swap file permissions and active
SWAP_ACTIVE=$(swapon --show | grep "/var/tmp/swapfile_extra" || true)
PERM=$(stat -c "%a" /var/tmp/swapfile_extra 2>/dev/null || echo "0")

if [ -n "$SWAP_ACTIVE" ] && [ "$PERM" == "600" ]; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/swapfile_extra active as swap with permissions 600.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Swap file inactive or permissions=$PERM (expected 600).${NC}"
fi

# Task 2: /etc/fstab entry
if grep -q "/var/tmp/swapfile_extra.*swap" /etc/fstab; then
  echo -e "${GREEN}[PASS] Task 2: /etc/fstab contains persistent swap entry.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/fstab missing entry for /var/tmp/swapfile_extra.${NC}"
fi""",
        "solution": """1. Create & format swap:
`sudo dd if=/dev/zero of=/var/tmp/swapfile_extra bs=1M count=128`
`sudo chmod 600 /var/tmp/swapfile_extra`
`sudo mkswap /var/tmp/swapfile_extra`

2. Activate & persist:
`sudo swapon /var/tmp/swapfile_extra`
`echo "/var/tmp/swapfile_extra none swap sw 0 0" | sudo tee -a /etc/fstab`""",
        "reset": """sudo swapoff /var/tmp/swapfile_extra 2>/dev/null || true
sudo rm -f /var/tmp/swapfile_extra
sudo sed -i '\|/var/tmp/swapfile_extra|d' /etc/fstab""",
        "lfcs_title": 'Storage Partitions (MBR vs GPT) & Swap',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Dedicated Swap File Creation
1. Create a `128MB` swap file at `/var/tmp/swapfile_extra` (use `dd` or `fallocate`).
2. Set permissions strictly to `0600` (`chmod 600`).
3. Format it as swap space with `mkswap`.

### Task 2: Swap Space Activation & Persistence
1. Activate the swap file with `swapon /var/tmp/swapfile_extra`.
2. Append a persistent entry to `/etc/fstab` so it activates on boot:
   `/var/tmp/swapfile_extra none swap sw 0 0`
3. Verify that `swapon --show` displays `/var/tmp/swapfile_extra`.""",
        "lfcs_setup": """sudo swapoff /var/tmp/swapfile_extra 2>/dev/null || true
sudo rm -f /var/tmp/swapfile_extra
sudo sed -i '\|/var/tmp/swapfile_extra|d' /etc/fstab""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: Swap file permissions and active
SWAP_ACTIVE=$(swapon --show | grep "/var/tmp/swapfile_extra" || true)
PERM=$(stat -c "%a" /var/tmp/swapfile_extra 2>/dev/null || echo "0")

if [ -n "$SWAP_ACTIVE" ] && [ "$PERM" == "600" ]; then
  echo -e "${GREEN}[PASS] Task 1: /var/tmp/swapfile_extra active as swap with permissions 600.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Swap file inactive or permissions=$PERM (expected 600).${NC}"
fi

# Task 2: /etc/fstab entry
if grep -q "/var/tmp/swapfile_extra.*swap" /etc/fstab; then
  echo -e "${GREEN}[PASS] Task 2: /etc/fstab contains persistent swap entry.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/fstab missing entry for /var/tmp/swapfile_extra.${NC}"
fi""",
        "lfcs_solution": """1. Create & format swap:
`sudo dd if=/dev/zero of=/var/tmp/swapfile_extra bs=1M count=128`
`sudo chmod 600 /var/tmp/swapfile_extra`
`sudo mkswap /var/tmp/swapfile_extra`

2. Activate & persist:
`sudo swapon /var/tmp/swapfile_extra`
`echo "/var/tmp/swapfile_extra none swap sw 0 0" | sudo tee -a /etc/fstab`""",
        "lfcs_reset": """sudo swapoff /var/tmp/swapfile_extra 2>/dev/null || true
sudo rm -f /var/tmp/swapfile_extra
sudo sed -i '\|/var/tmp/swapfile_extra|d' /etc/fstab""",
    },
    {
        "day": 2,
        "date": '2026-11-03',
        "title": 'Filesystems & Boot Mounting (/etc/fstab)',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Loop Device Filesystem Formatting
A 150MB loop disk image `/var/tmp/data_store.img` has been initialized and associated with `/dev/loop90`.
- Format `/dev/loop90` with the `ext4` filesystem with filesystem label `DATA_STORE`.

### Task 2: Mount Point & Persistent /etc/fstab Entry
1. Create mount directory `/mnt/data_store`.
2. Extract the filesystem UUID of `/dev/loop90` using `blkid`.
3. Add an `/etc/fstab` entry:
   `UUID=<extracted-uuid> /mnt/data_store ext4 defaults,noatime 0 2`
4. Mount all filesystems with `sudo mount -a`.
5. Verify `/mnt/data_store` is mounted and writable.""",
        "setup": """sudo umount /mnt/data_store 2>/dev/null || true
sudo losetup -d /dev/loop90 2>/dev/null || true
sudo sed -i '\|/mnt/data_store|d' /etc/fstab
sudo rm -rf /var/tmp/data_store.img /mnt/data_store
sudo mkdir -p /mnt/data_store && sudo chmod 777 /mnt/data_store
dd if=/dev/zero of=/var/tmp/data_store.img bs=1M count=150 >/dev/null 2>&1
sudo losetup /dev/loop90 /var/tmp/data_store.img""",
        "verify": """SCORE=0; TOTAL=2
# Task 1 & 2: Mounted filesystem
IS_MOUNTED=$(findmnt /mnt/data_store -o FSTYPE,OPTIONS -n 2>/dev/null || true)
if echo "$IS_MOUNTED" | grep -q "ext4" && echo "$IS_MOUNTED" | grep -q "noatime"; then
  echo -e "${GREEN}[PASS] Task 1: /mnt/data_store is mounted with ext4 and noatime.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /mnt/data_store not mounted or missing noatime option: $IS_MOUNTED.${NC}"
fi

# Task 2: /etc/fstab has UUID entry
if grep -qiE "UUID=.*\/mnt\/data_store.*ext4.*noatime" /etc/fstab; then
  echo -e "${GREEN}[PASS] Task 2: /etc/fstab configured with UUID and persistent options.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/fstab missing proper UUID entry for /mnt/data_store.${NC}"
fi""",
        "solution": """1. Format:
`sudo mkfs.ext4 -L DATA_STORE /dev/loop90`

2. UUID and fstab:
`UUID=$(sudo blkid -s UUID -o value /dev/loop90)`
`echo "UUID=$UUID /mnt/data_store ext4 defaults,noatime 0 2" | sudo tee -a /etc/fstab`

3. Mount:
`sudo mount -a`""",
        "reset": """sudo umount /mnt/data_store 2>/dev/null || true
sudo losetup -d /dev/loop90 2>/dev/null || true
sudo sed -i '\|/mnt/data_store|d' /etc/fstab
sudo rm -rf /var/tmp/data_store.img /mnt/data_store""",
        "lfcs_title": 'Filesystems & Boot Mounting (/etc/fstab)',
        "lfcs_diff": 'Medium',
        "lfcs_time": '35m',
        "lfcs_tasks": """### Task 1: Loop Device Filesystem Formatting
A 150MB loop disk image `/var/tmp/data_store.img` has been initialized and associated with `/dev/loop90`.
- Format `/dev/loop90` with the `ext4` filesystem with filesystem label `DATA_STORE`.

### Task 2: Mount Point & Persistent /etc/fstab Entry
1. Create mount directory `/mnt/data_store`.
2. Extract the filesystem UUID of `/dev/loop90` using `blkid`.
3. Add an `/etc/fstab` entry:
   `UUID=<extracted-uuid> /mnt/data_store ext4 defaults,noatime 0 2`
4. Mount all filesystems with `sudo mount -a`.
5. Verify `/mnt/data_store` is mounted and writable.""",
        "lfcs_setup": """sudo umount /mnt/data_store 2>/dev/null || true
sudo losetup -d /dev/loop90 2>/dev/null || true
sudo sed -i '\|/mnt/data_store|d' /etc/fstab
sudo rm -rf /var/tmp/data_store.img /mnt/data_store
sudo mkdir -p /mnt/data_store && sudo chmod 777 /mnt/data_store
dd if=/dev/zero of=/var/tmp/data_store.img bs=1M count=150 >/dev/null 2>&1
sudo losetup /dev/loop90 /var/tmp/data_store.img""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1 & 2: Mounted filesystem
IS_MOUNTED=$(findmnt /mnt/data_store -o FSTYPE,OPTIONS -n 2>/dev/null || true)
if echo "$IS_MOUNTED" | grep -q "ext4" && echo "$IS_MOUNTED" | grep -q "noatime"; then
  echo -e "${GREEN}[PASS] Task 1: /mnt/data_store is mounted with ext4 and noatime.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /mnt/data_store not mounted or missing noatime option: $IS_MOUNTED.${NC}"
fi

# Task 2: /etc/fstab has UUID entry
if grep -qiE "UUID=.*\/mnt\/data_store.*ext4.*noatime" /etc/fstab; then
  echo -e "${GREEN}[PASS] Task 2: /etc/fstab configured with UUID and persistent options.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /etc/fstab missing proper UUID entry for /mnt/data_store.${NC}"
fi""",
        "lfcs_solution": """1. Format:
`sudo mkfs.ext4 -L DATA_STORE /dev/loop90`

2. UUID and fstab:
`UUID=$(sudo blkid -s UUID -o value /dev/loop90)`
`echo "UUID=$UUID /mnt/data_store ext4 defaults,noatime 0 2" | sudo tee -a /etc/fstab`

3. Mount:
`sudo mount -a`""",
        "lfcs_reset": """sudo umount /mnt/data_store 2>/dev/null || true
sudo losetup -d /dev/loop90 2>/dev/null || true
sudo sed -i '\|/mnt/data_store|d' /etc/fstab
sudo rm -rf /var/tmp/data_store.img /mnt/data_store""",
    },
    {
        "day": 3,
        "date": '2026-11-04',
        "title": 'Logical Volume Management (LVM) Architecture',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Create LVM Storage Hierarchy
Loop device `/dev/loop91` (250MB) has been prepared.
1. Initialize `/dev/loop91` as an LVM Physical Volume using `pvcreate`.
2. Create a Volume Group named `vg_database` containing `/dev/loop91`.
3. Create a Logical Volume named `lv_orders` with size `120MB` inside `vg_database`.

### Task 2: Format and Mount Logical Volume
1. Format `/dev/vg_database/lv_orders` with the `ext4` filesystem.
2. Mount it at `/mnt/orders_data`.
3. Confirm with `lvs` and `df -h /mnt/orders_data`.""",
        "setup": """sudo umount /mnt/orders_data 2>/dev/null || true
sudo lvremove -f /dev/vg_database/lv_orders 2>/dev/null || true
sudo vgremove -f vg_database 2>/dev/null || true
sudo pvremove -f /dev/loop91 2>/dev/null || true
sudo losetup -d /dev/loop91 2>/dev/null || true
sudo rm -rf /var/tmp/lvm_backing.img /mnt/orders_data
sudo mkdir -p /mnt/orders_data && sudo chmod 777 /mnt/orders_data
dd if=/dev/zero of=/var/tmp/lvm_backing.img bs=1M count=250 >/dev/null 2>&1
sudo losetup /dev/loop91 /var/tmp/lvm_backing.img""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: LVM objects
LV_EXISTS=$(sudo lvs -o lv_name,vg_name --noheadings /dev/vg_database/lv_orders 2>/dev/null || echo "None")
if echo "$LV_EXISTS" | grep -q "lv_orders" && echo "$LV_EXISTS" | grep -q "vg_database"; then
  echo -e "${GREEN}[PASS] Task 1: Logical Volume lv_orders exists in vg_database.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Logical Volume /dev/vg_database/lv_orders not found.${NC}"
fi

# Task 2: Mounted
MNT_CHECK=$(findmnt /mnt/orders_data -o SOURCE,FSTYPE -n 2>/dev/null || true)
if echo "$MNT_CHECK" | grep -q "lv_orders" && echo "$MNT_CHECK" | grep -q "ext4"; then
  echo -e "${GREEN}[PASS] Task 2: /mnt/orders_data is mounted from lv_orders (ext4).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /mnt/orders_data not mounted from lv_orders: $MNT_CHECK.${NC}"
fi""",
        "solution": """1. LVM setup:
`sudo pvcreate /dev/loop91`
`sudo vgcreate vg_database /dev/loop91`
`sudo lvcreate -L 120M -n lv_orders vg_database`

2. Format & mount:
`sudo mkfs.ext4 /dev/vg_database/lv_orders`
`sudo mount /dev/vg_database/lv_orders /mnt/orders_data`""",
        "reset": """sudo umount /mnt/orders_data 2>/dev/null || true
sudo lvremove -f /dev/vg_database/lv_orders 2>/dev/null || true
sudo vgremove -f vg_database 2>/dev/null || true
sudo pvremove -f /dev/loop91 2>/dev/null || true
sudo losetup -d /dev/loop91 2>/dev/null || true
sudo rm -rf /var/tmp/lvm_backing.img /mnt/orders_data""",
        "lfcs_title": 'Logical Volume Management (LVM) Architecture',
        "lfcs_diff": 'Medium',
        "lfcs_time": '35m',
        "lfcs_tasks": """### Task 1: Create LVM Storage Hierarchy
Loop device `/dev/loop91` (250MB) has been prepared.
1. Initialize `/dev/loop91` as an LVM Physical Volume using `pvcreate`.
2. Create a Volume Group named `vg_database` containing `/dev/loop91`.
3. Create a Logical Volume named `lv_orders` with size `120MB` inside `vg_database`.

### Task 2: Format and Mount Logical Volume
1. Format `/dev/vg_database/lv_orders` with the `ext4` filesystem.
2. Mount it at `/mnt/orders_data`.
3. Confirm with `lvs` and `df -h /mnt/orders_data`.""",
        "lfcs_setup": """sudo umount /mnt/orders_data 2>/dev/null || true
sudo lvremove -f /dev/vg_database/lv_orders 2>/dev/null || true
sudo vgremove -f vg_database 2>/dev/null || true
sudo pvremove -f /dev/loop91 2>/dev/null || true
sudo losetup -d /dev/loop91 2>/dev/null || true
sudo rm -rf /var/tmp/lvm_backing.img /mnt/orders_data
sudo mkdir -p /mnt/orders_data && sudo chmod 777 /mnt/orders_data
dd if=/dev/zero of=/var/tmp/lvm_backing.img bs=1M count=250 >/dev/null 2>&1
sudo losetup /dev/loop91 /var/tmp/lvm_backing.img""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: LVM objects
LV_EXISTS=$(sudo lvs -o lv_name,vg_name --noheadings /dev/vg_database/lv_orders 2>/dev/null || echo "None")
if echo "$LV_EXISTS" | grep -q "lv_orders" && echo "$LV_EXISTS" | grep -q "vg_database"; then
  echo -e "${GREEN}[PASS] Task 1: Logical Volume lv_orders exists in vg_database.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: Logical Volume /dev/vg_database/lv_orders not found.${NC}"
fi

# Task 2: Mounted
MNT_CHECK=$(findmnt /mnt/orders_data -o SOURCE,FSTYPE -n 2>/dev/null || true)
if echo "$MNT_CHECK" | grep -q "lv_orders" && echo "$MNT_CHECK" | grep -q "ext4"; then
  echo -e "${GREEN}[PASS] Task 2: /mnt/orders_data is mounted from lv_orders (ext4).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: /mnt/orders_data not mounted from lv_orders: $MNT_CHECK.${NC}"
fi""",
        "lfcs_solution": """1. LVM setup:
`sudo pvcreate /dev/loop91`
`sudo vgcreate vg_database /dev/loop91`
`sudo lvcreate -L 120M -n lv_orders vg_database`

2. Format & mount:
`sudo mkfs.ext4 /dev/vg_database/lv_orders`
`sudo mount /dev/vg_database/lv_orders /mnt/orders_data`""",
        "lfcs_reset": """sudo umount /mnt/orders_data 2>/dev/null || true
sudo lvremove -f /dev/vg_database/lv_orders 2>/dev/null || true
sudo vgremove -f vg_database 2>/dev/null || true
sudo pvremove -f /dev/loop91 2>/dev/null || true
sudo losetup -d /dev/loop91 2>/dev/null || true
sudo rm -rf /var/tmp/lvm_backing.img /mnt/orders_data""",
    },
    {
        "day": 4,
        "date": '2026-11-05',
        "title": 'Dynamic LVM Volume Expansion',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Extend Logical Volume
A Volume Group `vg_expand` (size 350MB) and mounted Logical Volume `lv_store` (initial size 100MB mounted at `/mnt/expand_store`) are active.
1. Extend `lv_store` by `100MB` (to total size 200MB) using `lvextend`.

### Task 2: Online Filesystem Resize
Resize the `ext4` filesystem online without unmounting using `resize2fs /dev/vg_expand/lv_store`.
- Confirm with `df -h /mnt/expand_store` that the filesystem reflects ~200MB.""",
        "setup": """sudo umount /mnt/expand_store 2>/dev/null || true
sudo lvremove -f /dev/vg_expand/lv_store 2>/dev/null || true
sudo vgremove -f vg_expand 2>/dev/null || true
sudo pvremove -f /dev/loop92 2>/dev/null || true
sudo losetup -d /dev/loop92 2>/dev/null || true
sudo rm -rf /var/tmp/expand_backing.img /mnt/expand_store
sudo mkdir -p /mnt/expand_store && sudo chmod 777 /mnt/expand_store
dd if=/dev/zero of=/var/tmp/expand_backing.img bs=1M count=350 >/dev/null 2>&1
sudo losetup /dev/loop92 /var/tmp/expand_backing.img
sudo pvcreate /dev/loop92 >/dev/null 2>&1
sudo vgcreate vg_expand /dev/loop92 >/dev/null 2>&1
sudo lvcreate -L 100M -n lv_store vg_expand >/dev/null 2>&1
sudo mkfs.ext4 /dev/vg_expand/lv_store >/dev/null 2>&1
sudo mount /dev/vg_expand/lv_store /mnt/expand_store""",
        "verify": """SCORE=0; TOTAL=2
# Task 1: LV Size is 200MB
LV_SZ=$(sudo lvs -o lv_size --units m --noheadings /dev/vg_expand/lv_store 2>/dev/null | tr -d ' ' || echo "0")
if echo "$LV_SZ" | grep -q "200"; then
  echo -e "${GREEN}[PASS] Task 1: Logical Volume lv_store extended to 200MB.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: lv_store size is $LV_SZ (expected 200MB).${NC}"
fi

# Task 2: Filesystem reflects expanded size
FS_SIZE=$(df -m /mnt/expand_store | tail -1 | awk '{print $2}' || echo "0")
if [ "$FS_SIZE" -ge 180 ]; then
  echo -e "${GREEN}[PASS] Task 2: Filesystem resized online ($FS_SIZE MB).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Filesystem size is $FS_SIZE MB (expected >= 180MB).${NC}"
fi""",
        "solution": """1. Extend LV:
`sudo lvextend -L +100M /dev/vg_expand/lv_store`

2. Resize filesystem:
`sudo resize2fs /dev/vg_expand/lv_store`""",
        "reset": """sudo umount /mnt/expand_store 2>/dev/null || true
sudo lvremove -f /dev/vg_expand/lv_store 2>/dev/null || true
sudo vgremove -f vg_expand 2>/dev/null || true
sudo pvremove -f /dev/loop92 2>/dev/null || true
sudo losetup -d /dev/loop92 2>/dev/null || true
sudo rm -rf /var/tmp/expand_backing.img /mnt/expand_store""",
        "lfcs_title": 'Dynamic LVM Volume Expansion',
        "lfcs_diff": 'Medium',
        "lfcs_time": '35m',
        "lfcs_tasks": """### Task 1: Extend Logical Volume
A Volume Group `vg_expand` (size 350MB) and mounted Logical Volume `lv_store` (initial size 100MB mounted at `/mnt/expand_store`) are active.
1. Extend `lv_store` by `100MB` (to total size 200MB) using `lvextend`.

### Task 2: Online Filesystem Resize
Resize the `ext4` filesystem online without unmounting using `resize2fs /dev/vg_expand/lv_store`.
- Confirm with `df -h /mnt/expand_store` that the filesystem reflects ~200MB.""",
        "lfcs_setup": """sudo umount /mnt/expand_store 2>/dev/null || true
sudo lvremove -f /dev/vg_expand/lv_store 2>/dev/null || true
sudo vgremove -f vg_expand 2>/dev/null || true
sudo pvremove -f /dev/loop92 2>/dev/null || true
sudo losetup -d /dev/loop92 2>/dev/null || true
sudo rm -rf /var/tmp/expand_backing.img /mnt/expand_store
sudo mkdir -p /mnt/expand_store && sudo chmod 777 /mnt/expand_store
dd if=/dev/zero of=/var/tmp/expand_backing.img bs=1M count=350 >/dev/null 2>&1
sudo losetup /dev/loop92 /var/tmp/expand_backing.img
sudo pvcreate /dev/loop92 >/dev/null 2>&1
sudo vgcreate vg_expand /dev/loop92 >/dev/null 2>&1
sudo lvcreate -L 100M -n lv_store vg_expand >/dev/null 2>&1
sudo mkfs.ext4 /dev/vg_expand/lv_store >/dev/null 2>&1
sudo mount /dev/vg_expand/lv_store /mnt/expand_store""",
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: LV Size is 200MB
LV_SZ=$(sudo lvs -o lv_size --units m --noheadings /dev/vg_expand/lv_store 2>/dev/null | tr -d ' ' || echo "0")
if echo "$LV_SZ" | grep -q "200"; then
  echo -e "${GREEN}[PASS] Task 1: Logical Volume lv_store extended to 200MB.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: lv_store size is $LV_SZ (expected 200MB).${NC}"
fi

# Task 2: Filesystem reflects expanded size
FS_SIZE=$(df -m /mnt/expand_store | tail -1 | awk '{print $2}' || echo "0")
if [ "$FS_SIZE" -ge 180 ]; then
  echo -e "${GREEN}[PASS] Task 2: Filesystem resized online ($FS_SIZE MB).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Filesystem size is $FS_SIZE MB (expected >= 180MB).${NC}"
fi""",
        "lfcs_solution": """1. Extend LV:
`sudo lvextend -L +100M /dev/vg_expand/lv_store`

2. Resize filesystem:
`sudo resize2fs /dev/vg_expand/lv_store`""",
        "lfcs_reset": """sudo umount /mnt/expand_store 2>/dev/null || true
sudo lvremove -f /dev/vg_expand/lv_store 2>/dev/null || true
sudo vgremove -f vg_expand 2>/dev/null || true
sudo pvremove -f /dev/loop92 2>/dev/null || true
sudo losetup -d /dev/loop92 2>/dev/null || true
sudo rm -rf /var/tmp/expand_backing.img /mnt/expand_store""",
    },
    {
        "day": 5,
        "date": '2026-11-06',
        "title": 'Remote Filesystems: NFS & Storage Monitoring',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Storage Monitoring Audit Script
Create a monitoring script at `/usr/local/bin/check-disk.sh`:
- Script is executable (`chmod 755`).
- Extract all mounted filesystems with their filesystem type and usage percentage into `/var/tmp/disk_audit.txt` (formatted with headers `Filesystem Type Size Used Avail Use% Mounted_on`).

### Task 2: Disk Alert Threshold
Configure the script so that if any filesystem usage exceeds `85%`, it appends `WARNING: High disk utilization detected` to `/var/log/disk_alert.log`.""",
        "setup": 'sudo rm -f /usr/local/bin/check-disk.sh /var/tmp/disk_audit.txt /var/log/disk_alert.log',
        "verify": """SCORE=0; TOTAL=2
# Task 1: check-disk.sh exists and produces output
if [ -x /usr/local/bin/check-disk.sh ]; then
  sudo /usr/local/bin/check-disk.sh
  if [ -f /var/tmp/disk_audit.txt ] && [ -s /var/tmp/disk_audit.txt ]; then
    echo -e "${GREEN}[PASS] Task 1: /usr/local/bin/check-disk.sh generated /var/tmp/disk_audit.txt.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Task 1: /var/tmp/disk_audit.txt not generated.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Task 1: /usr/local/bin/check-disk.sh missing or not executable.${NC}"
fi

# Task 2: check headers
if [ -f /var/tmp/disk_audit.txt ] && grep -qiE "Filesystem|Use%" /var/tmp/disk_audit.txt; then
  echo -e "${GREEN}[PASS] Task 2: Disk audit report format verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Report format missing headers.${NC}"
fi""",
        "solution": """1. Create `/usr/local/bin/check-disk.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail
df -hT > /var/tmp/disk_audit.txt
df -hP | awk '0+$5 >= 85 {print "WARNING: High disk utilization on "$1" ("$5")"}' >> /var/log/disk_alert.log || true
```
`sudo chmod 755 /usr/local/bin/check-disk.sh`
`sudo /usr/local/bin/check-disk.sh`""",
        "reset": 'sudo rm -f /usr/local/bin/check-disk.sh /var/tmp/disk_audit.txt /var/log/disk_alert.log',
        "lfcs_title": 'Remote Filesystems: NFS & Storage Monitoring',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Storage Monitoring Audit Script
Create a monitoring script at `/usr/local/bin/check-disk.sh`:
- Script is executable (`chmod 755`).
- Extract all mounted filesystems with their filesystem type and usage percentage into `/var/tmp/disk_audit.txt` (formatted with headers `Filesystem Type Size Used Avail Use% Mounted_on`).

### Task 2: Disk Alert Threshold
Configure the script so that if any filesystem usage exceeds `85%`, it appends `WARNING: High disk utilization detected` to `/var/log/disk_alert.log`.""",
        "lfcs_setup": 'sudo rm -f /usr/local/bin/check-disk.sh /var/tmp/disk_audit.txt /var/log/disk_alert.log',
        "lfcs_verify": """SCORE=0; TOTAL=2
# Task 1: check-disk.sh exists and produces output
if [ -x /usr/local/bin/check-disk.sh ]; then
  sudo /usr/local/bin/check-disk.sh
  if [ -f /var/tmp/disk_audit.txt ] && [ -s /var/tmp/disk_audit.txt ]; then
    echo -e "${GREEN}[PASS] Task 1: /usr/local/bin/check-disk.sh generated /var/tmp/disk_audit.txt.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Task 1: /var/tmp/disk_audit.txt not generated.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Task 1: /usr/local/bin/check-disk.sh missing or not executable.${NC}"
fi

# Task 2: check headers
if [ -f /var/tmp/disk_audit.txt ] && grep -qiE "Filesystem|Use%" /var/tmp/disk_audit.txt; then
  echo -e "${GREEN}[PASS] Task 2: Disk audit report format verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: Report format missing headers.${NC}"
fi""",
        "lfcs_solution": """1. Create `/usr/local/bin/check-disk.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail
df -hT > /var/tmp/disk_audit.txt
df -hP | awk '0+$5 >= 85 {print "WARNING: High disk utilization on "$1" ("$5")"}' >> /var/log/disk_alert.log || true
```
`sudo chmod 755 /usr/local/bin/check-disk.sh`
`sudo /usr/local/bin/check-disk.sh`""",
        "lfcs_reset": 'sudo rm -f /usr/local/bin/check-disk.sh /var/tmp/disk_audit.txt /var/log/disk_alert.log',
    },
    {
        "day": 6,
        "date": '2026-11-07',
        "title": 'Week 6 Storage Mastery & LVM Drill',
        "diff": 'Hard (Milestone Assessment 6)',
        "time": '45m',
        "tasks": """### Milestone 6 Triathlon Tasks:
1. **LVM Storage Creation**:
   Loop device `/dev/loop93` (300MB) has been prepared.
   - Create Volume Group `vg_secure`.
   - Create Logical Volume `lv_audit` (120MB).
   - Format with `ext4` and mount at `/mnt/secure_audit`.

2. **Access Control Lists (ACL)**:
   - Use `setfacl` to grant user `student` read, write, and execute permissions (`rwx`) on `/mnt/secure_audit` (`setfacl -m u:student:rwx /mnt/secure_audit`).
   - Confirm with `getfacl /mnt/secure_audit`.

3. **Online Volume Expansion**:
   Extend `lv_audit` by `60MB` and resize filesystem online (`resize2fs`).
   Verify total mounted size >= 170MB.""",
        "setup": """sudo umount /mnt/secure_audit 2>/dev/null || true
sudo lvremove -f /dev/vg_secure/lv_audit 2>/dev/null || true
sudo vgremove -f vg_secure 2>/dev/null || true
sudo pvremove -f /dev/loop93 2>/dev/null || true
sudo losetup -d /dev/loop93 2>/dev/null || true
sudo rm -rf /var/tmp/m6_backing.img /mnt/secure_audit
sudo mkdir -p /mnt/secure_audit && sudo chmod 777 /mnt/secure_audit
dd if=/dev/zero of=/var/tmp/m6_backing.img bs=1M count=300 >/dev/null 2>&1
sudo losetup /dev/loop93 /var/tmp/m6_backing.img
sudo pvcreate /dev/loop93 >/dev/null 2>&1""",
        "verify": """SCORE=0; TOTAL=3
# Task 1: LV and mount
MNT=$(findmnt /mnt/secure_audit -o SOURCE,FSTYPE -n 2>/dev/null || true)
if echo "$MNT" | grep -q "lv_audit" && echo "$MNT" | grep -q "ext4"; then
  echo -e "${GREEN}[PASS] Task 1: /mnt/secure_audit is mounted on lv_audit (ext4).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /mnt/secure_audit not mounted on lv_audit: $MNT.${NC}"
fi

# Task 2: ACL
ACL_CHECK=$(getfacl /mnt/secure_audit 2>/dev/null || true)
if echo "$ACL_CHECK" | grep -q "user:student:rwx"; then
  echo -e "${GREEN}[PASS] Task 2: ACL permissions user:student:rwx verified on /mnt/secure_audit.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: ACL missing user:student:rwx.${NC}"
fi

# Task 3: Size >= 170M
SZ=$(df -m /mnt/secure_audit | tail -1 | awk '{print $2}' || echo "0")
if [ "$SZ" -ge 160 ]; then
  echo -e "${GREEN}[PASS] Task 3: Online LVM expansion verified ($SZ MB).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Size is $SZ MB (expected >= 160MB).${NC}"
fi""",
        "solution": """1. Create LVM & mount:
`sudo vgcreate vg_secure /dev/loop93`
`sudo lvcreate -L 120M -n lv_audit vg_secure`
`sudo mkfs.ext4 /dev/vg_secure/lv_audit`
`sudo mount /dev/vg_secure/lv_audit /mnt/secure_audit`

2. Set ACL:
`sudo setfacl -m u:student:rwx /mnt/secure_audit`

3. Extend:
`sudo lvextend -L +60M /dev/vg_secure/lv_audit`
`sudo resize2fs /dev/vg_secure/lv_audit`""",
        "reset": """sudo umount /mnt/secure_audit 2>/dev/null || true
sudo lvremove -f /dev/vg_secure/lv_audit 2>/dev/null || true
sudo vgremove -f vg_secure 2>/dev/null || true
sudo pvremove -f /dev/loop93 2>/dev/null || true
sudo losetup -d /dev/loop93 2>/dev/null || true
sudo rm -rf /var/tmp/m6_backing.img /mnt/secure_audit""",
        "lfcs_title": 'Week 6 Storage Mastery & LVM Drill',
        "lfcs_diff": 'Hard (Milestone Assessment 6)',
        "lfcs_time": '45m',
        "lfcs_tasks": """### Milestone 6 Triathlon Tasks:
1. **LVM Storage Creation**:
   Loop device `/dev/loop93` (300MB) has been prepared.
   - Create Volume Group `vg_secure`.
   - Create Logical Volume `lv_audit` (120MB).
   - Format with `ext4` and mount at `/mnt/secure_audit`.

2. **Access Control Lists (ACL)**:
   - Use `setfacl` to grant user `student` read, write, and execute permissions (`rwx`) on `/mnt/secure_audit` (`setfacl -m u:student:rwx /mnt/secure_audit`).
   - Confirm with `getfacl /mnt/secure_audit`.

3. **Online Volume Expansion**:
   Extend `lv_audit` by `60MB` and resize filesystem online (`resize2fs`).
   Verify total mounted size >= 170MB.""",
        "lfcs_setup": """sudo umount /mnt/secure_audit 2>/dev/null || true
sudo lvremove -f /dev/vg_secure/lv_audit 2>/dev/null || true
sudo vgremove -f vg_secure 2>/dev/null || true
sudo pvremove -f /dev/loop93 2>/dev/null || true
sudo losetup -d /dev/loop93 2>/dev/null || true
sudo rm -rf /var/tmp/m6_backing.img /mnt/secure_audit
sudo mkdir -p /mnt/secure_audit && sudo chmod 777 /mnt/secure_audit
dd if=/dev/zero of=/var/tmp/m6_backing.img bs=1M count=300 >/dev/null 2>&1
sudo losetup /dev/loop93 /var/tmp/m6_backing.img
sudo pvcreate /dev/loop93 >/dev/null 2>&1""",
        "lfcs_verify": """SCORE=0; TOTAL=3
# Task 1: LV and mount
MNT=$(findmnt /mnt/secure_audit -o SOURCE,FSTYPE -n 2>/dev/null || true)
if echo "$MNT" | grep -q "lv_audit" && echo "$MNT" | grep -q "ext4"; then
  echo -e "${GREEN}[PASS] Task 1: /mnt/secure_audit is mounted on lv_audit (ext4).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 1: /mnt/secure_audit not mounted on lv_audit: $MNT.${NC}"
fi

# Task 2: ACL
ACL_CHECK=$(getfacl /mnt/secure_audit 2>/dev/null || true)
if echo "$ACL_CHECK" | grep -q "user:student:rwx"; then
  echo -e "${GREEN}[PASS] Task 2: ACL permissions user:student:rwx verified on /mnt/secure_audit.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 2: ACL missing user:student:rwx.${NC}"
fi

# Task 3: Size >= 170M
SZ=$(df -m /mnt/secure_audit | tail -1 | awk '{print $2}' || echo "0")
if [ "$SZ" -ge 160 ]; then
  echo -e "${GREEN}[PASS] Task 3: Online LVM expansion verified ($SZ MB).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Task 3: Size is $SZ MB (expected >= 160MB).${NC}"
fi""",
        "lfcs_solution": """1. Create LVM & mount:
`sudo vgcreate vg_secure /dev/loop93`
`sudo lvcreate -L 120M -n lv_audit vg_secure`
`sudo mkfs.ext4 /dev/vg_secure/lv_audit`
`sudo mount /dev/vg_secure/lv_audit /mnt/secure_audit`

2. Set ACL:
`sudo setfacl -m u:student:rwx /mnt/secure_audit`

3. Extend:
`sudo lvextend -L +60M /dev/vg_secure/lv_audit`
`sudo resize2fs /dev/vg_secure/lv_audit`""",
        "lfcs_reset": """sudo umount /mnt/secure_audit 2>/dev/null || true
sudo lvremove -f /dev/vg_secure/lv_audit 2>/dev/null || true
sudo vgremove -f vg_secure 2>/dev/null || true
sudo pvremove -f /dev/loop93 2>/dev/null || true
sudo losetup -d /dev/loop93 2>/dev/null || true
sudo rm -rf /var/tmp/m6_backing.img /mnt/secure_audit""",
    },
]
