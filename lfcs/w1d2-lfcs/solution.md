# [LFCS W1D2-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Fix relative symlink:
```bash
sudo ln -sfn ../storage/v2/app-v2.conf /opt/link-lab/configs/active.conf
```

2. Create hard link:
```bash
sudo ln /opt/link-lab/storage/v2/app-v2.conf /opt/link-lab/backup/app-v2.conf.hl
echo "BACKUP_ENABLED=true" | sudo tee -a /opt/link-lab/backup/app-v2.conf.hl
```

3. Find and remove broken symlinks:
```bash
find /opt/link-lab/orphan_links -xtype l | sudo tee /var/tmp/removed_links.txt
cat /var/tmp/removed_links.txt | xargs -r sudo rm -f
```
