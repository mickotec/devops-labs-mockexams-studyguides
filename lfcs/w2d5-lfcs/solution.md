# [LFCS W2D5-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create archive:
```bash
sudo tar -czpf /var/tmp/systemd_backup.tar.gz /etc/systemd
```

2. Extract to destination:
```bash
mkdir -p /var/tmp/extracted_systemd
sudo tar -xzf /var/tmp/systemd_backup.tar.gz -C /var/tmp/extracted_systemd
```

3. Manifest:
```bash
tar -tzf /var/tmp/systemd_backup.tar.gz > /var/tmp/archive_manifest.txt
```
