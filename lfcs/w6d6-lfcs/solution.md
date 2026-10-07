# [LFCS W6D6-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create LVM & mount:
`sudo vgcreate vg_secure /dev/loop93`
`sudo lvcreate -L 120M -n lv_audit vg_secure`
`sudo mkfs.ext4 /dev/vg_secure/lv_audit`
`sudo mount /dev/vg_secure/lv_audit /mnt/secure_audit`

2. Set ACL:
`sudo setfacl -m u:student:rwx /mnt/secure_audit`

3. Extend:
`sudo lvextend -L +60M /dev/vg_secure/lv_audit`
`sudo resize2fs /dev/vg_secure/lv_audit`
