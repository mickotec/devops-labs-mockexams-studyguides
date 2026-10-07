# [LFCS W1D5-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Setup `~/.vimrc`:
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
```
