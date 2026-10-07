# [LFCS W2D6-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Init repo:
```bash
sudo mkdir -p /srv/repo
sudo chown -R $(whoami):$(whoami) /srv/repo
cd /srv/repo
git init -b main
git config user.name "Student"
git config user.email "student@example.com"
echo "config=v1" > system.conf
git add system.conf
git commit -m "initial commit"
```

2. Branch and merge:
```bash
git checkout -b feature-audit
echo "config=v2" > system.conf
git commit -am "feat: update v2"
git checkout main
git merge feature-audit
```

3. Tarball backup:
```bash
sudo mkdir -p /var/backups
sudo tar -czf /var/backups/repo.tar.gz -C /srv repo
```
