# [LFCS W8D6-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Storage audit:
`df -hT / | sudo tee /var/log/storage_audit.log >/dev/null`

2. Service security audit:
```bash
FAILED=$(systemctl --failed --no-legend)
if [ -z "$FAILED" ]; then
  echo "ALL_SERVICES_OPERATIONAL" | sudo tee /var/log/security_audit.log >/dev/null
else
  echo "$FAILED" | sudo tee /var/log/security_audit.log >/dev/null
fi
```

3. Backup script:
```bash
sudo bash -c 'cat << "EOF" > /usr/local/bin/system_backup.sh
#!/usr/bin/env bash
mkdir -p /var/backups
tar -czf /var/backups/etc_backup_audit.tar.gz /etc/systemd /etc/default 2>/dev/null
EOF'
sudo chmod +x /usr/local/bin/system_backup.sh
sudo /usr/local/bin/system_backup.sh
```

4. SSH permissions:
```bash
chmod 700 /home/student/.ssh
chmod 600 /home/student/.ssh/authorized_keys
chown -R student:student /home/student/.ssh
```
