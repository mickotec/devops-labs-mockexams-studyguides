# [LFCS W1D6-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Directory permissions:
```bash
sudo groupadd -f sysadmins
sudo groupadd -f contractors
sudo mkdir -p /srv/secure_vault/incoming /srv/secure_vault/configs /srv/secure_vault/storage
sudo touch /srv/secure_vault/storage/vault.conf
sudo chown root:sysadmins /srv/secure_vault
sudo chmod 2770 /srv/secure_vault
sudo chown root:contractors /srv/secure_vault/incoming
sudo chmod 1775 /srv/secure_vault/incoming
```

2. SUID audit:
```bash
sudo find /opt/binaries -type f \( -perm -4000 -o -perm -2000 \) > /var/tmp/suid_audit.txt
```

3. Relative symlink:
```bash
sudo ln -sf ../storage/vault.conf /srv/secure_vault/configs/current.conf
```

4. Archive:
```bash
sudo tar -czpf /var/backups/vault_initial.tar.gz -C /srv secure_vault
```
