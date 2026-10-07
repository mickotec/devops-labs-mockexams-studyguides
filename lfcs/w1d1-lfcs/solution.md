# [LFCS W1D1-LFCS] Solution Walkthrough: Consoles, Navigation & System Documentation

1. Documentation discovery:
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
```
