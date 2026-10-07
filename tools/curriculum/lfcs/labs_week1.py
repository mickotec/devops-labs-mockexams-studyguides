"""
Dedicated LFCS Lab Definitions for Week 1 (Days 1 to 6).
"""

WEEK_1_LABS = [
    {
        "day": 1,
        "date": '2026-09-14',
        "title": 'Consoles, Navigation & System Documentation',
        "diff": 'Medium',
        "time": '30m',
        "tasks": """### Task 1: Documentation Discovery & Querying
1. Use `apropos` (or `man -k`) to search for all manual pages discussing:
   - "partition table"
   - "password file"
2. Save the formatted list of matches to `/var/tmp/lfcs-doc-search.txt`.
3. Locate the manual page for the configuration file format of `/etc/passwd` (man section 5). Extract the field definitions and append them to `/var/tmp/lfcs-passwd-fields.txt`.

### Task 2: Advanced Directory Navigation Speed Drills
1. Write a shell function or commands in `/var/tmp/lfcs-nav.sh` demonstrating:
   - Creating a nested directory tree `/var/tmp/lfcs/a/b/c/d/e` in a single command (`mkdir -p`).
   - Pushing the current directory to the directory stack (`pushd`), creating `evidence.txt` inside `/var/tmp/lfcs/a/b/c/d/e/`, and returning with `popd`.
2. Execute the script and ensure `/var/tmp/lfcs/a/b/c/d/e/evidence.txt` exists.

### Task 3: Build a Command Synopsis Extractor (`quickman`)
1. Create an executable bash script `/usr/local/bin/quickman` (permissions `755`):
   - It accepts one argument: the command name (e.g. `quickman tar`).
   - If no argument is passed, exit with code 1 and message: `Usage: quickman <command>`.
   - It extracts and outputs **only** the `NAME` and `SYNOPSIS` sections from the target command's man page without any interactive pager pause (plain text output).
2. Test that running `quickman useradd` prints only the Name and Synopsis cleanly.""",
        "setup": """sudo rm -rf /var/tmp/lfcs*
sudo rm -f /usr/local/bin/quickman""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Documentation extraction files...${NC}"
if [ -f /var/tmp/lfcs-doc-search.txt ] && grep -qiE "fdisk|parted|gdisk" /var/tmp/lfcs-doc-search.txt && grep -qiE "passwd|shadow" /var/tmp/lfcs-doc-search.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/lfcs-doc-search.txt exists and contains expected search matches.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/lfcs-doc-search.txt missing or lacks search results.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Directory navigation tree & evidence...${NC}"
if [ -f /var/tmp/lfcs/a/b/c/d/e/evidence.txt ]; then
  echo -e "${GREEN}[PASS] Nested navigation structure and evidence file verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/lfcs/a/b/c/d/e/evidence.txt not found.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /usr/local/bin/quickman script functionality...${NC}"
if [ -x /usr/local/bin/quickman ]; then
  OUTPUT=$(/usr/local/bin/quickman useradd 2>&1 || true)
  if echo "$OUTPUT" | grep -qi "SYNOPSIS" && echo "$OUTPUT" | grep -qi "NAME"; then
    echo -e "${GREEN}[PASS] /usr/local/bin/quickman successfully extracts NAME and SYNOPSIS non-interactively.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] quickman did not output expected NAME and SYNOPSIS headers.${NC}"
  fi
else
  echo -e "${RED}[FAIL] /usr/local/bin/quickman does not exist or is not executable.${NC}"
fi""",
        "solution": """1. Documentation discovery:
```bash
apropos "partition table" > /var/tmp/lfcs-doc-search.txt
apropos "password file" >> /var/tmp/lfcs-doc-search.txt
man 5 passwd | col -b | head -n 30 > /var/tmp/lfcs-passwd-fields.txt
```

2. Directory navigation:
```bash
mkdir -p /var/tmp/lfcs/a/b/c/d/e
pushd /var/tmp/lfcs/a/b/c/d/e
touch evidence.txt
popd
```

3. Command synopsis extractor:
```bash
sudo tee /usr/local/bin/quickman << 'EOF'
#!/usr/bin/env bash
if [ -z "$1" ]; then
  echo "Usage: quickman <command>"
  exit 1
fi
man "$1" 2>/dev/null | col -b | sed -n '/^NAME/,/^[A-Z]/p' | head -n -1
man "$1" 2>/dev/null | col -b | sed -n '/^SYNOPSIS/,/^[A-Z]/p' | head -n -1
EOF
sudo chmod 755 /usr/local/bin/quickman
```""",
        "reset": """sudo rm -rf /var/tmp/lfcs*
sudo rm -f /usr/local/bin/quickman""",
        "lfcs_title": 'Consoles, Navigation & System Documentation',
        "lfcs_diff": 'Medium',
        "lfcs_time": '30m',
        "lfcs_tasks": """### Task 1: Documentation Discovery & Querying
1. Use `apropos` (or `man -k`) to search for all manual pages discussing:
   - "partition table"
   - "password file"
2. Save the formatted list of matches to `/var/tmp/lfcs-doc-search.txt`.
3. Locate the manual page for the configuration file format of `/etc/passwd` (man section 5). Extract the field definitions and append them to `/var/tmp/lfcs-passwd-fields.txt`.

### Task 2: Advanced Directory Navigation Speed Drills
1. Write a shell function or commands in `/var/tmp/lfcs-nav.sh` demonstrating:
   - Creating a nested directory tree `/var/tmp/lfcs/a/b/c/d/e` in a single command (`mkdir -p`).
   - Pushing the current directory to the directory stack (`pushd`), creating `evidence.txt` inside `/var/tmp/lfcs/a/b/c/d/e/`, and returning with `popd`.
2. Execute the script and ensure `/var/tmp/lfcs/a/b/c/d/e/evidence.txt` exists.

### Task 3: Build a Command Synopsis Extractor (`quickman`)
1. Create an executable bash script `/usr/local/bin/quickman` (permissions `755`):
   - It accepts one argument: the command name (e.g. `quickman tar`).
   - If no argument is passed, exit with code 1 and message: `Usage: quickman <command>`.
   - It extracts and outputs **only** the `NAME` and `SYNOPSIS` sections from the target command's man page without any interactive pager pause (plain text output).
2. Test that running `quickman useradd` prints only the Name and Synopsis cleanly.""",
        "lfcs_setup": """sudo rm -rf /var/tmp/lfcs*
sudo rm -f /usr/local/bin/quickman""",
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Documentation extraction files...${NC}"
if [ -f /var/tmp/lfcs-doc-search.txt ] && grep -qiE "fdisk|parted|gdisk" /var/tmp/lfcs-doc-search.txt && grep -qiE "passwd|shadow" /var/tmp/lfcs-doc-search.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/lfcs-doc-search.txt exists and contains expected search matches.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/lfcs-doc-search.txt missing or lacks search results.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Directory navigation tree & evidence...${NC}"
if [ -f /var/tmp/lfcs/a/b/c/d/e/evidence.txt ]; then
  echo -e "${GREEN}[PASS] Nested navigation structure and evidence file verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/lfcs/a/b/c/d/e/evidence.txt not found.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /usr/local/bin/quickman script functionality...${NC}"
if [ -x /usr/local/bin/quickman ]; then
  OUTPUT=$(/usr/local/bin/quickman useradd 2>&1 || true)
  if echo "$OUTPUT" | grep -qi "SYNOPSIS" && echo "$OUTPUT" | grep -qi "NAME"; then
    echo -e "${GREEN}[PASS] /usr/local/bin/quickman successfully extracts NAME and SYNOPSIS non-interactively.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] quickman did not output expected NAME and SYNOPSIS headers.${NC}"
  fi
else
  echo -e "${RED}[FAIL] /usr/local/bin/quickman does not exist or is not executable.${NC}"
fi""",
        "lfcs_solution": """1. Documentation discovery:
```bash
apropos "partition table" > /var/tmp/lfcs-doc-search.txt
apropos "password file" >> /var/tmp/lfcs-doc-search.txt
man 5 passwd | col -b | head -n 30 > /var/tmp/lfcs-passwd-fields.txt
```

2. Directory navigation:
```bash
mkdir -p /var/tmp/lfcs/a/b/c/d/e
pushd /var/tmp/lfcs/a/b/c/d/e
touch evidence.txt
popd
```

3. Command synopsis extractor:
```bash
sudo tee /usr/local/bin/quickman << 'EOF'
#!/usr/bin/env bash
if [ -z "$1" ]; then
  echo "Usage: quickman <command>"
  exit 1
fi
man "$1" 2>/dev/null | col -b | sed -n '/^NAME/,/^[A-Z]/p' | head -n -1
man "$1" 2>/dev/null | col -b | sed -n '/^SYNOPSIS/,/^[A-Z]/p' | head -n -1
EOF
sudo chmod 755 /usr/local/bin/quickman
```""",
        "lfcs_reset": """sudo rm -rf /var/tmp/lfcs*
sudo rm -f /usr/local/bin/quickman""",
    },
    {
        "day": 2,
        "date": '2026-09-15',
        "title": 'Files, Directories, Hard & Soft Links',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Relative Symbolic Link Migration & Repair
1. The directory `/opt/link-lab/configs` contains a broken symbolic link `active.conf` pointing to a deleted absolute path.
2. The real configuration file has been relocated to `/opt/link-lab/storage/v2/app-v2.conf`.
3. Re-create the symlink `/opt/link-lab/configs/active.conf` pointing to `../storage/v2/app-v2.conf` using a **relative path** (not an absolute path starting with `/`).

### Task 2: Critical Config Hard Linking
1. Create a hard link from `/opt/link-lab/storage/v2/app-v2.conf` to `/opt/link-lab/backup/app-v2.conf.hl`.
2. Append the line `BACKUP_ENABLED=true` to `/opt/link-lab/backup/app-v2.conf.hl`.
3. Verify that the original `/opt/link-lab/storage/v2/app-v2.conf` also displays `BACKUP_ENABLED=true` and shares the exact same inode.

### Task 3: Clean Dangling Symlinks
1. In directory `/opt/link-lab/orphan_links/`, find and remove all broken (dangling) symbolic links.
2. Save the names of the removed links to `/var/tmp/removed_links.txt`.""",
        "setup": """sudo rm -rf /opt/link-lab /var/tmp/removed_links.txt
sudo mkdir -p /opt/link-lab/configs /opt/link-lab/storage/v2 /opt/link-lab/backup /opt/link-lab/orphan_links
sudo bash -c 'echo "DATABASE_PORT=5432" > /opt/link-lab/storage/v2/app-v2.conf'
sudo ln -sf /nonexistent/path/app.conf /opt/link-lab/configs/active.conf
sudo ln -sf /nonexistent/old_log.txt /opt/link-lab/orphan_links/broken1.link
sudo ln -sf /opt/link-lab/storage/v2/app-v2.conf /opt/link-lab/orphan_links/valid.link
sudo ln -sf /nonexistent/legacy.sock /opt/link-lab/orphan_links/broken2.link""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Relative symbolic link...${NC}"
LINK_TARGET=$(readlink /opt/link-lab/configs/active.conf 2>/dev/null || true)
if [ -L /opt/link-lab/configs/active.conf ] && [ "$LINK_TARGET" == "../storage/v2/app-v2.conf" ] && [ -f /opt/link-lab/configs/active.conf ]; then
  echo -e "${GREEN}[PASS] Relative symlink active.conf points correctly to ../storage/v2/app-v2.conf.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] active.conf target is '$LINK_TARGET' (expected relative path '../storage/v2/app-v2.conf').${NC}"
fi

echo -e "${BOLD}Checking Task 2: Hard link and inode synchronization...${NC}"
if [ -f /opt/link-lab/backup/app-v2.conf.hl ] && [ -f /opt/link-lab/storage/v2/app-v2.conf ]; then
  INODE1=$(stat -c '%i' /opt/link-lab/storage/v2/app-v2.conf 2>/dev/null || echo "1")
  INODE2=$(stat -c '%i' /opt/link-lab/backup/app-v2.conf.hl 2>/dev/null || echo "2")
  if [ "$INODE1" == "$INODE2" ] && grep -q "BACKUP_ENABLED=true" /opt/link-lab/storage/v2/app-v2.conf; then
    echo -e "${GREEN}[PASS] Hard link shares identical inode ($INODE1) and content updated.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Inodes differ ($INODE1 vs $INODE2) or BACKUP_ENABLED missing.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Hard link /opt/link-lab/backup/app-v2.conf.hl not found.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Dangling links removed...${NC}"
if [ -f /var/tmp/removed_links.txt ] && ! [ -L /opt/link-lab/orphan_links/broken1.link ] && [ -L /opt/link-lab/orphan_links/valid.link ]; then
  echo -e "${GREEN}[PASS] Dangling symlinks removed and recorded in /var/tmp/removed_links.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Broken links still present or /var/tmp/removed_links.txt missing.${NC}"
fi""",
        "solution": """1. Fix relative symlink:
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
```""",
        "reset": 'sudo rm -rf /opt/link-lab /var/tmp/removed_links.txt',
        "lfcs_title": 'Files, Directories, Hard & Soft Links',
        "lfcs_diff": 'Medium',
        "lfcs_time": '35m',
        "lfcs_tasks": """### Task 1: Relative Symbolic Link Migration & Repair
1. The directory `/opt/link-lab/configs` contains a broken symbolic link `active.conf` pointing to a deleted absolute path.
2. The real configuration file has been relocated to `/opt/link-lab/storage/v2/app-v2.conf`.
3. Re-create the symlink `/opt/link-lab/configs/active.conf` pointing to `../storage/v2/app-v2.conf` using a **relative path** (not an absolute path starting with `/`).

### Task 2: Critical Config Hard Linking
1. Create a hard link from `/opt/link-lab/storage/v2/app-v2.conf` to `/opt/link-lab/backup/app-v2.conf.hl`.
2. Append the line `BACKUP_ENABLED=true` to `/opt/link-lab/backup/app-v2.conf.hl`.
3. Verify that the original `/opt/link-lab/storage/v2/app-v2.conf` also displays `BACKUP_ENABLED=true` and shares the exact same inode.

### Task 3: Clean Dangling Symlinks
1. In directory `/opt/link-lab/orphan_links/`, find and remove all broken (dangling) symbolic links.
2. Save the names of the removed links to `/var/tmp/removed_links.txt`.""",
        "lfcs_setup": """sudo rm -rf /opt/link-lab /var/tmp/removed_links.txt
sudo mkdir -p /opt/link-lab/configs /opt/link-lab/storage/v2 /opt/link-lab/backup /opt/link-lab/orphan_links
sudo bash -c 'echo "DATABASE_PORT=5432" > /opt/link-lab/storage/v2/app-v2.conf'
sudo ln -sf /nonexistent/path/app.conf /opt/link-lab/configs/active.conf
sudo ln -sf /nonexistent/old_log.txt /opt/link-lab/orphan_links/broken1.link
sudo ln -sf /opt/link-lab/storage/v2/app-v2.conf /opt/link-lab/orphan_links/valid.link
sudo ln -sf /nonexistent/legacy.sock /opt/link-lab/orphan_links/broken2.link""",
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Relative symbolic link...${NC}"
LINK_TARGET=$(readlink /opt/link-lab/configs/active.conf 2>/dev/null || true)
if [ -L /opt/link-lab/configs/active.conf ] && [ "$LINK_TARGET" == "../storage/v2/app-v2.conf" ] && [ -f /opt/link-lab/configs/active.conf ]; then
  echo -e "${GREEN}[PASS] Relative symlink active.conf points correctly to ../storage/v2/app-v2.conf.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] active.conf target is '$LINK_TARGET' (expected relative path '../storage/v2/app-v2.conf').${NC}"
fi

echo -e "${BOLD}Checking Task 2: Hard link and inode synchronization...${NC}"
if [ -f /opt/link-lab/backup/app-v2.conf.hl ] && [ -f /opt/link-lab/storage/v2/app-v2.conf ]; then
  INODE1=$(stat -c '%i' /opt/link-lab/storage/v2/app-v2.conf 2>/dev/null || echo "1")
  INODE2=$(stat -c '%i' /opt/link-lab/backup/app-v2.conf.hl 2>/dev/null || echo "2")
  if [ "$INODE1" == "$INODE2" ] && grep -q "BACKUP_ENABLED=true" /opt/link-lab/storage/v2/app-v2.conf; then
    echo -e "${GREEN}[PASS] Hard link shares identical inode ($INODE1) and content updated.${NC}"
    SCORE=$((SCORE + 1))
  else
    echo -e "${RED}[FAIL] Inodes differ ($INODE1 vs $INODE2) or BACKUP_ENABLED missing.${NC}"
  fi
else
  echo -e "${RED}[FAIL] Hard link /opt/link-lab/backup/app-v2.conf.hl not found.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Dangling links removed...${NC}"
if [ -f /var/tmp/removed_links.txt ] && ! [ -L /opt/link-lab/orphan_links/broken1.link ] && [ -L /opt/link-lab/orphan_links/valid.link ]; then
  echo -e "${GREEN}[PASS] Dangling symlinks removed and recorded in /var/tmp/removed_links.txt.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Broken links still present or /var/tmp/removed_links.txt missing.${NC}"
fi""",
        "lfcs_solution": """1. Fix relative symlink:
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
```""",
        "lfcs_reset": 'sudo rm -rf /opt/link-lab /var/tmp/removed_links.txt',
    },
    {
        "day": 3,
        "date": '2026-09-16',
        "title": 'Standard Linux File Permissions',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Create Groups and Users
Ensure the following group and users exist:
1. Group: `devops_eng` (system assigned GID)
2. User `alice` belonging to primary group `devops_eng`.
3. User `bob` belonging to primary group `devops_eng`.

### Task 2: Selective Permission Enforcement
In directory `/srv/data/engineering`:
1. Change group ownership of `/srv/data/engineering` and all its contents recursively to `devops_eng`.
2. Enforce standard permissions:
   - All files must have permissions `664` (`-rw-rw-r--`).
   - All directories must have permissions `775` (`drwxrwxr-x`).

### Task 3: Enforce Default DevOps Umask
Create an environment script `/etc/profile.d/devops_umask.sh`:
- When users belonging to group `devops_eng` log in, set their default umask to `002`.""",
        "setup": """sudo rm -rf /srv/data/engineering /etc/profile.d/devops_umask.sh
sudo mkdir -p /srv/data/engineering/src /srv/data/engineering/docs
sudo touch /srv/data/engineering/README.md /srv/data/engineering/src/main.py /srv/data/engineering/docs/spec.txt
sudo chmod 777 /srv/data/engineering/README.md /srv/data/engineering/src/main.py
sudo chmod 700 /srv/data/engineering/src /srv/data/engineering/docs""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Users & group devops_eng...${NC}"
if getent group devops_eng >/dev/null && id alice >/dev/null && id bob >/dev/null; then
  echo -e "${GREEN}[PASS] Users alice, bob and group devops_eng verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Group devops_eng or users alice/bob missing.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Directory permissions 775 / 664...${NC}"
PERM_DIR=$(stat -c '%a' /srv/data/engineering/src 2>/dev/null || echo "0")
PERM_FILE=$(stat -c '%a' /srv/data/engineering/README.md 2>/dev/null || echo "0")
GRP=$(stat -c '%G' /srv/data/engineering/README.md 2>/dev/null || echo "none")

if [ "$PERM_DIR" == "775" ] && [ "$PERM_FILE" == "664" ] && [ "$GRP" == "devops_eng" ]; then
  echo -e "${GREEN}[PASS] Recursive group devops_eng, dirs 775, files 664 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Permissions mismatch: dir=$PERM_DIR (expected 775), file=$PERM_FILE (expected 664), group=$GRP.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /etc/profile.d/devops_umask.sh...${NC}"
if [ -f /etc/profile.d/devops_umask.sh ] && grep -q "002" /etc/profile.d/devops_umask.sh; then
  echo -e "${GREEN}[PASS] /etc/profile.d/devops_umask.sh configured with umask 002.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /etc/profile.d/devops_umask.sh missing or lacks umask 002.${NC}"
fi""",
        "solution": """1. Create group and users:
```bash
sudo groupadd -f devops_eng
sudo id alice &>/dev/null || sudo useradd -g devops_eng -m alice
sudo id bob &>/dev/null || sudo useradd -g devops_eng -m bob
```

2. Enforce recursive permissions:
```bash
sudo chgrp -R devops_eng /srv/data/engineering
sudo find /srv/data/engineering -type d -exec chmod 775 {} +
sudo find /srv/data/engineering -type f -exec chmod 664 {} +
```

3. Configure umask profile script:
```bash
sudo tee /etc/profile.d/devops_umask.sh << 'EOF'
if id -nG | grep -qw "devops_eng"; then
  umask 002
fi
EOF
sudo chmod 644 /etc/profile.d/devops_umask.sh
```""",
        "reset": """sudo rm -rf /srv/data/engineering /etc/profile.d/devops_umask.sh
sudo userdel -r alice 2>/dev/null || true
sudo userdel -r bob 2>/dev/null || true
sudo groupdel devops_eng 2>/dev/null || true""",
        "lfcs_title": 'Standard Linux File Permissions',
        "lfcs_diff": 'Medium',
        "lfcs_time": '35m',
        "lfcs_tasks": """### Task 1: Create Groups and Users
Ensure the following group and users exist:
1. Group: `devops_eng` (system assigned GID)
2. User `alice` belonging to primary group `devops_eng`.
3. User `bob` belonging to primary group `devops_eng`.

### Task 2: Selective Permission Enforcement
In directory `/srv/data/engineering`:
1. Change group ownership of `/srv/data/engineering` and all its contents recursively to `devops_eng`.
2. Enforce standard permissions:
   - All files must have permissions `664` (`-rw-rw-r--`).
   - All directories must have permissions `775` (`drwxrwxr-x`).

### Task 3: Enforce Default DevOps Umask
Create an environment script `/etc/profile.d/devops_umask.sh`:
- When users belonging to group `devops_eng` log in, set their default umask to `002`.""",
        "lfcs_setup": """sudo rm -rf /srv/data/engineering /etc/profile.d/devops_umask.sh
sudo mkdir -p /srv/data/engineering/src /srv/data/engineering/docs
sudo touch /srv/data/engineering/README.md /srv/data/engineering/src/main.py /srv/data/engineering/docs/spec.txt
sudo chmod 777 /srv/data/engineering/README.md /srv/data/engineering/src/main.py
sudo chmod 700 /srv/data/engineering/src /srv/data/engineering/docs""",
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: Users & group devops_eng...${NC}"
if getent group devops_eng >/dev/null && id alice >/dev/null && id bob >/dev/null; then
  echo -e "${GREEN}[PASS] Users alice, bob and group devops_eng verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Group devops_eng or users alice/bob missing.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Directory permissions 775 / 664...${NC}"
PERM_DIR=$(stat -c '%a' /srv/data/engineering/src 2>/dev/null || echo "0")
PERM_FILE=$(stat -c '%a' /srv/data/engineering/README.md 2>/dev/null || echo "0")
GRP=$(stat -c '%G' /srv/data/engineering/README.md 2>/dev/null || echo "none")

if [ "$PERM_DIR" == "775" ] && [ "$PERM_FILE" == "664" ] && [ "$GRP" == "devops_eng" ]; then
  echo -e "${GREEN}[PASS] Recursive group devops_eng, dirs 775, files 664 verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Permissions mismatch: dir=$PERM_DIR (expected 775), file=$PERM_FILE (expected 664), group=$GRP.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /etc/profile.d/devops_umask.sh...${NC}"
if [ -f /etc/profile.d/devops_umask.sh ] && grep -q "002" /etc/profile.d/devops_umask.sh; then
  echo -e "${GREEN}[PASS] /etc/profile.d/devops_umask.sh configured with umask 002.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /etc/profile.d/devops_umask.sh missing or lacks umask 002.${NC}"
fi""",
        "lfcs_solution": """1. Create group and users:
```bash
sudo groupadd -f devops_eng
sudo id alice &>/dev/null || sudo useradd -g devops_eng -m alice
sudo id bob &>/dev/null || sudo useradd -g devops_eng -m bob
```

2. Enforce recursive permissions:
```bash
sudo chgrp -R devops_eng /srv/data/engineering
sudo find /srv/data/engineering -type d -exec chmod 775 {} +
sudo find /srv/data/engineering -type f -exec chmod 664 {} +
```

3. Configure umask profile script:
```bash
sudo tee /etc/profile.d/devops_umask.sh << 'EOF'
if id -nG | grep -qw "devops_eng"; then
  umask 002
fi
EOF
sudo chmod 644 /etc/profile.d/devops_umask.sh
```""",
        "lfcs_reset": """sudo rm -rf /srv/data/engineering /etc/profile.d/devops_umask.sh
sudo userdel -r alice 2>/dev/null || true
sudo userdel -r bob 2>/dev/null || true
sudo groupdel devops_eng 2>/dev/null || true""",
    },
    {
        "day": 4,
        "date": '2026-09-17',
        "title": 'Special Permissions: SUID, SGID & Sticky Bit',
        "diff": 'Medium',
        "time": '35m',
        "tasks": """### Task 1: Collaborative Shared Directory with SGID
1. Create a group named `marketing`.
2. Create directory `/opt/campaigns`.
3. Set ownership of `/opt/campaigns` to user `root` and group `marketing`.
4. Enforce permissions such that:
   - Group members have full read, write, and execute permissions (`rwx`).
   - Others have zero permissions (`---`).
   - Any new file or directory created inside automatically inherits the group `marketing` (SetGID bit).

### Task 2: Secure Public Drop Directory with Sticky Bit
1. Inside `/opt/campaigns`, create a directory `incoming`.
2. Configure permissions on `/opt/campaigns/incoming` with the Sticky bit (`1777` or `1770`):
   - Only the file owner or root can delete or rename files inside `incoming`.

### Task 3: World-Writable File Security Audit
1. Search `/var/log` for any world-writable files (`-perm -002`).
2. Save the list of matched paths to `/var/tmp/world_writable_audit.txt`.""",
        "setup": """sudo rm -rf /opt/campaigns /var/tmp/world_writable_audit.txt
sudo groupdel marketing 2>/dev/null || true""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: SGID directory /opt/campaigns...${NC}"
PERM_C=$(sudo stat -c '%a' /opt/campaigns 2>/dev/null || echo "0")
GRP_C=$(sudo stat -c '%G' /opt/campaigns 2>/dev/null || echo "none")

# Check if group inheritance works
sudo -u root touch /opt/campaigns/test_file 2>/dev/null || true
TEST_GRP=$(sudo stat -c '%G' /opt/campaigns/test_file 2>/dev/null || echo "none")
sudo rm -f /opt/campaigns/test_file

if [ "$GRP_C" == "marketing" ] && [ "$TEST_GRP" == "marketing" ] && [[ "$PERM_C" =~ ^2 ]]; then
  echo -e "${GREEN}[PASS] /opt/campaigns has SGID bit (perm $PERM_C) and group marketing.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/campaigns perm=$PERM_C, group=$GRP_C, test_grp=$TEST_GRP.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Sticky bit directory /opt/campaigns/incoming...${NC}"
PERM_INC=$(sudo stat -c '%a' /opt/campaigns/incoming 2>/dev/null || echo "0")
if [[ "$PERM_INC" =~ ^1 ]]; then
  echo -e "${GREEN}[PASS] /opt/campaigns/incoming has Sticky bit set (perm $PERM_INC).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/campaigns/incoming lacks Sticky bit (perm $PERM_INC).${NC}"
fi

echo -e "${BOLD}Checking Task 3: World writable audit...${NC}"
if [ -f /var/tmp/world_writable_audit.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/world_writable_audit.txt created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/world_writable_audit.txt missing.${NC}"
fi""",
        "solution": """1. Create group and configure SGID directory:
```bash
sudo groupadd -f marketing
sudo mkdir -p /opt/campaigns
sudo chown root:marketing /opt/campaigns
sudo chmod 2770 /opt/campaigns
```

2. Configure Sticky bit directory:
```bash
sudo mkdir -p /opt/campaigns/incoming
sudo chown root:marketing /opt/campaigns/incoming
sudo chmod 1770 /opt/campaigns/incoming
```

3. World-writable audit:
```bash
sudo find /var/log -type f -perm -002 > /var/tmp/world_writable_audit.txt
```""",
        "reset": """sudo rm -rf /opt/campaigns /var/tmp/world_writable_audit.txt
sudo groupdel marketing 2>/dev/null || true""",
        "lfcs_title": 'Special Permissions: SUID, SGID & Sticky Bit',
        "lfcs_diff": 'Medium',
        "lfcs_time": '35m',
        "lfcs_tasks": """### Task 1: Collaborative Shared Directory with SGID
1. Create a group named `marketing`.
2. Create directory `/opt/campaigns`.
3. Set ownership of `/opt/campaigns` to user `root` and group `marketing`.
4. Enforce permissions such that:
   - Group members have full read, write, and execute permissions (`rwx`).
   - Others have zero permissions (`---`).
   - Any new file or directory created inside automatically inherits the group `marketing` (SetGID bit).

### Task 2: Secure Public Drop Directory with Sticky Bit
1. Inside `/opt/campaigns`, create a directory `incoming`.
2. Configure permissions on `/opt/campaigns/incoming` with the Sticky bit (`1777` or `1770`):
   - Only the file owner or root can delete or rename files inside `incoming`.

### Task 3: World-Writable File Security Audit
1. Search `/var/log` for any world-writable files (`-perm -002`).
2. Save the list of matched paths to `/var/tmp/world_writable_audit.txt`.""",
        "lfcs_setup": """sudo rm -rf /opt/campaigns /var/tmp/world_writable_audit.txt
sudo groupdel marketing 2>/dev/null || true""",
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: SGID directory /opt/campaigns...${NC}"
PERM_C=$(sudo stat -c '%a' /opt/campaigns 2>/dev/null || echo "0")
GRP_C=$(sudo stat -c '%G' /opt/campaigns 2>/dev/null || echo "none")

# Check if group inheritance works
sudo -u root touch /opt/campaigns/test_file 2>/dev/null || true
TEST_GRP=$(sudo stat -c '%G' /opt/campaigns/test_file 2>/dev/null || echo "none")
sudo rm -f /opt/campaigns/test_file

if [ "$GRP_C" == "marketing" ] && [ "$TEST_GRP" == "marketing" ] && [[ "$PERM_C" =~ ^2 ]]; then
  echo -e "${GREEN}[PASS] /opt/campaigns has SGID bit (perm $PERM_C) and group marketing.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/campaigns perm=$PERM_C, group=$GRP_C, test_grp=$TEST_GRP.${NC}"
fi

echo -e "${BOLD}Checking Task 2: Sticky bit directory /opt/campaigns/incoming...${NC}"
PERM_INC=$(sudo stat -c '%a' /opt/campaigns/incoming 2>/dev/null || echo "0")
if [[ "$PERM_INC" =~ ^1 ]]; then
  echo -e "${GREEN}[PASS] /opt/campaigns/incoming has Sticky bit set (perm $PERM_INC).${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /opt/campaigns/incoming lacks Sticky bit (perm $PERM_INC).${NC}"
fi

echo -e "${BOLD}Checking Task 3: World writable audit...${NC}"
if [ -f /var/tmp/world_writable_audit.txt ]; then
  echo -e "${GREEN}[PASS] /var/tmp/world_writable_audit.txt created.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/world_writable_audit.txt missing.${NC}"
fi""",
        "lfcs_solution": """1. Create group and configure SGID directory:
```bash
sudo groupadd -f marketing
sudo mkdir -p /opt/campaigns
sudo chown root:marketing /opt/campaigns
sudo chmod 2770 /opt/campaigns
```

2. Configure Sticky bit directory:
```bash
sudo mkdir -p /opt/campaigns/incoming
sudo chown root:marketing /opt/campaigns/incoming
sudo chmod 1770 /opt/campaigns/incoming
```

3. World-writable audit:
```bash
sudo find /var/log -type f -perm -002 > /var/tmp/world_writable_audit.txt
```""",
        "lfcs_reset": """sudo rm -rf /opt/campaigns /var/tmp/world_writable_audit.txt
sudo groupdel marketing 2>/dev/null || true""",
    },
    {
        "day": 5,
        "date": '2026-09-18',
        "title": 'Pagers, Vim Mastery & Terminal Editing',
        "diff": 'Medium',
        "time": '25m',
        "tasks": """### Task 1: Engineer Vim Profile Configuration
Configure your user's `~/.vimrc` with:
- Line numbering (`set number`)
- Syntax highlighting (`syntax on`)
- 4-space indentation (`set tabstop=4`, `set shiftwidth=4`, `set expandtab`)
- Incremental search highlighting (`set hlsearch`, `set incsearch`)

### Task 2: In-place Refactoring of Legacy Configuration
A configuration file `/var/tmp/app_legacy.conf` requires updating:
1. Replace all occurrences of `PORT = 8080` with `PORT = 8443`.
2. Uncomment the line `# SSL_ENABLED = true` to `SSL_ENABLED = true`.
3. Delete all lines containing `DEPRECATED`.

### Task 3: Text Pipeline Analysis
Analyze `/var/tmp/sample_audit.log`:
1. Extract all unique status code fields (`STATUS: <CODE>`).
2. Count occurrences of each status and output the sorted counts to `/var/tmp/status_summary.txt`.""",
        "setup": """cat << 'EOF' > /var/tmp/app_legacy.conf
[server]
HOST = 0.0.0.0
PORT = 8080
# SSL_ENABLED = true
DEPRECATED_FEATURE_A = enabled
TIMEOUT = 300
DEPRECATED_FEATURE_B = active
EOF

cat << 'EOF' > /var/tmp/sample_audit.log
2026-09-14 10:00:01 [AUTH] STATUS: 200 user=alice
2026-09-14 10:00:02 [AUTH] STATUS: 401 user=guest
2026-09-14 10:00:03 [AUTH] STATUS: 200 user=bob
2026-09-14 10:00:04 [AUTH] STATUS: 500 user=alice
2026-09-14 10:00:05 [AUTH] STATUS: 200 user=admin
EOF
rm -f /var/tmp/status_summary.txt""",
        "verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: ~/.vimrc configuration...${NC}"
if [ -f ~/.vimrc ] && grep -q "tabstop=4" ~/.vimrc && grep -q "number" ~/.vimrc; then
  echo -e "${GREEN}[PASS] ~/.vimrc verified with tabstop=4 and line numbering.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] ~/.vimrc missing or lacks required settings.${NC}"
fi

echo -e "${BOLD}Checking Task 2: /var/tmp/app_legacy.conf refactoring...${NC}"
CONF=$(cat /var/tmp/app_legacy.conf 2>/dev/null || true)
if echo "$CONF" | grep -q "PORT = 8443" && echo "$CONF" | grep -q "^SSL_ENABLED = true" && ! echo "$CONF" | grep -q "DEPRECATED"; then
  echo -e "${GREEN}[PASS] /var/tmp/app_legacy.conf refactored correctly.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Configuration transformations incomplete.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/status_summary.txt...${NC}"
if [ -f /var/tmp/status_summary.txt ] && grep -q "200" /var/tmp/status_summary.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/status_summary.txt created with status counts.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/status_summary.txt missing or empty.${NC}"
fi""",
        "solution": """1. Setup `~/.vimrc`:
```bash
cat << 'EOF' >> ~/.vimrc
set number
syntax on
set tabstop=4
set shiftwidth=4
set expandtab
set hlsearch
set incsearch
EOF
```

2. Refactor configuration:
```bash
sed -i 's/PORT = 8080/PORT = 8443/' /var/tmp/app_legacy.conf
sed -i 's/^# SSL_ENABLED = true/SSL_ENABLED = true/' /var/tmp/app_legacy.conf
sed -i '/DEPRECATED/d' /var/tmp/app_legacy.conf
```

3. Pipeline extraction:
```bash
grep -oE "STATUS: [0-9]+" /var/tmp/sample_audit.log | sort | uniq -c > /var/tmp/status_summary.txt
```""",
        "reset": 'rm -f /var/tmp/app_legacy.conf /var/tmp/sample_audit.log /var/tmp/status_summary.txt',
        "lfcs_title": 'Pagers, Vim Mastery & Terminal Editing',
        "lfcs_diff": 'Medium',
        "lfcs_time": '25m',
        "lfcs_tasks": """### Task 1: Engineer Vim Profile Configuration
Configure your user's `~/.vimrc` with:
- Line numbering (`set number`)
- Syntax highlighting (`syntax on`)
- 4-space indentation (`set tabstop=4`, `set shiftwidth=4`, `set expandtab`)
- Incremental search highlighting (`set hlsearch`, `set incsearch`)

### Task 2: In-place Refactoring of Legacy Configuration
A configuration file `/var/tmp/app_legacy.conf` requires updating:
1. Replace all occurrences of `PORT = 8080` with `PORT = 8443`.
2. Uncomment the line `# SSL_ENABLED = true` to `SSL_ENABLED = true`.
3. Delete all lines containing `DEPRECATED`.

### Task 3: Text Pipeline Analysis
Analyze `/var/tmp/sample_audit.log`:
1. Extract all unique status code fields (`STATUS: <CODE>`).
2. Count occurrences of each status and output the sorted counts to `/var/tmp/status_summary.txt`.""",
        "lfcs_setup": """cat << 'EOF' > /var/tmp/app_legacy.conf
[server]
HOST = 0.0.0.0
PORT = 8080
# SSL_ENABLED = true
DEPRECATED_FEATURE_A = enabled
TIMEOUT = 300
DEPRECATED_FEATURE_B = active
EOF

cat << 'EOF' > /var/tmp/sample_audit.log
2026-09-14 10:00:01 [AUTH] STATUS: 200 user=alice
2026-09-14 10:00:02 [AUTH] STATUS: 401 user=guest
2026-09-14 10:00:03 [AUTH] STATUS: 200 user=bob
2026-09-14 10:00:04 [AUTH] STATUS: 500 user=alice
2026-09-14 10:00:05 [AUTH] STATUS: 200 user=admin
EOF
rm -f /var/tmp/status_summary.txt""",
        "lfcs_verify": """SCORE=0; TOTAL=3

echo -e "${BOLD}Checking Task 1: ~/.vimrc configuration...${NC}"
if [ -f ~/.vimrc ] && grep -q "tabstop=4" ~/.vimrc && grep -q "number" ~/.vimrc; then
  echo -e "${GREEN}[PASS] ~/.vimrc verified with tabstop=4 and line numbering.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] ~/.vimrc missing or lacks required settings.${NC}"
fi

echo -e "${BOLD}Checking Task 2: /var/tmp/app_legacy.conf refactoring...${NC}"
CONF=$(cat /var/tmp/app_legacy.conf 2>/dev/null || true)
if echo "$CONF" | grep -q "PORT = 8443" && echo "$CONF" | grep -q "^SSL_ENABLED = true" && ! echo "$CONF" | grep -q "DEPRECATED"; then
  echo -e "${GREEN}[PASS] /var/tmp/app_legacy.conf refactored correctly.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Configuration transformations incomplete.${NC}"
fi

echo -e "${BOLD}Checking Task 3: /var/tmp/status_summary.txt...${NC}"
if [ -f /var/tmp/status_summary.txt ] && grep -q "200" /var/tmp/status_summary.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/status_summary.txt created with status counts.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/status_summary.txt missing or empty.${NC}"
fi""",
        "lfcs_solution": """1. Setup `~/.vimrc`:
```bash
cat << 'EOF' >> ~/.vimrc
set number
syntax on
set tabstop=4
set shiftwidth=4
set expandtab
set hlsearch
set incsearch
EOF
```

2. Refactor configuration:
```bash
sed -i 's/PORT = 8080/PORT = 8443/' /var/tmp/app_legacy.conf
sed -i 's/^# SSL_ENABLED = true/SSL_ENABLED = true/' /var/tmp/app_legacy.conf
sed -i '/DEPRECATED/d' /var/tmp/app_legacy.conf
```

3. Pipeline extraction:
```bash
grep -oE "STATUS: [0-9]+" /var/tmp/sample_audit.log | sort | uniq -c > /var/tmp/status_summary.txt
```""",
        "lfcs_reset": 'rm -f /var/tmp/app_legacy.conf /var/tmp/sample_audit.log /var/tmp/status_summary.txt',
    },
    {
        "day": 6,
        "date": '2026-09-19',
        "title": 'Week 1 Consolidation & Permission Security Triathlon',
        "diff": 'Hard (Milestone Assessment 1)',
        "time": '45m',
        "tasks": """### Milestone 1 Triathlon Tasks:
1. **Collaborative Secure Tree:**
   Create groups `sysadmins` and `contractors`.
   Create directory `/srv/secure_vault` owned by `root:sysadmins` with permissions `2770` (SGID).
   Inside, create `/srv/secure_vault/incoming` owned by `root:contractors` with permissions `1775` (Sticky bit).
2. **SUID / SGID Audit:**
   Locate all SUID and SGID executables under `/opt/binaries` and save their full paths to `/var/tmp/suid_audit.txt`.
3. **Relative Symbolic Link:**
   In `/srv/secure_vault/configs`, create a relative symlink `current.conf` pointing to `../storage/vault.conf`.
4. **Archive & Backup:**
   Create a gzip-compressed archive `/var/backups/vault_initial.tar.gz` of `/srv/secure_vault` preserving file permissions (`-p`).""",
        "setup": """sudo rm -rf /srv/secure_vault /var/tmp/suid_audit.txt /var/backups/vault_initial.tar.gz /opt/binaries
sudo mkdir -p /opt/binaries /var/backups
sudo touch /opt/binaries/tool_suid /opt/binaries/tool_normal
sudo chmod 4755 /opt/binaries/tool_suid
sudo chmod 755 /opt/binaries/tool_normal
sudo groupdel sysadmins 2>/dev/null || true
sudo groupdel contractors 2>/dev/null || true""",
        "verify": """SCORE=0; TOTAL=4

echo -e "${BOLD}Checking Task 1: Secure vault directories...${NC}"
PERM_V=$(sudo stat -c '%a' /srv/secure_vault 2>/dev/null || echo "0")
PERM_I=$(sudo stat -c '%a' /srv/secure_vault/incoming 2>/dev/null || echo "0")
GRP_V=$(sudo stat -c '%G' /srv/secure_vault 2>/dev/null || echo "none")

if [ "$GRP_V" == "sysadmins" ] && [[ "$PERM_V" =~ ^2 ]] && [[ "$PERM_I" =~ ^1 ]]; then
  echo -e "${GREEN}[PASS] /srv/secure_vault (SGID, sysadmins) and /incoming (Sticky) verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Vault permissions incorrect: vault=$PERM_V, group=$GRP_V, incoming=$PERM_I.${NC}"
fi

echo -e "${BOLD}Checking Task 2: SUID audit...${NC}"
if [ -f /var/tmp/suid_audit.txt ] && grep -q "tool_suid" /var/tmp/suid_audit.txt && ! grep -q "tool_normal" /var/tmp/suid_audit.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/suid_audit.txt correctly identified SUID binary.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/suid_audit.txt missing or incorrect.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Relative symlink...${NC}"
LINK=$(sudo readlink /srv/secure_vault/configs/current.conf 2>/dev/null || true)
if [ "$LINK" == "../storage/vault.conf" ]; then
  echo -e "${GREEN}[PASS] Relative symlink current.conf points to ../storage/vault.conf.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Relative symlink missing or invalid: '$LINK'.${NC}"
fi

echo -e "${BOLD}Checking Task 4: Tar backup...${NC}"
if [ -f /var/backups/vault_initial.tar.gz ] && tar -tzf /var/backups/vault_initial.tar.gz &>/dev/null; then
  echo -e "${GREEN}[PASS] /var/backups/vault_initial.tar.gz exists and is a valid tar.gz archive.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/backups/vault_initial.tar.gz missing or invalid archive.${NC}"
fi""",
        "solution": """1. Directory permissions:
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
```""",
        "reset": """sudo rm -rf /srv/secure_vault /var/tmp/suid_audit.txt /var/backups/vault_initial.tar.gz /opt/binaries
sudo groupdel sysadmins 2>/dev/null || true
sudo groupdel contractors 2>/dev/null || true""",
        "lfcs_title": 'Week 1 Consolidation & Permission Security Triathlon',
        "lfcs_diff": 'Hard (Milestone Assessment 1)',
        "lfcs_time": '45m',
        "lfcs_tasks": """### Milestone 1 Triathlon Tasks:
1. **Collaborative Secure Tree:**
   Create groups `sysadmins` and `contractors`.
   Create directory `/srv/secure_vault` owned by `root:sysadmins` with permissions `2770` (SGID).
   Inside, create `/srv/secure_vault/incoming` owned by `root:contractors` with permissions `1775` (Sticky bit).
2. **SUID / SGID Audit:**
   Locate all SUID and SGID executables under `/opt/binaries` and save their full paths to `/var/tmp/suid_audit.txt`.
3. **Relative Symbolic Link:**
   In `/srv/secure_vault/configs`, create a relative symlink `current.conf` pointing to `../storage/vault.conf`.
4. **Archive & Backup:**
   Create a gzip-compressed archive `/var/backups/vault_initial.tar.gz` of `/srv/secure_vault` preserving file permissions (`-p`).""",
        "lfcs_setup": """sudo rm -rf /srv/secure_vault /var/tmp/suid_audit.txt /var/backups/vault_initial.tar.gz /opt/binaries
sudo mkdir -p /opt/binaries /var/backups
sudo touch /opt/binaries/tool_suid /opt/binaries/tool_normal
sudo chmod 4755 /opt/binaries/tool_suid
sudo chmod 755 /opt/binaries/tool_normal
sudo groupdel sysadmins 2>/dev/null || true
sudo groupdel contractors 2>/dev/null || true""",
        "lfcs_verify": """SCORE=0; TOTAL=4

echo -e "${BOLD}Checking Task 1: Secure vault directories...${NC}"
PERM_V=$(sudo stat -c '%a' /srv/secure_vault 2>/dev/null || echo "0")
PERM_I=$(sudo stat -c '%a' /srv/secure_vault/incoming 2>/dev/null || echo "0")
GRP_V=$(sudo stat -c '%G' /srv/secure_vault 2>/dev/null || echo "none")

if [ "$GRP_V" == "sysadmins" ] && [[ "$PERM_V" =~ ^2 ]] && [[ "$PERM_I" =~ ^1 ]]; then
  echo -e "${GREEN}[PASS] /srv/secure_vault (SGID, sysadmins) and /incoming (Sticky) verified.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Vault permissions incorrect: vault=$PERM_V, group=$GRP_V, incoming=$PERM_I.${NC}"
fi

echo -e "${BOLD}Checking Task 2: SUID audit...${NC}"
if [ -f /var/tmp/suid_audit.txt ] && grep -q "tool_suid" /var/tmp/suid_audit.txt && ! grep -q "tool_normal" /var/tmp/suid_audit.txt; then
  echo -e "${GREEN}[PASS] /var/tmp/suid_audit.txt correctly identified SUID binary.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/tmp/suid_audit.txt missing or incorrect.${NC}"
fi

echo -e "${BOLD}Checking Task 3: Relative symlink...${NC}"
LINK=$(sudo readlink /srv/secure_vault/configs/current.conf 2>/dev/null || true)
if [ "$LINK" == "../storage/vault.conf" ]; then
  echo -e "${GREEN}[PASS] Relative symlink current.conf points to ../storage/vault.conf.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] Relative symlink missing or invalid: '$LINK'.${NC}"
fi

echo -e "${BOLD}Checking Task 4: Tar backup...${NC}"
if [ -f /var/backups/vault_initial.tar.gz ] && tar -tzf /var/backups/vault_initial.tar.gz &>/dev/null; then
  echo -e "${GREEN}[PASS] /var/backups/vault_initial.tar.gz exists and is a valid tar.gz archive.${NC}"
  SCORE=$((SCORE + 1))
else
  echo -e "${RED}[FAIL] /var/backups/vault_initial.tar.gz missing or invalid archive.${NC}"
fi""",
        "lfcs_solution": """1. Directory permissions:
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
```""",
        "lfcs_reset": """sudo rm -rf /srv/secure_vault /var/tmp/suid_audit.txt /var/backups/vault_initial.tar.gz /opt/binaries
sudo groupdel sysadmins 2>/dev/null || true
sudo groupdel contractors 2>/dev/null || true""",
    },
]
